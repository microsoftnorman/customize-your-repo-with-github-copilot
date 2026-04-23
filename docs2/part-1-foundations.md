# Foundations and Why Customization Matters

[← Back to Guide](README.md) | [Next: The Agent Loop →](agent-loop.md)

*Updated: April 22, 2026.*

---

## What GitHub Copilot Is

GitHub Copilot is not one feature in one editor. It is a platform for agentic software development that runs across IDEs, the terminal, GitHub.com, GitHub Actions, and custom applications. The same core runtime can answer a question, plan a multi-step task, run tools, delegate work, review a pull request, or operate inside another surface entirely.

That broader view matters because customization only makes sense at the platform level. A repository is not teaching one chat panel how to behave. It is teaching GitHub Copilot how to work inside a specific engineering system.

## What This Guide Teaches

This guide is about the layer between a frontier model and a real codebase. Out of the box, GitHub Copilot already knows language syntax, common frameworks, and public patterns. It does not know the architectural choices, anti-patterns, review culture, or operational constraints that make one repository different from another.

The purpose of customization is to encode those differences explicitly.

This guide teaches that in four moves:

1. Explain the platform and the problem.
2. Explain the agent loop that turns a prompt into work.
3. Explain the eight primitives as levers on that loop.
4. Explain where the same knowledge runs after it leaves the editor.

## Key Terms

| Term | Meaning |
|------|---------|
| **Agentic** | GitHub Copilot plans steps, calls tools, checks results, and iterates instead of replying once and stopping. |
| **Primitive** | A repository-level customization mechanism such as Always-on Instructions, Prompts, Skills, Custom Agents, MCP, Hooks, or Memory. |
| **Agent loop** | The repeated cycle of context assembly, decision-making, tool use, result ingestion, and stopping conditions. |
| **Surface** | The environment where GitHub Copilot runs: VS Code, GitHub Copilot CLI, the Cloud Coding Agent, GitHub.com, or a custom app. |
| **Execution environment** | A runtime that consumes the same primitive layer in a different place, such as code review, Agentic Workflows, or the Copilot SDK. |

## Where GitHub Copilot Runs

The same repository can be read by multiple surfaces. That is why the customization files live in conventional places such as `.github/` and `.vscode/` instead of inside one editor's private state.

| Surface | Why It Matters |
|---------|----------------|
| **VS Code** | Richest customization support and the fastest feature cadence. |
| **GitHub Copilot CLI** | Shows the agent model most clearly because the loop, tools, and approvals are visible at the terminal. |
| **Cloud Coding Agent** | Demonstrates what happens when the same knowledge runs remotely and asynchronously. |
| **GitHub.com** | Important for code review, repository policy, and workflow-triggered automation. |
| **Other IDEs** | Useful reminder that the primitive layer is portable even when the authoring UX differs. |

**See it in action:** [Agent sessions and where agents run](https://www.youtube.com/watch?v=0CsKOO7d35I&t=129s) — Gwyneth Peña-Siguenza demos switching an agent session between local execution, GitHub Copilot CLI, and the GitHub platform.

## Models Matter, but They Are Not the Whole Story

Model quality still changes the ceiling. Better reasoning models handle ambiguity, larger refactors, and more nuanced review. Faster models are useful for narrow loops and lightweight tasks. But model selection does not replace repository customization.

A strong model with no repository context still defaults to public-code patterns. A repository with clear instructions, procedural knowledge, and guardrails makes every supported model more useful.

The practical rule is simple: choose the best model the task justifies, then teach that model how your repository works.

## The Three Inputs to Copilot Quality

| Input | What It Changes | Who Controls It |
|-------|-----------------|-----------------|
| **Model selection** | Reasoning depth, style, latency, and bias | The user, the team, or enterprise policy |
| **Codebase quality** | How easy it is to infer architecture and intent | The repository maintainers |
| **Repository customization** | What GitHub Copilot is explicitly told, allowed, and connected to | The repository maintainers |

This guide is mostly about the third input, but the other two never disappear. A messy repository cannot be rescued by instructions alone. A weak model cannot be turned into a frontier one by adding more YAML.

## Why Customize at All

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

The bad output people call hallucination is often a weaker problem than that. The model is usually making a reasonable choice for a generic public codebase. It is wrong only because the repository's local rules were never made explicit.

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

## The 80/20 Starting Point

Most teams do not need every primitive on day one.

Start with the smallest set that removes repeated pain:

1. **Always-on Instructions** for stack choices, conventions, and anti-patterns.
2. **One or two Skills or Prompts** for the tasks the team repeats constantly.
3. **One Custom Agent** when a recurring role needs a different posture, tool set, or review style.
4. **MCP or Hooks** only when the task genuinely requires outside reach or hard enforcement.

The mistake is not starting too small. The mistake is teaching GitHub Copilot a thousand tiny preferences before teaching it the few decisions that actually change outcomes.

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

That is why the next chapters shift quickly from platform basics into the case for customization and then into the agent loop itself.

## Where to Read Next

- Read [The Agent Loop](agent-loop.md) for the runtime model behind every later chapter.
- Read [Primitives in Action](primitives-in-action.md) once the loop is clear and the question becomes composition.
- Use [Operational Reference](part-3-reference.md) only when the question becomes purely operational.
