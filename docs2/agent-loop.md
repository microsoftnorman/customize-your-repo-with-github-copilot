# The Agent Loop

[← Back to Guide](README.md) | [← Foundations and Why Customization Matters](part-1-foundations.md) | [Next: Primitives in Action →](primitives-in-action.md)

*Updated: April 22, 2026.*

---

## Why This Chapter Is the Spine

Most teams meet the primitives as files. They should meet them as control points inside a runtime.

The agent loop is that runtime.

**See it in action:** [Inside The Agent Loop with Pierce Boggan](https://www.youtube.com/watch?v=ENxVTtLW_Bc&t=150s) — Pierce Boggan demos the agent loop as an iterative while-loop of prompts, tool calls, and model interactions.

A request enters the system. GitHub Copilot assembles context. The model chooses what to do next. A tool may run. Results come back. The model updates its plan. The loop continues until the task converges, fails, or is stopped.

Once that picture is clear, the primitives become easier to reason about:

- Always-on Instructions and File-based Instructions change what the loop sees.
- Prompts, Skills, and Custom Agents change how the loop is framed.
- MCP changes what the loop can reach.
- Hooks change what the loop is allowed to do at execution time.
- Memory changes what the loop already knows before it starts asking questions.

## One Turn Through the Loop

| Step | What Happens | What Can Change It |
|------|---------------|--------------------|
| **1. Context assembly** | The surface, model, conversation state, relevant files, and other high-signal inputs are assembled. | Instructions, agents, active task framing |
| **2. Task shaping** | The model sees the request through whatever customization layers apply. | Prompts, Skills, Custom Agents, matching instructions |
| **3. Decision** | The model decides whether to answer, read more, call a tool, or delegate work. | Skill descriptions, tool availability, agent posture |
| **4. Action** | A tool runs, a file is read, a command executes, or a subagent is launched. | MCP, surface capabilities, permissions, hooks |
| **5. Feedback** | Tool results come back into the model as fresh evidence. | Result quality, context size, validation signals |
| **6. Stop or continue** | The loop ends with an answer or continues with another step. | The task, the evidence, and any blocking controls |

The runtime is iterative by design. It is not one giant hidden prompt. It is a chain of smaller decisions connected by evidence.

## Where the Primitives Enter

| Primitive | Primary Effect on the Loop |
|-----------|----------------------------|
| **Always-on Instructions** | Establish base rules on every turn |
| **File-based Instructions** | Add scoped rules only when matching files are relevant |
| **Prompts** | Frame a specific task and often constrain tool use |
| **Skills** | Inject reusable procedure when intent matches |
| **Custom Agents** | Change role, toolset, and behavior across a conversation or delegated task |
| **MCP** | Expand the loop beyond the local workspace |
| **Hooks** | Intercept lifecycle boundaries outside the model |
| **Memory** | Contribute repository knowledge learned over time |

That breakdown is the reason this guide teaches composition early. A team almost never has a problem that is solved by one isolated file type in the abstract. It has a problem somewhere in this loop.

## Subagents Make the Loop Fractal

A subagent is not a side conversation. It is another loop.

The parent loop delegates a focused task, the child loop starts with narrower context, and the child returns a result instead of every intermediate search, failed guess, or detour.

That is why the subagent story matters so much in the local source material. The podcast and video coverage on subagents makes one point repeatedly: isolation is the feature. Without it, the parent loop drowns in its own exploratory work.

Use that model when the task benefits from:

- independent research,
- parallel exploration,
- specialized review,
- or different permissions and models for different branches of the same job.

## Hooks Change the Control Model

Most primitives guide reasoning. Hooks govern execution.

That difference is easy to miss until the agent is doing real work.

Instructions can say "do not print secrets". A hook can block the command that would print them. Instructions can say "avoid dangerous shell commands". A hook can inspect the invocation and deny it. That is why hooks belong in the loop chapter and not only in a later security appendix.

## Failure Modes That Feel Like Product Problems but Are Usually Loop Problems

The symptoms teams complain about often come from loop design, not model intelligence.

- **Context bloat**: too much irrelevant state makes each turn worse.
- **Weak decomposition**: the loop keeps taking shallow steps because the task was never framed clearly.
- **Missing repo knowledge**: the model uses public defaults because the repo never taught it otherwise.
- **Weak enforcement**: the model was asked nicely instead of being constrained operationally.
- **Poor tool reach**: the loop cannot access the external system the task depends on.

Those are the real reasons customization matters.

## The Question That Picks the Next Primitive

When deciding what to add, ask one question:

**What part of the loop is failing?**

- If the baseline rules are wrong, use instructions.
- If the task framing is wrong, use prompts, skills, or agents.
- If the agent cannot reach required systems, use MCP.
- If the action must be constrained, use hooks.
- If repeated repository knowledge keeps being rediscovered, capture it explicitly or let Memory reinforce it.

That question is more useful than memorizing filenames in isolation.

## Where to Read Next

- Read [Primitives in Action](primitives-in-action.md) next to see three end-to-end workflows built on this loop.
- Then use [The Eight Primitives](part-2-primitives.md) as the decision bridge into the individual chapters.
