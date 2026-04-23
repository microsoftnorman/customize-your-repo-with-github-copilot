# GitHub Copilot CLI

[← Where GitHub Copilot Runs](../where-github-copilot-runs.md) | [← VS Code](vscode.md) | [Next: Cloud Coding Agent →](cloud-coding-agent.md)

*Updated: April 22, 2026.*

---

## What This Surface Is

GitHub Copilot CLI is the terminal-first surface for the same agent loop.

For current capabilities, security controls, and customization behavior, use [About GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli) as the canonical reference.

If VS Code is the richest authoring environment, the CLI is often the clearest runtime environment. The loop is harder to hide in a terminal. Approvals, tool calls, command output, retries, and delegation are all more visible.

That makes the CLI useful for both adoption and diagnosis.

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

## The Main Caveat

Prompts are the main notable gap compared with the broadest VS Code customization story.

That does not weaken the CLI's value. It just means the terminal portability story is strongest around repository rules, procedures, tools, and runtime controls rather than every authoring affordance available in VS Code.

## The Short Version

Use GitHub Copilot CLI when the team wants the agent loop in its most visible operational form.

It is one of the best places to prove that customization is not editor theater. The repository knowledge is real because it still works when the UI falls away.

## Where to Read Next

- Read [Cloud Coding Agent](cloud-coding-agent.md) next for the remote version of the same portability story.
- Revisit [Skills](../primitive-4-skills.md) and [Hooks](../primitive-7-hooks.md) if the CLI's operational model is the main reason the team is customizing GitHub Copilot.
