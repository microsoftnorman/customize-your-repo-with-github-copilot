# GitHub Agentic Workflows

[← Copilot Memory](primitive-8-memory.md) | [Part II Overview](part-2-primitives.md) | [Copilot SDK →](copilot-sdk.md)

*Updated: April 22, 2026 · Validated against VS Code 1.116 and GitHub Copilot docs as of April 16, 2026.*

---

## Overview

Read this page as "the same primitive layer, but running in GitHub Actions." The instructions, skills, agents, and review guidance covered earlier do not stop at the editor. Agentic Workflows are what it looks like when that repository knowledge runs on a schedule, on repository events, or from a manual dispatch.

**Location:** `.github/workflows/*.md`
**Best For:** Scheduled, event-driven, and on-demand AI automation in GitHub Actions

**Official docs:** [Agentic Workflows](https://github.github.com/gh-aw/) · [Announcement](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/)

[GitHub Agentic Workflows](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/) run coding agents inside [GitHub Actions](https://docs.github.com/en/actions). You describe the desired outcome in plain Markdown, and a coding agent executes it on a schedule, on events, or on demand. GitHub calls this pattern **Continuous AI**: the integration of AI into the software development lifecycle alongside CI/CD.

CI/CD automates the things you can express as deterministic steps (build, test, deploy). Continuous AI automates the things you can only express as intent, like "triage new issues," "keep the docs in sync," or "find and fix code quality regressions." Agentic Workflows cover that second category.

GitHub Agentic Workflows are in technical preview (February 2026), developed by GitHub Next, Microsoft Research, and Azure Core Upstream. The product is in early development and may change significantly. Use it with caution and human oversight.

---

## How Agentic Workflows Work

An agentic workflow is a Markdown file in `.github/workflows/` with two parts:

1. **YAML frontmatter**: trigger, permissions, safe outputs, and tools
2. **Markdown body**: natural-language instructions describing the task

When the workflow runs, GitHub Actions spawns a coding agent (GitHub Copilot, Claude by Anthropic, or OpenAI Codex, depending on your [engine configuration](https://github.github.com/gh-aw/reference/engines/)) that reads the Markdown instructions and executes the task inside a sandboxed container.

Here is the daily repo report example from the [official documentation](https://github.github.com/gh-aw/):

**File:** `.github/workflows/daily-repo-status.md`

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

Create a daily status report for maintainers.

Include
- Recent repository activity (issues, PRs, discussions, releases, code changes)
- Progress tracking, goal reminders and highlights
- Project status and recommendations
- Actionable next steps for maintainers

Keep it concise and link to the relevant issues/PRs.
```

The `gh-aw` CLI extension generates a companion lock file (`.github/workflows/daily-repo-status.lock.yml`) that GitHub Actions executes. This two-file design separates intent (the Markdown) from execution (the compiled YAML).

### Frontmatter Reference

| Field | Purpose | Example |
|-------|---------|---------|
| `on` | When the workflow runs | `schedule: daily`, `issues: opened`, `push` |
| `permissions` | What the agent can read | `contents: read`, `issues: read` |
| `safe-outputs` | Pre-approved write operations (with constraints) | `create-issue:` with `title-prefix`, `labels`, `close-older-issues` |
| `tools` | External tools the agent can use | `github:` |

Safe outputs are the key security mechanism. They define the *only* write operations the workflow can perform. Each safe output type supports constraints like title prefixes and label requirements.

---

## Guardrails and Security

Agentic Workflows implement five security layers that work together to contain the impact of a confused or compromised agent:

1. **Read-only tokens.** The agent receives a GitHub token scoped to read-only permissions. Even if the agent attempts to push code or delete a file, the token doesn't allow it.

2. **Zero secrets in the agent.** The agent process never receives write tokens, API keys, or other credentials. Secrets exist only in separate, isolated jobs that run *after* the agent finishes and its output passes review.

3. **Containerized with network firewall.** The agent runs inside an isolated container. The [Agent Workflow Firewall](https://github.github.com/gh-aw/introduction/architecture/#agent-workflow-firewall-awf) routes all outbound traffic through a proxy enforcing a domain allowlist. Traffic to any other destination is dropped at the kernel level.

4. **Safe outputs with guardrails.** The agent cannot write to GitHub directly. Instead, it produces a structured artifact describing its intended actions. A separate job with scoped write permissions reads that artifact and applies only what the workflow explicitly permits, with hard limits per operation, required title prefixes, and label constraints.

5. **Agentic threat detection.** Before any output is applied, a dedicated job runs an AI-powered scan of the agent's proposed changes. It checks for prompt injection attacks, leaked credentials, and malicious code patterns. If anything looks suspicious, the workflow fails and nothing is written.

This differs from running coding agent CLIs directly in a standard GitHub Actions YAML workflow, which often grants more permission than a specific task requires. Agentic Workflows provide tighter constraints and clearer review points.

---

## Continuous AI Categories

Agentic Workflows enable six categories of repository automation:

| Category | What It Does |
|----------|-------------|
| **Continuous Triage** | Summarize, label, and route new issues automatically |
| **Continuous Documentation** | Keep READMEs and docs aligned with code changes |
| **Continuous Code Simplification** | Identify code improvements and open PRs for them |
| **Continuous Test Improvement** | Assess test coverage and add high-value tests |
| **Continuous Quality Hygiene** | Investigate CI failures, remediate security alerts, and propose targeted fixes |
| **Continuous Reporting** | Create regular reports on repository health, activity, and trends |

Continuous Quality Hygiene extends beyond CI failures into automated security remediation. Dependabot alerts can be assigned directly to coding agents, which design and implement fixes (including complex dependency upgrades such as major version bumps) then submit PRs for human approval. For large codebases, batch code scanning applies multiple security fixes across PRs in a single pass, accelerating security hygiene.

If repetitive work in a repository can be described in words, it's probably a good fit for an agentic workflow.

### Workflow Examples

The daily report shown earlier is a read-only workflow. It observes the repo and creates an issue. The examples below show the range, from simple triage to code-changing workflows. All three are adapted from [Peli's Agent Factory](https://github.github.com/gh-aw/blog/2026-01-12-welcome-to-pelis-agent-factory/), where GitHub Next runs dozens of agentic workflows against their own repository.

**Issue Triage.** When a new issue opens, label it and leave a comment explaining why:

```markdown
---
timeout-minutes: 5

on:
  issue:
    types: [opened, reopened]

permissions:
  issues: read

tools:
  github:
    toolsets: [issues, labels]

safe-outputs:
  add-labels:
    allowed: [bug, feature, enhancement, documentation, question, help-wanted, good-first-issue]
  add-comment: {}
---

# Issue Triage Agent

List open issues in ${{ github.repository }} that have no labels. For each
unlabeled issue, analyze the title and body, then add one of the allowed
labels: `bug`, `feature`, `enhancement`, `documentation`, `question`,
`help-wanted`, or `good-first-issue`.

Skip issues that:
- Already have any of these labels
- Have been assigned to any user (especially non-bot users)

Do research on the issue in the context of the codebase and, after
adding the label to an issue, mention the issue author in a comment, explain
why the label was added and give a brief summary of how the issue may be
addressed.
```

This is the "hello world" of agentic workflows: practical and low-risk. Note how the `safe-outputs` constrain the agent to a specific set of labels and comment-only writes.

**Code Simplification.** Run daily, find recently changed code that could be clearer:

```markdown
---
on:
  schedule: daily

permissions:
  contents: read
  pull-requests: read

safe-outputs:
  create-pull-request:
    title-prefix: "[simplify] "
    labels: [code-quality, automated]
    max: 1

tools:
  github:
---

# Automatic Code Simplifier

Analyze code changed in the last 3 commits. Look for opportunities to simplify
without changing functionality:

- Extract repeated logic into helper functions
- Convert nested if-statements to early returns
- Simplify boolean expressions
- Use standard library functions instead of custom implementations
- Consolidate similar error handling patterns

Create a single pull request with the simplifications. Each commit should be
a self-contained improvement. Preserve all existing tests — do not change
test behavior.

Skip: test files, generated code, configuration files, lock files.
```

This workflow creates PRs, so it requires `create-pull-request` in safe outputs. The `max: 1` constraint ensures the agent opens at most one PR per run. GitHub Next reports an 83% merge rate on simplification PRs from their own usage.

**Documentation Sync.** Keep docs aligned with code changes:

```markdown
---
on:
  schedule: daily

permissions:
  contents: read
  pull-requests: read

safe-outputs:
  create-pull-request:
    title-prefix: "[docs] "
    labels: [documentation, automated]
    max: 1

tools:
  github:
---

# Daily Documentation Updater

Review recent code changes and check whether the documentation still matches
the implementation.

## What to check
- README.md reflects current setup and usage instructions
- API documentation matches actual function signatures and parameters
- Code examples in docs actually work with the current codebase
- Configuration references match current option names and defaults

## What to do
- If docs are outdated, create a PR with the corrections
- Keep the same voice and style as existing documentation
- Explain in the PR description what changed in the code that triggered the update
- Do not rewrite documentation that is already correct
```

GitHub Next runs a similar workflow and reports a 96% merge rate on documentation update PRs. The rate is high because the changes are small and verifiable.

---

## Design Patterns

GitHub provides several design patterns for structuring agentic workflows:

- **ChatOps:** Trigger workflows from chat commands
- **DailyOps:** Scheduled daily automation (reports, triage, cleanup)
- **DataOps:** Data processing and analysis automation
- **IssueOps:** Issue-driven workflows (triage, routing, enrichment)
- **ProjectOps:** Project management automation
- **MultiRepoOps:** Coordination across multiple repositories
- **Orchestration:** Multi-step workflows with dependencies

---

## How the Customization Primitives Fit In

Agentic Workflows and the customization primitives covered in this guide operate at different scopes. Agentic Workflows decide *what work happens* against your repository. The primitives decide *how well the coding agent does that work*.

| | Customization Primitives | Agentic Workflows |
|---|---|---|
| **Where they run** | IDE (VS Code) and cloud agent sessions | GitHub Actions |
| **Who triggers them** | Developer (interactive) or cloud agent (assigned task) | Schedule, webhook event, or manual dispatch |
| **What they configure** | How Copilot thinks and what it knows | What autonomous tasks run against your repo |
| **Configuration format** | Instructions, skills, agents, MCP, hooks | Markdown files with YAML frontmatter |

### What matters for autonomous quality

When a coding agent runs autonomously (whether via an Agentic Workflow, an assigned issue, or direct invocation) it can't ask clarifying questions. The quality of your repo configuration directly determines the quality of its output. Three primitives matter most:

**Custom instructions** tell the agent what conventions to follow. Build commands, test expectations, PR format, and guardrails all belong here. The [Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent) reads custom instructions on every task. See [Primitive 1](primitive-1-always-on-instructions.md).

✅ Clear instruction for async work:
```markdown
- Run `npm test` before committing any changes
- If tests fail, fix the issue — do not commit failing tests
- Do not modify CI/CD configuration files without explicit approval
```

❌ Vague instruction that leaves decisions to the agent:
```markdown
- Make sure everything works before committing
- Be careful with infrastructure files
```

**Skills** load automatically by description match. A skill with description "Use when creating new React components" loads when the agent works on component-related tasks, whether in an IDE session or an autonomous run. See [Primitive 4](primitive-4-skills.md).

**Hooks** enforce policies regardless of who triggered the agent. A deployment gate hook that blocks `git push` without passing tests applies the same way to a human developer, a cloud agent session, and an Agentic Workflow run. See [Primitive 7](primitive-7-hooks.md).

### Primitives and extensions reference

| Primitive or extension | Role in Autonomous Work |
|------------------------|-------------------------|
| **Always-on Instructions** | Build commands, test expectations, PR conventions; read on every task |
| **File-based Instructions** | Pattern-matched rules that load when the agent touches matching files |
| **Skills** | Procedural knowledge (scaffolding, testing, domain tasks) loaded by description match |
| **Custom Agents** | Specialized personas for the cloud agent (e.g., frontend expert, documentation agent) |
| **MCP Servers** | External tool access (databases, APIs, monitoring) available during agent sessions |
| **Hooks** | Runtime enforcement; applies identically to interactive and autonomous work |
| **Copilot Memory** | Patterns learned over time that supplement explicit configuration |
| **GitHub Copilot SDK** *(platform extension)* | Embed the agent runtime in custom tools, CI pipelines, and internal platforms |

---

## Getting Started

1. Install the CLI extension: `gh extension install github/gh-aw`
2. Create a workflow Markdown file in `.github/workflows/`
3. Compile the lock file: `gh aw compile`
4. Commit and push both files
5. Add any required secrets (engine tokens or API keys)

Alternatively, use a coding agent to generate workflows interactively. Provide a prompt describing the desired outcome and reference the [creation guide](https://github.github.com/gh-aw/setup/creating-workflows/).

### Practical Guidance

- **Start with low-risk outputs** such as comments, reports, or issue labels before enabling pull request creation.
- **For coding workflows**, start with routine improvements (refactoring, test coverage, code simplification) rather than feature work.
- **Be specific about what "good" looks like.** Format, tone, links, when to stop. The more precise the Markdown instructions, the better the output.
- **Treat the workflow Markdown as code.** Review changes, keep instructions small, and evolve them intentionally.
- **Agentic Workflows complement CI/CD. They don't replace it.** CI/CD handles deterministic steps. Continuous AI handles subjective, repetitive tasks that deterministic workflows can't express.

---

## Further Reading

- [Automate repository tasks with GitHub Agentic Workflows](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/): Announcement blog post
- [GitHub Agentic Workflows documentation](https://github.github.com/gh-aw/): Quick start, patterns, and reference
- [Security architecture of GitHub Agentic Workflows](https://github.blog/ai-and-ml/generative-ai/under-the-hood-security-architecture-of-github-agentic-workflows/): Threat model and defense-in-depth details
- [About Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent): Cloud agent documentation
- [Custom Agents](primitive-5-custom-agents.md): Specialized agent personas
- [Skills](primitive-4-skills.md): Skills specification and patterns
- [Copilot Memory](primitive-8-memory.md): How Memory complements explicit customization
- [Copilot SDK](copilot-sdk.md): Embed the Copilot agent runtime in your own tools and applications

---

[← Copilot Memory](primitive-8-memory.md) | [Next: Copilot SDK →](copilot-sdk.md)
