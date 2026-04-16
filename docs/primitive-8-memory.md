# Copilot Memory

[← Hooks](primitive-7-hooks.md) | [Part II Overview](part-2-primitives.md)

*Updated: April 16, 2026 · Validated against VS Code 1.116 and GitHub Copilot docs as of April 16, 2026.*

---

## Overview

The customization primitives covered in this guide — instructions, prompts, skills, agents, MCP, and hooks — are all *explicit*. Someone writes them, commits them, and maintains them. They capture what a team *wants* Copilot to know.

[Copilot Memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory) works differently. It lets Copilot build its own understanding of a repository by automatically discovering and storing facts as it works — coding conventions, architectural patterns, cross-file dependencies, and other details that emerge from real activity. No one writes these down. Copilot observes, remembers, and applies them later.

**Status:** Public preview (on by default for Pro/Pro+ users as of [March 4, 2026](https://github.blog/changelog/2026-03-04-copilot-memory-now-on-by-default-for-pro-and-pro-users-in-public-preview))
**Best For:** Supplementing explicit customization with learned context that's hard to document manually
**Location:** Managed by GitHub — no repo file to configure
**Ownership:** Memory has no repo file to own, but **Security / Compliance** owns the enablement policy (enterprise or org setting), and **repository admins** own the periodic review-and-delete cadence for stored memories.

**Official docs:** [Copilot Memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory) · [Managing memories](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/copilot-memory)

### Quick Reference: View, Edit, or Disable

| Action | Where |
|--------|-------|
| **View or delete memories for a repo** | Repository → **Settings** → **Copilot** → **Memory** (requires repo owner). See [Viewing and Deleting Memories](#viewing-and-deleting-memories). |
| **Turn Memory off for yourself** | [github.com/settings/copilot](https://github.com/settings/copilot) → Features → Copilot Memory → **Disabled**. See [Enabling or Disabling Memory](#enabling-or-disabling-memory). |
| **Turn Memory off for an organization** | Org Settings → Copilot → Policies → Copilot Memory (org owners only). |
| **Turn Memory off enterprise-wide** | Enterprise → AI controls → Copilot → **Disabled everywhere**. |

Memories also auto-expire after 28 days and are re-validated against current code before every use — stale or incorrect memories are discarded automatically. Manual deletion is only needed for memories you want gone immediately.

Think of the relationship this way:

- **Primitives** shape what Copilot is *told* — explicit rules, procedures, and tools
- **Memory** captures what Copilot *learns* — patterns discovered through use

A well-configured repository uses both. Explicit customization prevents mistakes from day one. Memory fills in the nuances that accumulate over time.

---

## How Memory Works

When Copilot works in a repository — implementing features, reviewing pull requests, answering questions — it may notice patterns worth remembering. Each memory is a tightly scoped piece of information about the repository: a naming convention, a critical dependency, a non-obvious architectural rule.

### Lifecycle

```text
Copilot works in repo
     ↓
Discovers useful fact
     ↓
Stores memory with citations (references to specific code locations)
     ↓
Next session: validates citations against current codebase
     ↓
  ┌── Valid → Memory applied to current task
  └── Invalid → Memory discarded (code changed, no longer relevant)
     ↓
After 28 days → Memory auto-expires
```

### Key Properties

| Property | Detail |
|----------|--------|
| **Scope** | Repository-level — memories are tied to a single repo, not to a user or organization |
| **Creation** | Automatic — Copilot creates memories during normal operations, not from manual input |
| **Validation** | Citation-based — each memory references specific code locations; Copilot checks these against the current codebase before using a memory |
| **Expiration** | 28 days — prevents stale context from affecting decisions |
| **Renewal** | If a memory is validated and used, a new memory with the same details may be stored, extending its effective lifetime |
| **Permissions** | Only created from activity by users with write access to the repository |

Memories created from unmerged pull requests won't affect behavior — the validation step ensures the supporting code must exist in the current codebase.

---

## Where Memory Is Used

Memory currently works across three Copilot surfaces:

| Surface | How Memory Helps |
|---------|-----------------|
| **[Copilot cloud agent](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/copilot-memory)** | Applies learned conventions when implementing features and opening PRs |
| **[Copilot code review](https://docs.github.com/en/copilot/concepts/agents/copilot-memory#where-is-copilot-memory-used)** | Uses learned patterns to give more targeted review feedback |
| **[Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli)** | Brings repository awareness to terminal workflows |

Memories are shared across surfaces. If the coding agent discovers how your repository handles database connections, code review can apply that knowledge to spot inconsistent patterns in a pull request. If code review learns that two config files must stay synchronized, the coding agent will know to update both.

Memory is not yet available in VS Code Chat, Completions, or Inline Chat. GitHub has indicated it will extend to additional surfaces and scopes in future releases.

---

## Memory vs. Explicit Customization

Memory and explicit customization solve different problems. Neither replaces the other.

| | Explicit Customization | Copilot Memory |
|-|----------------------|----------------|
| **Source** | Written by developers, committed to repo | Automatically discovered by Copilot |
| **When it helps** | From the first interaction | After enough activity to learn from |
| **What it captures** | Deliberate rules and decisions | Emergent patterns and nuances |
| **Maintenance** | Manual — update instructions as codebase evolves | Automatic — expires stale memories, learns new ones |
| **Scope** | Varies by primitive (session, file, task) | Repository-wide |
| **Reliability** | Deterministic — same rules every time | Probabilistic — depends on what Copilot has observed |
| **Best for** | Must-follow rules, security requirements, architectural decisions | Coding style nuances, cross-file relationships, non-obvious conventions |

### When to Write Instructions vs. Let Memory Learn

**Write explicit customization when:**
- The rule must be followed from day one (no ramp-up period acceptable)
- Getting it wrong has consequences (security, data integrity, compliance)
- The pattern is a deliberate team decision, not an emergent convention
- Consistency across all contributors matters more than flexibility

**Let Memory handle it when:**
- The pattern is hard to articulate but easy to observe ("we tend to organize tests this way")
- The knowledge is cross-file and would be tedious to document exhaustively
- The convention is stable and well-established in the existing code
- You want Copilot to adapt to how the codebase actually works, not how the docs describe it

**Use both when:**
- Instructions set the rule ("use React Query, not Redux"), Memory learns the specific patterns ("in this repo, React Query hooks follow this naming convention and live in `src/hooks/queries/`")
- Skills encode the procedure ("deploy using these steps"), Memory learns the environment-specific details ("this repo deploys to three staging environments before production")

---

## Enabling and Managing Memory

Memory is granted at the **user** level, not the repository level. Once a user has Memory enabled, Copilot may create and use memories in any repository that user works in with Copilot cloud agent, Copilot code review, or Copilot CLI. The repository is the *scope* of a memory; the user is the *subject* of the enablement policy.

### Availability by Plan

| Plan | Default State | Who Controls | Where |
|------|--------------|--------------|-------|
| **Copilot Pro / Pro+** | Enabled by default | Individual user | Personal [Copilot settings](https://github.com/settings/copilot) |
| **Copilot Business** | **Disabled** by default | Organization owner | Organization Settings → Copilot → Policies |
| **Copilot Enterprise** | **Disabled** by default | Enterprise owner (may delegate) | Enterprise → AI controls → Copilot |

**Precedence rule:** If a user receives Copilot from multiple organizations, the **most restrictive** setting wins — Memory is only active when *every* assigning organization has it enabled. Enterprise-level `Disabled everywhere` overrides any org-level choice.

### Enabling or Disabling Memory

**Enterprise owners — set the enterprise-wide policy:**

1. Navigate to **Enterprise** → **AI controls** → **Copilot**
2. Under **Features**, scroll to **Copilot Memory**
3. Select a policy from the dropdown:
   - **Let organizations decide** — each org owner chooses independently
   - **Enabled everywhere** — on for every licensed member across every org in the enterprise
   - **Disabled everywhere** — off everywhere, and org owners cannot re-enable it

**Organization owners (Business, or Enterprise with `Let organizations decide`):**

1. Go to **Organization Settings** → **Copilot** → **Policies**
2. Under **Features**, scroll to **Copilot Memory**
3. Select **Enabled** from the dropdown — applies to all licensed members of the org

**Individual users (Pro / Pro+, or users whose org has enabled Memory):**

1. Click your profile picture → **Copilot settings**
2. Under **Features**, scroll to **Copilot Memory**
3. Select **Enabled** or **Disabled**

Users whose Copilot license comes from an org can only *opt out* — they cannot opt in if the org or enterprise has Memory disabled.

### Viewing and Deleting Memories

Only **repository owners** can view and manually delete the memories stored for a repository:

1. Go to the repository → **Settings** → **Copilot** → **Memory** (in the **Code & automation** section of the sidebar)
2. A chronological list of stored memories is displayed, newest first
3. Click the trashcan icon next to a memory to delete it, or use the checkboxes to select multiple memories and click **Delete**

Manual deletion is only needed to remove memories that are incorrect, outdated, or misleading — memories auto-expire on a 28-day cycle.

For full details, see [Managing and curating Copilot Memory](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/copilot-memory).

### Retention, Validation, and Renewal

Three mechanisms keep stored memories from going stale:

| Mechanism | How It Works | Effect |
|-----------|--------------|--------|
| **28-day expiration** | Every memory has a hard time-to-live. Unused memories are automatically deleted after 28 days. | Prevents old assumptions from affecting decisions indefinitely |
| **Citation validation** | Each memory is stored with citations — references to specific code locations that justify it. Before a memory is used, Copilot re-checks those citations against the current codebase and branch. | A memory whose supporting code has been deleted or changed is discarded rather than applied — including memories derived from PRs that were closed without merging |
| **Renewal on use** | When a memory is validated and used, a new memory with the same details may be stored, resetting the clock. | Memories that continue to match the codebase persist; memories no one hits quietly expire |

Together, these mean memory follows the living code: accurate facts stick around, obsolete ones fall off without needing human cleanup.

---

## Best Practices

1. **Don't skip explicit customization because Memory exists.** Memory takes time to build up. A new repository has zero memories. Instructions and skills work from the first interaction.

2. **Use instructions for guardrails, Memory for nuance.** Put security requirements, architectural rules, and technology choices in `copilot-instructions.md`. Let Memory learn the subtleties — naming patterns, file organization preferences, testing conventions that are "obvious" to the team but not documented anywhere.

3. **Review stored memories periodically.** Check what Copilot has learned about your repository. Delete memories that are misleading or based on patterns you're moving away from.

4. **Treat Memory as a complement to good onboarding.** Memory helps Copilot work the way your team works. It doesn't replace a well-structured `copilot-instructions.md` any more than institutional knowledge replaces a README.

5. **Consider the 28-day window.** Memories expire if not refreshed. For critical conventions, don't rely on Memory alone — write them down in instructions or skills where they persist indefinitely.

---

## Limitations

Copilot Memory is in public preview. Current limitations:

| Limitation | Detail |
|-----------|--------|
| **Preview status** | Behavior may change. Verify current capabilities against [official documentation](https://docs.github.com/en/copilot/concepts/agents/copilot-memory) |
| **Repository scope only** | Memories don't carry across repositories. No user-level or organization-level memory yet |
| **28-day expiration** | Memories auto-delete after 28 days. Frequently-used ones get refreshed, but rarely-relevant facts may not persist |
| **Limited surfaces** | Currently works with coding agent, code review, and Copilot CLI only. Not yet in VS Code Chat, Completions, or Inline Chat |
| **Write access required** | Memories are only created from activity by users with write permission in the repository |
| **Owner-only review** | Only repository owners can list or delete stored memories — team members and contributors cannot audit what Copilot has learned |
| **Org enablement required** | Users on Business / Enterprise plans cannot opt themselves in — Memory must first be enabled at the enterprise or organization level |
| **No manual creation** | You can view and delete memories, but you can't manually add them. Use instructions, skills, or agents for knowledge you want to inject directly |

---

## Further Reading

- [About agentic memory for GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/copilot-memory) — Concepts and architecture
- [Managing and curating Copilot Memory](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/copilot-memory) — Enablement, viewing, and deleting memories
- [Copilot Memory now on by default for Pro and Pro+ users](https://github.blog/changelog/2026-03-04-copilot-memory-now-on-by-default-for-pro-and-pro-users-in-public-preview) — Changelog announcement

---

[← Hooks](primitive-7-hooks.md) | [Next: Agentic Workflows →](agentic-workflows.md)
