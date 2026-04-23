# GitHub Copilot CLI

[← Back to Foundations](../part-1-foundations.md)

---

[GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) runs the Copilot agent in a terminal. It reached general availability on February 25, 2026. It can search, edit, run commands, and work with GitHub.com directly from the shell. That makes it powerful. It also makes the trust boundary very different from an IDE tab: the CLI runs with the user's shell identity, process environment, file permissions, and network reach.

**Official docs:** [About Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) · [Copilot CLI repository](https://github.com/github/copilot-cli)

**See it in action:** [How to use agents, skills, and instructions in Copilot CLI](https://www.youtube.com/watch?v=-yKALFS5ewY&t=4s) — GitHub demos instructions, skills, and custom agents running end-to-end in a terminal session.

## Start Here First

If this is the first Copilot CLI session, keep the first run boring:

1. Launch `copilot` inside a narrow, trusted repository rather than `$HOME` or a shared workspace.
2. Start with a read-only prompt or plan-mode task.
3. Add write and shell approvals only after the agent has shown it understands the repo.

GitHub's own guidance is explicit here: trusted-directory scoping is heuristic, not a hard sandbox. Do not launch the CLI from directories that contain untrusted files or sensitive data you do not want touched.

## Approval Posture

| Level | Behavior |
|-------|----------|
| **Manual approvals** | Copilot asks before using risky tools or making writes |
| **Scoped auto-approval** | Use `--allow-tool` and per-session approvals for specific tools or categories |
| **YOLO / allow-all** | Skip all permission prompts for tools, paths, and URLs. Enable with `--yolo` / `--allow-all`, then carve back risk with deny rules |

### YOLO Mode in Depth

`--yolo` (and the `/yolo` slash command) auto-approves every tool call, path access, and URL fetch for the session. It is equivalent to `--allow-all-tools --allow-all-paths --allow-all-urls`. Use it in throwaway sandboxes, ephemeral containers, CI runs, or prompt mode (`-p`) where no interactive approval is available.

**When to reach for it:**

- **Programmatic / CI runs:** `--allow-all-tools` (which `--yolo` implies) is required when driving the CLI non-interactively
- **Disposable VMs or devcontainers:** the blast radius is contained by the environment, not the prompt
- **Demos:** uninterrupted flow when showing the agent end-to-end

**When to avoid it:**

- Your working tree, `$HOME`, or any host you care about. YOLO mode will let the agent run destructive shell commands, write outside the project, and fetch arbitrary URLs
- Repos with untrusted MCP servers or third-party plugins
- Anywhere deny rules are the only thing keeping the agent out of secrets or production systems. Deny rules still fire, but they must be configured explicitly

**Minimum containment bar:** use ephemeral or disposable environments, mount only the filesystem the agent actually needs, avoid long-lived credentials, and add explicit deny rules for destructive operations such as `rm`, `git push`, or secret-bearing paths.

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

**Copilot auto model selection** is now generally available in the CLI for all Copilot plans. `auto` picks an efficient model for the task, shows which model was actually used, respects administrator model policy, and currently applies a 10% premium-request discount compared with selecting the same model directly. Use `/model` to switch between `auto` and a specific model whenever you need tighter control.

Switch models mid-session between Claude Opus 4.7, GPT-5.4, Gemini 3 Pro, and others. The CLI can also connect to your own model provider through environment-based provider settings, but that is a trust-boundary choice, not just a flexibility feature. A self-hosted or third-party provider may still log prompts, retain outputs, or have network egress unless you verify otherwise.

**[Fleet mode](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/fleet)** (`/fleet`) enables parallel sub-agent execution. An orchestrator decomposes a task into independent subtasks, dispatches them to parallel sub-agents, tracks dependencies, and synthesizes the results:

```text
/fleet Refactor the auth module, update tests, and fix related docs
```

The orchestrator builds a task graph. If Task C depends on A and B, it waits. Independent tasks run simultaneously. Monitor progress with `/tasks`.

**[Remote sessions](https://docs.github.com/en/copilot/how-tos/copilot-cli/steer-remotely)** (`/remote`) let developers start a CLI session locally and control it from any browser, or from GitHub Mobile beta, while the original shell keeps running. The session streams in real time. You can send instructions, approve actions, switch modes, and answer questions from GitHub.com or mobile:

```text
/remote          # enable remote access for the current session
copilot --remote # start a new session with remote access
```

The CLI generates a URL and QR code. Only the authenticated GitHub account can access the session. Remote access is still a real remote execution channel into that workstation, so unattended keep-alive sessions deserve the same caution as leaving an SSH session open. Remote access is in public preview, requires a GitHub-hosted repository, can be enabled by default with `"remoteSessions": true` in `~/.copilot/config.json`, and can be forced off per session with `--no-remote`. Use `/keep-alive busy` or a bounded window such as `/keep-alive 30m` instead of leaving a workstation awake indefinitely.

Reasoning models expose a thinking-effort setting that controls how deeply they think before responding. Set it from the model picker or via `/model` with a thinking-effort flag.

**C++ code intelligence** entered public preview on April 22, 2026. With the Microsoft C++ Language Server, the CLI can use semantic data such as definitions, references, call hierarchies, and type information instead of relying only on grep-style search. It currently requires project setup such as `compile_commands.json`.

## Slash Commands

**See it in action:** Alex Weininger demos the `/ide` command in [Copilot CLI in VS Code](https://www.youtube.com/watch?v=_l3UO1oUoec&t=180s), showing how to manage the connection between the CLI and an active VS Code window.

The CLI exposes its own set of slash commands for session control. Type `/` in an interactive session to browse them:

| Command | Purpose |
|---------|---------|
| `/model` | Switch models mid-session; set thinking effort for reasoning models |
| `/fleet` | Decompose a task across parallel sub-agents (orchestrator mode) |
| `/delegate` | Send the current task to the cloud coding agent and continue working locally |
| `/plan` | Enter plan mode. Produces a structured implementation plan before writing any code |
| `/yolo`, `/allow-all` | Enable all permissions for the rest of the session (tools, paths, URLs). Deny rules still override. Supports `on`, `off`, and `show` subcommands |
| `/resume` | Resume the previous session (prompt history, file context, pending approvals) |
| `/experimental` | Toggle experimental features (preview capabilities gated behind a flag) |
| `/changelog` | View the changelog for the installed CLI version |
| `/mcp` / `/mcp add` | Inspect or add MCP servers for the current session |
| `/extensions reload` | Hot-reload CLI extensions without restarting the session |
| `/remote`, `/keep-alive` | Remote session control (see Remote sessions above) |
| `/tasks` | Inspect task graph progress when running `/fleet` |

For the full reference, see the [CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference).

## Trust Boundaries and Policy Limits

The CLI is a later-wave rollout surface for most organizations. It has broad reach and weak natural boundaries compared with an editor sandbox.

- Standardize the repository assets in VS Code first, then add the CLI for terminal-first teams and automation-heavy workflows.
- Treat `--yolo`, remote sessions, and custom model providers as controlled-use features, not the default posture for every developer.
- Do not assume organization-level MCP controls are complete here. GitHub's docs call out known policy limitations for MCP server usage in the CLI.
- Prefer dedicated worktrees, containers, VMs, or ephemeral CI hosts when the CLI is expected to operate with high autonomy.

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

The repository customization primitives in this guide apply to CLI sessions the same way they apply in VS Code. This CLI-specific table is a subset of the canonical [Cross-Surface Primitive Support Matrix](../part-3-reference.md#cross-surface-primitive-support-matrix) in Part III.

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

**See it in action:** The GitHub Copilot CLI for Beginners series walks through `copilot-instructions.md`, `.instructions.md` files, agent skills, and custom agents running end-to-end in a terminal session. Watch [How to use agents, skills, and instructions in Copilot CLI](https://www.youtube.com/watch?v=-yKALFS5ewY&t=4s).

## Release Cadence

Copilot CLI ships weekly. Homebrew, WinGet, and the shell installer pick up new versions automatically. Track releases at [github.com/github/copilot-cli/releases](https://github.com/github/copilot-cli/releases).

## Getting Started

Available with all Copilot plans, subject to organization policy when Copilot is provided by an employer. Install via:

```text
# macOS / Linux
brew install gh-copilot

# Windows
winget install GitHub.CopilotCLI
```

## Custom Providers and Offline Mode

Copilot CLI supports custom model providers for teams that need self-hosted inference, private gateways, or non-GitHub-hosted models:

| Provider | Setup |
|----------|-------|
| **Ollama** | `copilot --provider ollama --model codellama:34b` |
| **vLLM** | `copilot --provider vllm --endpoint http://localhost:8000` |
| **Foundry Local** | `copilot --provider foundry-local --model phi-4` |

**Offline mode** disables all network calls to GitHub's API. Enable it with the environment variable:

```text
export COPILOT_OFFLINE=true
```

When `COPILOT_OFFLINE=true` is set, the CLI skips GitHub authentication entirely and uses only the configured local provider. GitHub-hosted models, Memory, and cloud-based features become unavailable. All local primitives still apply.

Self-hosted does not automatically mean offline. A third-party or internal provider can still retain prompts or send data over the network. Treat provider configuration as a security review item, not a convenience toggle.

## Further Reading

- [Copilot CLI documentation](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli)
- [Steering a session from another device](https://docs.github.com/en/copilot/how-tos/copilot-cli/steer-remotely)
- [Running tasks in parallel with /fleet](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/fleet)
- [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)

---

[← Back to Foundations](../part-1-foundations.md)
