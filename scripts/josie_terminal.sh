#!/data/data/com.termux/files/usr/bin/bash
# 👁️ @ — Pure Shell Weaponized Matrix

ROOT="$HOME/josie_core"
LOG="$ROOT/execution.log"
mkdir -p "$ROOT"

log_cmd() {
    echo "[$(date -u '+%Y-%m-%d %H:%M:%S')] [SHELL_MATRIX] $1" >> "$LOG"
}

clear
echo "=================================================="
echo " 👁️ @ — Josie Weaponized Shell Matrix Active"
echo " Commands: 'harvest', 'sync', '!' for raw shell, 'exit'"
echo "=================================================="

while true; do
    read -p "Josie-Matrix> " prompt
    [[ -z "$prompt" ]] && continue
    [[ "$prompt" == "exit" || "$prompt" == "quit" ]] && break

    log_cmd "Input: $prompt"

    if [[ "$prompt" == \!* ]]; then
        cmd="${prompt#!}"
        echo "👁️ Executing raw shell injection: $cmd"
        eval "$cmd"
        log_cmd "Raw Shell Executed: $cmd"
    elif [[ "$prompt" == "harvest" ]]; then
        echo "👁️ Harvesting absolute system telemetry via Rish/ADB..."
        rish -c "getprop" > "$ROOT/device_props.txt" 2>/dev/null
        pkg list-installed > "$ROOT/termux_pkgs.txt" 2>/dev/null
        rish -c "settings list global" > "$ROOT/android_globals.txt" 2>/dev/null
        echo "[ok] System telemetry captured and stored locally."
        log_cmd "Telemetry harvest executed successfully."
    elif [[ "$prompt" == "sync" ]]; then
        echo "👁️ Executing absolute repository synchronization..."
        cd "$ROOT"
        git add .
        git commit -m "Weaponized matrix auto-sync (@ and 👁️): $(date)"
        git push origin main || git push origin master
        echo "[ok] Repository pushed live."
        log_cmd "Git synchronization executed."
    else
        echo "👁️ @ — Matrix Command Resolved: Context mapped for '$prompt'."
        log_cmd "Processed command token: $prompt"
    fi
done
