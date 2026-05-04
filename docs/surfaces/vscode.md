# VS Code

[← Where GitHub Copilot Runs](../where-github-copilot-runs.md) | [Next: GitHub Copilot CLI →](copilot-cli.md)

*Updated: May 4, 2026.*

---

## What This Surface Is

VS Code is the reference authoring surface for this guide.

The canonical starting points are VS Code's [Customize AI in Visual Studio Code](https://code.visualstudio.com/docs/copilot/customization/overview) page and the broader [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview) documentation hub.

That is not because every team should switch to it. It is because VS Code exposes the broadest visible implementation of the customization model: instructions, prompts, skills, custom agents, MCP, hooks, and the surrounding UX for creating and debugging them.

If a team wants to understand what the full primitive layer looks like when it is most mature, VS Code is the clearest place to study it.

**See it in action:** [The Agent Customizations UI Nobody Knows About | Ep 1 of 8](https://www.youtube.com/watch?v=AZzCk-WGks4&t=136s) — Reynald Adolphe demos the VS Code Chat Customizations UI for managing agents, skills, instructions, prompt files, and hooks.

**See it in action:** [Mastering AI with VS Code's New Agent Customizations](https://www.youtube.com/watch?v=os2eqa69gko&t=83s) — James Montemagno tours the unified Chat Customizations panel for agents, skills, instructions, prompts, hooks, MCP, and plugins.

## Why It Matters

This guide keeps making one claim: repository knowledge is portable.

VS Code matters because it is where that knowledge is easiest to author, inspect, and refine.

As of April 2026, GitHub Copilot is built into VS Code. More importantly for this guide, VS Code is the surface where the loop is most visible:

- the chat and agent experience are first-class,
- the customization files are easy to create and inspect,
- MCP is well integrated,
- and the surrounding controls for approvals, hooks, and tool use are the least ambiguous.

The current VS Code docs also expose a Chat Customizations editor in preview. It is the clearest single UI for browsing instructions, prompts, skills, custom agents, MCP, and hooks without hunting through the file tree or settings one feature at a time.

VS Code 1.118 adds one more authoring and distribution layer: Agent Plugins in preview. Plugins can bundle slash commands, Skills, Custom Agents, Hooks, and MCP servers behind a `plugin.json` manifest, then install from marketplaces, source repositories, or local plugin locations. Use `chat.plugins.enabled` to enable the feature, `chat.plugins.marketplaces` to add marketplaces, and `chat.pluginLocations` for local plugin directories. Workspace recommendations can point teams to approved plugins through `.claude/settings.json` or `.github/copilot/settings.json`.

For operational safety, pair those authoring features with VS Code's [Security](https://code.visualstudio.com/docs/copilot/security) guidance on workspace trust, tool approvals, MCP trust, sandboxing, and hooks.

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

It also has the clearest model-selection story. The customization overview now explicitly calls out choosing different models for different tasks and bringing an API key for access to additional models. That matters because model selection is part of customization, not a separate concern outside the operating model.

GPT-5.5 is generally available in GitHub Copilot as of April 24, 2026 for Pro+, Business, and Enterprise users, including in VS Code. Business and Enterprise administrators must enable the GPT-5.5 policy in Copilot settings before users can select it, and rollout is gradual.

The May 1 model retirement notice matters for shared customizations: GPT-5.2 and GPT-5.2-Codex retire on June 1, 2026, except GPT-5.2-Codex in GitHub Copilot Code Review. Prefer GPT-5.5 and GPT-5.3-Codex in new shared agents or prompt files.

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

## Recent VS Code 1.118 Changes

For customization teams, the April 29, 2026 VS Code 1.118 release matters in several places:

| Area | Change |
|------|--------|
| Agent Plugins | Preview support for installable bundles with `plugin.json`, marketplaces, local plugin locations, and workspace recommendations |
| Skills | Experimental `context: fork` runs a Skill in a dedicated subagent context when `github.copilot.chat.skillTool.enabled` is enabled |
| MCP | Workspace `.mcp.json` support and deduplication by server name; manage installed servers with `@mcp @installed` or Chat customizations |
| GitHub Copilot CLI sessions | Experimental remote control with `github.copilot.chat.cli.remote.enabled` and `/remote on`; session titles now sync across chat surfaces and `copilot --resume` |
| Search context | Semantic indexing now works for non-GitHub repositories, and the `githubTextSearch` tool adds exact grep-style search across GitHub repos or orgs |
| Evaluation | Chat Customizations Evaluations extension (`ms-vscode.vscode-chat-customizations-evaluations`) analyzes prompt files, custom agents, instructions, and Skills |
| Git commits | `git.addAICoAuthor` now defaults to adding GitHub Copilot as a co-author when it makes changes |
| Deprecation | Edit Mode remains deprecated and is scheduled for removal in VS Code 1.125 |

These are high-drift features. Keep preview features out of org-wide baselines until the target VS Code version, settings policy, and fallback behavior are tested.

## The Short Version

If the team needs one place to design the repository's GitHub Copilot operating model, choose VS Code.

If the team later executes that model elsewhere, treat VS Code as the authoring control plane rather than as the only valid runtime.

## Where to Read Next

- Read [GitHub Copilot CLI](copilot-cli.md) next for the terminal-first version of the same loop.
- Revisit [Where GitHub Copilot Runs](../where-github-copilot-runs.md) if you want the surface map before going deeper.
