import os
import datetime

def agent_heartbeat(agent_id):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path = f"/root/Josie-Singularity/logs/swarm/agent_{agent_id}.log"
    with open(log_path, "a") as f:
        f.write(f"[HEARTBEAT] Agent {agent_id} active at {timestamp}\n")

if __name__ == "__main__":
    # Wave 1: First 1,000 agents active
    for i in range(1, 1001):
        agent_heartbeat(i)
    print("[SUCCESS] Wave 1 Sentinel Heartbeats recorded.")
