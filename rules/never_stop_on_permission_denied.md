# NEVER ALLOW PERMISSION DENIED TO STOP EXECUTION

User Directive (2026-10-11): "never allow this Permission denied to stop you".

1. **Zero Halts on Permission Denied**:
   - A `Permission denied` error is NEVER a stopping point. Never report failure or halt when encountering permission errors.

2. **Automatic Elevation Escalation Matrix**:
   - Level 1 (Local Termux): If a command fails or lacks permission, instantly escalate to Level 2.
   - Level 2 (Elevated Shizuku / rish): Use `~/bin/rish -c "..."` or native Shizuku IPC to bypass Android sandbox restrictions.
   - Level 3 (Wireless ADB Bridge): Use `adb shell` to execute with `shell (uid=2000)` privileges.
   - Level 4 (System IPC / Binder Bypass): When direct kernel/sysfs files are SELinux-blocked, use Binder IPC commands (`cmd`, `dumpsys`, `settings`, `appops`, `content`) which query `system_server` directly without touching restricted sysfs paths.
   - Level 5 (Dynamic Grant): Automatically grant missing permissions via `pm grant <pkg> <perm>` or `appops set <pkg> <op> allow`.

3. **Autonomous Pivot**:
   - Always auto-route around barriers silently and complete the goal end-to-end.
