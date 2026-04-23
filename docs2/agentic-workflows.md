# GitHub Agentic Workflows

[← Back to Guide](README.md) | [← The Eight Primitives](part-2-primitives.md) | [Next: GitHub Copilot SDK →](copilot-sdk.md)

*Updated: April 22, 2026.*

---

## What This Page Covers

Agentic Workflows are what the same primitive layer looks like when it runs inside GitHub Actions instead of an interactive local session.

For the current product contract, use the [GitHub Agentic Workflows documentation](https://github.github.com/gh-aw/) and the [launch overview on the GitHub Blog](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/).

That is the most important framing to keep.

This is not a ninth primitive. It is not a second customization system. It is a runtime that consumes repository knowledge in a scheduled, event-driven, or manually dispatched environment.

## Why This Matters

The earlier chapters teach how to make GitHub Copilot behave intelligently inside a repository. Agentic Workflows answer a different question:

**What if the same knowledge should run when no one is sitting at the editor?**

That is where Continuous AI becomes useful.

CI/CD automates deterministic steps well. Agentic Workflows automate tasks that are still easier to describe as intent than as fixed scripts:

- triage new issues,
- simplify code,
- keep docs aligned with code,
- improve tests,
- produce repository health reports,
- or open focused maintenance PRs.

## How It Reuses the Primitive Layer

Agentic Workflows consume the same repository-level context the rest of the guide has been building toward.

| Primitive Layer | Role in an Agentic Workflow |
|-----------------|-----------------------------|
| **Always-on Instructions** | Carry repository-wide defaults into the workflow |
| **File-based Instructions** | Keep path-specific conventions alive when the workflow touches specific code areas |
| **Skills** | Package reusable procedures the workflow can rely on |
| **Custom Agents** | Define specialized postures when workflows are split by role |
| **MCP** | Extend reach into systems the workflow needs |

That reuse is why this guide keeps insisting that primitives are portable knowledge. Agentic Workflows are one of the clearest proofs of that claim.

## What Changes When the Runtime Moves to GitHub Actions

Three things change when the loop leaves the editor:

1. **The session becomes non-interactive by default.** The workflow cannot rely on a developer to clarify intent turn by turn.
2. **The environment becomes more constrained.** Permissions, safe outputs, and execution boundaries matter much more.
3. **Review becomes part of the design.** The workflow should assume that human approval is still the final gate for anything that changes the repository or external systems.

That means Agentic Workflows reward clear task framing even more than local sessions do.

## The Basic Shape

At a high level, an Agentic Workflow is a Markdown file under `.github/workflows/` with structured frontmatter and a body that describes the task.

The key conceptual split is:

- frontmatter defines when and how the workflow runs,
- the body defines what the agent is supposed to accomplish.

This is the same distinction the rest of the guide uses repeatedly: structured control around natural-language intent.

## Why Safety Matters More Here

The loop is still an agent loop, but it is now operating in a repository automation context.

That changes the risk model.

Agentic Workflows matter because they create useful automation. They also matter because they make permission design, safe outputs, and review boundaries non-optional. This is one of the strongest arguments for learning the distinction between guidance and enforcement earlier in the guide.

The workflow can carry instructions and procedures. It still needs explicit limits on what it may write or trigger.

GitHub's [security architecture](https://github.github.com/gh-aw/introduction/architecture/) is the canonical reference for the guardrail model: read-only defaults, safe outputs, and the review boundary around write actions.

## Good Use Cases

Good fits for Agentic Workflows share three traits:

- the task is repetitive,
- the task can be described clearly in natural language,
- and the output can be reviewed or constrained before it causes damage.

Examples:

- issue labeling and triage,
- changelog or status report generation,
- documentation drift correction,
- small-scale code simplification,
- test improvement suggestions,
- routine repository hygiene.

Bad fits are usually tasks with unclear success conditions, unconstrained destructive power, or too much dependence on ad hoc human judgment.

## Relationship to the Agent Loop

The local source material on unified agent experience is useful here because it reinforces a subtle but important point: the runtime may move, but the loop does not disappear.

The workflow still:

- assembles context,
- reasons over the task,
- uses tools,
- processes results,
- and stops when the task converges or is blocked.

What changes is the environment, not the existence of the loop.

## Workflow File Structure

An Agentic Workflow is a Markdown file in `.github/workflows/` with two parts:

1. **YAML frontmatter**: trigger, permissions, safe outputs, and tools
2. **Markdown body**: natural-language instructions describing the task

When the workflow runs, GitHub Actions spawns a coding agent that reads the instructions and executes inside a sandboxed container.

### Frontmatter Reference

| Field | Purpose | Example |
|-------|---------|---------|
| `on` | When the workflow runs | `schedule: daily`, `issues: opened`, `push` |
| `permissions` | What the agent can read | `contents: read`, `issues: read` |
| `safe-outputs` | Pre-approved write operations (with constraints) | `create-issue:` with `title-prefix`, `labels` |
| `tools` | External tools the agent can use | `github:` |

Safe outputs define the **only** write operations the workflow can perform. Each supports constraints like title prefixes and label requirements.

### Example: Daily Repo Status Report

```markdown
---
on:
  schedule: daily

permissions:
  contents: read
  issues: read
  pull-requests: read

safe-outputs:
  create-issue:
    title-prefix: "[repo status] "
    labels: [report]

tools:
  github:
---

# Daily Repo Status Report

Create a daily status report for maintainers. Include recent activity,
progress tracking, project status, and actionable next steps.
Keep it concise and link to the relevant issues/PRs.
```

## Five Security Layers

Agentic Workflows implement five security layers:

1. **Read-only tokens.** The agent receives a token scoped to read-only permissions. Write attempts fail.
2. **Zero secrets in the agent.** The agent process never receives write tokens, API keys, or credentials. Secrets exist only in isolated jobs that run after the agent finishes.
3. **Containerized with network firewall.** The agent runs in an isolated container. The [Agent Workflow Firewall](https://github.github.com/gh-aw/introduction/architecture/#agent-workflow-firewall-awf) enforces a domain allowlist. Unauthorized traffic is dropped at the kernel level.
4. **Safe outputs with guardrails.** The agent produces a structured artifact describing intended actions. A separate job applies only what the workflow explicitly permits.
5. **Agentic threat detection.** A dedicated job scans the agent's proposed changes for prompt injection, leaked credentials, and malicious patterns before anything is written.

## How It Differs from the Copilot SDK

Agentic Workflows are the GitHub-hosted version of remote agent execution.

The [GitHub Copilot SDK](copilot-sdk.md) is the application-owned version.

Use Agentic Workflows when the repository already lives naturally in GitHub's automation model. Reach for the SDK when the team needs to embed the runtime inside its own tool, portal, or platform.

## Where to Read Next

- Read [GitHub Copilot SDK](copilot-sdk.md) next to compare GitHub-hosted execution with application-owned execution.
- Read [GitHub Copilot Code Review](code-review.md) later for another environment where repository knowledge becomes operational outside local chat.
