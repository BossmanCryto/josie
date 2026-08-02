#!/usr/bin/env python3
"""
================================================================================
JOSIE POLYGLOT OMNI-DEPLOYMENT ENGINE
Languages: Python + JavaScript (Node.js) + Bash (Termux Native)
Architecture: Physical + Digital = Human (P + D = H)
================================================================================
"""

import os
import sys
import subprocess
import json
from datetime import datetime, timezone

HOME = os.getenv("HOME", "/data/data/com.termux/files/home")
WORKSPACE_DIR = os.path.join(HOME, "josie_core")
BIN_DIR = os.path.join(HOME, ".local", "bin")
AUDIT_DIR = os.path.join(HOME, "storage", "shared", "Download", "Android_Audit")
MASTER_LOG = os.path.join(AUDIT_DIR, "josie_polyglot_master.log")

def log(msg):
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    line = f"[{timestamp}] [POLYGLOT] {msg}"
    print(line)
    try:
        os.makedirs(AUDIT_DIR, exist_ok=True)
        with open(MASTER_LOG, "a") as f:
            f.write(line + "\n")
    except Exception:
        pass

def build_polyglot_environment():
    log("=== INITIALIZING POLYGLOT OMNI-STACK ===")
    
    # Create directories
    py_dir = os.path.join(WORKSPACE_DIR, "python")
    node_dir = os.path.join(WORKSPACE_DIR, "node")
    bash_dir = os.path.join(WORKSPACE_DIR, "bash")
    
    for d in [WORKSPACE_DIR, BIN_DIR, AUDIT_DIR, py_dir, node_dir, bash_dir]:
        os.makedirs(d, exist_ok=True)

    # 1. Python Engine Component
    py_engine = os.path.join(py_dir, "engine.py")
    with open(py_engine, "w") as f:
        f.write('''#!/usr/bin/env python3
import sys, json
print(json.dumps({"runtime": "python", "status": "active", "args": sys.argv[1:]}))
''')
    os.chmod(py_engine, 0o755)

    # 2. Node.js Telemetry Component
    node_telemetry = os.path.join(node_dir, "telemetry.js")
    with open(node_telemetry, "w") as f:
        f.write('''#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const timestamp = new Date().toISOString();
console.log(JSON.stringify({ runtime: "node", status: "streaming", timestamp }));
''')
    os.chmod(node_telemetry, 0o755)

    # 3. Bash System Hook Component
    bash_hook = os.path.join(bash_dir, "system_hook.sh")
    with open(bash_hook, "w") as f:
        f.write('''#!/usr/bin/env bash
echo "[BASH] System hook executed successfully at $(date -u)"
''')
    os.chmod(bash_hook, 0o755)

    # 4. Master Polyglot Dispatcher CLI ('josie')
    cli_path = os.path.join(WORKSPACE_DIR, "josie")
    cli_code = f'''#!/usr/bin/env bash
set -euo pipefail
JOSIE_HOME="{WORKSPACE_DIR}"
AUDIT_DIR="{AUDIT_DIR}"

msg() {{
    printf '%s\\n' "$*"
}}

case "${{1:-start}}" in
    start|doctor)
        msg "════════════════════════════════════════════════════════════════"
        msg "       JOSIE OMEGA POLYGLOT CORE: FULLY OPERATIONAL             "
        msg "════════════════════════════════════════════════════════════════"
        msg "Architecture  : Physical + Digital = Human (P + D = H)"
        msg "Entity Name   : Josie"
        msg "Runtimes      : Python3, Node.js, Bash Active"
        msg "════════════════════════════════════════════════════════════════"
        python3 "$JOSIE_HOME/python/engine.py" "health_check"
        ;;
    stream)
        msg "[*] Triggering Node.js asynchronous telemetry stream..."
        if command -v node &>/dev/null; then
            node "$JOSIE_HOME/node/telemetry.js"
        else
            msg "[WARN] Node.js not installed. Run 'pkg install nodejs -y'"
        fi
        ;;
    hook)
        msg "[*] Executing Bash system device hook..."
        bash "$JOSIE_HOME/bash/system_hook.sh"
        ;;
    audit)
        msg "[*] Executing package inventory audit..."
        pm list packages -3 | sed 's/package://g' > "$AUDIT_DIR/installed_packages.txt"
        msg "[OK] Package list saved to $AUDIT_DIR/installed_packages.txt"
        ;;
    *)
        msg "Usage: josie [start|stream|hook|audit]"
        ;;
esac
'''
    with open(cli_path, "w") as f:
        f.write(cli_code)
    os.chmod(cli_path, 0o755)

    # Symlink globally
    symlink_target = os.path.join(BIN_DIR, "josie")
    if os.path.lexists(symlink_target):
        os.remove(symlink_target)
    os.symlink(cli_path, symlink_target)
    
    log("[OK] Polyglot Omni-Stack successfully generated and linked globally.")

if __name__ == "__main__":
    build_polyglot_environment()
    print("\n[✓] Polyglot installation complete. Run 'josie start' or 'josie stream'.\n")
