# The Definitive Guide to Customizing GitHub Copilot

*Published: February 10, 2026. Updated: April 15, 2026. File paths, configuration options, and feature availability may change as Copilot evolves—always verify against the [official documentation](https://code.visualstudio.com/docs/copilot).*

GitHub Copilot is more than autocomplete. When properly configured, it becomes a context-aware development partner that understands your architecture, follows your conventions, and produces code that passes review on the first try.

This guide is the complete reference for GitHub Copilot's customization primitives—the configuration files and patterns that transform Copilot from a generic AI assistant into a team member who knows your codebase.

---

## Who This Guide Is For

This guide is written for developers and engineering leads who want to maximize the value of GitHub Copilot across their projects and teams. Whether you're a solo developer looking to reduce repetitive prompting, or a team lead standardizing AI-assisted workflows across an organization, you'll find actionable guidance here.

**Time investment:** Plan for 1-2 hours to read through the foundations and primitive documentation. The return on that investment compounds with every Copilot interaction thereafter.

---

## What You'll Learn

By the end of this guide, you will understand:

- **Why customization matters** — The difference between fighting Copilot and working with it
- **The customization primitives** — What each configuration type does, when it activates, and when to use it
- **How primitives layer** — The mental model for how instructions, prompts, skills, agents, and MCP combine
- **Practical patterns** — Ready-to-use templates and real-world examples
- **Iteration strategies** — How to refine your configuration based on feedback
- **Measurement approaches** — How to track whether customization is working

**Terminology:** Throughout this guide, *agent* refers to Copilot operating in agentic mode — autonomously planning, executing tool calls, and iterating on results. A *custom agent* is a user-defined persona file that configures Copilot's behavior for a specific role. *Primitives* are the configuration file types that customize Copilot.

You can start anywhere using the table of contents below, but if you're new to Copilot customization, start with [Part I: Foundations](docs/part-1-foundations.md).

---

## The Primitives

GitHub Copilot provides ten customization primitives. Each serves a distinct purpose and loads at different points in your workflow:

| Primitive | Location | Purpose |
|-----------|----------|---------|
| [**Always-on Instructions**](docs/primitive-1-always-on-instructions.md) | `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md` | Global rules applied to every Copilot request |
| [**File-based Instructions**](docs/primitive-2-file-based-instructions.md) | `.github/instructions/*.instructions.md` | Rules that activate when working with specific file patterns |
| [**Prompts**](docs/primitive-3-prompts.md) | `.github/prompts/*.prompt.md` | Reusable task templates invoked as slash commands |
| [**Skills**](docs/primitive-4-skills.md) | `.github/skills/*/SKILL.md` | Procedural knowledge Copilot can discover and apply |
| [**Custom Agents**](docs/primitive-5-custom-agents.md) | `.github/agents/*.md` | Specialized AI personas with defined behaviors |
| [**MCP (Model Context Protocol)**](docs/primitive-6-mcp.md) | `.vscode/mcp.json` | Connections to external tools, APIs, and data sources |
| [**Hooks (Preview)**](docs/primitive-7-hooks.md) | `.github/hooks/*.json` | Runtime enforcement and audit logging for agent sessions |
| [**Memory (Preview)**](docs/primitive-8-memory.md) | GitHub cloud (repository-scoped) | Learned codebase knowledge that persists across sessions |
| [**Agentic Workflows (Preview)**](docs/primitive-9-agentic-workflows.md) | `.github/workflows/*.md` | Continuous AI via coding agents in GitHub Actions |
| [**Copilot SDK (Preview)**](docs/primitive-10-copilot-sdk.md) | External dependency (npm, pip, etc.) | Embed the Copilot agent runtime in your own tools and applications |

Understanding when and how to use each primitive is the core of this guide.

**Not sure which primitive to use?** Jump to the [Quick Decision Guide](docs/part-3-reference.md#quick-decision-guide).

---

## Guide Structure

### [Part I: Foundations](docs/part-1-foundations.md)

Start here. Why customization matters, how the primitives layer together, strategies for iteration, and approaches for measuring success.

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
- [Primitive 9: Agentic Workflows](docs/primitive-9-agentic-workflows.md) — Continuous AI via coding agents in GitHub Actions
- [Primitive 10: Copilot SDK](docs/primitive-10-copilot-sdk.md) — Embed the agent runtime in your own tools

### [Part III: Reference](docs/part-3-reference.md)

Quick reference tables, starter templates, and configuration reference for all ten primitives.

---

## Getting Started

New to Copilot customization? Start with [Part I: Foundations](docs/part-1-foundations.md), then work through the primitives in order — each builds on the previous.

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
- [Copilot Memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory) — Automatic repository-level learning that complements explicit customization
- [GitHub Agentic Workflows](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/) — Continuous AI via coding agents in GitHub Actions
- [VS Code 1.116 Release Notes](https://code.visualstudio.com/updates/v1_116) — Latest VS Code release with Copilot built-in
- [VS Code Source Code](https://github.com/microsoft/vscode) — The authoritative reference when documentation is unclear
- [Copilot Spaces](https://docs.github.com/en/copilot/how-tos/provide-context/use-copilot-spaces) — Organize relevant context into Spaces that ground Copilot's responses for specific tasks
- [product-brain](https://github.com/digitarald/product-brain) — A product management approach to workspace instructions
