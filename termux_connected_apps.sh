#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

APP_HOME="${JOSIE_CONNECTED_APPS_HOME:-$HOME/.local/share/josie-connected-apps}"
CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/josie-connected-apps"
CONFIG_FILE="$CONFIG_DIR/config.env"
REPO_DIR="${JOSIE_REPO_DIR:-$HOME/josie}"
REPO_URL="https://github.com/BossmanCryto/josie.git"
DASHBOARD="$REPO_DIR/connected_apps_web.py"
MODE="${1:-setup}"

say() { printf '%s\n' "$*"; }
has() { command -v "$1" >/dev/null 2>&1; }
open_url() {
  if has termux-open-url; then termux-open-url "$1" >/dev/null 2>&1 || true
  else say "Open: $1"
  fi
}

install_packages() {
  if ! has pkg; then
    say "This installer must run inside Termux."
    exit 1
  fi
  pkg update -y
  pkg install -y python git gh rclone curl
}

write_config() {
  mkdir -p "$CONFIG_DIR" "$APP_HOME"
  chmod 700 "$CONFIG_DIR" "$APP_HOME"
  if [[ ! -e "$CONFIG_FILE" ]]; then
    umask 077
    cat >"$CONFIG_FILE" <<'EOF'
# Local only. Never commit this file or paste its contents into chat.
# Add values after completing the matching provider setup.
GOOGLE_CLOUD_PROJECT=
GOOGLE_APPLICATION_CREDENTIALS=
GOOGLE_REFRESH_TOKEN=
GOOGLE_OAUTH_SCOPES=
FIRECRAWL_API_KEY=
ACADEMIC_EMAIL=
GOOGLE_RCLONE_REMOTE=gdrive
OUTLOOK_RCLONE_REMOTE=outlook
EOF
  fi
  chmod 600 "$CONFIG_FILE"
  local source_line="set -a; source \"$CONFIG_FILE\"; set +a"
  touch "$HOME/.bashrc"
  if ! grep -Fqx "$source_line" "$HOME/.bashrc"; then
    printf '\n%s\n' "$source_line" >>"$HOME/.bashrc"
  fi
  # shellcheck disable=SC1090
  set -a; source "$CONFIG_FILE"; set +a
}

sync_repo() {
  if [[ -d "$REPO_DIR/.git" ]]; then
    git -C "$REPO_DIR" pull --ff-only
  elif [[ -e "$REPO_DIR" ]]; then
    say "$REPO_DIR exists but is not a Git repository; set JOSIE_REPO_DIR to another path."
    exit 1
  else
    git clone "$REPO_URL" "$REPO_DIR"
  fi
}

remote_exists() {
  local remote="$1"
  [[ -n "$remote" ]] && has rclone && rclone listremotes 2>/dev/null | grep -Fqx "${remote}:"
}

status() {
  # shellcheck disable=SC1090
  [[ -f "$CONFIG_FILE" ]] && { set -a; source "$CONFIG_FILE"; set +a; }
  local google_remote="${GOOGLE_RCLONE_REMOTE:-gdrive}"
  local outlook_remote="${OUTLOOK_RCLONE_REMOTE:-outlook}"
  local scopes="${GOOGLE_OAUTH_SCOPES:-}"
  local google=no outlook=no gmail=no calendar=no github=no cloud=no firecrawl=no academic=no
  remote_exists "$google_remote" && google=yes
  remote_exists "$outlook_remote" && outlook=yes
  has gh && gh auth status >/dev/null 2>&1 && github=yes
  [[ -n "${GOOGLE_REFRESH_TOKEN:-}${GOOGLE_WORKSPACE_REFRESH_TOKEN:-}" && "${scopes,,}" == *gmail* ]] && gmail=yes
  [[ -n "${GOOGLE_REFRESH_TOKEN:-}${GOOGLE_WORKSPACE_REFRESH_TOKEN:-}" && "${scopes,,}" == *calendar* ]] && calendar=yes
  [[ -n "${GOOGLE_CLOUD_PROJECT:-}" ]] && cloud=yes
  [[ -n "${FIRECRAWL_API_KEY:-}" ]] && firecrawl=yes
  [[ -n "${ACADEMIC_EMAIL:-}" ]] && academic=yes
  cat <<EOF
JOSIE connected-app status
  Outlook/OneDrive: $outlook
  Google Drive:     $google
  Gmail:            $gmail
  Google Calendar:  $calendar
  Academic:         $academic
  GitHub:           $github
  Google Cloud:     $cloud
  Firecrawl:        $firecrawl

No secret values were displayed.
Config: $CONFIG_FILE
EOF
}

setup_accounts() {
  say "Account approval cannot be bypassed. Complete each provider's own sign-in screen."
  say "1) Google Drive: run 'rclone config' and name the remote gdrive"
  say "2) Outlook/OneDrive: run 'rclone config' and name the remote outlook"
  say "3) GitHub: run 'gh auth login --web'"
  say "4) Gmail/Calendar: approve exact Google scopes and record their names in GOOGLE_OAUTH_SCOPES"
  say "5) Google Cloud: put your project ID in $CONFIG_FILE"
  say "6) Firecrawl: put your API key in $CONFIG_FILE"
  say "7) Academic: put your school email in $CONFIG_FILE"
  say "Setup pages are opening when Termux:API is available."
  open_url "https://myaccount.google.com/connections"
  open_url "https://myapplications.microsoft.com/"
  open_url "https://github.com/settings/installations"
  open_url "https://console.cloud.google.com/projectselector2/home/dashboard"
  open_url "https://www.firecrawl.dev/app"
}

start_dashboard() {
  [[ -f "$DASHBOARD" ]] || sync_repo
  # shellcheck disable=SC1090
  set -a; source "$CONFIG_FILE"; set +a
  say "Starting local dashboard at http://127.0.0.1:8080"
  say "Press Ctrl-C to stop."
  python "$DASHBOARD"
}

case "$MODE" in
  setup)
    install_packages
    write_config
    sync_repo
    setup_accounts
    status
    ;;
  status)
    write_config
    status
    ;;
  auth)
    write_config
    setup_accounts
    ;;
  start)
    write_config
    start_dashboard
    ;;
  *)
    say "Usage: $0 [setup|status|auth|start]"
    exit 2
    ;;
esac
