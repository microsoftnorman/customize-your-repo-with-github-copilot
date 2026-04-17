# Hooks

[← MCP](primitive-6-mcp.md) | [Part II Overview](part-2-primitives.md)

*Updated: April 17, 2026 · Validated against VS Code 1.116 and GitHub Copilot docs as of April 16, 2026.*

---

## Overview

Most of the customization primitives operate inside Copilot's reasoning: instructions, file-based instructions, prompts, skills, custom agents, MCP, and Memory. They shape context and influence code generation. None of them can *enforce* anything. A rule in `copilot-instructions.md` is a strong suggestion, not a guarantee.

Hooks fill that gap. They execute custom shell commands at key points during Copilot coding agent sessions, operating *outside* the model entirely. The LLM never sees hook logic. It can't override hook logic, and it can't reason around it. That gives teams an enforcement layer independent of prompt engineering.

**\* Items marked with an asterisk (\*) reflect current behavior that may change as the hooks system evolves. Verify against [official documentation](https://docs.github.com/en/copilot/reference/hooks-configuration) when making architectural decisions.**

> **How strong is "enforcement"?** Hooks are **tripwires, not impenetrable guardrails**. `preToolUse` can deny a specific tool invocation based on the arguments the agent passes, but the agent can often reach the same outcome through a different tool or a slightly rephrased command. A regex `deny` list that blocks `rm -rf /` will not block `find / -delete`, `python -c "shutil.rmtree('/')"`, or an MCP tool that happens to offer a delete capability. Treat hooks as a high-signal audit layer and a last line of defense for known-bad patterns. They are not a substitute for scoped credentials, sandboxed execution environments, read-only tokens, and branch protection. The strongest setups pair hooks with infrastructure-level controls so that even if the agent bypasses a hook, the blast radius is bounded.

**Surface availability:** VS Code ✅ · GitHub Copilot CLI ✅ · Cloud Coding Agent ✅ · JetBrains — · Visual Studio — · Eclipse —

**Ownership:** Hooks are typically owned by **Security / Platform teams** because they enforce organization-wide policy. Application teams may contribute package-scoped hooks in a monorepo (e.g., per-service lint), but deny-list hooks that govern dangerous commands should live under a single owning team to keep the rules coherent and auditable.

**Loading:** During coding agent sessions (GitHub and GitHub Copilot CLI)*
**Best For:** Security enforcement, audit logging, compliance, and runtime guardrails

**Location:** `.github/hooks/*.json`

**Official docs:** [Copilot hooks](https://code.visualstudio.com/docs/copilot/customization/hooks)

**See it in action:** For a live demo, watch Pierce Boggan and James Montemagno in [Let it Cook: Agent Steering, Queueing, Hooks, CLI Integration, & more!](https://www.youtube.com/watch?v=FjvtWeG6EEo).

Primitives and hooks operate at different layers:

- **Primitives** (instructions, skills, agents, prompts, MCP) shape Copilot's *mind*. They determine what it knows, how it reasons, and what tools it can call.
- **Hooks** govern Copilot's *actions*. They intercept tool calls at execution time to approve, deny, or log them.

Use both. Primitives guide Copilot toward correct behavior. Hooks verify and audit that behavior as it happens.

### Availability & Requirements

Hooks are available with the **GitHub Copilot Pro, Pro+, Business, and Enterprise** plans.* They apply in three surfaces:*

| Surface | Hook Source | Notes |
|---------|------------|-------|
| **Copilot coding agent** (GitHub) | `.github/hooks/*.json` on the **default branch** | Hooks must be merged to the default branch before the coding agent uses them |
| **GitHub Copilot CLI** (terminal) | `.github/hooks/*.json` in the **current working directory** | Loads hooks from whoever is running the CLI locally |
| **VS Code Chat** (agent sessions) | `.github/hooks/*.json` or Claude Code config files | Available in VS Code 1.109.3+. File-based configuration |

For VS Code Chat configuration details, see [VS Code Hooks](#vs-code-hooks-chat-agent-sessions) below.

### Hooks vs. Primitives: Different Layers, Complementary Purposes

| Aspect | The Other Primitives | Hooks |
|--------|-------------------------|-------|
| **When they act** | Before and during LLM reasoning | At runtime, during agent execution |
| **What they influence** | What Copilot knows and how it thinks | What Copilot is allowed to do |
| **How they work** | Injected into the model's context window | Shell scripts that run outside the model |
| **Visible to the LLM** | Yes — the model reads and follows them | No — the model doesn't see hook logic |
| **Where they apply** | All Copilot surfaces (Chat, Completions, Inline, Coding Agent) | Coding agent, Copilot CLI, and VS Code Chat (1.109.3+) |
| **Can block actions** | No (advisory only) | Yes (`preToolUse` can deny tool calls) |
| **Can produce audit trails** | No | Yes (every hook type can log) |

### When to Use Hooks

Hooks fit scenarios the other primitives can't address:

| Scenario | Why Primitives Aren't Enough | What Hooks Add |
|----------|------------------------------|----------------|
| **Compliance auditing** | Instructions don't produce logs | Every hook type can write structured audit trails |
| **Blocking dangerous commands** | "Don't run `rm -rf /`" in instructions is advisory | `preToolUse` hard-blocks the command before execution |
| **Restricting file access** | File-based instructions guide *how* to edit files, not *whether* to edit them | `preToolUse` can deny edits outside allowed directories |
| **External notifications** | MCP gives Copilot tools to *call* external systems; it doesn't monitor Copilot's own actions | Hooks can send Slack alerts, emails, or webhook calls on any event |
| **Cost tracking** | No primitive tracks tool usage | `preToolUse`/`postToolUse` can log every tool invocation for cost allocation |
| **Session monitoring** | No primitive knows when sessions start or end | `sessionStart`/`sessionEnd` provide lifecycle visibility |

### Creating This Primitive

Sound off before you steer — let Copilot draft the hook. Hook JSON has a tight schema (`version`, valid event names, correct shell keys for `bash` and `powershell`, timeout formats) and a hand-typed file with a typo'd event name or missing `version` field is ignored silently. In VS Code, run `/create-hook` in Chat to scaffold `.github/hooks/*.json` with the correct structure, or describe the hook in plain English and let Copilot write it. There is no dedicated GUI editor for hooks today. See [Don't Hand-Type Primitives — Let the Helmsman Repeat the Order](part-2-primitives.md#dont-hand-type-primitives--let-the-helmsman-repeat-the-order) for the rationale.

> **💬 Try this prompt:**
>
> *Create a `.github/hooks/block-rm-rf.json` hook that uses `preToolUse` to deny any shell invocation whose command matches `rm -rf`, `find / -delete`, or `python -c "shutil.rmtree"`. Log the blocked attempt to `logs/blocked-commands.log` with a timestamp. Provide both `bash` and `powershell` variants.*

> **💬 Try this prompt:**
>
> *Scaffold a `.github/hooks/audit.json` hook that writes every `postToolUse` event to `logs/audit.jsonl` as one JSON object per line: timestamp, tool name, arguments, and exit status. Keep the shell commands short and cross-platform.*

---

## Getting Started

Follow these four steps to create your first hook:

### Step 1: Create the Hook File

Create a new `.json` file in `.github/hooks/`. The name is your choice. Use something descriptive:

```
.github/
└── hooks/
    └── my-first-hook.json
```

### Step 2: Add the Hook Template

Paste the following template and remove any hook types you don't need:

```json
{
  "version": 1,
  "hooks": {
    "sessionStart": [],
    "sessionEnd": [],
    "userPromptSubmitted": [],
    "preToolUse": [],
    "postToolUse": [],
    "errorOccurred": []
  }
}
```

### Step 3: Configure a Hook

Add a hook definition under the appropriate event. This minimal example logs every session start:

```json
{
  "version": 1,
  "hooks": {
    "sessionStart": [
      {
        "type": "command",
        "bash": "echo \"Session started: $(date)\" >> logs/session.log",
        "powershell": "Add-Content -Path logs/session.log -Value \"Session started: $(Get-Date)\"",
        "cwd": ".",
        "timeoutSec": 10
      }
    ]
  }
}
```

You can use inline commands (as above) or reference external script files:

```json
{
  "type": "command",
  "bash": "./scripts/hooks/my-hook.sh",
  "powershell": "./scripts/hooks/my-hook.ps1",
  "cwd": "scripts/hooks"
}
```

### Step 4: Commit and Merge

Commit the file to your repository and merge it into the **default branch**. For the coding agent, hooks are only loaded from the default branch. For Copilot CLI, hooks are loaded from the current working directory immediately.

---

## The Hook Lifecycle

Hooks fire at six points during an agent session. The following diagram shows when each hook type executes relative to the agent's workflow:

**See it in action:** [Let it Cook: Agent Steering, Queueing, Hooks, CLI Integration, & more!](https://www.youtube.com/watch?v=FjvtWeG6EEo&t=1868s). Pierce Boggan walks through the run-start, tool-call, and stop points in the agent loop and shows where hooks fire at each life-cycle event.

```
┌─────────────────────────────────────────────────────────────┐
│                    AGENT SESSION                            │
│                                                             │
│  ┌──────────────┐                                           │
│  │ sessionStart │ ← Session begins or resumes               │
│  └──────┬───────┘                                           │
│         │                                                   │
│         ▼                                                   │
│  ┌─────────────────────┐                                    │
│  │ userPromptSubmitted │ ← User sends a message             │
│  └──────┬──────────────┘                                    │
│         │                                                   │
│         ▼                                                   │
│  ┌─────────────────────────────────────┐                    │
│  │        Agent Reasoning Loop         │                    │
│  │                                     │                    │
│  │  ┌──────────┐    ┌─────────────┐    │                    │
│  │  │preToolUse│───►│ Tool Executes│    │  ← Can DENY       │
│  │  └──────────┘    └──────┬──────┘    │                    │
│  │                         │           │                    │
│  │                  ┌──────▼───────┐   │                    │
│  │                  │ postToolUse  │   │  ← Observe result  │
│  │                  └──────────────┘   │                    │
│  │                                     │                    │
│  │         (repeats for each tool)     │                    │
│  └─────────────────────────────────────┘                    │
│         │                                                   │
│         ▼ (on error at any point)                           │
│  ┌───────────────┐                                          │
│  │ errorOccurred │ ← Captures errors                        │
│  └───────────────┘                                          │
│         │                                                   │
│         ▼                                                   │
│  ┌────────────┐                                             │
│  │ sessionEnd │ ← Session completes or terminates           │
│  └────────────┘                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### The Six Hook Types

| Hook | Fires When | Can Modify Behavior? | Primary Use Cases |
|------|-----------|---------------------|-------------------|
| `sessionStart` | Agent session begins or resumes | No (output ignored) | Environment setup, session logging, resource initialization |
| `sessionEnd` | Session completes or terminates | No (output ignored) | Cleanup, session reports, notification of completion |
| `userPromptSubmitted` | User submits a prompt | No (can't modify prompt) | Audit logging, usage analysis, keyword alerting |
| `preToolUse` | Before any tool call (`bash`, `edit`, `view`, `create`)* | **Yes — can deny execution** | Security policies, command blocking, file access control |
| `postToolUse` | After a tool completes (success or failure) | No (can't modify result)* | Statistics tracking, failure alerts, audit trails |
| `errorOccurred` | An error occurs during execution | No (can't modify handling)* | Error logging, alerting, pattern tracking |

`preToolUse` is the only hook that can deny a tool call. Every other hook is observe-only.*

---

## Configuration

### File Structure

Hook configuration files live in `.github/hooks/` and use JSON format. A repository can contain multiple hook files. All `.json` files in the directory are loaded.

```
.github/
└── hooks/
    ├── security.json       # Security enforcement hooks
    ├── audit.json          # Compliance audit hooks
    └── notifications.json  # Alert and notification hooks
```

The hooks configuration must be present on the repository's **default branch** to be used by the coding agent. For Copilot CLI, hooks are loaded from the current working directory.

### Monorepo Discovery

VS Code 1.111+ discovers hooks from parent folders up to the repository root. This means team-wide hooks can live at the repo root while package-specific hooks live in subdirectories:

```
my-monorepo/
├── .github/
│   └── hooks/
│       └── security.json        # Applies to ALL packages
├── packages/
│   ├── frontend/
│   │   └── .github/
│   │       └── hooks/
│   │           └── lint.json    # Frontend-specific hooks
│   └── backend/
│       └── .github/
│           └── hooks/
│               └── db-check.json # Backend-specific hooks
```

Hooks at every level in the hierarchy are merged and executed. Root-level hooks enforce organization-wide policies (security, auditing), while package-level hooks handle context-specific concerns (linting rules, database access patterns). This eliminates the need to duplicate shared hooks across every package.

### Configuration Format

Every hooks file requires a `version` field (must be `1`)* and a `hooks` object containing arrays of hook definitions:

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

Each hook in an array is an object with the following fields:

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `type` | Yes | string | Must be `"command"`* |
| `bash` | Yes (Unix) | string | Shell command or path to script |
| `powershell` | Yes (Windows) | string | PowerShell command or path to script |
| `cwd` | No | string | Working directory, relative to repository root |
| `env` | No | object | Additional environment variables |
| `timeoutSec` | No | number | Maximum execution time in seconds (default: 30)* |
| `comment` | No | string | Human-readable description (used in official examples but not in formal schema)* |

### Minimal Example

A single hook that logs session starts:

```json
{
  "version": 1,
  "hooks": {
    "sessionStart": [
      {
        "type": "command",
        "bash": "echo \"Session started: $(date)\" >> logs/session.log",
        "powershell": "Add-Content -Path logs/session.log -Value \"Session started: $(Get-Date)\"",
        "cwd": ".",
        "timeoutSec": 10
      }
    ]
  }
}
```

### Full Example

A production-ready configuration with security, auditing, and alerting:

```json
{
  "version": 1,
  "hooks": {
    "sessionStart": [
      {
        "type": "command",
        "bash": "./scripts/hooks/session-start.sh",
        "powershell": "./scripts/hooks/session-start.ps1",
        "cwd": ".",
        "timeoutSec": 10,
        "comment": "Initialize session logging and verify environment"
      }
    ],
    "userPromptSubmitted": [
      {
        "type": "command",
        "bash": "./scripts/hooks/log-prompt.sh",
        "powershell": "./scripts/hooks/log-prompt.ps1",
        "cwd": "scripts/hooks",
        "env": {
          "LOG_LEVEL": "INFO"
        },
        "comment": "Log prompts for audit trail"
      }
    ],
    "preToolUse": [
      {
        "type": "command",
        "bash": "./scripts/hooks/security-check.sh",
        "powershell": "./scripts/hooks/security-check.ps1",
        "cwd": "scripts/hooks",
        "timeoutSec": 15,
        "comment": "Block dangerous commands and enforce file access policies"
      },
      {
        "type": "command",
        "bash": "./scripts/hooks/log-tool-use.sh",
        "powershell": "./scripts/hooks/log-tool-use.ps1",
        "cwd": "scripts/hooks",
        "comment": "Log all tool invocations for compliance"
      }
    ],
    "postToolUse": [
      {
        "type": "command",
        "bash": "cat >> logs/tool-results.jsonl",
        "powershell": "$input | Add-Content -Path logs/tool-results.jsonl",
        "comment": "Append tool results to audit log"
      }
    ],
    "errorOccurred": [
      {
        "type": "command",
        "bash": "./scripts/hooks/error-alert.sh",
        "powershell": "./scripts/hooks/error-alert.ps1",
        "cwd": "scripts/hooks",
        "comment": "Log errors and send alerts for critical failures"
      }
    ],
    "sessionEnd": [
      {
        "type": "command",
        "bash": "./scripts/hooks/cleanup.sh",
        "powershell": "./scripts/hooks/cleanup.ps1",
        "cwd": "scripts/hooks",
        "timeoutSec": 60,
        "comment": "Clean up temp resources and finalize session report"
      }
    ]
  }
}
```

---

## Hook Input and Output

Every hook receives JSON on stdin describing the event. The structure varies by hook type, but all include `timestamp` and `cwd`.

### sessionStart Input

```json
{
  "timestamp": 1704614400000,
  "cwd": "/path/to/project",
  "source": "new",
  "initialPrompt": "Create a new feature"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `timestamp` | number | Unix timestamp in milliseconds |
| `cwd` | string | Current working directory |
| `source` | string | `"new"`, `"resume"`, or `"startup"`* |
| `initialPrompt` | string | The user's initial prompt (if provided) |

**Output:** Ignored.

### sessionEnd Input

```json
{
  "timestamp": 1704618000000,
  "cwd": "/path/to/project",
  "reason": "complete"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `reason` | string | `"complete"`, `"error"`, `"abort"`, `"timeout"`, or `"user_exit"`* |

**Output:** Ignored.

### userPromptSubmitted Input

```json
{
  "timestamp": 1704614500000,
  "cwd": "/path/to/project",
  "prompt": "Fix the authentication bug"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `prompt` | string | The exact text the user submitted |

**Output:** Ignored. Prompt modification is not supported.*

### preToolUse Input

```json
{
  "timestamp": 1704614600000,
  "cwd": "/path/to/project",
  "toolName": "bash",
  "toolArgs": "{\"command\":\"rm -rf dist\",\"description\":\"Clean build directory\"}"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `toolName` | string | Name of the tool (`"bash"`, `"edit"`, `"view"`, `"create"`)* |
| `toolArgs` | string | JSON string containing the tool's arguments |

**Output:** This is the only hook that processes output. Return JSON to control execution:

```json
{
  "permissionDecision": "deny",
  "permissionDecisionReason": "Destructive operations require approval"
}
```

| Field | Values | Behavior |
|-------|--------|----------|
| `permissionDecision` | `"allow"` | Explicitly allow the tool call |
| | `"deny"` | Block the tool call (reason shown to agent) |
| | `"ask"` | Not currently processed by the agent* |
| `permissionDecisionReason` | string | Human-readable explanation |

If the hook produces no output or exits without JSON, the tool call is **allowed by default**.*

### postToolUse Input

```json
{
  "timestamp": 1704614700000,
  "cwd": "/path/to/project",
  "toolName": "bash",
  "toolArgs": "{\"command\":\"npm test\"}",
  "toolResult": {
    "resultType": "success",
    "textResultForLlm": "All tests passed (15/15)"
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `toolResult.resultType` | string | `"success"`, `"failure"`, or `"denied"`* |
| `toolResult.textResultForLlm` | string | The result text shown to the agent |

**Output:** Ignored. Result modification is not supported.*

### errorOccurred Input

```json
{
  "timestamp": 1704614800000,
  "cwd": "/path/to/project",
  "error": {
    "message": "Network timeout",
    "name": "TimeoutError",
    "stack": "TimeoutError: Network timeout\n    at ..."
  }
}
```

**Output:** Ignored. Error handling modification is not supported.*

---

## Practical Examples

### Example 1: Security Policy Enforcement

A `preToolUse` hook that blocks dangerous shell commands and restricts file edits to allowed directories:

**`.github/hooks/security.json`:**
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
        "comment": "Enforce security policies on all tool calls"
      }
    ]
  }
}
```

**`scripts/hooks/security-check.sh`:**
```bash
#!/bin/bash
set -e

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.toolName')
TOOL_ARGS=$(echo "$INPUT" | jq -r '.toolArgs')

# --- Block dangerous shell commands ---
if [ "$TOOL_NAME" = "bash" ]; then
  COMMAND=$(echo "$TOOL_ARGS" | jq -r '.command')

  # Pattern list of dangerous operations
  if echo "$COMMAND" | grep -qE "rm -rf /|sudo |mkfs\.|format |DROP TABLE|TRUNCATE TABLE"; then
    echo '{"permissionDecision":"deny","permissionDecisionReason":"Blocked: destructive system command detected"}'
    exit 0
  fi

  # Block commands that could leak secrets
  if echo "$COMMAND" | grep -qE "printenv|env\b|cat.*\.env|echo.*SECRET|echo.*TOKEN|echo.*PASSWORD"; then
    echo '{"permissionDecision":"deny","permissionDecisionReason":"Blocked: potential secret exposure"}'
    exit 0
  fi
fi

# --- Restrict file edits to allowed directories ---
if [ "$TOOL_NAME" = "edit" ] || [ "$TOOL_NAME" = "create" ]; then
  FILE_PATH=$(echo "$TOOL_ARGS" | jq -r '.path // empty')

  if [ -n "$FILE_PATH" ]; then
    # Only allow edits in src/, test/, and docs/
    if [[ ! "$FILE_PATH" =~ ^(src/|test/|docs/) ]]; then
      echo "{\"permissionDecision\":\"deny\",\"permissionDecisionReason\":\"Edits restricted to src/, test/, and docs/ directories\"}"
      exit 0
    fi
  fi
fi

# Allow everything else
```

**`scripts/hooks/security-check.ps1`:**
```powershell
$ErrorActionPreference = "Stop"

$input = [Console]::In.ReadToEnd() | ConvertFrom-Json
$toolName = $input.toolName
$toolArgs = $input.toolArgs | ConvertFrom-Json

# Block dangerous shell commands
if ($toolName -eq "bash") {
    $command = $toolArgs.command

    $dangerousPatterns = @(
        'rm -rf /', 'sudo ', 'mkfs\.', 'format ',
        'DROP TABLE', 'TRUNCATE TABLE'
    )

    foreach ($pattern in $dangerousPatterns) {
        if ($command -match $pattern) {
            @{
                permissionDecision = "deny"
                permissionDecisionReason = "Blocked: destructive system command detected"
            } | ConvertTo-Json -Compress
            exit 0
        }
    }
}

# Restrict file edits to allowed directories
if ($toolName -in @("edit", "create")) {
    $filePath = $toolArgs.path

    if ($filePath -and $filePath -notmatch '^(src/|test/|docs/)') {
        @{
            permissionDecision = "deny"
            permissionDecisionReason = "Edits restricted to src/, test/, and docs/ directories"
        } | ConvertTo-Json -Compress
        exit 0
    }
}

# Allow everything else (no output = allow)
```

### Example 2: Compliance Audit Trail

A complete audit logging setup that records every agent action as structured JSON Lines. The format suits compliance requirements, cost tracking, and post-incident analysis:

**`.github/hooks/audit.json`:**
```json
{
  "version": 1,
  "hooks": {
    "sessionStart": [
      {
        "type": "command",
        "bash": "./scripts/hooks/audit-session-start.sh",
        "powershell": "./scripts/hooks/audit-session-start.ps1",
        "comment": "Log session initialization"
      }
    ],
    "userPromptSubmitted": [
      {
        "type": "command",
        "bash": "./scripts/hooks/audit-prompt.sh",
        "powershell": "./scripts/hooks/audit-prompt.ps1",
        "comment": "Log user prompts"
      }
    ],
    "preToolUse": [
      {
        "type": "command",
        "bash": "./scripts/hooks/audit-tool-request.sh",
        "powershell": "./scripts/hooks/audit-tool-request.ps1",
        "comment": "Log tool invocation requests"
      }
    ],
    "postToolUse": [
      {
        "type": "command",
        "bash": "./scripts/hooks/audit-tool-result.sh",
        "powershell": "./scripts/hooks/audit-tool-result.ps1",
        "comment": "Log tool execution results"
      }
    ],
    "errorOccurred": [
      {
        "type": "command",
        "bash": "./scripts/hooks/audit-error.sh",
        "powershell": "./scripts/hooks/audit-error.ps1",
        "comment": "Log errors"
      }
    ],
    "sessionEnd": [
      {
        "type": "command",
        "bash": "./scripts/hooks/audit-session-end.sh",
        "powershell": "./scripts/hooks/audit-session-end.ps1",
        "comment": "Finalize session audit log"
      }
    ]
  }
}
```

**`scripts/hooks/audit-session-start.sh`:**
```bash
#!/bin/bash
INPUT=$(cat)
SOURCE=$(echo "$INPUT" | jq -r '.source')
TIMESTAMP=$(echo "$INPUT" | jq -r '.timestamp')

# Ensure log directory exists
mkdir -p logs/audit

# Write structured log entry
jq -n \
  --arg event "session_start" \
  --arg ts "$TIMESTAMP" \
  --arg source "$SOURCE" \
  --arg user "${USER:-unknown}" \
  '{event: $event, timestamp: $ts, source: $source, user: $user}' \
  >> logs/audit/agent-audit.jsonl
```

**`scripts/hooks/audit-tool-request.sh`:**
```bash
#!/bin/bash
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.toolName')
TOOL_ARGS=$(echo "$INPUT" | jq -r '.toolArgs')
TIMESTAMP=$(echo "$INPUT" | jq -r '.timestamp')

jq -n \
  --arg event "tool_request" \
  --arg ts "$TIMESTAMP" \
  --arg tool "$TOOL_NAME" \
  --arg args "$TOOL_ARGS" \
  --arg user "${USER:-unknown}" \
  '{event: $event, timestamp: $ts, tool: $tool, args: $args, user: $user}' \
  >> logs/audit/agent-audit.jsonl
```

**`scripts/hooks/audit-tool-result.sh`:**
```bash
#!/bin/bash
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.toolName')
RESULT_TYPE=$(echo "$INPUT" | jq -r '.toolResult.resultType')
TIMESTAMP=$(echo "$INPUT" | jq -r '.timestamp')

jq -n \
  --arg event "tool_result" \
  --arg ts "$TIMESTAMP" \
  --arg tool "$TOOL_NAME" \
  --arg result "$RESULT_TYPE" \
  '{event: $event, timestamp: $ts, tool: $tool, result: $result}' \
  >> logs/audit/agent-audit.jsonl

# Alert on failures
if [ "$RESULT_TYPE" = "failure" ]; then
  RESULT_TEXT=$(echo "$INPUT" | jq -r '.toolResult.textResultForLlm')
  echo "[ALERT] Tool failure: $TOOL_NAME - $RESULT_TEXT" >&2
fi
```

The resulting `logs/audit/agent-audit.jsonl` file contains one JSON object per line:

```jsonl
{"event":"session_start","timestamp":"1704614400000","source":"new","user":"developer"}
{"event":"tool_request","timestamp":"1704614600000","tool":"bash","args":"{\"command\":\"npm test\"}","user":"developer"}
{"event":"tool_result","timestamp":"1704614700000","tool":"bash","result":"success"}
{"event":"session_start","timestamp":"1704618000000","source":"resume","user":"developer"}
```

### Example 3: Code Quality Gates

A `postToolUse` hook that runs linting after file edits. It alerts when the agent introduces code that violates your standards:

**`scripts/hooks/quality-gate.sh`:**
```bash
#!/bin/bash
set -e

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.toolName')
RESULT_TYPE=$(echo "$INPUT" | jq -r '.toolResult.resultType')

# Only validate successful file edits
if [ "$RESULT_TYPE" != "success" ]; then
  exit 0
fi
if [ "$TOOL_NAME" != "edit" ] && [ "$TOOL_NAME" != "create" ]; then
  exit 0
fi

FILE_PATH=$(echo "$INPUT" | jq -r '.toolArgs' | jq -r '.path // empty')

# Only lint applicable file types
case "$FILE_PATH" in
  *.ts|*.tsx|*.js|*.jsx)
    if [ -f "$FILE_PATH" ]; then
      if ! npx eslint --quiet "$FILE_PATH" 2>/dev/null; then
        echo "[QUALITY] Lint errors introduced in $FILE_PATH" >> logs/quality.log
      fi
    fi
    ;;
  *.py)
    if [ -f "$FILE_PATH" ]; then
      if ! python -m ruff check "$FILE_PATH" 2>/dev/null; then
        echo "[QUALITY] Lint errors introduced in $FILE_PATH" >> logs/quality.log
      fi
    fi
    ;;
esac
```

### Example 4: Notification System

An `errorOccurred` hook that sends alerts to Slack when the agent encounters failures:

**`scripts/hooks/slack-alert.sh`:**
```bash
#!/bin/bash
INPUT=$(cat)
ERROR_MSG=$(echo "$INPUT" | jq -r '.error.message')
ERROR_NAME=$(echo "$INPUT" | jq -r '.error.name')
TIMESTAMP=$(echo "$INPUT" | jq -r '.timestamp')

# Format the timestamp
FORMATTED_TIME=$(date -d @$((TIMESTAMP / 1000)) '+%Y-%m-%d %H:%M:%S' 2>/dev/null || echo "$TIMESTAMP")

# Build Slack message payload
PAYLOAD=$(jq -n \
  --arg text ":warning: *Copilot Agent Error*\n*Type:* ${ERROR_NAME}\n*Message:* ${ERROR_MSG}\n*Time:* ${FORMATTED_TIME}\n*Repo:* ${GITHUB_REPOSITORY:-unknown}" \
  '{text: $text}')

# Send to Slack (webhook URL from environment)
if [ -n "$SLACK_WEBHOOK_URL" ]; then
  curl -s -X POST "$SLACK_WEBHOOK_URL" \
    -H 'Content-Type: application/json' \
    -d "$PAYLOAD" > /dev/null
fi
```

**`.github/hooks/notifications.json`:**
```json
{
  "version": 1,
  "hooks": {
    "errorOccurred": [
      {
        "type": "command",
        "bash": "./scripts/hooks/slack-alert.sh",
        "env": {
          "SLACK_WEBHOOK_URL": "${env:SLACK_WEBHOOK_URL}"
        },
        "timeoutSec": 10,
        "comment": "Send Slack alert on agent errors"
      }
    ],
    "sessionEnd": [
      {
        "type": "command",
        "bash": "./scripts/hooks/session-complete-notify.sh",
        "env": {
          "SLACK_WEBHOOK_URL": "${env:SLACK_WEBHOOK_URL}"
        },
        "timeoutSec": 10,
        "comment": "Notify team when agent session completes"
      }
    ]
  }
}
```

**⚠️ Never commit the webhook URL itself.** The `${env:SLACK_WEBHOOK_URL}` syntax above reads from the environment at hook execution time. Don't substitute the literal `https://hooks.slack.com/services/...` URL into the JSON. For the Copilot coding agent, store the webhook as an [Actions secret](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions) on the repository and expose it to the agent environment. For local CLI sessions, export it in your shell or a gitignored `.env` file. A Slack incoming webhook grants anyone who holds it the ability to post into your channel. Treat it like a credential.

### Example 5: Cost and Usage Tracking

Track every tool invocation for cost allocation and usage analysis:

**`scripts/hooks/usage-tracker.sh`:**
```bash
#!/bin/bash
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.toolName')
TIMESTAMP=$(echo "$INPUT" | jq -r '.timestamp')
USER=${USER:-unknown}
REPO=${GITHUB_REPOSITORY:-unknown}

# Append to CSV for easy analysis
mkdir -p logs/usage
echo "$TIMESTAMP,$USER,$REPO,$TOOL_NAME" >> logs/usage/tool-usage.csv
```

**`scripts/hooks/usage-summary.sh`** (runs at session end):
```bash
#!/bin/bash
INPUT=$(cat)
REASON=$(echo "$INPUT" | jq -r '.reason')
TIMESTAMP=$(echo "$INPUT" | jq -r '.timestamp')

USAGE_FILE="logs/usage/tool-usage.csv"

if [ -f "$USAGE_FILE" ]; then
  # Count tool invocations by type
  TOTAL=$(wc -l < "$USAGE_FILE")
  BASH_COUNT=$(grep -c ",bash$" "$USAGE_FILE" || echo 0)
  EDIT_COUNT=$(grep -c ",edit$" "$USAGE_FILE" || echo 0)
  VIEW_COUNT=$(grep -c ",view$" "$USAGE_FILE" || echo 0)
  CREATE_COUNT=$(grep -c ",create$" "$USAGE_FILE" || echo 0)

  jq -n \
    --arg event "session_summary" \
    --arg ts "$TIMESTAMP" \
    --arg reason "$REASON" \
    --argjson total "$TOTAL" \
    --argjson bash "$BASH_COUNT" \
    --argjson edit "$EDIT_COUNT" \
    --argjson view "$VIEW_COUNT" \
    --argjson create "$CREATE_COUNT" \
    '{event: $event, timestamp: $ts, reason: $reason, 
      tools: {total: $total, bash: $bash, edit: $edit, view: $view, create: $create}}' \
    >> logs/usage/session-summaries.jsonl
fi
```

---

## Multiple Hooks of the Same Type

Multiple hooks for the same event execute in array order. This allows separation of concerns: one hook for security, another for logging, a third for metrics:

```json
{
  "version": 1,
  "hooks": {
    "preToolUse": [
      {
        "type": "command",
        "bash": "./scripts/hooks/security-check.sh",
        "comment": "Security validation — runs first, can deny"
      },
      {
        "type": "command",
        "bash": "./scripts/hooks/audit-log.sh",
        "comment": "Audit logging — runs second"
      },
      {
        "type": "command",
        "bash": "./scripts/hooks/metrics.sh",
        "comment": "Metrics collection — runs third"
      }
    ]
  }
}
```

If any `preToolUse` hook returns `deny`, the tool call is blocked. Place security hooks first in the array for clarity, and audit/logging hooks after.

---

## Script Best Practices

### Reading Input

All hooks receive JSON on stdin. Read it into a variable, then parse with `jq` (Bash) or `ConvertFrom-Json` (PowerShell):

**Bash:**
```bash
#!/bin/bash
INPUT=$(cat)
TIMESTAMP=$(echo "$INPUT" | jq -r '.timestamp')
CWD=$(echo "$INPUT" | jq -r '.cwd')
```

**PowerShell:**
```powershell
$input = [Console]::In.ReadToEnd() | ConvertFrom-Json
$timestamp = $input.timestamp
$cwd = $input.cwd
```

### Producing Output (preToolUse Only)

Output must be valid JSON on a single line. Use `jq -c` in Bash or `ConvertTo-Json -Compress` in PowerShell:

**Bash:**
```bash
# Static deny
echo '{"permissionDecision":"deny","permissionDecisionReason":"Policy violation"}' | jq -c

# Dynamic deny with variable
REASON="File outside allowed directories"
jq -n --arg reason "$REASON" '{permissionDecision: "deny", permissionDecisionReason: $reason}'
```

**PowerShell:**
```powershell
@{
    permissionDecision = "deny"
    permissionDecisionReason = "Policy violation"
} | ConvertTo-Json -Compress
```

### Error Handling

Always handle errors gracefully. A crashing hook should not block the agent:

```bash
#!/bin/bash
set -e  # Exit on error

INPUT=$(cat)
# ... process input ...

# Exit 0 for success — non-zero exits are treated as hook failures
exit 0
```

### Keep Hooks Fast

Hooks run synchronously and block agent execution. Every millisecond of hook time is time the user waits.

| Guideline | Target |
|-----------|--------|
| Typical hook execution | Under 5 seconds |
| Maximum timeout | 30 seconds (default), configurable via `timeoutSec` |
| File I/O | Append to files (don't rewrite) |
| Network calls | Use timeouts, prefer async/fire-and-forget |
| Expensive operations | Offload to background processes |

```bash
#!/bin/bash
# ✅ Fast: append to file
echo "$LOG_ENTRY" >> logs/audit.jsonl

# ❌ Slow: rewrite entire file
cat logs/audit.jsonl | jq '. + [newEntry]' > logs/audit.jsonl.tmp && mv logs/audit.jsonl.tmp logs/audit.jsonl

# ✅ Fast: fire-and-forget network call
curl -s -X POST "$WEBHOOK_URL" -d "$PAYLOAD" &

# ❌ Slow: synchronous network call with retries
curl --retry 3 --retry-delay 5 "$WEBHOOK_URL" -d "$PAYLOAD"
```

---

## Security Considerations

Hooks execute shell commands with access to the repository and environment. Treat them with the same care as CI scripts.

| Concern | Recommendation |
|---------|----------------|
| **Input validation** | Always validate and sanitize JSON input. Untrusted data could lead to command injection. |
| **Shell escaping** | Use `jq` to construct commands rather than string interpolation. Prevents injection vulnerabilities. |
| **Secrets in logs** | Never log tokens, passwords, or API keys. Audit your log output. |
| **File permissions** | Hook scripts should be executable (`chmod +x`) but not world-writable. Lock down log directories. |
| **External calls** | Network calls introduce latency, failure modes, and potential data exposure. Use timeouts and consider what data is sent. |
| **Resource exhaustion** | Set appropriate `timeoutSec` values. A runaway hook blocks the entire agent session. |

---

## Where Hooks Overlap with Primitives

Hooks and the other primitives sometimes address the same concern from different angles. The table below shows where each rule belongs.

### Coding Standards

| Approach | Mechanism | Effect |
|----------|-----------|--------|
| Always-on instructions | "Use parameterized queries for all database calls" | Copilot generates code using parameterized queries |
| `preToolUse` hook | Block edits containing string concatenation in SQL | Prevents the agent from saving code that violates the rule |

**Use both.** Instructions produce correct code proactively. Hooks catch what slips through.

### File Access Control

| Approach | Mechanism | Effect |
|----------|-----------|--------|
| File-based instructions | Guidance for *how* to edit files matching a pattern | Copilot follows conventions for those files |
| `preToolUse` hook | Deny edits to files *outside* allowed directories | Hard-blocks unauthorized file modifications |

Instructions say "when editing these files, follow these rules." Hooks say "you may not edit those files at all."

### External Integrations

| Approach | Mechanism | Effect |
|----------|-----------|--------|
| MCP server | Gives Copilot a tool it can call during reasoning | Copilot can query a database, create a Jira ticket, etc. |
| Hook (e.g., `postToolUse`) | Runs a shell script the agent doesn't see or control | Sends a Slack notification after the agent does something |

MCP extends what Copilot can *do*. Hooks monitor what Copilot *did*.

### Security Rules

| Approach | Mechanism | Effect |
|----------|-----------|--------|
| Instructions | "Never use `eval()`, never hardcode secrets" | Advisory — the model follows this most of the time |
| `preToolUse` hook | Block shell commands matching dangerous patterns | Enforcement — the command is physically prevented |

Instructions reduce the frequency of violations. Hooks eliminate them.

### Summary: Use Primitives for Guidance, Hooks for Enforcement

```
┌─────────────────────────────────────────────────┐
│              Copilot's Mind                      │
│                                                  │
│  Instructions ──► "I should do X"               │
│  Skills       ──► "I know how to do X"          │
│  Agents       ──► "I am an expert in X"         │
│  Prompts      ──► "The user wants X"            │
│  MCP          ──► "I can call X"                │
│                                                  │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼  (Agent decides to take an action)
                       │
┌──────────────────────┼──────────────────────────┐
│              Hooks Layer                         │
│                                                  │
│  preToolUse   ──► "Is this action allowed?"     │
│  postToolUse  ──► "What happened?"              │
│  errorOccurred──► "Something went wrong"        │
│                                                  │
│  The model doesn't see or control this layer.    │
└─────────────────────────────────────────────────┘
```

---

## Debugging Hooks

### Enable Verbose Logging

Add debug output to stderr (stdout is reserved for JSON output in `preToolUse`):

```bash
#!/bin/bash
set -x  # Enable bash debug mode — outputs to stderr
INPUT=$(cat)
echo "DEBUG: Received input" >&2
echo "$INPUT" >&2
# ... rest of script
```

### Test Hooks Locally

Pipe test JSON into your hook script to validate behavior before committing:

```bash
# Test a preToolUse hook with a dangerous command
echo '{"timestamp":1704614600000,"cwd":"/tmp","toolName":"bash","toolArgs":"{\"command\":\"rm -rf /\"}"}' \
  | ./scripts/hooks/security-check.sh

# Check exit code
echo "Exit code: $?"

# Validate output is valid JSON
echo '{"timestamp":1704614600000,"cwd":"/tmp","toolName":"edit","toolArgs":"{\"path\":\"src/app.ts\"}"}' \
  | ./scripts/hooks/security-check.sh | jq .
```

### The `/troubleshoot` Command

VS Code 1.111+ includes the `/troubleshoot` slash command, which analyzes agent debug logs directly in chat. Use it to diagnose why a hook fired unexpectedly, why an instruction was ignored, or why a response was slow. It works with both current and past session logs, so it's a reasonable first stop when hooks behave differently than expected.

### Agent Debug Logs

VS Code 1.116 merges the previously separate "current session" and "historical session" debug log commands into a single **Chat: Show Agent Debug Logs** entry point. Open it from the Command Palette to browse logs from any agent session, current or past. The logs show every tool call, hook invocation, and context loading event in chronological order. Pair it with `/troubleshoot` to trace how hooks, instructions, and skills interacted during a session.

### Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| Hooks not executing | File not in `.github/hooks/` or not on default branch | Verify path and merge to default branch |
| Invalid JSON errors | Output not on a single line | Use `jq -c` (Bash) or `ConvertTo-Json -Compress` (PowerShell) |
| Hook timing out | Script exceeds default 30s timeout | Increase `timeoutSec` or optimize script |
| Permission denied | Script not executable | Run `chmod +x script.sh`, verify shebang line |
| Hook crashes silently | Unhandled errors in script | Add `set -e` and error logging to stderr |

---

## Cookbook: Common Patterns

### Pattern: Production Branch Protection

Block any shell commands that could affect production:

```bash
#!/bin/bash
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.toolName')

if [ "$TOOL_NAME" = "bash" ]; then
  COMMAND=$(echo "$INPUT" | jq -r '.toolArgs' | jq -r '.command')

  # Block production-targeting commands
  if echo "$COMMAND" | grep -qiE "production|prod-db|deploy.*prod|push.*main"; then
    echo '{"permissionDecision":"deny","permissionDecisionReason":"Production-affecting commands require manual execution"}'
    exit 0
  fi
fi
```

### Pattern: File Change Budget

Limit the number of files the agent can modify in a single session:

```bash
#!/bin/bash
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.toolName')
MAX_FILES=20
COUNTER_FILE="/tmp/copilot-edit-count"

if [ "$TOOL_NAME" = "edit" ] || [ "$TOOL_NAME" = "create" ]; then
  # Initialize or read counter
  COUNT=$(cat "$COUNTER_FILE" 2>/dev/null || echo 0)
  COUNT=$((COUNT + 1))

  if [ "$COUNT" -gt "$MAX_FILES" ]; then
    echo "{\"permissionDecision\":\"deny\",\"permissionDecisionReason\":\"Edit limit reached ($MAX_FILES files). Review changes before continuing.\"}"
    exit 0
  fi

  echo "$COUNT" > "$COUNTER_FILE"
fi
```

### Pattern: Secret Scanning Prevention

Block commands that could leak credentials or expose secrets to the terminal output:

```bash
#!/bin/bash
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.toolName')

if [ "$TOOL_NAME" = "bash" ]; then
  COMMAND=$(echo "$INPUT" | jq -r '.toolArgs' | jq -r '.command')

  # Block commands that dump environment or read secret files
  if echo "$COMMAND" | grep -qiE \
    'printenv|\benv\b|cat.*\.env|echo.*\$(.*SECRET|TOKEN|PASSWORD|API_KEY)|aws configure list|gcloud auth print-access-token'; then
    echo '{"permissionDecision":"deny","permissionDecisionReason":"Blocked: command may expose secrets or credentials"}'
    exit 0
  fi

  # Block piping secrets to files or network
  if echo "$COMMAND" | grep -qiE '(SECRET|TOKEN|PASSWORD|API_KEY).*\|.*(curl|wget|nc |tee )'; then
    echo '{"permissionDecision":"deny","permissionDecisionReason":"Blocked: potential secret exfiltration detected"}'
    exit 0
  fi
fi
```

Pair this with GitHub's built-in secret scanning for defense in depth. Hooks catch runtime exposure; secret scanning catches committed credentials.

### Pattern: Deployment Gate Validation

Enforce deployment readiness checks before the agent can execute deploy-related commands. Autonomous agents still follow release procedures this way:

```bash
#!/bin/bash
# Deployment Gate — adapt the test and audit commands to your stack.
# This example uses npm; replace with pytest, go test, cargo test, etc.
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.toolName')

if [ "$TOOL_NAME" = "bash" ]; then
  COMMAND=$(echo "$INPUT" | jq -r '.toolArgs' | jq -r '.command')

  # Detect deployment commands
  if echo "$COMMAND" | grep -qiE "deploy|kubectl apply|terraform apply|helm upgrade|git push.*main"; then

    # Gate 1: Tests must pass (adapt to your test runner)
    if ! npm test --silent 2>/dev/null; then
      echo '{"permissionDecision":"deny","permissionDecisionReason":"Deployment blocked: tests must pass before deploying"}'
      exit 0
    fi

    # Gate 2: No high-severity vulnerabilities (adapt to your audit tool)
    if npm audit --production 2>/dev/null | grep -q "high\|critical"; then
      echo '{"permissionDecision":"deny","permissionDecisionReason":"Deployment blocked: resolve high/critical vulnerabilities first"}'
      exit 0
    fi

    # Gate 3: Log the deployment attempt
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ),deploy-attempt,$COMMAND" >> logs/deployment-audit.csv
  fi
fi
```

This hook pattern-matches deployment commands regardless of method (Kubernetes, Terraform, direct pushes). Replace `npm test` and `npm audit` with your project's test runner and security scanner. Pair it with an [SRE custom agent](primitive-5-custom-agents.md#additional-agent-examples) that knows your deployment procedures.

### Pattern: Keyword Alerting on Prompts

Flag prompts mentioning sensitive topics:

```bash
#!/bin/bash
INPUT=$(cat)
PROMPT=$(echo "$INPUT" | jq -r '.prompt')

SENSITIVE_KEYWORDS="production|credentials|password|secret|deploy|rollback|delete"

if echo "$PROMPT" | grep -qiE "$SENSITIVE_KEYWORDS"; then
  MATCHED=$(echo "$PROMPT" | grep -oiE "$SENSITIVE_KEYWORDS" | head -1)
  echo "[ALERT] Sensitive keyword '$MATCHED' in prompt" >> logs/alerts.log
  # Optionally fire a webhook here
fi
```

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It's Problematic | Better Approach |
|--------------|---------------------|------------------|
| **Using hooks instead of instructions** | Hooks can only deny actions; they can't guide *how* to write code | Use instructions for guidance, hooks for enforcement |
| **Slow network calls in hooks** | Blocks agent execution; user waits for every tool call | Fire-and-forget (`curl ... &`) or batch and send at session end |
| **Logging secrets** | Audit logs may be persisted or shared | Filter sensitive fields before logging |
| **No timeout configuration** | Default 30s may be too long or too short | Set `timeoutSec` appropriate to each hook's operation |
| **Overly broad deny rules** | Blocking too many commands makes the agent ineffective | Be precise in pattern matching; test against real agent workflows |
| **Ignoring PowerShell** | Hooks fail silently on Windows if only `bash` is defined | Always provide both `bash` and `powershell` variants |
| **Hooks not on default branch** | Coding agent only loads hooks from the default branch | Merge hook configurations before testing with the agent |

---

## Using Hooks with GitHub Copilot CLI

Hooks work in both the coding agent (on GitHub) and **[GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli)** (in the terminal). The behavior is identical, with one key difference in how hooks are loaded:

| Aspect | Coding Agent | Copilot CLI |
|--------|-------------|-------------|
| **Hook source** | Default branch of the repository | Current working directory |
| **When loaded** | At session start (from remote) | At session start (from local) |
| **Updates** | Requires merge to default branch | Immediate (reads local files) |

This means you can test hooks locally with Copilot CLI before merging them to the default branch for the coding agent:

```bash
# 1. Create your hook file locally
mkdir -p .github/hooks
cat > .github/hooks/test-hook.json << 'EOF'
{
  "version": 1,
  "hooks": {
    "preToolUse": [
      {
        "type": "command",
        "bash": "echo 'Hook fired!' >&2",
        "powershell": "Write-Host 'Hook fired!'"
      }
    ]
  }
}
EOF

# 2. Start a Copilot CLI session — the hook fires immediately
# (Use the appropriate CLI command for your installation)

# 3. Once satisfied, commit and merge for the coding agent
git add .github/hooks/test-hook.json
git commit -m "Add preToolUse security hook"
git push
```

---

## VS Code Hooks (Chat Agent Sessions)

Hooks are supported in [VS Code Chat agent sessions](https://code.visualstudio.com/docs/copilot/customization/hooks) (VS Code 1.109.3+), extending coverage beyond the coding agent and Copilot CLI.

**See it in action:** [Let it Cook: Agent Steering, Queueing, Hooks, CLI Integration, & more!](https://www.youtube.com/watch?v=FjvtWeG6EEo&t=1969s). Pierce Boggan opens a `.github/hooks/` configuration in VS Code showing `sessionStart`, `userPromptSubmit`, and `toolUse` events wired to shell commands, then triggers them live from chat.

VS Code hooks use **file-based configuration** in `.github/hooks/*.json` (and other config file locations). They support eight PascalCase event types, a different set from the coding agent's six events:

### Event Types

| Event | Fires When | Coding Agent Equivalent |
|-------|-----------|------------------------|
| `SessionStart` | Chat agent session begins | `sessionStart` |
| `UserPromptSubmit` | User submits a prompt | `userPromptSubmitted` |
| `PreToolUse` | Before a tool call | `preToolUse` |
| `PostToolUse` | After a tool call completes | `postToolUse` |
| `PreCompact` | Before context window compaction | *VS Code only* |
| `SubagentStart` | Before a sub-agent is invoked | *VS Code only* |
| `SubagentStop` | After a sub-agent completes | *VS Code only* |
| `Stop` | When the agent stops execution | *VS Code only* |

VS Code hooks do not include `sessionEnd` or `errorOccurred` from the coding agent event model. The four VS Code-only event types address gaps in the coding agent hook model:

- **PreCompact** fires before the context window is compacted (trimmed to fit), enabling snapshots of the full context before information is lost
- **SubagentStart/SubagentStop** fire when the main agent spawns sub-agents, giving visibility into delegation boundaries
- **Stop** fires when the agent halts execution, whether from completion, user cancellation, or error

### Configuration

VS Code hooks are configured in file-based JSON. The primary shared location is `.github/hooks/*.json` — the same directory used by the coding agent and CLI. Additional configuration locations (in order of precedence):

- `.github/hooks/*.json` (workspace, shared — version-controlled)
- `.claude/settings.local.json` (workspace, local — git-ignored)
- `.claude/settings.json` (workspace)
- `~/.claude/settings.json` (user-level)

```jsonc
// .github/hooks/security.json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "./scripts/hooks/security-check.sh",
        "timeout": 10
      }
    ]
  }
}
```

VS Code hooks use `command` and `timeout` properties (not `bash`/`powershell` and `timeoutSec` as in the coding agent). The `.github/hooks/` location is compatible with both systems, and the JSON input/output protocol is the same — existing scripts work across both environments.

VS Code hooks also support additional output fields beyond the coding agent's `permissionDecision`/`permissionDecisionReason`. PreToolUse hooks can return `hookSpecificOutput` with `updatedInput` (to modify tool arguments) and `additionalContext` (to inject context). Exit code semantics differ as well: 0 = success, 2 = blocking error, any other code = non-blocking warning.

### Coding Agent vs. VS Code Hooks Comparison

| Aspect | Coding Agent / CLI | VS Code Chat |
|--------|-------------------|--------------|
| **Configuration** | `.github/hooks/*.json` | `.github/hooks/*.json` or Claude Code config files |
| **Event naming** | camelCase (`preToolUse`) | PascalCase (`PreToolUse`) |
| **Event count** | 6 events | 8 events (adds UserPromptSubmit, PreCompact, SubagentStart/Stop, Stop; does not include sessionEnd or errorOccurred) |
| **Hook properties** | `bash`/`powershell`, `timeoutSec` | `command`, `timeout` |
| **Script format** | Same (JSON stdin, JSON stdout for PreToolUse) | Same |
| **Sharing** | Version-controlled in repo | Version-controlled in repo (`.github/hooks/`) or local config files |

### Agent-Scoped Hooks

Hooks can be scoped to a specific custom agent by defining them directly in the agent's `.agent.md` YAML frontmatter using the `hooks:` field. These hooks execute only when that agent is active — they do not affect other agents or general chat interactions.

This requires the `chat.useCustomAgentHooks` setting to be enabled (Preview).

```yaml
---
name: 'Security Reviewer'
description: 'Reviews code for security vulnerabilities'
tools: ['search', 'readFile', 'usages']
hooks:
  PreToolUse:
    - type: command
      command: "./scripts/hooks/security-audit.sh"
      timeout: 15
---
```

Agent-scoped hooks attach enforcement or logging to a specific workflow without adding noise to every chat session. A security reviewer agent might audit every file read. A deployment agent might block production commands.

### When to Use Which

- **Coding agent hooks** (`.github/hooks/*.json`) for enforcement that must apply to automated agent sessions on GitHub — security policies, compliance auditing, CI-level guardrails
- **VS Code hooks** (`.github/hooks/*.json` or config files) for local development workflow enforcement — personal audit trails, local security checks, sub-agent monitoring
- **Agent-scoped hooks** (`.agent.md` frontmatter) for hooks that should only fire when a specific custom agent is active — targeted auditing, agent-specific guardrails
- **Both** when the same policies should apply everywhere — write scripts once in `.github/hooks/`, which is compatible with both systems

---

## Limitations and Failure Modes

Hooks are a local enforcement mechanism, not a server-side policy system. Know the boundaries before relying on them:

| Limitation | Detail |
|-----------|--------|
| **Local enforcement only** | Hooks run in VS Code, Copilot CLI, and the coding agent. They do not prevent direct file edits, IDE actions outside agent mode, or changes made through other tools |
| **Fail-closed on `preToolUse`** | If a `preToolUse` hook script exits with a non-zero code (crash, syntax error, unhandled exception), the tool call is **blocked**. This is safe by default but can stall the agent if hook scripts are unreliable |
| **Timeout behavior** | If a hook exceeds its `timeoutSec`, it is killed and treated as a failure. For `preToolUse`, this means the tool call is blocked. Set timeouts appropriate to each hook's operation |
| **Not a substitute for server-side policy** | Hooks run in the agent's environment. They complement, but do not replace, GitHub enterprise policies, branch protection rules, and CI checks |
| **Cloud coding agent reads from default branch only** | Hook files must be merged to the default branch before the cloud agent uses them. Work-in-progress hooks on feature branches have no effect on cloud agent sessions |

Design hooks as a defense-in-depth layer that works alongside other controls, not as the sole enforcement mechanism.

---

## Further Reading

- [About hooks](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-hooks) — Conceptual overview and hook types
- [Using hooks with GitHub Copilot agents](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/use-hooks) — Step-by-step setup guide
- [Hooks configuration reference](https://docs.github.com/en/copilot/reference/hooks-configuration) — Full input/output schemas, advanced patterns, and example use cases
- [About GitHub Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent) — Context on the coding agent that hooks extend
- [About GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) — The terminal surface where hooks also apply

---

[← MCP](primitive-6-mcp.md) | [Next: Copilot Memory →](primitive-8-memory.md)
