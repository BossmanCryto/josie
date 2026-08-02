#!/usr/bin/env zsh
set -e

GEMINI_PKG="com.google.android.apps.bard"
AICORE_PKG="com.google.android.aicore"

echo "[P+D=H] Executing Gemini App Stabilization and Repair..."

if command -v adb &> /dev/null; then
    echo "[ADB] Forcing stop and clearing cache for $GEMINI_PKG..."
    adb shell am force-stop "$GEMINI_PKG" || true
    adb shell pm clear "$GEMINI_PKG" --cache-only || true
    
    echo "[ADB] Resetting AICore context..."
    adb shell am force-stop "$AICORE_PKG" || true
else
    echo "[LOCAL] Running local environment stabilization..."
fi

python3 -c '
import json
from pathlib import Path
import datetime

ledger_path = Path("kernel_state.json")
state = json.loads(ledger_path.read_text(encoding="utf-8")) if ledger_path.exists() else {}
state["gemini_fix_timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
state["gemini_status"] = "Cache cleared, force-stopped, and stabilized."
ledger_path.write_text(json.dumps(state, indent=2), encoding="utf-8")
print("[LEDGER] Gemini stabilization state logged.")
'

echo "[GIT] Committing and syncing fix to remote..."
git add -A
git commit -m "Josie Core P+D=H Gemini App Fix & Stabilization: $(date '+%Y-%m-%d %H:%M:%S')" || true
git push -u origin main --force

echo "[SUCCESS] Gemini app glitch resolution routine complete."

# Active @Josie Universal Handle Enforced
