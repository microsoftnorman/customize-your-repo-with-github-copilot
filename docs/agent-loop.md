# The Agent Loop

[← Back to Guide](../README.md) | [← Why Customization Matters](why-customization-matters.md) | [Next: Primitives in Action →](primitives-in-action.md)

*Updated: April 23, 2026.*

---

## How the GitHub Copilot Harness Works

Think about a small team shipping a feature together. Nobody works alone. The tech lead frames the task. A developer searches the codebase. Someone else reads the relevant files and maps the constraints. Another person writes the code. A reviewer checks it. Along the way, each person hands evidence forward: "here are the files that matter," "this function owns that logic," "the test still passes." The work converges because every step is informed by the last.

The GitHub Copilot agent loop works the same way — except one runtime plays every role.

**See it in action:** [Inside The Agent Loop](https://www.youtube.com/watch?v=ENxVTtLW_Bc&t=0s) — A walkthrough of the agent loop as a runtime model of model calls, tools, context, and subagents. Local transcripts of that talk and related demos are in this repo: [Inside The Agent Loop](../references/transcripts/code-channel/2026-04-20-inside-the-agent-loop-with-pierce-boggan.md), [Your first agent session in action](../references/transcripts/code-channel/2026-04-06-your-first-agent-session-in-action.md), and [DEMO - Build your first app with agent mode](../references/transcripts/code-channel/2026-04-06-demo-build-your-first-app-with-agent-mode.md).

The VS Code team calls the machinery around the model the **harness** — the prompts, context-gathering strategies, tools, and custom models that combine to make the agent loop actually produce good results. The harness is not the model. It is everything the team has built so the model can do useful work: dynamically assembled system prompts tuned per model, tool schemas, context strategies, and a 15–20 person team continuously optimizing the path the agent takes to solve a problem. When a new model ships, the harness is fresh. Within weeks, the team refines prompts, runs thousands of evaluation cases on their own benchmark, and tunes the trajectory — not just whether the task succeeded, but whether the agent took a good path to get there.

The results of that optimization are measurable. As of April 2026, the VS Code harness achieves roughly 90% code acceptance with Claude Opus 4.6 — up from around 52–53% when the team first started working on the harness a year earlier. That gap is not the model improving alone. It is the harness improving: better prompts, better tool design, better context strategies, and purpose-built custom models behind the scenes for tasks like code retrieval. The benchmark the team uses is not SWE-bench — they built their own, with custom problems, specifically to avoid the data pollution issues that affect public benchmarks.

That acceptance rate also explains why the harness does not use the most expensive model for every call. Generating a chat session title, renaming a symbol, or running a focused subagent search does not need a frontier model. Those tasks route to faster, cheaper models — Haiku, a mini variant, or a purpose-built retrieval model — because the benchmarks show they perform well enough for the job and free up capacity and latency budget for the turns that actually need deep reasoning.

That harness is what a request enters when a developer hits Enter. It is a `while` loop. The system assembles the prompt. The model picks a tool or writes a response. The tool result comes back. The loop continues with better evidence. It keeps going until the task converges or is stopped.

That is the agent loop. It is not one giant opaque prompt. It is a sequence of model invocations, tool calls, and state updates — the same pattern a human team follows, compressed into a runtime. Once that clicks, the primitives stop looking like a pile of unrelated files and start reading as levers that change how the loop behaves.

Once that picture is clear, the primitives become easier to reason about:

- [Always-on Instructions](primitive-1-always-on-instructions.md) and [File-based Instructions](primitive-2-file-based-instructions.md) change what the loop sees.
- [Prompts](primitive-3-prompts.md), [Skills](primitive-4-skills.md), and [Custom Agents](primitive-5-custom-agents.md) change how the loop is framed.
- [MCP](primitive-6-mcp.md) changes what the loop can reach.
- [Hooks](primitive-7-hooks.md) change what the loop is allowed to do at execution time.
- [Memory](primitive-8-memory.md) changes what the loop already knows before it starts asking questions.

## The Easiest Mental Model: A Working Conversation

The agent loop is easier to understand when it stops sounding like a black box. It is not one brilliant answer appearing all at once. It is a working conversation between four things:

- the user,
- the model,
- the available tools,
- and the accumulating evidence from the repo, terminal, and previous turns.

Think about a simple request:

> 💬 **Try this prompt:**
> "Add a loading state to the checkout button and keep the existing styles."

First, the request enters the loop. GitHub Copilot does not start by editing code. It starts by assembling the best possible picture of the task: the conversation so far, the file in view, nearby context, applicable instructions, and the tools it can use.

Then the model looks at that picture and makes a small decision. Usually the first decision is not "write the answer." It is "get better evidence." That might mean searching for the checkout button, reading the component that renders it, or checking where the submit state already lives.

Next, the tools return something concrete: filenames, code, props, styles, and call sites. Now the loop has more than a request. It has evidence.

Then the model gets another turn. With better evidence, it can make a better choice. Maybe it reads one more file. Maybe it now has enough confidence to place the edit. Maybe it realizes the task is ambiguous and asks a clarifying question instead.

Finally, once the loop has enough context and the action succeeds, it stops. The response back to the user is the last step, not the first. The visible answer is the result of several smaller turns: gather context, choose a move, inspect the result, choose the next move, and only then conclude.

That is the science of it. First the system frames the turn. Then it gathers evidence. Then it acts. Then it checks what came back. Then it either continues or stops. Once that clicks, the runtime stops feeling mystical and starts feeling inspectable.

This also demystifies what people call "hallucination." The model is not lying. It is making the best guess it can from whatever evidence it has at that moment — the same way a new team member might confidently suggest the wrong file if nobody showed them the actual project structure first. When the loop has thin context, the model fills gaps with plausible-sounding assumptions. When the loop has strong context — good instructions, the right files read, relevant tool results — those assumptions get replaced by evidence, and the guesses get dramatically better. Most hallucination problems are not intelligence problems. They are context problems.

## See the Full Prompt Yourself

The assembled prompt is not a secret. VS Code exposes the exact payload sent to the model on every turn, including the system prompt, user prompt, attached context, and tool definitions.

To see it, open the **Chat Debug view**: select the `...` menu in the Chat view and choose **Show Chat Debug View**, or run `Developer: Show Chat Debug View` from the Command Palette. Each turn expands into sections for the system prompt, user prompt, context, response, and tool responses. That is the raw request — every instruction, every tool schema, every piece of context the model received.

For a chronological event log that also shows tool call sequences, token usage, and prompt-file discovery, open the **Agent Debug Log panel**: enable `github.copilot.chat.agentDebugLog.fileLogging.enabled`, then select `...` → **Show Agent Debug Logs** in the Chat view. The Logs view shows each event in order; the Agent Flow Chart view visualizes how subagents branched and returned.

Both views are documented at [Debug chat interactions](https://code.visualstudio.com/docs/copilot/chat/chat-debug-view).

## What the Assembled Prompt Looks Like

The Chat Debug view shows what the model actually receives. Here is a simplified example of a single turn's assembled prompt for a repository that uses several customization layers. The real payload is longer, but the structure is the same.

```text
── Model ──────────────────────────────────────────────────────

Claude Opus 4.6 (copilot)

── System Prompt ──────────────────────────────────────────────

You are a helpful AI assistant integrated into VS Code.
Follow the user's instructions carefully.

── Always-on Instructions (.github/copilot-instructions.md) ──

# Project: Acme API
- Language: TypeScript, strict mode
- Framework: Express 5 with Zod validation
- Tests: Vitest, co-located in __tests__/ directories
- Style: functional patterns, no classes, prefer const
- Never use moment.js or lodash — use native equivalents

── File-based Instructions (api-routes.instructions.md) ──────

When editing files matching src/routes/**:
- Every route must validate input with a Zod schema
- Return RFC 7807 problem details on errors
- Include an OpenAPI JSDoc comment above each handler

── Custom Agent (security-reviewer.agent.md) ──────────────────

You are a security reviewer. Focus on OWASP Top 10.
Start every review with a risk assessment.
Do not suggest fixes until the full review is complete.

── Available Tools ────────────────────────────────────────────

search        - Search for files or symbols in the workspace
readFile      - Read file contents
editFile      - Apply edits to a file
runTerminal   - Execute a shell command
runSubagent   - Delegate a task to an isolated subagent
mcp_postgres  - Query the project's Postgres database (MCP)

── Conversation History ───────────────────────────────────────

[user]  Review the /checkout route for security issues.

[assistant]  I'll start by reading the route handler and its
             Zod schema, then check the database queries.

[tool: readFile]  src/routes/checkout.ts  →  (file contents)
[tool: readFile]  src/schemas/checkout.ts →  (file contents)

── Current User Prompt ────────────────────────────────────────

Now check whether the discount code parameter is sanitized
before it reaches the database query.
```

Every customization primitive shows up somewhere in that payload. The model line at the top determines which language model reasons over everything below it — and the system prompt is dynamically tuned for that specific model. Always-on instructions set the baseline. File-based instructions add path-specific rules. The custom agent changes the persona and behavior. MCP tools extend what the model can reach. The conversation history carries forward evidence from earlier turns. And the user prompt at the bottom is the specific task for this turn.

The model choice ripples through the entire session. Different models get different system prompts, and subagents may run on a different model entirely. The harness section above explains why: not every turn needs the same reasoning depth, and the benchmarks back that up.

That is the prompt the model reasons over. Every turn rebuilds it with the latest evidence, which is why each decision is better informed than the last.

## One Turn Through the Loop

| Step | What Happens | What Can Change It |
|------|---------------|--------------------|
| **1. Context assembly** | The surface, model, conversation state, relevant files, terminal state, and other high-signal inputs are assembled. | Instructions, agents, active task framing |
| **2. Task shaping** | The model sees the request through whatever customization layers apply. | Prompts, Skills, Custom Agents, matching instructions |
| **3. Decision** | The model decides whether to answer, read more, call a tool, or delegate work. | Skill descriptions, tool availability, agent posture |
| **4. Action** | A tool runs, a file is read, a command executes, or a subagent is launched. | MCP, surface capabilities, permissions, hooks |
| **5. Feedback** | Tool results come back into the model as fresh evidence. | Result quality, context size, validation signals |
| **6. Stop or continue** | The loop ends with an answer or continues with another step. | The task, the evidence, and any blocking controls |

The runtime is iterative by design. It is not one giant hidden prompt. It is a chain of smaller decisions connected by evidence.

Another way to say it: the model is not solving the whole task in one leap. It is repeatedly choosing the next move that is justified by the evidence it has right now.

## Where the Primitives Enter

| Primitive | Primary Effect on the Loop |
|-----------|----------------------------|
| **[Always-on Instructions](primitive-1-always-on-instructions.md)** | Establish base rules on every turn |
| **[File-based Instructions](primitive-2-file-based-instructions.md)** | Add scoped rules only when matching files are relevant |
| **[Prompts](primitive-3-prompts.md)** | Frame a specific task and often constrain tool use |
| **[Skills](primitive-4-skills.md)** | Inject reusable procedure when intent matches |
| **[Custom Agents](primitive-5-custom-agents.md)** | Change role, toolset, and behavior across a conversation or delegated task |
| **[MCP](primitive-6-mcp.md)** | Expand the loop beyond the local workspace |
| **[Hooks](primitive-7-hooks.md)** | Intercept lifecycle boundaries outside the model |
| **[Memory](primitive-8-memory.md)** | Contribute repository knowledge learned over time |

That breakdown is the reason this guide teaches composition early. A team almost never has a problem that is solved by one isolated file type in the abstract. It has a problem somewhere in this loop.

## Subagents Make the Loop Fractal

A subagent is not a side conversation. It is another loop.

The parent loop delegates a focused task, the child loop starts with narrower context, and the child returns a result instead of replaying every intermediate search and read back into the parent session.

The local source material is clear about why this matters. [Subagents: Parallel Execution and Context Isolation](../references/transcripts/code-channel/2026-02-09-subagents-parallel-execution-and-context-isolation.md) and [Inside The Agent Loop](../references/transcripts/code-channel/2026-04-20-inside-the-agent-loop-with-pierce-boggan.md) both frame subagents as isolated nested loops that gather context or do focused work without bloating the parent thread. Isolation is not an implementation detail. It is the reason the parent loop stays usable.

Use that model when the task benefits from:

- independent research,
- parallel exploration,
- specialized review,
- or different permissions and models for different branches of the same job.

## Context Grows — and That Changes Everything

Every turn adds to the conversation: the user prompt, the system prompt, tool calls, tool results, and the model's own responses. That accumulation is the context window, and it is finite.

Early in a session, the context is small and focused. The model's decisions are fast and sharp. As the session progresses — more searches, more file reads, more edits — the context fills up. Each new turn costs more tokens, and the model has more text to reason over. Eventually the context approaches its limit.

When that happens, the harness has to **compact** the conversation: summarize older turns to free space for new ones. Compaction works, but it loses fidelity. Details from earlier turns get compressed into summaries, and the model may lose track of constraints or decisions that mattered.

That is exactly why subagents exist as a strategy. Instead of doing all exploratory work in the main loop — reading dozens of files, running searches, checking constraints — the main loop delegates that work to a subagent. The subagent uses its own isolated context window, does the research, and returns only a summary. The main loop stays fresh. It never saw the intermediate searches, so it never has to compact them away.

The practical takeaway: if a session starts drifting or the agent seems to forget earlier decisions, the context window is probably full and compaction is losing important details. The fix is not "try harder." It is decompose the task so the main loop stays focused and let subagents carry the exploratory weight.

That said, as of April 2026, context limits are far less of a daily concern than they were a year ago. Models ship with much larger context windows, the harness is smarter about what it includes, and subagent delegation handles most of the heavy lifting automatically. Most developers will never hit the wall. This section exists so that when a long session does start to drift, the explanation makes sense instead of feeling like a mystery.

## Hooks Change the Control Model

Most primitives guide reasoning. Hooks govern execution.

That difference is easy to miss until the agent is doing real work.

Instructions can say "do not print secrets". A hook can block the command that would print them. Instructions can say "avoid dangerous shell commands". A hook can inspect the invocation and deny it. That is why hooks belong in the loop chapter and not only in a later security appendix.

## Where to Read Next

- Read [Primitives in Action](primitives-in-action.md) next to see three end-to-end workflows built on this loop.
- Then use [The Eight Primitives](part-2-primitives.md) as the decision bridge into the individual chapters.
