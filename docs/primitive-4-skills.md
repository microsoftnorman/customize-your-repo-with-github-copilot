# Primitive 4: Skills

[← Back to The Eight Primitives](eight-primitives.md) | [← Prompts](primitive-3-prompts.md) | [Next: Custom Agents →](primitive-5-custom-agents.md)

*Updated: May 4, 2026.*

---

## Where It Enters the Loop

Skills enter the loop at task shaping and decision support.

The current official references are VS Code's [Use Agent Skills in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills) page, GitHub's [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills), and the open [Agent Skills specification](https://agentskills.io/).

They do not establish the repository's baseline. They do not create a persistent persona. They do not connect new tools. They package reusable procedure so the agent can load it when the task calls for it.

That is why Skills are one of the most misunderstood primitives. They sit in the same neighborhood as Prompts, but they solve a different problem.

## What This Primitive Is For

Skills help agent sessions. They do not feed the dedicated GitHub Copilot code review pipeline. If a standard must be reviewed on a pull request, put that standard in Always-on Instructions or File-based Instructions and let the Skill reference it.

Use a Skill when the repository needs reusable know-how rather than reusable wording.

Typical examples:

- debugging flaky tests,
- generating release notes from the team's existing process,
- triaging incidents according to a runbook,
- preparing issues with a standard structure,
- walking a deployment or rollback procedure.

The key is that the knowledge is procedural. It is not just "what should the output look like?" It is "how is this task actually done here?"

## What Makes Skills Different

Skills are discoverable. Prompts are invoked.

That distinction matters more than it first appears.

A Prompt is great when a human wants an explicit slash command for a one-shot workflow. A Skill is better when the procedure should also be available to the agent when the user asks for the task in normal language.

For example, a user can type, "draft release notes for the latest release." GitHub Copilot sees a `release-notes` Skill whose description says it generates release notes from merged pull requests and changelog conventions, then loads `SKILL.md` because the normal-language request matches that capability.

That makes Skills especially valuable in surfaces beyond one chat picker. They package knowledge in a way that can travel.

## The Unit of a Skill Is a Folder, Not Just a File

This primitive usually lives under `.github/skills/`, with one folder per skill and a `SKILL.md` at the center. VS Code also discovers project Skills from `.claude/skills/` and `.agents/skills/`, and personal Skills from `~/.copilot/skills/`, `~/.claude/skills/`, and `~/.agents/skills/`. Additional locations can be configured with `chat.agentSkillsLocations`; see the official [Create a skill](https://code.visualstudio.com/docs/copilot/customization/agent-skills#_create-a-skill) section for the current discovery paths.

That folder shape is important because it lets the procedure carry supporting assets:

- scripts,
- templates,
- reference docs,
- and other local resources.

This is the point where the rewrite stops treating all Markdown-based primitives as morally equivalent. A Skill is closer to a small capability package than to a paragraph of reusable instructions.

## Discovery Depends on Description Quality

The description is not metadata trivia. It is the activation surface.

If the description is vague, the Skill is harder to discover. If it names the task clearly and uses recognizable action language, the agent has a better chance of loading it at the right moment.

Weak description:

- "release notes skill"

Strong description:

- "Generate release notes from merged pull requests, changelog conventions, and the repository's existing release format. Use when the user asks to draft release notes or summarize a release."

The more procedural the capability, the more the description has to say what it does and when to use it.

## When to Use Skills Instead of Prompts

Use a Skill when:

- the capability should load automatically when relevant,
- the procedure needs supporting scripts or templates,
- the task should travel across multiple surfaces,
- or the team wants durable packaged know-how rather than only a slash command.

Stay with a Prompt when the task is simple, user-invoked, and mostly about templated phrasing.

## When to Use Skills Instead of File-based Instructions

File-based Instructions answer, "What rules apply when editing these files?"

Skills answer, "How is this task carried out?"

Those are different axes.

If the problem is path-scoped style or architecture, use File-based Instructions.
If the problem is a repeatable workflow, use a Skill.

Many teams need both at once.

## What a Good Skill Looks Like

```markdown
---
name: release-notes
description: Generate release notes from merged pull requests and the repository's changelog conventions. Use when the user asks to draft release notes or summarize a new release.
metadata:
	author: platform-team
	version: "1.0"
---

# Release Notes

## When to Use This Skill
- When the user asks to draft release notes
- When a release summary is needed from merged PRs

## Instructions
1. Read the existing changelog format
2. Gather merged PRs since the last release tag
3. Group changes by user-facing category
4. Flag unclear entries instead of guessing
```

The value is not the markdown alone. The value is that the procedure becomes reusable and portable.

## How It Composes with Other Primitives

| Primitive | Relationship |
|-----------|--------------|
| [Always-on Instructions](primitive-1-always-on-instructions.md) | Provide repo-wide context the Skill assumes |
| [File-based Instructions](primitive-2-file-based-instructions.md) | Provide file-scoped conventions the Skill can reference |
| [Prompts](primitive-3-prompts.md) | Sometimes overlap; a Skill can also be exposed through a slash-style experience depending on configuration |
| [Custom Agents](primitive-5-custom-agents.md) | Agents change role; Skills provide the reusable procedure that role may invoke |
| [MCP](primitive-6-mcp.md) | Skills often pair with MCP when the procedure needs access to external systems |

### Using a Skill to Reference File-based Instructions

A Skill defines *how* to carry out a task. File-based Instructions define *what conventions apply* when touching specific files. The most useful composition is a Skill that explicitly tells the agent to read and follow the relevant instruction file as part of its procedure.

This avoids duplicating conventions inside the Skill and keeps the conventions co-located with the code they apply to. The Skill owns the workflow; the instruction file owns the rules.

```markdown
---
name: scaffold-api-route
description: Scaffold a new API route following the project's route conventions. Use when the user asks to create or add a route, endpoint, or handler.
metadata:
  author: platform-team
  version: "1.0"
---

# Scaffold API Route

## Before You Start

Read `.github/instructions/api-routes.instructions.md` before generating any code.
That file defines the validation, error-handling, and documentation conventions
for all files under `src/routes/`. Follow those rules exactly.

## Steps

1. Ask which resource the route serves and which HTTP methods it needs.
2. Create the route handler in `src/routes/{resource}.ts`.
3. Create or update the Zod schema in `src/schemas/{resource}.ts`.
4. Add an OpenAPI JSDoc comment above each handler (per the instruction file).
5. Register the route in `src/routes/index.ts`.
6. Add a co-located test file at `src/routes/__tests__/{resource}.test.ts`.
```

The key line is `Read .github/instructions/api-routes.instructions.md before generating any code.` That tells the agent to load the instruction file as context before it starts writing. The Skill does not repeat the validation rules or error-handling patterns: those live in the instruction file and stay in sync with the code they govern.

This pattern scales cleanly. A deployment Skill can reference `ops.instructions.md`. A test-scaffolding Skill can reference `testing.instructions.md`. The Skill stays focused on the procedure; the instruction file stays focused on the conventions.

### Why This Matters for Code Review

GitHub Copilot code review currently loads only [Always-on Instructions](primitive-1-always-on-instructions.md), [File-based Instructions](primitive-2-file-based-instructions.md), and [Memory](primitive-8-memory.md). It does not load Skills. That means any coding standard that lives only inside a Skill will be enforced when the agent writes code but silently ignored when Copilot reviews a PR.

The practical rule: if a convention matters enough to catch in code review, it must live in an instruction file, not in a Skill. Skills can reference instruction files to stay aligned during agent-assisted coding, but the instruction file is what makes the same standard visible to both pipelines.

This is not a workaround. It is the intended layering. Instruction files own the standards. Skills own the workflows. The instruction file is the contract between writing and reviewing. See [GitHub Copilot Code Review](code-review.md) for the full pipeline details.

## Why Skills Matter in This Guide

Skills are where the guide starts to feel less like static documentation and more like operational knowledge design.

They are also one of the strongest examples of the central claim in this guide: the most useful customization is not just telling GitHub Copilot what the team likes. It is packaging how the team works.

## See It in Action

**See it in action:** [Agent Skills Explained in 5 Minutes | Ep 3 of 8](https://www.youtube.com/watch?v=mPjTZviv23s&t=40s) — Reynald Adolphe demos creating an Agent Skill that updates a README when a project feature changes.

**See it in action:** [The complete guide to Agent Skills](https://www.youtube.com/watch?v=fabAI1OKKww&t=99s) — Burke Holland walks through building a Hello World skill from scratch and shows how skill descriptions trigger the model to load them.

## Creating Skills

In VS Code, run `/create-skill` in Chat. The command scaffolds the folder under `.github/skills/`, writes `SKILL.md` with valid frontmatter, and prompts for the metadata that drives discovery. In the GitHub Copilot CLI, ask the agent to create the Skill directly.

> 💬 **Try this prompt:**
> "Create a skill at `.github/skills/debug-flaky-tests/SKILL.md` that walks through our playbook for diagnosing flaky tests: re-run with `--repeat`, check for unmocked network calls, check test ordering, and bisect with `git`. Write a description that fires when someone asks to debug a flaky test."

## Directory Structure

Every skill lives in its own folder with a `SKILL.md` file:

```text
.github/
└── skills/
    ├── image-manipulation/
    │   └── SKILL.md
    ├── github-issues/
    │   ├── SKILL.md
    │   └── templates/
    │       ├── bug-report.md
    │       └── feature-request.md
    └── web-testing/
        ├── SKILL.md
        └── scripts/
            └── playwright-setup.sh
```

Complex skills include supporting scripts, templates, and reference docs alongside `SKILL.md`.

An agent host is the application that discovers and runs the Skill, such as VS Code, GitHub Copilot CLI, the Cloud Coding Agent, Claude Code, or another skills-compatible runtime. That host determines which Skill locations, tool names, and installation commands apply.

## Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | **Yes** | 1-64 chars, lowercase, hyphens only, must match directory name |
| `description` | **Yes** | 1-1024 chars, describe WHAT it does AND WHEN to use it |
| `argument-hint` | No | Hint text shown in the chat input field when invoked as `/` command |
| `user-invocable` | No | Show as `/` slash command (default: `true`). Set to `false` to hide from the menu while still allowing automatic loading |
| `disable-model-invocation` | No | Require manual `/` invocation only (default: `false`) |
| `context` | No | Experimental. Set to `fork` to run the Skill in a dedicated subagent context. Requires `github.copilot.chat.skillTool.enabled` in VS Code |
| `metadata` | No | Key-value pairs (author, version) |

**Name validation rules:**
- ✅ `image-manipulation`, `github-issues`, `web-testing`
- ❌ `Image-Manipulation` (no uppercase), `-image` (no leading hyphens), `image--manipulation` (no consecutive hyphens)

## Complete Example: GitHub Issues Skill

**Directory:**
```text
github-issues/
├── SKILL.md
└── templates/
    ├── bug-report.md
    └── feature-request.md
```

**SKILL.md:**

``````markdown
---
name: github-issues
description: Create well-structured GitHub issues using team templates. Use when the user wants to file a bug, request a feature, or create any GitHub issue.
metadata:
  author: your-org
  version: "1.0"
---

# GitHub Issue Creation

## When to Use This Skill
- User wants to create a GitHub issue
- User found a bug and wants to report it
- User wants to request a new feature

## Required Tools
This skill works with the GitHub MCP server. Ensure it's configured in `.vscode/mcp.json`.

## Instructions

### For Bug Reports
1. Gather: steps to reproduce, expected vs actual, environment
2. Use the bug report template at `templates/bug-report.md`
3. Create the issue using the GitHub MCP `create_issue` tool

### For Feature Requests
1. Clarify requirements
2. Use the feature template at `templates/feature-request.md`
3. Create the issue with appropriate labels
``````

## Installing Skills with `gh skill`

The GitHub CLI ships `gh skill` (public preview, v2.90.0+) for discovering, installing, and managing skills across agent hosts.

| Command | Purpose |
|---------|---------|
| `gh skill search <query>` | Discover skills across GitHub repositories |
| `gh skill install OWNER/REPO [SKILL]` | Install one or all skills from a repository |
| `gh skill preview OWNER/REPO SKILL` | Inspect contents before installing |
| `gh skill update [NAME]` | Check for upstream changes; `--all` for non-interactive |
| `gh skill publish` | Validate against the agentskills.io spec |

```text
# Install a specific skill pinned to a release
gh skill install github/awesome-copilot documentation-writer --pin v1.2.0

# Install into a different agent host
gh skill install github/awesome-copilot documentation-writer --agent claude-code --scope user
```

Skills are installed into the correct directory for the target host. `--pin <tag>` locks the version; pinned skills are skipped during `gh skill update`.

**Security:** Skills are executable instructions that shape agent behavior. Before installing from a repository you do not control, run `gh skill preview` first and prefer pinned versions.

## Forked Skill Context

By default, a Skill loads inline into the parent agent's context. VS Code 1.118 adds an experimental alternative for large or investigative Skills:

```yaml
---
name: review-pr
description: Review a pull request for code quality, style, and correctness. Use when asked to review a PR.
context: fork
---
```

Use `context: fork` when the Skill needs to read many files, run a lengthy investigation, or produce a focused report whose intermediate context should not crowd the parent conversation. Only the final result returns to the parent agent. This requires the `github.copilot.chat.skillTool.enabled` setting in VS Code and should be treated as preview behavior.

## Skills vs. MCP: Complementary, Not Competing

- **Skills** provide *knowledge*: templates, conventions, workflows, domain expertise
- **MCP servers** provide *access*: authentication, API connections, live system interaction

Most serious integrations use both: an MCP server handles "how to connect to Jira" while a skill handles "how our team formats Jira tickets."

## Where to Read Next

- Read [Custom Agents](primitive-5-custom-agents.md) next if the workflow needs a persistent role in addition to reusable procedure.
- Read [MCP](primitive-6-mcp.md) after that if the procedure also needs external reach.
