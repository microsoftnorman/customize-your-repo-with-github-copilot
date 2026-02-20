# Part II: The Primitives

[← Back to Guide](../ReadMe.md) | [← Part I: Foundations](part-1-foundations.md)

---

GitHub Copilot provides seven customization primitives. Six shape what Copilot knows and how it thinks; the seventh — hooks — provides runtime enforcement and observability.

**See it in action:** [Agent Sessions Day](https://www.youtube.com/watch?v=tAezuMSJuFs) is a full-day event covering all seven primitives. Key segments: [Keynote](https://www.youtube.com/watch?v=tAezuMSJuFs&t=1152s) by Harald Kirschner, [Customize Your Agents](https://www.youtube.com/watch?v=flpKLkZla2Q) by Courtney Webster (instructions, prompts, skills, agents), and [Extend Agents with MCP](https://www.youtube.com/watch?v=_g29UQjIAeI) by Connor Peet.

| Primitive | Location | When Loaded | Scope |
|-----------|----------|-------------|-------|
| [**Always-on Instructions**](part-2-1-always-on-instructions.md) | `.github/copilot-instructions.md` | Every request | Entire session |
| [**File-based Instructions**](part-2-2-file-based-instructions.md) | `.github/instructions/*.instructions.md` | File pattern match | While file in context |
| [**Prompts**](part-2-3-prompts.md) | `.github/prompts/*.prompt.md` | User invokes `/name` | Single task |
| [**Skills**](part-2-4-skills.md) | `.github/skills/*/SKILL.md` | Description matches intent | Single task |
| [**Custom Agents**](part-2-5-custom-agents.md) | `.github/agents/*.md` | User invokes `@name` | Until switched |
| [**MCP**](part-2-6-mcp.md) | `.vscode/mcp.json` | Session start | Entire session |
| [**Hooks (Preview)**](part-2-7-hooks.md) | `.github/hooks/*.json` | Agent session events | Coding agent, CLI, and VS Code Chat (1.109.3+) |

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
|    Hooks (Preview)                      |  ← Runtime enforcement
|    preToolUse / postToolUse / etc.      |  ← Audit, deny, log
+-----------------------------------------+
```

Each layer adds specificity. The foundation (always-on instructions) applies everywhere; other primitives activate based on context.

**Important limitation:** Custom instructions, prompts, skills, and agents affect **Copilot Chat interactions only**. Inline suggestions (ghost text autocomplete) operate on a separate pipeline and do not read customization files. Use Chat-based interactions for convention-aware code generation.

**Not sure which primitive to use?** See the [Quick Decision Guide](part-3-reference.md#quick-decision-guide) in Part III for a lookup table that maps common scenarios to the right primitive.

---

## Composition Patterns

Individual primitives are table stakes. The real power is in how they combine. Most production setups use three or more primitives working together — each handling a different layer of the problem.

### Pattern 1: The Review Pipeline

A code review workflow that combines four primitives:

```
Always-on instructions    → "We use Vitest, not Jest. All components need tests."
     +
Custom agent (@reviewer)  → Persona with security expertise, constrained to read-only tools
     +
Skill (review-checklist)  → Step-by-step procedure: check types, check tests, check security
     +
MCP (GitHub)              → Reads PR diff, posts review comments directly
```

The instructions set the standards. The agent sets the personality and tool access. The skill provides the procedure. MCP connects to the external system. No single primitive could do this alone.

### Pattern 2: The Scaffolding Stack

A component generation workflow using three primitives:

```
File-based instructions    → "React components use functional style with TypeScript interfaces"
  (applyTo: **/*.tsx)
     +
Prompt (/new-component)   → Template with ${input:componentName}, references the design system
     +
MCP (Figma)               → Pulls component specs from design files
```

The file-based instruction activates automatically because the output is a `.tsx` file. The prompt provides the task template. MCP pulls external context the model couldn't otherwise access.

### Pattern 3: The Guarded Agent

An autonomous coding agent with safety rails:

```
Custom agent (@deploy)    → Persona authorized for deployment tasks, model array for fallback
     +
Skill (deploy-runbook)    → Full deployment procedure with rollback steps
     +
MCP (PagerDuty + AWS)     → Checks incident status, manages infrastructure
     +
Hooks (preToolUse)        → Blocks destructive commands, requires approval for production changes
```

The agent provides intent and tool access. The skill packages tribal knowledge. MCP connects to infrastructure. Hooks enforce guardrails *outside* the model's control — even if the model decides to do something dangerous, the hook blocks it before execution.

### How to Think About Composition

Each primitive answers a different question:

| Question | Primitive |
|----------|-----------|
| What rules always apply? | Always-on instructions |
| What rules apply to *this* file type? | File-based instructions |
| What steps does this task follow? | Prompts (user-triggered) or Skills (auto-discovered) |
| Who is the AI acting as? | Custom agents |
| What external systems can it reach? | MCP |
| What is it *not allowed* to do? | Hooks |

When designing a workflow, start from the task and ask each question. If the answer is "not applicable," skip that primitive. Most tasks need two or three; complex workflows use four or five. If a setup requires all seven, it's probably doing too much — consider splitting it into separate agent-driven workflows that hand off to each other.

---

## Context Window Guidelines

Every primitive consumes tokens. Keep them focused:

| Primitive | Recommended Size |
|-----------|------------------|
| Always-on instructions | 500-2000 words |
| File-based instructions | 200-500 words each |
| Prompts | 100-500 words |
| Skills | 500-1500 words |
| Custom agents | 200-1000 words |

If Copilot seems to "forget" rules, your instructions may be too long. Move specialized content to file-based instructions or skills.

For **individual** preferences that should persist across sessions and workspaces (e.g., preferred test style, naming conventions), consider enabling [Copilot Memory (Preview)](part-3-reference.md#copilot-memory-preview) instead of encoding personal preferences in shared customization files.

---

## Debugging What's Loaded

To see exactly what context is active:

Open diagnostics by right-clicking in the Chat view and selecting **Diagnostics**, or search for **Chat: Show Chat Customization Diagnostics** in the Command Palette. This shows loaded instructions, skills, and configuration status.

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

## 7. [Hooks (Preview)](part-2-7-hooks.md)

Runtime enforcement and observability for agent sessions. Execute custom shell commands at key points during agent sessions to enforce security policies, produce audit trails, block dangerous operations, and send notifications. Hooks operate outside the model's context — they don't influence how Copilot thinks, but they govern what the agent is allowed to do.

---

[← Part I: Foundations](part-1-foundations.md) | [Next: Part III - Reference →](part-3-reference.md)
