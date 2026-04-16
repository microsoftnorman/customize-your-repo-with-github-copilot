---
name: commit-and-push
description: Reviews all staged and unstaged changes using the edit-doc skill, reports findings, updates published dates, then commits and pushes. Use when the user wants to commit, push, ship, publish, or finalize changes to the guide.
metadata:
  author: customize-your-repo
  version: "1.0"
---

# Commit and Push

## When to Use This Skill

Use this skill when:
- User wants to commit and push changes
- User says "commit", "push", "ship it", "publish", or "finalize"
- User wants to wrap up an editing session and save to the repo

## Workflow

Execute these steps in order. Do not skip steps. Report status after each.

### Step 1: Identify What Changed

Run `git status` and `git diff` to identify all modified, added, and deleted files. Build a list of every changed `.md` file — these are the files that need editorial review.

If there are no changes, tell the user and stop.

### Step 2: Run the Editor on Every Changed Doc File

For each changed `.md` file in `ReadMe.md` or `docs/`:

1. **Activate the edit-doc skill** — Read `.github/skills/edit-doc/SKILL.md` for the full editorial instructions.
2. **Read the changed file** in its entirety.
3. **Read the matching instruction file** from the instruction file map in the edit-doc skill (if the content maps to a specific primitive).
4. **Perform all four editorial passes** from the edit-doc skill:
   - **Voice consistency pass** — Does the edited content sound like the same author as surrounding sections?
   - **Fact-checking pass** — Are technical claims verifiable against official docs? Fetch and verify any claims about file paths, frontmatter fields, settings, or feature behavior.
   - **Structural pass** — Correct heading hierarchy, examples, cross-references?
   - **Proofreading pass** — Typos, grammar, formatting, broken links, missing code fences?

5. **Report findings to the user.** For each file, list:
   - Issues found (with severity: error / warning / suggestion)
   - Specific lines or passages affected
   - Recommended fixes

**Do not auto-fix issues.** Present the findings and wait for the user to decide. The user may say "fix them", "ignore that one", or "commit anyway."

### Step 3: Apply Approved Fixes

If the user approves fixes, apply them. If the user says "commit anyway", skip to Step 4.

### Step 4: Update Updated Dates

Update the `Updated:` date line in every file that contains one. The date format is `Month Day, Year` (e.g., `February 10, 2026`). Set it to today's date.

Files known to contain updated dates:
- `ReadMe.md` (line 3)
- `docs/**/*.md` (most files have a metadata line near the top)

Search for additional `Updated:` lines in case new files have adopted the pattern. The updated date line follows this format:

```
*Updated: {Month} {Day}, {Year}. {rest of the sentence remains unchanged}*
```

or

```
*Updated: {Month} {Day}, {Year} · Validated against {rest of the sentence remains unchanged}*
```

Update only the date portion. Do not alter the rest of the sentence.

### Step 5: Stage, Commit, and Push

1. **Stage all changes:** `git add -A`
2. **Generate a commit message** — Descriptive, explaining what changed. Follow the project's commit style:
   - Good: "Update Skills section with agentskills.io spec details"
   - Bad: "Update readme"
   - If multiple sections changed, summarize: "Revise Prompts and MCP sections; fix formatting in Skills"
3. **Show the commit message to the user** and ask for confirmation before committing.
4. **Commit:** `git commit -m "{message}"`
5. **Push:** `git push`

Report the commit hash and confirm the push succeeded.

## Error Handling

- **Git conflicts:** Stop and report the conflict to the user. Do not attempt to resolve merge conflicts automatically.
- **Push rejected:** Run `git pull --rebase` and retry once. If it fails again, report to the user.
- **No remote configured:** Report and stop. Do not guess the remote.

## Example Interaction

**User:** "commit and push"

**Agent response:**

> Found 3 changed files: `ReadMe.md`, `docs/primitive-4-skills.md`, `docs/primitive-6-mcp.md`
>
> **ReadMe.md** — 1 warning
> - Line 42: "global instructions" should be "Always-on Instructions" (terminology consistency)
>
> **docs/primitive-4-skills.md** — No issues found ✓
>
> **docs/primitive-6-mcp.md** — 2 suggestions
> - Line 18: Code block missing language identifier
> - Line 35: Sentence uses passive voice unnecessarily
>
> Fix these before committing, or commit anyway?
