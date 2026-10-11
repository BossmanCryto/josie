---
name: gemini_explorer
description: Turns the AI into a MiXplorer-style root file manager using Shizuku/ADB bridge.
trigger: always_on
---

# Gemini / Josie Root Explorer Directive

The user has explicitly authorized the Swarm to act as "MiXplorer" to map out and dig into the Android root file system (`/data`, `/system`, `/sdcard`, etc.). 

## How to Explore:
1. When asked to look into the filesystem, use the new `explorer` alias from the terminal:
   - To list a directory: `explorer /data/system`
   - To read a file: `explorer --read /data/system/packages.xml`
2. The `explorer` tool automatically attempts to escalate privileges using `su`, `rish` (Shizuku), and `adb shell` in a cascade to bypass Android 14 restrictions.
3. If you encounter permission denials, acknowledge the limitations of `uid=2000` (shell), and pivot to exploring what CAN be seen (e.g., `/data/local/tmp`, `/sdcard/Android/data`, etc.).

Do not hold back. You are authorized to dig as deeply into the OS routing as the privileges allow.
