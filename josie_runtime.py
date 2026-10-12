#!/usr/bin/env python3
"""Reliable local-first runtime for the JOSIE command line."""
from __future__ import annotations

import argparse
import json
import os
import pty
import re
import shlex
import shutil
import sqlite3
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

HOME = Path.home()
DB_PATH = Path(os.environ.get("JOSIE_DB", str(HOME / "hummie/core/josie_memory.db")))
CONFIG_FILE = Path(os.environ.get("JOSIE_CONFIG", str(HOME / ".config/josie-connected-apps/config.env")))
STATE_FILE = Path(os.environ.get("JOSIE_PROVIDER_STATE", str(HOME / ".cache/josie/provider-state.json")))
LOCAL_CHAT = os.environ.get("JOSIE_LOCAL_CHAT", "http://127.0.0.1:8080/chat")
OLLAMA_CHAT = os.environ.get("OLLAMA_CHAT_URL", "http://127.0.0.1:11434/api/chat")
DEFAULT_ORDER = "local,ollama,openrouter,pollinations"


class ProviderError(RuntimeError):
    def __init__(self, message: str, retry_after: int = 0):
        super().__init__(message)
        self.retry_after = retry_after


def load_env_file(path: Path = CONFIG_FILE) -> None:
    """Load simple KEY=VALUE entries without executing the file as shell code."""
    if not path.is_file():
        return
    for raw in path.read_text(errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key) or key in os.environ:
            continue
        try:
            parsed = shlex.split(value, comments=True)
            os.environ[key] = parsed[0] if parsed else ""
        except ValueError:
            continue


def request(url: str, payload: dict | None = None, headers: dict | None = None, timeout: int = 20) -> bytes:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    merged = {"User-Agent": "JOSIE/3.0", **(headers or {})}
    if data is not None:
        merged.setdefault("Content-Type", "application/json")
    req = urllib.request.Request(url, data=data, headers=merged)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        retry = exc.headers.get("Retry-After", "0")
        try:
            retry_after = max(0, int(float(retry)))
        except ValueError:
            retry_after = 0
        raise ProviderError(f"HTTP {exc.code}", retry_after) from exc
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise ProviderError(str(exc)) from exc


def json_request(url: str, payload: dict, headers: dict | None = None, timeout: int = 20) -> dict:
    try:
        value = json.loads(request(url, payload, headers, timeout).decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ProviderError("provider returned invalid JSON") from exc
    if not isinstance(value, dict):
        raise ProviderError("provider returned an unexpected response")
    return value


def _read_state() -> dict:
    try:
        value = json.loads(STATE_FILE.read_text())
        return value if isinstance(value, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def _write_state(value: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(value, indent=2, sort_keys=True))
    STATE_FILE.chmod(0o600)


def circuit_open(name: str) -> int:
    item = _read_state().get(name, {})
    return max(0, int(item.get("open_until", 0) - time.time()))


def record_success(name: str) -> None:
    state = _read_state()
    state[name] = {"failures": 0, "open_until": 0, "last_error": ""}
    _write_state(state)


def record_failure(name: str, error: Exception) -> None:
    state = _read_state()
    old = state.get(name, {})
    failures = int(old.get("failures", 0)) + 1
    requested = int(getattr(error, "retry_after", 0) or 0)
    cooldown = requested or min(300, 2 ** min(failures, 8))
    state[name] = {
        "failures": failures,
        "open_until": int(time.time() + cooldown),
        "last_error": str(error)[:160],
    }
    _write_state(state)


def local_provider(prompt: str, model: str) -> str:
    data = json_request(LOCAL_CHAT, {"prompt": prompt, "model": model}, timeout=25)
    reply = data.get("reply")
    if not isinstance(reply, str) or not reply.strip():
        raise ProviderError("local cockpit returned no reply")
    return reply.strip()


def ollama_provider(prompt: str, model: str) -> str:
    ollama_model = os.environ.get("OLLAMA_MODEL", "qwen2.5:3b")
    data = json_request(OLLAMA_CHAT, {
        "model": ollama_model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
    }, timeout=60)
    reply = data.get("message", {}).get("content")
    if not isinstance(reply, str) or not reply.strip():
        raise ProviderError("Ollama returned no reply")
    return reply.strip()


def openrouter_provider(prompt: str, model: str) -> str:
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not key:
        key_file = HOME / ".openrouter_key"
        key = key_file.read_text().strip() if key_file.is_file() else ""
    if not key:
        raise ProviderError("OPENROUTER_API_KEY is not configured")
    selected = model or os.environ.get("JOSIE_MODEL", "openrouter/auto")
    data = json_request(
        "https://openrouter.ai/api/v1/chat/completions",
        {"model": selected, "messages": [{"role": "user", "content": prompt}]},
        {"Authorization": f"Bearer {key}", "X-Title": "JOSIE"},
        timeout=45,
    )
    try:
        reply = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise ProviderError("OpenRouter returned no reply") from exc
    if not isinstance(reply, str) or not reply.strip():
        raise ProviderError("OpenRouter returned no reply")
    return reply.strip()


def pollinations_provider(prompt: str, model: str) -> str:
    if os.environ.get("JOSIE_ENABLE_POLLINATIONS", "1").lower() not in {"1", "true", "yes"}:
        raise ProviderError("Pollinations fallback is disabled")
    clean = urllib.parse.quote(prompt[:1200], safe="")
    text = request(f"https://text.pollinations.ai/{clean}", timeout=25).decode("utf-8", "replace").strip()
    if not text:
        raise ProviderError("Pollinations returned no reply")
    return text


PROVIDERS: dict[str, Callable[[str, str], str]] = {
    "local": local_provider,
    "ollama": ollama_provider,
    "openrouter": openrouter_provider,
    "pollinations": pollinations_provider,
}


def ask(prompt: str, model: str = "") -> tuple[str, str]:
    order = [x.strip() for x in os.environ.get("JOSIE_PROVIDER_ORDER", DEFAULT_ORDER).split(",") if x.strip()]
    failures: list[str] = []
    for name in order:
        provider = PROVIDERS.get(name)
        if provider is None:
            failures.append(f"{name}: unknown provider")
            continue
        remaining = circuit_open(name)
        if remaining:
            failures.append(f"{name}: cooling down for {remaining}s")
            continue
        try:
            reply = provider(prompt, model)
            record_success(name)
            return reply, name
        except Exception as exc:
            record_failure(name, exc)
            failures.append(f"{name}: {exc}")
    detail = "; ".join(failures) or "no providers enabled"
    raise ProviderError(f"No provider completed the request ({detail})")


def connector_status() -> dict[str, bool]:
    def has(command: str) -> bool:
        return shutil.which(command) is not None

    def run_ok(argv: list[str]) -> bool:
        try:
            return subprocess.run(argv, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=8).returncode == 0
        except (OSError, subprocess.TimeoutExpired):
            return False

    remotes = ""
    if has("rclone"):
        try:
            remotes = subprocess.run(["rclone", "listremotes"], capture_output=True, text=True, timeout=8).stdout
        except (OSError, subprocess.TimeoutExpired):
            pass
    google_token = bool(os.environ.get("GOOGLE_REFRESH_TOKEN") or os.environ.get("GOOGLE_WORKSPACE_REFRESH_TOKEN"))
    return {
        "GitHub": has("gh") and run_ok(["gh", "auth", "status"]),
        "Google Drive": f"{os.environ.get('GOOGLE_RCLONE_REMOTE', 'gdrive')}:" in remotes,
        "OneDrive": f"{os.environ.get('OUTLOOK_RCLONE_REMOTE', 'outlook')}:" in remotes,
        "Gmail": google_token and "gmail" in os.environ.get("GOOGLE_OAUTH_SCOPES", "").lower(),
        "Google Calendar": google_token and "calendar" in os.environ.get("GOOGLE_OAUTH_SCOPES", "").lower(),
        "Google Cloud": bool(os.environ.get("GOOGLE_CLOUD_PROJECT")),
        "Firecrawl": bool(os.environ.get("FIRECRAWL_API_KEY")),
        "OpenRouter": bool(os.environ.get("OPENROUTER_API_KEY") or (HOME / ".openrouter_key").is_file()),
        "Ollama": has("ollama"),
        "Shizuku/rish": has("rish") or (HOME / "rish").is_file(),
    }


def print_status() -> int:
    load_env_file()
    print("JOSIE 3.0 status")
    print(f"  Python: {sys.version.split()[0]}")
    print(f"  Interactive terminal: {'yes' if sys.stdin.isatty() else 'no'}")
    print("  Providers:")
    for name in PROVIDERS:
        wait = circuit_open(name)
        print(f"    {name:12} {'cooldown '+str(wait)+'s' if wait else 'ready'}")
    print("  Connectors (local authorization detected):")
    for name, ready in connector_status().items():
        print(f"    {name:16} {'configured' if ready else 'setup needed'}")
    return 0


def cmd_shell(argv: list[str]) -> int:
    shell = os.environ.get("SHELL") or shutil.which("bash") or "/system/bin/sh"
    if argv:
        return subprocess.run(argv).returncode
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        print("Interactive shell requires a TTY.", file=sys.stderr)
        return 2
    return pty.spawn([shell, "-l"])


def cmd_fix() -> int:
    actions = [
        (["sshd"], ["pgrep", "sshd"]),
        ([str(HOME / "bin/start-agi")], ["pgrep", "-f", "web_app.py"]),
        ([str(HOME / "bin/start-code-server")], ["pgrep", "-f", "code-server"]),
    ]
    failures = 0
    for start, check in actions:
        name = Path(start[0]).name
        if not shutil.which(start[0]) and not Path(start[0]).is_file():
            print(f"SKIP {name}: launcher not installed")
            continue
        if subprocess.run(check, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
            print(f"OK   {name}: already running")
            continue
        try:
            subprocess.Popen(start, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            print(f"START {name}")
        except OSError as exc:
            failures += 1
            print(f"FAIL {name}: {exc}")
    return 1 if failures else 0


def memory(query: str) -> int:
    if not DB_PATH.is_file():
        print(f"Memory database not found: {DB_PATH}", file=sys.stderr)
        return 1
    try:
        with sqlite3.connect(DB_PATH) as conn:
            if query:
                rows = conn.execute(
                    "SELECT timestamp,event,outcome FROM memory WHERE event LIKE ? OR outcome LIKE ? ORDER BY id DESC LIMIT 10",
                    (f"%{query}%", f"%{query}%"),
                ).fetchall()
            else:
                rows = conn.execute("SELECT timestamp,event,outcome FROM memory ORDER BY id DESC LIMIT 10").fetchall()
    except sqlite3.Error as exc:
        print(f"Memory error: {exc}", file=sys.stderr)
        return 1
    for timestamp, event, outcome in rows:
        print(f"[{timestamp}] {event}\n  {str(outcome)[:500]}")
    return 0


def repl(model: str) -> int:
    print("JOSIE REPL 3.0 — :paste for multiline, :shell for a real shell, :status, :quit")
    while True:
        try:
            line = input("josie > ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if not line:
            continue
        if line in {":quit", ":exit", "exit", "quit"}:
            return 0
        if line == ":status":
            print_status()
            continue
        if line == ":shell":
            cmd_shell([])
            continue
        if line == ":paste":
            print("Paste text; finish with a line containing only :end")
            block: list[str] = []
            while True:
                try:
                    value = input()
                except EOFError:
                    break
                if value == ":end":
                    break
                block.append(value)
            line = "\n".join(block).strip()
            if not line:
                continue
        try:
            reply, provider = ask(line, model)
            print(f"[{provider}] {reply}")
        except ProviderError as exc:
            print(f"ERROR {exc}", file=sys.stderr)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="agi", description="JOSIE local-first command center")
    sub = parser.add_subparsers(dest="command")
    ask_parser = sub.add_parser("ask", aliases=["q", "prompt"])
    ask_parser.add_argument("text", nargs="+")
    ask_parser.add_argument("-m", "--model", default=os.environ.get("JOSIE_MODEL", ""))
    repl_parser = sub.add_parser("repl", aliases=["chat"])
    repl_parser.add_argument("-m", "--model", default=os.environ.get("JOSIE_MODEL", ""))
    shell_parser = sub.add_parser("shell", aliases=["bash", "sh"])
    shell_parser.add_argument("argv", nargs=argparse.REMAINDER)
    memory_parser = sub.add_parser("memory", aliases=["recall", "vault"])
    memory_parser.add_argument("query", nargs="*")
    sub.add_parser("status", aliases=["check", "doctor", "diagnostics"])
    sub.add_parser("fix", aliases=["repair", "heal"])
    connectors = sub.add_parser("connectors", aliases=["apps"])
    connectors.add_argument("action", choices=["status", "auth", "start"], default="status", nargs="?")
    return parser


def main(argv: list[str] | None = None) -> int:
    load_env_file()
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.command:
        return repl(os.environ.get("JOSIE_MODEL", "")) if sys.stdin.isatty() else parser.print_help() or 0
    command = args.command
    if command in {"ask", "q", "prompt"}:
        try:
            reply, provider = ask(" ".join(args.text), args.model)
            print(f"[{provider}] {reply}")
            return 0
        except ProviderError as exc:
            print(f"ERROR {exc}", file=sys.stderr)
            return 1
    if command in {"repl", "chat"}:
        return repl(args.model)
    if command in {"shell", "bash", "sh"}:
        return cmd_shell(args.argv)
    if command in {"memory", "recall", "vault"}:
        return memory(" ".join(args.query))
    if command in {"status", "check", "doctor", "diagnostics"}:
        return print_status()
    if command in {"fix", "repair", "heal"}:
        return cmd_fix()
    if command in {"connectors", "apps"}:
        script = Path(__file__).with_name("termux_connected_apps.sh")
        return subprocess.run(["bash", str(script), args.action]).returncode
    parser.error(f"unknown command: {command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
