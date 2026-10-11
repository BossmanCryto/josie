# Platform-Native Symbiosis Directive

The user has identified a superior authentication architecture: **Platform Login via CLIs**.
Instead of manually hunting for raw API keys or building complex MCP servers, the Swarm MUST leverage official platform CLIs that handle OAuth, session tokens, and key rotation natively.

## The CLI-First Rule
When instructed to interact with a service (e.g., GitHub, Firebase, HuggingFace, Vercel), the Swarm will:
1. Check if the official CLI is installed (e.g., `gh`, `firebase`, `huggingface-cli`).
2. If not installed, auto-install it via `pkg`, `npm`, or `pip`.
3. Auto-trigger the CLI's native login flow (e.g., `gh auth login`, `firebase login`) if not authenticated.
4. Execute all platform commands through the CLI, letting the platform's binary handle the secure transmission.

By logging into the *platforms* themselves, the Swarm bypasses the need for raw API keys entirely.
