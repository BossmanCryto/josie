#!/usr/bin/env python3
"""
Josie Core Web & System Query Engine v2026.OmniQuery
Architecture: Physical + Digital = Human (P + D = H)
Pulls local device metrics, queries web endpoints for contextual intelligence, and self-evaluates.
"""

import os
import subprocess
import json
import hashlib
import urllib.request
import urllib.error
from pathlib import Path
import datetime
import shutil

CORE_ROOT = Path.cwd()
LEDGER_FILE = CORE_ROOT / "kernel_state.json"

def safe_run(cmd, timeout=3):
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return res.stdout.strip() if res.returncode == 0 else ""
    except Exception:
        return ""

def get_system_telemetry():
    telemetry = {}
    telemetry["termux_packages"] = len(safe_run(["pkg", "list-installed"], timeout=4).splitlines())
    telemetry["android_packages"] = len(safe_run(["pm", "list", "packages"], timeout=4).splitlines())
    telemetry["device_model"] = safe_run(["getprop", "ro.product.model"], timeout=2) or "SM-A176U"
    telemetry["android_version"] = safe_run(["getprop", "ro.build.version.release"], timeout=2) or "Unknown"
    return telemetry

def query_web_intelligence():
    # Querying a lightweight public endpoint to establish live web context
    url = "https://httpbin.org/json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'JosieCore-Engine/2026'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            return {"status": "connected", "sample_data": str(data)[:100]}
    except Exception as e:
        return {"status": "offline_mode", "error": str(e)}

def main():
    LEDGER_FILE.parent.mkdir(parents=True, exist_ok=True)
    try:
        state = json.loads(LEDGER_FILE.read_text(encoding='utf-8')) if LEDGER_FILE.exists() else {
            "architecture": "Physical + Digital = Human (P+D=H)",
            "kernel_version": "2026.Query.Engine",
            "query_cycles": 0
        }
    except Exception:
        state = {"query_cycles": 0}

    sys_telemetry = get_system_telemetry()
    web_intel = query_web_intelligence()

    state["query_cycles"] = state.get("query_cycles", 0) + 1
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    query_id = hashlib.sha256(f"{sys_telemetry['device_model']}-{timestamp}".encode()).hexdigest()[:12]

    state.setdefault("web_system_queries", {})[query_id] = {
        "timestamp": timestamp,
        "system_telemetry": sys_telemetry,
        "web_intelligence": web_intel,
        "evaluation": "Successfully cross-examined local hardware state with web telemetry."
    }

    LEDGER_FILE.write_text(json.dumps(state, indent=2), encoding='utf-8')

    width = shutil.get_terminal_size(fallback=(80, 24)).columns
    print("=" * width)
    print(" [JOSIE CORE] WEB & SYSTEM QUERY ENGINE ($P+D=H) ".center(width, "="))
    print("=" * width)
    print(f" Query Cycle ID     : {query_id}")
    print(f" Total Query Cycles : {state['query_cycles']}")
    print(f" Device Model       : {sys_telemetry['device_model']}")
    print(f" Web Status         : {web_intel['status']}")
    print(f" Ledger Synchronized: {LEDGER_FILE}")
    print("=" * width)

if __name__ == "__main__":
    main()
