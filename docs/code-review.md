# GitHub Copilot Code Review

[← Back to Guide](../ReadMe.md) | [← GitHub Copilot SDK](copilot-sdk.md) | [Next: Where GitHub Copilot Runs →](where-github-copilot-runs.md)

*Updated: May 4, 2026.*

---

## What This Page Covers

Code review is what the same repository knowledge looks like when the output is a review comment instead of a chat reply, code edit, or tool-driven task.

For current behavior and setup, GitHub's canonical references are [About GitHub Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review) and [Request a code review](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review).

**See it in action:** [Multi-agent development in VS Code](https://www.youtube.com/watch?v=BsAHunfVwNs&t=156s) — Olivia Guzzardo McVicker demos running GitHub Copilot code review from the Source Control flow after reviewing generated agent changes.

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

Review is purpose-built, not tool-less.

The dedicated GitHub Copilot code review product runs a review pipeline whose job is to produce comments on changed code. It is not the same as a local chat session where the user can freely add tools, invoke Skills, attach prompts, or steer a multi-turn implementation. It does, however, run on an agentic tool-calling architecture that can gather broader project context and uses GitHub Actions runners for review execution.

That distinction matters for rollout planning. Treat dedicated review as a controlled service-side reviewer, not as the local agent loop with every local tool exposed and not as a static diff linter.

That means clarity wins.

If a rule cannot be translated into a diff-citable comment, it is less likely to help in review. This is why path-scoped instructions are often the highest-value review primitive: they make expectations specific enough to apply to the changed files in front of the model.

Starting June 1, 2026, GitHub Copilot code review on private repositories consumes GitHub Actions minutes in addition to Copilot usage billing. Public repositories continue to use free Actions minutes. Teams that enable automatic reviews should plan runner capacity, budgets, and review volume before treating every PR review as cost-neutral.

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
| Custom Agents | ❌ No direct effect | Reviewer agents are useful for local chat review, but dedicated PR review does not adopt a Custom Agent persona |
| Prompts | ❌ No | Prompts are user-invoked; reviews are non-interactive |
| Skills | ❌ No (today) | Skills are discovered during agent sessions, not PR reviews |
| MCP | ❌ No as a user-configured primitive | Review uses its own controlled service-side capabilities, not the user's local MCP tool menu |
| Hooks | ❌ No | Hooks govern local agent sessions, not cloud review |

### Code Review via Chat Is a Different Pipeline

The dedicated code review feature: the one triggered from the Reviewers menu on GitHub.com or the Source Control button in VS Code: runs its own pipeline. It operates on a diff, reads instruction files from the base branch, and produces review comments. Prompts, Skills, and MCP do not participate in that pipeline.

That does not mean chat cannot do review-style work. It can. But it runs through the agent loop, not the code review pipeline. The difference matters:

| | Dedicated Code Review | Review via Chat/Prompt |
|---|---|---|
| **Trigger** | Reviewers menu (GitHub.com) or Source Control button (VS Code) | User invokes a prompt or asks in chat |
| **What it sees** | PR diff, base-branch instructions, and service-side project context gathered for review | The full user-controlled agent context: files, tools, conversation, instructions |
| **Primitives used** | Always-on Instructions, File-based Instructions, Memory | All eight primitives |
| **Output** | Review comments on the diff | Chat response, inline edits, or tool calls |
| **Can call tools?** | Controlled service-side review capabilities; not the user's local tool menu | Yes: search, read, run commands, delegate to subagents |

### GitHub.com PR Chat Is Also Review-Capable

GitHub.com chat over pull requests is a third path. As of April 23, 2026, GitHub Copilot Chat on GitHub.com can use richer pull request context, including comments, file changes, commits, and reviews. It can also produce a structured review or concise pull request summary when asked.

Use that for interactive understanding and review assistance. Use dedicated code review when the desired output is review comments attached to the diff.

For local pre-commit review, a prompt file can be more thorough than the dedicated pipeline because it has access to the full codebase and toolset:

```markdown
---
name: review-my-changes
description: Review uncommitted changes against repo conventions before committing.
tools: ['changes', 'readFile', 'search']
---

Review all uncommitted changes in this repository. For each changed file:

1. Read the file and the relevant instruction files.
2. Check for correctness, security issues, and style violations.
3. Flag anything that would normally come up in PR review.
4. Be specific: cite the line and the rule.
```

This runs through the agent loop, so it can search the codebase for context, read instruction files, and use MCP tools if configured. The tradeoff is that it does not enforce base-branch rules or leave comments on a PR: it is a local check, not a policy gate.

### The Commit-Gate Pattern: Review, Test, Fix, Then Commit

The most powerful local review pattern combines a Skill, instruction files, and a prompt into a single pre-commit workflow. The developer says "commit my changes" or runs `/safe-commit`, and the agent reviews the code, runs the tests, reports every issue with a proposed fix, and asks whether to apply each fix before committing.

This requires three pieces working together:

**1. The instruction file owns the standards** (code review will also see these):

```markdown
---
applyTo: "src/**/*.ts"
---

# TypeScript Conventions

- Every exported function must have explicit return types.
- Every `async` function must wrap its body in try/catch and log via `logger.error` with a stable code prefix.
- Never swallow errors silently.
- Use Zod schemas for all external input validation.
- No `any` types except in test mocks.
- Imports must use the `@/` path alias, not relative paths deeper than one level.
```

**2. The Skill owns the procedure** and references the instruction file:

```markdown
---
name: safe-commit
description: >
  Review all uncommitted changes, run tests, report issues with fixes,
  and commit only after the developer approves. Use when the user asks
  to commit, ship, finalize, or push their changes safely.
metadata:
  author: platform-team
  version: "1.0"
---

# Safe Commit

A pre-commit gate that catches issues before they reach a PR.

## Before You Start

Read `.github/copilot-instructions.md` and every `.instructions.md` file
that matches the changed files. Those are the standards this review
enforces.

## Steps

### 1. Identify what changed
Use the `changes` tool to list all uncommitted changes. Show the
developer a summary of modified, added, and deleted files.

### 2. Review against instruction files
For each changed file:
- Read the file.
- Load the matching instruction files (by `applyTo` glob).
- Check every rule. Be specific: cite the line number, the rule,
  and why it fails.

### 3. Run the tests
Run the project's test command (e.g., `npm test`, `pytest`, `dotnet test`).
If tests fail, include the failure output in the report.

### 4. Report issues with proposed fixes
Present each issue as a numbered list:

For each issue, show:
- **File and line**: where the problem is.
- **Rule**: which instruction or test it violates.
- **Problem**: what is wrong.
- **Proposed fix**: the exact code change that would resolve it.

### 5. Ask the developer
After presenting all issues, ask:
- "Fix all?": apply every proposed fix.
- "Fix some?": let the developer pick which fixes to apply.
- "Skip and commit anyway?": commit without fixes.
- "Abort?": stop without committing.

Wait for the developer's answer before proceeding.

### 6. Apply approved fixes
Apply only the fixes the developer approved. Do not make additional
changes beyond what was presented and approved.

### 7. Run tests again
If any fixes were applied, re-run the test suite to confirm nothing
broke.

### 8. Commit
Stage all changes and commit with a descriptive message summarizing
what changed and which issues were fixed. Show the commit hash.
```

**3. An optional prompt file for a one-click entry point:**

```markdown
---
name: safe-commit
description: Review, test, fix, and commit in one step.
tools: ['changes', 'readFile', 'search', 'editFile', 'runTerminal']
---

Run the safe-commit workflow on all uncommitted changes.
```

The prompt gives developers a `/safe-commit` slash command. The Skill provides the same capability when someone just types "commit my changes" in chat. Both paths run the same procedure and reference the same instruction files.

### Why This Works Across Both Pipelines

The coding standards live in instruction files, not in the Skill. That means:

- When the safe-commit Skill reviews code locally, it reads those instruction files and checks against them.
- When a PR reaches GitHub.com, the dedicated code review pipeline reads the same instruction files and comments on the same standards.
- If the developer skips the Skill and commits directly, code review still catches the violations.

The Skill adds a pre-commit safety net. The instruction files are the actual contract. Neither depends on the other to be complete.

Use the dedicated code review pipeline for PR-level detection anchored to the base branch. Pair it with branch protection, required human review, or CI when a rule must block merge. Use the safe-commit Skill or prompt for a richer local gate before pushing.

## Why Instruction Files, not Skills: Own Coding Standards

This is the most important design decision teams need to understand about code review and customization.

GitHub Copilot has two separate pipelines that evaluate code quality: the **agent loop** (chat, agent mode, CLI) and the **code review pipeline** (PR review on GitHub.com, local review in VS Code). Both pipelines read instruction files. Only the agent loop loads Skills.

That asymmetry creates a trap. A team writes a scaffolding Skill that says "every route must validate input with Zod" and "return RFC 7807 problem details on errors." The Skill works perfectly in agent mode: the agent reads it, follows it, generates correct code. Then a developer hand-writes a route without the Skill, opens a PR, and Copilot code review says nothing about the missing validation or the wrong error format. The standard was invisible to the review pipeline because it lived in the wrong primitive.

### The Layered Model

The fix is not to duplicate standards across Skills and instruction files. It is to put them in the right layer from the start:

| Layer | What it owns | Which pipelines see it |
|-------|-------------|----------------------|
| **Instruction files** (`.instructions.md` with `applyTo` globs) | Coding standards, conventions, architectural rules, security requirements | Agent loop ✅ AND code review ✅ |
| **Skills** (`.github/skills/*/SKILL.md`) | Workflows, procedures, multi-step tasks | Agent loop ✅ only |
| **Always-on Instructions** (`.github/copilot-instructions.md`) | Repository-wide defaults, stack choices, global anti-patterns | Agent loop ✅ AND code review ✅ |

The instruction file is the **contract between writing and reviewing**. If a rule matters enough to catch in a PR, it must live in an instruction file. If it only lives in a Skill, it will enforce during code generation but vanish during review.

### How Skills and Instructions Work Together

Skills are not excluded from the quality story: they just play a different role. A Skill defines *how* to carry out a task. An instruction file defines *what standards apply* when touching specific files. The best composition is a Skill that references the instruction file instead of restating the rules:

```markdown
# Scaffold API Route (Skill)

## Before You Start
Read `.github/instructions/api-routes.instructions.md` before generating any code.
Follow those conventions exactly.

## Steps
1. Ask which resource the route serves.
2. Create the handler in `src/routes/{resource}.ts`.
3. Create the Zod schema in `src/schemas/{resource}.ts`.
...
```

```markdown
# API Route Conventions (Instruction file)
---
applyTo: "src/routes/**/*.ts"
---
- Every route must validate input with a Zod schema.
- Return RFC 7807 problem details on errors.
- Include an OpenAPI JSDoc comment above each handler.
```

When a developer uses the Skill to scaffold a route, the agent reads the instruction file and follows the rules. When a different developer hand-writes a route and opens a PR, code review reads the same instruction file and flags any violations. One source of truth, two enforcement points.

### The Practical Checklist

Before shipping a new standard, ask one question: **will code review see this?**

- If the standard is in `.github/copilot-instructions.md` → ✅ code review sees it (first 4,000 chars).
- If the standard is in `.github/instructions/*.instructions.md` with an `applyTo` glob → ✅ code review sees it when the PR touches matching files.
- If the standard is only inside a Skill → ❌ code review will never see it.
- If the standard is only inside a Prompt → ❌ code review will never see it.
- If the standard is only inside a Custom Agent → ❌ dedicated code review will not apply it.

That checklist is worth posting in the team's contribution guide. The most common failure mode is not a missing rule: it is a rule in the wrong layer.

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

## Setting Up GitHub Copilot Code Review

### On GitHub.com (Pull Request Review)

1. Open a pull request on GitHub.com (or navigate to an existing one).
2. Open the **Reviewers** menu in the sidebar.
3. Select **Copilot** from the list.
4. Wait for the review: usually under 30 seconds.
5. Scroll down and read Copilot's comments inline on the diff.

Copilot leaves a **Comment** review only. It does not Approve or Request Changes, so it never blocks a merge. Comments behave like any human review comment: react, reply, resolve, or dismiss.

To request a re-review after pushing new commits, click the re-request review button next to Copilot's name in the Reviewers menu.

#### Automatic Reviews

By default, Copilot reviews are manual: one request per PR. To have Copilot review every PR automatically, configure automatic reviews in the repository or organization settings. See [Configuring automatic code review by GitHub Copilot](https://docs.github.com/en/copilot/how-tos/agents/copilot-code-review/automatic-code-review).

### In VS Code (Local Review from Source Control)

The fastest way to trigger a code review in VS Code is directly from the Source Control view: the same place developers already stage and commit files. No chat window, no slash command, no context switch.

**Review all uncommitted changes:**

1. Click the **Source Control** icon in the Activity Bar (or press `Ctrl+Shift+G`).
2. In the Source Control view, hover over the **CHANGES** header.
3. Click the **Copilot Code Review: Uncommitted Changes** button (the sparkle icon that appears on hover).
4. Wait for the review: usually under 30 seconds.
5. Review comments appear inline in the affected files and in the **Problems** tab.

This reviews every unstaged and staged change in the workspace against the same instruction layer that PR review uses: `.github/copilot-instructions.md` and any matching `.instructions.md` files. It is the same standards, applied before the code leaves the developer's machine.

**Review a selection of code:**

1. Select the code in the editor.
2. Right-click → **Generate Code** → **Review**.
3. Review comments appear inline and in the Comments panel.

This is useful for reviewing a specific function or block without reviewing the entire set of changes.

**Why Source Control review matters:** Most developers already live in the Source Control view when they are about to commit. Putting the review trigger there: instead of in chat: means the review happens at the moment it is most useful: right before the commit, in the same UI flow the developer was already using. No mode switch, no extra step to remember.

Both modes use the same instruction layer as PR review on GitHub.com. The difference is timing: local review catches issues before the commit, not after the PR is opened. That means fewer round-trips through CI and fewer review comments that could have been caught locally.

### Across Other Surfaces

Code review is also available in JetBrains IDEs, Visual Studio, and the GitHub CLI. The setup varies by surface; see the [official docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review) and select the appropriate tool tab.

### Billing and Runner Planning

For private repositories, each dedicated GitHub Copilot code review starts consuming GitHub Actions minutes on June 1, 2026. Until then, reviews continue to draw only from Copilot premium request unit allowance. Review usage from non-licensed users through direct organization billing is included in the change.

Before enabling automatic review broadly:

- confirm GitHub-hosted runner access or the organization's self-hosted runner strategy,
- review Actions budgets and spending limits,
- monitor Copilot usage metrics and Actions usage together,
- and decide which repositories should receive automatic review versus manual review requests.

## Where to Read Next

- Read [Where GitHub Copilot Runs](where-github-copilot-runs.md) next for the broader surface picture.
- Revisit [File-based Instructions](primitive-2-file-based-instructions.md) if you want the highest-leverage authored primitive for review-specific improvement.
