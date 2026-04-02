# Copilot Memory

[← Hooks](part-2-7-hooks.md) | [Part II Overview](part-2-primitives.md)

---

## Overview

The customization primitives covered in this guide — instructions, prompts, skills, agents, MCP, and hooks — are all *explicit*. Someone writes them, commits them, and maintains them. They capture what a team *wants* Copilot to know.

[Copilot Memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory) works differently. It lets Copilot build its own understanding of a repository by automatically discovering and storing facts as it works — coding conventions, architectural patterns, cross-file dependencies, and other details that emerge from real activity. No one writes these down. Copilot observes, remembers, and applies them later.

**Status:** Public preview (on by default for Pro/Pro+ users as of [March 4, 2026](https://github.blog/changelog/2026-03-04-copilot-memory-now-on-by-default-for-pro-and-pro-users-in-public-preview))
**Best For:** Supplementing explicit customization with learned context that's hard to document manually
**Location:** Managed by GitHub — no repo file to configure

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

### Availability by Plan

| Plan | Default State | Who Controls |
|------|--------------|--------------|
| **Copilot Pro / Pro+** | Enabled by default | Individual user in [Copilot settings](https://github.com/settings/copilot) |
| **Copilot Business** | Disabled by default | Organization admin via Copilot policies |
| **Copilot Enterprise** | Disabled by default | Enterprise owner via AI controls, or delegated to org admins |

If a user receives Copilot from multiple organizations, the most restrictive setting wins — Memory is only active when *all* assigning organizations have it enabled.

### Enabling or Disabling Memory

**Individual users (Pro / Pro+):**

1. Click your profile picture → **Copilot settings**
2. Under **Features**, scroll to **Copilot Memory**
3. Select **Enabled** or **Disabled** from the dropdown

**Organization admins (Business / Enterprise):**

1. Go to **Organization Settings** → **Copilot** → **Policies**
2. Under **Features**, scroll to **Copilot Memory**
3. Select **Enabled** from the dropdown to turn it on for all licensed members

**Enterprise owners:**

1. Navigate to **Enterprise** → **AI controls** → **Copilot**
2. Under **Features**, scroll to **Copilot Memory**
3. Select a policy:
   - **Let organizations decide** — delegates to org admins
   - **Enabled everywhere** — turns on Memory for all licensed members across all orgs
   - **Disabled everywhere** — turns off Memory and prevents orgs from enabling it

### Viewing and Deleting Memories

Repository owners can review and delete stored memories:

1. Go to the repository → **Settings** → **Copilot** → **Memory**
2. A chronological list of stored memories is displayed (newest first)
3. Click the trash icon next to any memory to delete it, or select multiple and click **Delete**

Memories auto-expire after 28 days, so manual deletion is only needed to remove memories that are incorrect or misleading before they expire naturally.

For full details, see [Managing and curating Copilot Memory](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/copilot-memory).

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
| **No manual creation** | You can view and delete memories, but you can't manually add them. Use instructions, skills, or agents for knowledge you want to inject directly |

---

## Further Reading

- [About agentic memory for GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/copilot-memory) — Concepts and architecture
- [Managing and curating Copilot Memory](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/copilot-memory) — Enablement, viewing, and deleting memories
- [Copilot Memory now on by default for Pro and Pro+ users](https://github.blog/changelog/2026-03-04-copilot-memory-now-on-by-default-for-pro-and-pro-users-in-public-preview) — Changelog announcement

---

[← Hooks](part-2-7-hooks.md) | [Next: Agentic Workflows →](part-2-9-agentic-workflows.md)
