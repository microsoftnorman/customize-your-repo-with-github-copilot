# GitHub Copilot in Xcode

[← Back to Foundations](../part-1-foundations.md)

---

GitHub Copilot for Xcode is a standalone macOS application published by GitHub and distributed from the [`github/CopilotForXcode`](https://github.com/github/CopilotForXcode) repository. Unlike the VS Code, JetBrains, and Eclipse integrations — which ship as in-process plugins — the Xcode integration is a separate `.app` bundle that communicates with Xcode through the Source Editor Extension API and macOS Accessibility APIs. This architectural difference shapes everything that follows: the feature ceiling, the installation story, the customization primitive support matrix, and the operational quirks.

This page covers what ships today, how to install and authorize it on current macOS and Xcode versions, which customization primitives are supported, and the limitations iOS/macOS teams need to plan around.

## Distribution and Identity

| Field | Value |
|-------|-------|
| Product name | GitHub Copilot for Xcode |
| Vendor | GitHub |
| Source repository | [github/CopilotForXcode](https://github.com/github/CopilotForXcode) |
| Distribution | `.dmg` downloads on the [repo releases page](https://github.com/github/CopilotForXcode/releases); Homebrew cask `github-copilot-for-xcode` |
| Official docs | [Install GitHub Copilot for Xcode](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension?tool=xcode) |
| License | Source available under the repo's license; Copilot subscription required to use |
| Release cadence | Roughly monthly; track the [releases page](https://github.com/github/CopilotForXcode/releases) and the [GitHub Blog changelog](https://github.blog/changelog/label/copilot/) |

Because the app is distributed outside the Mac App Store, Gatekeeper and notarization apply: on first launch, approve the app at **System Settings → Privacy & Security**. Corporate-managed Macs may need IT to whitelist the bundle identifier and grant the Source Editor Extension and Accessibility permissions via MDM.

## System Requirements

- **macOS 12.0 (Monterey) or later** — current builds target macOS 14/15 primarily; older macOS versions are unsupported.
- **Xcode 8.0 or later** — the Source Editor Extension API exists from Xcode 8 onward; in practice teams run Xcode 15 or 16 with current Copilot builds.
- **Active GitHub Copilot subscription** — Free, Pro, Pro+, Business, or Enterprise. Feature availability within Xcode depends on plan (see [Plans](../part-1-foundations.md#plans)).

Verify minimum versions against the [install guide](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension?tool=xcode) and the latest release notes before upgrading.

## Installation

### Homebrew (recommended)

```bash
brew install --cask github-copilot-for-xcode
```

Homebrew handles download, signature verification, and future upgrades via `brew upgrade --cask github-copilot-for-xcode`.

### Manual `.dmg` install

Download the latest release `.dmg` from [github.com/github/CopilotForXcode/releases](https://github.com/github/CopilotForXcode/releases), open it, and drag **GitHub Copilot for Xcode.app** into `/Applications`. Launch it from Applications (not from the mounted DMG).

### Authorization Steps

On first launch, the app walks through three permission grants — all three are required or completions and chat will silently fail:

1. **System Settings → Privacy & Security → Extensions → Xcode Source Editor** → enable **GitHub Copilot for Xcode**. This exposes the completion and chat commands under Xcode's **Editor** menu.
2. **System Settings → Privacy & Security → Accessibility** → enable **GitHub Copilot for Xcode**. Accessibility access lets the app read the active editor's content to generate suggestions.
3. **Sign in to GitHub** from the Copilot for Xcode status-bar menu. The device-code flow opens a browser; paste the code and approve the **Authorize GitHub Copilot for Xcode** prompt.

Restart Xcode after granting permissions so it picks up the extension.

## What Ships in the App

Core capabilities mirror the other IDE surfaces but the implementation is more constrained because Xcode does not expose a plugin API on par with VS Code, JetBrains, or Eclipse. Cross-check current capabilities against the [install guide](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension?tool=xcode) and the [`github/CopilotForXcode`](https://github.com/github/CopilotForXcode) README.

### Code Completions

Inline suggestions appear as ghost text in the active editor. Accept with **Tab**, cycle alternatives and dismiss via the **Editor → GitHub Copilot** menu commands (bind these to keyboard shortcuts in Xcode's Key Bindings preferences). Completions work across Swift, Objective-C, C/C++, and any other language Xcode opens.

### Chat

A floating chat window outside the Xcode process. Chat can reference the selected code in the active Xcode editor (via Accessibility APIs) and answer questions, explain code, or draft changes. Because it runs out-of-process, chat cannot directly edit files — developers copy suggestions back into Xcode.

### Agent Mode

Agent mode is available and plans multi-step work across the project, reading files and proposing edits. The out-of-process architecture means agent mode writes through the file system rather than through Xcode's editor APIs — keep Xcode's **File → Auto-Save** behavior in mind when the agent modifies open files.

### Model Context Protocol (MCP)

[MCP](https://modelcontextprotocol.io) client support lets Copilot for Xcode connect to external tools and data sources. MCP server configuration is managed within the app's settings panel; there is no on-disk `.vscode/mcp.json` discovery analogous to VS Code.

### Custom Agents (Preview)

[Custom agent definitions](https://docs.github.com/en/copilot/reference/custom-agents-configuration) (`.github/agents/*.md`) are recognized in Preview status. Behavior and frontmatter stability may lag VS Code; verify against the repo's current release notes before relying on a specific field.

## Customization Primitive Support

The [official install docs](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension?tool=xcode) and the [`github/CopilotForXcode`](https://github.com/github/CopilotForXcode) repository are the authoritative sources. The table below is the **Xcode-specific subset** of the canonical [Cross-Surface Primitive Support Matrix](../part-3-reference.md#cross-surface-primitive-support-matrix) (Part III), validated April 2026:

| Primitive | Xcode status | Notes |
|-----------|--------------|-------|
| Always-on instructions (`.github/copilot-instructions.md`) | Preview | Repository-wide rules; use this for every convention you want Copilot to follow |
| File-based instructions (`.github/instructions/*.instructions.md`) | Not supported | `applyTo` glob matching is not implemented on Xcode |
| Prompt files (`.github/prompts/*.prompt.md`) | Preview | Invoke from chat; feature set lags VS Code |
| Custom agents (`.github/agents/*.md`) | Preview | Persona selection available from chat |
| [Agent skills](https://agentskills.io) (`.github/skills/`) | Not supported | No Xcode implementation |
| MCP servers | Supported | Configured from the app's preferences panel |
| Hooks (`.github/hooks/*.json`) | Not supported | Runtime enforcement is VS Code / CLI / cloud agent only |
| [Memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory) (Copilot Memory) | Not surfaced in IDE | Learned knowledge that exists is cloud-side; the Xcode app does not expose Memory review or toggles |
| Agent plugins | Not supported | VS Code / CLI only |

**The practical takeaway:** because file-based instructions, skills, and hooks are not available on Xcode, teams doing iOS/macOS work should fold all conventions into the root `.github/copilot-instructions.md`. Swift-specific, SwiftUI-specific, and test-specific rules that would normally live in separate `.instructions.md` files need to land in the single always-on file for Xcode-using teammates to benefit.

## Known Limitations

- **No workspace indexing.** Copilot for Xcode does not build a semantic index of the Xcode project. Chat and agent mode rely on the active selection, open files, and explicit `@file` references rather than project-wide retrieval. Large refactors that would benefit from cross-file context are weaker here than in VS Code.
- **Out-of-process editing.** Because the app is not an Xcode plugin, it cannot hook into Xcode's refactoring engine, the Fix-it system, or the Interface Builder editor. Agent mode edits Swift storyboards and `.xib` files as raw XML, not through the graphical tools.
- **No terminal tool.** Agent mode runs shell commands through the app's own sandboxed execution context, not through an Xcode-integrated terminal. Developers see command output in the Copilot window, not in Xcode.
- **Completions always insert `\n`.** Like Eclipse, completions use LF line endings regardless of the file's existing convention. Teams with CRLF conventions (rare on iOS/macOS but possible in cross-platform Swift) will see mixed line endings after accepting large completions.
- **MCP configuration is per-install, not per-repo.** There is no `.vscode/mcp.json`-equivalent auto-discovery. MCP servers configured in the app's settings apply across every project the developer opens, and are not committed with the repo.
- **Accessibility prompt reappears after OS updates.** Major macOS upgrades sometimes reset Accessibility grants; re-enable GitHub Copilot for Xcode at **System Settings → Privacy & Security → Accessibility** if completions stop appearing after a macOS upgrade.

## Diagnostics

When things go wrong, check in this order:

1. **Copilot for Xcode status-bar menu** — surfaces sign-in state, Xcode Source Editor Extension state, and network errors.
2. **Console.app** — filter by the `github.copilot` subsystem to see the app's structured logs, including LSP traffic to the language server.
3. **Xcode → Editor → GitHub Copilot menu** — if the submenu is missing entirely, the Source Editor Extension is not enabled; revisit **System Settings → Privacy & Security → Extensions**.

File bugs and feature requests at [github.com/github/CopilotForXcode/issues](https://github.com/github/CopilotForXcode/issues).

## Further Reading

- [Install GitHub Copilot for Xcode](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension?tool=xcode) — official GitHub docs
- [`github/CopilotForXcode`](https://github.com/github/CopilotForXcode) — source repository, release notes, and issue tracker
- [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=xcode) — cross-surface feature grid
- [Cross-Surface Primitive Support Matrix](../part-3-reference.md#cross-surface-primitive-support-matrix) — canonical Part III reference
- [Always-on Instructions](../primitive-1-always-on-instructions.md) — the highest-leverage primitive for Xcode teams
