# Foundations

[← Back to Guide](../README.md) | [Next: Why Customization Matters →](why-customization-matters.md)

*Updated: April 22, 2026.*

---

## What GitHub Copilot Is

GitHub Copilot is not one feature in one editor. It is a platform for agentic software development that runs across multiple surfaces: the IDE surface, the terminal surface, GitHub surfaces such as GitHub.com and GitHub Actions, and custom applications. The same core runtime can answer a question, plan a multi-step task, run tools, delegate work, review a pull request, or operate inside another surface entirely. For the broader surface map in this guide, see [Where GitHub Copilot Runs](where-github-copilot-runs.md).

That is also why GitHub Copilot should not be framed as editor-only coding assistance. [GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) brings the same agentic runtime into the terminal, and the [GitHub Copilot SDK](https://github.com/github/copilot-sdk) lets teams embed that runtime in their own apps and services. In practice, that means the system can support broader model-driven workflows such as automation, operational tasks, research, and other agentic interactions that are not limited to writing code in an IDE.

That broader view matters because customization only makes sense at the platform level. A repository is not teaching one chat panel how to behave. It is teaching GitHub Copilot how to work inside a specific engineering system. The current official entry point for that layer is [Customize AI in Visual Studio Code](https://code.visualstudio.com/docs/copilot/customization/overview).

## What This Guide Teaches

This guide is about the layer between a frontier model and a real codebase. Out of the box, GitHub Copilot already knows language syntax, common frameworks, and public patterns. It does not know the architectural choices, anti-patterns, review culture, or operational constraints that make one repository different from another.

The purpose of customization is to encode those differences explicitly.

This guide teaches that in four moves:

1. Explain the platform and the problem.
2. Explain the agent loop that turns a prompt into work.
3. Explain the eight primitives as levers on that loop.
4. Explain how the same knowledge travels across surfaces.

## Key Terms

| Term | Meaning |
|------|---------|
| **Agentic** | GitHub Copilot plans steps, calls tools, checks results, and iterates instead of replying once and stopping. |
| **Primitive** | A repository-level customization mechanism such as Always-on Instructions, Prompts, Skills, Custom Agents, MCP, Hooks, or Memory. |
| **Agent loop** | The repeated cycle of context assembly, decision-making, tool use, result ingestion, and stopping conditions. |
| **Surface** | The environment where GitHub Copilot runs: VS Code, GitHub Copilot CLI, the Cloud Coding Agent, GitHub.com, or a custom app. |
| **Execution environment** | A runtime that consumes the same primitive layer in a different place, such as code review, Agentic Workflows, or the Copilot SDK. |

## Where GitHub Copilot Runs

The same repository can be read by multiple surfaces. That is why the customization files live in conventional places such as `.github/` and `.vscode/` instead of inside one editor's private state.

For day-to-day parity checks across IDEs and GitHub surfaces, use the live [GitHub Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix).

| Surface | Why It Matters |
|---------|----------------|
| **VS Code** | Richest customization support and the fastest feature cadence. |
| **GitHub Copilot CLI** | Shows the agent model most clearly because the loop, tools, and approvals are visible at the terminal. |
| **Cloud Coding Agent** | Demonstrates what happens when the same knowledge runs remotely and asynchronously. |
| **GitHub.com** | Important for code review, repository policy, and workflow-triggered automation. |
| **Other IDEs** | Useful reminder that the primitive layer is portable even when the authoring UX differs. |

**See it in action:** [Agent sessions and where agents run](https://www.youtube.com/watch?v=0CsKOO7d35I&t=129s) — Gwyneth Peña-Siguenza demos switching an agent session between local execution, GitHub Copilot CLI, and the GitHub platform.

## Core Capabilities

GitHub Copilot assists developers across six interaction patterns:

| Pattern | What It Does | Where It Runs |
|---------|-------------|---------------|
| **Code completion** | Predicts the next lines as you type | IDEs (VS Code, JetBrains, Eclipse, Visual Studio, Xcode) |
| **Chat** | Conversational interface for questions, code generation, and explanations | IDEs, GitHub.com |
| **Agentic coding** | Plans multi-step tasks, calls tools, edits files, runs commands, and iterates | VS Code, Copilot CLI, Cloud Coding Agent |
| **Code review** | Automated first-pass review of pull requests | GitHub.com, GitHub Mobile, GitHub CLI, VS Code, Visual Studio, JetBrains, Xcode |
| **Agentic Workflows** | Coding agents inside GitHub Actions on schedules, events, or on demand | GitHub Actions (technical preview) |
| **Custom integration** | Embed the agent runtime in custom tools via the [Copilot SDK](copilot-sdk.md) | Your applications |

**Agentic coding** is where customization has the most impact. The quality of instructions, skills, and guardrails in the repository directly determines the quality of the output.

**Important:** The customization primitives in this guide affect **Copilot Chat and agent interactions only**. Inline suggestions (ghost text/autocomplete) operate on a separate pipeline. For convention-aware code generation, use Chat-based interactions.

## Models Matter, but They Are Not the Whole Story

Model quality still changes the ceiling. Better reasoning models handle ambiguity, larger refactors, and more nuanced review. Faster models are useful for narrow loops and lightweight tasks. But model selection does not replace repository customization.

A strong model with no repository context still defaults to public-code patterns. A repository with clear instructions, procedural knowledge, and guardrails makes every supported model more useful. The implementation layer for those controls is covered next in [Why Customization Matters](why-customization-matters.md) and later in [The Eight Primitives](eight-primitives.md).

The practical rule is simple: choose the best model the task justifies, then teach that model how your repository works.

## The Three Inputs to Copilot Quality

| Input | What It Changes | Who Controls It |
|-------|-----------------|-----------------|
| **Model selection** | Reasoning depth, style, latency, and bias | The user, the team, or enterprise policy |
| **Codebase quality** | How easy it is to infer architecture and intent | The repository maintainers |
| **Repository customization** | What GitHub Copilot is explicitly told, allowed, and connected to | The repository maintainers |

This guide is mostly about the third input, but the other two never disappear. A messy repository cannot be rescued by instructions alone. A weak model cannot be turned into a frontier one by adding more YAML.

## Plans

| Plan | Who It's For |
|------|-------------|
| **Copilot Free** | Individual developers; limited access to core features |
| **Copilot Pro / Pro+** | Individual developers; full access including agent mode, memory, and premium models |
| **Copilot Business** | Teams. Centralized management, policy controls, and org-wide customization |
| **Copilot Enterprise** | Large organizations. Enterprise governance, SSO, audit logging, data residency, and FedRAMP High authorization |

The core customization files (instructions, file-based instructions, prompts, skills, custom agents, and MCP) work on all plans, including Free. Features with additional requirements:

| Feature | Availability |
|---------|--------------|
| **Hooks** | Pro, Pro+, Business, Enterprise |
| **Memory** | Pro, Pro+ (on by default), Business, Enterprise (admin enables) |
| **Cloud Coding Agent** | Pro/Pro+ (public repos only), Business, Enterprise |
| **Agentic Workflows** | Technical preview; Business, Enterprise |

For the complete availability matrix, see the [Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix).

## Enterprise Policy Hierarchy

Copilot configuration operates within a hierarchy: **enterprise → organization → repository**. Each level constrains the levels below:

- **Enterprise policies** restrict which models are available, whether Memory is enabled, and which features are accessible across all organizations.
- **Organization settings** enforce or restrict specific primitives and control which MCP servers team members can use.
- **Repository-level customization** operates within the boundaries set above.

A repository cannot override an enterprise policy. If the enterprise disables Memory, no repo in any organization under that enterprise can use it.

## Where to Read Next

- Read [Why Customization Matters](why-customization-matters.md) next for the human problem, the bespoke-code examples, and the argument for keeping the signal sharp.
- Read [The Agent Loop](agent-loop.md) after that for the runtime model behind every later chapter.
- Use [Where GitHub Copilot Runs](where-github-copilot-runs.md) when the question becomes surface differences rather than foundations.