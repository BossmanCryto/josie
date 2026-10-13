#!/usr/bin/env python3
"""Standalone Google Gemini Vertex AI integration for JOSIE.

Usage:
  python gemini_integration.py "Your prompt"
  python gemini_integration.py

Required environment variables:
  GOOGLE_CLOUD_PROJECT      Google Cloud project ID
  GOOGLE_ACCESS_TOKEN       Short-lived OAuth access token with Vertex AI scope
  GEMINI_MODEL              Optional; default gemini-2.0-flash
  GOOGLE_CLOUD_LOCATION     Optional; default us-central1
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request


class GeminiError(RuntimeError):
    pass


def request_reply(prompt: str) -> str:
    project = os.environ.get("GOOGLE_CLOUD_PROJECT", "").strip()
    token = os.environ.get("GOOGLE_ACCESS_TOKEN", "").strip()
    if not project:
        raise GeminiError("GOOGLE_CLOUD_PROJECT is not configured")
    if not token:
        raise GeminiError("GOOGLE_ACCESS_TOKEN is not configured")

    model = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash").strip()
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1").strip()
    url = (
        f"https://{location}-aiplatform.googleapis.com/v1/projects/{project}"
        f"/locations/{location}/publishers/google/models/{model}:generateContent"
    )
    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": prompt}]}
        ]
    }
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "JOSIE-Gemini/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:300]
        raise GeminiError(f"Gemini HTTP {exc.code}: {detail}") from exc
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise GeminiError(f"Gemini request failed: {exc}") from exc

    try:
        reply = result["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError, TypeError) as exc:
        raise GeminiError("Gemini returned no usable reply") from exc
    if not isinstance(reply, str) or not reply.strip():
        raise GeminiError("Gemini returned an empty reply")
    return reply.strip()


def repl() -> int:
    print("JOSIE Gemini REPL — type a prompt, or :quit to exit")
    while True:
        try:
            prompt = input("gemini > ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if not prompt:
            continue
        if prompt in {":quit", ":exit", "exit", "quit"}:
            return 0
        try:
            print(request_reply(prompt))
        except GeminiError as exc:
            print(f"ERROR: {exc}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if not args:
        return repl()
    try:
        print(request_reply(" ".join(args)))
        return 0
    except GeminiError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())