# Measuring Success

[← Back to Guide](../ReadMe.md) | [← Why Customize](part-1b-why-customize.md)

*Updated: April 22, 2026 · Validated against VS Code 1.116 and GitHub Copilot docs as of April 16, 2026.*

---

Measuring GitHub Copilot well means tying customization work to business outcomes, not to activity dashboards. This chapter turns that into a practical scorecard: outward-facing business results, inward-facing delivery metrics, and an operating model for proving improvement as rollout expands from one team to the rest of the organization.

**See it in action:** [Let it Cook - This changes EVERYTHING](https://www.youtube.com/watch?v=uquSQY10AGM&t=1946s) — Pierce Boggan demos `agentrc eval`, generating repo-specific evals and comparing before-and-after customization outcomes to make instruction changes measurable.

**Official docs:** [GitHub Copilot usage metrics](https://docs.github.com/en/copilot/concepts/copilot-usage-metrics/copilot-metrics) · [Copilot usage metrics API](https://docs.github.com/en/rest/copilot/copilot-usage-metrics)

---

## Measuring Success

Measure GitHub Copilot the way leadership measures any operating investment: does it improve margin, bring revenue or adoption forward, increase useful output, reduce cost of delay, or lower delivery risk? Everything else is supporting evidence.

### Use [GQM](https://en.wikipedia.org/wiki/GQM), Not Dashboard Shopping

The simplest way to measure GitHub Copilot is [Goal-Question-Metric (GQM)](https://en.wikipedia.org/wiki/GQM): start with the goal, ask the question leadership cares about, then choose the metric that answers it.

This fits outcome-based planning. Start with the business outcome, not the dashboard and not tool activity such as chat volume or suggestion counts. The metric comes last.

Before deciding what to automate, map the [value stream](https://en.wikipedia.org/wiki/Value-stream_mapping). In practice that just means tracing how work moves from approved idea to production and marking where it waits, loops, or gets redone. That keeps teams from automating a bad process blindly and makes the obvious bottlenecks visible.

If a team cannot currently measure throughput in the system, it will struggle to prove improvement later. That is why baselines matter. Start by measuring the current flow with value stream mapping, value density versus waste density, and simple hypothesis testing around the biggest bottlenecks. If the claim is that GitHub Copilot will speed up review, reduce toil, or move features through the SDLC faster, define the before-state clearly enough that the after-state is defensible.

Some gains come from automating parts of the SDLC. Some come from improving the process itself by cutting rework, clarifying standards, or shortening review loops. Both count if they improve the business outcome.

For most teams, one table is enough:

| Goal | Executive Question | Outward-Facing Metric | Inward-Facing Metric | What Good Looks Like |
|------|--------------------|-----------------------|----------------------|----------------------|
| **Improve margin** | Are teams delivering more value for the same engineering spend? | Gross margin | Delivery cost per shipped feature, PR rework rate, toil time | Margin improves as cost per shipped feature falls and less time is lost to rewrite, review churn, repetitive manual work, and handoff delay |
| **Increase market speed** | Are important features reaching customers faster? | Time to market for customer-facing releases | Cycle time, queue time between stages, PR review time, deployment frequency | Approved work reaches production faster and release timing is more predictable |
| **Pull revenue or adoption forward** | Are releases landing soon enough to affect revenue, usage, or retention earlier? | Daily active users from recent releases, revenue or adoption from recent releases | Time from approved idea to customer availability, experiment cycle time, lead time for changes | Customer-facing releases land earlier, daily active use grows, and commercial impact appears sooner |
| **Increase useful feature output** | Are more valuable features shipping in the same planning period? | Customer behavior change after release | Features shipped per quarter, cycle time, deployment frequency | More customer-visible work ships and the shipped work changes customer behavior in the intended direction |
| **Reduce cost of delay** | Is high-value work spending less time waiting in backlog, review, or release queues? | Time to market for priority work | PR review time, cycle time, queue time between stages | Priority work spends less time idle and reaches the market while the opportunity still matters |
| **Reduce delivery risk** | Is faster delivery increasing production, compliance, or brand risk? | Defect escape rate | Change failure rate, mean time to recovery (MTTR) | Release speed improves without more incidents, and recovery stays fast when issues happen |

Outward-facing metrics show whether customers and the business feel the change. Inward-facing metrics show whether the delivery system is actually improving. Both matter, but the outward-facing metrics are the headline and the inward-facing metrics explain why they moved.

Toil is the plain-English term for routine, low-judgment work that has to get done but does not create customer value on its own. Reducing toil is often the first clear sign that a GitHub Copilot program is working because teams can see manual busywork disappear before larger financial gains show up in quarterly reporting.

Avoid treating prompt volume, chat activity, or raw suggestion counts as success metrics. Those numbers describe usage. They do not prove value.

### A Simple Operating Model

Run measurement in four steps:

1. Baseline the system hard. Take the last 4-8 weeks, map the value stream from approved work to production, measure throughput, and mark every queue, loop, handoff, and rework point. Separate value density from waste density. If the current state is not measurable, improvement claims will not survive scrutiny.
2. Attack the worst bottlenecks first. Start with repetitive work, approval drag, review churn, and obvious wait states. Use GitHub Copilot to remove manual toil and compress the path to production. Do not automate a broken workflow just because it is easy to script.
3. Run the rollout like an operating review. Review the scorecard monthly, not daily. Set a hypothesis before each change: what should improve, by how much, and by when. If a customization does not move the target metric, cut it or rewrite it.
4. Scale only what proves leverage. Expand the automations and process changes that improve the target outcome and shut down the ones that create activity without results. More tooling is not the goal. More throughput, faster learning, and better business performance are.

For a CxO audience, the message should fit in one sentence: GitHub Copilot is working if the company ships more valuable features faster, learns from the market sooner, and does so with less delay and no increase in production risk.

### What Different Audiences Should Watch

Different audiences should read the same scorecard at different depths. Executives should stay on the outward-facing metrics. Engineering managers should watch the inward-facing metrics to explain movement and decide where to tune the system.

Once that scorecard exists, rollout stops being faith-based. The team knows what it is trying to improve, what evidence counts, and what should happen before the next layer of customization goes live. That is where measurement turns into rollout discipline: start with the smallest set of primitives that can change daily work, prove they reduced friction, then expand.

## Rolling Out to Your Team

Once the scorecard is clear, rollout becomes simpler. Start small, prove that the system improved, then expand. GitHub Copilot customization works best in phases because each phase adds capability while preserving a short feedback loop:

| Phase | What to Deploy | What to Measure | Move to Next When |
|-------|---------------|-----------------|-------------------|
| **Day 1** | `copilot-instructions.md` + 2-3 skills + 1-2 custom agents | PR rework rate, developer feedback, repeated workflow reuse, specialized-agent usage | Rework rate decreases; the team starts using the same packaged workflows consistently; at least one targeted agent proves useful in recurring work |
| **Day 2-4** | File-based instructions, MCP servers, prompt files where lightweight slash commands still help | Cycle time, tool invocation frequency, targeted prompt reuse | More context is applied automatically; MCP tools integrate into daily workflow; prompt files remain only where they add clear convenience |
| **Day 5-8** | Hooks for enforcement, Memory enabled | Convention compliance, audit coverage | Hooks catch real violations; Memory reinforces patterns across repeated work |
| **Day 9-13** | Agentic Workflows, SDK integration, agent plugins | Autonomous task completion rate, CI-driven agent output quality | Workflows run reliably; trust in autonomous operation established |

Start with the highest-value baseline: `copilot-instructions.md`. Then add a small number of skills and one targeted custom agent before expanding into richer context, heavier enforcement, and broader automation. Each phase builds on the trust and evidence established in the previous one. For a small, already-aligned team, that sequence can fit inside two weeks. Larger rollouts take longer once security review, governance, and support planning enter the picture.

## Scaling Beyond One Team

The rollout above works for a single team on a single repo. Once that first team proves value, the next question is usually organizational: how does this scale without turning into chaos? At that point, the bottlenecks shift. Distribution, drift, ownership, and measurement matter more than authoring.

**Don't force every team onto the same rules.** The goal of scaling is to share what's genuinely reusable, not to impose uniformity. One team might require functional React with React Query; another might standardize on signals and a different state layer. One service might mandate strict typing and exhaustive error handling; another might optimize for rapid prototyping. Both can be right. Coupling every repo to a single source of truth turns customization into a political battleground and produces a baseline so watered-down it helps no one.

Aim for a thin shared baseline (security rules, commit conventions, org-wide anti-patterns) and let teams extend, override, or ignore the rest. GitHub Copilot reads the most specific instruction that applies. Use that to your advantage rather than fighting it.

**Patterns will emerge as you reshape for the AI-native SDLC.** Don't try to design the perfect org-wide customization system up front. As teams adopt Copilot, rework their workflows around autonomous agents, and push more work through the AI-assisted SDLC, shared conventions will surface on their own: a skill two teams independently wrote, a hook three teams copied, an instruction file that keeps showing up in PRs. *Those* are the patterns worth promoting to the shared baseline. Patterns imposed top-down before teams discover what actually works tend to calcify around yesterday's workflow and slow down tomorrow's.

Let the shared layer grow from real usage, not from a governance committee's whiteboard.

### Distribution Patterns

This leads to the practical question: how do those shared patterns reach many repos? Three mechanisms do most of the work. Most organizations combine all three, keeping the shared layer small and the team-specific layer fully under each team's control.

| Pattern | Best for | Tradeoffs |
|---------|----------|-----------|
| **Org-level `.github` repo** | Baseline rules every repo inherits (security policies, commit conventions, PR templates). GitHub auto-applies files from the special `.github` repo to every repo in the org that doesn't override them. | Only covers community health files natively; Copilot instructions must be copied in via template, sync action, or agent plugin. |
| **[Agent Plugins (Preview)](part-2-primitives.md#agent-plugins-preview)** | Bundling related primitives (skills + agents + hooks + instructions) as a versioned, installable package teams opt into. | Preview feature; plugin format still stabilizing. Best when you want opt-in adoption per repo. |
| **Template repositories** | New repos that should start with a full customization set (instructions, skills, MCP config, workflow files). | One-time imprint; drift starts on day one. Good for greenfield projects; weak for keeping existing repos in sync. |

A common blended model is straightforward: distribute a baseline `copilot-instructions.md` from a central repo with a sync action, deliver domain-specific skills and agents as opt-in agent plugins, and use template repos for new services.

### Ownership and CODEOWNERS

Customization files are source code. Review them like source code. Add `.github/copilot-instructions.md`, `.github/instructions/`, `.github/prompts/`, `.github/skills/`, `.github/agents/`, `.github/hooks/`, and `.vscode/mcp.json` to [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositories-settings-and-security/customizing-your-repository/about-code-owners) so the right team reviews each change:

```text
# .github/CODEOWNERS
.github/copilot-instructions.md    @acme/platform-dx
.github/instructions/security-*    @acme/appsec
.github/hooks/                     @acme/appsec @acme/platform-dx
.github/skills/                    @acme/platform-dx
.vscode/mcp.json                   @acme/platform-dx
```

Hooks and MCP configs deserve stricter ownership because they can execute code or expose external systems. Security review is non-optional.

### Drift Detection

Once customizations are distributed, they drift. Teams edit local copies, forget to pull upstream updates, and quietly diverge from the baseline. Some of that drift is healthy. A team adapting rules to fit their stack is exactly what you want. The goal isn't to eliminate drift, it's to distinguish *intentional divergence* from *silent rot* (outdated security rules, stale references, forgotten overrides). Detect drift with:

- **Scheduled sync actions.** A GitHub Action that, on a schedule, opens a PR in each downstream repo when the baseline repo's `copilot-instructions.md` or skill bundle has changed. Teams can merge, modify, or close the PR. Uses the [`peter-evans/create-pull-request`](https://github.com/peter-evans/create-pull-request) pattern or a custom script.
- **Drift reports.** A central workflow that clones every repo in the org, diffs its Copilot configuration against the canonical baseline, and posts a summary to Slack or an issue in the platform-DX repo. Treat it as visibility, not as a gate.
- **Agentic Workflows for review.** A scheduled agent workflow that inspects customization files across repos and flags *security-relevant* deviations (hook removal, MCP server changes, credential handling) rather than every stylistic difference. See [Agentic Workflows](agentic-workflows.md).

### Measuring Adoption at Scale

Per-team metrics (cycle time, rework rate) scale directly. Organization-level visibility comes from GitHub's APIs:

- **[Copilot Metrics API](https://docs.github.com/en/rest/copilot/copilot-metrics).** Aggregate usage (active users, chat turns, acceptance rates, agent mode sessions) at the org and enterprise level. Enables dashboards that correlate customization rollout with engagement.
- **[Copilot Usage API](https://docs.github.com/en/rest/copilot/copilot-usage).** Seat-level data for billing and license-management workflows.
- **[Audit log](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise#copilot-events).** Copilot events in the enterprise audit log (policy changes, MCP server approvals, seat assignments) for compliance and incident response.
- **Hook-driven logging.** Pipe [hooks](primitive-7-hooks.md) audit output to your SIEM for a per-session view of what Copilot did in high-risk repos.

### Phased Rollout Across the Organization

Resist the temptation to ship customizations org-wide on day one. Concentric waves build signal before scale:

| Wave | Scope | Exit criteria |
|------|-------|---------------|
| **Initial wave** | 1-2 volunteer teams on active repos | Early teams report friction down, PR rework down; baseline `copilot-instructions.md` and 2-3 skills stable |
| **Wave 1** | 5-10 teams, mixed tech stacks | Customizations survive contact with different stacks; central team knows which rules generalize vs. which need per-team overrides |
| **Wave 2** | Department or business unit | Distribution mechanism (sync action, agent plugin, template) is working; CODEOWNERS are in place; drift detection live |
| **Wave 3** | Entire organization | Copilot Metrics API dashboards running; audit logging integrated; support rotation staffed for customization questions |

At each wave, collect qualitative feedback (what rules fire unnecessarily? which skills did nobody discover?) and trim. The biggest org-wide rollout failure mode is accumulating every team's rules into a shared file that satisfies no one. Keep the baseline lean; let teams extend it locally.

### Further Reading

For richer patterns (shared skills libraries, MCP server registries, governance guardrails, and GitHub's own rollout playbook), see [Agent Plugins (Preview)](part-2-primitives.md#agent-plugins-preview) and [Agentic Workflows](agentic-workflows.md).

---

[← Why Customize](part-1b-why-customize.md) | [Next: The Primitives →](part-2-primitives.md)
