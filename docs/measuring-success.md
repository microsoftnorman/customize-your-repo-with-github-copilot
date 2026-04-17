# Measuring Success

[← Back to Guide](../ReadMe.md) | [← Why Customize](part-1b-why-customize.md)

*Updated: April 17, 2026 · Validated against VS Code 1.116 and GitHub Copilot docs as of April 16, 2026.*

---

Measuring GitHub Copilot well means tying customization work to business outcomes, not to activity dashboards. This chapter turns that into a practical scorecard: outward-facing business results, inward-facing delivery metrics, and a simple operating model for proving improvement.

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

---

[← Why Customize](part-1b-why-customize.md) | [Next: The Primitives →](part-2-primitives.md)
