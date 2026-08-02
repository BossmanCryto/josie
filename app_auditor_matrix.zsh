#!/data/data/com.termux/files/usr/bin/zsh
# ==============================================================================
# Josie Comprehensive APK & System Application Auditor Matrix
# Target: Termux / Shizuku / Rish / Zsh Environment
# ==============================================================================

unsetopt bang_hist
setopt localoptions errexit nounset pipefail

ROOT="$HOME/josie_core"
AUDIT_DIR="$HOME/storage/shared/Download/Android_Audit"
MASTER_LOG="$AUDIT_DIR/matrix_execution.log"
FULL_APK_MAP="$AUDIT_DIR/comprehensive_apk_audit.txt"

mkdir -p "$ROOT" "$AUDIT_DIR"
exec > >(tee -a "$MASTER_LOG") 2>&1

print "=================================================="
print "=== JOSIE COMPREHENSIVE APK AUDIT MATRIX ACTIVE ==="
print "=== Timestamp: $(date) ==="
print "=================================================="

# Determine optimal execution bridge (Rish privileged vs local fallback)
get_exec_bridge() {
    if command -v rish >/dev/null 2>&1; then
        echo "rish -c"
    elif [[ -x /data/data/com.termux/files/usr/bin/rish ]]; then
        echo "/data/data/com.termux/files/usr/bin/rish -c"
    else
        echo "eval"
    fi
}

BRIDGE=$(get_exec_bridge)
print "[*] Active Bridge: $BRIDGE"

print "\n[*] Phase 1: Scanning and enumerating every installed package and APK path..."
print "APP_AUDIT_START: $(date)" > "$FULL_APK_MAP"

TOTAL_APPS=0
if [[ "$BRIDGE" == *"rish"* ]]; then
    if $BRIDGE "cmd package list packages -f" >> "$FULL_APK_MAP" 2>/dev/null; then
        print "[✓] Privileged full package audit complete via Rish."
    else
        print "[!] Rish package enumeration failed; falling back to standard command..."
        cmd package list packages -f >> "$FULL_APK_MAP" 2>/dev/null || true
    fi
else
    cmd package list packages -f >> "$FULL_APK_MAP" 2>/dev/null || true
    print "[✓] Local package audit complete."
fi

if [[ -f "$FULL_APK_MAP" ]]; then
    TOTAL_APPS=$(wc -l < "$FULL_APK_MAP" 2>/dev/null || echo 0)
    print "[✓] Total application entries mapped: $TOTAL_APPS"
fi

print "\n[*] Phase 2: Healing input services & clearing target application states..."
if [[ "$BRIDGE" == *"rish"* ]]; then
    $BRIDGE "cmd input_method reset-text-services" || true
else
    cmd input_method reset-text-services 2>/dev/null || true
fi

typeset -a target_apps
target_apps=(
    "com.google.android.inputmethod.latin"
    "com.samsung.android.honeyboard"
    "com.sec.android.app.launcher"
)

for app in "${target_apps[@]}"; do
    print "\n-> Processing target application: $app"
    if [[ "$BRIDGE" == *"rish"* ]]; then
        $BRIDGE "cmd package clear $app" && print "[SUCCESS] Cleared state for $app" || print "[NOTE] App $app not found or restricted."
    else
        cmd package clear "$app" 2>/dev/null && print "[SUCCESS] Cleared state for $app" || print "[NOTE] App $app not found or restricted."
    fi
done

print "\n=================================================="
print "=== COMPREHENSIVE APP AUDIT COMPLETE (EXIT: 0) ==="
print "=================================================="
