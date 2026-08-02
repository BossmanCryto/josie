#!/usr/bin/env python3
"""
Josie Core Autonomous Audit & Logging Engine v2026.Auto
Architecture: Physical + Digital = Human (P + D = H)
Automatically logs all execution steps, telemetry, and diagnostics to disk and terminal.
"""

import os
import subprocess
import json
import hashlib
import logging
from pathlib import Path
import datetime
import shutil

CORE_ROOT = Path.cwd()
LEDGER_FILE = CORE_ROOT / "kernel_state.json"
LOG_FILE = CORE_ROOT / "josie_core.log"

# Configure dual logging (Console + Persistent File)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def safe_run(cmd, timeout=3):
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return res.stdout.strip() if res.returncode == 0 else ""
    except Exception as e:
        logging.warning(f"Command {' '.join(cmd)} failed: {e}")
        return ""

def get_comprehensive_telemetry():
    logging.info("Gathering comprehensive device & environment telemetry...")
    telemetry = {
        "device_model": safe_run(["getprop", "ro.product.model"]) or "SM-A176U",
        "android_version": safe_run(["getprop", "ro.build.version.release"]) or "Unknown",
        "termux_pkgs_count": len(safe_run(["pkg", "list-installed"]).splitlines()),
        "android_pkgs_count": len(safe_run(["pm", "list", "packages"]).splitlines()),
        "storage_free_mb": (lambda st: (st.f_bavail * st.f_frsize) // (1024 * 1024))(os.statvfs(str(CORE_ROOT)))
    }
    logging.info(f"Telemetry captured: Model={telemetry['device_model']}, Storage Free={telemetry['storage_free_mb']}MB")
    return telemetry

def main():
    LEDGER_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        state = json.loads(LEDGER_FILE.read_text(encoding='utf-8')) if LEDGER_FILE.exists() else {}
    except Exception:
        state = {}

    state.setdefault("architecture", "Physical + Digital = Human (P+D=H)")
    state.setdefault("generation", 1)
    state.setdefault("audit_logs", {})

    state["generation"] += 1
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    audit_id = hashlib.sha256(f"{timestamp}-{state['generation']}".encode()).hexdigest()[:12]

    logging.info(f"Starting Audit Cycle: ID={audit_id}, Generation={state['generation']}")
    telemetry = get_comprehensive_telemetry()

    state["audit_logs"][audit_id] = {
        "timestamp": timestamp,
        "generation": state["generation"],
        "telemetry": telemetry,
        "status": "Fully Audited & Logged"
    }

    LEDGER_FILE.write_text(json.dumps(state, indent=2), encoding='utf-8')
    logging.info(f"Kernel state successfully committed to ledger: {LEDGER_FILE}")
    logging.info(f"Detailed execution log saved to: {LOG_FILE}")

    width = shutil.get_terminal_size(fallback=(80, 24)).columns
    print("=" * width)
    print(" [JOSIE CORE] AUTONOMOUS AUDIT & LOGGING ENGINE ($P+D=H) ".center(width, "="))
    print("=" * width)
    print(f" Audit ID           : {audit_id}")
    print(f" Generation         : {state['generation']}")
    print(f" Log File Location  : {LOG_FILE}")
    print(f" Ledger Synchronized: {LEDGER_FILE}")
    print("=" * width)

if __name__ == "__main__":
    main()

# Active @Josie Universal Handle Enforced
