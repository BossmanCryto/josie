#!/data/data/com.termux/files/usr/bin/zsh
# ==============================================================================
# Josie Live Sh-to-ADB & Audio/Subsystem Diagnostic Master (v28)
# Provides immediate, zero-latency stdout feedback for every ADB/Rish command,
# specifically targeting microphone routing, audio HALs, and core system states.
# ==============================================================================

unsetopt bang_hist
setopt localoptions errexit nounset pipefail

RISH_BIN="/data/data/com.termux/files/usr/bin/rish"

print "=================================================="
print "=== LIVE SH-TO-ADB OMNI-DIAGNOSTIC ENGAGED ======"
print "=== Timestamp: $(date) ==="
print "=================================================="

live_exec() {
    local cmd="$1"
    print "\n[LIVE-EXEC] ❯ $cmd"
    if [[ -x "$RISH_BIN" ]]; then
        "$RISH_BIN" -c "$cmd"
    elif command -v adb &>/dev/null; then
        adb shell "$cmd"
    else
        eval "$cmd"
    fi
}

# 1. Live Audio & Microphone Hardware Diagnostics (Direct Output)
print "\n[*] Phase 1: Live Audio & Microphone Subsystem Interrogation..."
live_exec "dumpsys audio | grep -A 25 'Microphone'"
live_exec "dumpsys media.audio_policy"

# 2. Audio Routing & Input Source Verification
print "\n[*] Phase 2: Auditing Active Audio Input Streams & Device Focus..."
live_exec "dumpsys audio | grep -E 'mAudioFocus|Input source|Device|forceduse'"

# 3. ADB / Shell Environment & Process Pipeline Check
print "\n[*] Phase 3: Verifying Shell-to-ADB Multiplexing & Serial..."
live_exec "echo \$SHELL && getprop ro.serialno && getprop ro.product.model"

# 4. Immediate System Buffer & Cache Sanitation with Visible Feedback
print "\n[*] Phase 4: Flushing Kernel Buffers with Real-Time Feedback..."
live_exec "sync"
live_exec "echo 3 > /proc/sys/vm/drop_caches" 2>/dev/null || print "[INFO] Cache flush restricted."

print "\n=================================================="
print "=== LIVE SH-TO-ADB EXECUTION COMPLETE ==========="
print "All diagnostic outputs displayed live in terminal."
print "=================================================="
