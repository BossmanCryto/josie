#!/data/data/com.termux/files/usr/bin/bash
# ============================================================
# TERMUX GITHUB COMPLETE SETUP - ALL-IN-ONE MASTER SCRIPT
# ============================================================

set -e
export GH_PROMPT_DISABLED=1
WORKSPACE="$HOME/github"
LIST="$HOME/gh-repos.txt"

echo "TERMUX GITHUB COMPLETE SETUP - ALL IN ONE"
echo ""

# PHASE 1: Installing required packages
pkg install -y git gh bash-completion nano curl

# PHASE 2: Checking GitHub authentication
if gh auth status --hostname github.com >/dev/null 2>&1; then
    echo "Already authenticated as: $(gh api user --jq .login)"
else
    echo "Not authenticated. Starting token login..."
    echo "Create a classic PAT at: https://github.com/settings/tokens/new"
    echo "Required scopes: repo, read:org, gist, workflow"
    unset GH_TOKEN GITHUB_TOKEN GH_HOST
    read -r -s -p "Paste your GitHub token: " TOKEN
    printf '\n'
    if [ -z "$TOKEN" ]; then
        echo "ERROR: No token entered. Exiting."
        exit 1
    fi
    printf '%s\n' "$TOKEN" | gh auth login --hostname github.com --git-protocol https --with-token
    unset TOKEN
    if ! gh auth status --hostname github.com >/dev/null 2>&1; then
        echo "ERROR: Login failed."
        exit 1
    fi
    echo "Authenticated as: $(gh api user --jq .login)"
fi

# PHASE 3: Configuring Git global profile
gh auth setup-git
gh config set git_protocol https --host github.com
gh config set editor nano
git config --global user.name "$(gh api user --jq .login)"
git config --global user.email "joseamonterroso1999@gmail.com"
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global core.autocrlf input

# PHASE 4: Setting up shell environment
BASHRC="$HOME/.bashrc"
touch "$BASHRC"
sed -i '/gh completion/d' "$BASHRC" 2>/dev/null || true
sed -i '/export BROWSER=/d' "$BASHRC" 2>/dev/null || true
sed -i '/# --- Termux/d' "$BASHRC" 2>/dev/null || true
cat <<'EOF' >> "$BASHRC"
# --- Termux GitHub Environment ---
export BROWSER=termux-open-url
eval "$(gh completion -s bash)"
EOF

# PHASE 5: Cloning and syncing all repositories
mkdir -p "$WORKSPACE"
cd "$WORKSPACE"
: > "$LIST"
PAGE=1
TOTAL=0
while true; do
    COUNT=$(gh repo list BossmanCryto --limit 100 --page "$PAGE" --json name --jq 'length')
    [ "$COUNT" = "0" ] && break
    gh repo list BossmanCryto --limit 100 --page "$PAGE" --json name --jq '.[].name' >> "$LIST"
    TOTAL=$((TOTAL + COUNT))
    PAGE=$((PAGE + 1))
done
echo "Found $TOTAL repositories on GitHub."
while IFS= read -r repo; do
    [ -z "$repo" ] && continue
    REPO_DIR="$WORKSPACE/$repo"
    if [ -d "$REPO_DIR/.git" ]; then
        git -C "$REPO_DIR" remote set-url origin "https://github.com/BossmanCryto/${repo}.git" 2>/dev/null || true
        git -C "$REPO_DIR" fetch origin 2>/dev/null || true
    else
        gh repo clone "BossmanCryto/$repo" "$REPO_DIR" 2>/dev/null || {
            echo "SKIP (empty remote): $repo"
            continue
        }
    fi
done < "$LIST"

# PHASE 6: Full verification
echo ""
echo "AUTHENTICATION"
gh auth status --hostname github.com 2>/dev/null | head -5
echo ""
echo "GIT CONFIGURATION"
echo "User:  $(git config --global user.name)"
echo "Email: $(git config --global user.email)"
echo "Helper: $(git config --global --get credential.https://github.com.helper | tail -1)"
echo ""
echo "REPOSITORY SYNC STATUS"
printf "%-28s %-12s %s\n" "REPO" "BRANCH" "STATE"
while IFS= read -r repo; do
    [ -d "$WORKSPACE/$repo/.git" ] || continue
    BRANCH=$(git -C "$WORKSPACE/$repo" rev-parse --abbrev-ref HEAD 2>/dev/null || echo "none")
    if [ -n "$(git -C "$WORKSPACE/$repo" status --porcelain 2>/dev/null)" ]; then
        STATE="modified"
    else
        STATE="clean"
    fi
    printf "%-28s %-12s %s\n" "$repo" "$BRANCH" "$STATE"
done < "$LIST"
echo ""
echo "ALL CHECKS PASSED"
echo "Workspace: $WORKSPACE"
echo "Repos: $TOTAL"
echo "Auth: $(gh api user --jq .login)"
echo "Protocol: HTTPS"
echo "Editor: nano"
