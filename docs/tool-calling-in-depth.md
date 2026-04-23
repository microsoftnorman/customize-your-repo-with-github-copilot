# Tool Calling in Depth

[← Back to Guide](../README.md) | [← Where GitHub Copilot Runs](where-github-copilot-runs.md) | [Next: Debugging the Agent Loop →](debugging-the-agent-loop.md)

*Updated: April 22, 2026.*

---

## Why This Chapter Exists

The agent loop explains where decisions happen. Tool calling explains how those decisions become action.

Without tools, the model can only produce text. With tools, the runtime can read files, search the workspace, run commands, fetch web content, call external systems, or delegate work to subagents. That makes tool calling one of the main boundaries between a chat response and an agentic workflow.

The official VS Code docs describe this in two complementary ways. [Tools](https://code.visualstudio.com/docs/copilot/concepts/tools) explains the conceptual model: tools are the mechanism that lets the model act on the development environment. [Use tools with agents](https://code.visualstudio.com/docs/copilot/agents/agent-tools) explains the operational model: how tools are enabled, chosen, approved, and surfaced in chat.

## The Three Tool Types

VS Code supports three tool families:

- built-in tools that ship with VS Code,
- MCP tools provided by Model Context Protocol servers,
- and extension tools contributed by extensions through the Language Model Tools API.

That distinction matters because not all tool reach comes from the same layer. Some capability is built into the editor. Some is added by the repository or user through MCP. Some comes from extension-specific integrations.

## How Tool Calling Fits the Loop

Tool calling crosses four parts of the loop:

1. tool availability is determined,
2. the model chooses whether to call a tool,
3. the runtime executes or approves that call,
4. the result is fed back into the next turn.

The open-source code reflects that split.

- [`getAgentTools()` in `agentIntent.ts`](https://github.com/microsoft/vscode-copilot-chat/blob/main/src/extension/intents/node/agentIntent.ts#L65-L121) determines which tools are available for the current agent and model combination.
- [`languageModelToolsService.ts`](https://github.com/microsoft/vscode/blob/main/src/vs/workbench/contrib/chat/common/tools/languageModelToolsService.ts#L611-L637) shows the schema layer that defines how tools are exposed to the model.
- [`runOne()` in `toolCallingLoop.ts`](https://github.com/microsoft/vscode-copilot-chat/blob/main/src/extension/intents/node/toolCallingLoop.ts#L1276-L1289) is where a chosen tool call moves into execution.
- [`toolCalling.tsx`](https://github.com/microsoft/vscode-copilot-chat/blob/main/src/extension/prompts/node/panel/toolCalling.tsx#L247-L282) shows the tool rendering and execution path on the prompt side.
- [`toolCallingLoop.ts`](https://github.com/microsoft/vscode-copilot-chat/blob/main/src/extension/intents/node/toolCallingLoop.ts#L1443-L1469) is also where tool results are reintroduced into the next request.

That is the main mental model to keep: a tool is not just an API the model happens to know about. It is a structured capability the runtime exposes, gates, executes, and then converts back into context.

## Choosing a Tool Versus Writing Text

The core decision is simple: should the model respond directly, or should it call a tool first?

The official docs say this at the product level: when using agents, the agent automatically determines which tools to use from the enabled set based on the prompt and context. The source code shows the surrounding structure, even though the model's internal reasoning is not open-source.

The model is deciding inside a constrained menu. That menu is shaped by:

- the enabled tools,
- the selected agent or custom agent,
- prompt-file or agent-level tool restrictions,
- model-specific filtering,
- and the current state of the task.

This is why tool count matters. The official [Tools](https://code.visualstudio.com/docs/copilot/concepts/tools#_control-which-tools-are-available) page makes the product case clearly: fewer tools can preserve context, improve relevance, and reduce decision space. In practice, too many tools increase the odds of wasted calls and noisy trajectories.

## Tool Availability Is Part of Prompt Design

Tool availability is not a separate concern from prompting. It is one of the strongest prompt-shaping controls in the system.

The official [Use tools with agents](https://code.visualstudio.com/docs/copilot/agents/agent-tools#_enable-tools-for-chat) docs cover three main ways to control that availability:

- enable or disable tools in the tools picker for the current request,
- reference a specific tool explicitly with `#tool`,
- restrict the tool set through prompt files, custom agents, or tool sets.

That means the real question is not only “what did the user ask?” The question is also “what action surface was the model allowed to see?”

## Approvals, Trust, and Why Tool Calling Is a Security Boundary

Tools are not only a productivity feature. They are one of the main trust boundaries in the runtime.

The official docs split that boundary into several controls:

- approval prompts for tools with side effects,
- URL request and response approval for web access,
- permission levels such as Default Approvals, Bypass Approvals, and Autopilot,
- and per-tool or per-source approval management.

That is why tool calling cannot be treated as a neutral plumbing detail. The moment the loop can write files, run commands, or fetch external content, tool calling becomes part of the system's risk model.

Hooks are one layer of that boundary. [`chatHookService.ts`](https://github.com/microsoft/vscode-copilot-chat/blob/main/src/platform/chat/common/chatHookService.ts#L73-L103) defines the interface for pre-tool and post-tool interception, which is why [Hooks](primitive-7-hooks.md) matter so much for real execution control.

## Tool Results Become New Context

Tool calling does not end when the runtime gets an answer back. The result has to be turned into something the next turn can use.

That is why tool calling belongs inside the loop instead of beside it. Each call produces output that consumes context budget and changes the next decision. A clean tool result can reduce uncertainty. A noisy tool result can poison the next turn.

This is also where subagent calls matter. A subagent is still a tool call at the parent level, but its returned value is intentionally compressed compared with the internal work the child loop performed.

## Subagents Are Tool Calls with Different Semantics

The built-in delegation tool in [`runSubagentTool.ts`](https://github.com/microsoft/vscode/blob/main/src/vs/workbench/contrib/chat/common/tools/builtinTools/runSubagentTool.ts#L97-L151) is useful because it makes the boundary explicit.

A normal tool call usually returns data or performs one action. A subagent call launches a child loop, accumulates its own context, and returns a synthesized result to the parent.

That makes subagents part of tool calling, but not just another utility tool. They are tool-driven delegation.

## Tool Calling Failure Modes

Most tool-calling failures look like model failures from the outside. They usually are not.

The common causes are narrower:

- the wrong tools were available,
- too many tools were available,
- approvals blocked the useful path,
- a tool returned noisy or low-signal output,
- the call happened too early,
- or the result consumed context without improving the next decision.

That is why a tool-calling chapter belongs after the loop and the primitives. The reader needs the system model first. Then tool calling makes sense as a controlled action layer inside that system.

## Where to Read Next

- Read [Debugging the Agent Loop](debugging-the-agent-loop.md) next to inspect how tool calls, subagents, and returned results show up in real trajectories.
- Use [Primitive 6: MCP](primitive-6-mcp.md) and [Primitive 7: Hooks](primitive-7-hooks.md) when the question shifts from generic tool mechanics to external reach or execution control.