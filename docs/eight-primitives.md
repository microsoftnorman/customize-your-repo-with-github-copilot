# The Eight Primitives

[← Back to Guide](../README.md) | [← Primitives in Action](primitives-in-action.md) | [Next: Always-on Instructions →](primitive-1-always-on-instructions.md)

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

The important question is not "which file type do we have not used yet?" It is "which control point in the system is actually missing?"

For the quick chooser table, use [Operational Reference](part-3-reference.md#which-primitive-should-you-use). This chapter stays focused on what each primitive is and how the set fits together.

## Authoring Rule of Thumb

Best practice is to use GitHub Copilot itself as the authoring harness for the instruction file, prompt, skill, custom agent, MCP configuration, or hook definition you are creating, then review and refine what it produced. Prompt first, inspect the draft, evaluate it against the real workflow, and then hand-edit where needed.

Direct manual authoring is still valid. It is just not the best default when the goal is to shape agent behavior with the same system that will later consume those customizations.

Once the customization is correct, commit the repository files so other surfaces can consume them. The repository layout is the durable asset. The editor-specific creation UX is only the entry point.

## Composition Matters More Than Enumeration

Most good setups use two to four primitives together. Very few real workflows are solved by only one.

That is the right mental model to keep while reading the next chapters. The goal is not to memorize eight isolated file formats. The goal is to understand which control point the workflow is missing.

## How Primitives Layer Together

```
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

Each layer adds specificity. The foundation (always-on instructions) applies everywhere; other primitives activate based on context.

**When primitives conflict:** More specific primitives take precedence. File-based instructions override always-on instructions for matching files. Agent-scoped instructions override global instructions while that agent is active. This mirrors CSS specificity: the most targeted rule applies.

## Where Primitives Overlap

Several primitives look similar at first glance. These are the most common disambiguation questions:

| Confusion | The Difference | Rule of Thumb |
|-----------|---------------|---------------|
| **Always-on instructions vs. Custom agents** | Instructions are global rules for every interaction. Agents are specialized personas with their own tools, model, and behavior. | Put universal rules in instructions. Put role-specific behavior in agents. |
| **Prompts vs. Skills** | Both appear as `/` commands. Prompts are user-triggered, fire-and-forget. Skills can also activate automatically based on context. | Use prompts for simple single-purpose commands. Use skills when the knowledge should also activate without the user asking, or needs to travel across surfaces. |
| **Agents vs. Prompts** | An agent is a persistent persona that changes the entire conversation. A prompt is a single task template. | If the user switches into a "mode" (reviewer, architect), that is an agent. If the user runs a repeatable task (scaffold, generate tests), that is a prompt or skill. |
| **Instructions vs. Memory** | Instructions are explicit rules. Memory is implicit knowledge the system learns. | Write instructions for decisions already made. Let Memory learn patterns that are hard to articulate. |
| **Hooks vs. Instructions** | Instructions *ask* the model to avoid something. Hooks *enforce* it. | Use instructions for guidance. Use hooks when compliance is mandatory. Use both together for defense in depth. |
| **File-based instructions vs. Skills** | File-based instructions activate by file pattern. Skills activate by intent. | Use file-based instructions for "rules when editing these files." Use skills for "how to do this task." |

The overlap is intentional. The cost of putting something in the "wrong" primitive is low. The cost of not encoding it anywhere is high.

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
