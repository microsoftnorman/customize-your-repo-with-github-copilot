# GitHub Copilot in VS Code

[← Back to Foundations](../part-1-foundations.md)

---

[GitHub Copilot](https://github.com/features/copilot) has been **built in** to VS Code since version 1.116. Current stable is 1.117 (April 22, 2026). No extension installation is required. New users get [chat](https://code.visualstudio.com/docs/copilot/chat/copilot-chat), [inline suggestions](https://code.visualstudio.com/docs/copilot/ai-powered-suggestions), and [agent mode](https://code.visualstudio.com/docs/copilot/agents/overview) out of the box. Those who prefer not to use AI features can disable them with `chat.disableAIFeatures`.

**Official docs:** [Copilot in VS Code](https://code.visualstudio.com/docs/copilot) · [Customization overview](https://code.visualstudio.com/docs/copilot/customization/overview) · [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=vscode)

## Why VS Code

All eight primitives work in VS Code, along with both platform extensions (Agentic Workflows and Copilot SDK), plus features not yet available on other surfaces:

- **[Agent plugins](https://code.visualstudio.com/docs/copilot/customization/agent-plugins):** install bundled customizations (skills, agents, hooks, MCP) from marketplaces.
- **Agent-scoped hooks.** Attach hooks to specific custom agents via `.agent.md` frontmatter.
- **Nested sub-agents.** Sub-agents can invoke other sub-agents (max depth 5).
- **[Chat Customizations editor](https://code.visualstudio.com/docs/copilot/customization/overview):** manage all instructions, agents, skills, and plugins from one interface.
- **VS Code Agents app** (preview): a dedicated companion app for working with long-running agent sessions.
- **BYOK for Copilot Business and Enterprise.** VS Code 1.117 lets those plans use approved provider keys in chat and agent flows. It applies to chat, not inline completions.

This guide uses VS Code for examples and screenshots. Where a feature is VS Code-specific, it is noted.

**See it in action:** [A Unified Agent Experience](https://www.youtube.com/watch?v=YmpjvZ3xkx8&t=145s) — VS Code Team demos the target picker, local agent mode, and plan mode working together inside VS Code.

VS Code is also the best first authoring surface for shared repository assets. Teams can generate, inspect, and debug instructions, prompts, skills, and agents here before validating how those same files behave on JetBrains, Visual Studio, Xcode, or the cloud agent.

Treat preview features carefully. The Chat Customizations editor and the Agents app are still preview workflows. They are useful for pilots, but they should not become the enterprise baseline until the team is comfortable supporting stable and Insiders separately.

**Code to study:** [VS Code source](https://github.com/microsoft/vscode) and [VS Code Copilot Chat source](https://github.com/microsoft/vscode-copilot-chat)

**See it in action:** [Customize your agents](https://www.youtube.com/watch?v=flpKLkZla2Q&t=578s). Courtney Webster walks through the VS Code authoring flow for custom agents and related repo-level customizations.

## Primitive Support

| Primitive | Support |
|-----------|---------|
| Always-on Instructions | ✅ Supported |
| File-based Instructions | ✅ Supported |
| Prompts | ✅ Supported |
| Skills | ✅ Supported |
| Custom Agents | ✅ Supported |
| MCP | ✅ Supported |
| Hooks | ✅ Supported |
| Memory | Not in VS Code Chat or Inline Chat. See [Copilot Memory](../primitive-8-memory.md) for the surfaces where Memory is currently used. |

## 1.117 Highlights (April 22, 2026)

The current stable release adds a few customization-relevant changes on top of the 1.116 built-in milestone:

- **BYOK for Copilot Business and Enterprise.** Organizations can allow approved provider keys from GitHub policy settings. Usage is billed by the chosen provider and does not consume GitHub Copilot request quota.
- **System notifications for background terminal commands.** Long-running agent tasks are easier to supervise without living in the terminal panel.
- **Agent session sorting.** The Agent Sessions view now sorts by recent activity, which matters once teams start running many concurrent sessions.
- **Visual Studio Code Agents app remains Insiders-only.** It continues to improve, but it is still a preview companion app rather than the stable default workflow.

For the full list, see the [VS Code 1.117 release notes](https://code.visualstudio.com/updates/v1_117).

## Release Cadence

VS Code moved to **weekly stable releases** starting with v1.111 (March 2026). New Copilot features ship as soon as they're ready rather than waiting for a monthly window.

Track releases at [code.visualstudio.com/updates](https://code.visualstudio.com/updates/).

## Getting Started

With VS Code 1.116+, Copilot is available immediately. Sign in with your GitHub account and start using [Chat](https://code.visualstudio.com/docs/copilot/chat/copilot-chat), [inline suggestions](https://code.visualstudio.com/docs/copilot/ai-powered-suggestions), and [agent mode](https://code.visualstudio.com/docs/copilot/agents/overview). For older versions, install the [GitHub Copilot extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) from the VS Code Marketplace.

For a team rollout, the practical first move is simple: create the repository assets here, validate them in stable VS Code, and treat Insiders-only features as optional pilots until the policy, support, and training story is clear.

## Further Reading

- [VS Code Copilot documentation](https://code.visualstudio.com/docs/copilot)
- [Customization overview](https://code.visualstudio.com/docs/copilot/customization/overview)
- [Agent plugins](https://code.visualstudio.com/docs/copilot/customization/agent-plugins)
- [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)

---

[← Back to Foundations](../part-1-foundations.md)
