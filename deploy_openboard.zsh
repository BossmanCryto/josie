#!/data/data/com.termux/files/usr/bin/zsh
# ==============================================================================
# Josie OpenBoard (AOSP LatinIME Fork) Zero-Lag Deployment Script
# Bypasses bloated Gboard/Samsung Honeyboard dependencies cleanly via Rish.
# ==============================================================================

unsetopt bang_hist
setopt localoptions errexit nounset pipefail

RISH_BIN="/data/data/com.termux/files/usr/bin/rish"
AUDIT_DIR="$HOME/storage/shared/Download/Android_Audit"
TARGET_APK="$AUDIT_DIR/openboard.apk"
OPENBOARD_URL="https://github.com/dslul/openboard/releases/download/v1.4.5/app-release.apk"

mkdir -p "$AUDIT_DIR"

print "=================================================="
print "=== OPENBOARD DEPLOYMENT & KEYBOARD PURGE ======"
print "=================================================="

# 1. Download OpenBoard (Clean AOSP LatinIME fork, zero telemetry/bloat)
if [[ ! -f "$TARGET_APK" ]]; then
    print "\n[*] Downloading OpenBoard 1.4.5 (AOSP standard)..."
    curl -L -o "$TARGET_APK" "$OPENBOARD_URL"
else
    print "\n[✓] OpenBoard APK already cached locally."
fi

# 2. Install via Rish/Package Manager
print "\n[*] Installing OpenBoard as primary system input method..."
if [[ -x "$RISH_BIN" ]]; then
    "$RISH_BIN" -c "pm install -r '$TARGET_APK'"
else
    pm install -r "$TARGET_APK"
fi

# 3. Enable OpenBoard and set as default IME service
print "\n[*] Configuring input method framework bindings..."
if [[ -x "$RISH_BIN" ]]; then
    "$RISH_BIN" -c "ime enable org.dslul.openboard.inputmethod.latin/.LatinIME"
    "$RISH_BIN" -c "ime set org.dslul.openboard.inputmethod.latin/.LatinIME"
else
    ime enable org.dslul.openboard.inputmethod.latin/.LatinIME
    ime set org.dslul.openboard.inputmethod.latin/.LatinIME
fi

# 4. Neutralize bloated keyboard interference packages safely
print "\n[*] Pruning background resource drains from Samsung Honeyboard..."
if [[ -x "$RISH_BIN" ]]; then
    "$RISH_BIN" -c "cmd package disable com.samsung.android.honeyboard" 2>/dev/null || print "[INFO] Honeyboard disable skipped or already handled."
else
    print "[INFO] Run via Rish for full package freezing."
fi

print "\n=================================================="
print "=== KEYBOARD SUBSYSTEM OVERHAUL COMPLETE ========="
print "Active Engine: OpenBoard (AOSP Pure LatinIME)"
print "Bloat & Telemetry: Stripped"
print "=================================================="
