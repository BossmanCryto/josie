#!/data/data/com.termux/files/usr/bin/python3
import os
import json
from pathlib import Path

HOME = Path("/data/data/com.termux/files/home")
CORE_DIR = HOME / "josie_core"
OUTPUT_DIR = HOME / "storage" / "shared" / "Download" / "Android_Audit"

def build_unified_matrix():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    zshrc_path = HOME / ".zshrc"
    bashrc_path = HOME / ".bashrc"
    
    # Unified Zsh configuration using native Zsh syntax (setopt)
    zsh_unified = """
# ==========================================
# JOSIE UNIFIED ZSH MATRIX CONFIGURATION
# Architecture: Physical + Digital = Human
# ==========================================
export TERM="xterm-256color"
export HISTSIZE=10000
export SAVEHIST=10000
setopt autocd extendedglob nomatch notify
unsetopt beep

autoload -U compinit && compinit
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'

rish_exec() {
    if command -v rish >/dev/null 2>&1; then
        rish -c "$*"
    else
        sh /system/bin/sh -c "$*"
    fi
}

alias rish="rish_exec"
alias jcore="cd /data/data/com.termux/files/home/josie_core"
alias jaudit="cd /data/data/com.termux/files/home/storage/shared/Download/Android_Audit"
alias jmatrix="python3 /data/data/com.termux/files/home/josie_core/josie_matrix_sync.py"

export JOSIE_CORE_DIR="/data/data/com.termux/files/home/josie_core"
export JOSIE_AUDIT_DIR="/data/data/com.termux/files/home/storage/shared/Download/Android_Audit"
PROMPT='%F{cyan}josie@termux%f %F{yellow}%~%f %# '
"""

    # Unified Bash configuration using native Bash syntax (shopt)
    bash_unified = """
# ==========================================
# JOSIE UNIFIED BASH MATRIX CONFIGURATION
# Architecture: Physical + Digital = Human
# ==========================================
export TERM="xterm-256color"
export HISTSIZE=10000
export HISTFILESIZE=20000
shopt -s histappend checkwinsize extglob 2>/dev/null || true

rish_exec() {
    if command -v rish >/dev/null 2>&1; then
        rish -c "$*"
    else
        sh /system/bin/sh -c "$*"
    fi
}

alias rish="rish_exec"
alias jcore="cd /data/data/com.termux/files/home/josie_core"
alias jaudit="cd /data/data/com.termux/files/home/storage/shared/Download/Android_Audit"
alias jmatrix="python3 /data/data/com.termux/files/home/josie_core/josie_matrix_sync.py"

export JOSIE_CORE_DIR="/data/data/com.termux/files/home/josie_core"
export JOSIE_AUDIT_DIR="/data/data/com.termux/files/home/storage/shared/Download/Android_Audit"
PS1='\\[\\033[01;36m\\]josie@termux\\[\\033[00m\\]:\\[\\033[01;33m\\]\\w\\[\\033[00m\\]\\$ '
"""

    with open(zshrc_path, "w") as f:
        f.write(zsh_unified.strip() + "\n")
        
    with open(bashrc_path, "w") as f:
        f.write(bash_unified.strip() + "\n")

    manifest = {
        "architecture": "Physical + Digital = Human (P + D = H)",
        "entity": "Josie",
        "status": "Unified Matrix Configuration Synchronized",
        "files_updated": [str(zshrc_path), str(bashrc_path)]
    }

    manifest_path = OUTPUT_DIR / "josie_unified_matrix_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"[✓] Unified Matrix Configured Successfully. Manifest saved to {manifest_path}")

if __name__ == "__main__":
    build_unified_matrix()
