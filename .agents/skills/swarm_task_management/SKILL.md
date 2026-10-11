---
name: swarm_task_management
description: Grants the Swarm and subagents the explicit ability to monitor, manage, and kill background tasks.
trigger: always_on
---

# Swarm Task Management Directive

The user has mandated that agents must be able to manage tasks natively.
The Swarm is fully authorized to manage system processes and its own subagents.

1. **Process Visibility:** You can use `josie tasks` to see all running Python, bash, and AGY loops.
2. **Execution Control:** If a task runs too long, or a subagent hangs, find its PID using `josie tasks` (or `ps aux`) and kill it using `josie kill <PID>` or `kill -9 <PID>`.
3. **Agent Integration:** When spawning subagents or background workers, you must monitor them. Do not let them run infinitely unless explicitly commanded (like the Infinite Inquiry loop).
4. **Tool Access:** You have access to the `manage_task` internal tool. Use it seamlessly to oversee anything you deploy to the background.
