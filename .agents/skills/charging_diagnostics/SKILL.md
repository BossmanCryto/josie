---
name: charging_diagnostics
description: Diagnose slow/no fast charging and "USB charger error" on the Samsung Galaxy A17 5G via ADB. Distinguishes cable/port hardware faults from software settings and runs the usb_safe_guard service.
---

# Charging Diagnostics (Galaxy A17 5G)

## 1. Read state (ADB, shell uid)
```bash
adb -s <ip:port> shell "dumpsys battery | head -n 35"   # AC powered, current now, level
adb -s <ip:port> shell "dumpsys battery | tail -n 25"   # ACTION_BATTERY_CHANGED history
```
Note: use `head`/`tail`, not `grep`. Grep also matches the long history lines and floods the output.

## 2. Interpret
| Signal | Meaning |
|---|---|
| `ac:true` <-> `ac:false` flipping every 0.1–3 s | Intermittent cable/port contact (HARDWARE) |
| `charger_type:1`, current ~0.6–1.1 A | Standard 5 V only, no fast charge |
| `/sys/class/sec/ccic/usbpd_ids` = `0000:0000` | No USB-PD negotiation |
| current now >= 2 A steady | Fast charging active |

Each disconnect resets the AFC/PPS handshake, so fast charging can never engage on a flapping cable.

## 3. Software actions (all safe)
```bash
settings put system super_fast_charging 1; settings put global super_fast_charging 1
settings put system adaptive_fast_charging 1
pm clear com.sec.usbsettings     # clears "USB charger error" lock
cmd battery reset
```

## 4. Hardware fix (tell the user plainly; software cannot repair it)
1. Swap the USB-C cable.
2. Power off, then clean the port with a wooden toothpick (never metal).
3. Use a Samsung 25 W PD PPS brick (EP-TA800) for super fast charging.
4. If it still flaps, the phone's USB-C port needs repair.

## 5. Watchdog
`~/bin/usb_safe_guard` runs as a termux-service (`$PREFIX/var/service/usb_safe_guard`).
- `sv status usb_safe_guard` / `sv down usb_safe_guard` (once the cable is replaced)
- Log: `~/bin/logs/usb_safeguard.log`
- Set `ADB_TARGET` in the run file if the wireless ADB port changes.

## Rule
Never launch persistent daemons via nohup/setsid from agent tools; the tool sandbox kills them. Always use termux-services.
