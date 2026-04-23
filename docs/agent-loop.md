# The Agent Loop

[← Back to Guide](../README.md) | [← Why Customization Matters](why-customization-matters.md) | [Next: Primitives in Action →](primitives-in-action.md)

*Updated: April 23, 2026.*

---

## How the GitHub Copilot Harness Works

Think about a small team shipping a feature together. Nobody works alone. The tech lead frames the task. A developer searches the codebase. Someone else reads the relevant files and maps the constraints. Another person writes the code. A reviewer checks it. Along the way, each person hands evidence forward: "here are the files that matter," "this function owns that logic," "the test still passes." The work converges because every step is informed by the last.

The GitHub Copilot agent loop works the same way — except one runtime plays every role.

**See it in action:** [Inside The Agent Loop](https://www.youtube.com/watch?v=ENxVTtLW_Bc&t=0s) — A walkthrough of the agent loop as a runtime model of model calls, tools, context, and subagents.

The VS Code team calls the machinery around the model the **harness** — the prompts, context-gathering strategies, tools, and custom models that combine to make the agent loop actually produce good results. The harness is not the model. It is everything the team has built so the model can do useful work: dynamically assembled system prompts tuned per model, tool schemas, context strategies, and a 15–20 person team continuously optimizing the path the agent takes to solve a problem. When a new model ships, the harness is fresh. Within weeks, the team refines prompts, runs thousands of evaluation cases on their own benchmark, and tunes the trajectory — not just whether the task succeeded, but whether the agent took a good path to get there.

That harness is what a request enters when a developer hits Enter. It is a `while` loop. The system assembles the prompt. The model picks a tool or writes a response. The tool result comes back. The loop continues with better evidence. It keeps going until the task converges or is stopped.

That is the agent loop. It is not one giant opaque prompt. It is a sequence of model invocations, tool calls, and state updates — the same pattern a human team follows, compressed into a runtime. Once that clicks, the primitives stop looking like a pile of unrelated files and start reading as levers that change how the loop behaves.

Once that picture is clear, the primitives become easier to reason about:

- Always-on Instructions and File-based Instructions change what the loop sees.
- Prompts, Skills, and Custom Agents change how the loop is framed.
- MCP changes what the loop can reach.
- Hooks change what the loop is allowed to do at execution time.
- Memory changes what the loop already knows before it starts asking questions.

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

## A Session from Start to Finish

The demo transcripts in this repo show the same shape every time. See [Your first agent session in action](../references/transcripts/code-channel/2026-04-06-your-first-agent-session-in-action.md), [DEMO - Build your first app with agent mode](../references/transcripts/code-channel/2026-04-06-demo-build-your-first-app-with-agent-mode.md), and [Inside The Agent Loop](../references/transcripts/code-channel/2026-04-20-inside-the-agent-loop-with-pierce-boggan.md).

The user types a product-level goal — not a list of files to create:

> 💬 **Try this prompt:**
> "Build a URL shortener with a simple frontend."

The system assembles the first turn: conversation history, open files, terminal state, repository instructions, and the full set of tools the model may call. That assembled turn is the starting context, and it already includes every customization layer that applies.

The model's first move is almost never "write the answer." It searches for existing code, reads candidate files, and checks constraints. Those tool results flow back into the conversation as new evidence, so the next decision is grounded in the actual codebase rather than assumptions. The session narrows: this file owns the route, that one owns the styles, this command confirms the change works.

Once the model has enough signal, it acts — creating files, wiring pieces together, running verification commands. The visible answer the user sees is the last step, not the first. It is the product of several smaller turns that each added evidence and removed ambiguity.

That is what the loop looks like in practice. Not a single burst, but a session that keeps improving its own footing.

## See the Full Prompt Yourself

The assembled prompt is not a secret. VS Code exposes the exact payload sent to the model on every turn, including the system prompt, user prompt, attached context, and tool definitions.

To see it, open the **Chat Debug view**: select the `...` menu in the Chat view and choose **Show Chat Debug View**, or run `Developer: Show Chat Debug View` from the Command Palette. Each turn expands into sections for the system prompt, user prompt, context, response, and tool responses. That is the raw request — every instruction, every tool schema, every piece of context the model received.

For a chronological event log that also shows tool call sequences, token usage, and prompt-file discovery, open the **Agent Debug Log panel**: enable `github.copilot.chat.agentDebugLog.fileLogging.enabled`, then select `...` → **Show Agent Debug Logs** in the Chat view. The Logs view shows each event in order; the Agent Flow Chart view visualizes how subagents branched and returned.

Both views are documented at [Debug chat interactions](https://code.visualstudio.com/docs/copilot/chat/chat-debug-view).

## What the Assembled Prompt Looks Like

The Chat Debug view shows what the model actually receives. Here is a simplified example of a single turn's assembled prompt for a repository that uses several customization layers. The real payload is longer, but the structure is the same.

```text
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

Every customization primitive shows up somewhere in that payload. Always-on instructions set the baseline. File-based instructions add path-specific rules. The custom agent changes the persona and behavior. MCP tools extend what the model can reach. The conversation history carries forward evidence from earlier turns. And the user prompt at the bottom is the specific task for this turn.

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

The parent loop delegates a focused task, the child loop starts with narrower context, and the child returns a result instead of replaying every intermediate search and read back into the parent session.

The local source material is clear about why this matters. [Subagents: Parallel Execution and Context Isolation](../references/transcripts/code-channel/2026-02-09-subagents-parallel-execution-and-context-isolation.md) and [Inside The Agent Loop](../references/transcripts/code-channel/2026-04-20-inside-the-agent-loop-with-pierce-boggan.md) both frame subagents as isolated nested loops that gather context or do focused work without bloating the parent thread. Isolation is not an implementation detail. It is the reason the parent loop stays usable.

Use that model when the task benefits from:

- independent research,
- parallel exploration,
- specialized review,
- or different permissions and models for different branches of the same job.

## Hooks Change the Control Model

Most primitives guide reasoning. Hooks govern execution.

That difference is easy to miss until the agent is doing real work.

Instructions can say "do not print secrets". A hook can block the command that would print them. Instructions can say "avoid dangerous shell commands". A hook can inspect the invocation and deny it. That is why hooks belong in the loop chapter and not only in a later security appendix.

## Where to Read Next

- Read [Primitives in Action](primitives-in-action.md) next to see three end-to-end workflows built on this loop.
- Then use [The Eight Primitives](part-2-primitives.md) as the decision bridge into the individual chapters.
