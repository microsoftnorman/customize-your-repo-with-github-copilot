# The Definitive Guide to Customizing GitHub Copilot

*Updated: April 22, 2026. This is a reference guide. File paths, configuration details, and feature availability may drift as GitHub Copilot evolves, but the underlying runtime model and customization theory remain the same. Always verify current product specifics against the [official documentation](https://code.visualstudio.com/docs/copilot).*

---

GitHub Copilot is easiest to understand as a system, not a menu of isolated features. This guide explains that system clearly: what the agent loop is, where customization enters it, how the eight primitives work together, and why the same repository knowledge can travel across the editor, the terminal, pull request review, GitHub Actions, and custom applications.

Examples in this version of the guide use VS Code as the primary surface because it exposes the clearest view of GitHub Copilot's runtime and customization model. Other work surfaces operate in the same basic way: context is assembled, the task is shaped, tools and permissions govern action, and the loop continues until the task stops. Surface-specific differences still matter, but the theory carries across them.

It starts with the runtime, then moves into the control points that change behavior, and ends with the operational reference material teams need to roll out safely.

## Guide Map

- [Foundations](foundations.md)
- [Why Customization Matters](why-customization-matters.md)
- [The Agent Loop](agent-loop.md)
- [Primitives in Action](primitives-in-action.md)
- [The Eight Primitives](eight-primitives.md)
  - [Primitive 1: Always-on Instructions](primitive-1-always-on-instructions.md)
  - [Primitive 2: File-based Instructions](primitive-2-file-based-instructions.md)
  - [Primitive 3: Prompts](primitive-3-prompts.md)
  - [Primitive 4: Skills](primitive-4-skills.md)
  - [Primitive 5: Custom Agents](primitive-5-custom-agents.md)
  - [Primitive 6: MCP](primitive-6-mcp.md)
  - [Primitive 7: Hooks](primitive-7-hooks.md)
  - [Primitive 8: Memory](primitive-8-memory.md)
- [Measuring Success](measuring-success.md)
- [Executive Maturity Model](executive-maturity-model.md)
- [Operational Reference](part-3-reference.md)
- [Agentic Workflows](agentic-workflows.md)
- [GitHub Copilot SDK](copilot-sdk.md)
- [GitHub Copilot Code Review](code-review.md)
- [Where GitHub Copilot Runs](where-github-copilot-runs.md)
- [Tool Calling in Depth](tool-calling-in-depth.md)
- [Debugging the Agent Loop](debugging-the-agent-loop.md)
- [Appendix: Diagnosing Loop Failures](appendix-diagnosing-loop-failures.md)

## How This Guide Is Organized

- The agent loop is the organizing spine, not a side chapter.
- The primitives are taught as levers on the loop, not as eight disconnected file formats.
- Composition patterns appear early, before the file-by-file deep dives.
- Videos, transcripts, and podcast episodes are treated as proof points and demos, not decorative links.
- Cross-runtime chapters such as GitHub Copilot code review, Agentic Workflows, the GitHub Copilot SDK, and the surface guides are treated as places where the same primitive layer runs.
