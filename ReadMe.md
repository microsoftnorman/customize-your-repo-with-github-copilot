# The Definitive Guide to Customizing GitHub Copilot

*Updated: April 16, 2026. File paths, configuration options, and feature availability may change as Copilot evolves—always verify against the [official documentation](https://code.visualstudio.com/docs/copilot).*

GitHub Copilot is GitHub's platform for agentic software development. When properly configured, it becomes a context-aware development partner that understands your architecture, follows your conventions, and produces code that passes review on the first try.

This guide is the complete reference for GitHub Copilot's customization primitives—the configuration files and patterns that transform Copilot from a generic platform into one that knows your codebase.

---

## Table of Contents

- [Who This Guide Is For](#who-this-guide-is-for)
- [What You'll Learn](#what-youll-learn)
- [The Primitives](#the-primitives) — the eight customization primitives at a glance
- [Platform Extensions](#platform-extensions) — Agentic Workflows and the Copilot SDK
- [Guide Structure](#guide-structure) — how Parts I, II, and III fit together
- [Find What You Need Fast](#find-what-you-need-fast) — task-based entry points
- [Getting Started](#getting-started) — the 5-minute quick start
- [Data Collection Notice](#data-collection-notice)
- [Resources](#resources)

---

## Who This Guide Is For

This guide is written for developers and engineering leads who want to maximize the value of GitHub Copilot across their projects and teams. Whether you're a solo developer looking to reduce repetitive prompting, or a team lead standardizing AI-assisted workflows across an organization, you'll find actionable guidance here.

Examples focus on [**VS Code**](docs/surfaces/vscode.md), [**GitHub Copilot CLI**](docs/surfaces/copilot-cli.md), and the [**Copilot cloud coding agent**](docs/surfaces/cloud-coding-agent.md) — the three surfaces with the deepest customization support today. GitHub Copilot also runs in [**Visual Studio**](docs/surfaces/visual-studio.md), [**JetBrains IDEs**](docs/surfaces/jetbrains.md), [**Eclipse**](docs/surfaces/eclipse.md), and [**Xcode**](docs/surfaces.md#xcode), and the core theory in this guide — instructions, prompts, skills, agents, MCP, hooks, memory — applies in a similar fashion wherever Copilot runs. Surface-specific feature gaps are called out in the [per-surface reference](docs/surfaces.md).

This is a guide for humans. It is written to be read start-to-finish or dipped into by section. Copilot itself is a useful companion when working through it, but nothing here assumes you'll hand the reading off to an agent.

The Copilot product evolves quickly — features ship weekly, defaults change, and settings get renamed. Always verify specifics against the [official documentation](https://code.visualstudio.com/docs/copilot) before committing a pattern to production. This guide is refreshed on a roughly weekly cadence; the date at the top of the file tells you how current you are.

**Time investment:** Plan for 1-2 hours to read through the foundations and primitive documentation. The return on that investment compounds with every Copilot interaction thereafter.

---

## What You'll Learn

By the end of this guide, you will understand:

- **Why customization matters** — The difference between fighting Copilot and working with it
- **The customization primitives** — What each configuration type does, when it activates, and when to use it
- **Platform extensions** — How Agentic Workflows and the Copilot SDK take customization beyond the IDE
- **How primitives layer** — The mental model for how instructions, prompts, skills, agents, and MCP combine
- **Practical patterns** — Ready-to-use templates and real-world examples
- **Iteration strategies** — How to refine your configuration based on feedback
- **Measurement approaches** — How to track whether customization is working

**Terminology:** Throughout this guide, *agent* refers to Copilot operating in agentic mode — autonomously planning, executing tool calls, and iterating on results. A *custom agent* is a user-defined persona file that configures Copilot's behavior for a specific role. *Primitives* are the configuration file types that customize Copilot.

**See it in action:** [VS Code Live: Agent Sessions Day](https://www.youtube.com/watch?v=tAezuMSJuFs&t=1152s) — Harald Kirschner opens the keynote with a tour of the Copilot agent platform, followed by deep-dives on every primitive covered in this guide.

You can start anywhere using the table of contents below, but if you're new to Copilot customization, start with [Part I: Foundations](docs/part-1-foundations.md).

---

## The Primitives

GitHub Copilot provides eight customization primitives — configuration files and integrations that shape how Copilot understands your codebase. Each serves a distinct purpose and loads at different points in your workflow:

**See it in action:** [VS Code Live: Agent Sessions Day — Customize Your Agents](https://www.youtube.com/watch?v=tAezuMSJuFs&t=10598s) — Courtney Webster demos instructions, prompts, skills, and custom agents end-to-end.

| Primitive | Location | Purpose | Jump to |
|-----------|----------|---------|---------|
| [**Always-on Instructions**](docs/primitive-1-always-on-instructions.md) | `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md` | Global rules applied to every Copilot request | [When to use](docs/primitive-1-always-on-instructions.md#when-to-use-always-on-instructions) · [Anatomy](docs/primitive-1-always-on-instructions.md#anatomy-of-effective-instructions) · [Full example](docs/primitive-1-always-on-instructions.md#complete-example-production-nextjs-project) |
| [**File-based Instructions**](docs/primitive-2-file-based-instructions.md) | `.github/instructions/*.instructions.md` | Rules that activate when working with specific file patterns | [Glob patterns](docs/part-3-reference.md#glob-pattern-reference) · [Frontmatter](docs/part-3-reference.md#frontmatter-reference) |
| [**Prompts**](docs/primitive-3-prompts.md) | `.github/prompts/*.prompt.md` | Reusable task templates invoked as slash commands | [Execution modes](docs/part-3-reference.md#execution-modes) · [Available tools](docs/part-3-reference.md#available-tools) |
| [**Skills**](docs/primitive-4-skills.md) | `.github/skills/*/SKILL.md` | Procedural knowledge Copilot can discover and apply | [Overview](docs/primitive-4-skills.md#overview) |
| [**Custom Agents**](docs/primitive-5-custom-agents.md) | `.github/agents/*.md` | Specialized AI personas with defined behaviors | [Overview](docs/primitive-5-custom-agents.md#overview) · [Frontmatter](docs/part-3-reference.md#frontmatter-reference) |
| [**MCP (Model Context Protocol)**](docs/primitive-6-mcp.md) | `.vscode/mcp.json` | Connections to external tools, APIs, and data sources | [Configuration](docs/part-3-reference.md#mcp-configuration) · [Credentials](docs/primitive-6-mcp.md#credential-management) · [Tutorial](docs/primitive-6-mcp.md#end-to-end-tutorial-adding-a-github-mcp-server) |
| [**Hooks (Preview)**](docs/primitive-7-hooks.md) | `.github/hooks/*.json` | Runtime enforcement and audit logging for agent sessions | [Configuration](docs/part-3-reference.md#hooks-configuration-preview) |
| [**Memory (Preview)**](docs/primitive-8-memory.md) | GitHub cloud (repository-scoped) | Learned codebase knowledge that persists across sessions | [Overview](docs/primitive-8-memory.md) |

Understanding when and how to use each primitive is the core of this guide. For how they combine in practice, see [How Primitives Layer Together](docs/part-2-primitives.md#how-primitives-layer-together) and [Composition Patterns](docs/part-2-primitives.md#composition-patterns).

**Not sure which primitive to use?** Jump to the [Quick Decision Guide](docs/part-3-reference.md#quick-decision-guide). **Want to bundle them?** See [Agent Plugins (Preview)](docs/part-2-primitives.md#agent-plugins-preview).

---

## Platform Extensions

Beyond the primitives, two platform extensions take Copilot beyond the IDE — into CI/CD pipelines and custom applications:

| Extension | Location | Purpose |
|-----------|----------|---------|
| [**Agentic Workflows (Preview)**](docs/agentic-workflows.md) | `.github/workflows/*.md` | Continuous AI via coding agents in GitHub Actions |
| [**Copilot SDK (Preview)**](docs/copilot-sdk.md) | External dependency (npm, pip, etc.) | Embed the Copilot agent runtime in your own tools and applications |

These are not configuration primitives — they don't shape what Copilot knows about your codebase. Instead, they extend Copilot's reach into new environments. Both can be customized using the same primitives covered in this guide: your instructions, skills, and agents are consumed by Agentic Workflows when the coding agent runs in GitHub Actions, and by the Copilot SDK when you embed the runtime in your own tools. Everything you learn in Part II applies to these extensions too.

---

## Guide Structure

### Part I: Foundations

Start here. Part I is split into two halves:

- [**What Copilot Is**](docs/part-1-foundations.md) — the platform, [the surfaces it runs on](docs/part-1-foundations.md#where-github-copilot-runs), [the models](docs/part-1-foundations.md#model-selection), [the plans](docs/part-1-foundations.md#plans), and the [enterprise policy hierarchy](docs/part-1-foundations.md#enterprise-policy-hierarchy).
- [**Why Customize**](docs/part-1b-why-customize.md) — [Copilot without customization](docs/part-1b-why-customize.md#github-copilot-without-customization), [why customize](docs/part-1b-why-customize.md#why-customize), [iteration and fine-tuning](docs/part-1b-why-customize.md#iteration-and-fine-tuning), [measuring success](docs/part-1b-why-customize.md#measuring-success), [rolling out to your team](docs/part-1b-why-customize.md#rolling-out-to-your-team), and [best practices](docs/part-1b-why-customize.md#best-practices).

### [Part II: The Primitives](docs/part-2-primitives.md)

The heart of the guide. Each primitive gets comprehensive coverage — syntax, configuration, examples, patterns, and guidance on when to use it versus alternatives.

- [Primitive 1: Always-on Instructions](docs/primitive-1-always-on-instructions.md) — Your codebase's global rules
- [Primitive 2: File-based Instructions](docs/primitive-2-file-based-instructions.md) — Context-specific guidance
- [Primitive 3: Prompts](docs/primitive-3-prompts.md) — Reusable slash commands
- [Primitive 4: Skills](docs/primitive-4-skills.md) — Discoverable procedural knowledge
- [Primitive 5: Custom Agents](docs/primitive-5-custom-agents.md) — Specialized AI personas
- [Primitive 6: MCP](docs/primitive-6-mcp.md) — External tool integration
- [Primitive 7: Hooks](docs/primitive-7-hooks.md) — Runtime enforcement and audit logging
- [Primitive 8: Copilot Memory](docs/primitive-8-memory.md) — Automatic repository-level learning

**Platform Extensions:**

- [Agentic Workflows](docs/agentic-workflows.md) — Continuous AI via coding agents in GitHub Actions
- [Copilot SDK](docs/copilot-sdk.md) — Embed the agent runtime in your own tools

### [Part III: Reference](docs/part-3-reference.md)

Quick reference tables, starter templates, and configuration reference for all primitives and platform extensions.

- [Quick Reference: File Locations](docs/part-3-reference.md#quick-reference-file-locations)
- [When Primitives Load](docs/part-3-reference.md#when-primitives-load)
- [Cross-Surface Primitive Support Matrix](docs/part-3-reference.md#cross-surface-primitive-support-matrix)
- [Frontmatter Reference](docs/part-3-reference.md#frontmatter-reference) — every field, every primitive
- [Quick Decision Guide](docs/part-3-reference.md#quick-decision-guide) — pick the right primitive for a task
- [Debugging: What's Loaded?](docs/part-3-reference.md#debugging-whats-loaded)
- [Anti-Patterns to Avoid](docs/part-3-reference.md#anti-patterns-to-avoid)
- [Starter Templates](docs/part-3-reference.md#starter-templates)

---

## Find What You Need Fast

Task-based entry points for common scenarios:

| I want to... | Go to |
|--------------|-------|
| Add my first customization file | [5-Minute Quick Start](#5-minute-quick-start) |
| Understand *why* customization matters | [GitHub Copilot Without Customization](docs/part-1b-why-customize.md#github-copilot-without-customization) |
| Pick the right primitive for a job | [Quick Decision Guide](docs/part-3-reference.md#quick-decision-guide) |
| Learn the frontmatter for any primitive | [Frontmatter Reference](docs/part-3-reference.md#frontmatter-reference) |
| Know which primitives work in my IDE | [Cross-Surface Support Matrix](docs/part-3-reference.md#cross-surface-primitive-support-matrix) |
| See every primitive's feature support in one table | [IDE Surfaces overview](docs/surfaces.md) |
| Debug why a primitive isn't loading | [Debugging: What's Loaded?](docs/part-3-reference.md#debugging-whats-loaded) |
| Avoid common mistakes | [Anti-Patterns to Avoid](docs/part-3-reference.md#anti-patterns-to-avoid) |
| Copy a working starting point | [Starter Templates](docs/part-3-reference.md#starter-templates) |
| Connect Copilot to an external API or database | [MCP Configuration](docs/part-3-reference.md#mcp-configuration) · [MCP Tutorial](docs/primitive-6-mcp.md#end-to-end-tutorial-adding-a-github-mcp-server) |
| Build a specialized agent persona | [Custom Agents](docs/primitive-5-custom-agents.md) |
| Enforce runtime rules and audit logs | [Hooks (Preview)](docs/primitive-7-hooks.md) |
| Run AI continuously in CI/CD | [Agentic Workflows](docs/agentic-workflows.md) |
| Embed the agent runtime in my own app | [Copilot SDK](docs/copilot-sdk.md) |
| Roll out customization to my team | [Rolling Out to Your Team](docs/part-1b-why-customize.md#rolling-out-to-your-team) |
| Measure whether customization is working | [Measuring Success](docs/part-1b-why-customize.md#measuring-success) |

---

## Getting Started

### 5-Minute Quick Start

Create one file and get immediate value. Add `.github/copilot-instructions.md` to your repository root:

```markdown
# Copilot Instructions

## Tech Stack
- TypeScript with React 19
- Vitest for testing
- React Query for server state (not Redux)
- date-fns for dates (not moment.js)

## Conventions
- Functional components only — no class components
- All API responses use the ApiResponse<T> wrapper in src/types/
- Tests live next to the code they test (e.g., Button.test.tsx)

## Do Not
- Do not use any deprecated libraries listed in DEPRECATED.md
- Do not add console.log to production code
```

Replace the specifics with your stack and conventions. Commit the file and every Copilot Chat interaction in the repo will follow these rules. This single file eliminates the most common source of Copilot friction — suggestions that use the wrong libraries, patterns, or conventions.

For the full guide, start with [Part I: Foundations](docs/part-1-foundations.md), then work through the primitives in order — each builds on the previous.

For teams, consider reading individually first, then convening to discuss which primitives fit your workflows.

---

## Data Collection Notice

Starting April 24, 2026, GitHub uses Copilot interaction data from Free, Pro, and Pro+ accounts to train AI models by default. Users can opt out in [Copilot privacy settings](https://github.com/settings/copilot). Business and Enterprise plans are exempt from this policy. For details, see [GitHub's announcement](https://github.blog/changelog/label/copilot/).

---

## Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot Extension](https://code.visualstudio.com/docs/copilot)
- [GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) — Use Copilot as an AI agent directly from your terminal (GA since February 2026)
- [Copilot SDK](https://github.com/github/copilot-sdk) — Embed the Copilot agent runtime in your own applications (public preview)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Agent Skills Specification](https://agentskills.io) — Open standard for portable agent capabilities
- [Agent Plugins](https://code.visualstudio.com/docs/copilot/customization/agent-plugins) — Bundle skills, agents, hooks, and MCP servers into installable packages (preview)
- [Copilot Memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory) — Automatic repository-level learning that complements explicit customization
- [GitHub Agentic Workflows](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/) — Continuous AI via coding agents in GitHub Actions
- [VS Code 1.116 Release Notes](https://code.visualstudio.com/updates/v1_116) — Latest VS Code release with Copilot built-in
- [VS Code Source Code](https://github.com/microsoft/vscode) — The authoritative reference when documentation is unclear
- [Copilot Spaces](https://docs.github.com/en/copilot/how-tos/provide-context/use-copilot-spaces) — Organize relevant context into Spaces that ground Copilot's responses for specific tasks
- [product-brain](https://github.com/digitarald/product-brain) — A product management approach to workspace instructions
