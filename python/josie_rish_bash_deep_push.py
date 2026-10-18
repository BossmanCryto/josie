#!/data/data/com.termux/files/usr/bin/python3
"""Install a small Rish wrapper without aliases, recursion, or silent fallback."""
from __future__ import annotations

import json
import os
from pathlib import Path

DEFAULT_HOME = Path("/data/data/com.termux/files/home")
HOME = Path(os.environ.get("JOSIE_HOME", str(DEFAULT_HOME))).expanduser()
OUTPUT_DIR = Path(os.environ.get("JOSIE_OUTPUT_DIR", str(HOME / "storage/shared/Download/Android_Audit"))).expanduser()
START_MARKER = "# >>> JOSIE RISH BRIDGE >>>"
END_MARKER = "# <<< JOSIE RISH BRIDGE <<<"

RISH_BLOCK = r'''# >>> JOSIE RISH BRIDGE >>>
# Uses a real Rish script when present, then adb-exec. It never calls itself.
rish_exec() {
    local candidate
    for candidate in "$HOME/rish" "${PREFIX:-/data/data/com.termux/files/usr}/bin/rish" "/data/local/tmp/rish"; do
        if [ -f "$candidate" ]; then
            /system/bin/sh "$candidate" -c "$*"
            return $?
        fi
    done
    if command -v adb-exec >/dev/null 2>&1; then
        adb-exec "$*"
        return $?
    fi
    echo "Rish is not installed. Export it from Shizuku, then place rish and rish_shizuku.dex in $HOME." >&2
    return 127
}
alias rish-run='rish_exec'
export JOSIE_CORE_DIR="${JOSIE_CORE_DIR:-$HOME/josie_core}"
export JOSIE_AUDIT_DIR="${JOSIE_AUDIT_DIR:-$HOME/storage/shared/Download/Android_Audit}"
# <<< JOSIE RISH BRIDGE <<<'''


def replace_managed_block(content: str) -> str:
    start = content.find(START_MARKER)
    end = content.find(END_MARKER)
    if start >= 0 and end >= start:
        end += len(END_MARKER)
        content = content[:start].rstrip() + "\n" + content[end:].lstrip("\n")
    legacy = "# JOSIE DEEP-PUSH RISH & BASH INTEGRATION"
    if legacy in content:
        lines = content.splitlines()
        kept: list[str] = []
        dropping = False
        for line in lines:
            if legacy in line:
                dropping = True
                continue
            if dropping and line.startswith("export JOSIE_AUDIT_DIR="):
                dropping = False
                continue
            if not dropping:
                kept.append(line)
        content = "\n".join(kept)
    return content.rstrip() + "\n\n" + RISH_BLOCK + "\n"


def deploy_rish_bash_extensions() -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    bashrc_path = HOME / ".bashrc"
    bashrc_path.parent.mkdir(parents=True, exist_ok=True)
    content = bashrc_path.read_text(encoding="utf-8") if bashrc_path.exists() else ""
    updated = replace_managed_block(content)
    if updated != content:
        bashrc_path.write_text(updated, encoding="utf-8")

    manifest = {
        "status": "installed",
        "target_shell": str(bashrc_path),
        "command": "rish-run '<command>'",
        "fallback": "adb-exec",
    }
    manifest_path = OUTPUT_DIR / "josie_rish_bash_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Rish bridge installed. Restart the shell or run: source {bashrc_path}")
    return manifest_path


if __name__ == "__main__":
    deploy_rish_bash_extensions()
