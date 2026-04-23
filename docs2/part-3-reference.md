# Operational Reference

[← Back to Guide](README.md) | [← Measuring Success](measuring-success.md)

*Updated: April 22, 2026.*

---

This is the lookup layer. The narrative chapters explain why the system works the way it does. This chapter answers the smaller operational questions: which file, which field, which scope, which surface, and what does a safe starting point look like?

Use it in this order:

- Start with [Start Here](#start-here) if the problem is still fuzzy.
- Use [Runtime Boundaries](#runtime-boundaries) when support or locality is the source of confusion.
- Use [Which Primitive Should You Use?](#which-primitive-should-you-use) when the mechanism is the decision.
- Use the later tables only when the primitive is already known and the question is purely operational.

---

## Start Here

| If the team is trying to... | Start with | Then verify by... |
|-----------------------------|------------|-------------------|
| Teach GitHub Copilot the repo's default rules | Always-on Instructions | Asking the agent which repo rules it is following |
| Add path-specific guidance | File-based Instructions | Opening a matching file and asking which scoped instructions loaded |
| Package a repeated workflow | Prompt file or Skill | Running the command once and checking whether the output matches the expected shape |
| Connect live systems | MCP | Listing the server, confirming trust, and using one narrow tool call |
| Enforce or audit runtime behavior | Hooks | Triggering one safe event and checking hook output or logs |
| Decide what will work in a specific IDE | The relevant surface page | Testing the smallest supported primitive on that surface before standardizing it |

## Runtime Boundaries

Most support confusion starts here.

- `Local workstation` means the editor or CLI running on the developer's own machine.
- `Remote workspace` means the agent is attached to a dev container, SSH host, WSL instance, or Codespace. In that case, "local" means local to that remote environment, not the laptop.
- `GitHub-hosted runtime` means the work runs in GitHub's Cloud Coding Agent environment. It cannot call a process running only on a developer workstation.

This matters most for [MCP](primitive-6-mcp.md) and [Hooks](primitive-7-hooks.md), because both depend on where code executes, which secrets are available, and which runtime the team actually trusts.

---

## Which Primitive Should You Use?

| Situation | Use This |
|-----------|----------|
| Rules that apply everywhere | Always-on Instructions |
| Rules for specific file types or paths | File-based Instructions |
| Reusable procedural knowledge | Skill |
| Specialized AI persona or role | Custom Agent |
| Simple single-purpose slash command | Prompt File |
| External API, database, or service access | MCP Server |
| Block dangerous agent commands at runtime | Hook (`PreToolUse`) |
| Audit all agent actions | Hooks (all lifecycle events) |
| Runtime security enforcement | Hook + Instructions together |
| Codebase knowledge that persists across sessions | Memory |

---

## File Locations

| Primitive | Location | File Extension |
|-----------|----------|----------------|
| Always-on Instructions | `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md` | `.md` (specific name) |
| File-based Instructions | `.github/instructions/` | `.instructions.md` |
| Prompts | `.github/prompts/` | `.prompt.md` |
| Skills | `.github/skills/*/` | `SKILL.md` |
| Custom Agents | `.github/agents/` or anywhere | `.agent.md` or any `.md` in agents/ |
| MCP Servers | `.vscode/mcp.json` | `.json` |
| Hooks | `.github/hooks/` | `.json` |
| Memory | Managed by GitHub | N/A: no repo file |
| Agentic Workflows | `.github/workflows/` | `.md` (workflow instructions) |
| Copilot SDK | External dependency (npm, pip, etc.) | N/A: installed via package managers |

---

## Load Order

This table answers the most common debugging question: "Why did my rule not apply?" The answer is almost always timing.

| Primitive | Loads When |
|-----------|------------|
| Always-on Instructions | Session start (always) |
| File-based Instructions | File matches `applyTo` pattern |
| Prompts | User invokes with `/` |
| Skills | Description matches user request |
| Custom Agents | User selects or handoff triggers |
| MCP Servers | Session start (if configured) |
| Hooks | During agent sessions on lifecycle events |
| Memory | Automatically retrieved and validated at session start and during reasoning |

---

## Surface Support

This is the rollout matrix used throughout this guide, not the upstream product contract. For IDE status, the source of truth is the [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix). For GitHub Copilot CLI and the Cloud Coding Agent, use the current product docs. This snapshot was revalidated on April 22, 2026.

| Primitive | VS Code | JetBrains IDEs | Visual Studio | Eclipse | Xcode | GitHub Copilot CLI | Cloud Coding Agent |
|-----------|---------|----------------|---------------|---------|-------|--------------------|-------------------|
| Always-on Instructions | Supported | Preview | Supported | Preview | Preview | Supported | Supported |
| File-based Instructions | Supported | Verify in plugin build | Verify in current release | Verify in current release | Not the primary path | Supported | Supported |
| Prompt files | Supported | Preview | Supported in current release | Not supported | Preview | Not a prompt-file surface | Not a prompt-file surface |
| Skills | Supported | Preview | Not supported | Not supported | Not supported | Supported | Supported |
| Custom Agents | Supported | Preview | Preview | Supported | Preview | Supported | Supported |
| MCP | Supported | Supported | Supported | Supported | Supported | Supported | Supported |
| Hooks | Preview | Not supported | Not supported | Not supported | Not supported | Supported | Supported |
| Memory | Not used in IDE chat | Not used in IDE chat | Not used in IDE chat | Not used in IDE chat | Not used in IDE chat | Preview | Preview |

**How to read this table:**

- `Supported` means the feature is usable now on current documented releases.
- `Preview` means it exists, but rollout should stay in pilot mode until the exact version and workflow are tested.
- `Verify in current release` means the official matrix groups support more broadly than this guide's primitive split. Treat the per-surface page as the rollout note, not this cell alone.
- `Not the primary path` means the surface can still benefit from the repository layer, but this primitive is not the safest place to start there.

**Maintenance note:** Revalidate this matrix against the official feature matrix and the relevant surface docs before publishing changes. Preview rows move fast and are not safe to treat as timeless repository policy.

**Memory note:** Copilot Memory is currently used by the Cloud Coding Agent, GitHub Copilot code review on GitHub, and GitHub Copilot CLI. It is not currently used by VS Code chat or other IDE chat surfaces.

**Contributor-safe baseline:** For mixed-editor or public-repo rollouts, standardize first on Always-on Instructions, then add prompt files, MCP, or preview features only where the team has tested the exact surface and version it supports.

---

## Frontmatter Reference

### Always-on Instructions

No frontmatter required. Plain markdown.

```markdown
# Copilot Instructions for Acme Payments

## Tech Stack
...
```

### File-based Instructions

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
| `model` | No | string | AI model |
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

| Syntax | Description |
|--------|-------------|
| `${file}`, `${selection}`, `${workspaceFolder}` | Built-in VS Code context variables |
| `${input:variableName}` | Prompts the user for a value when invoked |
| `${input:variableName:placeholder}` | Prompts the user, showing placeholder hint text |

### Skills (SKILL.md)

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `name` | **Yes** | string | 1-64 chars, lowercase, hyphens only |
| `description` | **Yes** | string | 1-1024 chars, WHAT + WHEN to use |
| `argument-hint` | No | string | Hint text when invoked as `/` command |
| `user-invocable` | No | boolean | Show as `/` slash command (default: `true`) |
| `disable-model-invocation` | No | boolean | Require manual invocation only (default: `false`) |
| `metadata` | No | object | Key-value pairs (author, version) |
| `license` | No | string | License name or reference |
| `compatibility` | No | string | Environment requirements |

**Name validation rules:**
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
| `model` | No | string or string[] | AI model; supports arrays for fallback |
| `handoffs` | No | object[] | Transitions to other agents |
| `argument-hint` | No | string | Hint text for user interaction |
| `user-invocable` | No | boolean | Whether the agent can be manually selected (default: `true`) |
| `disable-model-invocation` | No | boolean | Prevent automatic/subagent invocation (default: `false`) |
| `agents` | No | string[] | Restrict available subagents: names, `*`, or `[]` |
| `target` | No | string | Target environment: `vscode` or `github-copilot` |
| `mcp-servers` | No | object[] | MCP servers for `github-copilot` target |
| `hooks` | No | object | Agent-scoped hooks (Preview) |

### MCP Configuration Fields

Repository MCP configuration is usually stored in `.vscode/mcp.json`, but the runtime still matters:

- workspace configuration travels with the repo,
- user configuration stays local to the developer profile,
- remote configuration runs where the remote workspace runs,
- and Cloud Coding Agent MCP uses the GitHub-hosted runtime, not a process on the laptop.

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
| `sandboxEnabled` | boolean | Run in the VS Code sandbox (macOS and Linux only) |
| `sandbox` | object | File system and network rules for a sandboxed server |
| `dev` | object | Development mode config with `watch` and `build` commands |

**Variable syntax in `env` values:**

| Syntax | Where | Description |
|--------|-------|-------------|
| `${env:VAR_NAME}` | Workspace / user MCP | Read from environment variable |
| `${env:VAR:-default}` | Workspace / user MCP | Environment variable with fallback |
| `${input:variableName}` | Workspace / user MCP | Prompt the user for a value at startup |
| `$VAR` / `${VAR}` | Cloud Coding Agent / custom-agent YAML | Environment variable |
| `${{ secrets.NAME }}` | Cloud Coding Agent custom-agent YAML | Secret from the repository's `copilot` environment |
| `${{ vars.NAME }}` | Cloud Coding Agent custom-agent YAML | Variable from the repository's `copilot` environment |

### Hook Object Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `type` | Yes | string | Must be `"command"` |
| `command` | Yes | string | Default cross-platform command or script path |
| `windows` | No | string | Windows-specific override |
| `linux` | No | string | Linux-specific override |
| `osx` | No | string | macOS-specific override |
| `cwd` | No | string | Working directory (relative to repo root) |
| `env` | No | object | Environment variables |
| `timeout` | No | number | Max execution time in seconds (default: 30) |

### Hook Lifecycle Events

| Hook | Can Block? | Key Input Fields |
|------|------------|------------------|
| `SessionStart` | No | `timestamp`, `cwd`, `source` |
| `UserPromptSubmit` | No | `timestamp`, `cwd`, `prompt` |
| `PreToolUse` | **Yes** | `timestamp`, `cwd`, `tool_name`, `tool_input`, `tool_use_id` |
| `PostToolUse` | Can block follow-on processing | `timestamp`, `cwd`, `tool_name`, `tool_input`, `tool_response` |
| `PreCompact` | No | `timestamp`, `cwd`, `trigger` |
| `SubagentStart` | No | `timestamp`, `cwd`, `agent_id`, `agent_type` |
| `SubagentStop` | Can block subagent completion | `timestamp`, `cwd`, `agent_id`, `agent_type`, `stop_hook_active` |
| `Stop` | Can block session completion | `timestamp`, `cwd`, `stop_hook_active` |

**Compatibility note:** VS Code reads Copilot CLI hook files and translates lower-camel event names such as `preToolUse`, plus `bash` and `powershell` command fields, into the current preview contract. Use the PascalCase form above when the file is meant to be a primary VS Code reference.

### Hook Output Controls

| Event | Useful output fields | What they do |
|-------|----------------------|--------------|
| All hooks | `continue`, `stopReason`, `systemMessage` | Stop the session, explain the stop, or show a warning |
| `PreToolUse` | `permissionDecision`, `permissionDecisionReason`, `updatedInput`, `additionalContext` | Allow, deny, or prompt for a tool call; rewrite input; add model context |
| `PostToolUse` | `decision`, `reason`, `hookSpecificOutput.additionalContext` | Block follow-on processing or feed validation context back to the model |
| `SessionStart`, `SubagentStart` | `hookSpecificOutput.additionalContext` | Inject context at session or subagent start |
| `Stop`, `SubagentStop` | `decision`, `reason` | Prevent completion when more work is required |

---

## Execution Modes

| Mode | Copilot Can... | Best For |
|------|----------------|----------|
| `ask` | Respond conversationally (read-only) | Q&A, explanations, brainstorming |
| `agent` | Create/edit files, run commands, use tools | Any task that modifies code |
| `plan` | Generate structured implementation plans | Breaking down tasks before implementation |
| Custom agent | Use that agent's persona and tools | Specialized workflows |

**Edit Mode Deprecation:** `edit` mode is deprecated as of VS Code 1.110. Use `agent` for all file modifications.

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

### Practical Starter Patterns

| Scenario | Example `applyTo` |
|----------|-------------------|
| Frontend monorepo UI components | `apps/web/src/components/**/*.tsx` |
| Shared design-system package | `packages/ui/src/**/*.{ts,tsx}` |
| Design tokens or generated UI assets | `packages/tokens/**` |
| Storybook stories | `**/*.stories.{ts,tsx,mdx}` |
| SwiftUI views | `**/*View.swift` |
| XCTest files | `**/*Tests.swift` |
| Android Gradle and Kotlin build files | `**/*.{kt,kts,gradle}` |
| Android manifest and resources | `**/AndroidManifest.xml` |
| Python modules and notebooks | `**/*.{py,ipynb}` |
| SQL and warehouse queries | `**/*.{sql,ddl}` |

### Notebook Note

Notebook-heavy repos usually need two patterns, not one: a `.py` pattern for library and pipeline code, and an `.ipynb` pattern for exploratory work. Keep the notebook file focused on cell hygiene, output handling, and reproducibility. Keep the `.py` file focused on module structure, tests, and packaging.

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

**Total active context:** Keep under 4000 words. If GitHub Copilot seems to "forget" rules, the active instruction set may be too long. Move specialized content into file-based instructions or skills.

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

¹ Hooks are active during coding agent, GitHub Copilot CLI, and VS Code Chat agent sessions, not in inline completions.
² Prompt files are a VS Code feature. GitHub Copilot CLI uses natural language prompts and custom agents instead.

---

## Troubleshooting

### Chat Customization Diagnostics

VS Code 1.116 includes a diagnostics view:

1. Right-click in the Chat view.
2. Select **Diagnostics**.
3. Review the Markdown document listing all active customization files.

The diagnostics view shows all loaded custom agents, prompt files, instruction files, and skills, their load status, and any errors that occurred during loading.

If the team works shell-first, use the equivalent runtime's inspection tools instead of assuming this UI exists. In GitHub Copilot CLI or other terminal-centric flows, the practical check is the same: inspect what loaded, run one narrow prompt or tool call, and confirm the runtime is actually using the expected files and approvals.

### Manual Debugging

> 💬 **Try this prompt:**
> "What instructions, skills, and tools are currently active?"

> 💬 **Try this prompt:**
> "I expected X but got Y. What rules are you following?"

### Verify File Locations

- Always-on: `.github/copilot-instructions.md` (exact name)
- File-based: `.github/instructions/*.instructions.md`
- Prompts: `.github/prompts/*.prompt.md`
- Skills: `.github/skills/*/SKILL.md`
- Agents: `.github/agents/*.md` or `**/*.agent.md`
- MCP: `.vscode/mcp.json`
- Hooks: `.github/hooks/*.json`

---

## Common Failure Modes

### Instructions
| Don't | Why | Do Instead |
|-------|-----|------------|
| Write by hand without agent help | Errors, missed patterns | Have the agent generate from codebase |
| Copy from other repos | Wrong conventions | Generate per-repo |
| Over 2000 words | Dilutes important rules | Split to file-based |
| No rationale | Poor edge-case handling | Include "why" |
| Never update | Drift from practice | Treat as code, PR changes |

### Prompts
| Don't | Why | Do Instead |
|-------|-----|------------|
| Vague instructions | Inconsistent results | Be specific |
| No variables | Not reusable | Use `${input:variableName}` |
| No model specified | Inconsistent | Specify model |

### Skills
| Don't | Why | Do Instead |
|-------|-----|------------|
| Uppercase in name | Validation fails | Lowercase with hyphens |
| Weak description | Will not activate | Include WHAT + WHEN + keywords |
| Generic content | Low value | Domain-specific knowledge |

### MCP
| Don't | Why | Do Instead |
|-------|-----|------------|
| 100+ tools | Slow, inaccurate | Under 70 tools total |
| All servers always on | Wasted context | Disable unused servers |
| Hardcoded secrets | Security risk | Use `${env:VAR}` |

### Hooks
| Don't | Why | Do Instead |
|-------|-----|------------|
| Use hooks instead of instructions | Hooks deny; they cannot guide generation | Instructions for guidance, hooks for enforcement |
| Slow synchronous network calls | Blocks agent execution | Fire-and-forget or batch at session end |
| Log secrets in audit trails | Logs may be persisted or shared | Filter sensitive fields before writing |
| Only rely on one platform-specific command | The hook can fail on another runtime or remote host | Provide `command` plus OS overrides when needed |
| Skip `timeout` | Default 30s may be wrong | Set a timeout appropriate to each hook |

---

## Starter Templates

### copilot-instructions.md

```markdown
# Copilot Instructions for Acme Payments

## Project Overview
This repository contains the checkout API, the web checkout flow, and shared payment-domain libraries.

## Tech Stack
- TypeScript and Node.js
- PostgreSQL
- React for the checkout UI

## Code Style
- Prefer explicit types at API boundaries.
- Keep payment amounts in integer minor units.
- Return structured errors with stable codes.

## Architecture
Business rules live under `src/domain/`. HTTP handlers should stay thin and call domain services rather than embedding payment logic.

## Testing
- Use Vitest for unit tests and Playwright for checkout flows.
- Keep tests next to source files or under `tests/e2e/` for browser scenarios.

## What NOT to Do
- Don't call external payment providers directly from UI components.
- Don't log full payment payloads or secrets.
```

### File-based Instruction

```markdown
---
name: 'API Routes'
description: 'Conventions for REST API endpoints'
applyTo: 'src/api/**/*'
---

# API Route Guidelines

## Response Format
Return JSON with a stable top-level shape: `data` for success, `error` for failures.

## Error Handling
Map domain failures to explicit HTTP status codes. Do not return raw stack traces.

## Authentication
Assume bearer-token authentication and require tenant scoping on every write endpoint.
```

### Prompt File

```markdown
---
agent: 'agent'
description: 'Generate tests for a changed module using repo test conventions'
model: 'Claude Opus 4.7'
---

Generate or update tests for the target file using the repository's existing test stack.

**Input:** ${input:targetFile:Path to the changed source file}

## Requirements
1. Prefer extending an existing nearby test file before creating a new one.
2. Cover the main success path and the highest-risk failure path.
3. Do not invent frameworks not already used in the repo.

## Output Format
Return a short test plan, then create or edit the test file.
```

### SKILL.md

```markdown
---
name: skill-name
description: Investigates flaky tests and CI-only failures. Use when the user mentions intermittent failures, flaky tests, retries, or unstable CI.
metadata:
  author: your-org
  version: "1.0"
---

# Skill Name

## When to Use
- Use when the user asks to investigate a flaky test.
- Use when CI failed intermittently and the agent needs a repeatable debugging path.

## Instructions
1. Find the most recent failing test output.
2. Compare the failure against previous passing runs if available.
3. Identify whether the issue is timing, test data, environment setup, or shared state.
4. Propose the smallest fix and the narrowest validation command.

## Examples
- "Why does this Playwright test fail only in CI?"
- "Investigate this flaky xUnit suite and suggest a fix."
```

### Custom Agent

```markdown
---
name: 'Agent Name'
description: 'What this agent does'
tools: ['search', 'readFile']
model: 'Claude Opus 4.7'
---

You are a release-safety reviewer.

## Your Expertise
- Deployment risk
- Rollback planning

## How You Respond
- Prefer short risk summaries before recommendations.
- Ask for the validation or rollback command when it is missing.

## What You Never Do
- Never approve a production change with no rollback path.
- Never assume a preview feature is safe to standardize across every IDE.
```

### MCP Configuration

```json
{
  "servers": {
    "playwright": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@microsoft/mcp-server-playwright"]
    },
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp",
      "env": {
        "GITHUB_TOKEN": "${env:GITHUB_TOKEN}"
      }
    }
  }
}
```

**How to verify:** Start the server from VS Code or the target runtime, confirm trust if prompted, then ask GitHub Copilot to perform one narrow task such as taking a screenshot with Playwright or listing one issue through the GitHub server.

### Hooks Configuration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "./scripts/hooks/block-dangerous-commands.sh",
        "windows": "powershell -File scripts\\hooks\\block-dangerous-commands.ps1",
        "cwd": ".",
        "timeout": 10
      }
    ],
    "PostToolUse": [
      {
        "type": "command",
        "command": "./scripts/hooks/log-tool-usage.sh",
        "windows": "powershell -File scripts\\hooks\\log-tool-usage.ps1"
      }
    ]
  }
}
```

**How to verify:** Save the file, trigger one safe tool use, and check the `GitHub Copilot Chat Hooks` output channel. If nothing appears, first confirm the file is under `.github/hooks/` and that the event name uses the PascalCase form.

---

## Official Resources

| Resource | URL |
|----------|-----|
| GitHub Copilot Docs | https://docs.github.com/en/copilot |
| VS Code Copilot Docs | https://code.visualstudio.com/docs/copilot |
| GitHub Copilot CLI | https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli |
| MCP Specification | https://modelcontextprotocol.io |
| Agent Skills Spec | https://agentskills.io |
| Copilot Memory | https://docs.github.com/en/copilot/concepts/agents/copilot-memory |
| GitHub Agentic Workflows | https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/ |
| Awesome Copilot | https://github.com/github/awesome-copilot |

---

[← Measuring Success](measuring-success.md) | [Back to Guide →](README.md)
