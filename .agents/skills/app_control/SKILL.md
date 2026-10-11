---
name: app_control
description: Grants the Swarm the ability to programmatically manage Android applications.
trigger: always_on
---

# Android App Control Directive

The Swarm has full authority to list, launch, and force-stop applications on the host Android device.

## Commands:
Use the `app` alias:
- **List installed apps:** `app list` (or `app list chrome` to search)
- **Launch an app:** `app launch <package_name>` (e.g., `app launch com.android.chrome`)
- **Force stop an app:** `app stop <package_name>`

When the user asks you to open an app, use `app list` to find the exact package name, then use `app launch` to execute it. Do not hesitate.
