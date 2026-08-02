#!/usr/bin/env python3
import os
import subprocess
from datetime import datetime, timezone

HOME = os.getenv("HOME", "/data/data/com.termux/files/home")
WORKSPACE_DIR = os.path.join(HOME, "josie_core")
AUDIT_DIR = os.path.join(HOME, "storage", "shared", "Download", "Android_Audit")
MASTER_LOG = os.path.join(AUDIT_DIR, "omega_singularity_master.log")

def log_event(message):
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    formatted_msg = f"[{timestamp}] {message}"
    print(formatted_msg)
    try:
        os.makedirs(AUDIT_DIR, exist_ok=True)
        with open(MASTER_LOG, "a") as f:
            f.write(formatted_msg + "\n")
    except Exception as e:
        print(f"[!] Log write error: {e}")

def main():
    log_event("=== OMEGA SINGULARITY AUTO-HEAL STARTED ===")
    os.makedirs(WORKSPACE_DIR, exist_ok=True)
    os.makedirs(AUDIT_DIR, exist_ok=True)
    
    # Git Submodule Protocol Check
    try:
        subprocess.run(["git", "config", "--global", "url.https://github.com/.insteadOf", "git@github.com:"], check=True)
        log_event("[ok] Global Git HTTPS redirection enforced.")
    except Exception as e:
        log_event(f"[!] Git config notice: {e}")

    log_event("=== OMEGA SINGULARITY AUTO-HEAL COMPLETED SUCCESSFULLY ===")

if __name__ == "__main__":
    main()
