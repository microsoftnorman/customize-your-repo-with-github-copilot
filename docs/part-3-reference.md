# Part III: Reference

[← Back to Guide](../ReadMe.md) | [← Part II: The Primitives](part-2-primitives.md)

*Updated: April 22, 2026 · Validated against VS Code 1.117 and GitHub Copilot docs as of April 22, 2026.*

---

This chapter is the lookup layer for the rest of the guide. Use it when the main question is no longer "why does this matter?" or "which chapter should I read next?" and has become "which file, field, scope, or support boundary applies here?"

If this still feels new, stop here and read [Part I: Foundations](part-1-foundations.md) and [Part II: The Primitives](part-2-primitives.md) first. This chapter is a cheat sheet, not a first tutorial.

Start with the [Quick Decision Guide](#quick-decision-guide) when the problem is still fuzzy. Use the tables below when you already know the primitive and need the exact location, load timing, frontmatter, or surface support detail.

---

## Quick Reference: File Locations

| Primitive | Plain-English use | Location | File Extension |
|-----------|-------------------|----------|----------------|
| Always-On Instructions | Rules that should apply everywhere in the repo | `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md` | `.md` (specific name) |
| File-Based Instructions | Extra rules for only some files or folders | `.github/instructions/` | `.instructions.md` |
| Prompts | Reusable slash commands for repeat tasks | `.github/prompts/` | `.prompt.md` |
| Skills | Multi-step know-how the agent can discover and reuse | `.github/skills/*/` | `SKILL.md` |
| Custom Agents | Named personas with different tools and behavior | `.github/agents/` OR anywhere | `.agent.md` or any `.md` in agents/ |
| MCP Servers | External tools and data sources | `.vscode/mcp.json` | `.json` |
| Hooks | Runtime checks and enforcement around agent actions | `.github/hooks/` | `.json` |
| Copilot Memory | Repository knowledge GitHub learns over time | Managed by GitHub | N/A: no repo file |
| Agentic Workflows | Continuous AI tasks in GitHub Actions | `.github/workflows/` | `.md` (workflow instructions) |
| Copilot SDK | Embed the runtime in another application | External dependency (npm, pip, etc.) | N/A: installed via package managers |

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

This is the **canonical primitive-by-surface matrix for this guide**. The [IDE Surfaces overview](surfaces.md) and each per-surface page link back here rather than duplicating it. For the current state, check the [Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix). The snapshot below was validated April 2026.

| Primitive | VS Code | JetBrains | Visual Studio 2026 | Eclipse | Xcode | Copilot CLI | Cloud Coding Agent |
|-----------|---------|-----------|--------------------|---------|-------|-------------|-------------------|
| Always-on Instructions | ✅ | Preview | ✅ | Preview | Preview | ✅ | ✅ |
| File-based Instructions | ✅ | Preview | ✅ | — | — | ✅ | ✅ |
| Prompts | ✅ | Preview | ✅ (18.4+) | — | Preview | — | — |
| Skills | ✅ | Preview | — | — | — | ✅ | ✅ |
| Custom Agents | ✅ | Preview | Preview (18.4+) | ✅ | Preview | ✅ | ✅ |
| MCP | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Hooks | ✅ | — | — | — | — | ✅ | ✅ |
| Memory | — | — | — | — | — | ✅ | ✅ |
| Agent plugins | ✅ | — | — | — | — | ✅ | — |

**Key:** ✅ = Generally available · Preview = Available but behavior may change · — = Not supported

**Memory note:** Copilot Memory currently applies in GitHub Copilot CLI, the Copilot cloud agent, and GitHub Copilot code review on GitHub. It is not currently used by VS Code Chat, Inline Chat, or the IDE-specific chat surfaces covered in this matrix.

Features marked "Preview" may require enabling experimental settings. Visual Studio minimum versions (18.4+, 18.4.1+) refer to Visual Studio 2026.

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

**Official docs:** [Agent Skills specification](https://agentskills.io)

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

**Official docs:** [Custom agents configuration reference](https://docs.github.com/en/copilot/reference/custom-agents-configuration)

For the runtime mental model behind delegated work, pair this reference with [The Agent Loop](agent-loop.md). For the clearest subagent explanation from the VS Code team, use [VS Code Insiders Podcast Episode 19: Subagents: Parallel Execution and Context Isolation](https://www.vscodepodcast.com/19). The repo also keeps the local transcript at [../references/transcripts/vscode-podcast/2026-02-09-subagents-parallel-execution-and-context-isolation-updated.md](../references/transcripts/vscode-podcast/2026-02-09-subagents-parallel-execution-and-context-isolation-updated.md).

**Also watch:** [Subagents: Parallel Execution and Context Isolation](https://www.youtube.com/watch?v=GMAoTeD9siU&t=0s) — Harald Kirschner explains context isolation and parallel delegation on the official VS Code channel.

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

### Subagents Quick Notes

Subagents are delegated agent loops with isolated context, not just extra prompts inside the same conversation. The main agent passes a focused task to the subagent, the subagent gathers its own evidence, and only the summarized result comes back. That is why the `agents`, `user-invocable`, and `disable-model-invocation` fields matter: they control which agents can be delegated, whether they appear in the picker, and whether they can be invoked automatically as subagents.

When documenting or debugging subagent behavior, start with these resources in order:

- [Subagents in Visual Studio Code](https://code.visualstudio.com/docs/copilot/agents/subagents)
- [The Agent Loop](agent-loop.md)
- [VS Code Insiders Podcast Episode 19](https://www.vscodepodcast.com/19)
- [Subagents: Parallel Execution and Context Isolation](https://www.youtube.com/watch?v=GMAoTeD9siU&t=0s)

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
```

---

## Execution Modes

| Mode | Copilot Can... | Best For |
|------|----------------|----------|
| `ask` | Respond conversationally (read-only) | Q&A, explanations, code review, brainstorming |
| `agent` | Create/edit files, run commands | Any task that modifies code |
| `plan` | Generate structured implementation plans | Breaking down tasks before implementation |
| Custom agent | Use that agent's persona and tools | Specialized workflows |

**Edit Mode Deprecation:** `edit` mode is deprecated as of VS Code 1.110. Users can temporarily re-enable it via the `chat.editMode.hidden` setting, but `edit` mode will be fully removed in VS Code 1.125. Use `agent` for all file modifications.

### Agent Permission Levels

| Level | Behavior | Best For |
|-------|----------|----------|
| Default | Prompts for approval on each action | Production work requiring oversight |
| Bypass Approvals | Skips low-risk confirmations automatically | Trusted workflows with repetitive actions |
| Autopilot (Preview) | Fully autonomous, no confirmations | Batch operations, CI-driven agent tasks |

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

**Official docs:** [MCP configuration reference](https://code.visualstudio.com/docs/copilot/reference/mcp-configuration) · [Add and manage MCP servers in VS Code](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) · [Model Context Protocol specification](https://modelcontextprotocol.io)

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

### Enable or Disable a Server

VS Code stores a server's enabled or disabled state separately from `mcp.json`. Disable a server from the **Extensions** view, **MCP: List Servers**, or the **Chat Customizations editor**. The shared `mcp.json` file keeps only the server definition.

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
| `sandboxEnabled` | boolean | Run a local stdio server in the VS Code sandbox (macOS and Linux only) |
| `sandbox` | object | File system and network rules for a sandboxed stdio server |
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

**Official docs:** [Agent hooks in Visual Studio Code](https://code.visualstudio.com/docs/copilot/customization/hooks)

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

For full documentation with practical examples, see [Primitive 7: Hooks](primitive-7-hooks.md).

### VS Code Hooks (Chat Agent Sessions)

VS Code 1.109.3+ supports hooks in Chat agent sessions via file-based configuration in `.github/hooks/*.json`. Eight PascalCase events are available: `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `PreCompact`, `SubagentStart`, `SubagentStop`, and `Stop`. See [Primitive 7: VS Code Hooks](primitive-7-hooks.md#vs-code-hooks-chat-agent-sessions) for configuration details.

---

## Context Window Guidelines

Every primitive consumes tokens. Target sizes:

| Content Type | Recommended Size |
|--------------|------------------|
| Always-on instructions | 500-2000 words |
| File-based instructions | 200-500 words each |
| Prompt file | 100-500 words |
| Individual skill | 500-1500 words |
| Custom agent | 200-1000 words |

**Total active context:** Keep under 4000 words. If Copilot seems to "forget" rules, your instructions may be too long. Move specialized content to file-based instructions or skills.

For codebase conventions that Copilot discovers through usage (patterns, constraints, and preferences that are hard to author manually), consider enabling [Copilot Memory (Preview)](primitive-8-memory.md). Memory is repository-scoped: anything stored is shared with all users who have Memory enabled in that repo.

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

VS Code 1.116 includes a diagnostics view for inspecting active customization files:

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

¹ Hooks are active during coding agent, Copilot CLI, and VS Code Chat agent sessions, not in inline completions.
² Prompt files (`.prompt.md`) are a VS Code feature. Copilot CLI uses natural language prompts and custom agents instead.

---

## Official Resources

| Resource | URL |
|----------|-----|
| GitHub Copilot Docs | https://docs.github.com/en/copilot |
| VS Code Copilot Docs | https://code.visualstudio.com/docs/copilot |
| VS Code Source Code | https://github.com/microsoft/vscode |
| VS Code Copilot Chat Source | https://github.com/microsoft/vscode-copilot-chat |
| GitHub Copilot CLI | https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli |
| GitHub Copilot CLI Repository | https://github.com/github/copilot-cli |
| GitHub Copilot SDK Repository | https://github.com/github/copilot-sdk |
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
