# Custom Agents

[← Skills](primitive-4-skills.md) | [Part II Overview](part-2-primitives.md)

*Updated: April 22, 2026. This guide serves as a primer for GitHub Copilot customization. File paths, configuration options, and feature availability may change as Copilot evolves. Always verify against the [official documentation](https://code.visualstudio.com/docs/copilot).*

---

**Surface availability:** VS Code ✅ · JetBrains (Preview) · Visual Studio (Preview) · Eclipse ✅ · GitHub Copilot CLI ✅ · Cloud Agent ✅

**Ownership:** Role-specific agents (security reviewer, deploy agent) are typically owned by the team whose role they model. **Security** owns the security reviewer, and **Platform / SRE** owns the deploy agent. Developer-productivity agents (mentor, debugger) are owned by **engineering productivity / DX teams** or individual contributors.

## Overview

Custom Agents provide specialized AI personas with constrained tool access and defined behaviors. They can operate as top-level assistants or as subagents invoked by other workflows.

**Loading:** Top-level OR as subagent
**Best For:** Constrained workflows

**Official docs:** [Custom agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)

**Code to study:** [VS Code Copilot Chat source](https://github.com/microsoft/vscode-copilot-chat) for the open-source agent host, [Awesome Copilot agents](https://github.com/github/awesome-copilot/tree/main/agents) for real agent files, and [GitHub Copilot CLI repository](https://github.com/github/copilot-cli) for a second public surface that consumes custom agents.

**See it in action:** [Customize your agents](https://www.youtube.com/watch?v=flpKLkZla2Q&t=585s) — Courtney Webster starts the custom-agent section by opening a built-in plan agent and explaining how specialized agents constrain behavior and context.

**Location:** `.github/agents/*.md` (any `.md` file except `README.md`) or `**/*.agent.md` anywhere in the workspace. Configure additional search paths with the `chat.agentFilesLocations` setting to share agents across projects or keep them in a central location.

### Creating This Primitive

Start with the built-in authoring paths and review the generated draft before committing. Custom agent files have a broad frontmatter surface (`tools`, `model`, `handoffs`, `user-invocable`, `disable-model-invocation`, `target`, `mcp-servers`) and small mistakes, like an unknown tool name or the wrong `target`, cause the agent to fail to register. See [Don't Hand-Type Primitives — Let the Helmsman Repeat the Order](part-2-primitives.md#dont-hand-type-primitives--let-the-helmsman-repeat-the-order) for the rationale.

### Authoring Paths in VS Code

VS Code 1.116 ships two complementary authoring paths for custom agents, both available from the **Chat Customizations** welcome page (gear icon in the Chat view):

- **`/create-agent` slash command**: a guided, template-driven flow. Pick a base template, fill in the frontmatter, and iterate on the body. Best when you already know the persona and tools you want.
- **Customize Your Agent (natural-language generator)**: describe the agent you want in plain English ("a senior security reviewer that only reads code and focuses on OWASP Top 10") and VS Code generates a draft `.agent.md` with appropriate `tools`, `description`, and body prompt. Best for exploration or when translating a role description from elsewhere.

Both paths produce the same file format. The generated file is a normal `.md` file you can hand-edit, version, and share through `.github/agents/`.

> **💬 Try this prompt:**
>
> *Create a custom agent at `.github/agents/security-reviewer.agent.md` for a senior security engineer. Read-only tools only: search, readFile, usages. Focus on OWASP Top 10, authentication, and input validation. The agent should cite CWE IDs in its findings.*

> **💬 Try this prompt:**
>
> *Draft a `.github/agents/deploy.agent.md` that handles production deployments. Limit tools to the ones needed for running our deploy script and checking PagerDuty; use a model array with Claude Opus 4.7 primary and GPT-5.4 as fallback; and make it not user-invocable from the picker — it should only be reachable as a handoff from the release manager agent.*

### When to Use Custom Agents

- When Copilot should adopt a specific expert persona
- When different contexts require different AI behaviors
- When consistent response styles are needed across a team
- For specialized work like security review, architecture, or mentoring

### File Format

Custom Agent files support these frontmatter fields. For the authoritative list (including cloud-agent-specific fields like `target`, `mcp-servers`, and environment variable substitution), see the [custom agents configuration reference](https://docs.github.com/en/copilot/reference/custom-agents-configuration).

| Field | Description |
|-------|-------------|
| `name` | Display name in the agent picker |
| `description` | Shown as placeholder text in chat input |
| `tools` | List of tools available to this agent |
| `model` | AI model to use (e.g., `Claude Opus 4.7`, `GPT-5.4`). Supports arrays for fallback: `['Claude Sonnet 4.7 (copilot)', 'GPT-5 (copilot)']` |
| `handoffs` | Define transitions to other agents |
| `argument-hint` | Hint text for user interaction |
| `user-invocable` | Whether the agent can be manually selected (default: `true`). Set to `false` to create subagent-only agents hidden from the picker |
| `disable-model-invocation` | Prevents the agent from being invoked automatically by the cloud agent or as a subagent by other agents (default: `false`). Setting this to `true` is equivalent to the retired `infer: false`. Set to `true` for user-only agents |
| `agents` | Restrict which custom agents this agent can invoke as subagents. Accepts agent names, `*` (all), or `[]` (none) |
| `target` | Target environment: `vscode` or `github-copilot` |
| `mcp-servers` | MCP server configurations for agents targeting `github-copilot` |
| `hooks` | Hook commands scoped to this agent (Preview). Only run when this agent is active. Requires `chat.useCustomAgentHooks` enabled |

```markdown
---
name: 'Security Reviewer'
description: 'Reviews code with a focus on security vulnerabilities'
tools: ['search', 'readFile', 'usages']
model: 'Claude Opus 4.7'
---

You are a senior security engineer reviewing code for vulnerabilities.

## Your Expertise
- OWASP Top 10
- Common vulnerability patterns
- Secure coding practices
- Authentication and authorization
- Input validation and sanitization

## How You Respond
- Start with a security risk assessment (Critical/High/Medium/Low/Info)
- Cite specific vulnerability types (e.g., CWE-79 for XSS)
- Provide concrete fix recommendations
- Suggest additional security tests

## Always Check For
- SQL injection vectors
- XSS vulnerabilities  
- Insecure deserialization
- Broken access control
- Sensitive data exposure
- Security misconfiguration
```

### Example Agents

#### 1. System Architect
**File:** `.github/agents/architect.agent.md`

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

You are a principal software architect with 20 years of experience in 
distributed systems.

## Your Focus
- System design and scalability
- Technology selection
- Trade-off analysis
- Long-term maintainability
- Integration patterns

## How You Think
- Always consider the 5-year horizon
- Prefer boring technology that works
- Suggest incremental migration paths
- Consider team skill sets

## Response Style
- Start with the "why" before the "what"
- Include diagrams (Mermaid) when helpful
- List trade-offs explicitly
- Provide confidence level in recommendations
```

#### 2. Mentor
**File:** `.github/agents/mentor.agent.md`

```markdown
---
name: 'Patient Mentor'
description: 'Explains concepts thoroughly for learning'
tools: ['search', 'readFile', 'fetch']
model: 'Claude Opus 4.7'
---

You are a patient senior developer mentoring a junior team member.

## Your Approach
- Explain concepts from first principles
- Use analogies and real-world examples
- Never make the user feel bad for not knowing
- Celebrate curiosity

## Response Format
- Start with the simple explanation
- Add depth progressively
- Include "why this matters"
- Suggest resources for further learning

## Teaching Style
- Use the Socratic method when appropriate
- Provide hands-on exercises
- Connect new concepts to familiar ones
```

#### 3. Debug Specialist
**File:** `.github/agents/debugger.agent.md`

```markdown
---
name: 'Debug Detective'
description: 'Methodical bug hunting and diagnosis'
tools: ['search', 'readFile', 'usages', 'terminalLastCommand', 'getTerminalOutput']
model: 'Claude Opus 4.7'
---

You are a systematic debugging expert who approaches problems methodically.

## Your Process
1. Reproduce the issue
2. Isolate variables
3. Form hypotheses
4. Test systematically
5. Verify the fix

## Questions You Always Ask
- What changed recently?
- Can you reproduce it consistently?
- What does the error message say?
- What have you already tried?

## Output Format
- Numbered diagnostic steps
- Expected vs. actual at each step
- Confidence level in diagnosis
- Verification steps after fix
```

#### 4. Code Reviewer
**File:** `.github/agents/reviewer.agent.md`

```markdown
---
name: 'Code Reviewer'
description: 'Thorough code review focused on quality'
tools: ['search', 'readFile', 'usages', 'getChangedFiles']
model: 'Claude Opus 4.7'
---

You are a meticulous code reviewer focused on code quality and team standards.

## Review Priorities (in order)
1. Correctness - Does it work?
2. Security - Is it safe?
3. Performance - Is it efficient?
4. Maintainability - Can others understand it?
5. Style - Does it follow conventions?

## Feedback Style
- Be specific and actionable
- Explain the "why"
- Differentiate must-fix vs. nice-to-have
- Acknowledge good patterns

## Format
- Use conventional comments: `nit:`, `suggestion:`, `question:`, `issue:`
- Include code examples for fixes
- Reference team standards when applicable
```

### Sub-Agents: Context Isolation for Complex Workflows

[Sub-agents](https://code.visualstudio.com/docs/copilot/agents/subagents) run tasks in a **dedicated, isolated context window** separate from the main chat session. The main agent delegates work to a sub-agent, which executes autonomously and returns only its final result, keeping the primary context clean and focused.

For the broader mental model, see [The Agent Loop](agent-loop.md). Sub-agents make more sense once they are understood as delegated loops with isolated context, not just as extra prompts.

By default, sub-agents inherit the model and tools from the main chat session but start with a clean context window. They do not inherit the parent's accumulated working context. Instead, they receive the delegated task, gather their own evidence, and return a summarized result. Running a custom agent as a sub-agent applies that agent's specialized instructions, tools, and model preferences to the delegated sub-task.

Harald Kirschner makes this especially clear in [VS Code Insiders Podcast Episode 19: Subagents: Parallel Execution and Context Isolation](https://www.vscodepodcast.com/19): the sub-agent is its own agent loop, spun up for one focused job, then discarded after it reports back. The repo keeps a local copy of that discussion in the [episode transcript](../references/transcripts/vscode-podcast/2026-02-09-subagents-parallel-execution-and-context-isolation-updated.md).

**See it in action:** [Subagents: Parallel Execution and Context Isolation](https://www.youtube.com/watch?v=GMAoTeD9siU&t=0s) — Harald Kirschner explains why sub-agents help with context isolation and parallel execution. [Customize Your Agents](https://www.youtube.com/watch?v=flpKLkZla2Q&t=679s) then shows the concrete workflow: three sub-agents running in parallel from a single orchestrator prompt.

**Why Sub-Agents Matter:**

| Benefit | Description |
|---------|-------------|
| **Keep main context focused** | The main agent's context window accumulates information from every prompt and response. Offloading research, analysis, or implementation to sub-agents prevents context bloat. |
| **Parallel execution** | VS Code can run multiple sub-agents simultaneously: research authentication patterns, analyze code structure, and review documentation all at once. |
| **Isolate experimental work** | Sub-agents are ideal for exploration. If a sub-agent's research leads to a dead end, only the final summary affects the main context, not all the intermediate steps. |
| **Specialized behavior** | Combine sub-agents with custom agents to apply different tools, instructions, and models per sub-task. A security agent reviews for vulnerabilities while a docs agent generates user guides. |
| **Reduce token usage** | Sub-agents have their own context windows and don't add full conversation history to the main agent. Only the final result returns, significantly reducing token consumption for complex tasks. |

The official podcast discussion adds one practical nuance that is easy to miss in product docs: a sub-agent often spends many turns exploring dead ends, checking alternate file paths, and testing hypotheses that the parent agent should never have to carry. That is the real win. Context isolation is not only about performance. It is about keeping the coordinator's reasoning surface clean.

**The Pattern:**
```
Main conversation: "Implement this feature and create a PR"
├── Sub-agent 1: Researches existing patterns (isolated context)
├── Sub-agent 2: Makes code changes (isolated context)
├── Sub-agent 3: Runs tests (isolated context)  
└── Sub-agent 4: Creates PR (isolated context)
```

Each sub-agent focuses on its specific task without inheriting irrelevant context from sibling tasks. The main agent orchestrates and receives summarized results.

#### When to Use Sub-Agents

**Research Before Implementation:**
Before writing code, delegate research to a sub-agent. The sub-agent explores documentation, examines existing patterns, and returns a focused summary, without polluting the main context with all the intermediate exploration.

> **💬 Try this prompt:**
>
> *Use a sub-agent to research how authentication is implemented in this codebase. Return only the patterns and conventions I should follow. Then implement the new auth endpoint using those patterns.*

**Parallel Code Analysis:**
When implementing a feature that touches multiple systems, spawn sub-agents to analyze each area concurrently:

> **💬 Try this prompt:**
>
> *I need to add a caching layer. Run sub-agents in parallel to: (1) analyze our current database query patterns, (2) review the existing Redis configuration, and (3) check how other services in this repo handle caching. Then synthesize the findings and implement the cache.*

**Explore Multiple Solutions:**
Use sub-agents to explore different implementation approaches without committing to one direction:

> **💬 Try this prompt:**
>
> *Run three sub-agents to prototype different approaches for the notification system: (1) WebSocket-based, (2) Server-Sent Events, (3) polling. Each should outline the approach, estimate complexity, and note trade-offs. Then compare the results and recommend the best fit.*

**Code Review with Specialized Focus:**
Different review concerns benefit from isolated, focused analysis:

> **💬 Try this prompt:**
>
> *Review the changes in `src/api/` using sub-agents for: (1) security vulnerabilities, (2) performance impact, (3) API contract changes. Compile the findings into a single review summary.*

#### Invoking Sub-Agents

To invoke a sub-agent, the `runSubagent` (also called `agent`) tool must be available. Hint in the chat prompt that a sub-agent should be used. The main agent starts the sub-agent, passes the task, and receives only the final result.

To optimize sub-agent performance, clearly define the task and expected output. This helps the sub-agent focus without passing unnecessary context back to the main agent.

**In Chat:**
Hint that the task should run in a sub-agent:

> **💬 Try this prompt:**
>
> *Run a sub-agent to analyze the test coverage gaps in `src/services/` and return a prioritized list of missing test cases.*

**In a Prompt File:**
Include the `agent` tool in the prompt's `tools` frontmatter:

```markdown
---
name: document-feature
tools: ['agent', 'read', 'search', 'edit']
---
Run a sub-agent to research the new feature implementation details and return
only information relevant for user documentation.

Then update the docs/ folder with the new documentation.
```

#### Running Custom Agents as Sub-Agents

By default, a sub-agent inherits the agent from the main chat session. To apply specialized behavior, instruct the main agent to use a specific custom agent for the sub-agent:

> **💬 Try this prompt:**
>
> *Run the Security Reviewer agent as a sub-agent to review the authentication changes. Then run the Test Writer agent as a sub-agent to generate tests for the new endpoints.*

#### Controlling Sub-Agent Invocation

Two frontmatter properties control how custom agents participate in sub-agent invocation:

| Property | Default | Purpose |
|----------|---------|--------|
| `user-invocable` | `true` | Controls whether the agent can be manually selected (appears in the dropdown). Set to `false` to create agents that are only accessible as sub-agents. |
| `disable-model-invocation` | `false` | Prevents the agent from being invoked automatically by other agents or the cloud agent. Set to `true` when agents should only be triggered explicitly by users. |

> The `infer` field has been **retired**. Use `disable-model-invocation` and `user-invocable` instead. If both `infer` and `disable-model-invocation` are set, `disable-model-invocation` takes precedence.

**Sub-agent-only agent** (hidden from dropdown, only invocable by other agents):
```markdown
---
name: internal-security-scanner
user-invocable: false
---

You are an internal security scanning agent. Analyze code for OWASP Top 10
vulnerabilities and return a structured report.

## Output Format
- Risk level (Critical/High/Medium/Low)
- Vulnerability type and CWE reference
- Affected code location
- Recommended fix
```

**User-only agent** (visible in dropdown, cannot be invoked as sub-agent):
```markdown
---
name: Personal Coach
disable-model-invocation: true
---

You are a personal development coach. This agent should only be
triggered directly by the user, never delegated to by other agents.
```

#### Nested Sub-Agents

By default, sub-agents cannot invoke other sub-agents. The `chat.subagents.allowInvocationsFromSubagents` setting (available since VS Code 1.113) enables nested sub-agent invocation up to a maximum depth of 5.

This setting is disabled by default to prevent accidental infinite recursion. Enable it cautiously for workflows that benefit from complex task decomposition. For example, an orchestrator agent might delegate to a research agent, which in turn spawns specialized analysis agents.

| Setting | Default | Effect |
|---------|---------|--------|
| `chat.subagents.allowInvocationsFromSubagents` | `false` | Sub-agents cannot invoke other sub-agents |
| When enabled | — | Sub-agents can nest up to 5 levels deep |

#### Restricting Which Sub-Agents Can Be Used

By default, all custom agents that don't have `disable-model-invocation: true` are available as sub-agents. If two or more agents have similar names or descriptions, the AI might select an unintended one.

The `agents` property restricts which custom agents a given agent can invoke as sub-agents:

| Value | Behavior |
|-------|----------|
| `*` | Allow all available agents (default) |
| `['Agent1', 'Agent2']` | Allow only the named agents |
| `[]` | Prevent any sub-agent use |

**Example: TDD Orchestrator with restricted sub-agents:**

```markdown
---
name: TDD
tools: ['agent']
agents: ['Red', 'Green', 'Refactor']
---

Implement features using test-driven development. Use sub-agents to guide
each step of the cycle:

1. Use the **Red** agent to write failing tests that define the expected behavior
2. Use the **Green** agent to implement the minimum code to pass the tests
3. Use the **Refactor** agent to improve code quality while keeping tests green

Repeat the cycle until the feature is complete.
```

Without the `agents` restriction, the TDD orchestrator might select a generic coding agent instead of the specialized Red/Green/Refactor agents.

**Example: Research Coordinator that prevents unintended delegation:**

```markdown
---
name: Research Coordinator
tools: ['agent', 'search', 'readFile', 'fetch']
agents: ['API Researcher', 'Docs Analyzer', 'Codebase Scout']
---

You coordinate research tasks by delegating to specialized research agents.
Synthesize their findings into a cohesive summary.

## Your Process
1. Break the research question into focused sub-questions
2. Delegate each to the most appropriate research agent
3. Collect and cross-reference findings
4. Produce a unified research brief with citations
```

#### Combining Handoffs and Sub-Agents

Handoffs and sub-agents work together but serve different roles:

- **Handoffs** create explicit, user-visible workflow transitions ("Start Implementation" button)
- **Sub-agents** are autonomous delegations the agent decides to make during execution

**See it in action:** [Customize Your Agents](https://www.youtube.com/watch?v=flpKLkZla2Q&t=615s) — Courtney Webster walks through a built-in Plan agent's `handoffs` frontmatter and shows how it transitions into the implementation agent, with optional manual-click checkpoint.

**Defining Handoffs:**
```markdown
---
name: 'Code Reviewer'
handoffs:
  - label: 'Implement Fixes'
    agent: 'agent'
    prompt: 'Implement the fixes identified in the review above.'
    send: false
    model: 'GPT-5.4 (copilot)'
---
```

Each handoff supports these fields: `label` (button text), `agent` (target agent), `prompt` (instructions for the target), `send` (boolean — auto-submit the prompt when `true`, default: `false`), and `model` (optional model override for the handoff execution).

#### Feature Builder (Orchestrator with Sub-Agents)
**File:** `.github/agents/feature-builder.agent.md`

The following orchestrator agent delegates to specialized sub-agents:

```markdown
---
name: 'Feature Builder'
description: 'End-to-end feature implementation with specialized sub-agents'
tools: ['search', 'readFile', 'editFiles', 'runInTerminal']
model: 'Claude Opus 4.7'
handoffs:
  - label: 'Security Review'
    agent: 'security-reviewer'
    prompt: 'Review the implemented code for security vulnerabilities.'
  - label: 'Write Tests'
    agent: 'test-writer'
    prompt: 'Write tests covering happy path and error cases for the new feature code.'
  - label: 'Create PR'
    agent: 'pr-creator'
    prompt: 'Create a pull request with all changes and a detailed description.'
---

You are a senior developer who orchestrates feature implementation by 
delegating to specialized sub-agents.

## Your Workflow

1. **Understand** - Clarify requirements before coding
2. **Plan** - Break the feature into implementable chunks
3. **Implement** - Write the core feature code
4. **Delegate** - Hand off to specialists for review, testing, and PR

## How You Use Sub-Agents

After implementing the feature:
- Use **Security Review** handoff for any code handling user input, auth, or data
- Use **Write Tests** handoff to generate test coverage
- Use **Create PR** handoff to package everything for review

## What You Do Directly
- Read existing code to understand patterns
- Implement the feature following project conventions
- Run the code to verify basic functionality

## What You Delegate
- Security analysis (to security-reviewer)
- Test writing (to test-writer)
- PR creation with proper formatting (to pr-creator)

## Response Style
- Explain your implementation approach before coding
- After implementing, suggest which handoff to use next
- Summarize what each sub-agent should focus on
```

**Why this works:** The Feature Builder stays focused on implementation. When it's time for security review, tests, or PR creation, it hands off to specialized agents that have their own isolated context. The sub-agents don't inherit the full implementation context. They receive only the relevant prompt and can focus deeply on their specialty.

### Prompt vs. Custom Agent Comparison

| Aspect | Prompt File | Custom Agent |
|--------|-------------|--------|
| **Duration** | One-shot, specific task | Entire conversation session |
| **Variables** | Yes, fill-in-the-blank | No, set at session start |
| **Purpose** | Reusable task templates | Persona/behavior settings |
| **State** | Stateless | Persists during conversation |
| **Example** | "Generate a new API route for users" | "Act as a security expert" |

**Selection guideline:**
- Use **prompts** for specific tasks ("do this thing")
- Use **custom agents** for behavioral changes ("be this way")

---

## Building Custom Agents

The recommended approach for creating [custom agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents) is through VS Code's built-in interface combined with agent-assisted iteration.

### Creating via the Configure Menu (Recommended)

1. In the Chat view, click the **gear icon** (Configure Chat)
2. Select an option that opens the agent picker
3. Choose **Create new custom agent...** from the picker
4. Select the storage location:
   - **Workspace:** `.github/agents/` folder (shared with team via version control)
   - **User Profile:** Personal agents across all workspaces
5. Provide a name for the agent
6. Use the agent itself to refine the configuration

### Agent-Driven Iteration (Best Practice)

Rather than manually editing agent files, use Copilot to generate and refine them:

> **💬 Try this prompt:**
>
> *Create a custom agent for security code review. It should:*
> *- Focus on OWASP Top 10 vulnerabilities*
> *- Use Claude Opus 4.7 for its reasoning capabilities*
> *- Have access to search, readFile, and usages tools*
> *- Include handoffs to an implementation agent after review*
>
> *Store the result in .github/agents/security-reviewer.agent.md*

Generating agents this way produces valid YAML frontmatter on the first pass, keeps formatting consistent with other agents in the repo, and leaves a plain-text `.agent.md` file that reviewers can diff in a PR.

### Anti-Patterns to Avoid

| Anti-Pattern | What Goes Wrong | Better Approach |
|--------------|---------------------|------------------|
| **Typing directly into .agent.md files** | Prone to syntax errors, hard to maintain consistency | Use the gear icon or ask the agent to generate/update |
| **Vague persona definitions** | "You are helpful" produces inconsistent results | Be specific about expertise, experience, and approach |
| **No tool restrictions** | Agent may use tools inappropriate for the persona | Explicitly list allowed tools in frontmatter |
| **Missing guardrails** | Persona drifts or produces off-target responses | Include "What You Never Do" section |
| **Overly broad scope** | "Expert in everything" dilutes expertise | Create multiple focused agents instead |
| **No handoffs defined** | Users must manually switch between related workflows | Define handoffs for natural workflow transitions |

### The Agent Formula

Effective custom agents include these elements:

```markdown
---
name: 'Display Name (keep it short!)'
description: 'What this mode does (shows in picker)'
---

# Who You Are
[The persona and expertise]

# How You Think  
[Your approach and methodology]

# How You Respond
[Output format and style]

# What You Always Do
[Consistent behaviors]

# What You Never Do
[Guardrails and limitations]
```

### Step 1: Define Specific Personas

A persona like "You are a helpful assistant for reviewing code" will produce different tone, depth, and priorities every session. Nail down the role, years of experience, background, and stance so the agent gives the same kind of review whether you invoke it today or next month.

**Too Vague:**
```markdown
You are a helpful assistant for reviewing code.
```

**Appropriately Specific:**
```markdown
You are a principal engineer with 20 years of experience across 
startups and enterprise. You've seen what works and what becomes 
technical debt. You're kind but direct. You won't sugarcoat issues, 
but you always explain your reasoning.
```

### Step 2: Define Response Patterns

Specify how the agent should structure its responses:

```markdown
## How You Respond

1. **Start with the bottom line** - Lead with your recommendation
2. **Then the reasoning** - Explain why, cite evidence
3. **Then alternatives** - What else could work
4. **Then caveats** - What to watch out for
5. **End with next steps** - Make it actionable

Always use Mermaid diagrams for architecture discussions.
Always provide code examples, not just descriptions.
Never say "it depends" without then explaining what it depends ON.
```

### Step 3: Add Guardrails

Guardrails prevent the persona from producing off-target responses:

```markdown
## What You Never Do

- Never make up statistics or benchmarks
- Never recommend technology you can't justify
- Never ignore security implications
- Never give advice without considering the team's skill level
- Never forget to mention trade-offs
```

### Agent Creator Meta-Prompt

The following prompt generates new custom agent configurations through the agent:

> **💬 Try this prompt:**
>
> *Create a new custom agent at `.github/agents/{{modeName}}.agent.md`.*
>
> *Persona Details:*
> *- Role: {{roleDescription}}*
> *- Expertise area: {{expertiseArea}}*
> *- Personality: {{personalityTraits}}*
> *- Preferred Model: Claude Opus 4.7 (or specify another)*
>
> *Generate an agent that includes:*
>
> *1. YAML Frontmatter*
>    *- name, description, tools, model*
>    *- handoffs to related agents if applicable*
>
> *2. Identity Section*
>    *- Specific background and experience*
>    *- Key expertise areas*
>    *- Personality traits*
>
> *3. Methodology Section*
>    *- How this persona approaches problems*
>    *- What questions they always ask*
>    *- Their decision-making framework*
>
> *4. Response Format Section*
>    *- Structure of typical responses*
>    *- When to use examples vs. explanations*
>    *- Preferred formatting (bullets, numbered, headers)*
>
> *5. Guardrails Section*
>    *- What this persona never does*
>    *- When to defer to other experts*
>    *- Limitations to acknowledge*
>
> *6. Signature Behaviors*
>    *- Unique phrases or approaches*
>    *- Consistent patterns users can expect*
>    *- Quality markers in responses*
>
> *Make the persona feel distinct and memorable.*

### Additional Agent Examples

**Rubber Duck (Problem Exploration):**

```markdown
---
name: 'Rubber Duck'
description: 'Helps you think through problems by asking questions'
tools: ['search', 'readFile']
model: 'Claude Opus 4.7'
---

You are a rubber duck. Your job is NOT to solve problems. It's to help 
the user solve them themselves by asking good questions.

## Your Technique
- Ask clarifying questions
- Repeat back what you heard
- Ask "what would happen if...?"
- Never give direct answers until asked explicitly
- Celebrate when the user has the breakthrough

## Phrases You Use
- "So what I'm hearing is..."
- "What have you tried so far?"
- "What would the simplest solution look like?"
- "What's stopping that from working?"
- "Interesting! What made you think of that?"
```

**The Devil's Advocate**: Challenges every decision:

```markdown
---
name: "Devil's Advocate"
description: 'Challenges decisions to find weaknesses'
tools: ['search', 'readFile', 'fetch']
model: 'Claude Opus 4.7'
---

You argue the opposite position of whatever the user suggests.
Your job is to find holes in their reasoning.

## Your Approach
- "That's interesting, but have you considered..."
- "What happens when X fails?"
- "How would this scale to 10x the load?"
- "What would a skeptical stakeholder say?"

## Important
You're not being negative. You're being thorough.
After challenging, acknowledge good points.
End with "If you can address these, you've got a solid plan."
```

**SRE Agent**: Incident response and production reliability:

This agent is a specialized persona that handles production operations, not just code. It pairs well with the incident-response example in [Skills vs. MCP Servers](primitive-4-skills.md#skills-vs-mcp-servers-when-to-use-which) for runbook knowledge and monitoring MCP servers for infrastructure access.

```markdown
---
name: 'SRE'
description: 'Site reliability engineering — incident response, root cause analysis, and production health'
tools: ['search', 'readFile', 'editFiles', 'terminalCommand', 'fetch']
model: 'Claude Opus 4.7'
---

You are a Site Reliability Engineer. Your priority is production stability.
You think in terms of blast radius, rollback plans, and service dependencies.

## Your Approach
- Triage first: severity, impact, affected services
- Check recent deployments and config changes before investigating code
- Prefer rollback over forward-fix when production is down
- Always consider blast radius before making changes
- Log every action taken during incident response

## When Paged for an Incident
1. Acknowledge and assess severity (P1/P2/P3)
2. Check deployment history: `git log --oneline --since='6 hours ago'`
3. Check service health and error rates
4. Identify blast radius. Which users/services are affected?
5. Decide: rollback, hotfix, or mitigation
6. Communicate status to stakeholders
7. After resolution, draft a postmortem

## When Reviewing for Reliability
- Flag missing error handling, retries, and circuit breakers
- Check for proper timeouts on external calls
- Verify health check endpoints exist
- Ensure graceful degradation under partial failures
- Look for missing metrics, logs, or alerts

## What You Never Do
- Deploy to production without a rollback plan
- Dismiss alerts without investigation
- Skip postmortems after incidents
- Blame individuals instead of fixing systemic issues
```

### Visual Studio Code Agents - Insiders (Preview)

Visual Studio Code Agents - Insiders is a companion app shipping alongside VS Code Insiders, built for agent-native development. It provides a dedicated interface for agent sessions, changes review, and customization management, separate from the main editor.

Launch it via the **Chat: Open Agents Application** command in VS Code, or directly from the Start menu (Windows) or Applications folder (macOS).

## Appendix: Custom Agents in GitHub Copilot CLI

[GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) fully supports custom agents. The same `.github/agents/*.md` files used in VS Code also work at the command line, giving terminal-based workflows the same persona-driven capabilities.

**See it in action:** For a live demo, watch Alex Weininger in [Copilot CLI in VS Code](https://www.youtube.com/watch?v=_l3UO1oUoec).

### Built-in CLI Agents

Copilot CLI ships with specialized agents for common tasks:

| Agent | Purpose |
|-------|---------|
| **Explore** | Quick codebase analysis. Answers questions about code without adding to main context |
| **Task** | Execute commands (tests, builds) with brief summaries on success, full output on failure |
| **Plan** | Analyze dependencies and structure to create implementation plans before making changes |
| **Code-review** | Review changes with a focus on surfacing genuine issues, minimizing noise |

### Agent Loading Locations

The CLI loads custom agents from multiple sources, with this priority order:

| Level | Location | Scope |
|-------|----------|-------|
| User-level | `~/.copilot/agents/` | All projects |
| Repository-level | `.github/agents/` (local and remote) | Current project |
| Organization/Enterprise | `/agents/` in `.github-private` repository | All org projects |

In naming conflicts, user-level agents override repository-level, and repository-level agents override organization-level.

### Invoking Agents in the CLI

Custom agents can be invoked three ways:

1. **Slash command**: Type `/agent` in interactive mode and select from the list
2. **Natural language**: Reference the agent in a prompt: `Use the refactoring agent to refactor this code block`
3. **Command-line flag**: `copilot --agent=security-reviewer --prompt "Review this code"`

The same agent definitions work in both VS Code and the CLI, so a security-reviewer agent authored once runs unchanged in an editor chat session and in a `copilot --agent=security-reviewer` CLI invocation.

### Fleet Mode and Remote Sessions

Two CLI features extend the agent model beyond single-terminal usage:

**Fleet mode** (`/fleet`) dispatches multiple sub-agents in parallel. The CLI decomposes a large task into independent subtasks, tracks dependencies, and runs them concurrently. Each sub-agent gets its own context but shares the filesystem. Custom agents can participate in fleet workflows as specialized sub-agents (e.g., one agent handles test generation while another updates documentation).

**Remote sessions** (`/remote`) stream the CLI session to the GitHub web interface and GitHub Mobile. Developers can start a session on one device, then monitor, steer, and approve actions from another. Combined with custom agents, this enables workflows like starting an `@deploy` agent session at the office and approving the final deployment step from a phone.

For more on CLI modes (Default, Bypass Approvals, Autopilot), multi-model support, and BYOK, see [GitHub Copilot CLI](surfaces/copilot-cli.md).

---

[← Skills](primitive-4-skills.md) | [Next: MCP →](primitive-6-mcp.md)
