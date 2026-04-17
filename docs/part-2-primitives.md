# Part II: The Primitives

[← Back to Guide](../ReadMe.md) | [← Part I: Foundations](part-1-foundations.md)

*Updated: April 17, 2026 · Validated against VS Code 1.116 and GitHub Copilot docs as of April 16, 2026.*

---

GitHub Copilot provides eight customization primitives that shape what Copilot knows and how it thinks. The first six (always-on instructions, file-based instructions, prompts, skills, custom agents, and MCP) handle context and capabilities. The remaining two extend into enforcement and learning: [Hooks](primitive-7-hooks.md) provide runtime enforcement, and [Copilot Memory](primitive-8-memory.md) provides automatic repository-level learning.

Beyond the primitives, two **platform extensions** take Copilot into new environments: [Agentic Workflows](agentic-workflows.md) run coding agents in GitHub Actions, and the [Copilot SDK](copilot-sdk.md) lets teams embed the agent runtime in their own tools. These aren't configuration primitives. They don't shape what Copilot knows about your codebase, but they consume the primitives you've defined. [Copilot code review](code-review.md) is a third cross-cutting feature: it reads your instruction files and surfaces convention violations as PR comments.

These mechanisms work across multiple Copilot surfaces: VS Code, Visual Studio, GitHub.com, and [GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) (a terminal-based AI agent). Because the primitives are plain files in your repository, any surface that reads `.github/` customization can consume them regardless of where they were authored. The tables below note each primitive's location, activation, scope, and CLI support.

| Mechanism | Location | When Loaded | Scope | CLI Support |
|-----------|----------|-------------|-------|-------------|
| [**Always-on Instructions**](primitive-1-always-on-instructions.md) | `.github/copilot-instructions.md` | Every request | Entire session | ✅ |
| [**File-based Instructions**](primitive-2-file-based-instructions.md) | `.github/instructions/*.instructions.md` | File pattern match | While file in context | ✅ |
| [**Prompts**](primitive-3-prompts.md) | `.github/prompts/*.prompt.md` | User invokes `/name` | Single task | Multi-surface |
| [**Skills**](primitive-4-skills.md) | `.github/skills/*/SKILL.md` | Description matches intent | Single task | ✅ |
| [**Custom Agents**](primitive-5-custom-agents.md) | `.github/agents/*.md` | User invokes `@name` | Until switched | ✅ |
| [**MCP**](primitive-6-mcp.md) | `.vscode/mcp.json` | Session start | Entire session | ✅ |
| [**Hooks**](primitive-7-hooks.md) | `.github/hooks/*.json` | Agent session events | Coding agent only | ✅ |
| [**Copilot Memory**](primitive-8-memory.md) | Managed by GitHub | Automatic | Repository-wide | ✅ |

**Platform Extensions:**

| Extension | Location | When Loaded | Scope | CLI Support |
|-----------|----------|-------------|-------|-------------|
| [**Agentic Workflows**](agentic-workflows.md) | `.github/workflows/*.md` | Schedule, event, or dispatch | Repository-wide | GitHub Actions |
| [**Copilot SDK**](copilot-sdk.md) | External dependency (npm, pip, etc.) | Application code | Custom surfaces | N/A — your app |

### Authoring the Primitives

The primitive files themselves are portable. They're just Markdown and JSON in `.github/`. How you *author* them varies by surface:

| Surface | Authoring experience |
|---------|---------------------|
| **VS Code** | Chat Customizations editor (gear icon in Chat view, or **Chat: Open Chat Customizations**). VS Code also provides `/create-instruction`, `/create-prompt`, `/create-skill`, `/create-agent`, and `/create-hook` slash commands in Chat to scaffold files from a plain-English description, plus `/init` to generate `copilot-instructions.md` from the existing codebase. |
| **Copilot CLI** | `/init` generates `copilot-instructions.md`. Other primitive files are authored directly or with AI assistance in the terminal session. |
| **Visual Studio, JetBrains, Xcode, Eclipse, GitHub.com** | Edit the files directly, or author them from VS Code / the CLI and commit. All surfaces read the same `.github/` layout. |

Regardless of how a primitive is authored, the output is always the same set of files listed above, and every supported surface loads them from the repository.

---

## Don't Hand-Type Primitives — Let the Helmsman Repeat the Order

On a ship, the captain gives an order and the helmsman repeats it aloud before acting. "Right standard rudder, aye" comes back before the wheel moves. This is called *sounding off* or the *repeat-back*, and it exists because a misheard order is cheap to fix before the ship turns and expensive to fix after. The helmsman's repeat-back closes the loop at the moment of lowest cost.

Authoring a Copilot primitive works the same way. The primitive files are YAML frontmatter plus Markdown, which looks simple enough to write by hand. It isn't. The first time a primitive silently fails to activate, the cause is almost always a hand-typed mistake: a wrong path, the wrong extension, a misspelled frontmatter field, an `applyTo` glob that doesn't match what the author thought it matched, or a file committed outside the folder Copilot actually scans. None of these produce an error. The primitive just sits there, ignored.

The fix is to let Copilot itself draft the primitive, then read the draft before saving it. That is the repeat-back.

**The rule: prefer built-in creation commands over hand-typing.**

The flow is three steps:

1. **Give the order.** Describe what the primitive should do in plain English. "Create a file-based instruction for our Python tests that requires pytest fixtures over `setUp`/`tearDown`."
2. **Let the helmsman repeat it.** Run the built-in authoring command for the surface: VS Code's `/create-instruction`, `/create-prompt`, `/create-skill`, `/create-agent`, `/create-hook`, the Chat Customizations editor, or the Copilot CLI equivalent. Copilot generates a draft primitive with the correct path, correct extension, correct frontmatter fields, and a starting body. Read the draft.
3. **Correct the course.** If the draft is wrong (the glob pattern is too broad, the description doesn't match how the skill should be triggered, the tool list is off), refine the order and have it regenerated. Don't hand-patch YAML frontmatter in a text editor.

This closes the loop at draft time, when the fix costs a sentence. It also means the primitive you end up with is the one Copilot itself understood — not the one you hoped it would understand from your hand-typed file.

### Entry points by surface

Use the creation path that matches where the author is working. All of them produce the same `.github/` files; what differs is the authoring UX.

| Surface | Creation entry point |
|---------|---------------------|
| **VS Code** | `/create-instruction`, `/create-prompt`, `/create-skill`, `/create-agent`, `/create-hook` slash commands in Chat, plus `/init` to scaffold `copilot-instructions.md` from the existing codebase. Also the Chat Customizations editor (gear icon in the Chat view, or **Chat: Open Chat Customizations**) and **MCP: Add Server** / **MCP: Open User Configuration** for MCP. |
| **Visual Studio** | `/generateInstructions` for `copilot-instructions.md`; prompt-file, skill, and agent authoring landing on 2026 releases. Until then, ask Copilot Chat to scaffold the file and commit. |
| **JetBrains IDEs** | File-based instructions and custom agents are in Preview. Use the Chat view to ask Copilot to scaffold the file; commit and the other surfaces will pick it up. |
| **GitHub Copilot CLI** | `/init` generates `copilot-instructions.md`. For other primitives, describe the primitive to the CLI and let it create the file directly. |
| **Cloud coding agent** | Assign an issue that describes the primitive to create. The agent opens a PR with the scaffolded file, which reviewers inspect before merge. |
| **Eclipse, Xcode** | No built-in scaffolding UI today. Ask Copilot Chat in the IDE to draft the file, then save it to the correct path. |

When in doubt, use the surface with the most tooling (VS Code or the CLI) to author the primitive, commit it, and let the other surfaces consume it. The files are portable.

### Why this matters

Every primitive has an activation contract: a specific path, a specific filename pattern, a specific set of frontmatter fields, a specific glob syntax. Copilot loads a primitive only when the file satisfies that contract. When a hand-typed file misses any of those, Copilot doesn't warn; it just silently ignores the file. Teams then debug by tweaking prose in the body, convinced the problem is how the rule is worded, when the real problem is that the rule never loaded.

The repeat-back catches these at draft time:

- **Wrong path.** The `/create-instruction` command writes to `.github/instructions/`; a hand-typed file in `docs/instructions/` never loads.
- **Wrong extension.** `.instruction.md` (singular) is silently ignored; the correct extension is `.instructions.md`.
- **Missing or malformed frontmatter.** Missing `applyTo`, the wrong quoting on a glob, unknown keys — Copilot ignores the file or skips the field.
- **Wrong glob.** `applyTo: "src/api/*"` matches one directory deep; `applyTo: "src/api/**"` matches recursively. Authors guess; the generator gets it right because it knows what the `applyTo` contract expects.
- **Forgotten fields.** Skills need a `description` that semantically matches the task; without it, the skill never activates.

The exception: small tweaks to an existing, working primitive are fine to do by hand. Fixing a typo, adding a bullet to a rule list, adjusting a sentence of guidance — a text editor is faster than round-tripping through Chat. The repeat-back matters most at *creation*, when the scaffolding has to be right for the primitive to work at all.

Sound off before you steer.

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

**When primitives conflict:** More specific primitives take precedence over less specific ones. File-based instructions override always-on instructions for the files they target. Agent-scoped instructions override global instructions while that agent is active. If a file-based instruction says "use spaces" and always-on instructions say "use tabs," the file-based rule wins for matching files. This mirrors CSS specificity: the most targeted rule applies.

**Important limitation:** Custom instructions, prompts, skills, and agents affect **Copilot Chat interactions only**. Inline suggestions (ghost text autocomplete) operate on a separate pipeline and do not read customization files. Use Chat-based interactions for convention-aware code generation.

**Monorepo support:** VS Code 1.116 added the `chat.useCustomizationsInParentRepositories` setting. When enabled, customization files (instructions, agents, skills, hooks) are discovered from parent repositories in a monorepo layout. Shared configurations at the repo root apply automatically to nested packages without duplication. This setting pairs with the existing monorepo hook discovery (VS Code 1.111+) to provide full customization inheritance across package boundaries.

**Not sure which primitive to use?** See the [Quick Decision Guide](part-3-reference.md#quick-decision-guide) in Part III for a lookup table that maps common scenarios to the right primitive.

### Where Primitives Overlap

Several primitives look similar at first glance. These are the most common "but don't these do the same thing?" questions:

| Confusion | The Difference | Rule of Thumb |
|-----------|---------------|---------------|
| **Always-on instructions vs. Custom agents** | Instructions are global rules that apply to every interaction. Agents are specialized personas with their own tools, model, and behavior; they *contain* instructions but also constrain scope. | Put universal rules (tech stack, conventions) in instructions. Put role-specific behavior (code reviewer persona, deployment specialist) in agents. |
| **Prompts vs. Skills** | Both appear as `/` commands. Prompts are user-triggered templates, fire-and-forget. Skills are procedural knowledge that Copilot can also discover and load *automatically* based on context. | Use prompts for simple, single-purpose commands. Use skills when the knowledge should also activate without the user asking, or needs to work in Copilot CLI and the cloud agent. See [Skills vs. File-Based Instructions](primitive-4-skills.md#skills-vs-file-based-instructions-overlapping-territory) for the full decision framework. |
| **Agents vs. Prompts** | Both are user-invoked. An agent is a persistent persona that changes *who Copilot is* for the entire conversation (tools, model, behavior). A prompt is a single task template; it runs once and Copilot returns to normal. | If the user switches into a "mode" (reviewer, architect, mentor), that's an agent. If the user runs a repeatable task (scaffold component, generate tests), that's a prompt or skill. |
| **Instructions vs. Memory** | Instructions are explicit rules you write. Memory is implicit knowledge Copilot learns from working in your repo. Instructions tell Copilot the right answer upfront. Memory captures patterns Copilot discovers over time. | Write instructions for decisions you've already made (tech stack, conventions). Let Memory learn the things that are hard to articulate (codebase patterns, naming conventions in specific areas). They reinforce each other. Memory won't contradict your instructions. |
| **Hooks vs. Instructions** | Instructions *ask* Copilot to avoid something ("don't modify production configs"). Hooks *enforce* it. A hook script runs outside the model and can block the action before it happens. | Use instructions for guidance the model should follow. Use hooks when compliance is mandatory and you can't risk the model ignoring the rule. Defense in depth: use both together. |
| **File-based instructions vs. Skills** | File-based instructions activate by file pattern (`applyTo: 'src/api/**'`). Skills activate by intent (description matching what the user is trying to do). | Use file-based instructions for "rules when editing these files." Use skills for "how to do this task." See [the detailed comparison](primitive-4-skills.md#skills-vs-file-based-instructions-overlapping-territory) in Primitive 4. |

The overlap is intentional. These primitives evolved from real needs, and different teams organize the same knowledge differently. The cost of putting something in the "wrong" primitive is low. The cost of not encoding it anywhere is high.

When a team is deciding where a new rule belongs, the fastest test is to ask Copilot to draft it as each candidate primitive and compare the results. Sound off before you steer: the repeat-back makes the choice visible before any file gets committed.

---

## Composition Patterns

Individual primitives are table stakes. They matter more in combination. Most production setups use three or more primitives working together, each handling a different layer of the problem.

**See it in action:** For a live demo, watch Burke Holland, Pierce Boggan, and Olivia Guzzardo in [Live Coding with GitHub Copilot Agent Mode](https://www.youtube.com/watch?v=j3jBOV0aaRQ).

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

**See it in action:** For a live demo, watch Pierce Boggan and James Montemagno in [Let it Cook: Agent Steering, Custom Instructions, and MCP](https://www.youtube.com/watch?v=LqEk35xR_GA).

The agent provides intent and tool access. The skill packages tribal knowledge. MCP connects to infrastructure. Hooks enforce guardrails *outside* the model's control. Even if the model decides to do something dangerous, the hook blocks it before execution.

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
| What has Copilot learned from working here? | Memory |

When designing a workflow, start from the task and ask each question. If the answer is "not applicable," skip that primitive. Most tasks need two or three; complex workflows use four or five. If a setup uses every primitive, it's probably doing too much. Consider splitting it into separate agent-driven workflows that hand off to each other.

When stacking primitives, let the helmsman repeat each order. Generate each primitive through its built-in authoring command, read the draft, then move on to the next layer. The stack is easier to reason about when every file in it was produced by the same repeat-back discipline.

---

## Agent Plugins (Preview)

Agent plugins bundle multiple primitives (skills, custom agents, hooks, and MCP servers) into a single installable package. Instead of configuring each primitive individually, teams can install a plugin that provides a complete workflow in one step.

**Official docs:** [Agent plugins](https://code.visualstudio.com/docs/copilot/customization/agent-plugins)

A plugin is a directory with a `plugin.json` manifest:

```text
my-testing-plugin/
  plugin.json              # Plugin metadata and configuration
  skills/
    test-runner/
      SKILL.md             # Testing skill instructions
  agents/
    test-reviewer.agent.md # Code review agent
  hooks/
    hooks.json             # Hook configuration
  .mcp.json                # MCP server definitions
```

**`plugin.json` required field:**

| Field | Description |
|-------|-------------|
| `name` | Kebab-case plugin name (lowercase, hyphens, max 64 chars) |

**Optional fields:** `description`, `version`, `author`, `skills`, `agents`, `hooks`, `mcpServers`

**Naming rules:** Plugin names must be **kebab-case** (lowercase letters, digits, and hyphens). `My_Plugin` and `myPlugin` are invalid. Use `my-plugin`. Plugin names must be unique within a marketplace.

**Auto-detection order:** VS Code discovers plugins in this order (first match wins on name conflicts):

1. User-installed plugins (`~/.vscode/plugins/`)
2. Workspace-installed plugins (`.vscode/plugins/`)
3. Plugins referenced by the `chat.plugins.installed` setting
4. Plugins bundled inside a repository via `agent-plugins` in workspace settings

Disable individual plugins with `chat.plugins.disabled` or gate installation with `chat.plugins.allowlist` at the organization level.

**Path tokens for plugin authors:** Inside `plugin.json`, `SKILL.md`, `.agent.md`, and hook commands, two tokens resolve to the plugin's install directory:

- `${PLUGIN_ROOT}`: VS Code / Copilot convention
- `${CLAUDE_PLUGIN_ROOT}`: Claude Code compatibility alias (same value)

Use these tokens to reference scripts, templates, or data files packaged inside the plugin (e.g., `bash: "${PLUGIN_ROOT}/scripts/lint.sh"`). Never hardcode absolute paths; plugins install to different locations per user.

**`mcpServers` vs `servers`:** This trips up many authors. Plugin manifests declare MCP servers under a top-level **`mcpServers`** key. Workspace MCP configuration (`.vscode/mcp.json`) uses **`servers`**. The object shape inside each is the same, but the enclosing key differs:

```jsonc
// plugin.json (plugin manifest)
{
  "name": "my-plugin",
  "mcpServers": {
    "my-mcp": { "type": "stdio", "command": "node", "args": ["server.js"] }
  }
}

// .vscode/mcp.json (workspace config)
{
  "servers": {
    "my-mcp": { "type": "stdio", "command": "node", "args": ["server.js"] }
  }
}
```

### Discovering and Installing Plugins

Plugins are available through marketplaces accessible in VS Code and the Copilot CLI:

```text
# VS Code: search @agentPlugins in the Extensions view

# Skills — use the dedicated gh skill command (public preview, April 2026)
gh skill search <query>
gh skill install github/awesome-copilot <skill-name>
gh skill install github/awesome-copilot <skill-name> --pin v1.2.0

# Full plugin bundles (skills + agents + hooks + MCP) via the Copilot CLI
copilot plugin marketplace browse awesome-copilot
copilot plugin install PLUGIN-NAME@awesome-copilot
copilot plugin install OWNER/REPO
```

For skills specifically, prefer `gh skill install`. It works across agent hosts (GitHub Copilot, Claude Code, Cursor, Codex, Gemini CLI), supports version pinning with `--pin`, and writes provenance metadata into the skill's frontmatter. See [Installing and Managing Skills with `gh skill`](primitive-4-skills.md#installing-and-managing-skills-with-gh-skill) for details. Use `copilot plugin install` when you need the full plugin bundle (hooks, agents, MCP servers alongside skills).

Plugin-provided customizations appear alongside locally defined ones. Skills show up in the Configure Skills menu, MCP servers in the server list, and agents in the agent picker.

**Security note:** Plugins can include hooks and MCP servers that run code on the local machine. Review plugin contents and publisher before installing, especially from community marketplaces.

### Plugins vs. Local Customization

| | Local Customization | Agent Plugins |
|-|-------------------|---------------|
| **Source** | `.github/` in your repo | Installed from marketplace or Git |
| **Scope** | One repository | Shared across projects |
| **Maintenance** | Your team maintains | Plugin author maintains |
| **Best for** | Project-specific conventions | Reusable cross-project tooling |

Plugins and local customization work together. A team might install a database plugin for MCP access while maintaining their own project-specific agents and instructions locally.

### CLI Extensions

The Copilot CLI also supports **extensions**: custom Node.js modules in `.github/extensions/` (project-scoped) or `~/.copilot/extensions/` (user-scoped). Each extension is an `extension.mjs` file that communicates with the CLI via JSON-RPC, enabling custom tools, slash commands, and lifecycle hooks:

```text
.github/extensions/
  my-tools/
    extension.mjs    # Entry point (ES Module required)
```

Extensions are auto-detected at session start. Use `/extensions reload` to hot-reload during development. Project extensions override user extensions on name conflicts.

For the full reference, see the [CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference).

**See it in action:** For a live demo, watch Alex Weininger in [Copilot CLI in VS Code](https://www.youtube.com/watch?v=_l3UO1oUoec).

---

## Context Window Guidelines

Every primitive consumes tokens. For recommended size limits per primitive and total active context guidance, see [Part III: Context Window Guidelines](part-3-reference.md#context-window-guidelines).

---

## Debugging What's Loaded

To see exactly what context is active:

Open diagnostics by right-clicking in the Chat view and selecting **Diagnostics**, or search for **Chat: Show Chat Customization Diagnostics** in the Command Palette. This shows loaded instructions, skills, and configuration status.

For deeper debugging, use **"Developer: Log Chat Input History"** or **"Developer: Inspect Chat Model"** commands.

---

## 1. [Always-on Instructions](primitive-1-always-on-instructions.md)

The foundation layer. Define your tech stack, coding conventions, security requirements, and anti-patterns. These rules apply to every Copilot interaction in your repository.

## 2. [File-based Instructions](primitive-2-file-based-instructions.md)

Targeted rules that activate based on file patterns. Use for language-specific conventions, area-specific rules, or different standards for different parts of your codebase.

## 3. [Prompts](primitive-3-prompts.md)

Reusable task templates invoked with `/promptname`. Create prompts for component scaffolding, test generation, documentation, and repeatable workflows.

## 4. [Skills](primitive-4-skills.md)

Procedural knowledge that Copilot discovers and applies when relevant. Package specialized capabilities like Prisma migrations or GitHub issue templates into portable, reusable skills.

## 5. [Custom Agents](primitive-5-custom-agents.md)

Specialized AI personas with defined behaviors and tool access. Build code reviewers, architects, mentors, and role-specific assistants.

## 6. [MCP (Model Context Protocol)](primitive-6-mcp.md)

External service integrations. Connect Copilot to databases, APIs, ticketing systems, and any external tool your workflow requires.

## 7. [Hooks (Preview)](primitive-7-hooks.md)

Runtime enforcement and observability for agent sessions. Execute custom shell commands at key points during agent sessions to enforce security policies, produce audit trails, block dangerous operations, and send notifications. Hooks operate outside the model's context. They don't influence how Copilot thinks, but they govern what the agent is allowed to do.

## 8. [Copilot Memory](primitive-8-memory.md)

Automatic repository-level learning that builds context over time. Unlike the explicit primitives above, Memory works passively. Copilot observes patterns in your codebase and conversations, then applies what it learned in future sessions. Memory complements explicit customization rather than replacing it.

**Official docs:** [Copilot Memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory)

## Platform Extensions

The following are not configuration primitives. They don't shape what Copilot knows about your codebase; they extend Copilot's reach into new environments, consuming the primitives defined above.

### [Agentic Workflows](agentic-workflows.md)

GitHub Agentic Workflows run coding agents inside GitHub Actions (on a schedule, on events, or on demand). This section covers how they work, how to configure the coding agent for autonomous tasks, and how the customization primitives from this guide feed into continuous AI automation.

**Official docs:** [GitHub Agentic Workflows](https://github.github.com/gh-aw/)

### [Copilot SDK](copilot-sdk.md)

The Copilot SDK packages the same agent runtime that powers Copilot CLI and the cloud agent as libraries for Node.js, Python, Go, .NET, and Java. Use it to embed Copilot's agentic capabilities (tool invocation, multi-turn sessions, streaming, and reasoning) in custom tools, internal platforms, and CI pipelines.

**Official docs:** [Copilot SDK](https://github.com/github/copilot-sdk)

### [Code Review](code-review.md)

GitHub Copilot code review runs on GitHub.com pull requests and inside every major IDE. It is not a primitive. It is a cross-cutting feature that reads the same `copilot-instructions.md` and path-scoped `*.instructions.md` files your team already maintains, and surfaces violations as PR comments. The [code review guide](code-review.md) covers which primitives affect review behavior, the character budget, and patterns for diff-citable rules.

**Official docs:** [Using GitHub Copilot code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review)

---

[← Part I: Foundations](part-1-foundations.md) | [Next: Part III - Reference →](part-3-reference.md)
