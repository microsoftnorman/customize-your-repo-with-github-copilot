# GitHub Copilot in VS Code

[← Back to Foundations](../part-1-foundations.md)

---

[GitHub Copilot](https://github.com/features/copilot) is **built-in** to VS Code as of version 1.116 (April 2026) — no extension installation required. New users get chat, inline suggestions, and agent mode out of the box. Those who prefer not to use AI features can disable them with `chat.disableAIFeatures`.

## Why VS Code

VS Code has the most complete Copilot customization support. All ten primitives work here, plus features not yet available on other surfaces:

- **Agent plugins** — install bundled customizations (skills + agents + hooks + MCP) from marketplaces
- **Agent-scoped hooks** — attach hooks to specific custom agents via `.agent.md` frontmatter
- **Nested sub-agents** — sub-agents can invoke other sub-agents (max depth 5)
- **Chat Customizations editor** — manage all instructions, agents, skills, and plugins from one unified interface
- **VS Code Agents app** (preview) — a dedicated companion app built for agent-native development

This guide uses VS Code for examples and screenshots because it has the most complete primitive support. Where a feature is VS Code-specific, it is noted.

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

## Release Cadence

VS Code moved to **weekly stable releases** starting with v1.111 (March 2026), driven by the rapid pace of AI development. New Copilot features ship as soon as they're ready rather than waiting for a monthly window.

Track releases at [code.visualstudio.com/updates](https://code.visualstudio.com/updates/).

## Getting Started

With VS Code 1.116+, Copilot is available immediately — no separate extension needed. Sign in with your GitHub account and start using Chat, inline suggestions, and agent mode.

For older versions, install the [GitHub Copilot extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) from the VS Code Marketplace.

## Further Reading

- [VS Code Copilot documentation](https://code.visualstudio.com/docs/copilot)
- [Customization overview](https://code.visualstudio.com/docs/copilot/customization/overview)
- [Agent plugins](https://code.visualstudio.com/docs/copilot/customization/agent-plugins)
- [Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)

---

[← Back to Foundations](../part-1-foundations.md)
