# GitHub Copilot CLI

[← Back to Foundations](../part-1-foundations.md)

---

[GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) brings the full agentic experience to the terminal. It reached general availability on February 25, 2026. The same agent capabilities available in VS Code — tool calling, file editing, test running — work directly from the command line.

## Permission Levels

| Level | Behavior |
|-------|----------|
| **Default** | Agent suggests actions; developer approves each one |
| **Bypass Approvals** | Skip confirmations for low-risk actions |
| **Autopilot** (preview) | Fully autonomous — agent retries on errors, works until task completion |

## Key Features

**Multi-model hot-swapping** — switch between Claude Opus 4.6, GPT-5.4, Gemini 3 Pro, and others during a session. Enterprises can use **BYOK (Bring Your Own Key)** to connect their own API keys for supported providers.

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

**Thinking effort** — configure how deeply reasoning models think before responding, balancing response quality and latency. Available from the model picker.

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

## Further Reading

- [Copilot CLI documentation](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli)
- [Steering a session from another device](https://docs.github.com/en/copilot/how-tos/copilot-cli/steer-remotely)
- [Running tasks in parallel with /fleet](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/fleet)
- [Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)

---

[← Back to Foundations](../part-1-foundations.md)
