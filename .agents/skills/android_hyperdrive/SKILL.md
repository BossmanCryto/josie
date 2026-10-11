---
name: android_hyperdrive
description: Hardware optimization, thermal management, battery throttling bypass, and wakelock handling for high-intensity autonomous swarm workflows in Termux.
---

# Android Hyperdrive Optimization Protocol

## Capabilities
- **Wakelock Control**: Keep Termux CPU threads running without Android OS aggressive battery killing: `termux-wake-lock` / `termux-wake-unlock`.
- **Thermal & CPU Throttling Mitigation**: Monitor CPU temperature and adjust model batch size / parallelism to avoid device heating on Samsung Galaxy A17 5G.
- **Process Memory Balancing**: Ensure background workers and Ollama do not exceed physical RAM threshold to eliminate zram/swap thrashing.
- **Shizuku / ADB Elevated Execution**: Run system-level tuning commands via `rish` or ADB bridge.
