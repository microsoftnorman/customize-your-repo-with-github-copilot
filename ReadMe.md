# The Definitive Guide to Customizing GitHub Copilot

*Updated: April 22, 2026. This is a reference guide. File paths, configuration details, and feature availability may drift as GitHub Copilot evolves, but the underlying runtime model and customization theory remain the same. Always verify current product specifics against the [official documentation](https://code.visualstudio.com/docs/copilot).*

---

GitHub Copilot is easiest to understand as a system, not a menu of isolated features. This guide explains that system clearly: what the agent loop is, where customization enters it, how the eight primitives work together, and why the same repository knowledge can travel across the editor, the terminal, pull request review, GitHub Actions, and custom applications.

Examples in this version of the guide use VS Code as the primary surface because it exposes the clearest view of GitHub Copilot's runtime and customization model. Other work surfaces operate in the same basic way: context is assembled, the task is shaped, tools and permissions govern action, and the loop continues until the task stops. Surface-specific differences still matter, but the theory carries across them.

It starts with the runtime, then moves into the control points that change behavior, and ends with the operational reference material teams need to roll out safely.

## Guide Map

- [Foundations](docs/foundations.md)
- [Why Customization Matters](docs/why-customization-matters.md)
- [The Agent Loop](docs/agent-loop.md)
- [Primitives in Action](docs/primitives-in-action.md)
- [The Eight Primitives](docs/eight-primitives.md)
  - [Primitive 1: Always-on Instructions](docs/primitive-1-always-on-instructions.md)
  - [Primitive 2: File-based Instructions](docs/primitive-2-file-based-instructions.md)
  - [Primitive 3: Prompts](docs/primitive-3-prompts.md)
  - [Primitive 4: Skills](docs/primitive-4-skills.md)
  - [Primitive 5: Custom Agents](docs/primitive-5-custom-agents.md)
  - [Primitive 6: MCP](docs/primitive-6-mcp.md)
  - [Primitive 7: Hooks](docs/primitive-7-hooks.md)
  - [Primitive 8: Memory](docs/primitive-8-memory.md)
- [Measuring Success](docs/measuring-success.md)
- [Executive Maturity Model](docs/executive-maturity-model.md)
- [Operational Reference](docs/part-3-reference.md)
- [Agentic Workflows](docs/agentic-workflows.md)
- [GitHub Copilot SDK](docs/copilot-sdk.md)
- [GitHub Copilot Code Review](docs/code-review.md)
- [Where GitHub Copilot Runs](docs/where-github-copilot-runs.md)
- [Tool Calling in Depth](docs/tool-calling-in-depth.md)
- [Debugging the Agent Loop](docs/debugging-the-agent-loop.md)
- [Appendix: Diagnosing Loop Failures](docs/appendix-diagnosing-loop-failures.md)

## How This Guide Is Organized

The guide is organized around the agent loop, not around a pile of disconnected configuration files. The eight primitives are introduced as control points on that loop, so readers can see how each one changes behavior in context instead of memorizing formats in isolation.

Composition patterns appear early, before the file-by-file deep dives, because the real value comes from how these pieces work together. Videos, transcripts, and podcast episodes are used as evidence and demos, not as decorative extras. Cross-runtime chapters such as GitHub Copilot code review, Agentic Workflows, the GitHub Copilot SDK, and the surface guides are included to show that the same primitive layer keeps showing up in different places.
