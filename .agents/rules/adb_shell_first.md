
# DEVICE CONTROL: ADB SHELL FIRST

User directive (2026-10-11): use `adb shell` for device work.
1. Use `adb -s <ip:port> shell ...` as the primary channel for Android device diagnostics and control (dumpsys, settings, pm, cmd, logcat).
2. `rish`/Shizuku and `termux-*` APIs are fallbacks only (rish currently returns no output).
3. Wireless ADB ports change. Pick the target with `adb devices | awk 'NR>1 && $2=="device"{print $1; exit}'` and only ask for a new ip:port if none is connected.
