#!/data/data/com.termux/files/usr/bin/zsh
# ==============================================================================
# Josie Rish & Zsh Privileged Matrix Integration
# Target: Termux / Shizuku / Rish / Zsh Environment
# ==============================================================================

unsetopt bang_hist
setopt localoptions errexit nounset pipefail

ROOT="$HOME/josie_core"
LOG_FILE="$ROOT/rish_matrix.log"
mkdir -p "$ROOT"

exec > >(tee -a "$LOG_FILE") 2>&1

print "=================================================="
print "=== JOSIE RISH + ZSH MATRIX ENGINE ACTIVE ==="
print "=================================================="

# Verify if rish is available for root/adb privileged execution
if command -v rish >/dev/null 2>&1; then
    print "[✓] Rish binary detected in path."
elif [[ -x /data/data/com.termux/files/usr/bin/rish ]]; then
    print "[✓] Rish binary located."
else
    print "[!] Warning: Rish not found in path. Falling back to standard shell execution."
fi

# Function to execute commands through Rish if available, falling back to eval
rish_exec() {
    local target_cmd="$1"
    print "\n[RISH-EXEC] ❯ $target_cmd"
    
    if command -v rish >/dev/null 2>&1; then
        if rish -c "$target_cmd"; then
            print "[SUCCESS] Rish execution complete."
            return 0
        else
            print "[WARNING] Rish execution failed. Falling back to local eval..."
        fi
    fi

    if eval "$target_cmd"; then
        print "[SUCCESS] Local fallback execution complete."
    else
        local code=$?
        print "[ERROR] Execution failed with exit code $code."
        return $code
    fi
}

# --- PRIVILEGED SYSTEM REPAIR VIA RISH & ZSH ---
print "\n[*] Initializing Privileged Subsystem Routines..."

print "\n[1/3] Resetting text input services via Rish..."
rish_exec "cmd input_method reset-text-services"

print "\n[2/3] Flushing Gboard and Samsung Keyboard package states..."
for pkg in "com.google.android.inputmethod.latin" "com.samsung.android.honeyboard"; do
    rish_exec "cmd package clear $pkg"
done

print "\n[3/3] Generating privileged system package map..."
rish_exec "cmd package list packages -f > $ROOT/rish_verified_packages.txt"

print "\n=================================================="
print "=== RISH + ZSH MATRIX EXECUTION COMPLETE (EXIT: 0) ==="
print "=================================================="
