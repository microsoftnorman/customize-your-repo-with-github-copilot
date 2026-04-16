# Part I: Foundations — Why Customize

[← Back to Guide](../ReadMe.md) | [← Part I: What Copilot Is](part-1-foundations.md)

*Updated: April 16, 2026 · Validated against VS Code 1.116 and GitHub Copilot docs as of April 16, 2026.*

---

[Part I: Foundations](part-1-foundations.md) covered *what* GitHub Copilot is and *where* it runs. This half covers *why* [customization](https://code.visualstudio.com/docs/copilot/customization/overview) matters, how to roll it out across a team, and how to measure whether the investment is paying off.

---

## GitHub Copilot Without Customization

Imagine your first day at a new company. Someone hands you a laptop, points at a million lines of code, and says "add a feature to checkout." No architecture docs. No style guide. No idea where to go for help.

You start reading. In one file, 2+2 equals 5. In another file, 2+2 equals 0. Someone invented their own math system three years ago and never documented it. The function called `save()` actually deletes things. The `UserService` doesn't handle users—that's in `AccountManager`, except when it's in `ProfileHandler`, except on the front-end which follows its own logic.

None of this matches anything you learned. It's not wrong, exactly—it's *bespoke*. Someone built a custom framework on top of a custom ORM on top of a custom router, and the only person who understood it left for a startup in 2019.

Now someone asks you to make a change. You do your best. You give them something reasonable based on everything you've read. They get mad. *"Why would you use Redux? We use React Query! It's obvious!"* 

It wasn't obvious. It was in a file you hadn't opened yet, buried in a .deprecated folder.

**That's Copilot's reality—*every single time you send a prompt.***

It's not hallucinating. It's doing exactly what you'd do: making the best possible suggestions from incomplete context. The suggestions you reject? Those are reasonable choices for a codebase Copilot hasn't been taught to understand. The "wrong" answers? They're only wrong because Copilot doesn't know your team decided to do things differently.

This guide fixes that.

**The right mental model: Copilot is a new developer on your team.**

But here's the twist: this new developer is already an excellent coder. Frontier models like Claude Opus 4.7, GPT-5.4, Gemini 3 Pro know language idioms, common patterns, and industry best practices. They've seen more code than any human ever will. You don't need to teach them how to write a for-loop or when to use async/await.

Now imagine handing this brilliant new hire a 10,000-line document of coding rules. Every edge case. Every preference. Tabs vs. spaces. Whether to use `index` or `i` in loops. Exactly how many blank lines between functions. They'd be paralyzed—second-guessing every keystroke, drowning in rules instead of shipping code.

**The goal isn't to control every decision. It's to share what makes your codebase *different*:**
- "We use React Query, not Redux"
- "All API responses use our `ApiResponse<T>` wrapper"
- "Don't use moment.js—use date-fns"

Leave out the obvious stuff. Skip the rules your linter already enforces. Trust the model on general coding practices. Focus your instructions on decisions that are genuinely non-obvious—the things that would waste time in PR review if they got it wrong.

Think about what makes code easy for *any* new team member to work with:
- Easy to read, well-formed code
- Small, modular functions with clear responsibilities
- Good naming conventions (not everything called `i`, `temp`, or `data`)
- Comprehensive tests that document expected behavior
- Clear architectural patterns that follow established conventions

These same qualities make code easier for Copilot to understand and extend correctly. Code that's maintainable for humans is maintainable for AI. Code that confuses developers will confuse Copilot too. As you work with Copilot, you may want to refactor your code so Copilot can be more effective — a companion guide on that topic is coming soon.

### The Three Pillars of GitHub Copilot Success

Copilot's output quality depends on three factors:

| Pillar | Impact | What You Control |
|--------|--------|------------------|
| **Model Selection** | Raw reasoning power and behavior | Choose frontier models for complex work; accept that different models work differently |
| **Codebase Quality** | How well Copilot can understand your code | Write clean, well-documented, modular code |
| **Repository Configuration** | The context and rules Copilot operates with | **This guide** — the customization primitives and platform extensions |

Your **model selection** matters — see [Model Selection](part-1-foundations.md#model-selection) in the first half of Part I for the full breakdown. Different models also *behave* differently, and that's okay. Some are more verbose. Some ask more clarifying questions. Some jump straight to implementation. Learn your model's personality and work with it, not against it.

**See it in action:** For a live demo, watch Sandeep Somavarapu in [Bring Your Own Model (BYOM)](https://www.youtube.com/watch?v=W_WnyS_cXCk) and Julia Kasper in [How We Ship Models in VS Code](https://www.youtube.com/watch?v=eVxIwpGbHEk).

Your **codebase quality** matters — a well-structured codebase with clear naming, small functions, and comprehensive tests gives Copilot better context to work with. Messy, tangled code confuses AI just as much as it confuses human developers.

But even with the best model and cleanest codebase, **repository configuration** is what transforms Copilot from a generic platform into a team-aware development partner. This guide is the complete reference for setting up your repository for the best possible outcomes with GitHub Copilot.

### The Over-Instruction Trap

Every model arrives with **bias** — a set of default preferences baked in by training data. Claude Opus 4.7 prefers functional patterns and explicit error handling. GPT-5.4 reaches for object-oriented structures and comprehensive type annotations. Gemini 3 Pro gravitates toward concise, pragmatic solutions. These biases aren't bugs. They're the distilled wisdom of millions of codebases, and most of the time they produce solid, idiomatic code without any instructions at all.

This creates a spectrum with two failure modes:

**Under-instructing** means Copilot falls back entirely on its training bias. It produces reasonable code — but reasonable *for the internet*, not for your team. It picks Redux because that's what most React tutorials use. It reaches for Express because that's the most common Node.js framework. It writes class components because its training data includes a decade of React history. The code works. It just doesn't match the decisions your team already made.

**Over-instructing** is the more insidious failure. When developers discover customization, the temptation is to encode *everything* — every naming convention, every formatting preference, every edge case they've ever encountered in code review. The result is a 3,000-word instructions file that reads like a legal contract. The model doesn't ignore it, exactly — it tries to satisfy every constraint simultaneously, and the output becomes stiff, over-engineered, and weirdly cautious. Like a new hire who's been handed a 50-page employee handbook and is now afraid to make any decision without checking it first.

The sweet spot is narrower than most people think: **instruct only where your team's decisions diverge from what the model would do on its own.**

If the model already defaults to functional React components, the instruction "use functional components" is wasted tokens. If the model already handles async/await correctly, don't belabor it. Instead, spend those tokens on the genuinely non-obvious choices:

- "Use React Query for server state, not Redux" — *the model's bias would pick Redux*
- "All dates use `date-fns`, never `moment.js`" — *the model's training includes both*
- "API responses use our `ApiResponse<T>` wrapper" — *the model has no way to know this exists*

Think of it as **corrective steering, not a complete driving manual.** The model already knows how to drive. Instructions tell it which turns to take on *your* roads.

**This changes with every model generation.** A year ago, explicit instructions to "prefer `const` over `let`" were useful — older models were inconsistent about it. Today's frontier models do this by default. Instructions that were essential in 2024 may be redundant in 2026, and instructions written for Claude may be unnecessary for GPT (or vice versa). This is why the [Iteration and Fine-Tuning](#iteration-and-fine-tuning) section matters — review instructions when you change models. Remove rules the model already follows. Add rules where a new model's bias diverges from your preferences. The instruction set should evolve with the model, not calcify around the one you started with.

### How the Context Window Works

Instructions are injected into the system prompt at the start of every interaction. File content, tool results, and conversation history share the remaining context window. When the total context exceeds the model's window, older messages are compacted — summarized to preserve key information while freeing space for new content.

This has a practical consequence: **long instructions crowd out useful context.** Every token spent on instructions is a token unavailable for code, tool results, and conversation history. The recommended budget of 500-2000 words for always-on instructions is a tradeoff between instruction specificity and available working context. See [Context Window Guidelines](part-2-primitives.md#context-window-guidelines) in Part II for per-primitive sizing recommendations.

---

## Why Customize?

### Memory Is Not Enough on Its Own

[Copilot Memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory) reduces some of the friction described above automatically — it learns patterns as Copilot works in your repo. But Memory only captures what it observes, and only after it's seen enough activity. Explicit customization tells Copilot the right answer from the start, before mistakes happen. The two approaches reinforce each other.

### ROI of Customization

Teams that configure Copilot extensively report measurable improvements:

| Metric | Without Customization | With Customization |
|--------|----------------------|-------------------|
| PR review friction | High — repeated convention corrections | Low — code matches standards |
| Code consistency | Variable — depends on who's prompting | Consistent — same patterns everywhere |
| Onboarding time | Long — new devs reinvent prompts | Fast — prompts and agents ready |
| Context switching | Frequent — explain stack each time | Minimal — AI knows the codebase |

The investment is front-loaded: a few hours of configuration produces ongoing returns across every Copilot interaction.

### The 80/20 Rule

Most teams get 80% of the value from 20% of the configuration:

1. **Always-on instructions file** — Define your tech stack, conventions, and the anti-patterns that waste everyone's time in code review. This single file eliminates 50% of Copilot frustrations.
2. **2-3 skills** — Encode the procedural knowledge your team repeats constantly: component scaffolding patterns, test generation conventions, deployment workflows. Skills are portable across VS Code, Copilot CLI, and the coding agent.
3. **1-2 custom agents** — Build a code reviewer agent that knows your standards and an architect agent for design discussions.

Prompt files (`.prompt.md`) still work well for simple, single-purpose slash commands, but skills and agents handle most use cases with better portability and discoverability. MCP, hooks, and advanced configurations provide additional value for specific use cases.

See the [Getting Started](../ReadMe.md#getting-started) section for the step-by-step path.

---

## Iteration and Fine-Tuning

Customization is never "done." Codebases evolve, patterns change, and you learn what works.

### The Feedback Loop

```text
Use Copilot → Notice friction → Update customization → Repeat
```

| Signal | Action |
|--------|--------|
| Same PR feedback repeatedly | Add rule to instructions |
| Prompt produces inconsistent results | Add constraints or examples |
| Nobody uses a prompt | Remove it or improve discoverability |
| Instructions file is huge | Split into file-based instructions |
| New library/pattern adopted | Update tech stack section |
| Copilot keeps making the same mistake | Add ✅/❌ example to instructions |
| Deprecated patterns appearing in suggestions | Add explicit "avoid X" rule |
| Team asks "is there a prompt for X?" | Create one |

### Team Iteration

Customizations are first-class code. Change them as often as your codebase changes. Use PRs so the team stays aware.

### Let Copilot Tune Itself

The fastest way to find the gaps in your customization is to ask Copilot to reflect on its own sessions. It has more signal about what worked and what didn't than you do — it knows which instructions it followed, which it ignored because they were ambiguous, and which friction points kept showing up in the conversation.

At the end of a work session, or after landing a non-trivial task, ask Copilot to self-review and propose improvements. Keep a human in the loop: Copilot proposes, you approve and commit.

> 💬 **Try this prompt:**
>
> Reflect on this session and propose updates to our customization files. Specifically:
>
> 1. Look at `.github/copilot-instructions.md`, any files in `.github/instructions/`, and any skills in `.github/skills/` that were relevant.
> 2. Identify moments in this session where you made a wrong assumption, asked me for context you should have found in the repo, or repeated a correction I had to give you.
> 3. For each moment, propose a concrete change: a new rule, a clarified rule, an added ✅/❌ example, a new skill, or a rule to *remove* because it's redundant with the model's defaults or with another instruction.
> 4. Output the proposals as a diff I can review, with a one-line rationale for each.
>
> Don't edit any files yet — just show me the proposed diff.

Run this regularly (end of a feature, end of a sprint, after a long debugging session) and merge the proposals that hold up. Over time the instruction set converges on the rules that actually matter, and stops accumulating ones that don't.

---

## Measuring Success

GitHub Copilot assists across the entire software development lifecycle — from planning and coding to testing, deployment, and maintenance. Measuring its impact requires looking at both immediate indicators and ultimate outcomes. Better Copilot outcomes in code should directly translate to better outcomes for your repo, team, and organization.

### Start With Business Goals

Before picking metrics, pick *outcomes*. Metrics in isolation are noise — a cycle-time dashboard that nobody ties to a business goal becomes a vanity chart. The teams that get the most out of Copilot customization work the measurement hierarchy **top-down**: start with what the business is trying to achieve, then choose the metrics that prove (or disprove) you're getting there.

Typical business goals and the metrics that track them:

| Business Goal | What It Means | Primary Metrics |
|---------------|---------------|-----------------|
| **Ship faster** | Reduce time from idea to customer | Cycle time, lead time, deployment frequency, time to market |
| **Ship more** | Increase output without increasing headcount | Throughput, features shipped per engineer, developer capacity |
| **Ship safer** | Reduce production incidents and rework | Change failure rate, defect escape rate, MTTR, rework rate |
| **Lower total cost of ownership (TCO)** | Reduce fully loaded cost to build *and* run software | Engineering cost per feature, maintenance burden, cost to operate, infrastructure spend |
| **Improve developer experience** | Retain engineers, reduce friction, speed onboarding | Developer satisfaction (DX surveys), onboarding time to first PR, time spent on toil vs. new work |
| **Accelerate experimentation** | Learn faster by shipping more experiments cheaply | Experiments per quarter, cost of delay, cost to build per experiment, feature kill rate |
| **Increase revenue impact per engineer** | Make the engineering org a revenue lever, not just a cost center | Revenue per feature, feature ROI, feature adoption |
| **Improve customer satisfaction** | Ship the right things and ship them well — users notice quality, speed, and responsiveness | CSAT/NPS, time-to-resolution on customer-reported issues, support ticket volume |
| **Reduce risk and compliance exposure** | Meet regulatory obligations without slowing delivery | Audit coverage, policy violations caught pre-merge, security review turnaround |

Pick two or three goals that matter to *your* organization right now. Pin them to the wall. Every Copilot customization investment — instructions, skills, agents, hooks, workflows — should trace back to at least one. If it doesn't move any of the numbers that matter, it's optional.

The sections below walk the measurement stack top-down — business outcomes first (what leadership tracks), then DORA (engineering health), then flow metrics (leading indicators that move first). Flow metrics shift within days; DORA within weeks; business outcomes within quarters.

### Business Outcomes

Business outcomes are the point. Everything below them — DORA, flow, adoption — exists to move these numbers. Not every team needs to think this way; open-source projects, internal tools, and prototypes have different success criteria. But if the software needs to generate revenue, justify its operating costs, or compete for continued investment, engineering speed alone doesn't tell the full story.

**Organizational metrics** — the numbers a CFO or CTO reads on a quarterly dashboard:

| Metric | What It Measures | Connection to Copilot |
|--------|------------------|----------------------|
| **Time to Market** | Elapsed time from concept to production | Faster cycles across the SDLC compress this directly |
| **Engineering Cost per Feature** | Fully loaded cost to ship a capability | Copilot reduces effort per feature without adding headcount |
| **Total Cost of Ownership (TCO)** | Fully loaded cost to build, run, and maintain software over its lifetime | Copilot lowers build cost up front and shortens maintenance and incident-response work over time |
| **Defect Escape Rate** | Bugs reaching production per release | Better-generated tests and code review catch issues earlier |
| **Maintenance Burden** | % of engineering time spent on upkeep vs. new work | Copilot accelerates maintenance tasks, freeing capacity for new features |
| **Developer Capacity** | Effective output per engineer | The same team ships more — or the same output requires fewer people |

**Product and feature metrics** — whether what you ship actually matters:

| Metric | What It Measures | Why It Matters |
|--------|------------------|----------------|
| **Feature Adoption** | % of users who engage with a shipped feature | A feature nobody uses costs time to build and money to maintain |
| **Feature ROI** | Value delivered relative to cost of building | Connects engineering effort directly to outcomes |
| **Revenue per Feature** | Revenue attributable to a specific capability | Ties engineering output directly to business outcomes |
| **Cost of Delay** | Revenue or value lost per unit of time a feature isn't shipped | Quantifies the price of slow delivery — makes the case for faster cycles |
| **Feature Kill Rate** | % of shipped features retired or rolled back | High rates signal weak product judgment; low rates may signal over-caution |

Copilot compresses the *cost to build*, but compressed build costs only improve ROI if the features being built are the right ones. By making each experiment cheaper, Copilot makes it economically viable to try more ideas, kill the losers faster, and concentrate investment on the winners — product judgment still belongs to humans. Track these numbers before and after adoption; if the trendlines move while team size and practices stay roughly constant, the investment is paying off. Engineering organizations that articulate impact in business terms — cost, revenue, risk — get more investment and more autonomy than those reporting on developer satisfaction alone.

### Engineering Metrics (DORA)

DORA is how you know your engineering machine is actually capable of producing the business outcomes above:

| Metric | What It Measures | Target Impact |
|--------|------------------|---------------|
| **Deployment Frequency** | How often you ship | Increase |
| **Change Failure Rate** | % of deployments causing incidents | Decrease |
| **Mean Time to Recovery** | Time to fix production issues | Decrease |
| **Lead Time for Changes** | Commit to production | Decrease |

### Leading Indicators: Flow Metrics

Flow metrics move first — the earliest signal that a customization investment is paying off, and they predict the DORA and business numbers above.

| Metric | What It Measures | Target Direction |
|--------|------------------|------------------|
| **Cycle Time** | Time from work started to PR merged | Decrease |
| **Lead Time** | Time from issue created to deployed | Decrease |
| **Throughput** | PRs merged per week (team) | Increase |
| **PR Review Time** | Time from PR opened to first review | Decrease |
| **Rework Rate** | % of PRs requiring changes after review | Decrease |

Track via GitHub Insights, the GitHub API, or third-party tooling (LinearB, Jellyfish).

### The New Benchmark: A Feature a Day

With an AI-enhanced SDLC, **a feature a day** becomes the realistic target. Not a massive feature—a well-scoped, user-facing change that ships to production.

If you can't ship a feature in a day, examine:

| Blocker | Questions to Ask |
|---------|------------------|
| **Governance** | How many approvals are required? Can any be automated or parallelized? |
| **Handoffs** | How many people touch a feature before release? Can the same person carry it further? |
| **Feature Size** | Are you scoping features small enough? Can this be split into independently shippable slices? |
| **Environment** | How long does CI/CD take? Are deployments manual or automated? |
| **Testing** | Is testing blocking delivery? Can Copilot help generate tests faster? |

The bottleneck is rarely the coding. It's everything around the coding—reviews, approvals, deployments, coordination. AI accelerates the work; your processes determine whether that acceleration reaches users.

**Target state:** Issue created in the morning → designed, coded, tested, reviewed, deployed by end of day.

### SDLC Coverage

Copilot customization can improve every phase. Measure what matters — flow and feedback, not activity:

| SDLC Phase | Copilot Helps With | Measure |
|------------|-------------------|----------|
| **Planning** | Issue creation, story writing | Time from idea to ready-for-work |
| **Design** | Architecture discussions, API design | Decisions per iteration |
| **Coding** | Code generation, refactoring | Time in active development |
| **Testing** | Test generation, test design | Defects escaped to production |
| **Review** | PR reviews, security checks | Wait time for feedback |
| **Deploy** | Release notes, deployment scripts, deployment gates | Lead time to production |
| **Maintain** | Bug diagnosis, incident response, documentation | Mean time to recovery |

### Agentic Workflows: The Bigger Picture

The SDLC table above shows what Copilot helps with in each phase. **[GitHub Agentic Workflows](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/)** extend this further — agents don't just assist developers interactively, they run autonomously against your repository on a schedule, on events, or on demand.

Agentic Workflows are Markdown files in `.github/workflows/` that run coding agents inside GitHub Actions. GitHub calls this **Continuous AI**: the integration of AI into the SDLC alongside CI/CD. They handle continuous triage, documentation, code simplification, test improvement, quality hygiene, and reporting — all with defense-in-depth security, sandboxed execution, and safe outputs that require human review before merging.

The customization primitives covered in this guide shape how the coding agent performs during these workflows. Each primitive contributes a different layer:

- **Instructions** tell agents what conventions to follow
- **Skills** encode procedural knowledge the agent loads automatically
- **Custom agents** create specialized personas for specific tasks
- **MCP servers** connect agents to external APIs and tools
- **Hooks** enforce runtime policies and audit trails

For complete details — including workflow examples, coding agent configuration, and how each primitive feeds into autonomous work — see [Agentic Workflows](agentic-workflows.md).

### Practical Measurement Approach

**Solo developers:**
- Ask yourself: "Am I shipping faster?"
- Monitor PR merge time
- Note tasks that used to take hours but now take minutes

**Teams:**
- Baseline metrics before customization
- Track cycle time and throughput weekly
- Compare rework rates before/after

**Organizations:**
- Aggregate flow metrics across teams
- Track deployment frequency and change failure rate
- Measure onboarding time for new developers
- Calculate ROI based on time savings

---

## Rolling Out to Your Team

Adopting GitHub Copilot customization works best in phases. Each phase adds capability while giving teams time to build confidence:

| Phase | What to Deploy | What to Measure | Move to Next When |
|-------|---------------|-----------------|-------------------|
| **Day 1** | `copilot-instructions.md` + 2-3 prompt files | PR rework rate, developer feedback | Rework rate decreases; team reports less repetitive prompting |
| **Day 2-4** | File-based instructions, skills, MCP servers | Cycle time, tool invocation frequency | Skills actively discovered; MCP tools integrated into daily workflow |
| **Day 5-8** | Custom agents, hooks for enforcement, Memory enabled | Convention compliance, audit coverage | Hooks catch real violations; agents used for specialized tasks |
| **Day 9-13** | Agentic Workflows, SDK integration, agent plugins | Autonomous task completion rate, CI-driven agent output quality | Workflows run reliably; trust in autonomous operation established |

Start with the highest-value, lowest-risk primitive (`copilot-instructions.md`), prove value, then expand. Each phase builds on the trust and patterns established in the previous one — the full rollout fits inside two weeks.

---

## Scaling Beyond One Team

The rollout above works for a single team on a single repo. When the first team proves value and leadership asks "how do we roll this out across the org?", the operational questions change. Distribution, drift, ownership, and measurement become the bottlenecks — not authoring.

**Don't force every team onto the same rules.** The goal of scaling is to share what's genuinely reusable, not to impose uniformity. One team might require functional React with React Query; another might standardize on signals and a different state layer. One service might mandate strict typing and exhaustive error handling; another might optimize for rapid prototyping. Both can be right. Coupling every repo to a single source of truth turns customization into a political battleground and produces a baseline so watered-down it helps no one.

Aim for a thin shared baseline (security rules, commit conventions, org-wide anti-patterns) and let teams extend, override, or ignore the rest. GitHub Copilot reads the most specific instruction that applies — use that to your advantage rather than fighting it.

**Patterns will emerge as you reshape for the AI-native SDLC.** Don't try to design the perfect org-wide customization system up front. As teams adopt Copilot, rewire their workflows around autonomous agents, and push more work through the AI-assisted SDLC, shared conventions will surface on their own — a skill two teams independently wrote, a hook three teams copied, an instruction file that keeps showing up in PRs. *Those* are the patterns worth promoting to the shared baseline. Patterns imposed top-down before teams have discovered what actually works tend to calcify around yesterday's workflow and slow down tomorrow's.

Let the shared layer grow from real usage, not from a governance committee's whiteboard.

### Distribution Patterns

Three mechanisms ship customizations to many repos. Most organizations combine all three — keeping the shared layer small and the team-specific layer fully under each team's control.

| Pattern | Best for | Tradeoffs |
|---------|----------|-----------|
| **Org-level `.github` repo** | Baseline rules every repo inherits (security policies, commit conventions, PR templates). GitHub auto-applies files from the special `.github` repo to every repo in the org that doesn't override them. | Only covers community health files natively; Copilot instructions must be copied in via template, sync action, or agent plugin. |
| **[Agent Plugins (Preview)](part-2-primitives.md#agent-plugins-preview)** | Bundling related primitives (skills + agents + hooks + instructions) as a versioned, installable package teams opt into. | Preview feature; plugin format still stabilizing. Best when you want opt-in adoption per repo. |
| **Template repositories** | New repos that should start with a full customization set (instructions, skills, MCP config, workflow files). | One-time imprint — drift starts on day one. Good for greenfield projects; weak for keeping existing repos in sync. |

A common blended model: baseline `copilot-instructions.md` distributed via a sync action from a central repo, domain-specific skills and agents delivered as agent plugins teams install per repo, and template repos for new services.

### Ownership and CODEOWNERS

Customization files are source code — review them like source code. Add `.github/copilot-instructions.md`, `.github/instructions/`, `.github/prompts/`, `.github/skills/`, `.github/agents/`, `.github/hooks/`, and `.vscode/mcp.json` to [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositories-settings-and-security/customizing-your-repository/about-code-owners) so the right team reviews each change:

```text
# .github/CODEOWNERS
.github/copilot-instructions.md    @acme/platform-dx
.github/instructions/security-*    @acme/appsec
.github/hooks/                     @acme/appsec @acme/platform-dx
.github/skills/                    @acme/platform-dx
.vscode/mcp.json                   @acme/platform-dx
```

Hooks and MCP configs deserve stricter ownership because they can execute code or expose external systems — security review is non-optional.

### Drift Detection

Once customizations are distributed, they drift. Teams edit local copies, forget to pull upstream updates, and quietly diverge from the baseline. Some of that drift is healthy — a team adapting rules to fit their stack is exactly what you want. The goal isn't to eliminate drift, it's to distinguish *intentional divergence* from *silent rot* (outdated security rules, stale references, forgotten overrides). Detect drift with:

- **Scheduled sync actions** — a GitHub Action that, on a schedule, opens a PR in each downstream repo when the baseline repo's `copilot-instructions.md` or skill bundle has changed. Teams can merge, modify, or close the PR. Uses the [`peter-evans/create-pull-request`](https://github.com/peter-evans/create-pull-request) pattern or a custom script.
- **Drift reports** — a central workflow that clones every repo in the org, diffs its Copilot configuration against the canonical baseline, and posts a summary to Slack or an issue in the platform-DX repo. Treat it as visibility, not as a gate.
- **Agentic Workflows for review** — a scheduled agent workflow that inspects customization files across repos and flags *security-relevant* deviations (hook removal, MCP server changes, credential handling) rather than every stylistic difference. See [Agentic Workflows](agentic-workflows.md).

### Measuring Adoption at Scale

Per-team metrics (cycle time, rework rate) scale directly. Organization-level visibility comes from GitHub's APIs:

- **[Copilot Metrics API](https://docs.github.com/en/rest/copilot/copilot-metrics)** — aggregate usage (active users, chat turns, acceptance rates, agent mode sessions) at the org and enterprise level. Enables dashboards that correlate customization rollout with engagement.
- **[Copilot Usage API](https://docs.github.com/en/rest/copilot/copilot-usage)** — seat-level data for billing and license-management workflows.
- **[Audit log](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise#copilot-events)** — Copilot events in the enterprise audit log (policy changes, MCP server approvals, seat assignments) for compliance and incident response.
- **Hook-driven logging** — pipe [hooks](primitive-7-hooks.md) audit output to your SIEM for a per-session view of what Copilot did in high-risk repos.

### Phased Rollout Across the Organization

Resist the temptation to ship customizations org-wide on day one. Concentric waves build signal before scale:

| Wave | Scope | Exit criteria |
|------|-------|---------------|
| **Pilot** | 1-2 volunteer teams on active repos | Pilot teams report friction down, PR rework down; baseline `copilot-instructions.md` and 2-3 skills stable |
| **Wave 1** | 5-10 teams, mixed tech stacks | Customizations survive contact with different stacks; central team knows which rules generalize vs. which need per-team overrides |
| **Wave 2** | Department or business unit | Distribution mechanism (sync action, agent plugin, template) is working; CODEOWNERS are in place; drift detection live |
| **Wave 3** | Entire organization | Copilot Metrics API dashboards running; audit logging integrated; support rotation staffed for customization questions |

At each wave, collect qualitative feedback (what rules fire unnecessarily? which skills did nobody discover?) and trim. The biggest org-wide rollout failure mode is accumulating every team's rules into a shared file that satisfies no one. Keep the baseline lean; let teams extend it locally.

### Further Reading

For richer patterns — shared skills libraries, MCP server registries, governance guardrails, and GitHub's own rollout playbook — see [Rolling Out to Your Team](#rolling-out-to-your-team) above, [Agent Plugins (Preview)](part-2-primitives.md#agent-plugins-preview), and [Agentic Workflows](agentic-workflows.md).

---

## Best Practices

1. **Version control all customizations** — Treat `.github/` as code. Review changes in PRs.

2. **Start small** — Begin with 3-5 rules addressing common mistakes. Expand as friction points emerge.

3. **Use examples** — GitHub Copilot learns better from ✅/❌ patterns than abstract rules.

4. **Explain rationale** — When you specify a rule, explain *why*. Copilot uses this to make better edge-case decisions.

5. **Keep instructions focused** — If over 2000 words, split into file-based instructions or skills.

6. **Test prompts** — Run 3-5 times with varying inputs before sharing with team.

7. **Review quarterly** — Remove deprecated patterns, add new conventions, prune unused prompts.

[← Part I: What Copilot Is](part-1-foundations.md) | [Next: Part II - The Primitives →](part-2-primitives.md)
