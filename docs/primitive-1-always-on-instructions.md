# Primitive 1: Always-on Instructions

[← Back to The Eight Primitives](eight-primitives.md) | [Next: File-based Instructions →](primitive-2-file-based-instructions.md)

*Updated: April 22, 2026.*

---

## Where It Enters the Loop

Always-on Instructions shape the loop at the earliest useful point: context assembly.

Before GitHub Copilot decides whether to search, edit, call a tool, or answer directly, it needs a baseline picture of the repository it is operating inside. Always-on Instructions provide that baseline. They tell the runtime what this repository is, what it values, what it avoids, and which defaults should be treated as wrong here even if they are common elsewhere.

That is why this primitive belongs first. If the defaults are wrong, every later step in the loop starts from the wrong assumptions.

## What This Primitive Is For

Use Always-on Instructions for rules that should apply to nearly every chat or agent interaction in the repository:

- stack choices,
- architectural defaults,
- naming and organization patterns,
- security guardrails stated as guidance,
- deprecated libraries and patterns,
- and the recurring review comments that do not belong to one folder or one task.

Use it to answer the question, "What would a strong developer need to know on day one to stop fighting the repo?"

## What Does Not Belong Here

Do not turn this file into a dumping ground.

Always-on Instructions are the wrong place for:

- path-specific rules that only matter in one part of the tree,
- long procedures for repeatable tasks,
- role-specific personas,
- tool integrations,
- or hard enforcement requirements.

Those belong in File-based Instructions, Skills, Custom Agents, MCP, or Hooks.

The easiest smell test is scope. If the rule is not true for most repository work, it probably does not belong here.

## What It Changes

This primitive changes the loop in three ways:

1. It reduces repeated prompting by loading baseline repository knowledge automatically.
2. It lowers the chance that the model falls back to generic public-code defaults.
3. It gives every later primitive a cleaner foundation to build on.

This is why teams usually feel the first payoff here before anywhere else. A short, well-written instructions file can eliminate large amounts of low-value prompting.

## Inline Suggestions Are Still a Separate Pipeline

Always-on Instructions affect GitHub Copilot Chat and agent sessions. They do not change inline suggestions as you type.

That distinction matters because teams often test the file in the wrong place, see no difference in ghost text, and conclude the configuration failed. The file can be working correctly while inline completion ignores it.

The practical rule is simple: use Chat, agent mode, or prompt-driven workflows when you need convention-aware output.

## Where the File Lives

The repository-level home is `.github/copilot-instructions.md`.

The current guide also documents `AGENTS.md` and `CLAUDE.md` as recognized workspace instruction files in supported environments. That flexibility is useful when a team already has one of those conventions in place, but the main teaching path in this guide remains `.github/copilot-instructions.md` because it is the clearest cross-team default.

## Anatomy of a Good Instructions File

A good instructions file is short enough to stay readable and specific enough to change behavior.

It usually includes:

- what the project is,
- the tech stack and the choices the team made,
- coding patterns to prefer,
- patterns to avoid,
- and a few examples that show the difference between the two.

The best files also include short rationale where the reason behind a rule changes how edge cases should be handled.

```markdown
# Copilot Instructions for Example Service

## Tech Stack
- TypeScript with strict mode
- React Query for server state
- Zod for validation

## Architecture
- Route handlers stay thin
- Business logic lives in `src/server/services/`
- Database access goes through repository modules

## Avoid
- Do not introduce Redux for server state
- Do not fetch directly in `useEffect` for standard data loading

## Why
We use React Query because cache invalidation, retry behavior, and loading states are already standardized around it.
```

## What Makes These Instructions Effective

The file is most useful when it captures non-obvious local choices rather than generic advice.

Good examples:

- "Use React Query, not Redux, for server state."
- "All API responses use our `ApiResponse<T>` envelope."
- "Business logic belongs in service modules, not route handlers."

Weak examples:

- "Write clean code."
- "Use best practices."
- "Handle errors properly."

GitHub Copilot cannot act on vague preferences. It can act on concrete rules with recognizable examples.

## When to Split Instead of Grow

If the instructions file keeps expanding, that is usually not a sign of maturity. It is a sign that the knowledge is being stored at the wrong layer.

Split into other primitives when:

- a rule only applies to tests, API routes, or one language,
- the content is really a repeatable task procedure,
- a specialized role needs different behavior,
- or the knowledge is operational rather than architectural.

The global file should stay the foundation, not become the whole building.

## How It Composes with Other Primitives

Always-on Instructions work best when they define the floor, not the ceiling.

| Primitive | Relationship |
|-----------|--------------|
| [File-based Instructions](primitive-2-file-based-instructions.md) | Add scoped exceptions or additions for matching files |
| [Prompts](primitive-3-prompts.md) | Reuse the baseline defaults while framing one explicit task |
| [Skills](primitive-4-skills.md) | Assume the baseline context and add procedural knowledge |
| [Custom Agents](primitive-5-custom-agents.md) | Operate inside the repo defaults while changing posture and tool use |
| [Memory](primitive-8-memory.md) | Reinforce patterns the repo keeps expressing through use |
| [Hooks](primitive-7-hooks.md) | Enforce rules that are too important to leave as guidance |

## How to Create It Safely

Use GitHub Copilot's built-in scaffolding or repo analysis to draft the file, then edit the draft.

The first failure mode is usually not wording. It is scaffolding: wrong path, wrong filename, or a file the intended surface does not load. Starting from generated structure lowers that risk.

> 💬 **Try this prompt:**
> "Scan this repository and draft `.github/copilot-instructions.md` with our stack choices, architecture defaults, testing expectations, and deprecated patterns. Flag anything uncertain instead of guessing."

## See It in Action

**See it in action:** [Customize your agents](https://www.youtube.com/watch?v=flpKLkZla2Q&t=367s) — Courtney Webster demos a repo-level instructions file loading as always-on context and surfacing in the chat debug view.

## Creating the File

Every surface reads `.github/copilot-instructions.md`, but the authoring path differs. Use the scaffolding command for the surface the team is working in. The generator handles path, filename, and initial structure; hand-typing is where silent failures live.

| Surface | Command | Notes |
|---------|---------|-------|
| **VS Code** | `/init` in Chat, or `/create-instruction` | Also available through the Chat Customizations editor (gear icon) |
| **GitHub Copilot CLI** | `/init` | Scaffolds `copilot-instructions.md` from codebase analysis |
| **Visual Studio** | `/generateInstructions` | Chat window only; enable under **Tools → Options → GitHub → Copilot** |
| **Cloud Coding Agent** | Assign an issue describing the file | Agent opens a PR for review |
| **Other surfaces** | Author in VS Code or CLI, then commit | All surfaces read the same `.github/` layout |

> 💬 **Try this prompt:**
> "Analyze this repository and create `.github/copilot-instructions.md` with our tech stack, code-style rules, security requirements, and architectural patterns. Flag anything uncertain so I can review."

Small tweaks to an existing file are fine to make by hand. The generator matters most at creation time, when the scaffolding has to be right.

## Complete Example: Production Next.js Project

``````markdown
# Project Guidelines for Copilot

## Project Overview
B2B SaaS platform for inventory management.
Prioritizes reliability over cutting-edge features.

## Architecture
- Next.js 14 App Router
- PostgreSQL with Prisma ORM
- NextAuth.js for authentication
- Stripe for payments

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
  return db.inventory.update({ where: { id: validated.id }, data: validated });
}

// ❌ Bad: No validation, no auth check
export async function updateInventory(data: any) {
  return db.inventory.update({ data });
}
```

## Testing
- Co-locate unit tests: `Component.tsx` → `Component.test.tsx`
- Integration tests in `__tests__/integration/`
- E2E in `e2e/` using Playwright
- Minimum 80% line coverage for `server/`

## Error Handling
Use our custom error hierarchy:
- `AppError` → `ValidationError` (400) → `UnauthorizedError` (401) → `ForbiddenError` (403) → `NotFoundError` (404)

## Security
- All `/app/(auth)/` routes require session
- Use `auth()` from NextAuth, never roll your own
- All queries must include `organizationId` filter
- Validate ALL external input with Zod schemas

## Dependencies — Do Not Use
- `moment.js` → use `date-fns`
- `axios` → use native `fetch`
- `lodash` → use native methods or `es-toolkit`
- Class components → use functional components
``````

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Better Approach |
|--------------|-------------|------------------|
| Typing the file by hand from scratch | Wrong path or filename goes unnoticed | Use `/init` or `/create-instruction` |
| Copy-pasting from another repo | Does not reflect actual local conventions | Generate custom instructions per repo |
| Overly verbose file | Consumes context window, dilutes important rules | Keep to 500-2000 words |
| No rationale | Model cannot make edge-case decisions | Include brief "why" for guidelines |
| Never updating | Instructions drift from actual practice | Review when stack or patterns change |

## Gathering Team Knowledge

Use these questions to surface the most valuable rules:

1. **"What does Copilot frequently get wrong?"** → explicit rules
2. **"What feedback appears repeatedly in PR reviews?"** → guidelines
3. **"What would a new hire need to know on day one?"** → context
4. **"What libraries or patterns have been deprecated?"** → the "avoid" list

> 💬 **Try this prompt:**
> "Review the last 20 merged pull requests. Identify repeated review feedback, common mistakes, style corrections, and recurring architecture concerns. Summarize as candidate rules for `copilot-instructions.md`."

## Instruction Priority

When multiple instruction sources exist, Copilot applies them in this priority order:

1. **Personal instructions** (highest priority)
2. **Repository instructions** (`.github/copilot-instructions.md` or `AGENTS.md`)
3. **Organization instructions** (lowest priority)

All relevant instructions are provided to the model, but higher-priority instructions take precedence when rules conflict.

## Organization-Wide Instructions

Organization-level custom instructions are generally available (April 2, 2026) and apply automatically to every chat session for org members. Disable per-workspace with `github.copilot.chat.organizationInstructions.enabled: false`.

Use organization instructions for company-wide coding standards, compliance requirements, and best practices that should not be duplicated across every repo.

## CLAUDE.md and AGENTS.md Compatibility

VS Code detects `AGENTS.md` as a workspace instruction file alongside `copilot-instructions.md`. It also detects `CLAUDE.md` files, providing compatibility with Claude Code workflows. Teams using multiple AI agents can maintain a single instructions file recognized by all of them.

For monorepos, VS Code supports nested `AGENTS.md` files in subfolders (experimental, via `chat.useNestedAgentsMdFiles`). Each subfolder can carry its own scoped instructions.

If the team opens a package subfolder instead of the repo root, parent-repository discovery is separate. Enable `chat.useCustomizationsInParentRepositories` to load `copilot-instructions.md`, `AGENTS.md`, prompts, skills, agents, and hooks from the parent repository. That setting is off by default.

## Validating the Configuration

To verify the file is working:

1. Open Copilot Chat and ask: "What are the coding standards for this project?"
2. Check that the response references content from the instructions file
3. Generate sample code and verify it follows the rules

If instructions are not applied, check: setting `chat.includeApplyingInstructions` is enabled, the filename is exact, the file is in `.github/`, and the VS Code window has been reloaded.
If `.github/copilot-instructions.md` is not applied, start with the file path, the response References section, and Chat Diagnostics. Reserve `chat.includeApplyingInstructions` for pattern-based instruction files. For `AGENTS.md` and `CLAUDE.md`, also confirm their feature flags are enabled and that parent-repository discovery is enabled when the repo root is outside the open workspace.

**Diagnostics:** Right-click in the Chat view and select **Diagnostics** to see all loaded instruction files, agents, prompts, and skills.

## Where to Read Next

- Read [File-based Instructions](primitive-2-file-based-instructions.md) next for rules that are true only in part of the repo.
- Read [Primitives in Action](primitives-in-action.md) again if the distinction between baseline defaults and scoped defaults is still fuzzy.
