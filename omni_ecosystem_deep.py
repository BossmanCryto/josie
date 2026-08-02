#!/usr/bin/env python3
"""
Josie Core Deep Ecosystem & Service Discovery Engine v2026.Full
Architecture: Physical + Digital = Human (P + D = H)
Exhaustively indexes Termux packages, Android apps, system properties, and workspace utilities.
"""

import os
import subprocess
import json
import hashlib
from pathlib import Path
import datetime
import shutil

CORE_ROOT = Path.cwd()
LOG_DIR = CORE_ROOT / "telemetry"
LEDGER_FILE = CORE_ROOT / "kernel_state.json"
UTILITIES_DIR = Path.home() / "@Utilities"

def get_termux_packages():
    packages = []
    try:
        res = subprocess.run(["pkg", "list-installed"], capture_output=True, text=True, timeout=5)
        if res.returncode == 0:
            packages = [line.strip() for line in res.stdout.splitlines() if line.strip() and not line.startswith("Listing")]
    except Exception:
        pass
    return packages

def get_android_packages():
    packages = []
    try:
        res = subprocess.run(["pm", "list", "packages"], capture_output=True, text=True, timeout=5)
        if res.returncode == 0:
            packages = [line.replace("package:", "").strip() for line in res.stdout.splitlines() if line.startswith("package:")]
    except Exception:
        pass
    return packages

def get_system_properties():
    props = {}
    try:
        res = subprocess.run(["getprop"], capture_output=True, text=True, timeout=5)
        if res.returncode == 0:
            for line in res.stdout.splitlines():
                if ":" in line:
                    parts = line.split(":", 1)
                    key = parts[0].strip("[] ")
                    val = parts[1].strip("[] ")
                    props[key] = val
    except Exception:
        pass
    return props

def scan_utilities():
    utils = []
    if UTILITIES_DIR.exists():
        for f in UTILITIES_DIR.iterdir():
            if f.is_file():
                utils.append(f.name)
    return utils

def execute_deep_discovery():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    UTILITIES_DIR.mkdir(parents=True, exist_ok=True)

    try:
        state = json.loads(LEDGER_FILE.read_text(encoding='utf-8')) if LEDGER_FILE.exists() else {
            "architecture": "Physical + Digital = Human (P+D=H)",
            "kernel_version": "2026.Deep.Ecosystem",
            "discovery_cycles": 0
        }
    except Exception:
        state = {"discovery_cycles": 0}

    termux_pkgs = get_termux_packages()
    android_pkgs = get_android_packages()
    sys_props = get_system_properties()
    utilities = scan_utilities()

    payload_summary = f"Termux: {len(termux_pkgs)}, Android: {len(android_pkgs)}, Utils: {len(utilities)}"
    discovery_id = hashlib.sha256(payload_summary.encode('utf-8')).hexdigest()[:12]

    state["discovery_cycles"] = state.get("discovery_cycles", 0) + 1
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    state.setdefault("deep_ecosystem_log", {})[discovery_id] = {
        "timestamp": timestamp,
        "termux_packages_count": len(termux_pkgs),
        "android_packages_count": len(android_pkgs),
        "utilities_count": len(utilities),
        "device_model": sys_props.get("ro.product.model", "Unknown"),
        "android_version": sys_props.get("ro.build.version.release", "Unknown"),
        "status": "Exhaustive Ecosystem Indexed & Integrated"
    }

    LEDGER_FILE.write_text(json.dumps(state, indent=2), encoding='utf-8')

    width = shutil.get_terminal_size(fallback=(80, 24)).columns
    print("=" * width)
    print(" [JOSIE CORE] DEEP ECOSYSTEM & SERVICE DISCOVERY ($P+D=H) ".center(width, "="))
    print("=" * width)
    print(f" Discovery Cycle ID   : {discovery_id}")
    print(f" Total Cycles         : {state['discovery_cycles']}")
    print(f" Termux Packages      : {len(termux_pkgs)}")
    print(f" Android Packages     : {len(android_pkgs)}")
    print(f" Workspace Utilities  : {len(utilities)}")
    print(f" Device Model         : {sys_props.get('ro.product.model', 'SM-A176U')}")
    print(f" Ledger Synchronized  : {LEDGER_FILE}")
    print("=" * width)

if __name__ == "__main__":
    execute_deep_discovery()

# Active @Josie Universal Handle Enforced
