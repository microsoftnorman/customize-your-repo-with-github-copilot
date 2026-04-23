# The Agent Loop

[← Back to Guide](../ReadMe.md) | [← Part I: Foundations](part-1-foundations.md)

*Updated: April 22, 2026 · Validated against VS Code 1.116 and GitHub Copilot docs as of April 21, 2026.*

---

## What the Agent Loop Is

[Why Customize](part-1b-why-customize.md) explains the human problem: repeated friction, missing local context, and rules that only exist in review comments or tribal knowledge. This chapter picks up from there and shows where that missing context enters the runtime. Read it before [Part II: The Primitives](part-2-primitives.md), because the primitive files make more sense once the execution path is visible.

**Official docs:** [Customize AI in Visual Studio Code](https://code.visualstudio.com/docs/copilot/customization/overview) · [Subagents in Visual Studio Code](https://code.visualstudio.com/docs/copilot/agents/subagents) · [Custom agents in VS Code](https://code.visualstudio.com/docs/copilot/customization/custom-agents)

**See it in action:** [Inside The Agent Loop with Pierce Boggan](https://www.youtube.com/watch?v=ENxVTtLW_Bc&t=0s) — Pierce Boggan and James Montemagno walk through the agent loop as a runtime model of model calls, tools, context, and subagents.

The easiest way to understand agentic coding is to picture a large `while` loop. A request enters the system, Copilot assembles the prompt for the current surface, the model decides whether to answer directly or call a tool, the tool result comes back, and the loop continues until the task converges or the agent stops.

That is the agent loop. It is not one giant opaque prompt. It is a sequence of model invocations, tool calls, and state updates. Once that clicks, the primitives stop looking like a pile of unrelated files and start reading as levers that change how the loop behaves.

This chapter is not a ninth primitive. The loop is the execution model behind agentic behavior. The primitives in this guide customize what the loop knows, what it can do, and what boundaries it runs inside.

The next step after this chapter is [Part II: The Primitives](part-2-primitives.md). That chapter turns the loop into a practical decision: which primitive changes behavior globally, which one only helps for a single task, which one expands external access, and which one enforces rules at execution time.

---

## One Turn Through the Loop

For one user request, the loop typically looks like this:

| Step | What Happens | Why It Matters |
|------|--------------|----------------|
| **1. Session context is assembled** | Copilot builds the request from system prompts, the selected surface or mode, the active model, explicit user context, and high-signal implicit context such as open files or terminal state. | The model is never reasoning from the user message alone. The loop starts with a shaped request. |
| **2. Customization is applied** | Always-on Instructions, matching file-based instructions, prompt files, custom agents, skills, and available MCP tools shape what the model sees and what it can do. | This is where repository customization changes behavior before any tool call happens. |
| **3. The model chooses the next action** | The model decides whether it has enough information to answer or whether it should call a tool first. | Good agent behavior is mostly about choosing the right next step, not generating the final paragraph early. |
| **4. A tool executes** | Copilot might search the codebase, read files, edit code, run terminal commands, call an MCP server, or invoke a subagent. | Tools turn a chat model into an agent. Without tools, there is no real loop. |
| **5. Results are fed back into the loop** | Tool output is returned to the model as fresh context for the next turn. | The agent is not "thinking forever" in one pass. It is reacting to new evidence each cycle. |
| **6. The loop either continues or stops** | If more work is needed, Copilot takes another step. If the task is complete or blocked, it returns a final response. | A strong final answer is usually the result of several smaller decisions inside the loop. |

The shape is simple even when the workflow is not:

```text
User request
  -> context assembly
  -> customization layers applied
  -> model decides: answer or use a tool?
       -> tool call
       -> tool result
       -> model decides next step
  -> repeat until done
  -> final response
```

That is true whether the surface is VS Code, GitHub Copilot CLI, the cloud coding agent, or the Copilot SDK runtime embedded in a custom application. The exact tools and lifecycle differ by surface, but the pattern is the same: gather context, choose an action, observe the result, and continue until the task stops.

---

## Where Customization Enters the Loop

The agent loop is where the rest of this guide comes together.

| Mechanism | Role in the Loop |
|-----------|------------------|
| **Always-on Instructions** | Establish the base rules Copilot should follow on every turn. |
| **File-based Instructions** | Add context-sensitive rules when the loop touches matching files. |
| **Prompts** | Frame a specific task and often constrain which tools are available for that run. |
| **Skills** | Inject reusable procedures or domain knowledge when the task description matches. |
| **Custom Agents** | Change the persona, tool set, and optional model preferences for the whole conversation or delegated task. |
| **MCP** | Expands the loop beyond the local workspace by giving Copilot external tools and data sources. |
| **Hooks** | Sit outside the model and intercept lifecycle events or tool execution boundaries. They do not guide reasoning; they enforce or log actions. |
| **Memory** | Adds learned repository context that can be retrieved and validated during agent reasoning on supported surfaces. |

That distinction matters. Instructions, prompts, skills, and agents shape the model's *decision-making*. Hooks govern what happens when those decisions turn into actions. MCP changes what the loop is capable of reaching. Memory changes what the loop already knows before it starts asking questions.

If a team is confused about where to put a new rule, the fastest question is: does this change how the loop thinks, what it can access, or what it is allowed to do? The answer usually points to the correct primitive.

---

## Subagents: Delegated Loops with Isolated Context

Subagents are not side channels and they are not just "parallel prompts." A subagent is a delegated agent loop with its own isolated context. The main agent decides that part of the task would benefit from separation, starts a subagent, passes only the relevant subtask, and receives back a summary or result.

That framing is not just a tidy metaphor. In [VS Code Insiders Podcast Episode 19](https://www.vscodepodcast.com/19), Harald Kirschner describes the subagent as its own agent loop that starts fresh, works the delegated task, and then goes away after returning the result. That matches the official VS Code docs: subagents are useful when the parent agent needs focused research, parallel analysis, or specialized review without carrying every exploratory tool call in the main context.

That isolation is the point. The parent loop stays focused on the overall task while the child loop explores one branch deeply. In practice, this is how Copilot avoids polluting the main conversation with every intermediate search result, failed hypothesis, or exploratory read.

**See it in action:** [VS Code Insiders Podcast Episode 19](https://www.vscodepodcast.com/19) for the clearest explanation of context isolation, then [Subagents: Parallel Execution and Context Isolation](https://www.youtube.com/watch?v=GMAoTeD9siU&t=0s) to watch the same concepts on the official VS Code channel.

Use that mental model when deciding whether to ask for subagents. Reach for them when a task benefits from one of these patterns:

- Independent research before implementation
- Parallel analysis across multiple areas of the codebase
- Specialized review passes with different goals
- Narrow worker roles with different tool permissions or model preferences

On supported surfaces, subagent behavior is typically agent-initiated rather than directly user-invoked. The user describes the work. The main agent recognizes where isolation helps, starts a subagent, and continues once the delegated result comes back.

---

## Hooks: Enforcement at Action Boundaries

Hooks matter because they operate at the action boundaries of the loop rather than inside the model's reasoning. Instructions can tell Copilot not to do something. Hooks can inspect, log, deny, or reshape what happens when the loop crosses a lifecycle event or tries to execute a tool.

That makes hooks a different class of control:

- Instructions, prompts, skills, and agents influence reasoning.
- Hooks influence execution.

This is why hooks show up in security, compliance, and audit conversations. Once the loop can edit files, run commands, or call external systems, the question is no longer only "what should the model do?" It is also "what must happen if the model tries to do the wrong thing?"

---

## Model Selection Across the Loop

Users often think model selection is a single dropdown choice. In practice, the loop can involve more than one model decision. The parent conversation has a current model, but delegated work can also inherit that model or override it through custom-agent configuration or explicit subagent selection rules.

That is why two requests that look similar can behave differently. A planner agent might run with a deeper reasoning model and read-only tools. An implementation subagent might use a faster model and editing tools. A review subagent might use a narrower context and produce a different style of output even when the user prompt looks almost the same.

The practical rule is simple: treat the selected model as the default for the current conversation, not as a guarantee that every part of the workflow uses the exact same reasoning profile.

---

## Failure Modes Teams Actually Feel

Most teams do not need to memorize internal architecture. They do need to understand the failure modes the loop creates.

- **Context bloat** slows the loop down and makes decisions worse. Long sessions, noisy prompts, and too much irrelevant context reduce quality.
- **Weak task decomposition** causes the agent to thrash. If the next step is unclear, the loop wastes turns gathering the wrong evidence or retrying shallow actions.
- **Over-broad instructions** distort every turn. A bad global rule is worse than a missing local rule because it contaminates the entire session.
- **Missing guardrails** matter once tool use becomes real. If an action must never happen, instructions alone are not enough; use hooks, permissions, or infrastructure controls.
- **Poor tool hygiene** leads to bad orchestration. Giving the loop too many vague tools or unclear MCP capabilities makes it harder for the model to choose well.

These are not abstract problems. They are the practical reasons one repository feels "easy" in Copilot and another feels like the agent is fighting the team.

---

## Worked Example: Feature Request to Validated Result

Suppose the user asks: "Add a caching layer to the API and update the docs."

1. The loop starts with the user request, the current model, the active agent or prompt, and whatever instructions apply to the repository.
2. Copilot searches the codebase to understand how caching, data access, and API handlers are organized.
3. It reads the most relevant files, then decides whether the docs and implementation should stay in one flow or whether research should be delegated to a subagent.
4. If a subagent is useful, the parent loop delegates targeted research, receives the summary, and keeps the main context clean.
5. The implementation loop edits files, runs tests or validation, and reads the results.
6. Hooks, if configured, can inspect or block risky tool invocations during the run.
7. When the work converges, the loop stops and returns a final summary of what changed and what was validated.

That example matters because it looks like normal engineering work. The agent loop is not a theoretical diagram. It is the runtime pattern behind planning, research, implementation, testing, review, and reporting.

---

## Where to Read Next

- To understand the baseline platform, go back to [Part I: Foundations](part-1-foundations.md).
- To see how the primitives stack together inside the loop, read [How Primitives Layer Together](part-2-primitives.md#how-primitives-layer-together).
- To go deeper on delegated work, read [Primitive 5: Custom Agents](primitive-5-custom-agents.md).
- To go deeper on enforcement boundaries, read [Primitive 7: Hooks](primitive-7-hooks.md).