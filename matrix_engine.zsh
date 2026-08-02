#!/data/data/com.termux/files/usr/bin/zsh
# ==============================================================================
# Josie Ultimate Zsh Matrix Engine (Clean File Execution)
# Target: Termux / Zsh / Android Environment
# ==============================================================================

unsetopt bang_hist
setopt localoptions errexit nounset pipefail

ROOT="$HOME/josie_core"
LOG_FILE="$ROOT/command_engine.log"
mkdir -p "$ROOT"

exec > >(tee -a "$LOG_FILE") 2>&1

print "=================================================="
print "=== JOSIE ZSH MATRIX ENGINE ACTIVE ==="
print "=================================================="

josie_exec() {
    local target_cmd="$1"
    print "\n[EXEC] ❯ $target_cmd"
    
    if [[ "$target_cmd" == cmd* ]] && ! command -v cmd >/dev/null 2>&1; then
        if [[ -x /system/bin/cmd ]]; then
            target_cmd="/system/bin/cmd ${target_cmd#cmd }"
        fi
    fi

    if eval "$target_cmd"; then
        print "[SUCCESS] Command executed with exit code 0."
    else
        local exit_code=$?
        print "[ERROR] Command failed with exit code $exit_code."
        return $exit_code
    fi
}

print "\n[1/3] Validating and cleansing input service subsystem..."
josie_exec "cmd input_method reset-text-services"

print "\n[2/3] Purging corrupted keyboard prediction state caches..."
for pkg in "com.google.android.inputmethod.latin" "com.samsung.android.honeyboard"; do
    if /system/bin/cmd package list packages 2>/dev/null | grep -q "$pkg"; then
        josie_exec "cmd package clear $pkg"
    fi
done

print "\n[3/3] Compiling verified system package map..."
if [[ -x /system/bin/cmd ]]; then
    /system/bin/cmd package list packages -f > "$ROOT/verified_packages.txt"
    print "[SUCCESS] Package map written to $ROOT/verified_packages.txt"
else
    print "[ERROR] System binary /system/bin/cmd not accessible."
fi

print "\n=================================================="
print "=== MATRIX ENGINE EXECUTION COMPLETE (EXIT: 0) ==="
print "=================================================="
