# Always-On Instructions

[← Part I: Foundations](part-1-foundations.md) | [Part II Overview](part-2-primitives.md)

*Updated: April 16, 2026. This guide serves as a primer for GitHub Copilot customization. File paths, configuration options, and feature availability may change as Copilot evolves—always verify against the [official documentation](https://code.visualstudio.com/docs/copilot).*

---

## Overview

**Heads up — inline suggestions ignore these files.** Always-on instructions apply to Copilot Chat and agent sessions only. Ghost text (inline autocomplete) runs on a separate pipeline and does not read `copilot-instructions.md`, `AGENTS.md`, `.instructions.md`, or any other customization primitive in this guide. For convention-aware code generation, use Chat, agent mode, or prompts. See [Inline Suggestions Are Not Affected](#inline-suggestions-are-not-affected) below.

Always-on instructions (also known as the **Copilot Instructions File**) represent the foundational layer of Copilot customization. These instructions load automatically at the start of every Copilot session and apply to all interactions within the repository.

**Location:** `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md` [*](https://code.visualstudio.com/docs/copilot)

**Official docs:** [Custom instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)

Both `copilot-instructions.md` and `AGENTS.md` are recognized as workspace instruction files. The `/init` command can discover and update either format.

**Relevant Settings:** Instruction file detection is controlled by `chat.includeApplyingInstructions` (pattern-matched instructions), `chat.includeReferencedInstructions` (Markdown-linked instructions), and `chat.useAgentsMdFile` (`AGENTS.md` support). All are enabled by default. [*](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)

**Ownership:** Typically maintained by the **application team** for per-repo conventions, with **platform / enablement teams** contributing shared defaults via organization-level instructions. Security and compliance teams should review the security and guardrails sections.

When this file exists in a repository and the setting is enabled, Copilot reads and applies its contents as persistent context. Chat responses and code generation will respect these guidelines without requiring explicit invocation.

## Inline Suggestions Are Not Affected

Custom instructions are **not** applied to inline suggestions (ghost text) as you type in the editor — they only affect Copilot Chat interactions. This is a fundamental limitation: the autocomplete engine operates on a different pipeline than Chat and does not read instruction files.

If Copilot's inline suggestions ignore your conventions, that's expected behavior. Use Chat-based interactions (ask mode, agent mode, prompts) for convention-aware code generation.

**See it in action:** For a live demo, watch Courtney Webster in [Customize Your Agents](https://www.youtube.com/watch?v=flpKLkZla2Q).

## When to Use Always-On Instructions

- Coding style and conventions that apply universally
- Technology stack declarations and preferences
- Security requirements and guardrails
- Architectural patterns to follow or avoid
- Documentation standards
- Error handling approaches
- Deprecated patterns to avoid

## Anatomy of Effective Instructions

A well-structured instructions file typically includes the following sections:

**See it in action:** [Customize Your Agents](https://www.youtube.com/watch?v=flpKLkZla2Q&t=221s) — Courtney Webster walks through the best practices that shape an effective instructions file: be specific about frameworks, include reasoning, add code examples, and skip rules that linters or formatters already enforce.

```markdown
# Copilot Instructions for [Your Project Name]

## Tech Stack
- TypeScript (strict mode, always)
- React 18 with functional components only
- TanStack Query for data fetching
- Zod for validation
- Tailwind CSS for styling

## Code Style
- Use named exports, not default exports
- Prefer `const` over `let`; never use `var`
- All functions should have explicit return types
- Use early returns to reduce nesting
- Maximum function length: 50 lines

## File Organization
- Co-locate tests with source files (`Component.tsx` + `Component.test.tsx`)
- Use barrel exports (`index.ts`) for public APIs only
- Keep components under 200 lines; extract hooks if larger

## Security
- Never commit secrets or API keys
- Always sanitize user input
- Use parameterized queries for any database operations
- Validate all external data with Zod schemas

## What NOT to Do
- Don't use `any` type (use `unknown` and narrow)
- Don't use class components
- Don't use moment.js (use date-fns instead)
- Don't write inline CSS
```

## Including Rationale (Appraisals)

Instructions files become more effective when they include the reasoning behind rules. This context helps Copilot make better decisions in edge cases:

```markdown
## Why We Made These Choices

### Why TypeScript Strict Mode?
We had three production bugs in Q2 2024 that would have been caught by strict 
null checks. The 30-minute investment per feature to properly type things 
saves us hours of debugging.

### Why No Class Components?
Our team benchmarks showed functional components with hooks reduced our bundle 
size by 15% and made testing significantly easier.
```

This helps Copilot understand not just *what* to do, but *why*—leading to better suggestions in edge cases.

## Complete Example: Production Next.js Project

``````markdown
# Project Guidelines for Copilot

## Project Overview
This is a B2B SaaS platform for inventory management. 
We prioritize reliability over cutting-edge features.

## Architecture
- Next.js 14 App Router
- PostgreSQL with Prisma ORM
- NextAuth.js for authentication
- Stripe for payments
- Deployed on Vercel

### Directory Structure
```
src/
+-- app/                    # Next.js App Router pages
—   +-- (auth)/            # Auth-required routes (grouped)
—   +-- (public)/          # Public routes
—   +-- api/               # API routes (webhooks only)
+-- components/
—   +-- ui/                # Shared UI primitives
—   +-- features/          # Feature-specific components
+-- lib/                   # Shared utilities
+-- server/
—   +-- actions/           # Server Actions
—   +-- db/                # Database queries (Prisma)
—   +-- services/          # Business logic
+-- types/                 # Shared TypeScript types
```

### Data Flow
1. Client components call Server Actions for mutations
2. Server Components fetch data directly via Prisma
3. TanStack Query for client-side cache invalidation
4. Never use Route Handlers except for webhooks

## Coding Standards

### TypeScript
- Enable all strict checks
- No `any` types except in test mocks
- Prefer interfaces over types for object shapes
- Use discriminated unions for complex state
- Export types from `types/` directory, not inline

### React Patterns
```typescript
// ✅ Good: Custom hook for data fetching
function useInventoryItems(warehouseId: string) {
  return useQuery({
    queryKey: ['inventory', warehouseId],
    queryFn: () => fetchInventory(warehouseId),
  });
}

// ❌ Bad: Fetching in useEffect
useEffect(() => {
  fetch('/api/inventory').then(/* ... */);
}, []);
```

### Server Actions
```typescript
// ✅ Good: Validated, authorized, audited
export async function updateInventory(input: UpdateInventoryInput) {
  const validated = updateInventorySchema.parse(input);
  const session = await auth();
  if (!session) throw new UnauthorizedError();
  
  await auditLog('inventory.update', { userId: session.user.id, ...validated });
  return db.inventory.update({ where: { id: validated.id }, data: validated });
}

// ❌ Bad: No validation, no auth check
export async function updateInventory(data: any) {
  return db.inventory.update({ data });
}
```

## Testing Requirements

### Test Structure
- Co-locate unit tests with source: `Component.tsx` → `Component.test.tsx`
- Integration tests in `__tests__/integration/`
- E2E tests in `e2e/` using Playwright

### Coverage Requirements
- Minimum 80% line coverage for `server/` directory
- All Server Actions must have integration tests
- All user-facing flows must have E2E tests

### Testing Patterns
```typescript
// ✅ Good: Descriptive test with clear arrange/act/assert
describe('updateInventory', () => {
  it('should update quantity and log audit event', async () => {
    // Arrange
    const item = await createTestInventoryItem({ quantity: 10 });
    
    // Act
    await updateInventory({ id: item.id, quantity: 15 });
    
    // Assert
    const updated = await db.inventory.findUnique({ where: { id: item.id } });
    expect(updated?.quantity).toBe(15);
    expect(await getAuditLogs('inventory.update')).toHaveLength(1);
  });
});

// ❌ Bad: Vague test name, no clear structure
test('inventory works', async () => {
  const result = await updateInventory({ id: '1', quantity: 5 });
  expect(result).toBeTruthy();
});
```

### Mocking Guidelines
- Use `vi.mock()` for external services only
- Never mock Prisma in integration tests (use test database)
- Reset mocks in `beforeEach`, not `afterEach`

## Error Handling

### Error Types
Use our custom error hierarchy:
- `AppError` - Base class for all application errors
- `ValidationError` - Invalid input (400)
- `UnauthorizedError` - Not authenticated (401)
- `ForbiddenError` - Not authorized (403)  
- `NotFoundError` - Resource doesn't exist (404)

### Error Pattern
```typescript
// ✅ Good: Specific error with context
if (!warehouse) {
  throw new NotFoundError('Warehouse', warehouseId);
}

// ❌ Bad: Generic error
if (!warehouse) {
  throw new Error('Not found');
}
```

## Security Guidelines

### Authentication
- All `/app/(auth)/` routes require session
- Use `auth()` from NextAuth, never roll your own
- Session checks happen in Server Components, not middleware

### Authorization
- All queries must include `organizationId` filter
- Use `assertCanAccess(resource, session)` helper
- Never trust client-provided organization IDs

### Data Validation
- Validate ALL external input with Zod schemas
- Schemas live in `lib/schemas/` 
- Reuse schemas between client and server

## Accessibility Guidelines

Accessibility is a first-class concern. Treat WCAG 2.2 AA as the minimum bar, not an afterthought.

### Component Requirements
- All interactive elements must be keyboard-operable (Tab, Enter, Space, Esc)
- Form inputs require associated `<label>` elements or `aria-label`
- Images need meaningful `alt` text; decorative images use `alt=""`
- Color contrast must meet 4.5:1 for body text, 3:1 for large text and UI components
- Never convey meaning through color alone

### Semantic HTML First
```typescript
// ✅ Good: Semantic, screen-reader friendly
<button onClick={handleSave}>Save changes</button>

// ❌ Bad: Div masquerading as a button
<div onClick={handleSave}>Save changes</div>
```

### Testing
- Every feature PR must pass `axe-core` automated checks in CI
- Keyboard-navigation smoke test for every new interactive flow
- Skip-link and focus-trap verification for modals and menus

**Why:** Accessibility failures surface in customer complaints, App Store review rejections, and EU accessibility audits. Catching them in instructions and automated checks is an order of magnitude cheaper than catching them after release.

## Performance Guidelines

### Database
- Always use `select` to limit returned fields
- Use `include` sparingly (prefer separate queries)
- Add indexes for any field used in WHERE clauses

### React
- Use `React.memo()` only when profiler shows need
- Prefer Server Components for static content
- Use `loading.tsx` for Suspense boundaries

## Dependencies

### Approved Libraries
- Date handling: `date-fns` (NOT moment.js)
- Forms: `react-hook-form` + `zod`
- Styling: Tailwind CSS only
- Icons: `lucide-react`

### Deprecated (Do Not Use)
- `moment.js` - Use `date-fns` instead
- `axios` - Use native `fetch`
- `lodash` - Use native methods or `es-toolkit`
- Class components - Use functional components

## Git Conventions

### Branch Naming
- `feature/INV-123-add-bulk-import`
- `fix/INV-456-quantity-calculation`
- `chore/update-dependencies`

### Commit Messages
Follow Conventional Commits:
- `feat(inventory): add bulk import endpoint`
- `fix(auth): handle expired session redirect`
- `test(warehouse): add integration tests for transfer`
``````

For a product management approach to workspace instructions, see [product-brain](https://github.com/digitarald/product-brain) — a template that structures AI interactions around product requirements, user stories, and feature specifications.

---

## Creating an Instructions File

Every Copilot surface reads the same `.github/copilot-instructions.md` (or `AGENTS.md`) file, but each surface has a different path for authoring it. Pick the workflow that matches where your team works — the resulting file is identical and portable across every other surface.

### VS Code

VS Code offers the richest authoring experience, with both an agent-driven command and a menu-driven flow.

**Using the `/init` command (fastest):**

1. Open Copilot Chat
2. Type `/init` in the chat input box
3. Review the generated `.github/copilot-instructions.md` file
4. Make any necessary edits and save

The `/init` command follows a structured workflow:

1. **Discovery** — Searches for existing AI conventions in your workspace (such as `copilot-instructions.md` or `AGENTS.md`)
2. **Analysis** — Examines your project structure and coding patterns
3. **Generation** — Creates comprehensive workspace instructions tailored to your project

In VS Code 1.109 and later, the `/init` command is implemented as a contributed prompt file, meaning you can customize its behavior by modifying the underlying prompt in your workspace.

**See it in action:** For a live demo, watch Courtney Webster in [Customize Your Agents with Reusable Prompts, Instructions, and Tools](https://www.youtube.com/watch?v=LNftRSF37WI).

**Using the Configure menu:**

1. In the Chat view, click the **gear icon** (Configure Chat)
2. Select **Generate Chat Instructions** to auto-generate, or
3. Select **Chat Instructions** > **New instruction file...** for manual creation
4. Select the storage location:
   - **Workspace:** `.github/` folder [*](https://code.visualstudio.com/docs/copilot) (shared with team via version control)
   - **User Profile:** Personal instructions across all workspaces
5. Author the instructions or let the agent generate initial content

### Visual Studio

Visual Studio 2022 (17.13+) and Visual Studio 2026 ship a dedicated slash command for generating the instructions file:

1. Open the **Copilot Chat** window (not inline chat — the slash command is only available in the chat window)
2. Type `/generateInstructions` and send
3. Copilot analyzes the solution and produces a `.github/copilot-instructions.md` file
4. Review and commit the result

The **Enable custom instructions** toggle at **Tools → Options → All Settings → GitHub → Copilot → Copilot Chat** controls whether the file is attached to requests. See [IDE Surfaces — Visual Studio](surfaces.md#visual-studio) for per-version details.

### JetBrains IDEs

The GitHub Copilot plugin exposes an instructions authoring panel under the IDE settings:

1. Open **Settings → Tools → GitHub Copilot → Customizations**
2. Locate **Copilot Instructions** and toggle between **Workspace** and **Global**
3. Edit directly in the panel — the IDE writes to `.github/copilot-instructions.md` (workspace) or the platform-specific global path
4. Save; the plugin picks up the file on the next chat turn

JetBrains also supports a machine-global instructions file that applies across every workspace the signed-in user opens. See [IDE Surfaces — JetBrains](surfaces.md#jetbrains-ides) for global file paths and IDE compatibility.

### GitHub Copilot CLI

The CLI recognizes both `.github/copilot-instructions.md` and `AGENTS.md` at the repository root but does not ship a dedicated generator. Two practical options:

1. **Generate with the CLI's agent itself** — run `copilot` in the repo and ask it to analyze the codebase and write `.github/copilot-instructions.md` using the prompt from the [Agent-Driven Generation](#agent-driven-generation-any-surface) section below.
2. **Create manually** — author the file in any editor and commit it. The CLI will pick it up on the next session.

See [Copilot CLI](surfaces/copilot-cli.md) for session flags and session control.

### GitHub.com (Copilot Coding Agent)

On GitHub.com, the Copilot coding agent can generate instructions for a repository:

1. Navigate to [github.com/copilot/agents](https://github.com/copilot/agents)
2. Select your repository from the dropdown
3. Use the onboarding prompt from [GitHub's documentation](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions)
4. Review the generated PR with the instructions file and merge

This is particularly effective because the agent validates build commands and tests them before documenting them in the file.

### Xcode and Eclipse

The Xcode and Eclipse extensions read `.github/copilot-instructions.md` but do not currently offer an in-IDE generator. Create the file using one of the surfaces above (VS Code `/init`, Visual Studio `/generateInstructions`, or the Copilot CLI), commit it to the repository, and the Xcode/Eclipse extension will consume it automatically. See [IDE Surfaces — Xcode](surfaces.md#xcode) and [Eclipse](surfaces.md#eclipse) for the current primitive support matrix.

### Agent-Driven Generation (Any Surface)

Whichever surface you use, the highest-quality output usually comes from asking the agent to analyze the repository and write the file for you:

> **💬 Try this prompt:**
>
> *Analyze this repository and create a .github/copilot-instructions.md file that:*
>
> *1. Documents the tech stack and architecture*
> *2. Identifies coding conventions from existing code*
> *3. Notes patterns that should be followed*
> *4. Lists patterns that should be avoided*
> *5. Includes testing requirements*
> *6. Adds rationale for each guideline*
>
> *Examine the package.json, existing source files, and any documentation to ensure accuracy. Format as a human-readable markdown file I can review and refine.*

This approach ensures:
- Instructions reflect actual codebase patterns
- Consistent formatting and structure
- Human-verifiable output for PR review
- No syntax errors or typos

## Anti-Patterns to Avoid

| Anti-Pattern | Why It's Problematic | Better Approach |
|--------------|---------------------|------------------|
| **Typing directly into the file** | Prone to errors, may miss patterns | Have the agent generate from codebase analysis |
| **Copy-pasting from other repos** | Doesn't reflect your actual conventions | Generate custom instructions for each repo |
| **Overly verbose instructions** | Consumes context window, dilutes important rules | Keep to 500-2000 words, focus on non-obvious rules |
| **No rationale** | Copilot can't make good edge case decisions | Include "why" for each guideline |
| **Conflicting rules** | Copilot produces inconsistent results | Have agent check for contradictions |
| **Never updating** | Instructions drift from actual practice | Review quarterly, use agent to refresh |

## Gathering Team Knowledge

Effective instructions files encode team knowledge. Use these questions to surface the most valuable rules:

1. **"What does Copilot frequently get wrong?"** — These become explicit rules
2. **"What feedback appears repeatedly in PR reviews?"** — These become guidelines
3. **"What would a new hire need to know on day one?"** — This becomes context
4. **"What libraries or patterns have been deprecated?"** — This becomes the "avoid" list

**Practical tip:** Review the last 10-20 PR comments from the team. Repeated feedback indicates rules that should be codified in the instructions file.

> **💬 Try this prompt:**
>
> *Analyze the last 20 merged pull requests in this repository. Look at the review comments and identify:*
>
> *1. Repeated feedback patterns (things reviewers keep asking for)*
> *2. Common mistakes that get flagged*
> *3. Style or convention corrections*
> *4. Architectural concerns raised multiple times*
>
> *Summarize these as candidate rules for our copilot-instructions.md file.*

## Use the "Good vs Bad" Pattern

Copilot responds more effectively to examples than to abstract rules. Instead of stating "prefer functional patterns," demonstrate the preference:

```markdown
## Data Transformation

✅ **Preferred:**
```typescript
const activeUsers = users
  .filter(user => user.isActive)
  .map(user => user.name);
```

❌ **Avoid:**
```typescript
let activeUsers = [];
for (let i = 0; i < users.length; i++) {
  if (users[i].isActive) {
    activeUsers.push(users[i].name);
  }
}
```

**Why:** Declarative patterns are easier to read and less error-prone. 
Our eslint config will flag the imperative version anyway.
```

## Iterating with the Agent

After initial generation, refine the instructions file through conversation:

> **💬 Try this prompt:**
>
> *Review the .github/copilot-instructions.md file and:*
>
> *1. Check for any contradictions between rules*
> *2. Add examples for the most important conventions*
> *3. Include rationale where it's missing*
> *4. Remove any rules that are standard/obvious*
> *5. Ensure the tech stack section is accurate*
>
> *Make the changes and explain what you updated.*

This creates a feedback loop where the agent refines its own guidelines based on human review.

## Validating the Configuration

To verify the instructions file is working correctly:

1. Open Copilot Chat in VS Code
2. Ask: "What are the coding standards for this project?"
3. Copilot should reference content from the instructions file
4. Generate sample code and verify it follows the defined rules

If instructions are not being applied, verify:
- The `chat.includeApplyingInstructions` setting is enabled (default: `true`)
- File is named exactly `copilot-instructions.md` or `AGENTS.md`
- File is located in the `.github/` folder [*](https://code.visualstudio.com/docs/copilot)
- VS Code window has been reloaded after creating the file

**Using Diagnostics:** Right-click in the Chat view and select **Diagnostics** to see all loaded instruction files, custom agents, prompt files, and skills—along with any errors.

## Cross-Editor Compatibility

The `.github/copilot-instructions.md` file is recognized by GitHub Copilot across multiple environments:
- VS Code
- Visual Studio
- GitHub.com (Copilot Chat, coding agent, code review)
- [GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) (terminal-based AI agent)

This means the same instructions file works whether your team uses different editors, interacts with Copilot on the web, or works from the command line. Copilot CLI also recognizes `AGENTS.md` as a workspace instruction file.

## Instruction Priority

When multiple types of custom instructions exist, Copilot applies them in this [priority order](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-personal-instructions):

1. **Personal instructions** (highest priority)
2. **Repository instructions** (`.github/copilot-instructions.md` or `AGENTS.md`)
3. **Organization instructions** (lowest priority)

All relevant instructions are provided to Copilot, but higher-priority instructions take precedence when conflicts occur.

## Organization-Wide Instructions

Organization-level [custom instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-organization-instructions) reached **general availability on April 2, 2026** and are supported in VS Code and other Copilot surfaces.

If your GitHub organization has configured custom instructions for Copilot, they are automatically applied to your chat sessions, ensuring consistent guidance across your team. This feature is enabled by default.

**Setting:** `github.copilot.chat.organizationInstructions.enabled`

Set to `false` to disable organization instructions if you need to override them for a specific workspace.

Organization instructions are particularly valuable for:
- Enforcing company-wide coding standards
- Maintaining compliance requirements across repositories
- Sharing best practices without duplicating instructions in every repo

## Referencing Tools in Instructions

Instruction files can reference specific tools using the `#tool:` syntax. This signals to Copilot which tools are relevant for a given convention:

```markdown
## Testing
- Always run tests with #tool:runInTerminal after making changes
- Use #tool:search to find existing test patterns before writing new tests
```

Tool references help Copilot understand not just _what_ to do, but _how_ to accomplish it using available capabilities.

## CLAUDE.md Compatibility

VS Code also [detects `CLAUDE.md` files](https://code.visualstudio.com/docs/copilot/customization/custom-instructions) and applies them as always-on instructions, providing compatibility with Claude Code and other Claude-based tools. This enables teams using multiple AI agents to maintain a single set of instructions recognized by all of them.

**Detected locations:**

| Location | Purpose |
|----------|--------|
| `CLAUDE.md` in workspace root | Primary workspace instructions |
| `.claude/CLAUDE.md` | Alternative workspace location |
| `~/.claude/CLAUDE.md` | Personal instructions across all projects |
| `CLAUDE.local.md` | Local-only instructions (not committed to version control) |

**Setting:** `chat.useClaudeMdFile` — enable or disable `CLAUDE.md` detection.

For scoped rules, VS Code also detects instructions files in the `.claude/rules` workspace folder and the `~/.claude/rules` user folder. These use a `paths` property (instead of `applyTo`) for glob patterns, following the [Claude Rules format](https://code.claude.com/docs/en/memory#basic-structure). The `paths` property accepts an array of glob patterns and defaults to `**` (all files) when omitted.

## Nested AGENTS.md Files (Experimental)

For monorepos or projects with distinct subsystems, VS Code supports [nested `AGENTS.md` files](https://code.visualstudio.com/docs/copilot/customization/custom-instructions) in subfolders. Each subfolder can have its own `AGENTS.md` with instructions scoped to that part of the project.

**Setting:** `chat.useNestedAgentsMdFiles` — enable or disable nested `AGENTS.md` support.

When enabled, VS Code searches recursively through all subfolders for `AGENTS.md` files and adds their relative paths to the chat context. The agent decides which instructions to use based on the files being edited.

```
my-monorepo/
├── AGENTS.md              # Root-level instructions
├── frontend/
│   └── AGENTS.md          # Frontend-specific instructions
├── backend/
│   └── AGENTS.md          # Backend-specific instructions
└── shared/
    └── AGENTS.md          # Shared library instructions
```

For folder-specific instructions without the experimental setting, file-based instructions with targeted `applyTo` patterns provide the same scoping capability.

---

[← Part I: Foundations](part-1-foundations.md) | [Next: File-Based Instructions →](primitive-2-file-based-instructions.md)
