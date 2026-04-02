# Part II: The Primitives

[← Back to Guide](../ReadMe.md) | [← Part I: Foundations](part-1-foundations.md)

---

GitHub Copilot provides six customization primitives that shape what Copilot knows and how it thinks. Beyond the primitives, hooks provide runtime enforcement, and [Copilot Memory](part-2-8-memory.md) provides automatic repository-level learning.

These mechanisms work across multiple Copilot surfaces — VS Code, Visual Studio, GitHub.com, and [GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) (a terminal-based AI agent). The table below notes where each one applies:

| Mechanism | Location | When Loaded | Scope | CLI Support |
|-----------|----------|-------------|-------|-------------|
| [**Always-on Instructions**](part-2-1-always-on-instructions.md) | `.github/copilot-instructions.md` | Every request | Entire session | ✅ |
| [**File-based Instructions**](part-2-2-file-based-instructions.md) | `.github/instructions/*.instructions.md` | File pattern match | While file in context | ✅ |
| [**Prompts**](part-2-3-prompts.md) | `.github/prompts/*.prompt.md` | User invokes `/name` | Single task | VS Code only |
| [**Skills**](part-2-4-skills.md) | `.github/skills/*/SKILL.md` | Description matches intent | Single task | ✅ |
| [**Custom Agents**](part-2-5-custom-agents.md) | `.github/agents/*.md` | User invokes `@name` | Until switched | ✅ |
| [**MCP**](part-2-6-mcp.md) | `.vscode/mcp.json` | Session start | Entire session | ✅ |
| [**Hooks**](part-2-7-hooks.md) | `.github/hooks/*.json` | Agent session events | Coding agent only | ✅ |
| [**Copilot Memory**](part-2-8-memory.md) | Managed by GitHub | Automatic | Repository-wide | ✅ |

---

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
|    Hooks (coding agent only)            |  ← Runtime enforcement
|    preToolUse / postToolUse / etc.      |  ← Audit, deny, log
+-----------------------------------------+
```

Each layer adds specificity. The foundation (always-on instructions) applies everywhere; other primitives activate based on context.

---

## Context Window Guidelines

Every primitive consumes tokens. Keep them focused:

| Primitive | Recommended Size |
|-----------|------------------|
| Always-on instructions | 500-2000 words |
| File-based instructions | 200-500 words each |
| Skills | 500-3000 words |
| Custom agents | 200-1000 words |

If Copilot seems to "forget" rules, your instructions may be too long. Move specialized content to file-based instructions or skills.

---

## Debugging What's Loaded

To see exactly what context is active:

1. Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Run **"Chat: Diagnostics"** (from the Configure menu)
3. This shows loaded instructions, skills, and configuration status

For deeper debugging, use **"Developer: Log Chat Input History"** or **"Developer: Inspect Chat Model"** commands.

---

## 1. [Always-on Instructions](part-2-1-always-on-instructions.md)

The foundation layer. Define your tech stack, coding conventions, security requirements, and anti-patterns. These rules apply to every Copilot interaction in your repository.

## 2. [File-based Instructions](part-2-2-file-based-instructions.md)

Targeted rules that activate based on file patterns. Use for language-specific conventions, area-specific rules, or different standards for different parts of your codebase.

## 3. [Prompts](part-2-3-prompts.md)

Reusable task templates invoked with `/promptname`. Create prompts for component scaffolding, test generation, documentation, and repeatable workflows.

## 4. [Skills](part-2-4-skills.md)

Procedural knowledge that Copilot discovers and applies when relevant. Package specialized capabilities—like Prisma migrations or GitHub issue templates—into portable, reusable skills.

## 5. [Custom Agents](part-2-5-custom-agents.md)

Specialized AI personas with defined behaviors and tool access. Build code reviewers, architects, mentors, and role-specific assistants.

## 6. [MCP (Model Context Protocol)](part-2-6-mcp.md)

External service integrations. Connect Copilot to databases, APIs, ticketing systems, and any external tool your workflow requires.

## 7. [Hooks](part-2-7-hooks.md)

Runtime enforcement and observability for the coding agent. Execute custom shell commands at key points during agent sessions to enforce security policies, produce audit trails, block dangerous operations, and send notifications. Hooks operate outside the model's context — they don't influence how Copilot thinks, but they govern what the agent is allowed to do.

## 8. [Copilot Memory](part-2-8-memory.md)

Automatic repository-level learning that builds context over time. Unlike the explicit primitives above, Memory works passively — Copilot observes patterns in your codebase and conversations, then applies what it learned in future sessions. Memory complements explicit customization rather than replacing it.

## 9. [Agentic Workflows](part-2-9-agentic-workflows.md)

GitHub Agentic Workflows run coding agents inside GitHub Actions — on a schedule, on events, or on demand. This section covers how they work, how to configure the coding agent for autonomous tasks, and how the customization primitives from this guide feed into continuous AI automation.

---

[← Part I: Foundations](part-1-foundations.md) | [Next: Part III - Reference →](part-3-reference.md)
