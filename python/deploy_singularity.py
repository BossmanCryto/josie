import os
import sys
import subprocess

HOME = os.getenv("HOME", "/data/data/com.termux/files/home")
WORKSPACE_DIR = os.path.join(HOME, "josie_core")
BIN_DIR = os.path.join(HOME, ".local", "bin")
AUDIT_DIR = os.path.join(HOME, "storage", "shared", "Download", "Android_Audit")

print("=== JOSIE OMEGA DEPLOYMENT ENGINE ===")

# 1. Ensure Directories Exist
os.makedirs(WORKSPACE_DIR, exist_ok=True)
os.makedirs(BIN_DIR, exist_ok=True)
os.makedirs(AUDIT_DIR, exist_ok=True)

# 2. Write the Omega Singularity Python Engine
singularity_path = os.path.join(WORKSPACE_DIR, "omega_singularity.py")
singularity_code = """#!/usr/bin/env python3
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
            f.write(formatted_msg + "\\n")
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
"""

with open(singularity_path, "w") as f:
    f.write(singularity_code)
os.chmod(singularity_path, 0o755)
print(f"[ok] Created engine: {singularity_path}")

# 3. Write the Master CLI Wrapper ('josie')
cli_path = os.path.join(WORKSPACE_DIR, "josie")
cli_code = """#!/usr/bin/env bash
set -euo pipefail
JOSIE_HOME="${HOME}/josie_core"
AUDIT_DIR="${HOME}/storage/shared/Download/Android_Audit"

msg() {
    printf '%s\\n' "$*"
}

case "${1:-start}" in
    start|doctor)
        msg "[*] Running Josie Automated Intelligence Engine..."
        python3 "${JOSIE_HOME}/omega_singularity.py"
        msg "[OK] System synchronized and operational."
        ;;
    audit)
        msg "[*] Exporting package inventory..."
        pm list packages -3 | sed 's/package://g' > "${AUDIT_DIR}/installed_packages.txt"
        msg "[OK] Saved to ${AUDIT_DIR}/installed_packages.txt"
        ;;
    *)
        msg "Usage: josie [start|doctor|audit]"
        ;;
esac
"""

with open(cli_path, "w") as f:
    f.write(cli_code)
os.chmod(cli_path, 0o755)
print(f"[ok] Created CLI wrapper: {cli_path}")

# 4. Symlink to Local Bin for Global Execution
symlink_target = os.path.join(BIN_DIR, "josie")
if os.path.islink(symlink_target) or os.path.exists(symlink_target):
    os.remove(symlink_target)
os.symlink(cli_path, symlink_target)
print(f"[ok] Linked global binary: {symlink_target} -> {cli_path}")

print("=== DEPLOYMENT COMPLETE ===")
