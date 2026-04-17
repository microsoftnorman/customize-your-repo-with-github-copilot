# Where GitHub Copilot Runs: IDE Surfaces

[← Back to Foundations](part-1-foundations.md)

---

The customization primitives in this guide are **file-based and IDE-agnostic**. A `.github/copilot-instructions.md` file applies whether the developer is in VS Code, JetBrains, the CLI, or the cloud agent.

This page is the narrative reference for surface-specific details: authoring UX, setup gotchas, and the limitations that matter when picking an IDE.

**See it in action:** In [A Unified Agent Experience](https://www.youtube.com/watch?v=tAezuMSJuFs&t=4350s), Josh Spicer demos how agent sessions work consistently across VS Code, the cloud agent, and the Copilot CLI from a single unified view.

## Primitive Support by Surface

The canonical matrix lives in [Part III: Cross-Surface Primitive Support Matrix](part-3-reference.md#cross-surface-primitive-support-matrix). For the authoritative upstream source, always consult the [GitHub Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix).

Verify the live state before locking in tooling decisions. Primitive parity on non-VS-Code surfaces changes monthly.

For [GitHub Copilot code review](code-review.md), which runs on GitHub.com, GitHub Mobile, and most IDE plugins, see the dedicated [Code Review guide](code-review.md) for which primitives steer review behavior and where each surface's in-IDE review lives.

## Surface Notes

### VS Code

**Official docs:** [Copilot in VS Code](https://code.visualstudio.com/docs/copilot) · [Customization overview](https://code.visualstudio.com/docs/copilot/customization/overview)

**See it in action:** Courtney Webster's [Customize Your Agents](https://www.youtube.com/watch?v=tAezuMSJuFs&t=10598s) walkthrough demos VS Code's Chat Customizations editor and the `/create-agent`, `/create-skill`, and `/create-instruction` authoring flows.

- **Built-in since VS Code 1.116.** No extension to install. Disable AI features with `chat.disableAIFeatures`.
- **Most complete primitive support.** This guide uses VS Code for examples because every primitive is available here first.
- **Authoring:** Chat Customizations editor (gear icon in Chat view) plus `/create-instruction`, `/create-prompt`, `/create-skill`, `/create-agent`, `/create-hook`, and `/init` slash commands.
- **Parent repository discovery** (`chat.useCustomizationsInParentRepositories`) lets monorepos share customizations across subfolder workspaces.
- **Edit mode is on a deprecation path.** As of VS Code 1.116 (April 2026) it is still present but de-emphasized. Agent mode is the recommended path for all file modifications. Verify the status in the [VS Code release notes](https://code.visualstudio.com/updates/) before building workflows around it.

### Visual Studio

**Official docs:** [Copilot in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-extension) · [Feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=visualstudio)

- **Two product lines:** Visual Studio 2022 (17.x) and Visual Studio 2026 (18.x). Feature cadence is slower than VS Code because Copilot ships with Visual Studio servicing updates, not a separate extension.
- **Agent mode requires VS 2022 17.14 or any VS 2026 release.** MCP is GA on both.
- **Prompt files, custom agents, skills, and BYOK are Visual Studio 2026 only.** Hooks and agent plugins are not supported on any Visual Studio version.
- **Built-in agents:** `@debugger`, `@profiler`, `@test`, `@modernize` (.NET/C++), and `@vs` integrate with features unique to Visual Studio (debugger state, profiler traces, Test Explorer).
- **MCP config discovery** reads `%USERPROFILE%\.mcp.json`, `<SOLUTIONDIR>\.vs\mcp.json`, `<SOLUTIONDIR>\.mcp.json`, `.vscode/mcp.json`, and `.cursor/mcp.json` in that order. A repo's VS Code MCP config therefore works in Visual Studio with no duplication.
- **Enablement:** custom instructions require toggling **Tools → Options → GitHub → Copilot → Copilot Chat → Enable custom instructions**. Off by default.

### JetBrains IDEs

**Official docs:** [Install for JetBrains](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension?tool=jetbrains) · [Feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=jetbrains) · [Plugin on Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot)

- **Single plugin (`com.github.copilot`)** installs into IntelliJ IDEA, PyCharm, WebStorm, PhpStorm, RubyMine, GoLand, RustRover, CLion, Rider, DataGrip, DataSpell, Android Studio, JetBrains Client, MPS, and Writerside. Fleet and AppCode are not supported.
- **Same `.github/` layout as VS Code.** No JetBrains-specific config files.
- **Global user instructions** live outside the repo at `~/.config/github-copilot/intellij/global-copilot-instructions.md` (and the Windows/macOS equivalents). Repo instructions layer on top.
- **Trust Project** must be accepted before agent mode's file-write and terminal tools will run. This is a common cause of "agent does nothing on a fresh clone."
- **Android Studio trails upstream IntelliJ by one or two versions.** The plugin's minimum-IDE-build sometimes excludes current Android Studio stable. Verify on the Marketplace versions page before upgrading.
- **JetBrains AI Assistant is a separate product.** A chat panel that ignores `.github/copilot-instructions.md` is usually AI Assistant, not Copilot.
- **File bugs at** [`microsoft/copilot-intellij-feedback`](https://github.com/microsoft/copilot-intellij-feedback).

### Xcode

**Official docs:** [Install for Xcode](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension?tool=xcode) · [CopilotForXcode repo](https://github.com/github/CopilotForXcode) · [Full reference: surfaces/xcode.md](surfaces/xcode.md)

- **Standalone macOS application** distributed as a `.dmg` (or via the `github-copilot-for-xcode` Homebrew cask), not an Xcode extension proper. Integrates via the Source Editor Extension API and requires Accessibility and Source Editor Extension permissions.
- **Requires macOS 12.0+ and Xcode 8.0+.**
- **Agent mode and MCP are supported.** File-based instructions, skills, hooks, and memory are not. Use `.github/copilot-instructions.md` for all conventions.
- **No workspace indexing.** Semantic search over the project is not available.

For install paths, permission setup, the primitive support table, and known limitations, see [surfaces/xcode.md](surfaces/xcode.md).

### Eclipse

**Official docs:** [Install for Eclipse](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension?tool=eclipse) · [Feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=eclipse) · [Copilot for Eclipse on the Marketplace](https://marketplace.eclipse.org/content/github-copilot) · [Feedback repo](https://github.com/microsoft/copilot-eclipse-feedback)

- **Open source (MIT)**, [released to open source in 2026](https://devblogs.microsoft.com/java/ghc-eclipse-is-going-open-source/). Maintained by Microsoft and community contributors.
- **Agent mode, custom agents, and MCP are supported.** Prompt files, skills, and hooks are not.
- **Eclipse Theia** (the cloud/web IDE) supports Copilot natively from version 1.68: authentication, model selection, and agent features included.

### GitHub Copilot CLI

**Official docs:** [GitHub Copilot CLI](https://github.com/features/copilot/cli/) · [copilot-cli repo](https://github.com/github/copilot-cli)

The [CLI reference](surfaces/copilot-cli.md) covers its own slash-command vocabulary (`/fleet`, `/delegate`, `/plan`, `/yolo`, `/remote`), YOLO mode, CLI-specific extensions (`.github/extensions/`), and the fact that it is the only surface besides VS Code with full hooks support.

### GitHub Copilot Cloud Agent

The [cloud agent reference](surfaces/cloud-coding-agent.md) covers the agent that runs in GitHub Actions, reads the same customization primitives, and is governed through organization-level policy. It's a fundamentally different operational model from the IDE surfaces above.

### GitHub Copilot SDK

**Official docs:** [copilot-sdk repo](https://github.com/github/copilot-sdk)

See [copilot-sdk.md](copilot-sdk.md) for the full reference. The SDK is not an IDE surface. It's a library for embedding the agent runtime in custom tools, internal platforms, or CI pipelines.

## Choosing a Surface

The primitives are portable, but surfaces have clear fits:

| Use this surface | When |
|------------------|------|
| **VS Code** | You want the newest primitives first, the widest extension ecosystem, or you're building/authoring customizations. |
| **Visual Studio** | The team works in `.sln` / MSBuild, depends on the .NET debugger/profiler/designers, or maintains C++/WinForms/WPF. |
| **JetBrains** | The team is already standardized on IntelliJ-family IDEs (Kotlin/Android, Scala, Rider-based .NET, data-stack via PyCharm/DataSpell). |
| **Xcode** | iOS/macOS/visionOS native development where Xcode is required. |
| **Eclipse** | Java enterprise environments or Eclipse Theia-based cloud IDEs. |
| **GitHub Copilot CLI** | Terminal-first workflows, CI/automation, SSH-only hosts, or parallel sub-agent work (`/fleet`). |
| **Cloud Agent** | Autonomous tasks started from issues, Agents panel, or mobile, plus anything that should produce a PR without a developer at a keyboard. |
| **GitHub Copilot SDK** | You're building a custom surface that isn't covered by the above. |

---

[← Back to Foundations](part-1-foundations.md)
