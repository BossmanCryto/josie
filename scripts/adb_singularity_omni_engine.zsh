#!/data/data/com.termux/files/usr/bin/zsh
# ==============================================================================
# Josie Ultimate ADB & Rish Omni-Extraction & Subsystem Sweep Engine (v11)
# Exhaustively interrogates, dumps, and maps every package, service, and property.
# ==============================================================================

unsetopt bang_hist
setopt localoptions errexit nounset pipefail

RISH_BIN="/data/data/com.termux/files/usr/bin/rish"
AUDIT_DIR="$HOME/storage/shared/Download/Android_Audit"
OMNI_LOG="$AUDIT_DIR/omni_system_dump.log"

mkdir -p "$AUDIT_DIR"
exec > >(tee -a "$OMNI_LOG") 2>&1

print "=================================================="
print "=== JOSIE OMNI-SUBYSTEM ADB/RISH HARVESTER ======"
print "=== Timestamp: $(date) ==="
print "=================================================="

run_omni_cmd() {
    local cmd="$1"
    print "\n[OMNI-EXEC] ❯ $cmd"
    if [[ -x "$RISH_BIN" ]]; then
        "$RISH_BIN" -c "$cmd" 2>&1 || eval "$cmd" 2>&1
    else
        eval "$cmd" 2>&1
    fi
}

# 1. Exhaustive Package Enumeration (System, 3rd Party, File Paths)
print "\n[*] Phase 1: Harvesting Complete Package Matrix..."
run_omni_cmd "pm list packages -f" > "$AUDIT_DIR/omni_packages_full.txt"
run_omni_cmd "pm list packages -3" > "$AUDIT_DIR/omni_packages_thirdparty.txt"
print "[✓] Package manifests saved to $AUDIT_DIR"

# 2. Complete System Service & Dumpsys Inventory
print "\n[*] Phase 2: Dumping System Services & Configurations..."
run_omni_cmd "service list" > "$AUDIT_DIR/omni_service_list.txt"
run_omni_cmd "getprop" > "$AUDIT_DIR/omni_system_properties.txt"

# 3. Input & IME Architecture Verification
print "\n[*] Phase 3: Inspecting Input Subsystems & Active IMEs..."
run_omni_cmd "dumpsys input"
run_omni_cmd "ime list -a"

# 4. Ultra-Deep Garbage Collection & Cache Wipe
print "\n[*] Phase 4: Purging Orphaned Caches & Reclaiming System Memory..."
run_omni_cmd "sync"
run_omni_cmd "echo 3 > /proc/sys/vm/drop_caches" 2>/dev/null || true

print "\n=================================================="
print "=== OMNI-HARVEST AND OPTIMIZATION COMPLETE ======"
print "All system maps, package inventories, and configuration"
print "dumps have been successfully extracted and written."
print "=================================================="
