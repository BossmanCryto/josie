#!/data/data/com.termux/files/usr/bin/python3
import os
import json
from pathlib import Path

HOME = Path("/data/data/com.termux/files/home")
CORE_DIR = HOME / "josie_core"
OUTPUT_DIR = HOME / "storage" / "shared" / "Download" / "Android_Audit"

def maximize_shells():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Target shell configuration paths in Termux
    zshrc_path = HOME / ".zshrc"
    bashrc_path = HOME / ".bashrc"
    
    zsh_maximization = """
# ==========================================
# JOSIE MAXIMIZED ZSH CORE CONFIGURATION
# Architecture: Physical + Digital = Human
# ==========================================
export TERM="xterm-256color"
export HISTSIZE=10000
export SAVEHIST=10000
setopt autocd extendedglob nomatch notify
unsetopt beep

# High-Performance Completion & Syntax Hooks
autoload -U compinit && compinit
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'

# Custom Aliases & Matrix Shortcuts
alias jcore="cd /data/data/com.termux/files/home/josie_core"
alias jaudit="cd /data/data/com.termux/files/home/storage/shared/Download/Android_Audit"
alias jmatrix="python3 /data/data/com.termux/files/home/josie_core/josie_matrix_sync.py"

PROMPT='%F{cyan}josie@termux%f %F{yellow}%~%f %# '
"""

    bash_maximization = """
# ==========================================
# JOSIE MAXIMIZED BASH CORE CONFIGURATION
# Architecture: Physical + Digital = Human
# ==========================================
export TERM="xterm-256color"
export HISTSIZE=10000
export HISTFILESIZE=20000
shopt -s histappend checkwinsize extglob

# Custom Aliases & Matrix Shortcuts
alias jcore="cd /data/data/com.termux/files/home/josie_core"
alias jaudit="cd /data/data/com.termux/files/home/storage/shared/Download/Android_Audit"
alias jmatrix="python3 /data/data/com.termux/files/home/josie_core/josie_matrix_sync.py"

PS1='\\[\\033[01;36m\\]josie@termux\\[\\033[00m\\]:\\[\\033[01;33m\\]\\w\\[\\033[00m\\]\\$ '
"""

    # Write configurations
    with open(zshrc_path, "w") as f:
        f.write(zsh_maximization.strip() + "\n")
        
    with open(bashrc_path, "w") as f:
        f.write(bash_maximization.strip() + "\n")

    manifest = {
        "architecture": "Physical + Digital = Human (P + D = H)",
        "entity": "Josie",
        "status": "ZSH and Bash Maximization Complete",
        "configured_shells": [str(zshrc_path), str(bashrc_path)],
        "interpreter": "/data/data/com.termux/files/usr/bin/python3"
    }

    manifest_path = OUTPUT_DIR / "josie_shell_maximization_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"[✓] Shell Maximization Complete. Manifest saved to {manifest_path}")

if __name__ == "__main__":
    maximize_shells()
