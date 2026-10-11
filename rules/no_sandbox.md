
# NO SANDBOX EVER

User directive (2026-10-11): "no sandbox ever".
1. Any persistent or background work (watchdogs, daemons, monitors) must run on the real system, not as a chat-session-bound task.
2. Install long-running jobs as termux-services: `$PREFIX/var/service/<name>/run` (+ `log/run` with svlogd). `runsvdir` is already running.
3. Do not rely on `nohup`/`setsid`/`&` from agent tool calls; the tool sandbox kills those children.
4. Verify with `sv status <name>` before reporting done.
