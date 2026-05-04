---
name: 'improve-primitives'
agent: 'agent'
description: 'Use when reviewing primitives, improving instructions, analyzing recent commits, or learning from chat sessions'
tools: ['changes', 'search', 'readFile', 'editFiles', 'runInTerminal']
---

# Improve Primitives

Review this repository's GitHub Copilot customization system.

Use these inputs:

1. Recent commits, staged changes, and unstaged changes.
2. Recent chat, agent, or debug sessions if they are available in the workspace.
3. Current customization files:
   - `.github/copilot-instructions.md`
   - `.github/instructions/*.instructions.md`
   - `.github/prompts/*.prompt.md`
   - `.github/skills/*/SKILL.md`
   - `.github/agents/*.md`
   - `.vscode/mcp.json`
   - `.github/hooks/*.json`

For each finding, decide whether the right action is to:

- add a missing primitive,
- edit an existing primitive,
- delete stale or redundant guidance,
- move guidance to a better primitive,
- or leave the system unchanged.

Prefer small, reactive changes. Do not add rules unless recent work shows real friction.

Before editing, produce this triage table:

| Evidence | Problem | Recommended primitive | Action | Rationale |
|----------|---------|-----------------------|--------|-----------|

Ask for approval before changing files.

After approval:

1. Apply the approved edits.
2. Delete obsolete files if removal was approved.
3. Run the smallest validation checks available for changed files.
4. Summarize what changed, why each primitive changed, what evidence supported it, and what the team should watch in the next few sessions.