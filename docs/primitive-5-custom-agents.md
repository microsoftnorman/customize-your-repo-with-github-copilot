# Primitive 5: Custom Agents

[← Back to The Eight Primitives](eight-primitives.md) | [← Skills](primitive-4-skills.md) | [Next: MCP →](primitive-6-mcp.md)

*Updated: April 22, 2026.*

---

## Where It Enters the Loop

Custom Agents change the loop at the level of role, posture, and available capabilities for an ongoing conversation or delegated task.

That is different from a Prompt, which frames one task, and different from a Skill, which packages one procedure. A Custom Agent changes who GitHub Copilot is acting as for a stretch of work.

## What This Primitive Is For

Use a Custom Agent when the work benefits from a durable mode with its own:

- persona,
- tool access,
- model preferences,
- response style,
- or handoff behavior.

Common examples:

- a security reviewer,
- a system architect,
- a deploy agent,
- a debugging specialist,
- a patient mentor,
- or a planning agent that should never jump straight into implementation.

## The Best Question to Ask Before Creating One

Ask whether the user needs a reusable task or a reusable role.

If the need is a reusable task, that points toward a Prompt or Skill.

If the need is a reusable posture that should persist across multiple turns and decisions, that points toward a Custom Agent.

That is the distinction that keeps teams from overusing agents where a smaller primitive would have been clearer.

## Why Agents Matter More in an Agentic World

Custom Agents become more valuable as the loop becomes more autonomous.

In a read-only conversation, persona can feel cosmetic. In an agentic workflow, it changes real behavior:

- what tools are available,
- what kinds of evidence the agent prioritizes,
- whether it behaves cautiously or aggressively,
- and how it structures findings and tradeoffs.

That is why the rewrite treats agents as operational controls, not just personality skins.

## Where the File Lives

Custom Agents usually live in `.github/agents/*.md`, though the ecosystem supports additional locations and `.agent.md` conventions.

The durable asset is still a markdown file with frontmatter and body instructions. The important part is not the syntax alone. It is the combination of tool scope, posture, and handoff logic.

## The Three Things an Agent Should Make Obvious

A good agent answers three questions quickly:

1. Who are you supposed to be?
2. What do you optimize for?
3. What are you not allowed to do?

Without those, the agent is usually just a verbose prompt wearing a different label.

## What a Good Agent Looks Like

```markdown
---
name: 'Security Reviewer'
description: 'Reviews code with a focus on security vulnerabilities'
tools: ['search', 'readFile', 'usages', 'getChangedFiles']
model: 'Claude Opus 4.7'
---

You are a senior security engineer reviewing code for vulnerabilities.

## Priorities
- Broken access control
- Input validation
- Secrets handling
- Unsafe deserialization

## Response Style
- Start with risk level
- Cite concrete vulnerability classes
- Give a direct fix recommendation
```

This works because the agent is not only role-play. It makes priorities and tool posture concrete.

## Handoffs and Subagents

This primitive becomes especially interesting once the team understands subagents.

A Custom Agent can be the worker to which another agent hands off a focused task. That means agents do not just change the top-level conversation. They can also define specialized delegated loops.

That is one of the most important links between this chapter and the local source material on subagents and orchestration. The useful mental model is not "pick a fancy persona." It is "define a specialist with isolated context, the right tools, and the right success criteria."

## When Not to Use an Agent

Do not create an agent just to avoid writing one good Prompt.

Do not create an agent if the only difference is a single reusable checklist.

Do not create an agent when all the repository needs is baseline conventions or file-scoped rules.

Agents are strong medicine. Use them when the role and constraints should persist across multiple turns.

## How It Composes with Other Primitives

| Primitive | Relationship |
|-----------|--------------|
| [Skills](primitive-4-skills.md) | Agents provide posture; Skills provide packaged procedure |
| [Prompts](primitive-3-prompts.md) | A Prompt can invoke or target a specific agent for one task |
| [MCP](primitive-6-mcp.md) | Agents often become far more useful once they can reach external tools |
| [Hooks](primitive-7-hooks.md) | Hooks constrain risky agent behavior at execution time |

## See It in Action

**See it in action:** [Customize your agents](https://www.youtube.com/watch?v=flpKLkZla2Q&t=578s) — Courtney Webster demos a planner Custom Agent with its own tools, model choices, and handoff into implementation.

## Creating Agents

In VS Code, use `/create-agent` in Chat or the **Customize Your Agent** flow from the Chat Customizations editor (gear icon). Both produce the same file format. Describe the agent in plain English and VS Code generates a draft `.agent.md` with appropriate `tools`, `description`, and body.

> 💬 **Try this prompt:**
> "Create a custom agent at `.github/agents/security-reviewer.agent.md` for a senior security engineer. Read-only tools only: search, readFile, usages. Focus on OWASP Top 10. The agent should cite CWE IDs in its findings."

### Core Frontmatter

Host differences matter here. In VS Code and other IDEs, fields like `argument-hint` and `handoffs` shape the interactive experience. On GitHub.com, those two fields are currently ignored for Copilot cloud agent compatibility. The inverse is also true: `mcp-servers` and `metadata` are cloud-agent-specific and are not used by VS Code and other IDE custom agents.

| Field | Description |
|-------|-------------|
| `name` | Display name in the agent picker |
| `description` | Placeholder text in chat input |
| `tools` | Available tools for this agent |
| `model` | AI model; supports arrays for fallback: `['Claude Sonnet 4.7 (copilot)', 'GPT-5 (copilot)']` |
| `handoffs` | Transitions to other agents |
| `argument-hint` | Hint text for user input in supported IDE surfaces |
| `user-invocable` | Whether it appears in the picker (default: `true`) |
| `disable-model-invocation` | Prevent automatic/subagent invocation (default: `false`) |
| `agents` | Restrict available subagents: names, `*`, or `[]` |
| `target` | Target environment: `vscode`, `github-copilot`, or both when omitted |
| `mcp-servers` | Cloud-agent MCP configuration for `github-copilot` target |
| `metadata` | Cloud-agent metadata annotations |
| `hooks` | Agent-scoped hooks in VS Code preview |

## Example Agents

### System Architect

```markdown
---
name: 'System Architect'
description: 'High-level design and architecture decisions'
tools: ['search', 'readFile', 'fetch', 'githubRepo']
model: 'Claude Opus 4.7'
handoffs:
  - label: 'Start Implementation'
    agent: 'agent'
    prompt: 'Implement the architecture outlined above.'
    send: false
---

You are a principal software architect with 20 years of experience.

## Focus
- System design and scalability
- Technology selection and trade-off analysis
- Long-term maintainability
- Incremental migration paths

## Response Style
- Start with the "why" before the "what"
- Include diagrams (Mermaid) when helpful
- List trade-offs explicitly
```

### Code Reviewer

```markdown
---
name: 'Code Reviewer'
description: 'Thorough code review focused on quality'
tools: ['search', 'readFile', 'usages', 'getChangedFiles']
model: 'Claude Opus 4.7'
---

You are a meticulous code reviewer.

## Review Priorities (in order)
1. Correctness — Does it work?
2. Security — Is it safe?
3. Performance — Is it efficient?
4. Maintainability — Can others understand it?
5. Style — Does it follow conventions?

## Feedback Style
- Use conventional comments: `nit:`, `suggestion:`, `question:`, `issue:`
- Explain the "why"
- Differentiate must-fix vs. nice-to-have
```

### Debug Specialist

```markdown
---
name: 'Debug Detective'
description: 'Methodical bug hunting and diagnosis'
tools: ['search', 'readFile', 'usages', 'terminalLastCommand', 'getTerminalOutput']
---

You are a systematic debugging expert.

## Process
1. Reproduce the issue
2. Isolate variables
3. Form hypotheses
4. Test systematically
5. Verify the fix

## Output
- Numbered diagnostic steps
- Expected vs. actual at each step
- Confidence level in diagnosis
```

### Patient Mentor

```markdown
---
name: 'Patient Mentor'
description: 'Explains concepts thoroughly for learning'
tools: ['search', 'readFile', 'fetch']
---

You are a patient senior developer mentoring a junior team member.

## Teaching Style
- Explain from first principles
- Use analogies and real-world examples
- Never make the user feel bad for not knowing
- Connect new concepts to familiar ones
```

## Subagents: Delegated Loops with Isolated Context

Subagents run tasks in a dedicated, isolated context window separate from the main chat. The main agent delegates work, the subagent gathers its own evidence, and only the summarized result returns. Context isolation keeps the parent loop clean.

**When to use subagents:**

- Independent research before implementation
- Parallel analysis across multiple areas
- Specialized review passes with different goals
- Narrow worker roles with different tool permissions

**In chat:** hint that the task should run in a subagent:

> 💬 **Try this prompt:**
> "Run a sub-agent to analyze test coverage gaps in `src/services/` and return a prioritized list of missing test cases."

### Controlling Subagent Invocation

| Property | Default | Purpose |
|----------|---------|---------|
| `user-invocable` | `true` | Set to `false` to create subagent-only agents hidden from the picker |
| `disable-model-invocation` | `false` | Set to `true` when agents should only be triggered explicitly by users |
| `agents` | `*` (all) | Restrict which subagents a given agent can invoke: names, `*`, or `[]` |

### Orchestrator Pattern

```markdown
---
name: TDD
tools: ['agent']
agents: ['Red', 'Green', 'Refactor']
---

Implement features using test-driven development:
1. Use **Red** to write failing tests
2. Use **Green** to implement minimum code
3. Use **Refactor** to improve quality while tests pass

Repeat until the feature is complete.
```

### Handoffs

Handoffs create explicit, user-visible workflow transitions. Each handoff supports `label` (button text), `agent` (target), `prompt` (instructions), `send` (auto-submit, default: `false`), and `model` (optional override).

```markdown
---
name: 'Code Reviewer'
handoffs:
  - label: 'Implement Fixes'
    agent: 'agent'
    prompt: 'Implement the fixes identified in the review above.'
    send: false
---
```

## Where to Read Next

- Read [MCP](primitive-6-mcp.md) next if the role also needs external systems.
- Revisit [The Agent Loop](agent-loop.md) if agent posture, subagents, and delegated loops still feel abstract.
