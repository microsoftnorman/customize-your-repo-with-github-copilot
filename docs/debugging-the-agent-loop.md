# Debugging the Agent Loop

[← Back to Guide](../README.md) | [← Tool Calling in Depth](tool-calling-in-depth.md) | [Next: Appendix: Diagnosing Loop Failures →](appendix-diagnosing-loop-failures.md)

*Updated: April 22, 2026.*

---

## Why This Chapter Exists

The agent loop is easy to describe in theory and harder to inspect in practice. Once teams start asking why a tool was chosen, why a subagent was launched, why the agent stopped early, or why context ballooned, they are no longer doing conceptual learning. They are debugging the runtime.

That is a later skill. It belongs after the loop model, the primitive chapters, and the cross-runtime material.

## Inspecting the Loop in Debug Views

The loop is inspectable in VS Code. For practical troubleshooting, the relevant surfaces are:

- `Developer: Show Chat Debug View`
- `Developer: Show Agent Debug Logs`

The official starting point is the VS Code documentation for [Agent Logs and the Chat Debug view](https://code.visualstudio.com/docs/copilot/chat/chat-debug-view). The broader [Chat overview](https://code.visualstudio.com/docs/copilot/chat/copilot-chat#_troubleshoot-chat-interactions) also points readers there in its troubleshooting section.

The debug infrastructure behind those views is visible in the open-source code.

- [`otelSpanToChatDebugEvent.ts`](https://github.com/microsoft/vscode-copilot-chat/blob/main/src/extension/trajectory/vscode-node/otelSpanToChatDebugEvent.ts#L275-L292) converts tracing spans into chat debug events, including subagent relationships.
- [`vscode.proposed.chatDebug.d.ts`](https://github.com/microsoft/vscode-copilot-chat/blob/main/src/extension/vscode.proposed.chatDebug.d.ts#L252-L287) defines debug event shapes such as subagent invocation events.
- [`toolsService.ts`](https://github.com/microsoft/vscode-copilot-chat/blob/main/src/extension/tools/vscode-node/toolsService.ts#L151-L179) records trace context so child invocations can be linked back to the parent session.

Those views are useful for different reasons:

- The Chat Debug View shows the live structure of the session: model turns, tool calls, subagent invocations, and high-level flow.
- The Agent Debug Logs show the lower-level trajectory data that explains why the loop took a particular path.

## What To Look For

Use the debug views when one of these questions appears:

- Why did the agent choose that tool?
- Why did it delegate to a subagent?
- Why did it stop early?
- Why did it gather so much context before editing?
- Why did a faster or smaller model appear in the session?

At that point, the useful unit of analysis is the trajectory. The question is not only whether the task succeeded. The question is what path the loop took, where it gathered context, where it delegated, where it retried, and where it accumulated waste.

## Example Debug Prompt

The easiest way to make the loop visible is to give it a task that forces context gathering, tool calls, edits, validation, and possibly delegation. A prompt like the following usually produces a useful debug trace:

```text
In this repository, add a new command called Copy Relative File Path. First inspect how existing commands are registered, how menu or palette contributions are wired, and how similar behavior is tested. Use subagents if helpful to explore those areas in parallel. Then implement the feature, update the narrowest relevant tests, run the smallest validation step that proves the change, and summarize which files changed and why.
```

That prompt is useful because it typically exercises several parts of the loop in one run:

- context assembly, because the agent has to identify the command-registration surface,
- task shaping, because it has to interpret both the feature request and the constraints,
- decision, because it must choose between search, read, edit, test, and delegation,
- action, because it must call tools and possibly subagents,
- feedback, because tool results and test results have to feed back into the next turn,
- stop-or-continue, because the agent has to decide whether the task is actually complete.

## Reading the Trace Like an Engineer

The fastest way to get value from these views is to read them in order:

1. Identify the turn where the session visibly changed direction.
2. Check what context had already been gathered before that turn.
3. Check which tools were available and which one was chosen.
4. Check whether a subagent boundary removed noise or just moved it.
5. Check whether the returned result actually improved the next decision.

That makes the debug views useful for more than incident response. They become a way to evaluate customization quality. A strong harness produces cleaner trajectories. A weak harness produces longer, noisier, more expensive ones.

## Turning Sessions into Better Customizations

This is one of the most practical uses of the debug surfaces.

Once a team has a successful or revealing session, it has raw material for better customizations. The goal is not to preserve the whole transcript. The goal is to extract the stable pattern from it.

Use a real session this way:

1. identify the turns that actually improved the trajectory,
2. separate stable guidance from one-off repository details,
3. decide which primitive the pattern belongs in,
4. then ask GitHub Copilot to turn that pattern into a reusable artifact and review the result.

The mapping is usually straightforward:

- repeated one-shot workflow becomes a Prompt,
- repeated role and posture becomes a Custom Agent,
- repeated default repository rule becomes an instruction file,
- repeated discoverable procedure becomes a Skill,
- repeated execution boundary becomes a Hook or tool restriction.

That is why trajectories matter even when they are messy. They show the difference between what the team thinks GitHub Copilot needs and what the runtime actually needed.

## Where to Read Next

- Return to [Measuring Success](measuring-success.md) to connect runtime quality back to rollout metrics.
- Use [Operational Reference](part-3-reference.md) when the question shifts from behavior to file paths, scopes, or support boundaries.
- Use [Appendix: Diagnosing Loop Failures](appendix-diagnosing-loop-failures.md) when the problem is no longer "what happened in the trace?" but "which loop stage actually failed?"