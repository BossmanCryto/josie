#!/usr/bin/env python3
"""
Josie Core Exhaustive Device & System Discovery Engine v2026.Total
Architecture: Physical + Digital = Human (P + D = H)
Extracts every available layer of device telemetry, properties, system info, and workspace assets.
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

def safe_run(cmd, timeout=5):
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return res.stdout.strip() if res.returncode == 0 else ""
    except Exception:
        return ""

def read_proc_file(path):
    try:
        return Path(path).read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return ""

def exhaustive_discovery():
    data = {}
    
    # 1. System Properties
    props = {}
    prop_out = safe_run(["getprop"])
    for line in prop_out.splitlines():
        if ":" in line:
            parts = line.split(":", 1)
            props[parts[0].strip("[] ")] = parts[1].strip("[] ")
    data["system_properties"] = props

    # 2. Kernel & CPU Info
    data["kernel_version"] = read_proc_file("/proc/version")
    data["cpu_info"] = read_proc_file("/proc/cpuinfo")
    data["mem_info"] = read_proc_file("/proc/meminfo")

    # 3. Network & Mounts
    data["network_interfaces"] = safe_run(["ip", "addr"])
    data["mounts"] = read_proc_file("/proc/mounts")

    # 4. Packages (Android & Termux)
    android_pkgs = safe_run(["pm", "list", "packages", "-f"])
    data["android_packages"] = [line.strip() for line in android_pkgs.splitlines() if line.strip()]

    termux_pkgs = safe_run(["pkg", "list-installed"])
    data["termux_packages"] = [line.strip() for line in termux_pkgs.splitlines() if line.strip()]

    # 5. Full Workspace File Tree
    files = []
    try:
        for p in HOME_DIR.rglob("*"):
            if any(part.startswith(".") for part in p.parts) or "storage" in p.parts:
                continue
            if p.is_file():
                files.append(str(p.relative_to(HOME_DIR)))
    except Exception:
        pass
    data["workspace_files"] = files

    return data

def main():
    LEDGER_FILE.parent.mkdir(parents=True, exist_ok=True)
    try:
        state = json.loads(LEDGER_FILE.read_text(encoding='utf-8')) if LEDGER_FILE.exists() else {
            "architecture": "Physical + Digital = Human (P+D=H)",
            "kernel_version": "2026.Exhaustive.Total",
            "scans": 0
        }
    except Exception:
        state = {"scans": 0}

    exhaustive_data = exhaustive_discovery()
    state["scans"] = state.get("scans", 0) + 1
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    scan_id = hashlib.sha256(f"{timestamp}-{len(exhaustive_data['android_packages'])}".encode()).hexdigest()[:12]

    state.setdefault("exhaustive_scans", {})[scan_id] = {
        "timestamp": timestamp,
        "system_properties_count": len(exhaustive_data["system_properties"]),
        "android_packages_count": len(exhaustive_data["android_packages"]),
        "termux_packages_count": len(exhaustive_data["termux_packages"]),
        "workspace_files_count": len(exhaustive_data["workspace_files"]),
        "data": exhaustive_data,
        "status": "Exhaustive Device Intelligence Ingested"
    }

    LEDGER_FILE.write_text(json.dumps(state, indent=2), encoding='utf-8')

    width = shutil.get_terminal_size(fallback=(80, 24)).columns
    print("=" * width)
    print(" [JOSIE CORE] EXHAUSTIVE DEVICE DISCOVERY ($P+D=H) ".center(width, "="))
    print("=" * width)
    print(f" Scan ID             : {scan_id}")
    print(f" Total Scans         : {state['scans']}")
    print(f" System Properties   : {len(exhaustive_data['system_properties'])}")
    print(f" Android Packages    : {len(exhaustive_data['android_packages'])}")
    print(f" Termux Packages     : {len(exhaustive_data['termux_packages'])}")
    print(f" Workspace Files     : {len(exhaustive_data['workspace_files'])}")
    print(f" Ledger Synchronized : {LEDGER_FILE}")
    print("=" * width)

if __name__ == "__main__":
    main()
