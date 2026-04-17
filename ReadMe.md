# The Definitive Guide to Customizing GitHub Copilot

*Updated: April 17, 2026. File paths, configuration options, and feature availability may change as Copilot evolves. Always verify against the [official documentation](https://code.visualstudio.com/docs/copilot).*

GitHub Copilot is GitHub's platform for agentic software development. When properly configured, it becomes a context-aware development partner that understands your architecture, follows your conventions, and produces code that fits your codebase.

This guide is the complete reference for GitHub Copilot's customization primitives: the configuration files and patterns that teach Copilot how your codebase works.

---

## Table of Contents

- [Who This Guide Is For](#who-this-guide-is-for)
- [What You'll Learn](#what-youll-learn)
- [The Primitives](#the-primitives): the eight customization primitives at a glance
- [Platform Extensions](#platform-extensions): Agentic Workflows and the Copilot SDK
- [Guide Structure](#guide-structure): how Parts I, II, and III fit together
- [Find What You Need Fast](#find-what-you-need-fast): task-based entry points
- [Getting Started](#getting-started)
- [Data Collection Notice](#data-collection-notice)
- [Resources](#resources)

---

## Who This Guide Is For

This guide is written for developers and engineering leads who want to maximize the value of GitHub Copilot across their projects and teams. Whether you're a solo developer looking to reduce repetitive prompting, or a team lead standardizing AI-assisted workflows across an organization, you'll find actionable guidance here.

Examples focus on [**VS Code**](docs/surfaces/vscode.md), [**GitHub Copilot CLI**](docs/surfaces/copilot-cli.md), and the [**Copilot cloud coding agent**](docs/surfaces/cloud-coding-agent.md). Those three surfaces have the deepest customization support today. GitHub Copilot also runs in [**Visual Studio**](docs/surfaces/visual-studio.md), [**JetBrains IDEs**](docs/surfaces/jetbrains.md), [**Eclipse**](docs/surfaces/eclipse.md), and [**Xcode**](docs/surfaces/xcode.md), and the core theory in this guide (instructions, prompts, skills, agents, MCP, hooks, memory) applies in a similar fashion wherever Copilot runs. Surface-specific feature gaps are called out in the [per-surface reference](docs/surfaces.md).

This is a guide for humans. It is written to be read start-to-finish or dipped into by section. Copilot itself is a useful companion when working through it, but nothing here assumes you'll hand the reading off to an agent.

The Copilot product evolves quickly. Features ship weekly, defaults change, and settings get renamed. Always verify specifics against the [official documentation](https://code.visualstudio.com/docs/copilot) before committing a pattern to production. This guide is refreshed on a roughly weekly cadence; the date at the top of the file tells you how current you are.

**Time investment:** Plan for 1-2 hours to read through the foundations and primitive documentation. That investment pays back across the Copilot work you do afterward.

---

## What You'll Learn

By the end of this guide, you will understand:

- **Why customization matters:** The difference between fighting Copilot and working with it
- **The customization primitives:** What each configuration type does, when it activates, and when to use it
- **Platform extensions:** How Agentic Workflows and the Copilot SDK take customization beyond the IDE
- **How primitives layer:** The mental model for how instructions, prompts, skills, agents, and MCP combine
- **Practical patterns:** Ready-to-use templates and real-world examples
- **Iteration strategies:** How to refine your configuration based on feedback
- **Measurement approaches:** How to track whether customization is working

**Terminology:** Throughout this guide, *agent* refers to Copilot operating in agentic mode — autonomously planning, executing tool calls, and iterating on results. A *custom agent* is a user-defined persona file that configures Copilot's behavior for a specific role. *Primitives* are the configuration file types that customize Copilot.

**See it in action:** [VS Code Live: Agent Sessions Day](https://www.youtube.com/watch?v=tAezuMSJuFs&t=1152s). Harald Kirschner opens the keynote with a tour of the Copilot agent platform, followed by deep-dives on every primitive covered in this guide.

You can start anywhere using the table of contents below, but if you're new to Copilot customization, start with [Part I: Foundations](docs/part-1-foundations.md).

---

## The Primitives

GitHub Copilot provides eight customization primitives: configuration files and integrations that shape how Copilot understands your codebase. Each serves a distinct purpose and loads at different points in your workflow:

**See it in action:** [VS Code Live: Agent Sessions Day — Customize Your Agents](https://www.youtube.com/watch?v=tAezuMSJuFs&t=10598s). Courtney Webster demos instructions, prompts, skills, and custom agents end-to-end.

| Primitive | Location | Purpose | Plan availability | Jump to |
|-----------|----------|---------|-------------------|---------|
| [**Always-on Instructions**](docs/primitive-1-always-on-instructions.md) | `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md` | Global rules applied to every Copilot request | All plans (incl. Free) | [When to use](docs/primitive-1-always-on-instructions.md#when-to-use-always-on-instructions) · [Anatomy](docs/primitive-1-always-on-instructions.md#anatomy-of-effective-instructions) · [Full example](docs/primitive-1-always-on-instructions.md#complete-example-production-nextjs-project) |
| [**File-based Instructions**](docs/primitive-2-file-based-instructions.md) | `.github/instructions/*.instructions.md` | Rules that activate when working with specific file patterns | All plans | [Glob patterns](docs/part-3-reference.md#glob-pattern-reference) · [Frontmatter](docs/part-3-reference.md#frontmatter-reference) |
| [**Prompts**](docs/primitive-3-prompts.md) | `.github/prompts/*.prompt.md` | Reusable task templates invoked as slash commands | All plans | [Execution modes](docs/part-3-reference.md#execution-modes) · [Available tools](docs/part-3-reference.md#available-tools) |
| [**Skills**](docs/primitive-4-skills.md) | `.github/skills/*/SKILL.md` | Procedural knowledge Copilot can discover and apply | All plans | [Overview](docs/primitive-4-skills.md#overview) |
| [**Custom Agents**](docs/primitive-5-custom-agents.md) | `.github/agents/*.md` | Specialized AI personas with defined behaviors | All plans | [Overview](docs/primitive-5-custom-agents.md#overview) · [Frontmatter](docs/part-3-reference.md#frontmatter-reference) |
| [**MCP (Model Context Protocol)**](docs/primitive-6-mcp.md) | `.vscode/mcp.json` | Connections to external tools, APIs, and data sources | All plans | [Configuration](docs/part-3-reference.md#mcp-configuration) · [Credentials](docs/primitive-6-mcp.md#credential-management) · [Tutorial](docs/primitive-6-mcp.md#end-to-end-tutorial-adding-a-github-mcp-server) |
| [**Hooks (Preview)**](docs/primitive-7-hooks.md) | `.github/hooks/*.json` | Runtime enforcement and audit logging for agent sessions | Pro, Pro+, Business, Enterprise | [Configuration](docs/part-3-reference.md#hooks-configuration-preview) |
| [**Memory (Preview)**](docs/primitive-8-memory.md) | GitHub cloud (repository-scoped) | Learned codebase knowledge that persists across sessions | Pro/Pro+ (on by default); Business/Enterprise (admin toggle) | [Overview](docs/primitive-8-memory.md) |

**Plan notes:** The six core primitives (instructions, file-based instructions, prompts, skills, custom agents, MCP) work on every plan including Copilot Free. Hooks and Memory require a paid plan. See [Plans](docs/part-1-foundations.md#plans) for the full breakdown, and the [Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix) for the live availability grid.

Understanding when and how to use each primitive is the core of this guide. For how they combine in practice, see [How Primitives Layer Together](docs/part-2-primitives.md#how-primitives-layer-together) and [Composition Patterns](docs/part-2-primitives.md#composition-patterns).

**Not sure which primitive to use?** Jump to the [Quick Decision Guide](docs/part-3-reference.md#quick-decision-guide). **Want to bundle them?** See [Agent Plugins (Preview)](docs/part-2-primitives.md#agent-plugins-preview).

---

## Platform Extensions

Beyond the primitives, two platform extensions take Copilot beyond the IDE, into CI/CD pipelines and custom applications:

| Extension | Location | Purpose |
|-----------|----------|---------|
| [**Agentic Workflows (Preview)**](docs/agentic-workflows.md) | `.github/workflows/*.md` | Continuous AI via coding agents in GitHub Actions |
| [**Copilot SDK (Preview)**](docs/copilot-sdk.md) | External dependency (npm, pip, etc.) | Embed the Copilot agent runtime in your own tools and applications |
| [**Code Review**](docs/code-review.md) | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` | Automated PR review steered by your instruction files |

These are not configuration primitives. They don't shape what Copilot knows about your codebase. Instead, they extend Copilot's reach into new environments. Both can be customized using the same primitives covered in this guide: your instructions, skills, and agents are consumed by Agentic Workflows when the coding agent runs in GitHub Actions, and by the Copilot SDK when you embed the runtime in your own tools. Everything you learn in Part II applies to these extensions too.

---

## Guide Structure

### Part I: Foundations

Start here. Part I has two core chapters plus a dedicated measurement guide:

- [**What Copilot Is**](docs/part-1-foundations.md): the platform, [the surfaces it runs on](docs/part-1-foundations.md#where-github-copilot-runs), [the models](docs/part-1-foundations.md#model-selection), [the plans](docs/part-1-foundations.md#plans), and the [enterprise policy hierarchy](docs/part-1-foundations.md#enterprise-policy-hierarchy).
- [**Why Customize**](docs/part-1b-why-customize.md): [Copilot without customization](docs/part-1b-why-customize.md#github-copilot-without-customization), [why customize](docs/part-1b-why-customize.md#why-customize), [iteration and fine-tuning](docs/part-1b-why-customize.md#iteration-and-fine-tuning), [rolling out to your team](docs/part-1b-why-customize.md#rolling-out-to-your-team), [scaling beyond one team](docs/part-1b-why-customize.md#scaling-beyond-one-team), and [best practices](docs/part-1b-why-customize.md#best-practices).
- [**Measuring Success**](docs/measuring-success.md): Goal-Question-Metric, value stream mapping, outward-facing versus inward-facing metrics, toil reduction, and the operating model for proving business impact.

### [Part II: The Primitives](docs/part-2-primitives.md)

The heart of the guide. Each primitive gets a full chapter covering syntax, configuration, examples, patterns, and guidance on when to use it versus alternatives.

- [Primitive 1: Always-on Instructions](docs/primitive-1-always-on-instructions.md): Your codebase's global rules
- [Primitive 2: File-based Instructions](docs/primitive-2-file-based-instructions.md): Context-specific guidance
- [Primitive 3: Prompts](docs/primitive-3-prompts.md): Reusable slash commands
- [Primitive 4: Skills](docs/primitive-4-skills.md): Discoverable procedural knowledge
- [Primitive 5: Custom Agents](docs/primitive-5-custom-agents.md): Specialized AI personas
- [Primitive 6: MCP](docs/primitive-6-mcp.md): External tool integration
- [Primitive 7: Hooks](docs/primitive-7-hooks.md): Runtime enforcement and audit logging
- [Primitive 8: Copilot Memory](docs/primitive-8-memory.md): Automatic repository-level learning

**Platform Extensions:**

- [Agentic Workflows](docs/agentic-workflows.md): Continuous AI via coding agents in GitHub Actions
- [Copilot SDK](docs/copilot-sdk.md): Embed the agent runtime in your own tools
- [Code Review](docs/code-review.md): Automated PR review steered by your instruction files

### [Part III: Reference](docs/part-3-reference.md)

Quick reference tables, starter templates, and configuration reference for all primitives and platform extensions.

- [Quick Reference: File Locations](docs/part-3-reference.md#quick-reference-file-locations)
- [When Primitives Load](docs/part-3-reference.md#when-primitives-load)
- [Cross-Surface Primitive Support Matrix](docs/part-3-reference.md#cross-surface-primitive-support-matrix)
- [Frontmatter Reference](docs/part-3-reference.md#frontmatter-reference): every field, every primitive
- [Quick Decision Guide](docs/part-3-reference.md#quick-decision-guide): pick the right primitive for a task
- [Debugging: What's Loaded?](docs/part-3-reference.md#debugging-whats-loaded)
- [Anti-Patterns to Avoid](docs/part-3-reference.md#anti-patterns-to-avoid)
- [Starter Templates](docs/part-3-reference.md#starter-templates)

---

## Find What You Need Fast

Common problems and where in the guide to read about them.

| Problem | Where in the guide |
|---------|--------------------|
| Copilot keeps picking the wrong libraries and patterns for my codebase | [Creating an Instructions File](docs/primitive-1-always-on-instructions.md#creating-an-instructions-file) |
| I don't understand why customization matters in the first place | [GitHub Copilot Without Customization](docs/part-1b-why-customize.md#github-copilot-without-customization) |
| I have too many primitives to choose from and don't know which fits my use case | [Quick Decision Guide](docs/part-3-reference.md#quick-decision-guide) |
| Rules should only apply to certain files (tests, SQL, backend, etc.), not the whole repo | [File-based Instructions](docs/primitive-2-file-based-instructions.md) · [Glob patterns](docs/part-3-reference.md#glob-pattern-reference) |
| My team keeps typing the same 10-line prompt over and over | [Prompts](docs/primitive-3-prompts.md) |
| I want Copilot to follow a multi-step procedure (deploy, scaffold a component, run a checklist) | [Skills](docs/primitive-4-skills.md) |
| Different tasks need different personas (reviewer, architect, security auditor) | [Custom Agents](docs/primitive-5-custom-agents.md) |
| Copilot can't see my issue tracker, database, or internal API | [MCP Tutorial](docs/primitive-6-mcp.md#end-to-end-tutorial-adding-a-github-mcp-server) · [MCP Configuration](docs/part-3-reference.md#mcp-configuration) |
| Agents sometimes run commands or touch files they shouldn't | [Hooks (Preview)](docs/primitive-7-hooks.md) |
| Copilot forgets context across sessions, so I have to re-explain the codebase every time | [Copilot Memory](docs/primitive-8-memory.md) |
| I forget the frontmatter fields for instructions / prompts / skills / agents | [Frontmatter Reference](docs/part-3-reference.md#frontmatter-reference) |
| My team uses JetBrains / Visual Studio / Xcode / Eclipse. What's supported there? | [Cross-Surface Support Matrix](docs/part-3-reference.md#cross-surface-primitive-support-matrix) · [IDE Surfaces overview](docs/surfaces.md) |
| I added an instructions file but Copilot isn't picking it up | [Debugging: What's Loaded?](docs/part-3-reference.md#debugging-whats-loaded) |
| I want to avoid the most common pitfalls before I write anything | [Anti-Patterns to Avoid](docs/part-3-reference.md#anti-patterns-to-avoid) |
| I don't want to write customization from scratch | [Starter Templates](docs/part-3-reference.md#starter-templates) |
| I want AI to run on my repo continuously: triage issues, review PRs, maintain docs | [Agentic Workflows](docs/agentic-workflows.md) |
| I want to embed the Copilot agent runtime inside my own product or tool | [Copilot SDK](docs/copilot-sdk.md) |
| I want Copilot to review pull requests against my team's rules and conventions | [Code Review](docs/code-review.md) |
| I'm ready to roll this out to my team but don't know where to start | [Rolling Out to Your Team](docs/part-1b-why-customize.md#rolling-out-to-your-team) |
| I need to scale customization across many teams without forcing uniformity | [Scaling Beyond One Team](docs/part-1b-why-customize.md#scaling-beyond-one-team) |
| My leadership wants to know whether Copilot is actually paying off | [Measuring Success](docs/measuring-success.md) |

---

## Getting Started

Start with [Part I: Foundations](docs/part-1-foundations.md), then work through the primitives in order. Each builds on the previous. To bootstrap your first customization file, see [Creating an Instructions File](docs/primitive-1-always-on-instructions.md#creating-an-instructions-file); it covers `/init` in VS Code and the Copilot CLI, `/generateInstructions` in Visual Studio, and manual authoring for every other surface.

Before authoring anything by hand, read [Don't Hand-Type Primitives — Let the Helmsman Repeat the Order](docs/part-2-primitives.md#dont-hand-type-primitives--let-the-helmsman-repeat-the-order). The short version: use the built-in `/create-instruction`, `/create-prompt`, `/create-skill`, `/create-agent`, and `/create-hook` commands to scaffold primitives, then refine the draft. Silent activation failures from a hand-typed path, extension, or glob are the most common reason a primitive doesn't work.

For teams, consider reading individually first, then convening to discuss which primitives fit your workflows.

---

## Data Collection Notice

Starting April 24, 2026, GitHub uses Copilot interaction data from Free, Pro, and Pro+ accounts to train AI models by default. Users can opt out in [Copilot privacy settings](https://github.com/settings/copilot). Business and Enterprise plans are exempt from this policy. For details, see [GitHub's announcement](https://github.blog/changelog/label/copilot/).

---

## Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot Extension](https://code.visualstudio.com/docs/copilot)
- [GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli): Use Copilot as an AI agent directly from your terminal (GA since February 2026)
- [Copilot SDK](https://github.com/github/copilot-sdk): Embed the Copilot agent runtime in your own applications (public preview)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Agent Skills Specification](https://agentskills.io): Open standard for portable agent capabilities
- [Agent Plugins](https://code.visualstudio.com/docs/copilot/customization/agent-plugins): Bundle skills, agents, hooks, and MCP servers into installable packages (preview)
- [Copilot Memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory): Automatic repository-level learning that complements explicit customization
- [GitHub Agentic Workflows](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/): Continuous AI via coding agents in GitHub Actions
- [VS Code 1.116 Release Notes](https://code.visualstudio.com/updates/v1_116): Latest VS Code release with Copilot built-in
- [VS Code Source Code](https://github.com/microsoft/vscode): The authoritative reference when documentation is unclear
- [Copilot Spaces](https://docs.github.com/en/copilot/how-tos/provide-context/use-copilot-spaces): Organize relevant context into Spaces that ground Copilot's responses for specific tasks
- [product-brain](https://github.com/digitarald/product-brain): A product management approach to workspace instructions

### Recommended Video Channels

The guide's "See it in action" links point to demos on these two official channels. Subscribe to stay current on new Copilot features.

- [**@code** on YouTube](https://www.youtube.com/@code): The official Visual Studio Code channel. Livestreams, release-note walkthroughs, and deep-dives from the VS Code and Copilot teams.
- [**@GitHub** on YouTube](https://www.youtube.com/@GitHub): The official GitHub channel. Product announcements, Copilot demos, and GitHub Universe sessions.

### Recommended X / Twitter Accounts

Official product and team accounts for real-time announcements, changelog updates, and behind-the-scenes commentary.

**Organizations**

- [**@github**](https://x.com/github): GitHub's official account. Release announcements and Copilot news.
- [**@GitHubNext**](https://x.com/githubnext): GitHub Next. Experimental features and research previews (agentic workflows, coding agents).
- [**@code**](https://x.com/code): Visual Studio Code. Release highlights, tips, and Copilot integration updates.
- [**@VisualStudio**](https://x.com/visualstudio): Visual Studio. .NET and Copilot in Visual Studio.

**GitHub Copilot and VS Code team members**

- [**@martinwoodward**](https://x.com/martinwoodward): Martin Woodward, VP of DevRel, GitHub.
- [**@digitarald**](https://x.com/digitarald): Harald Kirschner, Principal PM, GitHub Copilot and VS Code.
- [**@pierceboggan**](https://x.com/pierceboggan): Pierce Boggan, Group PM, VS Code.
- [**@burkeholland**](https://x.com/burkeholland): Burke Holland, Principal Cloud Advocate.
