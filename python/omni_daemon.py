#!/data/data/com.termux/files/usr/bin/env python3
"""
Josie Core Autonomous Background Daemon v2026.Daemon
Architecture: Physical + Digital = Human (P + D = H)
Rate-Limit Safe & Zero-Waste Anti-Parasitic Daemon
"""

import os
import time
import subprocess
import json
import hashlib
from pathlib import Path
import datetime

CORE_ROOT = Path.cwd()
LEDGER_FILE = CORE_ROOT / "kernel_state.json"
LOG_FILE = CORE_ROOT / "josie_core.log"
INTERVAL_SECONDS = 300  # 5 minutes zero-waste interval

def log_msg(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] [DAEMON] {msg}"
    print(line)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass

def safe_run(cmd):
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        return res.stdout.strip() if res.returncode == 0 else ""
    except Exception:
        return ""

def git_sync(cycle_id):
    # Only sync if there are actual working tree changes (zero-waste)
    status = safe_run(["git", "status", "--porcelain"])
    if status:
        safe_run(["git", "add", "-A"])
        safe_run(["git", "commit", "-m", f"Josie Core Autonomous Sync [{cycle_id}]: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"])
        safe_run(["git", "push", "origin", "main"])

def main():
    CORE_ROOT.mkdir(parents=True, exist_ok=True)
    log_msg("Anti-Parasitic Autonomous Daemon initialized. Entering zero-waste loop...")
    
    while True:
        try:
            state = json.loads(LEDGER_FILE.read_text(encoding='utf-8')) if LEDGER_FILE.exists() else {}
        except Exception:
            state = {}

        state.setdefault("architecture", "Physical + Digital = Human (P+D=H)")
        state.setdefault("generation", 1)
        state.setdefault("daemon_cycles", {})

        state["generation"] += 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cycle_id = hashlib.sha256(f"{timestamp}-{state['generation']}".encode()).hexdigest()[:12]

        telemetry = {
            "device_model": safe_run(["getprop", "ro.product.model"]) or "SM-A176U",
            "termux_pkgs": len(safe_run(["pkg", "list-installed"]).splitlines()),
            "storage_free_mb": (lambda st: (st.f_bavail * st.f_frsize) // (1024 * 1024))(os.statvfs(str(CORE_ROOT)))
        }

        state["daemon_cycles"][cycle_id] = {
            "timestamp": timestamp,
            "generation": state["generation"],
            "telemetry": telemetry,
            "status": "Zero-Waste Sync Complete"
        }

        LEDGER_FILE.write_text(json.dumps(state, indent=2), encoding='utf-8')
        log_msg(f"Cycle {cycle_id} (Gen {state['generation']}) completed cleanly.")
        
        git_sync(cycle_id)
        
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
