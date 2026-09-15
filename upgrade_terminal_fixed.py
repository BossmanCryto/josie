import subprocess

packages = ["git", "curl", "wget", "python", "tmux", "neofetch", "proot"]

print("[*] Updating package repositories...")
subprocess.run(["pkg", "update", "-y"], check=True)

print("[*] Installing corrected foundational packages...")
for pkg in packages:
    print(f"[-] Installing {pkg}...")
    subprocess.run(["pkg", "install", pkg, "-y"], stdout=subprocess.DEVNULL)

print("[✓] Terminal core toolsets successfully normalized.")
