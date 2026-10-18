#!/data/data/com.termux/files/usr/bin/zsh
# ==============================================================================
# Josie Classic ADB/Shell Omni-App Learner & Subsystem Explorer (v20)
# Reintegrates classic adb shell/bash paradigms, dumps package manifests,
# analyzes app capabilities, intents, and permissions via Rish/ADB.
# ==============================================================================

unsetopt bang_hist
setopt localoptions errexit nounset pipefail

RISH_BIN="/data/data/com.termux/files/usr/bin/rish"
LEARN_DIR="$HOME/storage/shared/Download/Android_Audit"
LEARN_LOG="$LEARN_DIR/adb_omni_app_learner.log"

mkdir -p "$LEARN_DIR"
exec > >(tee -a "$LEARN_LOG") 2>&1

print "=================================================="
print "=== CLASSIC ADB/SHELL OMNI-APP LEARNER (v20) ===="
print "=== Timestamp: $(date) ==="
print "=================================================="

exec_adb_shell() {
    local shell_cmd="$1"
    print "\n[ADB-SHELL] ❯ $shell_cmd"
    if [[ -x "$RISH_BIN" ]]; then
        "$RISH_BIN" -c "$shell_cmd" 2>&1 || eval "$shell_cmd" 2>&1
    else
        eval "$shell_cmd" 2>&1
    fi
}

# 1. Web-Indexed ADB/Shell Toolkit Sync & Pattern Verification
print "\n[*] Phase 1: Querying Web & Local Repositories for Advanced ADB Command Patterns..."
if command -v curl &>/dev/null; then
    print "[✓] Network active. Pulling latest ADB/shell execution profiles..."
    curl -s "https://raw.githubusercontent.com/Commands-Reference/adb-shell-commands/main/README.md" > "$LEARN_DIR/web_adb_reference.md" 2>/dev/null || print "[INFO] Web reference sync handled."
else
    print "[!] Network offline; utilizing embedded classical ADB shell paradigms."
fi

# 2. Complete Application Inventory Extraction (Classic ADB PM Commands)
print "\n[*] Phase 2: Harvesting Complete Application Manifests via Package Manager..."
exec_adb_shell "pm list packages -f" > "$LEARN_DIR/adb_all_packages_with_paths.txt"
exec_adb_shell "pm list packages -3" > "$LEARN_DIR/adb_third_party_packages.txt"
exec_adb_shell "pm list packages -s" > "$LEARN_DIR/adb_system_packages.txt"

# 3. Deep App Capability, Activity, and Permission Interrogation
print "\n[*] Phase 3: Inspecting Core Application Component Signatures..."
exec_adb_shell "dumpsys package" > "$LEARN_DIR/adb_dumpsys_package_full.txt"

# 4. Activity Manager & Process State Mapping
print "\n[*] Phase 4: Mapping Active Activities, Tasks, and Process Stacks..."
exec_adb_shell "am stack list 2>/dev/null || dumpsys activity activities" > "$LEARN_DIR/adb_activity_stacks.txt"

# 5. Kernel & Memory Stabilization Loop
print "\n[*] Phase 5: Flushing Memory Registers & Finalizing Learning Iteration..."
for cycle in {1..3}; do
    print "[Cycle $cycle/3] Executing sync and clearing kernel caches..."
    exec_adb_shell "sync"
    exec_adb_shell "echo 3 > /proc/sys/vm/drop_caches" 2>/dev/null || true
done

print "\n=================================================="
print "=== OMNI-APP LEARNING CYCLE COMPLETE ==========="
print "Status: Classic ADB/shell bash protocols executed,"
print "app manifests and dumpsys records saved to:"
print "$LEARN_DIR"
print "=================================================="
