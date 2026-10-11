---
name: deep_memory_vault
description: Persistent cross-session knowledge storage, cognitive logging, and SQLite memory queries for the JOSIE Swarm.
---

# Deep Memory Vault Protocol

## Operations
- **Database Location**: `/data/data/com.termux/files/home/hummie/core/josie_memory.db` and `orchestrator_state.db`.
- **Memory Querying**: Fast retrieval of historical decisions, device network topologies, and debugging fixes.
- **Vacuum & Maintenance**: Self-healing SQLite databases via `josie recover` / `hummie recover`.
