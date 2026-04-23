# Primitive 7: Hooks

[← Back to The Eight Primitives](part-2-primitives.md) | [← MCP](primitive-6-mcp.md) | [Next: Memory →](primitive-8-memory.md)

*Updated: April 22, 2026.*

---

## Where It Enters the Loop

Hooks do not enter the model's reasoning context. They sit around execution.

That is the defining trait of this primitive.

Instructions, Prompts, Skills, Agents, and MCP all shape what the loop knows or can attempt. Hooks operate after the model has already decided to do something and the runtime is about to execute, has executed, or has hit an error boundary.

That is why Hooks are the enforcement primitive.

## Surface Reality

Hooks are not an IDE-wide baseline primitive.

In VS Code, the current canonical reference is [Agent hooks in Visual Studio Code](https://code.visualstudio.com/docs/copilot/customization/hooks), which also documents the preview status and current lifecycle events.

In current official guidance, VS Code hooks are a preview feature. Hooks are also part of the GitHub Copilot CLI and Cloud Coding Agent story. They are not the normal path in JetBrains IDEs, Visual Studio, Eclipse, or Xcode.

That matters because rollout advice changes by surface. A VS Code, CLI, or Cloud Coding Agent team can use Hooks as a live enforcement layer. A mixed-IDE team still needs instructions, CI, and repository protections as the broader baseline.

## What This Primitive Is For

Use Hooks when the team needs runtime control rather than better advice.

Typical examples:

- deny dangerous shell invocations,
- restrict edits to allowed directories,
- log tool activity for audit,
- notify downstream systems when sensitive operations happen,
- track agent-session lifecycle events,
- or attach compliance checks to execution boundaries.

The question Hooks answer is: "What should happen around the action, regardless of how the model reasoned its way there?"

## What This Looks Like in Practice

Without Hooks, a repository can say "do not run destructive commands against production." The model may follow that rule. It may also misunderstand it.

With Hooks, the runtime can inspect the attempted action and deny it, require approval, rewrite the input, log it, or force additional validation before the session ends.

That is the practical difference. Hooks do not ask the model to remember a rule. They run code at execution boundaries.

## Why Hooks Are Different from Instructions

Instructions can say, "Do not print secrets."

Hooks can inspect a tool invocation and deny it.

That does not make Hooks magical or complete security in a box. It does make them fundamentally different from every primitive that relies on the model to follow guidance.

This distinction is one of the most important in the entire guide.

## Hooks Are Tripwires, Not Total Containment

The current guide makes an important point that this guide preserves: Hooks are strong operational controls, but not absolute containment.

They can block known-bad paths. They can log high-signal behavior. They can create a last line of defense. They do not remove the need for proper credentials, repository protections, scoped tokens, and runtime sandboxing.

The right mental model is defense in depth, not perfect denial.

## Where Hooks Attach

Current VS Code guidance exposes eight lifecycle events:

- `SessionStart`,
- `UserPromptSubmit`,
- `PreToolUse`,
- `PostToolUse`,
- `PreCompact`,
- `SubagentStart`,
- `SubagentStop`,
- and `Stop`.

That is why they belong in the loop chapter as much as in their own primitive chapter. Hooks are easiest to understand once the reader already sees the runtime as a repeated chain of decisions and actions.

## What Hooks Can Actually Influence

Hooks can do more than deny a command.

They can:

- inject additional context at session start,
- change approval behavior for a specific tool call,
- rewrite tool input before execution,
- add follow-up context after a tool returns,
- observe subagent boundaries,
- and block stop or compaction transitions until required work is done.

That broader control plane is why stale event or field documentation is so dangerous. It understates what the primitive can actually do.

## The Smallest Working Path

Start with one safe event and one visible effect.

```json
{
	"hooks": {
		"PostToolUse": [
			{
				"type": "command",
				"command": "npx prettier --write \"$TOOL_INPUT_FILE_PATH\"",
				"windows": "powershell -Command \"npx prettier --write $env:TOOL_INPUT_FILE_PATH\""
			}
		]
	}
}
```

Save the file under `.github/hooks/format.json`, trigger one file edit, and then check the `GitHub Copilot Chat Hooks` output channel.

Success looks like a visible hook run tied to the tool event you expected. Failure usually comes from one of four things:

- the file is in the wrong location,
- the event name is wrong,
- the command cannot run in the active runtime,
- or the runtime never reached that event in the first place.

Only after that works should the team move to deny rules, approval shaping, or audit integrations.

## What Good Hook Usage Looks Like

Good Hook usage is targeted and operationally justified.

Examples:

- block known-dangerous command patterns,
- record structured audit events,
- restrict writes outside a safe workspace area,
- capture error patterns for incident review.

Weak Hook usage tries to express broad natural-language policy through brittle denial logic or treats Hooks as a replacement for infrastructure controls.

For CLI-heavy teams, Hooks are often most legible here because the runtime is already command-centric. That makes approval shaping, deny lists, and audit output easier to reason about. It also raises the cost of mistakes when headless or lower-friction execution is enabled, which is exactly why the policy needs to stay narrow and explicit.

Frontend and QA teams can use the same primitive for practical gates, not just security policy. A hook can require lint or test verification after large UI edits, block risky writes to generated design-token outputs, or record whether a test gate actually ran.

## How It Composes with Other Primitives

| Primitive | Relationship |
|-----------|--------------|
| [Always-on Instructions](primitive-1-always-on-instructions.md) | Tell the model what it should avoid |
| [MCP](primitive-6-mcp.md) | Makes enforcement more important because the loop can reach real systems |
| [Custom Agents](primitive-5-custom-agents.md) | Can narrow the situations where risky tools are even available |
| [Code Review](code-review.md) | Complements static and review-time guidance with runtime controls |

## The Most Important Use Case

Hooks matter most when the cost of a bad action is materially higher than the cost of a bad answer.

That is the dividing line.

If a wrong explanation is the problem, improve instructions or task framing.
If a wrong command, edit, or external action is the problem, Hooks become relevant.

## Where Hooks Fail as a Security Boundary

Hooks are strong runtime controls. They are not clean containment.

Three limits matter in practice:

- If the agent can edit the scripts a hook runs, the boundary is weaker than it looks.
- If the runtime itself has broad credentials, a denied tool call may still leave too much power elsewhere in the system.
- If the repo is public or broadly shared, `.github/hooks/*.json` is executable configuration and should be reviewed like automation code, not like prose.

That is why the right operating model includes ownership, false-positive handling, and a break-glass path.

Typical production questions are boring on purpose:

- Who owns deny rules?
- Where do audit events go?
- What is the escalation path when a legitimate task is blocked?
- When should CI or branch protection carry the rule instead of a local hook?

Those questions matter more than clever hook logic.

## Remote and Ephemeral Runtimes

When Hooks run in a remote workspace, container, Codespace, CLI automation, or Cloud Coding Agent environment, the enforcement still exists, but the assumptions change.

- The command runs where that runtime lives, not necessarily on the workstation.
- Logs and helper scripts must exist in that runtime.
- Ephemeral environments reward repo-owned setup and visible validation because drift is harder to debug after the session ends.

This is one reason remote-first teams should keep hook behavior easy to inspect and easy to recreate from source control.

## See It in Action

**See it in action:** [Let it cook: Agent Steering, Queueing, Hooks, CLI Integration, & more!](https://www.youtube.com/watch?v=FjvtWeG6EEo&t=1975s) — Pierce Boggan demos hooks wired to agent lifecycle events through `.github/hooks` definitions for session start, tool use, and stop behavior.

## Creating Hooks

In VS Code, run `/create-hook` in Chat to scaffold `.github/hooks/*.json` with the correct structure. There is no dedicated GUI editor for hooks. Describe the hook in plain English and let GitHub Copilot write the JSON.

> 💬 **Try this prompt:**
> "Create a `.github/hooks/protect-secrets.json` hook that uses `PreToolUse` to deny shell commands that print common secret environment variables or read `.env` files. Log denied attempts to `logs/secret-policy.jsonl`."

## Getting Started

### Step 1: Create the hook file

```
.github/
└── hooks/
    └── my-first-hook.json
```

### Step 2: Add the template

```json
{
  "hooks": {
    "SessionStart": [],
    "PreToolUse": [],
    "PostToolUse": [],
    "Stop": []
  }
}
```

### Step 3: Configure a hook

This minimal example logs every session start:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "type": "command",
        "command": "echo \"Session started: $(date)\" >> logs/session.log",
        "windows": "powershell -Command \"Add-Content -Path logs/session.log -Value \\\"Session started: $(Get-Date)\\\"\""
      }
    ]
  }
}
```

### Step 4: Commit and merge

For the Copilot Cloud Coding Agent, hooks are only loaded from the default branch. For GitHub Copilot CLI, hooks load from the current working directory immediately.

## The Hook Lifecycle

```
Session Start
  → User Prompt Submit
    → Agent Reasoning Loop
      → PreToolUse  (can DENY)
      → Tool Executes
      → PostToolUse (observe result)
      → (repeats for each tool)
    → SubagentStart / SubagentStop
    → PreCompact
  → Stop
```

### The Eight Lifecycle Events

| Hook | Fires When | Can Block? | Primary Use Cases |
|------|-----------|------------|-------------------|
| `SessionStart` | Session begins or resumes | No | Environment setup, session logging |
| `UserPromptSubmit` | User sends a message | No | Audit logging, keyword alerting |
| `PreToolUse` | Before any tool call | **Yes** | Security policies, command blocking, file access control |
| `PostToolUse` | After a tool completes | Can block follow-on | Statistics, failure alerts, audit trails |
| `PreCompact` | Before context compaction | No | Save context state before summarization |
| `SubagentStart` | Before a subagent launches | No | Track delegated work |
| `SubagentStop` | After a subagent completes | Can block completion | Validate subagent output |
| `Stop` | Session is about to end | Can block completion | Require final validation before stopping |

`PreToolUse` is the primary enforcement point. Return JSON to deny:

```json
{
  "permissionDecision": "deny",
  "permissionDecisionReason": "Destructive operations require approval"
}
```

If the hook produces no output, the tool call is **allowed by default**.

## Configuration Format

Every hook file requires a `hooks` object with arrays of hook definitions:

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

All `.json` files in `.github/hooks/` are loaded. A repository can contain multiple hook files organized by purpose (security, audit, notifications).

### Monorepo discovery

VS Code 1.111+ discovers hooks from parent folders up to the repository root. Root-level hooks enforce org-wide policies; package-level hooks handle context-specific concerns:

```
my-monorepo/
├── .github/hooks/security.json       # Applies to ALL packages
├── packages/frontend/.github/hooks/lint.json
└── packages/backend/.github/hooks/db-check.json
```

## Production Example

```json
{
  "hooks": {
    "SessionStart": [
      {
        "type": "command",
        "command": "./scripts/hooks/session-start.sh",
        "windows": "./scripts/hooks/session-start.ps1",
        "timeout": 10
      }
    ],
    "PreToolUse": [
      {
        "type": "command",
        "command": "./scripts/hooks/security-check.sh",
        "windows": "./scripts/hooks/security-check.ps1",
        "timeout": 15
      }
    ],
    "PostToolUse": [
      {
        "type": "command",
        "command": "cat >> logs/tool-results.jsonl",
        "windows": "powershell -Command \"$input | Add-Content -Path logs/tool-results.jsonl\""
      }
    ],
    "Stop": [
      {
        "type": "command",
        "command": "./scripts/hooks/cleanup.sh",
        "windows": "./scripts/hooks/cleanup.ps1",
        "timeout": 60
      }
    ]
  }
}
```

## Hook Input and Output

Every hook receives JSON on stdin describing the event. All events include `timestamp` and `cwd`.

**PreToolUse input:**

```json
{
  "timestamp": 1704614600000,
  "cwd": "/path/to/project",
  "tool_name": "bash",
  "tool_input": { "command": "rm -rf dist" },
  "tool_use_id": "abc123"
}
```

**PreToolUse output fields:**

| Field | Values | Effect |
|-------|--------|--------|
| `permissionDecision` | `"allow"`, `"deny"` | Allow or block the tool call |
| `permissionDecisionReason` | string | Explanation shown to the agent |
| `updatedInput` | object | Rewrite the tool input before execution |
| `additionalContext` | string | Inject context for the next model turn |

**PostToolUse** can also return `decision` and `reason` to block follow-on processing, and `hookSpecificOutput.additionalContext` to feed validation results back to the model.

## When to Use Hooks vs. Other Enforcement

| Scenario | Why Instructions Are Not Enough | What Hooks Add |
|----------|--------------------------------|----------------|
| **Compliance auditing** | Instructions do not produce logs | Every hook type can write audit trails |
| **Blocking dangerous commands** | "Don't run `rm -rf /`" is advisory | `PreToolUse` blocks the command before execution |
| **Restricting file access** | File-based instructions guide *how* to edit, not *whether* | `PreToolUse` can deny edits outside allowed directories |
| **External notifications** | No primitive monitors the agent's own actions | Hooks can send Slack alerts or webhooks on any event |

## Where to Read Next

- Read [Memory](primitive-8-memory.md) next for the other non-standard primitive in the set: learned context rather than authored files.
- Revisit [The Agent Loop](agent-loop.md) if the distinction between guidance and enforcement still feels blurry.
