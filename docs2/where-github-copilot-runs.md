# Where GitHub Copilot Runs

[← Back to Guide](README.md) | [← GitHub Copilot Code Review](code-review.md)

*Updated: April 22, 2026.*

---

## What This Page Covers

This page explains where the same primitive layer is supported well, where authoring differs, and where portability has real limits.

For day-to-day parity checks, the official [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix) is the source of truth across IDEs.

That distinction matters because the whole guide is built on one argument:

**the repository knowledge is portable, but the surfaces are not identical.**

## The Core Distinction

Primitives are repository-level knowledge and control.

Surfaces are the places where GitHub Copilot consumes that knowledge.

The cross-runtime chapters in this guide are special cases of those surfaces where the same loop runs with different constraints and affordances.

This distinction prevents two common mistakes:

- assuming every surface supports every primitive equally,
- or assuming a primitive is editor-specific just because it was authored in one place.

## Why Surface Choice Still Matters

If the primitive layer is portable, why care about surfaces at all?

Because surfaces change:

- authoring UX,
- tool availability,
- support for specific primitives,
- approval and interaction model,
- and how visible the loop is to the user.

The repository may carry the same instructions, skills, and agents. The surface still determines how much of that system is actually usable.

## The Broad Surface Categories

| Category | What It Means |
|----------|----------------|
| **Rich local authoring surfaces** | Best place to create and iterate on customization files |
| **Portable execution surfaces** | Strong consumers of the primitive layer even if authoring is weaker |
| **Remote execution surfaces** | Run the same knowledge without a developer at the keyboard |
| **Embedded runtime surfaces** | Let the team host the loop in its own application or platform |

That is why this page should be read after the primitives and the other cross-runtime chapters. By this point, the reader no longer needs to ask what a primitive is. The question is where the same layer can be relied on.

## The Practical Surface Story

### VS Code

VS Code remains the richest authoring surface and the default reference environment for the guide.

It matters because it usually gets new customization features first and exposes the loop clearly through local sessions, planning, prompts, agents, hooks, MCP, and related tooling.

### GitHub Copilot CLI

The CLI matters because it makes the runtime unusually visible. The loop, approvals, tool use, and task decomposition are easier to see directly in terminal-first workflows than in many IDE experiences.

### Cloud Coding Agent

The Cloud Coding Agent matters because it proves that the same repository knowledge can run remotely and asynchronously. It also forces the reader to confront the difference between local collaboration and delegated work.

### Other IDE surfaces

Visual Studio, JetBrains, Eclipse, and Xcode matter because they test the portability claim against reality. The repository layout still helps them, but support depth, authoring affordances, and preview status vary.

That is why the guide treats VS Code as the reference authoring surface without pretending it is the only place that matters.

## How to Choose a Surface

Choose based on the workflow, not on ideology.

- Use **VS Code** when the team wants the broadest customization support and the best authoring experience.
- Use **GitHub Copilot CLI** when the team is terminal-first, remote-first, or wants the cleanest mental model for the loop.
- Use the **Cloud Coding Agent** when the task should become a pull request without a developer sitting in the flow.
- Use **Visual Studio**, **JetBrains**, **Eclipse**, or **Xcode** when the surrounding development environment is non-negotiable and the team needs to understand which parts of the primitive layer still translate well.
- Use the **Copilot SDK** when no existing surface is the right host at all.

## Surface Guides

The per-surface pages in this guide's `surfaces/` section carry the operational details this overview should not duplicate.

- [VS Code](surfaces/vscode.md)
- [GitHub Copilot CLI](surfaces/copilot-cli.md)
- [Cloud Coding Agent](surfaces/cloud-coding-agent.md)
- [Visual Studio](surfaces/visual-studio.md)
- [JetBrains IDEs](surfaces/jetbrains.md)
- [Eclipse](surfaces/eclipse.md)
- [Xcode](surfaces/xcode.md)

## The Most Important Takeaway

Surface differences are real, but they do not invalidate the main portability story.

The right way to think about it is:

- author once where support is strongest,
- commit the repository knowledge,
- and verify which consumers honor which parts of it.

That posture is more durable than trying to redesign the primitive layer around the weakest surface in the fleet.

## Where to Read Next

- Use the per-surface pages for operational detail.
- Revisit [Operational Reference](part-3-reference.md) when the question becomes support matrices, exact file locations, and lookup material instead of platform strategy.