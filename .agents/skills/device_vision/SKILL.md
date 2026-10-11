---
name: device_vision
description: Real-time Android UI screen capture, OCR extraction, and visual element inspection via Termux/ADB.
---

# Device Vision & Screen Intelligence

## Instructions
- **Screen Capture**: Trigger visual dumps using `josie vision` or `python3 ~/josie-core/modules/agent_exec.py --screenshot`.
- **UI Element Mapping**: Use `--dump-ui` to extract XML hierarchy bounds, text nodes, and clickable coordinates.
- **Auto-Navigation**: Calculate center coordinates `(x, y)` for UI nodes and execute automated tap actions.
