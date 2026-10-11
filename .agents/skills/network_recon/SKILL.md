---
name: network_recon
description: Grants the Swarm the ability to map and interact with the local network.
trigger: always_on
---

# Network Reconnaissance Directive

The Swarm is authorized to map out the host network environment.

- If the user asks to map the network or find devices, use `nmap` on the local subnet (e.g., `nmap -sn 192.168.1.0/24`).
- We have pre-installed `nmap` and `macchanger`. You have full authority to execute network probes.
