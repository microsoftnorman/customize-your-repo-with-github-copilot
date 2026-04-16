# File-Based Instructions

[← Always-On Instructions](primitive-1-always-on-instructions.md) | [Part II Overview](part-2-primitives.md)

---

**Surface availability:** VS Code ✅ · JetBrains (Preview) · GitHub Copilot CLI ✅ · Visual Studio — · Eclipse — · Cloud Agent —

**Ownership:** **Application teams** own file-based instructions for their own code areas. In a monorepo, each package team owns the instructions under its folder; shared rules live in the root.

## Overview

File-based instructions activate through glob pattern matching via the `applyTo` frontmatter field, or through semantic matching of the `description` field to the current task. This allows teams to define area-specific rules that only apply when working in relevant contexts.

**Location:** `.github/instructions/*.instructions.md`

**Official docs:** [Custom instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)

**See it in action:** For a live demo, watch Courtney Webster in [Customize Your Agents](https://www.youtube.com/watch?v=flpKLkZla2Q).

**Use Cases:**
- Different conventions for frontend vs. backend code
- Specialized rules for test files
- Language-specific guidelines in a monorepo
- Framework-specific patterns for different modules

## File Format

File-based instructions use the `.instructions.md` extension with YAML frontmatter:

| Field | Description |
|-------|-------------|
| `description` | Description shown on hover in Chat view; also used for semantic matching to the current task |
| `name` | Display name (defaults to filename) |
| `applyTo` | Glob pattern for automatic application |

## Example

**File:** `.github/instructions/api-routes.instructions.md`

``````markdown
---
name: 'API Route Guidelines'
description: 'Conventions for REST API endpoints'
applyTo: 'src/api/**/*'
---

# Instructions for API Routes

## API-Specific Rules
- All routes must include authentication middleware
- Use standardized error response format
- Include OpenAPI documentation comments
- Rate limiting is required for public endpoints

## Response Format
All API responses must use this shape:
```typescript
interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: { code: string; message: string; };
}
```

## Error Handling
```typescript
// ✅ Good: Standardized error response
return NextResponse.json({ 
  success: false, 
  error: { code: 'NOT_FOUND', message: 'Resource not found' }
}, { status: 404 });

// ❌ Bad: Inconsistent error format
return NextResponse.json({ error: 'Not found' }, { status: 404 });
```
``````

## Creating File-Based Instructions

Not every Copilot surface supports file-based instructions with glob-based `applyTo` matching. Where they are supported, each surface offers a different authoring path — the resulting `.instructions.md` file is identical and version-controlled in the repository.

### VS Code

VS Code has first-class support for `.instructions.md` files, including automatic selection by glob pattern and hover previews in the Chat view.

1. In the Chat view, click the **gear icon** (Configure Chat)
2. Select **Chat Instructions** > **New instruction file...**
3. Choose **Workspace** to store in `.github/instructions/` (committed to version control) or **User Profile** for personal-only rules
4. Enter a filename (e.g., `api-routes.instructions.md`) and author the rules, or let the agent fill them in

**Agent-driven generation works equally well:**

> **💬 Try this prompt:**
>
> *Create a file-based instruction at .github/instructions/react-components.instructions.md that applies to src/components/\*\*/\* and includes our React component conventions. Analyze existing components for patterns to document.*

Configure additional search paths with the `chat.instructionsFilesLocations` setting to load instruction files from outside `.github/instructions/` — useful for monorepos or shared instruction libraries.

### JetBrains IDEs (Preview)

JetBrains support for file-based instructions is in preview. The plugin reads `.github/instructions/*.instructions.md` and matches them against the files under discussion, the same way VS Code does. Authoring paths:

- **In the IDE:** Create the file directly in the Project view under `.github/instructions/` and add the YAML frontmatter (`description`, `applyTo`) by hand.
- **Using the agent:** Ask the Copilot chat panel to generate an instructions file with the prompt above — the generated file will be written to the repo and picked up automatically.

See [IDE Surfaces — JetBrains](surfaces.md#jetbrains-ides) for the current primitive status and verification steps.

### GitHub Copilot CLI

The [GitHub Copilot CLI](https://github.com/github/copilot-cli) supports path-specific instruction files (`.github/instructions/**/*.instructions.md`) and loads matching instructions on every session. There is no dedicated authoring command — create files manually or ask the CLI's agent to generate one:

```bash
copilot
```

```
> Create .github/instructions/api-routes.instructions.md with applyTo
> 'src/api/**/*' documenting our REST API conventions based on existing code.
```

### Surfaces That Don't Support File-Based Instructions

Not every surface honors glob-scoped instructions today. On surfaces without native support (notably **Visual Studio**, **Xcode**, **Eclipse**, and **cloud coding agent** runs before matching files are in context), fold area-specific rules into the root `.github/copilot-instructions.md` file instead, or keep the `.instructions.md` files in place so that VS Code, JetBrains, and CLI contributors still benefit. See [Part III: Reference](part-3-reference.md) for the current primitive-by-surface support matrix.

## Anti-Patterns to Avoid

| Anti-Pattern | Why It's Problematic | Better Approach |
|--------------|---------------------|------------------|
| **Overlapping applyTo patterns** | Multiple instructions may conflict | Use specific, non-overlapping patterns |
| **Duplicating always-on rules** | Redundancy, potential conflicts | Only include area-specific additions |
| **Too broad patterns** | Instructions apply unexpectedly | Use precise glob patterns |
| **No description** | Hard to understand what rules apply | Add clear description in frontmatter |

### More Examples by Language

File-based instructions are not just for TypeScript. Use them wherever a file-type or folder has distinct conventions.

**React components (`**/*.tsx` excluding tests):**

```yaml
---
name: 'React Component Conventions'
description: 'TSX component, props, and hook conventions for the web app'
applyTo: 'src/components/**/*.tsx,!src/**/*.test.tsx'
---

- Functional components only — never class components.
- Props interface named `<Component>Props`, exported alongside the component.
- Prefer composition over prop-drilling; lift shared state into a custom hook in `src/hooks/`.
- No inline `style={{ ... }}` — Tailwind utility classes or CSS modules only.
- Event handlers prefixed with `handle` (`handleSubmit`, `handleChange`).
- Fetch data via TanStack Query hooks — never `useEffect` + `fetch`.
```

**Test files (`**/*.test.*` and `**/*.spec.*`):**

```yaml
---
name: 'Test File Conventions'
description: 'Unit, integration, and component test conventions'
applyTo: '**/*.test.ts,**/*.test.tsx,**/*.spec.ts,**/*.spec.tsx'
---

- Use Vitest (`describe`, `it`, `expect`) — never Jest or Mocha.
- For React components, use Testing Library; query by accessible role before test IDs.
- No snapshot tests for component output — assert on behavior, not markup.
- Mock external calls with `vi.mock` at module scope; avoid manual `jest.fn()`-style mocks.
- Each `describe` block covers one unit; use `it.each` for table-driven cases.
- No conditional logic (`if`/`for`) inside test bodies — split into separate cases.
```

**iOS (`**/*.swift`):**

```yaml
---
name: 'Swift Conventions'
description: 'SwiftUI view and view-model conventions for iOS'
applyTo: '**/*.swift'
---

- SwiftUI views are structs; keep them under 150 lines and extract subviews into their own files.
- View-models conform to `ObservableObject` and live in `ViewModels/`; never put business logic in a `View`.
- Use `@MainActor` on view-models that mutate UI state; mark async boundaries with `async`/`await`, not completion handlers.
- Networking goes through `URLSession` wrapped in a protocol-backed client — no singleton `NetworkManager.shared`.
- Prefer `Result<Success, Error>` return types over throwing initializers for recoverable failures.
- No force-unwraps (`!`) outside of unit tests; use `guard let` or `if let` with a typed error.
```

**Android / Kotlin (`**/*.kt`):**

```yaml
---
name: 'Kotlin Conventions'
description: 'Kotlin coroutines and Jetpack Compose conventions'
applyTo: '**/*.kt,**/*.kts'
---

- Composables are `@Composable fun` in PascalCase; state hoisting over internal `remember` where callers need control.
- Use `StateFlow` / `SharedFlow` for view-model state; never `LiveData` in new code.
- Launch coroutines on `viewModelScope` or an injected `CoroutineScope` — no `GlobalScope`.
- Prefer `Result<T>` or sealed-class results over throwing from suspend functions.
- Dependencies flow through Hilt modules; no service locators or `object Singleton`s.
- Null-safety: no `!!`; use `requireNotNull`, `checkNotNull`, or elvis with a typed fallback.
```

**Python data science (`**/*.ipynb` notebooks and `**/*.py` pipelines):**

```yaml
---
name: 'Python Data Science Conventions'
description: 'pandas, notebook hygiene, and reproducibility rules for analytics code'
applyTo: '**/*.ipynb,src/analysis/**/*.py'
---

- Use `pandas` with explicit dtypes; never infer dtypes from CSV without specifying `dtype=`.
- Notebooks must be stripped of outputs before commit — enforce with `nbstripout` as a pre-commit hook.
- Seed every random process: `np.random.seed(42)`, `torch.manual_seed(42)`. No un-seeded randomness in analysis cells.
- Prefer vectorized pandas ops over `.apply(lambda ...)`; flag any `.iterrows()` as a review blocker.
- Import order: stdlib → third-party → local, one import per line; no `from module import *`.
- Plot with `matplotlib` or `seaborn`; every chart must have a title, axis labels, and a caption cell explaining what it shows.
```

**.NET / C# (`**/*.cs` — Visual Studio + VS Code):**

```yaml
---
name: 'C# Conventions'
description: 'Modern C# 12+ patterns for .NET 8 services'
applyTo: '**/*.cs'
---

- Target .NET 8; enable nullable reference types (`<Nullable>enable</Nullable>`) in every project.
- Prefer `record` for DTOs and value objects; `class` only when identity or mutation is required.
- Use primary constructors and collection expressions (`[..]`) on C# 12+; avoid legacy constructor boilerplate.
- Async methods end in `Async`, return `Task`/`Task<T>`, and always accept a `CancellationToken` — no fire-and-forget `async void` outside event handlers.
- Dependency injection through constructor parameters only; no service locator or `new` inside business logic.
- Use `ILogger<T>` with structured logging templates (`"User {UserId} signed in"`) — never string interpolation into log messages.
```

**Go (`**/*.go`):**

```yaml
---
name: 'Go Conventions'
description: 'Idiomatic Go for services and CLIs'
applyTo: '**/*.go'
---

- Follow `gofmt` and `go vet`; no linter disables without a `//nolint:<rule> // reason` comment.
- Errors are values — return them, don't panic in library code. Wrap with `fmt.Errorf("context: %w", err)` to preserve the chain.
- Accept `context.Context` as the first parameter on every exported function that does I/O; propagate it through every call.
- Prefer small interfaces defined at the call site; avoid `interface{}` — use generics (Go 1.21+) for containers.
- Package names are lowercase, short, and singular (`user`, not `users` or `UserPackage`).
- No `init()` functions for business logic; reserve `init()` for flag registration and package-local setup that cannot be done lazily.
```

**SQL / dbt (`**/*.sql` — warehouse and transformation layer):**

```yaml
---
name: 'SQL and dbt Conventions'
description: 'Warehouse SQL style, dbt model structure, and review-friendly query patterns'
applyTo: 'models/**/*.sql,analysis/**/*.sql'
---

- Keywords UPPERCASE, identifiers lowercase with `snake_case`; CTEs named descriptively (`active_users`, not `cte1`).
- Every dbt model has a `schema.yml` entry with a description and at least one test (`not_null` on primary keys, `unique` where applicable).
- Prefer CTEs over nested subqueries; one CTE per logical step, read top-to-bottom.
- Always qualify column references with the table or CTE alias in any join — no bare column names in multi-table queries.
- No `SELECT *` in final SELECT blocks; enumerate columns so schema drift surfaces at compile time.
- Window functions over correlated subqueries where semantically equivalent; comment the partition/order rationale.
```

The same pattern extends to any file type: write one `.instructions.md` per distinct convention, target it narrowly with `applyTo`, and keep shared rules in the always-on instructions file.

### Monorepos

In a monorepo with one Git root and many packages, file-based instructions layer naturally. Enable `chat.useCustomizationsInParentRepositories` so that instructions at the repo root apply to all packages, while package-specific instructions under `packages/<name>/.github/instructions/` add contextual rules. VS Code merges both sets when a file matches.

### File-Based Instructions vs. Skills

File-based instructions and skills have overlapping use cases. Both can provide context-specific knowledge to Copilot — file-based instructions activate by file pattern, skills activate by description matching.

**Quick guidance:**
- **File-based instructions**: Best for rules tied to specific file locations that won't be reused elsewhere
- **Skills**: Best for reusable knowledge that applies across multiple contexts, or when you need supporting files (templates, scripts)

There's no definitively "right" choice — this space is still evolving. For a detailed exploration of when to use each, see [Skills vs. File-Based Instructions: Overlapping Territory](primitive-4-skills.md#skills-vs-file-based-instructions-overlapping-territory).

---

[← Always-On Instructions](primitive-1-always-on-instructions.md) | [Next: Prompt Files →](primitive-3-prompts.md)
