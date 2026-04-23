# GitHub Copilot Code Review

[← Back to Guide](README.md) | [← GitHub Copilot SDK](copilot-sdk.md) | [Next: Where GitHub Copilot Runs →](where-github-copilot-runs.md)

*Updated: April 22, 2026.*

---

## What This Page Covers

Code review is what the same repository knowledge looks like when the output is a review comment instead of a chat reply, code edit, or tool-driven task.

For current behavior and setup, GitHub's canonical references are [About GitHub Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review) and [Request a code review](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review).

That is why this page belongs with the cross-runtime chapters instead of with the primitives themselves.

## Why This Matters

Teams often discover their strongest customization candidates in review first.

The same comments appear again and again:

- wrong library choice,
- missing error handling,
- inconsistent logging,
- auth checks in the wrong place,
- architecture drift in one subsystem.

Code review is where repeated friction becomes visible enough to encode.

It is also where the value of good repository-level customization becomes easiest to prove to skeptical teams: fewer routine comments, faster first-pass review, and more human attention left for design and correctness.

## How Code Review Reuses the Primitive Layer

Code review does not run the full primitive set equally.

The important distinction is not just which files exist. It is which parts of repository knowledge the review environment can actually consume.

The strongest inputs today are:

- **Always-on Instructions** for universal review rules,
- **File-based Instructions** for path-specific review logic,
- **Memory** for learned repository patterns,
- and, more indirectly, the instruction logic that may also support reviewer-style agents elsewhere.

That is why this page matters strategically. It shows which authored knowledge pays off across local agent sessions and pull request review at the same time.

## What Changes in Review Compared with Local Agent Sessions

Review is narrower and more static.

The runtime is looking at a diff, not carrying out an open-ended task. It is not discovering new tools midstream. It is not following a long interactive conversation. It is comparing changed code against repository expectations.

That means clarity wins.

If a rule cannot be translated into a diff-citable comment, it is less likely to help in review. This is why path-scoped instructions are often the highest-value review primitive: they make expectations specific enough to apply to the changed files in front of the model.

## Why Base-Branch Behavior Matters

One of the most practically important details in the current guide is that review consumes the instruction layer from the base branch rather than trusting the contributor's feature branch to rewrite the rules.

That design matters because it keeps the review policy anchored in already-accepted repository standards.

The broader lesson is architectural: review is not just another chat surface. It is a policy-sensitive environment.

## The Best Review-Oriented Customization Pattern

The most reliable pattern is:

1. Put repository-wide expectations in Always-on Instructions.
2. Move domain-specific rules into File-based Instructions by path.
3. Keep each review-relevant rule concrete enough to cite against a diff.
4. Let Memory reinforce the patterns the repository keeps teaching over time.

That pattern is stronger than trying to make one global document carry the whole review culture.

## What Review Does Not Replace

Code review is not enforcement, and it is not the same thing as Hooks or branch protection.

It can surface issues. It can reduce human toil. It can make repository knowledge operational. It does not block merges by itself, and it does not replace the need for CI, branch policy, or runtime controls.

That distinction keeps this page aligned with one of the core values of this guide: be direct about what each mechanism can and cannot do.

## Why This Chapter Belongs Here

This chapter exists to make a broader point visible:

the repository does not only teach GitHub Copilot how to write code. It also teaches GitHub Copilot how to read and critique changes.

That is one of the clearest reasons to think of customization as shared infrastructure instead of as better prompting.

## How Code Review Reads Customization in Detail

Copilot code review reads customization files the same way chat and agent mode do, with a few specifics:

- **Base branch wins.** Review uses instruction files on the **base branch**, not the feature branch. A contributor cannot change the review rules in their own PR.
- **Character budget.** Copilot code review reads up to the first **4,000 characters** of each custom instruction file. Content beyond that is ignored. Splitting into path-scoped `.instructions.md` files keeps each scope focused.
- **All scopes are provided, with priority ordering.** Personal instructions take highest priority, then repository, then organization.
- **Opt out per file with `excludeAgent`.** Path-scoped instruction files can set `excludeAgent: "code-review"` in frontmatter to skip code review entirely, or `excludeAgent: "cloud-agent"` for the reverse.
- **Toggle at the repository.** Custom instructions for code review can be disabled per-repository from **Settings → Copilot → Code review** without removing the files.
- **Review type is "Comment" only.** Copilot leaves suggestions as review comments. It does not approve, request changes, or block merges.

## Primitive-by-Primitive Leverage

Not every primitive affects code review today:

| Primitive | Affects review? | How |
|-----------|----------------|-----|
| Always-on Instructions | ✅ Yes | First 4,000 chars included as review context |
| File-based Instructions | ✅ Yes | `applyTo` globs activate path-specific rules for matching files |
| Memory | ✅ Yes | Learned patterns carry into review comments |
| Custom Agents | Indirect | Agent instruction files still influence reviews even though agents do not auto-run in PRs |
| Prompts | ❌ No | Prompts are user-invoked; reviews are non-interactive |
| Skills | ❌ No (today) | Skills are discovered during agent sessions, not PR reviews |
| MCP | ❌ No (today) | External tools are not invoked during review |
| Hooks | ❌ No | Hooks govern local agent sessions, not cloud review |

### Writing Review-Effective Instructions

✅ **Good:** specific and testable

```markdown
## Error handling
- Every `async` function must wrap its body in try/catch and log errors via `logger.error` with a stable code prefix (e.g. `ERR_AUTH_001`).
- Never swallow errors silently.
```

❌ **Bad:** vague and unreviewable

```markdown
## Error handling
- Handle errors properly.
- Write clean code.
```

### Path-Scoped Review Rules

```markdown
---
applyTo: "src/auth/**/*.ts"
---

# Authentication review rules
- Never log request bodies, tokens, session IDs, or password fields.
- All session comparisons must use constant-time comparison.
- Authorization checks must happen before any database mutation.
```

A PR that touches `src/auth/session.ts` picks up these rules automatically; a PR that only changes `tests/**` does not.

## Where to Read Next

- Read [Where GitHub Copilot Runs](where-github-copilot-runs.md) next for the broader surface picture.
- Revisit [File-based Instructions](primitive-2-file-based-instructions.md) if you want the highest-leverage authored primitive for review-specific improvement.
