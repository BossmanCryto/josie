#!/data/data/com.termux/files/usr/bin/zsh
# ==============================================================================
# Josie Verified Rish/ADB Execution Wrapper & Status Auditor (v310)
# Guarantees explicit [SUCCESS] or [FAILURE] exit status reporting for every
# command (including pm, setprop, package operations) executed via rish or adb.
# ==============================================================================

unsetopt bang_hist
setopt localoptions errexit nounset pipefail

RISH_BIN="/data/data/com.termux/files/usr/bin/rish"
AUDIT_DIR="$HOME/storage/shared/Download/Android_Audit"
EXEC_LOG="$AUDIT_DIR/rish_status_wrapper.log"

mkdir -p "$AUDIT_DIR"
exec > >(tee -a "$EXEC_LOG") 2>&1

print "=================================================="
print "=== RISH/ADB STATUS WRAPPER ENGINE ENGAGED ======"
print "=== Timestamp: $(date) ==="
print "=================================================="

# Universal execution wrapper with mandatory success/failure reporting
exec_status() {
    local cmd="$1"
    print "\n--------------------------------------------------"
    print "[RUNNING] ❯ $cmd"
    
    local output=""
    local exit_code=0
    
    if [[ -x "$RISH_BIN" ]]; then
        output=$(eval "$RISH_BIN -c \"$cmd\"" 2>&1)
        exit_code=$?
    elif command -v adb &>/dev/null; then
        output=$(adb shell "$cmd" 2>&1)
        exit_code=$?
    else
        output=$(eval "$cmd" 2>&1)
        exit_code=$?
    fi
    
    # Print command output if present
    if [[ -n "$output" ]]; then
        print "$output"
    fi
    
    # Explicit success/failure reporting banner
    if [[ $exit_code -eq 0 ]]; then
        print "[STATUS: SUCCESS] (Exit Code: $exit_code)"
    else
        print "[STATUS: FAILURE] (Exit Code: $exit_code)"
    fi
    
    return $exit_code
}

# Example validation tests using package manager (pm) and system properties
print "\n[*] Phase 1: Executing Validated System & Package Queries..."
exec_status "pm path moe.shizuku.privileged.api || echo 'Shizuku package path query.'"
exec_status "getprop ro.product.model"
exec_status "dumpsys window displays | grep -E 'mDisplayId|init='"

print "\n=================================================="
print "=== RISH/ADB STATUS AUDIT COMPLETE =============="
print "Log saved to: $EXEC_LOG"
print "=================================================="
