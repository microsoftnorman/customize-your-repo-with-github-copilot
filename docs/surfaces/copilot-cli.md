# GitHub Copilot CLI

[← Where GitHub Copilot Runs](../where-github-copilot-runs.md) | [← VS Code](vscode.md) | [Next: Cloud Coding Agent →](cloud-coding-agent.md)

*Updated: May 4, 2026.*

---

## What This Surface Is

GitHub Copilot CLI is the terminal-first surface for the same agent loop.

For current capabilities, security controls, and customization behavior, use [About GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli) as the canonical reference.

If VS Code is the richest authoring environment, the CLI is often the clearest runtime environment. The loop is harder to hide in a terminal. Approvals, tool calls, command output, retries, and delegation are all more visible.

That makes the CLI useful for both adoption and diagnosis.

**See it in action:** [How to use agents, skills, and instructions in Copilot CLI | Tutorial for beginners](https://www.youtube.com/watch?v=-yKALFS5ewY&t=64s) — GitHub (Copilot CLI for Beginners series) demos adding project instructions so GitHub Copilot CLI follows team standards.

**See it in action:** [You need to try the GitHub Copilot CLI right now](https://www.youtube.com/watch?v=CqcqWLv-sDM&t=1055s) — Burke Holland demos plan mode and Autopilot inside GitHub Copilot CLI for terminal-first agent sessions.

## Why It Matters

Many teams do not need another editor. They need the agent to work where they already work:

- in shells,
- in containers,
- over SSH,
- in devcontainers and Codespaces,
- or inside scripted workflows.

The CLI matters because it proves that the repository knowledge is not IDE-dependent.

## What Carries Over Cleanly

The CLI is one of the strongest consumers of the repository layer.

The important carryovers are:

- Always-on Instructions,
- File-based Instructions,
- Skills,
- Custom Agents,
- MCP,
- Hooks,
- Agent Plugins,
- and Memory.

That is why terminal-first teams can participate in the same customization strategy instead of maintaining a parallel one.

## What the CLI Makes Easier to Understand

The CLI makes three parts of the system unusually legible:

- the approval model,
- the relationship between task framing and autonomy,
- and the fact that the agent is doing real work with tools, not just producing text.

For many teams, the CLI is the fastest way to understand the agent loop without the abstraction layers of an IDE.

## Where the CLI Changes the Experience

The CLI is not just VS Code without windows.

It changes the posture of the interaction:

- prompts tend to be more operational,
- command execution is more central,
- permissions become more concrete,
- and delegation to remote or parallel work is easier to reason about.

This is why it is a particularly good fit for infrastructure, platform, and DevOps-heavy teams.

## What It Is Best At

GitHub Copilot CLI is especially strong when the task already sounds like terminal work:

- inspect this repository,
- run the failing tests and fix them,
- refactor this module and update the docs,
- search the codebase and summarize the pattern,
- or keep working on this task while the developer watches the shell.

It is also one of the strongest surfaces for remote and delegated workflows.

## The Main Difference from VS Code

VS Code is the better authoring surface.

The CLI is often the better teaching surface for how the loop actually behaves.

That distinction matters. Teams do not need to pick one permanently. Many will author in VS Code and execute heavy operational work in the CLI.

## VS Code-Managed CLI Sessions vs Terminal-Native CLI

There are two common CLI experiences now, and they should not be collapsed into one sentence.

VS Code-managed GitHub Copilot CLI sessions run in the background through the GitHub Copilot CLI agent harness while VS Code starts, monitors, and resumes them through the Chat view. In that session context, GitHub Copilot CLI supports slash commands, reusable prompts, Skills, Hooks, `/compact`, and approval toggles such as `/yolo` or `/autoApprove`.

Terminal-native CLI remains the shell-first experience. It is still strongest around natural-language prompts, repository instructions, Skills, Custom Agents, MCP, Hooks, plugins, approvals, and visible command execution. It may not expose every VS Code authoring affordance the same way.

## Recent CLI Changes

VS Code 1.118 and the current GitHub Copilot CLI docs add several operational details worth knowing. For command names, permission flags, MCP configuration, Skills, Custom Agents, and telemetry, use the official [GitHub Copilot CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference).

| Area | Change |
|------|--------|
| Remote control | Experimental remote control lets a developer monitor and steer a running CLI session from GitHub.com or GitHub Mobile. Enable `github.copilot.chat.cli.remote.enabled`, then run `/remote on`. |
| Session titles | VS Code now uses the GitHub Copilot SDK session title APIs so Chat view titles, editor tabs, terminal session titles, and `copilot --resume` stay synchronized. |
| Plugins | GitHub Copilot CLI plugins install from marketplaces or direct sources and can bundle agents, Skills, hooks, MCP servers, commands, and LSP servers behind `plugin.json`. |
| MCP | Workspace `.mcp.json` support in VS Code aligns better with GitHub Copilot CLI, but teams should still verify active servers with `/mcp` in terminal-native sessions. |

Remote control is useful for long-running work, but it changes the operating model. A session can now ask for approval while the developer is away from the machine that started it. Teams should decide which repos and approval modes are acceptable before making it a default workflow.

## The Short Version

Use GitHub Copilot CLI when the team wants the agent loop in its most visible operational form.

It is one of the best places to prove that customization is not editor theater. The repository knowledge is real because it still works when the UI falls away.

## Where to Read Next

- Read [Cloud Coding Agent](cloud-coding-agent.md) next for the remote version of the same portability story.
- Revisit [Skills](../primitive-4-skills.md) and [Hooks](../primitive-7-hooks.md) if the CLI's operational model is the main reason the team is customizing GitHub Copilot.
