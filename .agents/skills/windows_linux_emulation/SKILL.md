---
name: windows_linux_emulation
description: Run Windows apps (.exe, .msi, WineHQ) and Linux GUI desktops on Android Termux via Wine 10.0, PRoot, and Termux-X11.
trigger: always_on
---

# Windows & Linux Emulation Matrix

## Capabilities & Directives
1. **Windows Apps (WineHQ 10.0)**:
   - Use `/data/data/com.termux/files/home/bin/winrun <path/to/exe>` to execute Windows applications.
   - Automatically initializes Termux-X11 on display `:0` and runs through Debian PRoot Wine 10.0.
   - Configuration / settings: `winrun winecfg`.

2. **Linux Graphical Desktop**:
   - Use `/data/data/com.termux/files/home/bin/start-desktop` to launch the Openbox X11 desktop environment.
   - Output renders to the Termux:X11 Android app.

3. **Remote SSH Terminal Access**:
   - Diagnostic script: `/data/data/com.termux/files/home/bin/ssh-info`.
   - Access from ChromeOS, PC, or Linux: `ssh -p 8022 u0_a298@<IP>`.
