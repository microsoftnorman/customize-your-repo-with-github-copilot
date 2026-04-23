# The Eight Primitives

[← Back to Guide](README.md) | [← Primitives in Action](primitives-in-action.md) | [Next: Measuring Success →](measuring-success.md)

*Updated: April 22, 2026.*

---

## The Eight Primitives as Loop Controls

The eight primitives are easiest to understand as control points on the agent loop.

They do not all solve the same problem.

- Some shape the loop's defaults.
- Some shape one task or one role.
- Some expand reach.
- Some enforce boundaries.
- Some accumulate learned knowledge.

That is why this chapter comes before the individual deep dives. The file-by-file chapters matter. But the bigger decision is where a rule belongs in the system.

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

Use these distinctions first.

| If the problem is... | Start here |
|----------------------|------------|
| GitHub Copilot keeps using the wrong defaults everywhere | [Always-on Instructions](primitive-1-always-on-instructions.md) |
| The rule is only true for one part of the repo | [File-based Instructions](primitive-2-file-based-instructions.md) |
| The team wants a slash-command style task template | [Prompts](primitive-3-prompts.md) |
| The team wants reusable procedure, not just a template | [Skills](primitive-4-skills.md) |
| The user needs GitHub Copilot to act in a distinct role for a whole session | [Custom Agents](primitive-5-custom-agents.md) |
| The task depends on tools or data outside the workspace | [MCP](primitive-6-mcp.md) |
| The rule must be enforced even if the model chooses badly | [Hooks](primitive-7-hooks.md) |
| The repository keeps teaching the same patterns by repetition | [Memory](primitive-8-memory.md) |

## The Most Common Confusions

| Confusion | Better Question |
|-----------|-----------------|
| Prompts vs. Skills | Is this just a template, or should the procedure be discoverable on its own? |
| Skills vs. Agents | Does the team need a reusable procedure, a durable role, or both? |
| Instructions vs. Hooks | Is the model being guided, or is execution being constrained? |
| Instructions vs. Memory | Is the rule already known and explicit, or should the system learn it through use? |
| Agents vs. MCP | Does the problem need a different posture, a new tool connection, or both? |

## Authoring Rule of Thumb

Create primitives through the best available authoring surface, then commit the files to the repository so other surfaces can consume them. The repository layout is the durable asset. The editor-specific creation UX is just the entry point.

## Composition Matters More Than Enumeration

Most good setups use two to four primitives together. Very few real workflows are solved by only one.

That is the right mental model to keep while reading the next chapters. The goal is not to memorize eight isolated file formats. The goal is to understand which control point the workflow is missing.

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
