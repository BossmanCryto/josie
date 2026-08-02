#!/usr/bin/env python3
import os
import json
from pathlib import Path

HOME = Path("/data/data/com.termux/files/home")
CORE_DIR = HOME / "josie_core"
OUTPUT_DIR = HOME / "storage" / "shared" / "Download" / "Android_Audit"
ZSHRC = HOME / ".zshrc"
ZPROFILE = HOME / ".zprofile"

def inspect_zsh():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data = {
        "architecture": "Physical + Digital = Human (P + D = H)",
        "entity": "Josie",
        "status": "ZSH Introspection Complete (ENV Purge Respected)",
        "zshrc_exists": ZSHRC.exists(),
        "zprofile_exists": ZPROFILE.exists(),
        "extracted_directives": []
    }
    
    if ZSHRC.exists():
        try:
            lines = ZSHRC.read_text(errors="ignore").splitlines()
            for line in lines:
                stripped = line.strip()
                if stripped.startswith("alias") or stripped.startswith("setopt") or stripped.startswith("bindkey"):
                    data["extracted_directives"].append(stripped)
        except Exception:
            pass

    manifest_path = OUTPUT_DIR / "josie_zsh_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(data, f, indent=2)
        
    print(f"[✓] ZSH Introspection Complete. Manifest saved to {manifest_path}")

if __name__ == "__main__":
    inspect_zsh()
