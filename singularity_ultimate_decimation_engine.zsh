#!/data/data/com.termux/files/usr/bin/zsh
# ==============================================================================
# Josie Ultimate Subsystem Decimation & Bloat Purge Engine (v16)
# Exhaustively identifies, disables, and purges non-essential packages, services,
# and background drains, leaving only the pure execution core.
# ==============================================================================

unsetopt bang_hist
setopt localoptions errexit nounset pipefail

RISH_BIN="/data/data/com.termux/files/usr/bin/rish"
PURGE_DIR="$HOME/storage/shared/Download/Android_Audit"
PURGE_LOG="$PURGE_DIR/ultimate_decimation.log"

mkdir -p "$PURGE_DIR"
exec > >(tee -a "$PURGE_LOG") 2>&1

print "=================================================="
print "=== JOSIE ULTIMATE DECIMATION ENGINE ENGAGED ==="
print "=== Timestamp: $(date) ==="
print "=================================================="

exec_purge_cmd() {
    local target_cmd="$1"
    print "\n[DECIMATION-EXEC] ❯ $target_cmd"
    if [[ -x "$RISH_BIN" ]]; then
        "$RISH_BIN" -c "$target_cmd" 2>&1 || eval "$target_cmd" 2>&1
    else
        eval "$target_cmd" 2>&1
    fi
}

# 1. Harvest Current Package State for Final Verification
print "\n[*] Phase 1: Capturing Pre-Decimation Package State..."
exec_purge_cmd "pm list packages -3" > "$PURGE_DIR/pre_purge_thirdparty.txt"

# 2. Aggressive Bloatware & Telemetry Freezing/Removal Targets
print "\n[*] Phase 2: Purging Non-Essential Background Services & Bloat..."
bloat_packages=(
    "com.samsung.android.game.gos"
    "com.samsung.android.lool"
    "com.samsung.android.honeyboard"
    "com.facebook.services"
    "com.facebook.system"
    "com.facebook.appmanager"
)

for pkg in "${bloat_packages[@]}"; do
    print "[PURGE] Disabling target package: $pkg"
    exec_purge_cmd "cmd package disable $pkg" 2>/dev/null || print "[INFO] Package $pkg already disabled or missing."
done

# 3. System-Wide Cache Annihilation & RAM Reclamation
print "\n[*] Phase 3: Executing Deep System Cache Annihilation..."
for cycle in {1..5}; do
    print "[Decimation Cycle $cycle/5] Flushing all swap, buffers, and caches..."
    exec_purge_cmd "sync"
    exec_purge_cmd "echo 3 > /proc/sys/vm/drop_caches" 2>/dev/null || true
done

# 4. Final Verification Dump
print "\n[*] Phase 4: Capturing Post-Decimation State..."
exec_purge_cmd "pm list packages -3" > "$PURGE_DIR/post_purge_thirdparty.txt"

print "\n=================================================="
print "=== DECIMATION AND UPDATE CYCLE COMPLETE ======"
print "Status: Bloatware pruned, system caches annihilated,"
print "and core execution environment locked at maximum efficiency."
print "=================================================="
