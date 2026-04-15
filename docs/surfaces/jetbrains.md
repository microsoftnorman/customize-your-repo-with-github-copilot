# GitHub Copilot in JetBrains IDEs

[← Back to Foundations](../part-1-foundations.md)

---

[GitHub Copilot for JetBrains](https://plugins.jetbrains.com/plugin/17718-github-copilot) covers IntelliJ IDEA, PyCharm, WebStorm, GoLand, Rider, and others. The plugin provides code completion, Chat, agent mode, MCP, checkpoints, and workspace indexing.

## Primitive Support

Customization primitive support is growing but not yet at full parity with VS Code:

| Primitive | JetBrains Support |
|-----------|-------------------|
| Custom instructions | Preview |
| Custom agents | Preview |
| Agent skills | Preview |
| Prompt files | Preview |
| MCP servers | ✅ Supported |
| Agent mode | ✅ Supported |
| Hooks | Not yet supported |

The same `.github/copilot-instructions.md`, `.github/agents/*.md`, and `.vscode/mcp.json` files used in VS Code are read by the JetBrains plugin. Teams that invest in repo-level customization get value across both IDEs without maintaining separate configurations.

## Release Cadence

JetBrains support ships in the Copilot plugin (currently v1.5.66+), not in the IDE itself. The plugin updates **multiple times per week** — sometimes daily. Enable automatic plugin updates to avoid interruptions, as older versions may become incompatible.

## Getting Started

1. Open **Settings** → **Plugins** → **Marketplace**
2. Search for "GitHub Copilot"
3. Install and restart the IDE
4. Sign in with your GitHub account

Requires an active Copilot subscription (Free, Pro, Pro+, Business, or Enterprise).

## Further Reading

- [JetBrains Marketplace — GitHub Copilot](https://plugins.jetbrains.com/plugin/17718-github-copilot)
- [Installing Copilot in JetBrains](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-the-github-copilot-extension-in-your-environment)
- [Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)

---

[← Back to Foundations](../part-1-foundations.md)
