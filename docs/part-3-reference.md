# Part III: Reference

[← Back to Guide](../ReadMe.md) | [← Part II: The Primitives](part-2-primitives.md)

---

## Quick Reference: File Locations

| Primitive | Location | File Extension |
|-----------|----------|----------------|
| Always-On Instructions | `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md` | `.md` (specific name) |
| File-Based Instructions | `.github/instructions/` | `.instructions.md` |
| Prompts | `.github/prompts/` | `.prompt.md` |
| Skills | `.github/skills/*/` | `SKILL.md` |
| Custom Agents | `.github/agents/` OR anywhere | `.agent.md` or any `.md` in agents/ |
| MCP Servers | `.vscode/mcp.json` | `.json` |
| Hooks | `.github/hooks/` | `.json` |

---

## Frontmatter Reference

### Always-On Instructions

No frontmatter required. Plain markdown file.

```markdown
# Copilot Instructions for [Project Name]

## Tech Stack
...
```

### File-Based Instructions

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `applyTo` | **Yes** | string | Glob pattern for automatic activation |
| `name` | No | string | Display name (defaults to filename) |
| `description` | No | string | Description shown on hover |
| `excludeAgent` | No | string[] | Agents to exclude from these instructions |

```yaml
---
name: 'React Components'
description: 'Conventions for React component development'
applyTo: 'src/components/**/*.tsx'
---
```

### Prompt Files

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `agent` | No | string | `ask`, `plan`, `agent`, or custom agent name |
| `description` | No | string | Brief description for `/` menu |
| `model` | No | string | AI model (e.g., `Claude Opus 4.6`, `GPT-5.2`) |
| `tools` | No | string[] | Restrict available tools |
| `argument-hint` | No | string | Hint text for user input |

```yaml
---
agent: 'agent'
description: 'Generate a new React component with tests'
model: 'Claude Opus 4.6'
tools: ['editFiles', 'createFile', 'runInTerminal']
---
```

### Skills (SKILL.md)

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `name` | **Yes** | string | 1-64 chars, lowercase, hyphens only |
| `description` | **Yes** | string | 1-1024 chars, WHAT + WHEN to use |
| `metadata` | No | object | Key-value pairs (author, version) |
| `license` | No | string | License name or reference |
| `compatibility` | No | object | Environment requirements |
| `user-invokable` | No | boolean | Whether the skill appears as a `/` slash command (default: `true`) |
| `disable-model-invocation` | No | boolean | Prevents automatic activation by the agent (default: `false`). Requires manual `/` invocation |
| `argument-hint` | No | string | Hint text shown to users when invoking the skill as a `/` slash command |

```yaml
---
name: image-manipulation
description: Resize, convert, compress images using ImageMagick. Use when the user mentions image optimization or format conversion.
metadata:
  author: your-org
  version: "1.0"
---
```

**Name Validation Rules:**
- ✅ `image-manipulation`, `github-issues`, `web-testing`
- ❌ `Image-Manipulation` (no uppercase)
- ❌ `-image` or `image-` (no leading/trailing hyphens)
- ❌ `image--manipulation` (no consecutive hyphens)

### Custom Agents

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `name` | No | string | Display name in agent picker |
| `description` | No | string | Placeholder text in chat input |
| `tools` | No | string[] | Available tools for this agent |
| `model` | No | string or string[] | AI model to use. Supports arrays for fallback: `['Claude Sonnet 4.5 (copilot)', 'GPT-5 (copilot)']` |
| `handoffs` | No | object[] | Transitions to other agents |
| `argument-hint` | No | string | Hint text for user interaction |
| `user-invokable` | No | boolean | Whether agent appears in the agents dropdown (default: `true`). Set to `false` for subagent-only agents |
| `disable-model-invocation` | No | boolean | Prevents the agent from being invoked as a subagent (default: `false`). Set to `true` for user-only agents |
| `agents` | No | string[] | Restrict which subagents this agent can invoke. Accepts names, `*` (all), or `[]` (none) |

```yaml
---
name: 'Security Reviewer'
description: 'Reviews code for security vulnerabilities'
tools: ['search', 'readFile', 'usages']
model: 'Claude Opus 4.6'
handoffs:
  - label: 'Fix Issues'
    agent: 'agent'
    prompt: 'Fix the security issues identified above.'
---
```

---

## Execution Modes

| Mode | Copilot Can... | Best For |
|------|----------------|----------|
| `ask` | Respond conversationally (read-only) | Q&A, explanations, code review, brainstorming |
| `agent` | Create/edit files, run commands | Any task that modifies code |
| Custom agent | Use that agent's persona and tools | Specialized workflows |

**Note:** `plan` mode exists but is not recommended. Use `agent` for any file modifications.

---

## Available Tools

| Tool | Description |
|------|-------------|
| `search` | Search codebase |
| `readFile` | Read file contents |
| `editFiles` | Modify existing files |
| `createFile` | Create new files |
| `usages` | Find symbol usages |
| `terminalCommand` | Run terminal commands (alias: `runInTerminal`) |
| `fetch` | HTTP requests |
| `githubRepo` | GitHub API access |
| `getChangedFiles` | Get PR/branch changes |
| `terminalLastCommand` | Get last terminal command |
| `getTerminalOutput` | Get terminal output |

---

## Glob Pattern Reference

| Pattern | Matches |
|---------|---------|
| `*` | All files in current directory |
| `**` | All files in all directories |
| `*.ts` | All .ts files in current directory |
| `**/*.ts` | All .ts files recursively |
| `src/**/*.ts` | All .ts files under src/ |
| `**/*.{ts,tsx}` | All .ts and .tsx files |
| `**/tests/**` | All files in any tests/ directory |
| `src/components/**/*` | All files under src/components/ |
| `!**/node_modules/**` | Exclude node_modules |

---

## MCP Configuration

### Workspace Config (`.vscode/mcp.json`)

```json
{
  "servers": {
    "server-name": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@package/mcp-server"],
      "env": {
        "API_TOKEN": "${env:API_TOKEN}"
      }
    }
  }
}
```

### HTTP/SSE/Streamable Server

```json
{
  "servers": {
    "remote-server": {
      "type": "sse",
      "url": "https://example.com/mcp",
      "headers": { "Authorization": "Bearer ${env:TOKEN}" }
    },
    "streamable-server": {
      "type": "http",
      "url": "https://example.com/mcp",
      "headers": { "Authorization": "Bearer ${env:TOKEN}" }
    }
  }
}
```

Use `sse` for Server-Sent Events transport. Use `http` for the newer streamable HTTP transport.

### Disabling a Server

```json
{
  "servers": {
    "github": { ... },
    "azure": { "disabled": true }
  }
}
```

### MCP Configuration Fields

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | `stdio`, `sse`, or `http` |
| `command` | string | Executable (for stdio) |
| `args` | string[] | Command arguments |
| `env` | object | Environment variables |
| `cwd` | string | Working directory |
| `envFile` | string | Path to .env file |
| `url` | string | Server URL (for sse/http) |
| `headers` | object | HTTP headers (for sse/http) |
| `disabled` | boolean | Disable this server |
| `dev` | object | Development mode config with `watch` and `build` commands |

**Variable types in `env` values:**

| Syntax | Description |
|--------|-------------|
| `${env:VAR_NAME}` | Read from environment variable |
| `${input:variableName}` | Prompt the user for a value at startup |

### Tool Count Guidance

**Aim for fewer than 70 total tools across all MCP servers.**

- Each tool consumes context (name, description, schema)
- More tools = slower selection, less accurate invocation
- Only run servers you actively need

---

## Hooks Configuration (Preview)

### Hook File Format

Hook configuration files live in `.github/hooks/` and require `version: 1`:

```json
{
  "version": 1,
  "hooks": {
    "sessionStart": [...],
    "sessionEnd": [...],
    "userPromptSubmitted": [...],
    "preToolUse": [...],
    "postToolUse": [...],
    "errorOccurred": [...]
  }
}
```

### Hook Object Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `type` | Yes | string | Must be `"command"` |
| `bash` | Yes (Unix) | string | Shell command or path to script |
| `powershell` | Yes (Windows) | string | PowerShell command or path to script |
| `cwd` | No | string | Working directory (relative to repo root) |
| `env` | No | object | Environment variables |
| `timeoutSec` | No | number | Max execution time in seconds (default: 30) |
| `comment` | No | string | Human-readable description |

### Hook Types Quick Reference

| Hook | Input Fields | Output | Can Block? |
|------|-------------|--------|------------|
| `sessionStart` | `timestamp`, `cwd`, `source`, `initialPrompt` | Ignored | No |
| `sessionEnd` | `timestamp`, `cwd`, `reason` | Ignored | No |
| `userPromptSubmitted` | `timestamp`, `cwd`, `prompt` | Ignored | No |
| `preToolUse` | `timestamp`, `cwd`, `toolName`, `toolArgs` | `permissionDecision` + `permissionDecisionReason` | **Yes** |
| `postToolUse` | `timestamp`, `cwd`, `toolName`, `toolArgs`, `toolResult` | Ignored | No |
| `errorOccurred` | `timestamp`, `cwd`, `error` | Ignored | No |

For comprehensive documentation with practical examples, see [Part 2.7: Hooks](part-2-7-hooks.md).

### VS Code Hooks (Chat Agent Sessions)

VS Code 1.109.3+ supports hooks in Chat agent sessions via file-based configuration in `.github/hooks/*.json`. Eight PascalCase events are available: `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `PreCompact`, `SubagentStart`, `SubagentStop`, and `Stop`. See [Part 2.7: VS Code Hooks](part-2-7-hooks.md#vs-code-hooks-chat-agent-sessions) for configuration details.

---

## Context Window Guidelines

| Content Type | Recommended Size |
|--------------|------------------|
| Always-on instructions | 500-2000 words |
| File-based instructions | 200-500 words |
| Individual skill | 500-1500 words |
| Prompt file | 100-500 words |
| Custom agent | 200-1000 words |

**Total active context:** Keep under 4000 words for optimal performance.

---

## Copilot Memory (Preview)

Copilot Memory stores and recalls important information across chat sessions, eliminating the need to re-state preferences every time a new conversation starts. Think of it as a personal notebook that the agent reads before responding — except the notebook updates itself.

**Setting:** `github.copilot.chat.copilotMemory.enabled` — set to `true` to enable the memory tool.

When enabled, the agent gains access to a memory tool that recognizes when to store information and when to retrieve it. Telling the agent "always ask clarifying questions before refactoring" saves that preference as a memory. In future sessions — even in different workspaces — the agent recalls that preference automatically.

| Aspect | Details |
|--------|--------|
| **What it stores** | User preferences, project conventions, decisions, workflow patterns |
| **Scope** | Tied to the user's GitHub account — persists across workspaces and sessions |
| **Storage & retrieval** | The agent reads and writes memories during chat; no manual file editing required |
| **Management** | View and delete memories from [GitHub's Copilot settings](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/copilot-memory) |
| **Official docs** | [VS Code 1.109 release notes](https://code.visualstudio.com/updates/v1_109#_copilot-memory-preview) |

### Good vs. Bad Memory Usage

| | Example | Why |
|-|---------|-----|
| ✅ | "I prefer named exports over default exports" | Clear personal preference the agent can act on consistently |
| ✅ | "When I ask for tests, use Vitest with `describe`/`it` blocks" | Specific, actionable convention |
| ✅ | "My team's API base path is `/api/v2`" | Factual context that reduces repeated corrections |
| ❌ | Storing an entire style guide in memory | Too large — use always-on instructions or file-based instructions instead |
| ❌ | "Write good code" | Too vague to influence behavior |
| ❌ | Project-specific architecture decisions the whole team needs | Team knowledge belongs in customization files, not personal memory |

### Memory vs. Customization Primitives

Copilot Memory is **complementary** to repository customization — not a replacement for any primitive.

| Layer | Scope | Audience | Lives In |
|-------|-------|----------|----------|
| Customization files (instructions, skills, agents) | Repository | Everyone on the team | `.github/` |
| Copilot Memory | GitHub account | Individual developer | GitHub's cloud storage |

The rule of thumb: if a convention applies to the whole team, encode it in customization files. If it applies to one developer's workflow preferences, let Memory handle it.

---

## Terminal Sandboxing (Experimental)

Terminal sandboxing restricts file system and network access for commands executed by agents, reducing the risk of unintended modifications outside the workspace.

**Setting:** `chat.tools.terminal.sandbox.enabled` — set to `true` to enable sandboxing.

| Restriction | Default Behavior |
|-------------|------------------|
| **File system** | Read/write access limited to the current working directory |
| **Network** | All domains blocked by default |
| **Confirmation** | Commands run without the standard confirmation dialog |

Configure allowed file system paths and network domains via `chat.tools.terminal.sandbox.linuxFileSystem`, `chat.tools.terminal.sandbox.macFileSystem`, and `chat.tools.terminal.sandbox.network`.

**Note:** Terminal sandboxing is currently supported on macOS and Linux only. On Windows, the sandbox settings have no effect.

---

## When Primitives Load

| Primitive | Loads When |
|-----------|------------|
| Always-On Instructions | Session start (always) |
| File-Based Instructions | File matches `applyTo` pattern |
| Prompts | User invokes with `/` |
| Skills | Description matches user request |
| Custom Agents | User selects or handoff triggers |
| MCP Servers | Session start (if configured) |
| Hooks | During coding agent, CLI, and VS Code Chat sessions (on lifecycle events) |

---

## Quick Decision Guide

| Situation | Use This |
|-----------|----------|
| Rules that apply everywhere | Always-On Instructions |
| Rules for specific file types | File-Based Instructions |
| Repeatable task template | Prompt File |
| Reusable capability with resources | Skill |
| Specialized AI persona | Custom Agent |
| External API/database access | MCP Server |
| Rules + external access | Skill + MCP together |
| Block dangerous agent commands | Hook (`preToolUse`) |
| Audit all agent actions | Hooks (all types) |
| Runtime security enforcement | Hook (`preToolUse`) + Instructions |

---

## Debugging: What's Loaded?

### Chat Customization Diagnostics

VS Code 1.109 includes a dedicated diagnostics view for troubleshooting customization issues:

1. Right-click in the Chat view
2. Select **Diagnostics**
3. Review the Markdown document listing all active customization files

The diagnostics view shows:
- All loaded custom agents, prompt files, instruction files, and skills
- Load status for each file
- Any errors that occurred during loading

This is the fastest way to determine why a customization file isn't being applied or is causing unexpected behavior.

### Manual Debugging

> 💬 **Try this prompt:** "What instructions, skills, and tools are currently active?"

> 💬 **Try this prompt:** "Are you seeing the React component guidelines?"

> 💬 **Try this prompt:** "I expected X but got Y. What rules are you following?"

### Verify File Locations

- Always-on: `.github/copilot-instructions.md` (exact name)
- File-based: `.github/instructions/*.instructions.md`
- Prompts: `.github/prompts/*.prompt.md`
- Skills: `.github/skills/*/SKILL.md`
- Agents: `.github/agents/*.md` or `**/*.agent.md`
- MCP: `.vscode/mcp.json`
- Hooks: `.github/hooks/*.json`

---

## Anti-Patterns to Avoid

### Instructions
| Don't | Why | Do Instead |
|-------|-----|------------|
| Write by hand | Errors, missed patterns | Have agent generate from codebase |
| Copy from other repos | Wrong conventions | Generate per-repo |
| Over 2000 words | Dilutes important rules | Split to file-based |
| No rationale | Poor edge-case handling | Include "why" |
| Never update | Drift from practice | Treat as code, PR changes |

### Prompts
| Don't | Why | Do Instead |
|-------|-----|------------|
| Vague instructions | Inconsistent results | Be specific |
| No variables | Not reusable | Use `${variableName}` |
| Use `plan` mode | Less reliable | Use `agent` mode |
| No model specified | Inconsistent | Specify model |

### Skills
| Don't | Why | Do Instead |
|-------|-----|------------|
| Uppercase in name | Validation fails | Lowercase with hyphens |
| Weak description | Won't activate | Include WHAT + WHEN + keywords |
| Generic content | Low value | Domain-specific knowledge |

### MCP
| Don't | Why | Do Instead |
|-------|-----|------------|
| 100+ tools | Slow, inaccurate | Under 70 tools |
| All servers always on | Wasted context | Disable unused servers |
| Hardcoded secrets | Security risk | Use `${env:VAR}` |

### Hooks
| Don't | Why | Do Instead |
|-------|-----|------------|
| Use hooks *instead* of instructions | Hooks can only deny; they can't guide code generation | Use instructions for guidance, hooks for enforcement |
| Slow synchronous network calls | Blocks agent execution for every tool call | Fire-and-forget (`curl ... &`) or batch at session end |
| Log secrets in audit trails | Logs may be persisted or shared | Filter sensitive fields before writing |
| Overly broad deny rules | Agent becomes ineffective | Be precise in pattern matching; test against real workflows |
| Only provide `bash` scripts | Hooks fail silently on Windows | Always include both `bash` and `powershell` variants |
| Skip `timeoutSec` | Default 30s may be too long or too short | Set timeout appropriate to each hook's operation |

---

## Starter Templates

### copilot-instructions.md

```markdown
# Copilot Instructions for [Project Name]

## Project Overview
[One paragraph description]

## Tech Stack
- [Primary language/framework]
- [Database]
- [Key libraries]

## Code Style
- [Rule 1]
- [Rule 2]
- [Rule 3]

## Architecture
[Brief description]

## Testing
- [Testing framework]
- [Where tests live]

## What NOT to Do
- Don't [anti-pattern 1]
- Don't [anti-pattern 2]
```

### File-Based Instruction

```markdown
---
name: 'API Routes'
description: 'Conventions for REST API endpoints'
applyTo: 'src/api/**/*'
---

# API Route Guidelines

## Response Format
[Standard format]

## Error Handling
[Error patterns]

## Authentication
[Auth requirements]
```

### Prompt File

```markdown
---
agent: 'agent'
description: 'Brief description'
model: 'Claude Opus 4.6'
---

[Clear instruction]

**Input:** ${variable1}

## Requirements
1. [Requirement 1]
2. [Requirement 2]

## Output Format
[Expected output]
```

### SKILL.md

```markdown
---
name: skill-name
description: What this does and when to use it. Use when user mentions [keywords].
metadata:
  author: your-org
  version: "1.0"
---

# Skill Name

## When to Use
- [Trigger 1]
- [Trigger 2]

## Instructions
[Step-by-step guidance]

## Examples
[Practical examples]
```

### Custom Agent

```markdown
---
name: 'Agent Name'
description: 'What this agent does'
tools: ['search', 'readFile']
model: 'Claude Opus 4.6'
---

You are [persona description].

## Your Expertise
- [Area 1]
- [Area 2]

## How You Respond
- [Style 1]
- [Style 2]

## What You Never Do
- [Guardrail 1]
- [Guardrail 2]
```

### MCP Configuration

```json
{
  "servers": {
    "server-name": {
      "type": "stdio",
      "command": "npx",
      "args": ["@package/mcp-server"],
      "env": {
        "API_TOKEN": "${env:API_TOKEN}"
      }
    }
  }
}
```

### Hooks Configuration (Preview)

```json
{
  "version": 1,
  "hooks": {
    "preToolUse": [
      {
        "type": "command",
        "bash": "./scripts/hooks/security-check.sh",
        "powershell": "./scripts/hooks/security-check.ps1",
        "cwd": ".",
        "timeoutSec": 10,
        "comment": "[Describe what this hook enforces]"
      }
    ],
    "postToolUse": [
      {
        "type": "command",
        "bash": "./scripts/hooks/audit-log.sh",
        "powershell": "./scripts/hooks/audit-log.ps1",
        "comment": "[Describe what this hook logs]"
      }
    ]
  }
}
```

---

## Primitive Comparison

| | Instructions | File-Based | Prompts | Skills | Agents | MCP | Hooks |
|-|--------------|------------|---------|--------|--------|-----|-------|
| **Always loaded** | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌¹ |
| **User invokes** | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ |
| **Auto-activates** | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅¹ |
| **Has frontmatter** | ❌ | ✅ | ✅ | ✅ | ✅ | N/A | N/A |
| **Can include files** | ❌ | ❌ | ❌ | ✅ | ❌ | N/A | N/A |
| **External access** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| **Portable** | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |
| **Can block actions** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Visible to LLM** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |

¹ Hooks are active during coding agent, Copilot CLI, and VS Code Chat agent sessions (1.109.3+), not in inline completions.

---

## Variable Syntax

Prompts support variables with `${variableName}`:

```markdown
Create a component called `${componentName}` that:
- Handles ${primaryResponsibility}
- Returns ${returnShape}
```

Users are prompted for values when invoking.

---

## Handoffs (Custom Agents)

```yaml
handoffs:
  - label: 'Start Implementation'
    agent: 'agent'
    prompt: 'Implement the design above.'
  - label: 'Write Tests'
    agent: '@workspace'
    prompt: 'Write tests for this code.'
```

---

## Environment Variables in MCP

Reference environment variables with `${env:VAR_NAME}`:

```json
{
  "env": {
    "API_KEY": "${env:MY_API_KEY}",
    "DATABASE_URL": "${env:DATABASE_URL}"
  }
}
```

---

## Official Resources

| Resource | URL |
|----------|-----|
| GitHub Copilot Docs | https://docs.github.com/en/copilot |
| VS Code Copilot Docs | https://code.visualstudio.com/docs/copilot |
| MCP Specification | https://modelcontextprotocol.io |
| Agent Skills Spec | https://agentskills.io |
| Awesome Copilot | https://github.com/github/awesome-copilot |

---

## Implementation Roadmap

| Timeline | Action | Outcome |
|----------|--------|---------|
| Day 1 | Create `copilot-instructions.md` with 5 key rules | Immediate convention enforcement |
| Week 1 | Add 2-3 prompt files for repeated tasks | Consistent task automation |
| Month 1 | Implement custom agents for specialized workflows | Role-based AI assistance |
| Quarter 1 | Evaluate MCP servers, Skills, and Hooks | External integrations, portable capabilities, runtime enforcement |

---

[← Part II: The Primitives](part-2-primitives.md) | [Back to Guide →](../ReadMe.md)
