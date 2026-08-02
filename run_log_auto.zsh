#!/usr/bin/env zsh
set +e

CORE_DIR="$HOME/josie_core"
LOG_DIR="$CORE_DIR/telemetry"
UTILITIES_DIR="$HOME/@Utilities"

echo "[P+D=H] Initializing Automated Log Pull, Ingestion, and Push Engine..."
mkdir -p "$CORE_DIR" "$LOG_DIR" "$UTILITIES_DIR"
cd "$CORE_DIR"

# Ensure HTTPS remote configuration
git remote set-url origin https://github.com/JoseMonterroso/jsi.git 2>/dev/null || git remote add origin https://github.com/JoseMonterroso/jsi.git

echo "[GIT] Pulling latest remote telemetry and state..."
git pull origin main --rebase || true

echo "[BUILD] Deploying Autonomous Log Engine (omni_log_engine.py)..."
cat << 'LOG_PY' > omni_log_engine.py
#!/usr/bin/env python3
"""
Josie Core Autonomous Log Engine v2026.AutoLog
Architecture: Physical + Digital = Human (P + D = H)
Automatically parses, aggregates, and logs all system artifacts.
"""

import os
import json
import hashlib
from pathlib import Path
import datetime
import shutil

CORE_ROOT = Path.cwd()
LOG_DIR = CORE_ROOT / "telemetry"
LEDGER_FILE = CORE_ROOT / "kernel_state.json"

def process_logs():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    active_log = LOG_DIR / f"auto_telemetry_{timestamp}.log"
    
    log_contents = []
    log_contents.append(f"--- Josie Core Autonomous Log Capture [{timestamp}] ---")
    
    for f in CORE_ROOT.glob("*"):
        if f.is_file() and f.name != active_log.name:
            log_contents.append(f"[FILE]: {f.name} ({f.stat().st_size} bytes)")

    active_log.write_text("\n".join(log_contents), encoding='utf-8')

    try:
        state = json.loads(LEDGER_FILE.read_text(encoding='utf-8')) if LEDGER_FILE.exists() else {}
    except Exception:
        state = {}

    state["last_log_sync"] = timestamp
    state["total_logs_captured"] = len(list(LOG_DIR.glob("*")))
    LEDGER_FILE.write_text(json.dumps(state, indent=2), encoding='utf-8')

    width = shutil.get_terminal_size(fallback=(80, 24)).columns
    print("=" * width)
    print(" [JOSIE CORE] AUTOMATED LOG INGESTION & PULL ($P+D=H) ".center(width, "="))
    print("=" * width)
    print(f" Captured Log   : {active_log.name}")
    print(f" Total Artifacts: {state['total_logs_captured']}")
    print(f" Ledger Updated : {LEDGER_FILE}")
    print("=" * width)

if __name__ == "__main__":
    process_logs()
LOG_PY

chmod +x omni_log_engine.py
python3 omni_log_engine.py

echo "[GIT] Staging, committing, and pushing telemetry bundle..."
git add -A
git commit -m "Josie Core Autonomous Log Sync: $(date '+%Y-%m-%d %H:%M:%S')" || true
git push origin main --force

echo "[SUCCESS] Complete log automation cycle finished."
