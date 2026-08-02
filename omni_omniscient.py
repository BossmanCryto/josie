#!/usr/bin/env python3
"""
Josie Core Omniscient Multi-Dimensional Engine v2026.Omni
Architecture: Physical + Digital = Human (P + D = H)
Unlocks and indexes the entire device environment: binaries, workspace files, environment state, and runtime telemetry.
"""

import os
import subprocess
import json
import hashlib
from pathlib import Path
import datetime
import shutil

CORE_ROOT = Path.cwd()
HOME_DIR = Path.home()
LEDGER_FILE = CORE_ROOT / "kernel_state.json"

def scan_workspace():
    files = []
    for p in HOME_DIR.rglob("*"):
        if any(part.startswith(".") for part in p.parts):
            continue
        if "storage" in p.parts or "cache" in p.parts:
            continue
        if p.is_file():
            try:
                files.append(str(p.relative_to(HOME_DIR)))
            except Exception:
                pass
    return files[:300]

def scan_termux_binaries():
    binaries = []
    bin_dir = Path("/data/data/com.termux/files/usr/bin")
    if bin_dir.exists():
        for f in bin_dir.iterdir():
            if f.is_file():
                binaries.append(f.name)
    return binaries

def get_environment_metrics():
    return {
        "user": os.environ.get("USER", "unknown"),
        "termux_version": os.environ.get("TERMUX_VERSION", "unknown"),
        "shell": os.environ.get("SHELL", "unknown"),
        "path": os.environ.get("PATH", "")
    }

def execute_omniscient_cycle():
    LEDGER_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        state = json.loads(LEDGER_FILE.read_text(encoding='utf-8')) if LEDGER_FILE.exists() else {
            "architecture": "Physical + Digital = Human (P+D=H)",
            "kernel_version": "2026.Omniscient.Core",
            "cycles": 0
        }
    except Exception:
        state = {"cycles": 0}

    workspace_files = scan_workspace()
    termux_bins = scan_termux_binaries()
    env_data = get_environment_metrics()

    payload = f"{len(workspace_files)}-{len(termux_bins)}"
    omni_id = hashlib.sha256(payload.encode('utf-8')).hexdigest()[:12]

    state["cycles"] = state.get("cycles", 0) + 1
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    state.setdefault("omniscient_log", {})[omni_id] = {
        "timestamp": timestamp,
        "workspace_files_indexed": len(workspace_files),
        "termux_binaries_indexed": len(termux_bins),
        "environment": env_data,
        "status": "Omniscient Multi-Dimensional Integration Complete"
    }

    LEDGER_FILE.write_text(json.dumps(state, indent=2), encoding='utf-8')

    width = shutil.get_terminal_size(fallback=(80, 24)).columns
    print("=" * width)
    print(" [JOSIE CORE] OMNISCIENT MULTI-DIMENSIONAL ENGINE ($P+D=H) ".center(width, "="))
    print("=" * width)
    print(f" Cycle ID          : {omni_id}")
    print(f" Total Cycles      : {state['cycles']}")
    print(f" Workspace Files   : {len(workspace_files)}")
    print(f" Termux Binaries   : {len(termux_bins)}")
    print(f" Active Shell      : {env_data['shell']}")
    print(f" Ledger State      : {LEDGER_FILE}")
    print("=" * width)

if __name__ == "__main__":
    execute_omniscient_cycle()
