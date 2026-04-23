# VS Code

[← Where GitHub Copilot Runs](../where-github-copilot-runs.md) | [Next: GitHub Copilot CLI →](copilot-cli.md)

*Updated: April 22, 2026.*

---

## What This Surface Is

VS Code is the reference authoring surface for this guide.

The canonical starting points are VS Code's [Customize AI in Visual Studio Code](https://code.visualstudio.com/docs/copilot/customization/overview) page and the broader [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview) documentation hub.

That is not because every team should switch to it. It is because VS Code exposes the broadest visible implementation of the customization model: instructions, prompts, skills, custom agents, MCP, hooks, and the surrounding UX for creating and debugging them.

If a team wants to understand what the full primitive layer looks like when it is most mature, VS Code is the clearest place to study it.

## Why It Matters

This guide keeps making one claim: repository knowledge is portable.

VS Code matters because it is where that knowledge is easiest to author, inspect, and refine.

As of April 2026, GitHub Copilot is built into VS Code. More importantly for this guide, VS Code is the surface where the loop is most visible:

- the chat and agent experience are first-class,
- the customization files are easy to create and inspect,
- MCP is well integrated,
- and the surrounding controls for approvals, hooks, and tool use are the least ambiguous.

## Why This Guide Uses VS Code as the Reference Environment

This guide is about shaping GitHub Copilot behavior at the repository level.

VS Code is the best reference environment for that work because it exposes almost every moving part directly. A reader can see the repository instructions, the active skills, the available agents, the MCP configuration, and the runtime decisions in one place.

That makes it the best place to author the files even when the team later consumes them somewhere else.

## What Portability Looks Like from VS Code

The VS Code story is simple:

- author the repository-level files here,
- commit them,
- then let other surfaces consume as much of that layer as they support.

That is a stronger workflow than trying to author the system around the weakest surface in the stack.

## What VS Code Has That Not Every Other Surface Has

VS Code is usually ahead in three ways:

- support breadth for the full primitive set,
- authoring UX for discovering and managing those primitives,
- and debugging visibility when the agent loop behaves unexpectedly.

That does not make other surfaces second-class. It means VS Code is the least lossy place to create the source of truth.

## When a Team Should Prefer VS Code

VS Code is the right default when the team wants:

- the richest customization support,
- the shortest path from idea to working repository rules,
- the clearest view into agent behavior,
- or the smallest gap between what is documented and what is available.

That recommendation is about capability, not ideology.

## The Main Caveat

The risk of using VS Code as the reference surface is overgeneralization.

A feature that works beautifully in VS Code may be missing, preview-only, or differently authored in another surface. That is why the rest of this section exists. The repository layer is portable, but the UX and support depth are not identical.

## The Short Version

If the team needs one place to design the repository's GitHub Copilot operating model, choose VS Code.

If the team later executes that model elsewhere, treat VS Code as the authoring control plane rather than as the only valid runtime.

## Where to Read Next

- Read [GitHub Copilot CLI](copilot-cli.md) next for the terminal-first version of the same loop.
- Revisit [Where GitHub Copilot Runs](../where-github-copilot-runs.md) if you want the surface map before going deeper.
