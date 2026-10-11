#!/data/data/com.termux/files/usr/bin/bash
# ==============================================================================
# JOSIE OS AUTONOMOUS BOOT INITIALIZER
# Executed automatically upon device boot by Termux:Boot
# ==============================================================================

# 1. Acquire Termux wake lock to prevent CPU sleep
termux-wake-lock

# 2. Add bin directories to PATH
export PATH="/data/data/com.termux/files/home/.local/bin:/data/data/com.termux/files/home/bin:$PREFIX/bin:$PATH"
export HOME="/data/data/com.termux/files/home"

# 3. Start SSH Server on Port 8022
if ! pgrep -x sshd >/dev/null 2>&1; then
    sshd
fi

# 4. Run local ADB auto-connect in background (captures rotated mDNS ports)
nohup /data/data/com.termux/files/home/bin/auto-adb > /data/data/com.termux/files/home/.auto_adb_boot.log 2>&1 &

# 5. Start Josie Guardian Sentinel Pro Daemon
nohup /data/data/com.termux/files/home/bin/josie-guardian daemon > /data/data/com.termux/files/home/.guardian_boot.log 2>&1 &

# 6. Start Unified Web Dashboard on Port 8080
if ! pgrep -f "web_app.py" >/dev/null 2>&1; then
    nohup python3 /data/data/com.termux/files/home/web_app.py > /data/data/com.termux/files/home/.webapp_boot.log 2>&1 &
fi

# 7. Start Performance Auto-Tune
if [ -f "/data/data/com.termux/files/home/bin/josie-auto-tune" ]; then
    nohup python3 /data/data/com.termux/files/home/bin/josie-auto-tune > /dev/null 2>&1 &
fi

exit 0
