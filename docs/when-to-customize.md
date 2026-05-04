# When to Customize (If Required)

[← Back to Guide](../ReadMe.md) | [← Foundations](foundations.md) | [Next: The Agent Loop →](agent-loop.md)

*Updated: May 4, 2026.*

---

## When Models Outgrow the Rules

The base GitHub Copilot agent on frontier models is already incredibly capable. Many internal teams use the base agent with little or no repository customization, because it can add value the moment it is pointed at a repository. In May 2026, frontier models like Claude Opus 4.7 and GPT-5.5 already follow language idioms, infer obvious patterns, and navigate unfamiliar codebases. The right starting point is an empty `.github/` folder and a real task, not a pre-authored stack of primitives written for a model that no longer exists. And if you do need to customize, the simplest move is to let GitHub Copilot do it for you. This guide explains how. Less is more.

GitHub Copilot also reads surrounding code the way a good developer does. It may not know why the team picked one pattern over another, but it can usually see what the repository already does and follow it. If `X` is a common engineering pattern, or if the codebase repeats it consistently, it probably does not need to become a rule. GitHub Copilot will often infer the pattern from context and copy the existing shape. Save customization for the cases where the reason matters, the pattern is surprising, or the model keeps guessing wrong.

Be cautious before importing the team's existing process wholesale. Code review checklists, onboarding docs, style guides, and PR templates were built to compensate for human limitations (forgetfulness, inconsistency, missing context) that frontier models do not share. Encoding those habits as primitives often re-creates problems the model would not have had, and adds context budget cost on top. Before turning a human convention into a rule, ask whether the model actually fails without it.

Many authoring habits also come from the GPT-3.5 Turbo and GPT-4 era, when models needed heavy scaffolding to produce useful work. Most of that scaffolding is now noise. It consumes context budget and hides the handful of rules that actually matter. The feedback loop runs both ways: teams add rules as they discover friction, but rarely delete rules newer models no longer need.

Colby, an engineer on the VS Code team, puts it directly: if primitives were written for an earlier model generation, consider deleting them and regenerating from scratch. The newer model may not need half the guidance, and the half it does need may be different.

The same rule cuts the other way for new repositories. Premature optimization with primitives (a polished `copilot-instructions.md`, a folder of prompts, a custom agent or two, a hook for every risky action) looks productive but is mostly guessing at problems the model would have handled on its own. Each unnecessary primitive burns context budget every session and locks in assumptions about a model generation that will be obsolete within months. Start empty. Use GitHub Copilot. Add a primitive only when a real session proves one is missing.

Tooling can help with that first pass. Projects like [microsoft/agentrc](https://github.com/microsoft/agentrc) score a repository's AI-readiness, generate a starter `copilot-instructions.md`, `.vscode/mcp.json`, and an evaluation file from the actual code, and re-check whether the generated context is still useful. Tools like that are a reasonable accelerator, but treat their output the way you would treat any generated scaffold: prune aggressively. The conventions, primitives, and even the tools themselves move fast. Anything generated today is calibrated to today's models and today's primitive surface, and may not age well. Whatever such a tool produces should still pass the same test as a hand-written rule: does the model actually fail without it?

What is clear, regardless of the tool, is that no team needs to start with forty primitives. The repositories that build GitHub Copilot, including [microsoft/vscode](https://github.com/microsoft/vscode) and [dotnet/runtime](https://github.com/dotnet/runtime) / [dotnet/aspnetcore](https://github.com/dotnet/aspnetcore), are some of the largest, oldest codebases at Microsoft, and their `copilot-instructions.md` files are remarkably short. The [How Microsoft and GitHub Actually Configure Their Repos](#how-microsoft-and-github-actually-configure-their-repos) section walks through what they encode and, just as importantly, what they leave out.

With that framing in place, the rest of this chapter explains where customization does earn its keep: the local, bespoke knowledge no model can infer on its own.

**See it in action:** [The Agent Customizations UI Nobody Knows About | Ep 1 of 8](https://www.youtube.com/watch?v=AZzCk-WGks4&t=24s) — Reynald Adolphe demos why VS Code customization matters and how agents, skills, instructions, prompt files, and hooks shape GitHub Copilot behavior.

## When to Customize (If Required)

The fastest way to understand customization is to forget AI for a moment and think about onboarding.

A new developer joins the team. They know the language. They know the frameworks. They are competent. What they do not know is where this repository is strange on purpose.

That is the right way to frame GitHub Copilot too: it is a new coworker who is already an excellent engineer, but still does not know this repository's local rules, tradeoffs, and history.

They do not know:

- why one framework was chosen over another,
- which folder owns a business concept,
- which shortcuts are tolerated in tests but forbidden in production,
- which review comments appear every week,
- which operational rules are mandatory even when they are inconvenient.

GitHub Copilot starts in exactly that position.

The bad output people call "hallucination" is usually not the model being broken. It is the model making the best guess it can from whatever context it has, the same way a competent new hire might confidently suggest the wrong file because nobody showed them the project structure first. When the context is thin, the model fills gaps with plausible-sounding assumptions drawn from public patterns. When the context is strong (clear instructions, the right files, relevant tool results), those assumptions get replaced by evidence, and the guesses get dramatically better. Most hallucination problems are not intelligence problems. They are context problems, and context is exactly what customization provides.

That is the real bespoke-software story. Most production repositories are not built from textbook defaults. They carry years of local decisions, and the failure modes are often weirdly specific. A generic model might wire up a `saveDraft()` path that also clears the published record because another codebase used the same helper for cleanup. It might call a `deleteUser()` routine that does not delete anything at all here because the team turned it into a soft-delete years ago and left the name behind. It might create a neat new caching layer that quietly bypasses the audit trail everyone is required to preserve. Code can look clean, compile, and even pass tests while still being bad code for that repository.

That is why customization matters. The problem is not only that GitHub Copilot might generate broken code. The deeper problem is that it can generate plausible code that ignores the repository's bespoke constraints and quietly reintroduces the same mistakes the team already learned not to make.

## What Customization Actually Does

Customization turns private team knowledge into shared runtime context.

It does not exist to micromanage every token. It exists to encode the decisions that would otherwise be rediscovered in review, in debugging, or in repeated prompting.

That usually means four kinds of knowledge:

- **Stack choices**: what the team uses and what it explicitly avoids.
- **Architectural patterns**: where concepts live and how code is expected to flow.
- **Procedural knowledge**: how recurring tasks are actually performed here.
- **Safety boundaries**: what the agent must not do, even if a model decides poorly.

## The Real Payoff

The payoff is not just better prose in chat. It is lower friction across the whole loop.

| Friction Without Customization | What Changes After Customization |
|--------------------------------|----------------------------------|
| Repeated review comments | Conventions become visible earlier |
| Re-explaining the stack in every session | Baseline context loads automatically |
| One person knows the deployment dance | That procedure becomes reusable knowledge |
| Risky actions rely on trust alone | Guardrails become enforceable |
| Good results depend on one careful prompter | The repo carries the knowledge, not just the individual |

### ROI of Customization

Teams that configure GitHub Copilot extensively report measurable improvements:

| Metric | Without Customization | With Customization |
|--------|----------------------|-------------------|
| PR review friction | High, repeated convention corrections | Low, code matches standards |
| Code consistency | Variable, depends on who is prompting | Consistent, same patterns everywhere |
| Onboarding time | Long, new devs reinvent prompts | Fast, prompts and agents ready |
| Context switching | Frequent, explain stack each time | Minimal, the system already knows |

The investment is front-loaded: a few hours of configuration produces ongoing returns across every GitHub Copilot interaction.

## The 80/20 Starting Point

Most teams do not need every primitive on day one.

Start with the smallest set that removes repeated pain:

1. **Always-on Instructions** for stack choices, conventions, and anti-patterns.
2. **One or two Skills or Prompts** for the tasks the team repeats constantly.
3. **One Custom Agent** when a recurring role needs a different posture, tool set, or review style.
4. **MCP or Hooks** only when the task genuinely requires outside reach or hard enforcement.

The mistake is not starting too small. The mistake is teaching GitHub Copilot a thousand tiny preferences before teaching it the few decisions that actually change outcomes.

That failure mode is easy to miss because it feels responsible. A team keeps adding one more rule, then one more exception, then one more style note, until the repository is effectively handing GitHub Copilot a policy binder instead of useful guidance. The context gets polluted with preferences, edge cases, and duplicated warnings that crowd out the few facts that actually matter.

Ask the same question a human developer would ask: what would anyone do with 100,000 rules? They would skim, miss half of them, memorize the ones that seem important, and start ignoring the document the moment it stopped sounding connected to real work. GitHub Copilot has the same problem in a different form. More rules do not automatically produce better behavior. Past a certain point, they just make the signal harder to find.

Good customization feels less like writing a constitution and more like leaving sharp, useful notes for the next competent engineer. Tell GitHub Copilot which paths are dangerous, which patterns are deliberate, and which defaults are wrong here. Do not bury that guidance under a mountain of policy trivia.

### The Over-Coupling Trap

Organizations that roll out GitHub Copilot across many repositories almost always make the same first move: they try to build one comprehensive configuration and push it everywhere. A central team drafts a master `copilot-instructions.md` with every convention, every architectural preference, every naming rule, every testing policy, then copies it into every repo, sometimes enforced through a template or automation.

It feels like good governance. It is actually the fastest way to produce instructions that help nobody.

The problem is coupling. A rule that matters in the payments service does not matter in the design system. A build procedure for the monorepo does not apply to the CLI tool. An API naming convention for the public SDK is irrelevant to an internal data pipeline. When every repo carries every rule, most of the context budget in any given session is wasted on rules that do not apply, and the model has to guess which ones matter right now.

The fix is not to avoid organization-wide configuration. It is to treat each repository's configuration as a hypothesis, not a policy.

**Start with a question, not a document.** Before adding a rule, ask: *What specific friction does this rule remove in this repo?* If the answer is "none yet, but it might help eventually," skip it. Add it when friction proves it is needed.

**Test, measure, delete.** Add one rule. Use GitHub Copilot for a few sessions. Did the output improve in a way the team can point to? Keep it. Did nothing change? Delete it. A rule that does not measurably change behavior is not free. It costs context budget every time it loads.

**Apply Colby's rule aggressively.** The "delete and regenerate" advice from the VS Code team is not just for stale instructions. It is a mindset. Every few model generations, the right move is to start from a blank file, add back only the rules that current models still need, and let go of everything else. Teams that treat their instruction files as permanent artifacts end up maintaining a document that was written for a model that no longer exists.

The organizations that get the most out of GitHub Copilot are not the ones with the most rules. They are the ones that iterate fastest by testing small hypotheses, measuring whether they worked, and deleting the ones that did not.

## What Not to Encode

Do not waste the context budget on rules the model already knows or tools already enforce.

Skip:

- formatting trivia the formatter can handle,
- lint rules the linter already blocks,
- generic language advice every strong model already follows,
- review preferences that no one can explain concretely.

Use customization for the parts of the repository that would surprise a competent outsider.

## The Feedback Loop

Customization is infrastructure, not a one-time setup task.

```text
Use GitHub Copilot -> notice friction -> encode the missing knowledge -> validate -> repeat
```

The strongest signals are boring ones:

- the same review comment appears again,
- the same stack choice has to be restated,
- the same task needs a long setup prompt,
- the same risky action needs human correction,
- the same repository concept is inferred incorrectly.

That is where the next rule, skill, prompt, or hook usually comes from.

### Let GitHub Copilot Tune Itself

One of the fastest ways to find missing guidance is to ask GitHub Copilot to reflect on its own sessions. It can often identify where it made a wrong assumption, where a rule was ambiguous, or where the same correction appeared repeatedly.

> 💬 **Try this prompt:**
> "Reflect on this session and propose updates to our customization files. Review the relevant instruction files and skills, identify where you made a wrong assumption or needed a repeated correction, and propose a concrete rule, example, skill, or deletion for each case. Output the proposals as a diff with a one-line rationale for each change. Do not edit any files yet."

For a fuller version that reviews commits, changed files, and available debug sessions before adding, editing, moving, or deleting primitives, use the [Primitive Maintenance Review prompt](primitive-3-prompts.md#primitive-maintenance-review).

Done regularly, that loop helps the instruction set converge on the rules that actually matter instead of accumulating ones that do not.

### How Microsoft and GitHub Actually Configure Their Repos

The best evidence for "less is more" comes from the teams that build GitHub Copilot and the tools it runs inside. These are not small hobby projects. They are among the largest, oldest, and most complex codebases at Microsoft, and their instruction files are remarkably short.

| Repository | Age / Scale | `copilot-instructions.md` Size | What It Covers |
|------------|-------------|-------------------------------|----------------|
| [`microsoft/vscode`](https://github.com/microsoft/vscode) | 15+ years, 600K+ LOC TypeScript | ~150 lines | Project architecture, build/validation steps, coding style, one "Learnings" entry |
| [`dotnet/runtime`](https://github.com/dotnet/runtime) | 25+ years of .NET lineage, millions of LOC | ~250 lines | Build/test matrix, C# conventions, commit policy, AI disclosure |
| [`dotnet/aspnetcore`](https://github.com/dotnet/aspnetcore) | Massive web framework | ~60 lines (plus topic-specific instruction files) | C# style, test runner, environment activation |

A few patterns stand out:

**They encode only what would surprise a competent contributor.** The VS Code instructions do not explain TypeScript. They explain *this codebase's* layered architecture, *this project's* tab-vs-space decision, and *this team's* disposable registration pattern. The dotnet/runtime instructions do not teach C#. They teach the mandatory baseline build step that trips up every new contributor and the specific `is null` preference that deviates from older .NET convention.

**They lean on structure, not volume.** ASP.NET Core keeps its root instructions under 60 lines and delegates component-specific rules to separate instruction files (like `components.instructions.md`). That is the file-based instruction primitive doing exactly what it was designed for: keeping the always-on file focused on what applies everywhere.

**They trust the model.** None of these files explain how to write a for-loop, handle exceptions generically, or follow basic language idioms. Those are rules the model already knows. The context budget goes to the rules it cannot know without being told.

The lesson is simple: if the teams building GitHub Copilot can configure a 15-year-old, 600K-line codebase in 150 lines, most repositories can do it in fewer. Start lean. Add a rule only when friction proves it is needed. And when the model gets smarter (which it will, with every generation) go back and delete the rules it no longer needs.

## Measurement Belongs Here, Not at the End

Teams often treat measurement as a later management concern. That is backwards.

If customization is supposed to reduce friction, the team should decide early what improvement would look like. That does not require a giant analytics program. It requires a small scorecard tied to the pain that triggered the work in the first place.

Useful early indicators include:

- repeated review comments per PR,
- time lost re-explaining repo conventions,
- number of recurring workflows still handled manually,
- number of safe tasks the team is comfortable delegating.

The full scorecard belongs in [Measuring Success](measuring-success.md). The important point here is simpler: if the team cannot describe the friction, it cannot tell whether the configuration helped.

## Why This Guide Starts with the Loop

Most documentation explains the file formats first. That is useful for lookup, but weak for understanding. Teams do not struggle because they forgot that `.prompt.md` exists. They struggle because they do not know where prompts, skills, agents, MCP, and hooks enter the same runtime.

That is why the next chapters shift quickly from the case for customization into the agent loop itself.

## Where to Read Next

- Read [The Agent Loop](agent-loop.md) for the runtime model behind every later chapter.
- Read [Primitives in Action](primitives-in-action.md) once the loop is clear and the question becomes composition.
- Use [Operational Reference](part-3-reference.md) only when the question becomes purely operational.