# Primitives in Action

[← Back to Guide](README.md) | [← The Agent Loop](agent-loop.md) | [Next: The Eight Primitives →](part-2-primitives.md)

*Updated: April 22, 2026.*

---

## Why This Chapter Exists

Most guides explain the primitives one by one and only later hint that they can be combined. Real teams discover them the other way around. They start with a workflow, feel the friction, and then realize that multiple primitives solve different parts of the same problem.

This chapter makes that composition visible early.

## Workflow 1: Teaching a New Repository to Stop Fighting Back

**Problem:** A team keeps re-explaining its stack and architecture every time it asks GitHub Copilot for help.

**What the loop needs:** better defaults, not a more creative one-off prompt.

| Primitive | Role |
|-----------|------|
| **Always-on Instructions** | Declare the tech stack, banned defaults, naming patterns, and architectural rules that apply everywhere |
| **File-based Instructions** | Scope framework or testing conventions to the folders where they actually matter |
| **Memory** | Reinforce the patterns GitHub Copilot keeps seeing in the repo |

**Why this works:** the first turn improves before the agent has to guess. The repository stops acting like an anonymous public codebase.

## Workflow 2: Turning Review Culture into Review Infrastructure

**Problem:** The same review comments appear in every pull request.

**What the loop needs:** reusable standards plus the ability to apply them in multiple environments.

| Primitive | Role |
|-----------|------|
| **Always-on Instructions** | Capture rules that should influence every review |
| **File-based Instructions** | Target domain-specific review expectations by path |
| **Custom Agent** | Create a reviewer posture for human-in-the-loop sessions |
| **Code Review** | Reuse the same instruction layer during pull request review |

**Why this works:** the knowledge moves out of reviewer memory and into repository memory, both explicit and implicit.

## Workflow 3: A Guarded Operational Agent

**Problem:** A team wants automation for deployment and incident work, but not blind trust.

**What the loop needs:** role definition, procedural knowledge, external reach, and hard boundaries.

| Primitive | Role |
|-----------|------|
| **Custom Agent** | Switch GitHub Copilot into a deployment or incident posture |
| **Skills** | Package the operational runbook so the steps stay consistent |
| **MCP** | Connect to the systems the task actually depends on |
| **Hooks** | Block risky commands and log sensitive behavior |

**Why this works:** one primitive changes the posture, one packages the knowledge, one expands reach, and one constrains execution.

## Workflow 4: Continuous AI Outside the Editor

**Problem:** The team wants the same repository knowledge to run on schedules, events, or remote infrastructure.

**What the loop needs:** portability.

| Environment | What It Reuses |
|-------------|----------------|
| **Agentic Workflows** | Instructions, skills, agents, and task intent in GitHub Actions |
| **Code Review** | Instruction files and repository knowledge on pull requests |
| **Copilot SDK** | The same runtime concepts inside a custom application |
| **Cloud Coding Agent** | The same repository layer, but running remotely and asynchronously |

**Why this works:** the primitives are not editor decorations. They are portable knowledge.

## The Pattern Behind All Four Workflows

Every successful setup answers the same four questions:

1. What should GitHub Copilot assume by default?
2. What task or role needs extra structure?
3. What systems must it reach?
4. What must it never be allowed to do?

That pattern is the bridge into the next chapter.

## Where to Read Next

Read [The Eight Primitives](part-2-primitives.md) next. That chapter takes these workflows apart and shows which primitive should carry which responsibility.
