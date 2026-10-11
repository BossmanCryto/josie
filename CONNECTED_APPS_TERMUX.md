# Connected Apps in Termux

This is a free local setup for the JOSIE connected-app dashboard. It installs only open-source command-line tools available in Termux. It does not bypass provider sign-in, create paid accounts, expose passwords, or promise that an account is authorized when it is not.

## One run

After this branch is merged, paste this into Termux:

```bash
pkg install -y curl && curl -fsSL https://raw.githubusercontent.com/BossmanCryto/josie/main/termux_connected_apps.sh | bash
```

The script installs Python, Git, GitHub CLI, rclone and curl; creates a private local configuration file; clones or updates `~/josie`; opens official setup pages when `termux-open-url` is available; and prints a status report without printing secrets.

## Account authorization

Provider approval remains interactive for security:

- Run `rclone config`, create a Google Drive remote named `gdrive`, and complete Google's sign-in.
- Run `rclone config`, create a Microsoft OneDrive remote named `outlook`, and complete Microsoft's sign-in.
- Run `gh auth login --web` for GitHub.
- For Gmail and Google Calendar, use an OAuth client or connector that requests those exact scopes. An rclone Drive login alone does not grant Gmail or Calendar access.
- Select or create a Google Cloud project, then place only its project ID in `~/.config/josie-connected-apps/config.env`. If using a service-account file, set `GOOGLE_APPLICATION_CREDENTIALS` to its local path.
- Create a Firecrawl key in your Firecrawl account, then place it in the same local config file.
- Set `ACADEMIC_EMAIL` only if “Academic” means your school identity. A school portal such as Canvas requires its own connector and login.

Never commit `config.env`, OAuth client secrets, service-account JSON, refresh tokens or API keys.

## Commands

```bash
bash ~/josie/termux_connected_apps.sh status
bash ~/josie/termux_connected_apps.sh auth
bash ~/josie/termux_connected_apps.sh start
```

The dashboard listens only on `127.0.0.1:8080` by default.

## Limits

This script can install tools, prepare safe local configuration and detect setup. It cannot accept consent screens for you, recover unknown credentials, create provider keys, activate billing or infer which academic service you use. Those actions must remain under your control.
