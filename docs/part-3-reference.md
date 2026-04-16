# Part III: Reference

[← Back to Guide](../ReadMe.md) | [← Part II: The Primitives](part-2-primitives.md)

*Updated: April 16, 2026 · Validated against VS Code 1.116 and GitHub Copilot docs as of April 16, 2026.*

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
| Copilot Memory | Managed by GitHub | N/A — no repo file |
| Agentic Workflows | `.github/workflows/` | `.md` (workflow instructions) |
| Copilot SDK | External dependency (npm, pip, etc.) | N/A — installed via package managers |

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
| Memory | Automatically retrieved and validated at session start and during reasoning |

---

## Cross-Surface Primitive Support Matrix

Not every surface supports every primitive. This consolidated matrix shows current support across all Copilot surfaces:

| Primitive | VS Code | JetBrains | Visual Studio | Eclipse | Xcode | Copilot CLI | Cloud Coding Agent |
|-----------|---------|-----------|---------------|---------|-------|-------------|-------------------|
| Always-on Instructions | ✅ | Preview | ✅ | Preview | Preview | ✅ | ✅ |
| File-based Instructions | ✅ | Preview | — | — | — | ✅ | — |
| Prompts | ✅ | Preview | ✅ | — | Preview | — | — |
| Skills | ✅ | Preview | — | — | — | ✅ | — |
| Custom Agents | ✅ | Preview | Preview | ✅ | Preview | ✅ | — |
| MCP | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| Hooks | ✅ | — | — | — | — | ✅ | ✅ |
| Memory | ✅\* | ✅\* | ✅\* | — | — | ✅ | ✅ |

**Key:** ✅ = Generally available · Preview = Available but subject to change · — = Not yet supported · \* = Available via the Copilot cloud agent and code review, not in IDE Chat/Completions/Inline Chat

Features marked "Preview" may require enabling experimental settings. Consult the [Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix) for the latest status.

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
| `agent` | No | string | `ask`, `agent`, `plan`, or custom agent name |
| `description` | No | string | Brief description for `/` menu |
| `model` | No | string | AI model (e.g., `Claude Opus 4.7`, `GPT-5.4`) |
| `tools` | No | string[] | Restrict available tools |
| `argument-hint` | No | string | Hint text for user input |

```yaml
---
agent: 'agent'
description: 'Generate a new React component with tests'
model: 'Claude Opus 4.7'
tools: ['editFiles', 'createFile', 'runInTerminal']
---
```

#### Variable Syntax

Prompts support both built-in variables (`${file}`, `${selection}`, etc.) and input variables that prompt the user for a value:

| Syntax | Description |
|--------|-------------|
| `${file}`, `${selection}`, `${workspaceFolder}` | Built-in VS Code context variables |
| `${input:variableName}` | Prompts the user for a value when invoked |
| `${input:variableName:placeholder}` | Prompts the user, showing placeholder hint text |

```markdown
Create a component called `${input:componentName}` that:
- Handles ${input:primaryResponsibility}
- Returns ${input:returnShape}
```

Users are prompted for input variable values when invoking the prompt.

### Skills (SKILL.md)

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `name` | **Yes** | string | 1-64 chars, lowercase, hyphens only |
| `description` | **Yes** | string | 1-1024 chars, WHAT + WHEN to use |
| `argument-hint` | No | string | Hint text shown when invoked as `/` command |
| `user-invocable` | No | boolean | Show as `/` slash command (default: `true`) |
| `disable-model-invocation` | No | boolean | Require manual `/` invocation only (default: `false`) |
| `metadata` | No | object | Key-value pairs (author, version) |
| `license` | No | string | License name or reference |
| `compatibility` | No | string | Environment requirements |

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
| `model` | No | string or string[] | AI model to use. Supports arrays for fallback: `['Claude Sonnet 4.7 (copilot)', 'GPT-5 (copilot)']` |
| `handoffs` | No | object[] | Transitions to other agents |
| `argument-hint` | No | string | Hint text for user interaction |
| `user-invocable` | No | boolean | Whether the agent can be manually selected (default: `true`) |
| `disable-model-invocation` | No | boolean | Prevent automatic/subagent invocation (default: `false`); replaces retired `infer` field |
| `agents` | No | string[] | Restrict available subagents: names, `*`, or `[]` |
| `target` | No | string | Target environment: `vscode` or `github-copilot` |
| `mcp-servers` | No | object[] | MCP servers for `github-copilot` target |
| `hooks` | No | object | Agent-scoped hooks (Preview) |

```yaml
---
name: 'Security Reviewer'
description: 'Reviews code for security vulnerabilities'
tools: ['search', 'readFile', 'usages']
model: 'Claude Opus 4.7'
handoffs:
  - label: 'Fix Issues'
    agent: 'agent'
    prompt: 'Fix the security issues identified above.'
    send: false
    model: 'GPT-5.4 (copilot)'
---

---

## Execution Modes

| Mode | Copilot Can... | Best For |
|------|----------------|----------|
| `ask` | Respond conversationally (read-only) | Q&A, explanations, code review, brainstorming |
| `agent` | Create/edit files, run commands | Any task that modifies code |
| `plan` | Generate structured implementation plans | Breaking down tasks before implementation |
| Custom agent | Use that agent's persona and tools | Specialized workflows |

**Edit Mode Deprecation:** `edit` mode is officially deprecated as of VS Code 1.110. Users can temporarily re-enable it via the `chat.editMode.hidden` setting, but `edit` mode will be fully removed in VS Code 1.125. Use `agent` for all file modifications.

### Agent Permission Levels

| Level | Behavior | Best For |
|-------|----------|----------|
| Default | Prompts for approval on each action | Production work requiring oversight |
| Bypass Approvals | Skips low-risk confirmations automatically | Trusted workflows with repetitive actions |
| Autopilot (Preview) | Fully autonomous — no confirmations | Batch operations, CI-driven agent tasks |

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
| `**/*.{swift,m,mm}` | iOS / Objective-C sources |
| `**/*.{kt,kts}` | Kotlin sources and Gradle scripts |
| `**/*.{py,ipynb}` | Python and Jupyter notebooks |
| `**/*.{cs,csproj}` | C# and .NET project files |
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

### HTTP Server

```json
{
  "servers": {
    "remote-server": {
      "type": "http",
      "url": "https://example.com/mcp",
      "headers": { "Authorization": "Bearer ${env:TOKEN}" }
    },
    "sse-server": {
      "type": "sse",
      "url": "https://example.com/mcp/sse",
      "headers": { "Authorization": "Bearer ${env:TOKEN}" }
    }
  }
}
```

Use `http` for the newer streamable HTTP transport. Use `sse` for servers that expose Server-Sent Events.

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
| `type` | string | `stdio` or `http` |
| `command` | string | Executable (for stdio) |
| `args` | string[] | Command arguments |
| `env` | object | Environment variables |
| `cwd` | string | Working directory |
| `envFile` | string | Path to .env file |
| `url` | string | Server URL (for http) |
| `headers` | object | HTTP headers (for http) |
| `disabled` | boolean | Disable this server |
| `dev` | object | Development mode config with `watch` and `build` commands |

**Variable types in `env` values:**

| Syntax | Where | Description |
|--------|-------|-------------|
| `${env:VAR_NAME}` | Workspace / user MCP | Read from environment variable |
| `${env:VAR:-default}` | Workspace / user MCP | Environment variable with fallback |
| `${input:variableName}` | Workspace / user MCP | Prompt the user for a value at startup |
| `$VAR` / `${VAR}` | Cloud agent / custom-agent YAML | Environment variable (Claude Code syntax) |
| `${VAR:-default}` | Cloud agent / custom-agent YAML | Environment variable with fallback |
| `${{ secrets.NAME }}` | Cloud agent custom-agent YAML | Secret from the repository's `copilot` environment |
| `${{ vars.NAME }}` | Cloud agent custom-agent YAML | Variable from the repository's `copilot` environment |

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

For comprehensive documentation with practical examples, see [Primitive 7: Hooks](primitive-7-hooks.md).

### VS Code Hooks (Chat Agent Sessions)

VS Code 1.109.3+ supports hooks in Chat agent sessions via file-based configuration in `.github/hooks/*.json`. Eight PascalCase events are available: `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `PreCompact`, `SubagentStart`, `SubagentStop`, and `Stop`. See [Primitive 7: VS Code Hooks](primitive-7-hooks.md#vs-code-hooks-chat-agent-sessions) for configuration details.

---

## Context Window Guidelines

Every primitive consumes tokens. Keep them focused:

| Content Type | Recommended Size |
|--------------|------------------|
| Always-on instructions | 500-2000 words |
| File-based instructions | 200-500 words each |
| Prompt file | 100-500 words |
| Individual skill | 500-1500 words |
| Custom agent | 200-1000 words |

**Total active context:** Keep under 4000 words for optimal performance. If Copilot seems to "forget" rules, your instructions may be too long — move specialized content to file-based instructions or skills.

For codebase conventions that Copilot discovers through usage — patterns, constraints, and preferences that are hard to author manually — consider enabling [Copilot Memory (Preview)](primitive-8-memory.md). Memory is repository-scoped: anything stored is shared with all users who have Memory enabled in that repo.

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

## Quick Decision Guide

| Situation | Use This |
|-----------|----------|
| Rules that apply everywhere | Always-On Instructions |
| Rules for specific file types | File-Based Instructions |
| Reusable workflow or procedural knowledge | Skill |
| Specialized AI persona | Custom Agent |
| Simple single-purpose slash command | Prompt File |
| External API/database access | MCP Server |
| Rules + external access | Skill + MCP together |
| Block dangerous agent commands | Hook (`preToolUse`) |
| Audit all agent actions | Hooks (all types) |
| Runtime security enforcement | Hook (`preToolUse`) + Instructions |
| Codebase knowledge that persists across sessions | Memory |

---

## Debugging: What's Loaded?

### Chat Customization Diagnostics

VS Code 1.116 includes a dedicated diagnostics view for troubleshooting customization issues:

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
| No variables | Not reusable | Use `${input:variableName}` |
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
model: 'Claude Opus 4.7'
---

[Clear instruction]

**Input:** ${input:variable1}

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
model: 'Claude Opus 4.7'
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
| **CLI support** | ✅ | ✅ | ❌² | ✅ | ✅ | ✅ | ✅¹ |

¹ Hooks are only active during coding agent and Copilot CLI sessions, not in Chat/Completions/Inline.
² Prompt files (`.prompt.md`) are a VS Code feature. Copilot CLI uses natural language prompts and custom agents instead.

---

## Official Resources

| Resource | URL |
|----------|-----|
| GitHub Copilot Docs | https://docs.github.com/en/copilot |
| VS Code Copilot Docs | https://code.visualstudio.com/docs/copilot |
| GitHub Copilot CLI | https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli |
| MCP Specification | https://modelcontextprotocol.io |
| Agent Skills Spec | https://agentskills.io |
| Copilot Memory (concepts) | https://docs.github.com/en/copilot/concepts/agents/copilot-memory |
| Copilot Memory (managing) | https://docs.github.com/en/copilot/how-tos/use-copilot-agents/copilot-memory |
| GitHub Agentic Workflows | https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/ |
| Awesome Copilot | https://github.com/github/awesome-copilot |
| `gh skill` CLI (preview) | https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli |

---

## Implementation Roadmap

| Timeline | Action | Outcome |
|----------|--------|---------|
| Day 1 | Create `copilot-instructions.md` with 5 key rules | Immediate convention enforcement |
| Week 1 | Add 2-3 skills for repeated workflows (scaffolding, testing, deployments) | Portable task automation across VS Code, CLI, and coding agent |
| Week 2 | Create 1-2 custom agents (code reviewer, architect) | Role-based AI assistance |
| Month 1 | Evaluate MCP servers and Hooks | External integrations, runtime enforcement |
| Ongoing | Add prompt files for simple single-purpose slash commands as needed | Quick task shortcuts |

---

[← Part II: The Primitives](part-2-primitives.md) | [Back to Guide →](../ReadMe.md)
