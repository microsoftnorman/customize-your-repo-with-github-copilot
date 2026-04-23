# Primitive 8: Memory

[← Back to The Eight Primitives](eight-primitives.md) | [← Hooks](primitive-7-hooks.md) | [Next: Measuring Success →](measuring-success.md)

*Updated: April 22, 2026.*

---

## Where It Enters the Loop

Memory enters the loop during context assembly and reasoning, but unlike the other primitives, it is not authored in the repository as a file.

That is what makes it unusual.

Always-on Instructions, File-based Instructions, Prompts, Skills, Agents, MCP, and Hooks all represent knowledge or control the team defines explicitly. Memory represents repository knowledge GitHub Copilot learns over time from actual work.

## What This Primitive Is For

Use Memory to supplement explicit customization with patterns that are easier to observe than to document.

GitHub's canonical reference is [About agentic memory for GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/copilot-memory), which is also the place to check preview status and current rollout scope.

Examples include:

- naming patterns that recur across modules,
- cross-file relationships the team rarely writes down,
- architectural habits that are stable but tedious to explain explicitly,
- and conventions that repeatedly surface in code review or implementation work.

The question Memory answers is: "What has the system learned from how this repository actually behaves?"

## Why Memory Does Not Replace Explicit Customization

Memory is useful precisely because it is not the same thing as authored instructions.

It is weaker in one sense and stronger in another.

- Weaker because it is learned over time, expires, and depends on observed activity.
- Stronger because it can capture patterns no one would realistically maintain by hand.

That is why the right pairing is explicit plus learned, not one or the other.

Write down what must be true from day one. Let Memory reinforce the patterns that emerge from real repository work.

## What Makes Memory Different from the Other Seven

It has no repository file to create.

That changes how the primitive should be taught.

The story is no longer about file location and frontmatter. It is about lifecycle:

- how memories are created,
- where they are used,
- how they are validated,
- how they expire,
- and when humans should review or delete them.

That is why Memory belongs at the end of the primitive sequence. It makes the most sense once the reader already understands the authored layer it complements.

## The Relationship to Instructions

Always-on Instructions tell GitHub Copilot what the team already knows it wants.

Memory captures what GitHub Copilot keeps discovering through repeated work.

If the rule is explicit, important, and should apply immediately, write it down.

If the pattern is real but difficult to document exhaustively, let Memory help.

The strongest repositories use both.

## Surface Reality

The current guide positions Memory most clearly in places where repository knowledge needs to persist across work:

- Cloud Coding Agent sessions,
- code review,
- and CLI-based workflows.

That usage pattern matters because it reinforces one of the big themes of this guide: the primitive layer is portable, but not every part of it applies in every surface in the same way.

## What Good Memory Hygiene Looks Like

Good Memory hygiene means:

- using explicit customization for critical rules,
- periodically reviewing stored memories,
- deleting misleading or stale memories when needed,
- and understanding that expiration and validation are features, not bugs.

For the operational details on validation, retention, and manual cleanup, see [Managing and curating Copilot Memory](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/copilot-memory).

Memory is most useful when it follows the living code rather than becoming another undocumented system that accumulates stale assumptions.

## How It Composes with Other Primitives

| Primitive | Relationship |
|-----------|--------------|
| [Always-on Instructions](primitive-1-always-on-instructions.md) | Define the explicit rules Memory should reinforce, not replace |
| [File-based Instructions](primitive-2-file-based-instructions.md) | Capture scoped truths that should not wait to be learned |
| [Code Review](code-review.md) | Learned repository patterns can surface during review |
| [Cloud Coding Agent](surfaces/cloud-coding-agent.md) | Memory becomes especially valuable when work happens remotely over time |

## The Most Useful Mental Model

The shortest accurate explanation is this:

**Instructions are what the team tells GitHub Copilot. Memory is what GitHub Copilot learns from the team.**

That is the distinction to keep.

## How Memory Works

As GitHub Copilot works in a repository, it notices patterns worth remembering. Each memory is a tightly scoped fact: a naming convention, an architectural rule, a cross-file relationship.

### Lifecycle

```text
Copilot works in repo
     → Discovers useful fact
     → Stores memory with citations (references to specific code locations)
     → Next session: validates citations against current codebase
     → Valid → Memory applied
     → Invalid → Memory discarded
     → After 28 days → Memory auto-expires
```

### Key Properties

| Property | Detail |
|----------|--------|
| **Scope** | Repository-level: tied to a single repo, not a user or org |
| **Creation** | Automatic from normal operations, not manual input |
| **Validation** | Citation-based: checks referenced code locations before use |
| **Expiration** | 28 days; frequently-used memories get refreshed |
| **Permissions** | Only created from activity by users with write access |

## Where Memory Is Used

| Surface | How Memory Helps |
|---------|-----------------|
| **Cloud Coding Agent** | Applies learned conventions when implementing features and opening PRs |
| **Copilot code review** | Uses learned patterns to give more targeted review feedback |
| **GitHub Copilot CLI** | Brings repository awareness to terminal workflows |

Memory is shared across surfaces. If the coding agent discovers how the repo handles database connections, code review applies that knowledge when spotting inconsistencies.

Memory is not yet available in VS Code Chat, Completions, or Inline Chat.

## Availability by Plan

| Plan | Default State | Who Controls |
|------|--------------|--------------|
| **Copilot Pro / Pro+** | Enabled by default | Individual user |
| **Copilot Business** | **Disabled** by default | Organization owner |
| **Copilot Enterprise** | **Disabled** by default | Enterprise owner |

**Precedence:** If a user receives Copilot from multiple organizations, the most restrictive setting wins. Enterprise `Disabled everywhere` overrides any org-level choice.

## Viewing and Deleting Memories

Only repository owners can view and delete stored memories:

1. Repository → **Settings** → **Copilot** → **Memory**
2. Review the chronological list
3. Delete individual memories or select multiple

Manual deletion is only needed for incorrect or misleading memories. Auto-expiration handles the rest.

> 💬 **Try this prompt:**
> "Summarize the memories you currently have for this repository. Group them by topic and flag any that might be out of date."

## Memory vs. Explicit Customization

| | Explicit Customization | Copilot Memory |
|-|----------------------|----------------|
| **Source** | Written by developers | Automatically discovered |
| **When it helps** | From the first interaction | After enough activity |
| **Maintenance** | Manual | Automatic (expires stale, learns new) |
| **Reliability** | Deterministic | Probabilistic |
| **Best for** | Must-follow rules, security, architecture | Style nuances, cross-file relationships |

**Write instructions** when the rule must be followed from day one or getting it wrong has consequences.

**Let Memory handle it** when the pattern is hard to articulate but easy to observe, or the convention is stable in the existing code.

**Use both** when instructions set the rule ("use React Query, not Redux") and Memory learns the specific patterns ("in this repo, React Query hooks follow this naming convention and live in `src/hooks/queries/`").

## Best Practices

1. **Do not skip explicit customization because Memory exists.** A new repository has zero memories. Instructions work from the first interaction.
2. **Use instructions for guardrails, Memory for nuance.** Security requirements and tech stack choices belong in `copilot-instructions.md`. Let Memory learn the subtleties.
3. **Review stored memories periodically.** Delete memories that are misleading or based on patterns the team is moving away from.
4. **Consider the 28-day window.** For critical conventions, do not rely on Memory alone.

## Limitations

| Limitation | Detail |
|-----------|--------|
| Preview status | Behavior may change |
| Repository scope only | No user-level or org-level memory yet |
| 28-day expiration | Rarely-relevant facts may not persist |
| Limited surfaces | Not yet in VS Code Chat or IDE-specific chat |
| Write access required | Only created from activity by users with write permission |
| Owner-only review | Only repo owners can list or delete memories |
| No manual creation | Cannot manually add memories; use instructions for injected knowledge |

## Where to Read Next

- Go back to [The Eight Primitives](part-2-primitives.md) if you want to compare all eight as one system again.
- Use [Code Review](code-review.md), [Agentic Workflows](agentic-workflows.md), and the surface guides to see where explicit and learned repository knowledge show up outside the editor.
