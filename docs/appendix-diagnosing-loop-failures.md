# Appendix: Diagnosing Loop Failures

[← Back to Guide](../README.md) | [← Debugging the Agent Loop](debugging-the-agent-loop.md)

*Updated: April 22, 2026.*

---

## Why This Appendix Exists

This is not the place to learn the loop for the first time. It is the place to diagnose a session after the basic loop model already makes sense.

That is why this material lives at the end of the guide. By this point, the reader should already understand context assembly, task shaping, tool calling, hooks, subagents, and the debug surfaces.

## Failure Modes That Feel Like Product Problems but Are Usually Loop Problems

When teams say "GitHub Copilot is being weird," the problem is often easier to locate in the loop than in the model.

The simplest way to read a bad session is to ask which step failed:

- **Context assembly failed**: the loop started with the wrong files, the wrong symbols, stale turns, or too much irrelevant context.
- **Task shaping failed**: the request was framed too loosely, the wrong agent or prompt posture was used, or the instructions did not constrain the job well enough.
- **Decision failed**: the model chose to answer too early, searched in the wrong place, or used a tool when it should have asked for more context.
- **Action failed**: the right step was chosen, but the tool could not run, the permissions were too narrow, the hook blocked execution, or the runtime could not reach the target system.
- **Feedback failed**: the tool returned noisy output, too much output, or low-signal output, so the next turn reasoned from weak evidence.
- **Stop conditions failed**: the loop kept going after it had enough evidence, or stopped before the task was actually resolved.

That is usually the real reason customization matters. The work is not only to improve answers. It is to make the loop take better steps.

The useful concept here is the agent trajectory, not just whether a task eventually succeeded. The question is not only "did the agent solve it?" The better question is "where did the loop become wasteful, confused, blocked, or overconfident?"

## How To Use This Appendix

Use this appendix when a session failed in a way that felt vague from the outside.

Do not start with broad complaints such as "the model is bad" or "the agent wandered." Start by placing the failure in one loop stage. Once that is clear, the next question becomes more concrete:

- Was the wrong context gathered?
- Was the task framed too loosely?
- Was the wrong tool chosen?
- Did the runtime fail to execute the chosen action?
- Did noisy results corrupt the next turn?
- Did the loop stop too early or continue too long?

That is the practical value of the loop model. It gives the team a way to diagnose trajectories without collapsing every failure into model quality.

## Where to Read Next

- Revisit [Debugging the Agent Loop](debugging-the-agent-loop.md) when you need to inspect a specific trajectory in the Chat Debug View or Agent Debug Logs.
- Use [Operational Reference](part-3-reference.md) when the question shifts from diagnosis to file paths, support boundaries, or configuration lookup.