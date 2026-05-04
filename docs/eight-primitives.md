# The Eight Primitives

[← Back to Guide](../ReadMe.md) | [← Primitives in Action](primitives-in-action.md) | [Next: Always-on Instructions →](primitive-1-always-on-instructions.md)

*Updated: May 4, 2026.*

---

## The Eight Primitives as Loop Controls

The eight primitives are easiest to understand as control points on the agent loop.

For the current product-level customization map, start with VS Code's [Customize AI in Visual Studio Code](https://code.visualstudio.com/docs/copilot/customization/overview) documentation. It is the closest official overview of how instructions, prompts, Skills, Custom Agents, MCP, hooks, and plugins fit together in one authoring surface.

They do not all solve the same problem.

- Some shape the loop's defaults.
- Some shape one task or one role.
- Some expand reach.
- Some enforce boundaries.
- Some accumulate learned knowledge.

That is why this chapter comes before the individual deep dives. The file-by-file chapters matter. But the bigger decision is where a rule belongs in the system.

**See it in action:** [Instructions vs Skills vs Hooks & More Explained By Copilot Itself | Ep 7 of 8](https://www.youtube.com/watch?v=oyMMotLlcgQ&t=80s) — Reynald Adolphe demos using GitHub Copilot to compare customization primitives and build a reference chart for when to use each one.

## A Note on Pace

The current set of eight primitives came together in less than 14 months. Do not read that as a checklist. This product layer is modernizing fast, and most teams should not adopt every primitive just because it exists.

Many teams get real value from one or two primitives: Always-on Instructions plus a small set of File-based Instructions, or a Prompt plus a Skill for one repeated workflow. Add more only when real work exposes a missing control point.

Agent Plugins are the newest sign of that pace. They are not a ninth primitive. They are a preview distribution layer that can bundle slash commands, Skills, Custom Agents, Hooks, and MCP servers behind a `plugin.json` manifest so teams can install a coherent package instead of copying each artifact by hand. Treat them as packaging and supply-chain architecture, not as a new kind of instruction. See the official [Agent Plugins documentation](https://code.visualstudio.com/docs/copilot/customization/agent-plugins) before adopting the preview format.

## The Primitive Set

| Primitive | Primary Job | Where It Enters the Loop | Best Used For |
|-----------|-------------|--------------------------|---------------|
| [Always-on Instructions](primitive-1-always-on-instructions.md) | Base defaults | Context assembly | Team-wide conventions and stack choices |
| [File-based Instructions](primitive-2-file-based-instructions.md) | Scoped defaults | Context assembly for matching files | Path-specific rules |
| [Prompts](primitive-3-prompts.md) | Explicit task framing | Task shaping | User-invoked templates |
| [Skills](primitive-4-skills.md) | Reusable procedure | Task shaping and decision support | Repeatable workflows that should be discoverable |
| [Custom Agents](primitive-5-custom-agents.md) | Persistent role and posture | Task shaping across a conversation | Reviewer, architect, deployer, mentor modes |
| [MCP](primitive-6-mcp.md) | External reach | Action selection and tool execution | APIs, databases, issue trackers, internal systems |
| [Hooks](primitive-7-hooks.md) | Enforcement and audit | Lifecycle boundaries around execution | Deny, inspect, log, or constrain risky actions |
| [Memory](primitive-8-memory.md) | Learned repo knowledge | Context assembly and reasoning | Patterns that are hard to author but easy to observe |

## Choosing the Right Primitive

The important question is not "which file type do we have not used yet?" It is "which control point in the system is actually missing?"

For the quick chooser table, use [Operational Reference](part-3-reference.md#which-primitive-should-you-use). This chapter stays focused on what each primitive is and how the set fits together.

## Authoring Rule of Thumb

Apply [Colby's rule](when-to-customize.md#when-models-outgrow-the-rules) here. Some authoring habits around these primitives come from the GPT-3.5 Turbo era, when models needed more scaffolding before they could produce useful work. That old scaffolding is not the right default in April 2026. Agents running on frontier models like Claude Opus 4.7 and GPT-5.5 are good enough to draft useful customizations from a clear goal, a little repository context, and one real workflow.

Start small and react to friction. Do not spend days pre-authoring a perfect instruction system before the team gets value. Use GitHub Copilot, notice where it guesses wrong, and add the smallest rule, prompt, skill, agent, MCP configuration, or hook that fixes that failure. Less is usually better until real work proves otherwise.

The bigger shift is learning how to communicate with the agent. Say what outcome you want, which constraints matter, what evidence it should inspect, and what a good result looks like. Then let GitHub Copilot draft the instruction file, prompt, skill, custom agent, MCP configuration, or hook definition. Review the draft, test it against the real workflow, and hand-edit only where the behavior proves the wording is wrong or incomplete.

Direct manual authoring is still valid. It is just not the best default when the goal is to shape agent behavior with the same system that will later consume those customizations.

Once the customization is correct, commit the repository files so other surfaces can consume them. The repository layout is the durable asset. The editor-specific creation UX is only the entry point.

## Composition Matters More Than Enumeration

Most good setups use two to four primitives together. Very few real workflows are solved by only one.

That is the right mental model to keep while reading the next chapters. The goal is not to memorize eight isolated file formats. The goal is to understand which control point the workflow is missing.

## How Primitives Layer Together

```text
User's Message
     ↓
+-----------------------------------------+
|     Custom Agent (if activated)         |  ← Modifies entire session
+-----------------------------------------|
|    Prompt Template (if invoked)         |  ← Single task
+-----------------------------------------|
|   Skills (loaded by description match)  |  ← On-demand knowledge
+-----------------------------------------|
|  File-Based Instructions (if matched)   |  ← Context for this file
+-----------------------------------------|
|       Always-On Instructions            |  ← Foundation layer
+-----------------------------------------|
|    MCP Tools (available throughout)     |  ← External capabilities
+-----------------------------------------+
     ↓
Response
     ↓
+-----------------------------------------+
|    Hooks                                |  ← Runtime enforcement
|    PreToolUse / PostToolUse / etc.      |  ← Audit, deny, log
+-----------------------------------------+
```

Each layer adds specificity in practice, but the runtime does not promise a simple CSS-style cascade across every surface. File-based instructions add path-specific guidance when matching files are in play. Custom Agents add role-specific guidance when selected or invoked. Tool and prompt settings can also narrow what the agent can do for a turn. When two rules conflict, do not depend on hidden precedence. Rewrite the rules so the intended behavior is explicit, test the target surface, and keep mandatory policy in the narrowest instruction file or enforcement mechanism that actually owns it.

## Where Primitives Overlap

Several primitives look similar at first glance. These are the most common disambiguation questions:

| Confusion | The Difference | Rule of Thumb |
|-----------|---------------|---------------|
| **Always-on instructions vs. Custom agents** | Instructions are global rules for every interaction. Agents are specialized personas with their own tools, model, and behavior. | Put universal rules in instructions. Put role-specific behavior in agents. |
| **Prompts vs. Skills** | Both appear as `/` commands. Prompts are user-triggered, fire-and-forget. Skills can also activate automatically based on context. | Use prompts for simple single-purpose commands. Use skills when the knowledge should also activate without the user asking, or needs to travel across surfaces. |
| **Agents vs. Prompts** | An agent is a persistent persona that changes the entire conversation. A prompt is a single task template. | If the user switches into a "mode" (reviewer, architect), that is an agent. If the user runs a repeatable task (scaffold, generate tests), that is a prompt or skill. |
| **Instructions vs. Memory** | Instructions are defined, reviewed, source-controlled rules. Memory is inferred, validated, temporary repository knowledge. | Put rules that should steer or override behavior in instructions. Let Memory learn patterns that are useful context but not policy. |
| **Hooks vs. Instructions** | Instructions *ask* the model to avoid something. Hooks *enforce* it. | Use instructions for guidance. Use hooks when compliance is mandatory. Use both together for defense in depth. |
| **File-based instructions vs. Skills** | File-based instructions activate by file pattern. Skills activate by intent. | Use file-based instructions for "rules when editing these files." Use skills for "how to do this task." |

The overlap is conceptual, not operational. Instructions and Memory can both carry repository context, but they do not have the same authority. In supported agent surfaces, GitHub Copilot can call or surface Memory as a runtime capability. That does not make it a user-authored instruction file, a repository-configured MCP server or tool, or a slash command the user normally invokes manually. If a rule should steer behavior, override a default, or apply from the first interaction, make it an instruction. Memory can reinforce observed patterns, but it is inferred, citation-validated, and temporary.

## Where to Read Next

Start with the primitive that fixes the broadest problem first:

1. [Always-on Instructions](primitive-1-always-on-instructions.md)
2. [File-based Instructions](primitive-2-file-based-instructions.md)
3. [Prompts](primitive-3-prompts.md)
4. [Skills](primitive-4-skills.md)
5. [Custom Agents](primitive-5-custom-agents.md)
6. [MCP](primitive-6-mcp.md)
7. [Hooks](primitive-7-hooks.md)
8. [Memory](primitive-8-memory.md)

If the question is already operational rather than conceptual, jump to [Operational Reference](part-3-reference.md).
