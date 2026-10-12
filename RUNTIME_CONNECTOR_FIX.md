# Runtime and connector repair v3

This branch replaces the two divergent `agi` implementations with one tested runtime.

## What changed

- `agi` with no arguments opens a real REPL when attached to a terminal.
- `:paste` accepts multiline text until `:end`, so pasted scripts are not dispatched line by line.
- `:shell` or `agi shell` opens a PTY-backed login shell; `agi shell command arg...` executes an argument vector without `shell=True`.
- Provider routing is local-first: cockpit, Ollama, OpenRouter, then optional Pollinations.
- Each failed provider gets a persistent exponential cooldown. HTTP `Retry-After` is honored, preventing repeated 429 storms.
- Connector status distinguishes Drive/OneDrive authorization from Gmail/Calendar OAuth scopes.
- Configuration parsing no longer executes `config.env` as shell code inside Python.
- `agi fix` starts only known installed launchers and does not delete broad lock-file patterns.
- Root `agi` and `bin/agi` now call the same implementation.

## Install from this branch

```bash
cd ~/josie
git fetch origin
git switch fix/runtime-connectors-v3
python -m unittest discover -s tests -v
chmod +x agi bin/agi
mkdir -p ~/bin
ln -sf "$PWD/bin/agi" ~/bin/agi
agi status
```

## Interactive use

```bash
agi
# :paste  -> paste multiple lines, finish with :end
# :shell  -> enter a real interactive shell
# :status -> provider and connector status
# :quit   -> exit
```

## Provider controls

```bash
export JOSIE_PROVIDER_ORDER=local,ollama,openrouter,pollinations
export OLLAMA_MODEL=qwen2.5:3b
export JOSIE_MODEL=openrouter/auto
export JOSIE_ENABLE_POLLINATIONS=1
```

Use `JOSIE_ENABLE_POLLINATIONS=0` to disable the public keyless fallback. OpenRouter is attempted only when a key is configured. Provider failures are reported separately instead of being collapsed into a generic cascade error.

## Connector controls

Run `agi connectors status`, then `agi connectors auth`. OAuth consent, provider billing, and account passwords remain user-controlled; software can prepare and verify local configuration but cannot lawfully approve those account actions by itself.
