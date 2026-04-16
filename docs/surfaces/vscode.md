# GitHub Copilot in VS Code

[← Back to Foundations](../part-1-foundations.md)

---

[GitHub Copilot](https://github.com/features/copilot) is **built-in** to VS Code as of version 1.116 (April 2026) — no extension installation required. New users get [chat](https://code.visualstudio.com/docs/copilot/chat/copilot-chat), [inline suggestions](https://code.visualstudio.com/docs/copilot/ai-powered-suggestions), and [agent mode](https://code.visualstudio.com/docs/copilot/agents/overview) out of the box. Those who prefer not to use AI features can disable them with `chat.disableAIFeatures`.

## Why VS Code

VS Code has the most complete Copilot customization support. All eight primitives work here — along with both platform extensions (Agentic Workflows and Copilot SDK) — plus features not yet available on other surfaces:

- **[Agent plugins](https://code.visualstudio.com/docs/copilot/customization/agent-plugins)** — install bundled customizations (skills + agents + hooks + MCP) from marketplaces
- **Agent-scoped hooks** — attach hooks to specific custom agents via `.agent.md` frontmatter
- **Nested sub-agents** — sub-agents can invoke other sub-agents (max depth 5)
- **[Chat Customizations editor](https://code.visualstudio.com/docs/copilot/customization/overview)** — manage all instructions, agents, skills, and plugins from one unified interface
- **VS Code Agents app** (preview) — a dedicated companion app built for agent-native development

This guide uses VS Code for examples and screenshots because it has the most complete primitive support. Where a feature is VS Code-specific, it is noted.

**See it in action:** [Customize Your Agents](https://www.youtube.com/watch?v=tAezuMSJuFs&t=10598s) — Courtney Webster walks through authoring custom agents, skills, instructions, and prompts from the VS Code Chat Customizations editor.

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
| Memory | ✅ Supported (via cloud agent) |

## 1.116 Highlights (April 2026)

The April 2026 release is the first where Copilot is fully built-in. A few customization-relevant additions:

- **Chat Customizations welcome page.** A single entry point (gear icon in the Chat view, or `Chat: Open Chat Customizations`) lists every instruction file, prompt, skill, agent, hook, and MCP server active in the workspace, and surfaces the authoring flows for each.
- **Customize Your Agent (natural-language generator).** Describe an agent in plain English and VS Code generates a draft [`.agent.md`](https://code.visualstudio.com/docs/copilot/customization/custom-agents) — complementary to `/create-agent`. See [Custom Agents → Authoring Paths in VS Code](../primitive-5-custom-agents.md#authoring-paths-in-vs-code).
- **JS/TS Chat Features skill bundle.** A built-in skill bundle for JavaScript and TypeScript workspaces, toggleable with `jsts-chat-features.skills.enabled`. Ships language-aware behaviors (test scaffolding, import fixing, type narrowing) without a plugin install.
- **Foreground terminal tool support.** Agent-invoked terminal commands can run in the foreground terminal the user is looking at, making long-running tasks easier to monitor and interrupt.
- **Tool confirmation carousel.** When an agent queues multiple tool calls, confirmations are grouped into a carousel so you can approve, deny, or edit them as a batch instead of one at a time.
- **Background terminal notifications on by default.** When a backgrounded terminal command finishes or needs input, the editor surfaces a notification — no more silently-completed agent runs.

For the full list, see the [VS Code 1.116 release notes](https://code.visualstudio.com/updates/).

## Release Cadence

VS Code moved to **weekly stable releases** starting with v1.111 (March 2026), driven by the rapid pace of AI development. New Copilot features ship as soon as they're ready rather than waiting for a monthly window.

Track releases at [code.visualstudio.com/updates](https://code.visualstudio.com/updates/).

## Getting Started

With VS Code 1.116+, Copilot is available immediately — no separate extension needed. Sign in with your GitHub account and start using [Chat](https://code.visualstudio.com/docs/copilot/chat/copilot-chat), [inline suggestions](https://code.visualstudio.com/docs/copilot/ai-powered-suggestions), and [agent mode](https://code.visualstudio.com/docs/copilot/agents/overview). For older versions, install the [GitHub Copilot extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) from the VS Code Marketplace.

## Further Reading

- [VS Code Copilot documentation](https://code.visualstudio.com/docs/copilot)
- [Customization overview](https://code.visualstudio.com/docs/copilot/customization/overview)
- [Agent plugins](https://code.visualstudio.com/docs/copilot/customization/agent-plugins)
- [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)

---

[← Back to Foundations](../part-1-foundations.md)
