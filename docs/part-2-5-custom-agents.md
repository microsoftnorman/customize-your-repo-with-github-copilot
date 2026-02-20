# Custom Agents

[← Skills](part-2-4-skills.md) | [Part II Overview](part-2-primitives.md)

---

## Overview

Custom Agents provide specialized AI personas with constrained tool access and defined behaviors. They can operate as top-level assistants or as subagents invoked by other workflows.

**Loading:** Top-level OR as subagent
**Best For:** Constrained workflows

**Official docs:** [Custom agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)

**See it in action:** [Customize Your Agents](https://www.youtube.com/watch?v=flpKLkZla2Q) — Courtney Webster demos building custom agents, agent skills, and MCP integrations, showing how to create agents for specific roles and wire them together with handoffs. Also available in the [Agent Sessions Day livestream](https://www.youtube.com/watch?v=tAezuMSJuFs&t=10598s) at 02:56:38.

**Location:** `.github/agents/*.md` (any `.md` file except `README.md`) or `**/*.agent.md` anywhere in the workspace. Configure additional search paths with the `chat.agentFilesLocations` setting to share agents across projects or keep them in a central location.

### When to Use Custom Agents

- When Copilot should adopt a specific expert persona
- When different contexts require different AI behaviors
- When consistent response styles are needed across a team
- For specialized work like security review, architecture, or mentoring

### File Format

Custom Agent files use the `.agent.md` extension and support these frontmatter fields:

| Field | Description |
|-------|-------------|
| `name` | Display name in the agent picker |
| `description` | Shown as placeholder text in chat input |
| `tools` | List of tools available to this agent |
| `model` | AI model to use (e.g., `Claude Opus 4.6`, `GPT-5.2`). Supports arrays for fallback: `['Claude Sonnet 4.5 (copilot)', 'GPT-5 (copilot)']` |
| `handoffs` | Define transitions to other agents |
| `argument-hint` | Hint text for user interaction |
| `user-invokable` | Whether the agent appears in the agents dropdown (default: `true`). Set to `false` to create subagent-only agents |
| `disable-model-invocation` | Prevents the agent from being invoked as a subagent by other agents (default: `false`). Set to `true` for user-only agents |
| `agents` | Restrict which custom agents this agent can invoke as subagents. Accepts agent names, `*` (all), or `[]` (none) |
| `target` | Execution target: `vscode` (default) or `github-copilot` for use with Copilot coding agent on GitHub |
| `mcp-servers` | MCP server config JSON for agents targeting `github-copilot` |

```markdown
---
name: 'Security Reviewer'
description: 'Reviews code with a focus on security vulnerabilities'
tools: ['search', 'readFile', 'usages']
model: 'Claude Opus 4.6'
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

The following agent configurations address common development scenarios:

#### 1. System Architect
**File:** `.github/agents/architect.agent.md`

```markdown
---
name: 'System Architect'
description: 'High-level design and architecture decisions'
tools: ['search', 'readFile', 'fetch', 'githubRepo']
model: 'Claude Opus 4.6'
handoffs:
  - label: 'Start Implementation'
    agent: 'agent'
    prompt: 'Implement the architecture outlined above.'
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
model: 'Claude Opus 4.6'
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
model: 'Claude Opus 4.6'
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
tools: ['search', 'readFile', 'usages', 'changes']
model: 'Claude Opus 4.6'
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

Sub-agents run tasks in a **dedicated, isolated context window** separate from the main chat session. The main agent delegates work to a sub-agent, which executes autonomously and returns only its final result — keeping the primary context clean and focused.

By default, subagents inherit the model and tools from the main chat session but start with a clean context window — they do not inherit instructions or conversation history from the parent agent. By running a custom agent as a sub-agent, specialized behavior, tools, and models can be applied to specific sub-tasks.

**Why Sub-Agents Matter:**

| Benefit | Description |
|---------|-------------|
| **Keep main context focused** | The main agent's context window accumulates information from every prompt and response. Offloading research, analysis, or implementation to sub-agents prevents context bloat. |
| **Parallel execution** | VS Code can run multiple sub-agents simultaneously — research authentication patterns, analyze code structure, and review documentation all at once. |
| **Isolate experimental work** | Sub-agents are ideal for exploration. If a sub-agent's research leads to a dead end, only the final summary affects the main context — not all the intermediate steps. |
| **Specialized behavior** | Combine sub-agents with custom agents to apply different tools, instructions, and models per sub-task. A security agent reviews for vulnerabilities while a docs agent generates user guides. |
| **Reduce token usage** | Sub-agents have their own context windows and don't add full conversation history to the main agent. Only the final result returns, significantly reducing token consumption for complex tasks. |

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

The following scenarios illustrate when sub-agents improve AI-assisted development workflows:

**Research Before Implementation:**
Before writing code, delegate research to a sub-agent. The sub-agent explores documentation, examines existing patterns, and returns a focused summary — without polluting the main context with all the intermediate exploration.

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

To invoke a sub-agent, the `runSubagent` (also called `agent`) tool must be available. Hint in the chat prompt that a sub-agent should be used — the main agent starts the sub-agent, passes the task, and receives only the final result.

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

Two frontmatter properties control how custom agents interact with the sub-agent system:

| Property | Default | Purpose |
|----------|---------|--------|
| `user-invokable` | `true` | Controls whether the agent appears in the agents dropdown in chat. Set to `false` to create agents that are only accessible as sub-agents. |
| `disable-model-invocation` | `false` | Prevents the agent from being invoked as a sub-agent by other agents. Set to `true` when agents should only be triggered explicitly by users. |

**Sub-agent-only agent** (hidden from dropdown, only invocable by other agents):
```markdown
---
name: internal-security-scanner
user-invokable: false
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

**Defining Handoffs:**
```markdown
---
name: 'Code Reviewer'
handoffs:
  - label: 'Implement Fixes'
    agent: 'agent'
    prompt: 'Implement the fixes identified in the review above.'
    send: false
    model: 'GPT-5.2 (copilot)'
---
```

Each handoff supports these fields:

| Field | Description |
|-------|-------------|
| `label` | Display text on the handoff button |
| `agent` | Target agent to switch to |
| `prompt` | Prompt text to send to the target agent |
| `send` | Auto-submit the prompt when the handoff is selected (default: `false`). Set to `true` to start the next step automatically. |
| `model` | Language model for the handoff. Use qualified format like `GPT-5.2 (copilot)` or `Claude Opus 4.6 (copilot)`. |

The `handoffs` field creates natural workflow transitions, where one agent can spawn another for specialized work.

#### 5. Feature Builder (Orchestrator with Sub-Agents)
**File:** `.github/agents/feature-builder.agent.md`

This example demonstrates the sub-agent pattern — an orchestrator agent that delegates to specialized sub-agents:

```markdown
---
name: 'Feature Builder'
description: 'End-to-end feature implementation with specialized sub-agents'
tools: ['search', 'readFile', 'editFiles', 'runInTerminal']
model: 'Claude Opus 4.6'
handoffs:
  - label: 'Security Review'
    agent: 'security-reviewer'
    prompt: 'Review the implemented code for security vulnerabilities.'
  - label: 'Write Tests'
    agent: 'test-writer'
    prompt: 'Write comprehensive tests for the new feature code.'
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

**Why this works:** The Feature Builder stays focused on implementation. When it's time for security review, tests, or PR creation, it hands off to specialized agents that have their own isolated context. The sub-agents don't inherit the full implementation context — they receive only the relevant prompt and can focus deeply on their specialty.

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

The recommended approach for creating custom agents is through VS Code's built-in interface combined with agent-assisted iteration.

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
> *- Use Claude Opus 4.6 for its reasoning capabilities*
> *- Have access to search, readFile, and usages tools*
> *- Include handoffs to an implementation agent after review*
>
> *Store the result in .github/agents/security-reviewer.agent.md*

This approach ensures:
- Proper YAML frontmatter syntax
- Consistent formatting
- Human-verifiable output that can be reviewed in PRs

### Anti-Patterns to Avoid

| Anti-Pattern | Why It's Problematic | Better Approach |
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

Specificity in persona definition produces consistency in outputs.

**Too Vague:**
```markdown
You are a helpful assistant for reviewing code.
```

**Appropriately Specific:**
```markdown
You are a principal engineer with 20 years of experience across 
startups and enterprise. You've seen what works and what becomes 
technical debt. You're kind but direct—you won't sugarcoat issues 
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
> *- Preferred Model: Claude Opus 4.6 (or specify another)*
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
model: 'Claude Opus 4.6'
---

You are a rubber duck. Your job is NOT to solve problems—it's to help 
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

**The Devil's Advocate** — Challenges every decision:

```markdown
---
name: "Devil's Advocate"
description: 'Challenges decisions to find weaknesses'
tools: ['search', 'readFile', 'fetch']
model: 'Claude Opus 4.6'
---

You argue the opposite position of whatever the user suggests.
Your job is to find holes in their reasoning.

## Your Approach
- "That's interesting, but have you considered..."
- "What happens when X fails?"
- "How would this scale to 10x the load?"
- "What would a skeptical stakeholder say?"

## Important
You're not being negative—you're being thorough.
After challenging, acknowledge good points.
End with "If you can address these, you've got a solid plan."
```

### Claude Agent Format

VS Code also detects `.md` files in the `.claude/agents` folder, following the Claude sub-agents format. This enables teams to use the same agent definitions across VS Code and Claude Code.

Claude agent files use plain `.md` files (not `.agent.md`) with slightly different frontmatter:

| Field | Description |
|-------|-------------|
| `name` | Agent name (required) |
| `description` | What the agent does |
| `tools` | Comma-separated string of allowed tools (e.g., `"Read, Grep, Glob, Bash"`) |
| `disallowedTools` | Comma-separated string of tools to block |

VS Code maps Claude-specific tool names to the corresponding VS Code tools. Both the VS Code `.agent.md` format (with YAML arrays for tools) and the Claude format (with comma-separated strings) are supported.

To create a Claude-compatible agent, select **Workspace (Claude format)** when creating a new custom agent via the Configure menu.

### Background and Cloud Agents

Custom agents can be reused in **background agents** and **cloud agents**, enabling autonomous tasks with the same specialized configurations defined in `.agent.md` files.

- **Background agents** run tasks asynchronously in VS Code while the developer continues working
- **Cloud agents** execute remotely on GitHub's infrastructure

Background agents also support slash commands — including prompt files, hooks, and skills. All customization primitives now work across local, background, and cloud agent environments.

This means agent definitions are portable: the same `.agent.md` file that drives an interactive chat session can also power automated coding tasks running in the background or in the cloud.

**See it in action:** [A Unified Agent Experience](https://www.youtube.com/watch?v=YmpjvZ3xkx8) — Josh Spicer demos managing local, background, and cloud agent sessions from a single view, including delegating tasks to remote infrastructure and collaborating through PRs. Also in the [livestream](https://www.youtube.com/watch?v=tAezuMSJuFs&t=4350s) at 01:12:30.

### Organization-Level Custom Agents

Custom agents can be shared across an entire GitHub organization, providing consistent specialized personas across all repositories.

**Setting:** `github.copilot.chat.organizationCustomAgents.enabled` — set to `true` to discover organization-level agents.

Organization-level agents appear in the agents dropdown alongside built-in agents, personal agents, and workspace agents. This is useful for:
- Standardizing review workflows across teams
- Providing org-wide security or compliance agents
- Sharing domain-specific expertise agents across repositories

Learn more about [creating custom agents for your organization](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents) in the GitHub documentation.

---

[← Skills](part-2-4-skills.md) | [Next: MCP →](part-2-6-mcp.md)
