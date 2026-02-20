# File-Based Instructions

[← Always-On Instructions](part-2-1-always-on-instructions.md) | [Part II Overview](part-2-primitives.md) | [Next: Prompt Files →](part-2-3-prompts.md)

---

## Overview

File-based instructions activate through glob pattern matching via the `applyTo` frontmatter field, or through semantic matching of the `description` field to the current task. This allows teams to define area-specific rules that only apply when working in relevant contexts.

**Location:** `.github/instructions/*.instructions.md`

Configure additional search paths with the `chat.instructionsFilesLocations` setting to load instruction files from outside `.github/instructions/` — useful for monorepos or shared instruction libraries.

**Official docs:** [Custom instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)

**See it in action:** [Customize Your Agents](https://www.youtube.com/watch?v=flpKLkZla2Q) — Courtney Webster demonstrates how file-based instructions with `applyTo` patterns provide targeted context for different parts of a codebase. Also in the [Agent Sessions Day livestream](https://www.youtube.com/watch?v=tAezuMSJuFs&t=10598s) at 02:56:38.

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
| `excludeAgent` | String value (`"code-review"` or `"coding-agent"`) — excludes this instruction from the specified agent (GitHub.com only) |

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

1. In the Chat view, click the **gear icon** (Configure Chat)
2. Select an option that opens the instruction file picker
3. Choose **New instruction file...** from the picker
4. Select **Workspace** to store in `.github/instructions/`
5. Use the agent to generate context-specific rules

Alternatively, ask the agent directly:

> 💬 **Try this prompt:**
>
> *Create a file-based instruction at .github/instructions/react-components.instructions.md that applies to src/components/\*\*/\* and includes our React component conventions. Analyze existing components for patterns to document.*

## Anti-Patterns to Avoid

| Anti-Pattern | Why It's Problematic | Better Approach |
|--------------|---------------------|------------------|
| **Overlapping applyTo patterns** | Multiple instructions may conflict | Use specific, non-overlapping patterns |
| **Duplicating always-on rules** | Redundancy, potential conflicts | Only include area-specific additions |
| **Too broad patterns** | Instructions apply unexpectedly | Use precise glob patterns |
| **No description** | Hard to understand what rules apply | Add clear description in frontmatter |

File-based instructions complement always-on instructions by providing contextual specialization.

## More Examples

File-based instructions become powerful when tailored to specific areas of a codebase. The following examples demonstrate common patterns.

### Test Files

**File:** `.github/instructions/test-conventions.instructions.md`

``````markdown
---
name: 'Testing Conventions'
description: 'Test structure, naming, and patterns'
applyTo: '**/*.test.{ts,tsx},**/*.spec.{ts,tsx}'
---

# Testing Standards

## Structure
- Use `describe()` for grouping, `it()` for individual cases (not `test()`)
- Follow Arrange-Act-Assert pattern
- One assertion per test when practical

## Naming
- Describe blocks: noun (the thing under test)
- It blocks: `should [behavior] when [condition]`

## Mocking
- Mock external services only — never mock the module under test
- Use `vi.mock()` for module mocks, `vi.fn()` for function stubs
- Reset mocks in `beforeEach`

## Coverage
- All public functions must have at least one happy-path and one error-path test
``````

### Backend API Routes

**File:** `.github/instructions/backend-api.instructions.md`

``````markdown
---
name: 'Backend API Conventions'
description: 'REST API patterns, validation, and error handling'
applyTo: 'src/api/**/*,src/server/**/*'
---

# Backend API Guidelines

## Response Envelope
All responses use `ApiResponse<T>`:
```typescript
interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: { code: string; message: string };
}
```

## Validation
- Validate every request body with a Zod schema
- Schemas live alongside the route file: `route.ts` + `route.schema.ts`

## Authentication
- All routes under `/api/protected/` require a valid session
- Use the `requireAuth()` middleware — never check `session` manually

## Error Handling
Throw typed errors from our error hierarchy (`ValidationError`, `NotFoundError`, etc.). The global error handler converts them to `ApiResponse` format.
``````

### Infrastructure and Config Files

**File:** `.github/instructions/infrastructure.instructions.md`

``````markdown
---
name: 'Infrastructure Config'
description: 'Rules for CI/CD, Docker, and config files'
applyTo: '**/Dockerfile,**/.github/workflows/**,**/docker-compose*.yml'
---

# Infrastructure Conventions

## Docker
- Use multi-stage builds to minimize image size
- Pin base image versions (e.g., `node:20.11-alpine`, not `node:latest`)
- Run as non-root user in production images

## GitHub Actions
- Pin action versions to full SHA, not tags
- Cache dependencies (`actions/cache`) in every build workflow
- Use environment secrets — never hardcode credentials
``````

### Referencing Tools in Instructions

Instruction files can reference specific tools using the `#tool:` syntax. This tells Copilot which tools to prefer for a given convention:

``````markdown
---
name: 'Database Migration Conventions'
applyTo: 'src/db/migrations/**'
---

# Database Migrations

- After creating a migration, run it with #tool:runInTerminal using `npx prisma migrate dev`
- Use #tool:search to check for existing migrations that touch the same table
- Always generate a rollback script alongside the migration
``````

Tool references help Copilot connect _what_ to do with _how_ to do it.

## File-Based Instructions vs. Skills

File-based instructions and skills have overlapping use cases. Both can provide context-specific knowledge to Copilot — file-based instructions activate by file pattern, skills activate by description matching.

**Quick guidance:**
- **File-based instructions**: Best for rules tied to specific file locations that won't be reused elsewhere
- **Skills**: Best for reusable knowledge that applies across multiple contexts, or when you need supporting files (templates, scripts)

There's no definitively "right" choice — this space is still evolving. For a detailed exploration of when to use each, see [Skills vs. File-Based Instructions: Overlapping Territory](part-2-4-skills.md#skills-vs-file-based-instructions-overlapping-territory).

---

[← Always-On Instructions](part-2-1-always-on-instructions.md) | [Next: Prompt Files →](part-2-3-prompts.md)
