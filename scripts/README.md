# Termux GitHub Setup Scripts

All-in-one setup and management scripts for running GitHub CLI on Android via Termux.

## Quick Start

```bash
chmod +x scripts/termux-github-setup.sh
./scripts/termux-github-setup.sh
```

## What It Does

1. **Packages**: Installs git, gh, bash-completion, nano, curl
2. **Auth**: Checks existing login or prompts for PAT (hidden input)
3. **Git Config**: Sets user.name, email, default branch, credential helper
4. **Shell**: Configures ~/.bashrc with completions and browser handler
5. **Repos**: Clones/updates all repos into ~/github workspace
6. **Verify**: Prints auth status, git config, and repo sync table

## Prerequisites

- Termux from F-Droid or GitHub Releases
- GitHub Personal Access Token (classic) with repo, read:org, gist scopes

## Key Commands

```bash
gh repo list BossmanCryto --limit 50
gh repo clone BossmanCryto/<repo>
gh pr list --state open
gh issue list -R BossmanCryto/<repo>
gh release list -R BossmanCryto/<repo>
gh codespace list
gh workflow run <workflow>.yml -R BossmanCryto/<repo>
gh secret set NAME -R BossmanCryto/<repo>
gh variable set NAME --body "value" -R BossmanCryto/<repo>
gh project list --owner "@me"
gh search repos --owner BossmanCryto
gh api user --jq .login
gh auth status
```

## Running Copilot CLI on Android

Copilot CLI rejects Android directly. Use Ubuntu proot:

```bash
pkg install -y proot-distro
proot-distro install ubuntu
proot-distro login ubuntu -- bash -c '
  apt update && apt install -y curl nodejs git gh
  npm install -g @github/copilot
'
```
