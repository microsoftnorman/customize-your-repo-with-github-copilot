# GitHub Copilot CLI

[← Back to Foundations](../part-1-foundations.md)

---

[GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) brings the full agentic experience to the terminal. It reached general availability on February 25, 2026. The same agent capabilities available in VS Code — tool calling, file editing, test running — work directly from the command line.

**Official docs:** [About Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) · [Copilot CLI repository](https://github.com/github/copilot-cli)

**See it in action:** [Copilot CLI in VS Code](https://www.youtube.com/watch?v=_l3UO1oUoec&t=0s) — Alex Weininger demos the CLI and its integration with VS Code.

## Permission Levels

| Level | Behavior |
|-------|----------|
| **Default** | Agent suggests actions; developer approves each one |
| **Bypass Approvals** | Skip confirmations for low-risk actions |
| **YOLO / allow-all** | Skip all permission prompts for tools, paths, and URLs. Enable with `--yolo` (alias of `--allow-all`) at launch, `/yolo` (alias of `/allow-all`) mid-session, or `COPILOT_ALLOW_ALL=true`. Deny rules still override — `--deny-tool` and `--deny-url` take precedence, even with `--yolo` set |
| **Autopilot** (preview) | Fully autonomous — agent retries on errors, works until task completion |

### YOLO Mode in Depth

`--yolo` (and the `/yolo` slash command) auto-approves every tool call, path access, and URL fetch for the session — equivalent to `--allow-all-tools --allow-all-paths --allow-all-urls`. Use it in throwaway sandboxes, ephemeral containers, CI runs, or prompt mode (`-p`) where no interactive approval is available.

**When to reach for it:**

- **Programmatic / CI runs** — `--allow-all-tools` (which `--yolo` implies) is required when driving the CLI non-interactively
- **Disposable VMs or devcontainers** — the blast radius is contained by the environment, not the prompt
- **Demos** — uninterrupted flow when showing the agent end-to-end

**When to avoid it:**

- Your working tree, `$HOME`, or any host you care about — YOLO mode will let the agent run destructive shell commands, write outside the project, and fetch arbitrary URLs
- Repos with untrusted MCP servers or third-party plugins
- Anywhere deny rules are the only thing keeping the agent out of secrets or production systems — remember deny rules still fire, but they must be configured explicitly

**Scoping YOLO safely:**

```text
# Allow everything except destructive git and writes to .env
copilot --yolo \
  --deny-tool='shell(git push)' \
  --deny-tool='shell(rm:*)' \
  --deny-tool='write(.env)' \
  --deny-url='*.prod.example.com'
```

`/yolo` state and any path approvals it grants persist across `/restart` and `/clear` within the same session. Start fresh with a new `copilot` invocation to reset.

## Key Features

**Multi-model hot-swapping** — switch between Claude Opus 4.7, GPT-5.4, Gemini 3 Pro, and others during a session. Enterprises can use **BYOK (Bring Your Own Key)** to connect their own API keys for supported providers.

**Fleet mode** (`/fleet`) enables parallel sub-agent execution. An orchestrator decomposes a task into independent subtasks, dispatches them to parallel sub-agents, tracks dependencies, and synthesizes the results:

```text
/fleet Refactor the auth module, update tests, and fix related docs
```

The orchestrator builds a task graph — if Task C depends on A and B, it waits. Independent tasks run simultaneously. Monitor progress with `/tasks`.

**Remote sessions** (`/remote`) let developers start a CLI session locally and control it from any device via the GitHub web interface or GitHub Mobile. The session streams in real time — send instructions, approve actions, switch modes, and answer questions from a browser or phone:

```text
/remote          # enable remote access for the current session
copilot --remote # start a new session with remote access
```

The CLI generates a URL and QR code. Only the authenticated GitHub account can access the session. Use `/keep-alive` to prevent the machine from sleeping during long tasks.

**Thinking effort** — configure how deeply reasoning models think before responding, balancing response quality and latency. Available from the model picker or via `/model` with a thinking-effort flag.

## Slash Commands

**See it in action:** [Copilot CLI in VS Code](https://www.youtube.com/watch?v=_l3UO1oUoec&t=180s) — Alex Weininger demos the `/ide` command for managing the connection between the CLI and an active VS Code window.

The CLI exposes its own set of slash commands for session control. Type `/` in an interactive session to browse them:

| Command | Purpose |
|---------|---------|
| `/model` | Switch models mid-session; set thinking effort for reasoning models |
| `/fleet` | Decompose a task across parallel sub-agents (orchestrator mode) |
| `/delegate` | Send the current task to the cloud coding agent and continue working locally |
| `/plan` | Enter plan mode — produce a structured implementation plan before writing any code |
| `/yolo`, `/allow-all` | Enable all permissions for the rest of the session (tools, paths, URLs). Deny rules still override. Supports `on`, `off`, and `show` subcommands |
| `/resume` | Resume the previous session (prompt history, file context, pending approvals) |
| `/experimental` | Toggle experimental features (preview capabilities gated behind a flag) |
| `/changelog` | View the changelog for the installed CLI version |
| `/mcp` / `/mcp add` | Inspect or add MCP servers for the current session |
| `/extensions reload` | Hot-reload CLI extensions without restarting the session |
| `/remote`, `/keep-alive` | Remote session control (see Remote sessions above) |
| `/tasks` | Inspect task graph progress when running `/fleet` |

For the full reference, see the [CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference).

### Installing Skills with `gh skill`

Skills installed into `.github/skills/` (or the user scope) are available in CLI sessions just like in VS Code. As of April 2026, the [`gh skill`](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli) command (GitHub CLI v2.90.0+, public preview) is the recommended way to discover, install, pin, and update skills:

```text
gh skill search <query>
gh skill install github/awesome-copilot <skill-name>
gh skill install github/awesome-copilot <skill-name> --pin v1.2.0
gh skill update --all
```

Use `copilot plugin install` for full plugin bundles (skills + agents + hooks + MCP); use `gh skill install` when you only need a skill and want cross-host portability and version pinning. See [Installing and Managing Skills with `gh skill`](../primitive-4-skills.md#installing-and-managing-skills-with-gh-skill).

## Primitive Support

The repository customization primitives in this guide apply to CLI sessions the same way they apply in VS Code:

| Primitive | Support |
|-----------|---------|
| Always-on Instructions | ✅ Supported |
| File-based Instructions | ✅ Supported |
| Skills | ✅ Supported |
| Custom Agents | ✅ Supported |
| MCP | ✅ Supported |
| Hooks | ✅ Supported |
| Memory | ✅ Supported |
| Prompts | VS Code only |

**See it in action:** [How to use agents, skills, and instructions in Copilot CLI](https://www.youtube.com/watch?v=-yKALFS5ewY&t=52s) — the GitHub Copilot CLI for Beginners series walks through `copilot-instructions.md`, `.instructions.md` files, agent skills, and custom agents running end-to-end in a terminal session.

## Release Cadence

Copilot CLI ships **weekly updates** with automatic updates via Homebrew, WinGet, and the shell installer. Track releases at [github.com/github/copilot-cli/releases](https://github.com/github/copilot-cli/releases).

## Getting Started

Available to all paid Copilot subscribers (Pro, Pro+, Business, Enterprise). Install via:

```text
# macOS / Linux
brew install gh-copilot

# Windows
winget install GitHub.CopilotCLI
```

## Local Models & Offline Mode

Copilot CLI supports local model providers for air-gapped environments, latency-sensitive workflows, or teams that prefer self-hosted inference:

| Provider | Setup |
|----------|-------|
| **Ollama** | `copilot --provider ollama --model codellama:34b` |
| **vLLM** | `copilot --provider vllm --endpoint http://localhost:8000` |
| **Foundry Local** | `copilot --provider foundry-local --model phi-4` |

**Offline mode** disables all network calls to GitHub's API. Enable it with the environment variable:

```text
export COPILOT_OFFLINE=true
```

When `COPILOT_OFFLINE=true` is set, the CLI skips GitHub authentication entirely and uses only the configured local provider. This means GitHub-hosted models, Memory, and cloud-based features are unavailable — but all local primitives (instructions, skills, hooks, MCP) still apply.

When using a local or third-party provider *with* network access, GitHub authentication is optional. The CLI authenticates only when accessing GitHub-hosted models or cloud features like Memory.

## Further Reading

- [Copilot CLI documentation](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli)
- [Steering a session from another device](https://docs.github.com/en/copilot/how-tos/copilot-cli/steer-remotely)
- [Running tasks in parallel with /fleet](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/fleet)
- [Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)

---

[← Back to Foundations](../part-1-foundations.md)
