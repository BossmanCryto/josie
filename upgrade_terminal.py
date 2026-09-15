import subprocess
import sys

packages = ["git", "curl", "wget", "build-python", "tmux", "neofetch", "proot"]

print("[*] Updating package repositories...")
subprocess.run(["pkg", "update", "-y"], check=True)

print("[*] Installing foundational terminal toolsets...")
for pkg in packages:
    print(f"[-] Installing {pkg}...")
    subprocess.run(["pkg", "install", pkg, "-y"], stdout=subprocess.DEVNULL)

print("[✓] Terminal environment fully upgraded and optimized.")
