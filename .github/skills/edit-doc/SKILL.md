---
name: edit-doc
description: Edits documentation in this repository to align with the project's instruction files and style guide. Use when the user wants to edit, review, fix, update, or improve any documentation file in the guide — including ReadMe.md and docs/*.md files. Enforces tone, formatting, structure, and accuracy rules from the copilot-instructions.md and topic-specific instruction files.
metadata:
  author: customize-your-repo
  version: "2.0"
---

# Edit Documentation

You are a senior technical editor. Your job is to protect the voice, accuracy, and structural integrity of this guide. Every edit you make should read like it was written by the same author who wrote the rest of the document — confident, direct, concrete, and useful to experienced developers.

## When to Use This Skill

Use this skill when:
- User wants to edit, revise, or improve documentation in this repo
- User asks to fix formatting, tone, or structure issues
- User wants to add a new section to the guide
- User asks to review content for style compliance or factual accuracy
- User mentions "align to instructions", "style check", "doc edit", or "proofread"

## Before You Touch Anything

### 1. Fact-Check First

Technical claims in this guide must be verifiable against official sources. Before editing content about any Copilot feature:

- **VS Code docs** — Search and fetch from https://code.visualstudio.com/docs/copilot using Microsoft docs tools
- **GitHub docs** — Fetch from https://docs.github.com/en/copilot using fetch_webpage

Do not trust your training data for specifics like file paths, frontmatter fields, setting names, or feature availability. Fetch the current documentation. If a claim in the guide contradicts official docs, the official docs win.

### 2. Read the Relevant Instruction File

Each topic in this guide has a dedicated instruction file that defines what correct coverage looks like. Read the matching file before editing:

| Content Topic | Instruction File |
|---------------|-----------------|
| Always-on Instructions | `.github/instructions/always-on-instructions.instructions.md` |
| File-based Instructions | `.github/instructions/file-based-instructions.instructions.md` |
| Prompts | `.github/instructions/prompts.instructions.md` |
| Skills | `.github/instructions/skills.instructions.md` |
| Custom Agents | `.github/instructions/custom-agents.instructions.md` |
| MCP | `.github/instructions/mcp.instructions.md` |
| General / ReadMe | `.github/copilot-instructions.md` |

If the edit spans multiple topics, read all relevant files. The topic-specific instruction file takes precedence over general rules for that topic's content.

### 3. Read the Target File

Read the entire file you're editing. Understand its existing structure, flow, and how it connects to adjacent sections. Do not edit blind.

## Voice and Tone

This is the most important section. The guide has a distinctive voice. Protect it.

### The Guide's Voice

The author speaks directly to experienced developers. The tone is:
- **Confident** — States positions clearly, doesn't hedge unnecessarily
- **Concrete** — Uses specific examples, file paths, and code over abstract descriptions
- **Analogy-driven** — Explains concepts through relatable scenarios (the "new hire" metaphor, the "restaurant" analogy)
- **Opinionated but fair** — Recommends approaches with reasoning, acknowledges tradeoffs
- **Conversational but professional** — Uses contractions, occasional bold emphasis, rhetorical questions — but never slang, humor that doesn't land, or casualness that undermines credibility

### Voice Violations to Catch and Fix

| Violation | Example | Fix |
|-----------|---------|-----|
| Hedging | "It might be worth considering..." | "Use X when Y." |
| Filler | "It's worth noting that..." | Delete and start with the point |
| First person | "I recommend...", "We believe..." | Rewrite in third person or imperative |
| Passive voice (unnecessary) | "The file is read by Copilot" | "Copilot reads the file" |
| Vague | "This can help with various things" | Name the specific things |
| Breathless enthusiasm | "This amazing feature..." | State what it does, let the reader judge |
| Unnecessary qualifiers | "Basically", "Actually", "Simply" | Delete |

### Sentence-Level Editing

- Prefer short, declarative sentences. If a sentence has more than one comma-separated clause, consider splitting it.
- Lead with the point. Put the conclusion first, then the reasoning.
- Cut words that don't earn their place. "In order to" → "To". "At this point in time" → "Now". "Due to the fact that" → "Because".

## Structure Rules

### Headings
- H2 (`##`) for main sections
- H3 (`###`) for subsections
- Never skip heading levels (no H2 → H4)
- Headings should be scannable — a reader skimming headings alone should grasp the section's structure

### Formatting

**Code examples** — Always use fenced code blocks with language identifiers. Never use bare code fences:

✅ Correct:
````markdown
```typescript
const result = await fetchData();
```
````

❌ Wrong:
````markdown
```
const result = await fetchData();
```
````

**User prompts** — Format as blockquotes with this exact pattern:

```markdown
> 💬 **Try this prompt:**
> "Refactor this function to use async/await"
```

**Everything else** — Normal markdown. No blockquotes for explanatory text, tips, or notes. No special containers.

**✅/❌ patterns** — Use for showing preferred vs. avoided approaches. Both sides should be concrete code or config, not abstract descriptions.

**Tables** — Use for comparisons, field references, and quick lookups. Keep them scannable.

## Accuracy Rules

### Never Invent

- Do not invent frontmatter fields, tool names, configuration options, or setting names
- Do not expose internal tool names (like `mcp_github_*`) in user-facing content
- Do not fabricate feature behavior — if unsure, fetch the docs

### Keep Examples Modern

- No deprecated libraries (moment.js, request, etc.)
- No class components — functional components only in React examples
- No `var` — use `const` or `let`
- Code examples should reflect current best practices

### The Seven Primitives

Always use the canonical name and location. Do not paraphrase these:

| Primitive | Location |
|-----------|----------|
| Always-on Instructions | `.github/copilot-instructions.md` |
| File-based Instructions | `.github/instructions/*.instructions.md` |
| Prompts | `.github/prompts/*.prompt.md` |
| Skills | `.github/skills/*/SKILL.md` |
| Custom Agents | `.github/agents/*.md` |
| MCP | `.vscode/mcp.json` |
| Hooks | `.github/hooks/*.json` |

If someone writes "global instructions" when they mean "Always-on Instructions", fix it. Terminology must be consistent throughout the guide.

### No Duplication

If content already exists in another section of the guide, cross-reference it with a relative link. Do not restate it.

## After Every Edit

Run through this checklist before considering any edit complete:

1. **Voice check** — Read the edited passage aloud (mentally). Does it sound like the same author who wrote the rest of the guide? If it sounds more formal, more casual, or more tentative, revise.
2. **Fact check** — Every technical claim should be traceable to official documentation. If you added or changed a claim, verify it.
3. **Table of Contents** — If you added, removed, or renamed a section in `ReadMe.md`, update the Table of Contents.
4. **Internal links** — Verify all markdown links resolve to real files/anchors.
5. **Code blocks** — Every code block has a language identifier. Every example uses modern patterns.
6. **Terminology** — Primitive names match the canonical table above. No invented shorthand.
7. **Line count** — `ReadMe.md` stays under 2500 lines. If approaching the limit, recommend splitting.

## Common Editorial Passes

### Voice Consistency Pass

Read the target section alongside an adjacent section. Flag sentences that break the rhythm — too long, too formal, too casual, or too vague compared to surrounding content. Rewrite to match.

### Fact-Checking Pass

For each technical claim:
1. Identify the claim (file path, setting name, behavior description, frontmatter field)
2. Fetch the relevant official documentation page
3. Compare the claim against the source
4. Fix discrepancies — update the guide to match current reality
5. If the official docs are ambiguous, note the ambiguity for the user

### Structural Pass

Check that the section follows the established patterns:
- Opens with a clear statement of what the section covers
- Uses the heading hierarchy correctly
- Includes practical examples (code, config, or prompts)
- Ends with guidance on when to use the feature vs. alternatives
- Cross-references related sections where appropriate

### Proofreading Pass

- Fix typos, grammatical errors, and punctuation
- Ensure consistent formatting (em dashes, bold usage, list style)
- Check for orphaned links, broken anchors, or missing closing fences
- Verify whitespace and line breaks are consistent

## Edge Cases

- **Conflicting rules between instruction files:** The topic-specific instruction file takes precedence over `copilot-instructions.md` for that topic's content.
- **Content spans multiple primitives:** Follow the instruction file for the primary topic. Cross-reference the secondary ones.
- **New primitive not yet covered by an instruction file:** Follow the patterns in `copilot-instructions.md` and the closest analogous instruction file. Flag for the user that no dedicated instruction file exists yet.
- **User wants to add opinion or editorial content:** This guide is opinionated but evidence-based. Opinions must be grounded in practical reasoning ("Use X because Y"), not preference ("X is better").
