# Primitive 3: Prompts

[← Back to The Eight Primitives](eight-primitives.md) | [← File-based Instructions](primitive-2-file-based-instructions.md) | [Next: Skills →](primitive-4-skills.md)

*Updated: April 22, 2026.*

---

## Where It Enters the Loop

Prompts do not change the loop globally. They shape one task.

When a user invokes a prompt file, the loop starts with a stronger task frame than the raw user message alone would provide. The prompt says, in effect, "For this run, here is the workflow, the output shape, the expected constraints, and possibly the model and tool posture."

That makes Prompts the lightest-weight task primitive in the system.

## What This Primitive Is For

Use a Prompt when the workflow is explicit, user-invoked, and repeatable.

Good candidates:

- scaffold a component,
- prepare a PR for review,
- generate tests for a selected file,
- write docs in a known format,
- analyze a bug with a stable output structure.

The key property is that the user chooses to run it. Prompts are not meant to be silently discovered in the background.

## What Makes Prompts Different

Prompts sit between plain chat and richer task packaging.

They are more structured than typing the same paragraph over and over. They are less heavyweight than a Skill. They do not create a persistent role the way a Custom Agent does.

That makes them ideal when the team wants consistency without building a larger capability package.

## Where the File Lives

Prompt files live in `.github/prompts/*.prompt.md`.

They are invoked from chat as slash commands in supported surfaces. That means a Prompt is both a reusable instruction artifact and a user-facing command surface.

## Core Frontmatter

The current guide documents these high-value fields:

- `description`
- `agent`
- `model`
- `tools`
- `argument-hint`

The practical effect is straightforward:

- `description` tells the user what the prompt does,
- `agent` chooses execution posture,
- `model` can bias the run toward a specific model,
- and `tools` can narrow the capabilities available for that task.

Tool names are host-specific. A prompt file that lists VS Code tool IDs is describing the current VS Code runtime, not a portable canonical list that every IDE or GitHub surface will understand unchanged.

## Execution Modes Matter

Prompts are not only reusable text. They can choose the posture of the task.

That is why the `agent` field matters so much.

- `ask` is useful when the prompt should stay read-only.
- `agent` is useful when the prompt should edit files, run commands, or work across multiple steps.
- `plan` is useful when the first deliverable should be a scoped plan rather than implementation.

This makes Prompts a clean way to standardize not just wording, but also how much autonomy the task should have.

## When a Prompt Is Better Than a Skill

Use a Prompt when:

- the task should only run when a human explicitly chooses it,
- the workflow is narrow and template-like,
- the team mainly wants to avoid retyping,
- or the logic does not justify its own folder, resources, and discovery behavior.

Promote a Prompt into a Skill when the procedure should be discoverable automatically, portable across more surfaces, or accompanied by supporting files and scripts.

## What a Good Prompt Looks Like

Good prompts are concrete, structured, and opinionated about output.

```markdown
---
agent: 'agent'
description: 'Generate tests for the selected file'
tools: ['search', 'readFile', 'editFiles', 'createFile']
---

Analyze the selected file and create tests that:

1. Match the repository's existing test framework and naming style
2. Cover happy paths and failure paths
3. Add edge-case tests for null, empty, or boundary inputs
4. Explain any behavior that cannot be tested without refactoring
```

Weak prompts are vague and under-specified:

- "Make me a component."
- "Write some tests."
- "Review this code."

Those do not really save thought. They just move a vague request from the chat box into a file.

## How It Composes with Other Primitives

| Primitive | Relationship |
|-----------|--------------|
| [Always-on Instructions](primitive-1-always-on-instructions.md) | Provide baseline repo context for every prompt invocation |
| [File-based Instructions](primitive-2-file-based-instructions.md) | Still apply when the prompt touches matching files |
| [Skills](primitive-4-skills.md) | Overlap in reusable workflow territory, but Skills are more discoverable and portable |
| [Custom Agents](primitive-5-custom-agents.md) | A prompt can target a custom agent when the task should run through a specific persona |

## The Best Use Case

Prompts shine when the team has a task that is common enough to standardize but not broad enough to deserve a full capability package.

That is why so many strong prompt examples are one-shot workflows:

- `/new-component`
- `/generate-tests`
- `/review-prep`
- `/generate-docs`

Each one removes repeated setup friction without pretending to be a universal reasoning layer.

## See It in Action

**See it in action:** [Customize your agents](https://www.youtube.com/watch?v=flpKLkZla2Q&t=524s) — Courtney Webster demos prompt files as slash-command workflows for one-shot tasks like PR cleanup and test generation.

## Creating Prompt Files

Start with the built-in generator. In VS Code, run `/create-prompt` in Chat, or open the Command Palette and run **Chat: New Prompt File**. The generator writes to `.github/prompts/` with the correct `.prompt.md` extension and scaffolds the frontmatter fields. A prompt saved as `.prompt.md` with a wrong path or committed outside `.github/prompts/` never appears in the slash-command picker.

> 💬 **Try this prompt:**
> "Create a prompt file at `.github/prompts/new-component.prompt.md` that scaffolds a React component with a colocated test file. Accept the component name as input and use agent mode."

Store prompts in **Workspace** (`.github/prompts/`, shared via version control) or **User Profile** (personal, across all workspaces).

### Variable Syntax

Prompts support both built-in variables and input variables that prompt the user for a value:

| Syntax | Description |
|--------|-------------|
| `${file}`, `${selection}`, `${workspaceFolder}` | Built-in VS Code context variables |
| `${input:variableName}` | Prompts the user for a value when invoked |
| `${input:variableName:placeholder}` | Prompts with placeholder hint text |

## Essential Prompt Templates

### Component Generator

**File:** `.github/prompts/new-component.prompt.md`

```markdown
---
agent: 'agent'
description: 'Scaffold a new React component with tests and barrel export'
model: 'Claude Opus 4.7'
---

Create a new component called `${input:componentName}` in `src/components/${input:componentName}/`:

## Required Files
1. `${input:componentName}.tsx` - The component
2. `${input:componentName}.test.tsx` - Unit tests
3. `index.ts` - Barrel export

## Requirements
- TypeScript with explicit prop types
- Proper accessibility attributes
- Loading and error states

Follow the patterns in copilot-instructions.md and existing components.
```

### Test Generator

**File:** `.github/prompts/generate-tests.prompt.md`

```markdown
---
agent: 'agent'
description: 'Analyze coverage gaps and generate missing tests'
tools: ['search', 'readFile', 'editFiles', 'createFile', 'runInTerminal']
---

Analyze the selected file and generate tests:

## Phase 1: Audit
1. Identify the test framework in use and follow its conventions
2. Read co-located test files to learn naming and assertion style
3. List untested exports and untested branches

## Phase 2: Write
- Happy-path unit tests for each public function
- Edge cases: empty inputs, null/undefined, boundary values
- Error paths: thrown exceptions, rejected promises
- Co-locate with source unless the repo uses a different convention

## Phase 3: Verify
- Run the test suite and confirm new tests pass
- Report the coverage delta
```

### API Route Generator

**File:** `.github/prompts/new-api-route.prompt.md`

```markdown
---
agent: 'agent'
description: 'Create a new API endpoint with validation and error handling'
---

Create a new API route at `src/app/api/${input:resourceName}/route.ts`:

- Implement ${input:httpMethods} methods
- Zod schema for request validation
- Proper error handling with ApiResponse type
- Integration tests in `__tests__/api/${input:resourceName}.test.ts`
```

### Bug Fix Assistant

**File:** `.github/prompts/fix-bug.prompt.md`

```markdown
---
agent: 'agent'
description: 'Analyze and fix a bug with explanation'
---

**Bug:** ${input:bugDescription}
**Expected:** ${input:expectedBehavior}
**Actual:** ${input:actualBehavior}

1. Root cause analysis
2. The fix with explanation
3. Related issues this might cause
4. Suggested regression test
```

### GitHub Issue Creator (MCP Integration)

```markdown
---
agent: 'agent'
description: 'Create a GitHub issue from a bug report or feature request'
tools: ['githubRepo']
---

Create a GitHub issue:
**Type:** ${input:issueType}
**Title:** ${input:issueTitle}
**Description:** ${input:issueDescription}

Format with proper markdown, apply labels based on type, and return the issue URL.
```

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|--------------|-------------|------------------|
| Vague instructions | "Make me a component" produces inconsistent results | Be specific about requirements and structure |
| No variables | Prompt can only do one specific thing | Use `${input:variableName}` for reusable parts |
| No model specification | Inconsistent results across sessions | Specify model for reproducibility |
| No reference to instructions | Prompt ignores team conventions | Reference copilot-instructions.md explicitly |

## Where to Read Next

- Read [Skills](primitive-4-skills.md) next if the workflow should be discoverable automatically instead of only by explicit invocation.
- Read [Custom Agents](primitive-5-custom-agents.md) later if the problem is persistent role, not just task framing.
