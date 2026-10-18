#!/usr/bin/env python3
"""Small, dependency-free dashboard for connection readiness.

The dashboard never returns credential values. It reports whether each service has
local authentication/configuration available and gives the user a direct setup link.
"""
from __future__ import annotations

import json
import os
import shutil
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Callable
from urllib.parse import urlsplit

HOST = os.environ.get("CONNECTED_APPS_HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", os.environ.get("CONNECTED_APPS_PORT", "8080")))


def env_present(*names: str) -> bool:
    return any(bool(os.environ.get(name, "").strip()) for name in names)


def credentials_file_present() -> bool:
    value = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "").strip()
    return bool(value and Path(value).expanduser().is_file())


def google_ready() -> bool:
    return env_present("GOOGLE_REFRESH_TOKEN", "GOOGLE_WORKSPACE_REFRESH_TOKEN") or credentials_file_present()


def rish_ready() -> bool:
    candidates = (
        Path.home() / "rish",
        Path(os.environ.get("PREFIX", "/data/data/com.termux/files/usr")) / "bin" / "rish",
        Path("/data/local/tmp/rish"),
    )
    return shutil.which("rish") is not None or any(path.is_file() for path in candidates)


APP_DEFS: tuple[dict[str, object], ...] = (
    {"id": "outlook", "name": "Outlook", "check": lambda: env_present("MICROSOFT_REFRESH_TOKEN", "MS_REFRESH_TOKEN"), "setup": "https://myapplications.microsoft.com/"},
    {"id": "drive", "name": "Google Drive", "check": google_ready, "setup": "https://myaccount.google.com/connections"},
    {"id": "gmail", "name": "Gmail", "check": google_ready, "setup": "https://myaccount.google.com/connections"},
    {"id": "calendar", "name": "Google Calendar", "check": google_ready, "setup": "https://myaccount.google.com/connections"},
    {"id": "academic", "name": "Academic", "check": lambda: env_present("ACADEMIC_EMAIL", "GOOGLE_WORKSPACE_DOMAIN"), "setup": "https://myaccount.google.com/"},
    {"id": "github", "name": "GitHub", "check": lambda: env_present("GH_TOKEN", "GITHUB_TOKEN"), "setup": "https://github.com/settings/installations"},
    {"id": "gcloud", "name": "Google Cloud", "check": lambda: credentials_file_present() or env_present("GOOGLE_CLOUD_PROJECT", "GCLOUD_PROJECT"), "setup": "https://console.cloud.google.com/"},
    {"id": "firecrawl", "name": "Firecrawl", "check": lambda: env_present("FIRECRAWL_API_KEY"), "setup": "https://www.firecrawl.dev/app"},
    {"id": "rish", "name": "Rish", "check": rish_ready, "setup": "https://github.com/RikkaApps/Shizuku-API/tree/master/rish"},
)


def get_app_statuses() -> list[dict[str, object]]:
    statuses: list[dict[str, object]] = []
    for item in APP_DEFS:
        check = item["check"]
        configured = bool(check()) if isinstance(check, Callable) else False
        statuses.append({
            "id": item["id"],
            "name": item["name"],
            "status": "configured" if configured else "setup_needed",
            "label": "Configured" if configured else "Setup needed",
            "setup": item["setup"],
        })
    return statuses


INDEX_HTML = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Connected Apps</title>
<style>
:root{color-scheme:dark;--bg:#0b1020;--panel:#151c31;--line:#2b3658;--text:#eef2ff;--muted:#aab4d0;--ok:#39d98a;--warn:#ffbd59;--blue:#6ea8fe}*{box-sizing:border-box}body{margin:0;background:linear-gradient(145deg,#080c18,#101831);color:var(--text);font:16px/1.45 system-ui,sans-serif}main{max-width:980px;margin:auto;padding:40px 18px}header{display:flex;gap:18px;align-items:end;justify-content:space-between;margin-bottom:24px}h1{margin:0;font-size:clamp(28px,5vw,46px)}p{color:var(--muted);margin:6px 0}.button{border:1px solid var(--line);background:#1b2645;color:var(--text);padding:10px 14px;border-radius:10px;cursor:pointer;font-weight:700}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px}.card{background:rgba(21,28,49,.92);border:1px solid var(--line);border-radius:16px;padding:18px;min-height:150px;display:flex;flex-direction:column;justify-content:space-between}.top{display:flex;align-items:center;justify-content:space-between;gap:8px}.name{font-size:19px;font-weight:800}.badge{font-size:12px;font-weight:800;padding:5px 9px;border-radius:999px}.configured{color:var(--ok);background:#123b2d}.setup_needed{color:var(--warn);background:#46351c}.setup{color:var(--blue);text-decoration:none;font-weight:700}footer{margin-top:24px;color:var(--muted);font-size:13px}.error{color:#ff7b7b}</style>
</head>
<body><main><header><div><h1>Connected Apps</h1><p>See what is configured on this device. Secret values are never shown.</p></div><button class="button" id="refresh">Refresh</button></header><section id="apps" class="grid" aria-live="polite"></section><footer id="summary">Checking local configuration…</footer></main>
<script>
const root=document.getElementById('apps'), summary=document.getElementById('summary');
function safeText(value){return document.createTextNode(String(value))}
function card(app){const el=document.createElement('article');el.className='card';const top=document.createElement('div');top.className='top';const name=document.createElement('span');name.className='name';name.append(safeText(app.name));const badge=document.createElement('span');badge.className='badge '+app.status;badge.append(safeText(app.label));top.append(name,badge);const note=document.createElement('p');note.append(safeText(app.status==='configured'?'Local credentials or configuration found.':'No local credentials found.'));const link=document.createElement('a');link.className='setup';link.href=app.setup;link.target='_blank';link.rel='noopener noreferrer';link.append(safeText(app.status==='configured'?'Manage connection →':'Set up →'));el.append(top,note,link);return el}
async function load(){root.replaceChildren();summary.textContent='Checking local configuration…';try{const response=await fetch('/api/apps',{cache:'no-store'});if(!response.ok)throw new Error('Request failed');const data=await response.json();data.apps.forEach(app=>root.append(card(app)));summary.textContent=`${data.configured} of ${data.total} apps configured. Status checks configuration only; they do not read account data.`}catch(error){summary.className='error';summary.textContent='Could not load app status.'}}
document.getElementById('refresh').addEventListener('click',load);load();
</script></body></html>'''


class Handler(BaseHTTPRequestHandler):
    server_version = "ConnectedApps/1.0"

    def log_message(self, format: str, *args: object) -> None:
        if os.environ.get("CONNECTED_APPS_LOG", "").lower() in {"1", "true", "yes"}:
            super().log_message(format, *args)

    def _send(self, status: int, content_type: str, body: bytes) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        path = urlsplit(self.path).path
        if path == "/":
            self._send(200, "text/html; charset=utf-8", INDEX_HTML.encode())
            return
        if path in {"/health", "/api/apps"}:
            apps = get_app_statuses()
            configured = sum(app["status"] == "configured" for app in apps)
            payload = {"ok": True, "configured": configured, "total": len(apps)}
            if path == "/api/apps":
                payload["apps"] = apps
            self._send(200, "application/json; charset=utf-8", json.dumps(payload).encode())
            return
        self._send(404, "application/json; charset=utf-8", b'{"error":"not found"}')


def main() -> None:
    with ThreadingHTTPServer((HOST, PORT), Handler) as server:
        print(f"Connected Apps running at http://{HOST}:{PORT}", flush=True)
        server.serve_forever()


if __name__ == "__main__":
    main()
