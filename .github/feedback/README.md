# Feedback Folder

This folder is the communication channel between the reviewer agents (The Newb, The Intermediate, The Cook) and the Doc Maintainer agent.

## How It Works

1. A reviewer agent reads documentation in `docs/` or `ReadMe.md`.
2. The reviewer writes a feedback file to this folder using the naming convention below.
3. The Doc Maintainer reads pending feedback files from this folder and triages them.
4. Once the Doc Maintainer has addressed the feedback, the file is deleted or moved.

## File Naming Convention

```
{agent}-{target}-{date}.md
```

| Component | Description | Example |
|-----------|-------------|---------|
| `agent` | Reviewer slug: `newb`, `intermediate`, `cook` | `newb` |
| `target` | Doc file reviewed (without extension) | `part-2-3-prompts` |
| `date` | ISO date of review | `2026-02-20` |

**Examples:**
- `newb-part-2-1-always-on-instructions-2026-02-20.md`
- `intermediate-readme-2026-02-20.md`
- `cook-part-2-6-mcp-2026-02-20.md`

## Feedback File Format

Each feedback file must include this frontmatter:

```yaml
---
reviewer: 'The Newb' | 'The Intermediate' | 'The Cook'
target: 'docs/part-2-3-prompts.md'
date: 2026-02-20
status: pending | in-progress | resolved
---
```

**Status values:**
- `pending` — New feedback, not yet reviewed by Doc Maintainer
- `in-progress` — Doc Maintainer is actively addressing this feedback
- `resolved` — All items addressed; safe to delete

The body contains the reviewer's feedback using their persona-specific markers.

## For Reviewers

After reading a doc file, write your feedback to this folder. One file per doc reviewed. Use your persona's feedback format (markers, verdict, tone). Always set `status: pending`.

## For Doc Maintainer

Check this folder for `status: pending` files. Triage by severity, update status to `in-progress` while working, and mark `resolved` (or delete the file) when done.
