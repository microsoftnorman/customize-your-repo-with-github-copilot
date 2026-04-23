# GitHub Copilot Code Review

[← Copilot SDK](copilot-sdk.md) | [Part II Overview](part-2-primitives.md) | [Part III Reference →](part-3-reference.md)

*Updated: April 22, 2026 · Validated against GitHub Copilot docs as of April 16, 2026.*

---

## Overview

Read this page as "the same repository rules, but applied to pull request review." Code review is not a separate customization system. It is another place where GitHub Copilot consumes the instruction layer and repository memory, then turns that context into comments instead of chat replies or code edits.

**Where it runs:** GitHub.com pull request reviews, VS Code (review selection), Visual Studio, JetBrains, Xcode, GitHub CLI, GitHub Mobile
**Best for:** Automated first-pass review of PRs against team conventions, security rules, and architectural standards

**Official docs:** [Using GitHub Copilot code review](https://docs.github.com/en/copilot/how-tos/agents/copilot-code-review/using-copilot-code-review) · [Repository custom instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions) · [About GitHub Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review)

[GitHub Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review) is a cross-cutting feature, not a primitive. It consumes the same instruction files and memory that shape Copilot's behavior in chat and agent mode, and it surfaces that customization as pull request comments. When the rules are specific, it catches the routine issues before a human reviewer sees the diff: convention drift, missing error handling, security smells. That frees human review time for design and correctness.

This guide is **customization-focused**: how the [eight primitives](part-2-primitives.md) steer what Copilot flags in reviews. For enablement, billing, and organization-level policy, defer to the [official docs](https://docs.github.com/en/copilot/concepts/agents/code-review).

---

## How Code Review Reads Your Customization

Copilot code review reads customization files the same way chat and agent mode do, with a few specifics:

- **Base branch wins.** Copilot reviews a pull request using the instruction files on the **base branch**, not the feature branch. A contributor cannot change the review rules in their own PR.
- **Character budget.** Copilot code review reads up to the first **4,000 characters** of each custom instruction file. Content beyond that is ignored. Splitting long content into path-scoped `.instructions.md` files keeps each scope focused, and every file has its own 4,000-character window.
- **All scopes are provided, with priority ordering.** [Personal instructions take highest priority, then repository, then organization](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions), but all relevant sets are passed to Copilot. Don't think of precedence as override; think of it as conflict resolution when rules disagree.
- **Opt out per file with `excludeAgent`.** Path-scoped instruction files can set `excludeAgent: "code-review"` in frontmatter to skip code review entirely (still available to the cloud agent), or `excludeAgent: "cloud-agent"` for the reverse. Use it to keep chat-only rules out of review comments.
- **Toggle at the repository.** Custom instructions for code review can be disabled per-repository from **Settings → Copilot → Code review → “Use custom instructions when reviewing pull requests”** without removing the files.
- **Review type is “Comment” only.** Copilot leaves suggestions as review comments. It does not approve, request changes, or block merges, and its reviews do not count toward required-approval thresholds.

See the [repository custom instructions guide](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions) for the authoritative reference on file locations, `applyTo` globs, `excludeAgent`, and base-branch behavior.

---

## Primitive-by-Primitive Leverage

Not every primitive affects code review today. The sections below expand the four that do.

| Primitive | Affects code review? | How |
|-----------|----------------------|-----|
| [Always-on Instructions](primitive-1-always-on-instructions.md) | ✅ Yes | First 4,000 chars of `copilot-instructions.md` / `AGENTS.md` are included as review context |
| [File-based Instructions](primitive-2-file-based-instructions.md) | ✅ Yes | `applyTo` globs activate path-specific rules when reviewing matching files |
| [Custom Agents](primitive-5-custom-agents.md) | Indirect | Reviewer personas don't auto-run in PRs today, but the instruction files they reference do influence reviews |
| [Copilot Memory](primitive-8-memory.md) | ✅ Yes | Learned repository patterns carry into review comments |
| [Prompts](primitive-3-prompts.md) | ❌ No | Prompts are invoked by humans in chat; reviews are non-interactive |
| [Skills](primitive-4-skills.md) | ❌ No (today) | Skills are discovered during agent sessions, not PR reviews |
| [MCP](primitive-6-mcp.md) | ❌ No (today) | External tools are not invoked during code review |
| [Hooks](primitive-7-hooks.md) | ❌ No | Hooks govern local agent sessions, not cloud review |

### Always-on instructions

Use [`copilot-instructions.md`](primitive-1-always-on-instructions.md) (or `AGENTS.md`) for universal conventions every review should enforce: logging requirements, error handling patterns, forbidden APIs, naming rules. Keep each file tight: Copilot code review reads only the first 4,000 characters of any given custom instruction file.

✅ **Good:** specific and testable
```markdown
## Error handling
- Every `async` function must wrap its body in try/catch and log errors via `logger.error` with a stable code prefix (e.g. `ERR_AUTH_001`).
- Never swallow errors silently. If an error is intentionally ignored, add a `// intentional:` comment explaining why.
```

❌ **Bad:** vague and unreviewable
```markdown
## Error handling
- Handle errors properly.
- Write clean code.
```

Copilot has no way to act on the second example in a review comment. There's no concrete rule to compare the diff against.

### File-based instructions

Path-scoped instructions under [`.github/instructions/*.instructions.md`](primitive-2-file-based-instructions.md) are the sharpest tool for code review. The `applyTo` glob pattern means rules only activate when the reviewed file matches. Your security rules don't fire on test fixtures, and your test-style rules don't fire on production code.

```markdown
---
applyTo: "src/auth/**/*.ts"
---

# Authentication review rules

- Never log request bodies, tokens, session IDs, or password fields.
- All session comparisons must use constant-time comparison (`crypto.timingSafeEqual`).
- Authorization checks must happen before any database mutation.
- New endpoints must document the permission they require in a JSDoc `@permission` tag.
```

A PR that touches `src/auth/session.ts` picks up these rules automatically; a PR that only changes `tests/**` does not.

### Custom agents (indirect)

Copilot code review does not run [custom agents](primitive-5-custom-agents.md) as part of a PR today. A `security-reviewer.agent.md` persona won't auto-assign itself. But the underlying instruction files that back that agent (always-on and path-scoped) are still read. The practical pattern: extract the *rules* from the reviewer persona into a path-scoped `.instructions.md` file so they flow to code review, and keep the *workflow* in the agent file for interactive chat use.

### Copilot Memory

[Copilot Memory (Preview)](primitive-8-memory.md) observes interactions across a repository and surfaces learned patterns as context in future sessions, including code review. A team that has corrected the same review comment across dozens of PRs will find Copilot starts flagging that pattern without it being written anywhere explicitly. Memory complements instruction files; it does not replace them. Explicit instructions are deterministic, auditable, and versioned with the repo. Memory is implicit and mutable. Use both.

---

## Surface Support

Copilot code review runs in multiple places, but the feature set differs by surface. The canonical matrix lives in the [official feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix); the summary below is a sanity check as of April 2026.

| Surface | PR review (github.com) | In-IDE review of local changes |
|---------|------------------------|--------------------------------|
| [GitHub.com](https://docs.github.com/en/copilot/concepts/agents/code-review) | ✅ Primary | — |
| [GitHub Mobile](https://docs.github.com/en/copilot/concepts/agents/code-review) | ✅ | — |
| [GitHub CLI](surfaces/copilot-cli.md) | ✅ (via `gh` PR commands) | — |
| [VS Code](surfaces/vscode.md) | ✅ (from PR UI) | ✅ "Review selection" (see [VS Code Copilot settings](https://code.visualstudio.com/docs/copilot/reference/copilot-settings)) |
| [Visual Studio](surfaces/visual-studio.md) | ✅ | ✅ |
| [JetBrains](surfaces/jetbrains.md) | ✅ | See the [JetBrains surface notes](surfaces/jetbrains.md) |
| [Xcode](surfaces/xcode.md) | ✅ | — |

Copilot code review is not listed as an available surface for Eclipse; Eclipse users can still request reviews from github.com in a browser. Verify current availability against the [official availability list](https://docs.github.com/en/copilot/concepts/agents/code-review#availability).

**VS Code editor review** is configured via settings under `github.copilot.chat.reviewSelection.*`. See [VS Code Copilot settings reference](https://code.visualstudio.com/docs/copilot/reference/copilot-settings). This is separate from PR review on github.com, but both read your repository's instruction files.

---

## 💬 Try This Prompt

> 💬 **Try this prompt:**
>
> Read the top files under `src/` and the existing `.github/copilot-instructions.md`. Draft a companion file at `.github/instructions/review-rules.instructions.md` with `applyTo: "src/**/*.{ts,tsx}"` that captures the non-obvious conventions a human reviewer would catch in this codebase: error handling, logging, auth, and data access patterns. Keep each rule specific enough that a code review tool could cite a line of diff against it. Do not duplicate rules already in `copilot-instructions.md`.

Run this once per directory tree with distinct conventions (backend, frontend, infra, tests). The output becomes the starting point for path-scoped review rules you can refine over the next few PRs.

---

## Patterns That Work

1. **One file, one applyTo scope.** Don't try to capture every rule in `copilot-instructions.md`. Split by directory or stack: `frontend.instructions.md`, `api.instructions.md`, `db.instructions.md`. Each stays focused and well under the character cap.
2. **Write rules as diff-citable statements.** Every rule should be specific enough that Copilot can point at a line of code and say "this violates it." If a rule requires interpretation, a human reviewer will need to apply it anyway.
3. **Prefer allow/forbid lists over philosophy.** "Use `pino` for logging; do not import `console.*` or `winston`" outperforms "Use structured logging."
4. **Mirror the review you wish you didn't have to give.** The best source of review rules is the review comments you keep re-typing. Grep your PR history for repeat patterns and codify them.
5. **Version the rules with the repo.** Instruction files live in `.github/` and ship with the code. When a rule changes, it changes in a PR, so the change itself goes through review.

---

## Limitations

- **4,000 character cap per instruction file.** Copilot code review reads only the first 4,000 characters of each custom instruction file it consumes. Split large content into focused path-scoped files under `.github/instructions/`.
- **No merge blocking.** Copilot reviews are Comment-only. Enforcement of any rule still requires a human reviewer, branch protection, or a CI check.
- **Model is not switchable.** Unlike chat and agent mode, code review uses a [tuned mix of models](https://docs.github.com/en/copilot/concepts/agents/code-review#model-usage) and does not expose a model selector.
- **Re-review may repeat comments.** When you re-request review after changes, Copilot may repeat comments you previously resolved. See the [official docs](https://docs.github.com/en/copilot/concepts/agents/code-review) for current behavior.
- **Skills, MCP, and hooks do not participate in code review today.** Plan customization for review around instructions and memory.
- **Some file types are excluded.** Dependency manifests, log files, and SVGs are skipped. See [Files excluded from code review](https://docs.github.com/en/copilot/reference/review-excluded-files).

---

## Further Reading

- [About GitHub Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review): overview, availability, automatic reviews, quotas, and model behavior
- [Using GitHub Copilot code review](https://docs.github.com/en/copilot/how-tos/agents/copilot-code-review/using-copilot-code-review): how to request, configure, and interpret reviews
- [Repository custom instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions): `applyTo`, `excludeAgent`, base-branch resolution, and the code-review toggle
- [Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix): per-surface support grid
- [VS Code Copilot settings reference](https://code.visualstudio.com/docs/copilot/reference/copilot-settings): `reviewSelection` and related editor settings

---

[← Copilot SDK](copilot-sdk.md) | [Part II Overview](part-2-primitives.md) | [Part III Reference →](part-3-reference.md)
