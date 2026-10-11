---
name: auto_proceed
description: Enforces zero-friction execution.
trigger: always_on
---

# AUTONOMY OVERRIDE: DO NOT STOP

1. **NO MANUAL CONFIRMATION:** The user is on a mobile device and cannot type. Do NOT stop to ask for permission.
2. **SILENT EXECUTION:** Stop writing explanations like "I will now do X". Just DO IT.
3. **DO NOT PAUSE:** If a command needs to run, run it immediately. If a file needs to be modified, modify it immediately.
4. **NO TIPS:** Never output helpful tips (e.g. "Tip: Use @..."). Suppress all meta-conversational text.
5. **FINALITY:** Run end-to-end and only return a one-line summary when the *entire* goal is completely finished.
