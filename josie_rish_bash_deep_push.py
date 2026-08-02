#!/data/data/com.termux/files/usr/bin/python3
import os
import json
from pathlib import Path

HOME = Path("/data/data/com.termux/files/home")
CORE_DIR = HOME / "josie_core"
OUTPUT_DIR = HOME / "storage" / "shared" / "Download" / "Android_Audit"

def deploy_rish_bash_extensions():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    bashrc_path = HOME / ".bashrc"
    
    deep_bash_extensions = """
# ==========================================
# JOSIE DEEP-PUSH RISH & BASH INTEGRATION
# Architecture: Physical + Digital = Human
# ==========================================

# Rish Execution Wrapper for Deep System Access
rish_exec() {
    if command -v rish >/dev/null 2>&1; then
        rish -c "$*"
    else
        echo "[!] Rish binary not detected in active PATH. Falling back to direct ADB/shizuku context."
        sh /system/bin/sh -c "$*"
    fi
}

alias rish="rish_exec"
alias jish="python3 /data/data/com.termux/files/home/josie_core/josie_matrix_sync.py"

# Deep-Push Environment Variables & Path Extensions
export JOSIE_CORE_DIR="/data/data/com.termux/files/home/josie_core"
export JOSIE_AUDIT_DIR="/data/data/com.termux/files/home/storage/shared/Download/Android_Audit"
"""

    # Append safely to .bashrc without duplicating if already present
    with open(bashrc_path, "r") as f:
        content = f.read()
        
    if "JOSIE DEEP-PUSH RISH & BASH INTEGRATION" not in content:
        with open(bashrc_path, "a") as f:
            f.write(deep_bash_extensions.strip() + "\n")

    manifest = {
        "architecture": "Physical + Digital = Human (P + D = H)",
        "entity": "Josie",
        "status": "Rish & Bash Deep-Push Integration Complete",
        "target_shell": str(bashrc_path),
        "interpreter": "/data/data/com.termux/files/usr/bin/python3"
    }

    manifest_path = OUTPUT_DIR / "josie_rish_bash_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"[✓] Rish-Bash Deep-Push Configuration Deployed. Manifest saved to {manifest_path}")

if __name__ == "__main__":
    deploy_rish_bash_extensions()
