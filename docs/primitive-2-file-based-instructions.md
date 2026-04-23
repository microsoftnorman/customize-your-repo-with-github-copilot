# Primitive 2: File-based Instructions

[← Back to The Eight Primitives](eight-primitives.md) | [← Always-on Instructions](primitive-1-always-on-instructions.md) | [Next: Prompts →](primitive-3-prompts.md)

*Updated: April 22, 2026.*

---

## Where It Enters the Loop

File-based Instructions enter the same place as Always-on Instructions, but with narrower scope.

They change context assembly only when matching files matter. That means the loop starts with different rules for an API route than it does for a React component, a Swift view, or a test file.

That is the whole point. A repository with multiple languages, frameworks, or architectural zones should not force one global instructions file to carry every local exception.

## What This Primitive Is For

Use File-based Instructions when a rule is true for one slice of the tree and not for the repo as a whole.

Typical examples:

- frontend versus backend conventions,
- test-only rules,
- language-specific monorepo standards,
- route-handler expectations,
- infrastructure-as-code conventions,
- notebook or data science hygiene.

The question this primitive answers is: "What should GitHub Copilot know when these files are in play that it should not assume everywhere else?"

## The Key Difference from Always-on Instructions

Always-on Instructions say, "This is how the repo generally works."

File-based Instructions say, "This is how this part of the repo works."

That sounds small, but it is one of the biggest practical upgrades a team can make. It keeps the global file short while still letting local areas encode strong rules.

## How It Loads

The main mechanism is `applyTo` in the frontmatter.

```markdown
---
name: 'API Route Guidelines'
description: 'Conventions for REST API endpoints'
applyTo: 'src/api/**/*'
---
```

When matching files are relevant to the task, the instructions load into context. When they are not, the file stays dormant.

That is why this primitive usually improves signal quality more than simply making the global instructions file longer.

## When to Reach for It

Reach for File-based Instructions when:

- a repeated review comment only applies to one folder,
- one area of the repo uses a different framework or data flow,
- one language needs rules the rest of the repo would find noisy,
- or a team keeps stuffing path-specific details into Always-on Instructions.

Do not reach for it when the rule is actually a procedure. If the knowledge reads like steps, it is probably a Skill or Prompt instead.

## What Good File-based Instructions Look Like

Strong file-based rules are narrow, concrete, and obviously tied to the files they target.

```markdown
---
name: 'React Component Conventions'
description: 'TSX component, props, and hook conventions for the web app'
applyTo: 'src/components/**/*.tsx'
---

- Functional components only.
- Export a `<Component>Props` interface next to the component.
- Fetch data through existing query hooks, not `useEffect` + `fetch`.
- Prefer composition over prop drilling.
```

Weak file-based instructions usually fail in one of three ways:

- the glob is too broad,
- the rules duplicate the global file,
- or the content is so generic that it would have been better as Always-on Instructions.

## The Main Failure Mode

This primitive fails silently more often than any other authored primitive.

Wrong filename, wrong folder, wrong glob, or a badly quoted `applyTo` pattern can all leave the file unused with no obvious warning. That is why generated scaffolding matters here more than it does for most plain Markdown files.

Start with generated structure, then refine the rules.

> 💬 **Try this prompt:**
> "Create `.github/instructions/react-components.instructions.md` targeting `src/components/**/*.tsx` and derive the conventions from the existing components in this repo instead of inventing new ones."

## How It Composes with Other Primitives

| Primitive | Relationship |
|-----------|--------------|
| [Always-on Instructions](primitive-1-always-on-instructions.md) | Provide the repo-wide floor that this file narrows or extends |
| [Prompts](primitive-3-prompts.md) | Task templates run on top of whatever scoped instructions match |
| [Skills](primitive-4-skills.md) | Skills can provide procedure while File-based Instructions provide file-local conventions |
| [Code Review](code-review.md) | Path-scoped rules are especially valuable in review because they only fire where they should |

## When It Beats Growing the Global File

If the global instructions file starts reading like a directory tour, stop and split.

Examples that usually deserve File-based Instructions:

- test style and naming,
- API response envelopes,
- component structure rules,
- mobile-platform specifics,
- infrastructure modules,
- notebooks and analysis code.

The result is better than one giant instructions file for two reasons: less noise in the loop, and clearer ownership for the teams who maintain different areas of the codebase.

## Surface Reality

This primitive is portable at the repository level, but not every surface honors it equally today. That matters because a team may author the file once but consume it across multiple environments.

That portability story belongs partly here and partly in the surface guides. The practical reading is simpler: keep the file in the repo, then verify the target surface actually supports scoped instructions before treating it as universal.

## See It in Action

**See it in action:** [Customize your agents](https://www.youtube.com/watch?v=flpKLkZla2Q&t=67s) — Courtney Webster demos file-based instructions as scoped, pattern-matched rules for areas like Python files and tests.

## Where to Read Next

- Read [Prompts](primitive-3-prompts.md) next for explicit task framing.
- Read [Operational Reference](part-3-reference.md) later for exact frontmatter and support-matrix details.
