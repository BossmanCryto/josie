#!/data/data/com.termux/files/usr/bin/zsh
# ==============================================================================
# Josie Master Synchronization & Unified Execution Engine
# Target: Termux / Rish / Zsh / Android Environment
# ==============================================================================

unsetopt bang_hist
setopt localoptions errexit nounset pipefail

ROOT="$HOME/josie_core"
AUDIT_DIR="$HOME/storage/shared/Download/Android_Audit"
LOG_FILE="$ROOT/master_rebuild.log"

mkdir -p "$ROOT" "$AUDIT_DIR"
exec > >(tee -a "$LOG_FILE") 2>&1

print "=================================================="
print "=== JOSIE MASTER REBUILD & SYNCHRONIZATION ==="
print "=== Timestamp: $(date) ==="
print "=================================================="

# 1. Verify Privilege Bridge (Rish / Local Fallback)
run_action() {
    local target_cmd="$1"
    print "\n[EXEC] ❯ $target_cmd"
    
    if command -v rish >/dev/null 2>&1; then
        if rish -c "$target_cmd"; then
            print "[SUCCESS] Executed via Rish."
            return 0
        fi
    fi

    if eval "$target_cmd"; then
        print "[SUCCESS] Executed locally."
        return 0
    else
        local code=$?
        print "[ERROR] Failed with exit code $code."
        return $code
    fi
}

# 2. Execute Full System Healing & Optimization
print "\n[*] Step 1: Flushing and resetting keyboard subsystems..."
run_action "cmd package clear com.google.android.inputmethod.latin"
run_action "cmd package clear com.samsung.android.honeyboard"

print "\n[*] Step 2: Generating complete package map..."
if command -v rish >/dev/null 2>&1; then
    rish -c "cmd package list packages -f" > "$AUDIT_DIR/complete_package_map.txt"
else
    cmd package list packages -f > "$AUDIT_DIR/complete_package_map.txt"
fi
print "[✓] Package map saved to $AUDIT_DIR/complete_package_map.txt"

print "\n[*] Step 3: Packaging workspace state into portable Base64 payload..."
tar czf - -C "$HOME" josie_core | base64 > "$HOME/storage/shared/Download/josie_payload.b64"
print "[✓] Payload generated: $HOME/storage/shared/Download/josie_payload.b64"

print "\n=================================================="
print "=== MASTER REBUILD COMPLETED SUCCESSFULLY (EXIT: 0) ==="
print "=================================================="
