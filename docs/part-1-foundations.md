# Part I: Foundations

[← Back to Guide](../ReadMe.md)

*Published: February 20, 2026 · Validated against VS Code 1.116 and GitHub Copilot docs as of April 15, 2026.*

---

## Introduction

### What is GitHub Copilot?

GitHub Copilot is an AI coding assistant built into the editor. As of VS Code 1.116 (April 2026), Copilot is **built-in** — no extension installation required. New users get chat, inline suggestions, and agent mode out of the box. (Those who prefer not to use AI features can disable them with `chat.disableAIFeatures`.)

Copilot operates in three modes:

| Mode | What It Does | How to Use It |
|------|-------------|---------------|
| **Inline suggestions** | Predicts the next lines of code as you type (ghost text) | Just type — suggestions appear automatically |
| **Chat** | A conversational interface for asking questions, generating code, and explaining concepts | Open the Chat panel or press `Ctrl+I` / `Cmd+I` |
| **Agent** | An autonomous mode where Copilot plans multi-step tasks, calls tools, edits files, and runs terminal commands. **Autopilot** (preview) adds a fully autonomous permission level — the agent approves its own actions with no manual confirmations required. | Type in Chat with agent mode enabled |

Copilot connects to frontier language models (Claude, GPT, Gemini) hosted by GitHub. The models do the reasoning; the editor integration handles context — pulling in open files, workspace structure, and the customization files this guide covers.

**This guide assumes Copilot is already installed and working.** If not, start at [github.com/features/copilot](https://github.com/features/copilot) to set up a subscription. With VS Code 1.116+, Copilot is available immediately — no separate extension needed.

### GitHub Copilot CLI

[GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) reached general availability on February 25, 2026, bringing the full agentic experience to the terminal. The same agent capabilities available in VS Code — tool calling, file editing, test running — work directly from the command line.

| Mode | Behavior |
|------|----------|
| **Default** | Agent suggests actions; developer approves each one |
| **Bypass Approvals** | Skip confirmations for low-risk actions |
| **Autopilot** | Fully autonomous — agent approves its own actions, retries on errors, works until task completion |

Copilot CLI supports **multi-model** hot-swapping between Claude Opus 4.6, GPT-5.4, Gemini 3 Pro, and others during a session. Enterprises can use **BYOK (Bring Your Own Key)** to connect their own API keys for supported providers.

**Fleet mode** (`/fleet`) enables parallel sub-agent execution. Instead of one agent working sequentially, an orchestrator decomposes a task into independent subtasks, dispatches them to parallel sub-agents, tracks dependencies, and synthesizes the results. Use `/fleet` for large refactors, repo-wide maintenance, multi-file test generation, or any workload that can be divided and run concurrently:

```text
/fleet Refactor the auth module, update tests, and fix related docs
```

The orchestrator builds a task graph with dependency tracking — if Task C depends on A and B, it waits. Independent tasks run simultaneously. Monitor progress with `/tasks`.

**Remote sessions** (`/remote`) let developers start a CLI session locally and control it from any device via the GitHub web interface or GitHub Mobile. The session streams in real time — send instructions, approve actions, switch modes, and answer questions from a browser or phone. Useful for long-running tasks, headless environments, or moving between devices without losing context:

```text
/remote          # enable remote access for the current session
copilot --remote # start a new session with remote access
```

The CLI generates a URL and QR code. Only the authenticated GitHub account can access the session. Use `/keep-alive` to prevent the machine from sleeping during long tasks.

Available to all paid Copilot subscribers (Pro, Pro+, Business, Enterprise). The repository customization primitives covered in this guide — instructions, skills, agents, MCP — apply to CLI sessions the same way they apply in VS Code.

### Key Terms

These terms appear throughout the guide:

| Term | Meaning |
|------|---------|
| **Primitive** | A configuration file type that customizes Copilot (always-on instructions, file-based instructions, prompts, skills, custom agents, MCP, hooks, memory, agentic workflows, Copilot SDK) |
| **Agent** (agentic mode) | Copilot operating autonomously — planning steps, calling tools, iterating on results |
| **Custom agent** | A `.agent.md` file that defines a specialized persona with constrained tools and behavior |
| **Context window** | The total amount of text the model can consider at once — instructions, code, and conversation all compete for this space |
| **Inline suggestions** | Ghost text (autocomplete) that appears as you type — a separate pipeline from Copilot Chat |
| **MCP** | Model Context Protocol — a standard for connecting AI agents to external tools and data sources |

Imagine your first day at a new company. Someone hands you a laptop, points at a million lines of code, and says "add a feature to checkout." No architecture docs. No style guide. No idea where to go for help.

You start reading. In one file, 2+2 equals 5. In another file, 2+2 equals 0. Someone invented their own math system three years ago and never documented it. The function called `save()` actually deletes things. The `UserService` doesn't handle users—that's in `AccountManager`, except when it's in `ProfileHandler`, except on the front-end which follows its own logic.

None of this matches anything you learned. It's not wrong, exactly—it's *bespoke*. Someone built a custom framework on top of a custom ORM on top of a custom router, and the only person who understood it left for a startup in 2019.

Now someone asks you to make a change. You do your best. You give them something reasonable based on everything you've read. They get mad. *"Why would you use Redux? We use React Query! It's obvious!"* 

It wasn't obvious. It was in a file you hadn't opened yet, buried in a .deprecated folder.

**That's Copilot's reality—*every single time you send a prompt.***

It's not hallucinating. It's doing exactly what you'd do: making the best possible suggestions from incomplete context. The suggestions you reject? Those are reasonable choices for a codebase Copilot hasn't been taught to understand. The "wrong" answers? They're only wrong because Copilot doesn't know your team decided to do things differently.

This guide fixes that.

**The right mental model: Copilot is a new developer on your team.**

But here's the twist: this new developer is already an excellent coder. Frontier models like Claude Opus 4.6, GPT-5.4, Gemini 3 Pro know language idioms, common patterns, and industry best practices. They've seen more code than any human ever will. You don't need to teach them how to write a for-loop or when to use async/await.

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

### The Three Pillars of Copilot Success

Copilot's output quality depends on three factors:

| Pillar | Impact | What You Control |
|--------|--------|------------------|
| **Model Selection** | Raw reasoning power and behavior | Choose frontier models for complex work; accept that different models work differently |
| **Codebase Quality** | How well Copilot can understand your code | Write clean, well-documented, modular code |
| **Repository Configuration** | The context and rules Copilot operates with | **This guide** — the ten customization primitives |

Your **model selection** matters more than most people realize. A frontier model with extended thinking will dramatically outperform a model from two years ago—it's not even close. Claude Opus 4.6, GPT-5.4, Gemini 3 Pro with thinking enabled will reason through multi-file refactors, catch edge cases, and produce code that actually works on the first try. Older or faster models (like GPT-5.4 mini) trade depth for speed — useful for simple tasks but prone to missing the point on complex ones.

Different models also *behave* differently, and that's okay. Some are more verbose. Some ask more clarifying questions. Some jump straight to implementation. Learn your model's personality and work with it, not against it. The best model for your workflow might not be the newest or the fastest—it's the one whose behavior matches how you like to work.

**See it in action:** For a live demo, watch Sandeep Somavarapu in [Bring Your Own Model (BYOM)](https://www.youtube.com/watch?v=W_WnyS_cXCk) and Julia Kasper in [How We Ship Models in VS Code](https://www.youtube.com/watch?v=eVxIwpGbHEk).

Your **codebase quality** matters — a well-structured codebase with clear naming, small functions, and comprehensive tests gives Copilot better context to work with. Messy, tangled code confuses AI just as much as it confuses human developers.

But even with the best model and cleanest codebase, **repository configuration** is what transforms Copilot from a generic assistant into a team-aware partner. This guide is the complete reference for setting up your repository for the best possible outcomes with GitHub Copilot.

### The Over-Instruction Trap

Every model arrives with **bias** — a set of default preferences baked in by training data. Claude Opus 4.6 prefers functional patterns and explicit error handling. GPT-5.4 reaches for object-oriented structures and comprehensive type annotations. Gemini 3 Pro gravitates toward concise, pragmatic solutions. These biases aren't bugs. They're the distilled wisdom of millions of codebases, and most of the time they produce solid, idiomatic code without any instructions at all.

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

---

**About This Guide**

This guide focuses on the customization primitives that help Copilot understand your existing codebase — your conventions, patterns, and preferences. These tools work with your code as it exists today.

**Coming Soon:** A companion guide covering how to refactor and restructure code so AI agents have an easier time understanding and modifying it.

**Multiple Surfaces:** GitHub Copilot operates across multiple environments — VS Code, Visual Studio, GitHub.com, and [GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) (a terminal-based AI agent). Most customization primitives covered in this guide work across all these surfaces, meaning the configuration you create for VS Code also benefits developers working from the command line or on GitHub.com. Surface-specific differences are noted in each primitive's documentation.

**Copilot Memory:** Beyond explicit customization, [Copilot Memory](primitive-8-memory.md) (public preview) lets Copilot automatically learn and retain repository-level context across sessions. Memory complements the primitives covered here — see the [dedicated section](primitive-8-memory.md) for how the two approaches work together.

**Open Source Reference:** VS Code and the GitHub Copilot extension are open source. When documentation is unclear or you want to understand exactly how a feature works, the source code at https://github.com/microsoft/vscode is the authoritative reference. Search the codebase for instruction parsing, prompt handling, or MCP integration to see implementation details firsthand.

When properly configured, Copilot can:

- Respect team coding conventions automatically
- Follow architectural patterns without prompting
- Avoid deprecated libraries and anti-patterns
- Generate code that passes PR review on the first try

This guide provides a comprehensive walkthrough of every customization primitive available in GitHub Copilot. By the end, development teams will have the knowledge to transform Copilot from a generic assistant into a context-aware team member that understands the nuances of their specific codebase.

**Official docs:** [Copilot customization overview](https://code.visualstudio.com/docs/copilot/copilot-customization)

**See it in action:** For a live demo, watch Harald Kirschner in the [Agent Sessions Day Keynote](https://www.youtube.com/watch?v=2-Q_sdJ5H2c), Pierce Boggan and Peng Lyu in [How VS Code Builds with AI](https://www.youtube.com/watch?v=ee-obY-4rqk), Courtney Webster in [Customize Your Agents](https://www.youtube.com/watch?v=flpKLkZla2Q), Connor Peet in [Extend Agents with MCP](https://www.youtube.com/watch?v=_g29UQjIAeI), Josh Spicer in [A Unified Agent Experience](https://www.youtube.com/watch?v=YmpjvZ3xkx8), and Alex Weininger in [Copilot CLI in VS Code](https://www.youtube.com/watch?v=_l3UO1oUoec).

---

## Why Customize?

### The Cost of Not Customizing

Without customization, every Copilot interaction starts from zero. The AI doesn't know:
- Your team uses React Query, not Redux
- Tests should use Vitest, not Jest
- All API responses must follow your envelope format
- Certain libraries are deprecated

This information gets repeated in prompts, ignored in suggestions, or caught in PR review. Each instance costs time.

The customization primitives are your onboarding documentation for this AI team member.

[Copilot Memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory) reduces some of this friction automatically — it learns patterns as Copilot works in your repo. But Memory only captures what it observes, and only after it’s seen enough activity. Explicit customization tells Copilot the right answer from the start, before mistakes happen. The two approaches reinforce each other.

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

---

## Measuring Success

GitHub Copilot assists across the entire software development lifecycle — from planning and coding to testing, deployment, and maintenance. Measuring its impact requires looking at both immediate indicators and ultimate outcomes. Better Copilot outcomes in code should directly translate to better outcomes for your repo, team, and organization.

### The Measurement Hierarchy

```text
+-----------------------------------+
|     Ultimate Outcomes             |  ← Revenue, costs, features shipped, customer satisfaction
+-----------------------------------+
|     Product Metrics               |  ← Deployment frequency, change failure rate, MTTR
+-----------------------------------+
|     Flow Metrics (Leading)        |  ← Cycle time, lead time, throughput
+-----------------------------------+
|     Adoption Metrics              |  ← Usage, engagement, prompt invocations
+-----------------------------------+
```

### Leading Indicators: Flow Metrics

These metrics show early impact and predict downstream improvements:

| Metric | What It Measures | How to Track |
|--------|------------------|---------------|
| **Cycle Time** | Time from work started to PR merged | GitHub Insights, LinearB, Jellyfish |
| **Lead Time** | Time from issue created to deployed | Jira/GitHub + deployment tracking |
| **Throughput** | PRs merged per week (team) | GitHub API |
| **PR Review Time** | Time from PR opened to first review | GitHub Insights |
| **Rework Rate** | % of PRs requiring changes after review | PR comment/commit analysis |

**What to look for:**
- Cycle time decreasing (faster delivery)
- Throughput increasing (more work completed)
- Rework rate decreasing (higher first-time quality)

### Engineering Metrics (DORA)

The four DORA metrics connect flow to engineering outcomes:

| Metric | What It Measures | Target Impact |
|--------|------------------|---------------|
| **Deployment Frequency** | How often you ship | Increase |
| **Change Failure Rate** | % of deployments causing incidents | Decrease |
| **Mean Time to Recovery** | Time to fix production issues | Decrease |
| **Lead Time for Changes** | Commit to production | Decrease |

### Product Metrics

DORA tells you how well your engineering machine runs. Product metrics tell you whether what comes out of that machine matters.

Not every team needs to think this way — open-source projects, internal tools, and prototypes have different success criteria. But if the software needs to generate revenue, justify its operating costs, or compete for continued investment, engineering speed alone doesn't tell the full story. Shipping faster only counts if what ships moves the needle.

| Metric | What It Measures | Why It Matters |
|--------|------------------|----------------|
| **Feature Adoption** | % of users who engage with a shipped feature | A feature nobody uses costs time to build and money to maintain |
| **Feature ROI** | Value delivered relative to cost of building | Connects engineering effort directly to outcomes |
| **Cost of Delay** | Revenue or value lost per unit of time a feature isn't shipped | Quantifies the price of slow delivery — makes the case for faster cycles |
| **Cost to Build** | Total engineering investment (time, people, infrastructure) | Baseline for ROI calculations; Copilot should bend this curve down |
| **Cost to Operate** | Ongoing infrastructure, maintenance, and support costs | Features that are cheap to build but expensive to run still erode margins |
| **Revenue per Feature** | Revenue attributable to a specific capability | Ties engineering output directly to business outcomes |

**Where Copilot fits:** Copilot compresses the *cost to build* — faster coding, faster testing, faster iteration. But compressed build costs only improve ROI if the features being built are the right ones. The most productive engineering team in the world still loses if it ships features nobody wants.

This creates a feedback loop worth paying attention to:

```text
Lower cost to build → Ship more experiments → Learn faster → Pick better features → Higher feature ROI
```

Copilot doesn't pick the right features to build. Product judgment still belongs to humans. But by reducing the cost of each experiment, Copilot makes it economically viable to try more ideas, validate them faster, and kill the ones that don't work before they accumulate operating costs.

### Business Metrics

For organizations where software is a revenue driver — or where engineering is a cost center that needs to justify its budget — these metrics connect the dots between Copilot adoption and the numbers leadership actually cares about.

| Metric | What It Measures | Connection to Copilot |
|--------|------------------|----------------------|
| **Time to Market** | Elapsed time from concept to production | Faster cycles across the SDLC compress this directly |
| **Engineering Cost per Feature** | Fully loaded cost to ship a capability | Copilot reduces effort per feature without adding headcount |
| **Defect Escape Rate** | Bugs reaching production per release | Better-generated tests and code review catch issues earlier |
| **Maintenance Burden** | % of engineering time spent on upkeep vs. new work | Copilot accelerates maintenance tasks, freeing capacity for new features |
| **Developer Capacity** | Effective output per engineer | The same team ships more — or the same output requires fewer people |

None of these metrics require attributing every improvement to Copilot specifically. Track them before and after adoption. If the trendlines move in the right direction while engineering practices and team size stay roughly constant, the investment is paying off.

**A note on framing:** Engineering organizations that can articulate their impact in business terms — cost savings, revenue acceleration, risk reduction — tend to get more investment, more autonomy, and more trust. Copilot customization is a lever worth measuring in those terms, not just developer satisfaction surveys.

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

For complete details — including workflow examples, coding agent configuration, and how each primitive feeds into autonomous work — see [Primitive 9: Agentic Workflows](primitive-9-agentic-workflows.md).

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

## Best Practices

1. **Version control all customizations** — Treat `.github/` as code. Review changes in PRs.

2. **Start small** — Begin with 3-5 rules addressing common mistakes. Expand as friction points emerge.

3. **Use examples** — Copilot learns better from ✅/❌ patterns than abstract rules.

4. **Explain rationale** — When you specify a rule, explain *why*. Copilot uses this to make better edge-case decisions.

5. **Keep instructions focused** — If over 2000 words, split into file-based instructions or skills.

6. **Test prompts** — Run 3-5 times with varying inputs before sharing with team.

7. **Review quarterly** — Remove deprecated patterns, add new conventions, prune unused prompts.

[Next: Part II - The Primitives →](part-2-primitives.md)
