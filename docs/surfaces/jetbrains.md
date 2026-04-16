# GitHub Copilot in JetBrains IDEs

[← Back to Foundations](../part-1-foundations.md)

---

GitHub Copilot ships as a first-party plugin on the JetBrains Marketplace — [GitHub Copilot](https://plugins.jetbrains.com/plugin/17718-github-copilot) (Plugin ID `com.github.copilot`, vendor GitHub, Inc.). A single binary installs into any compatible JetBrains IDE from the IntelliJ Platform family, which means teams that standardize on JetBrains get the same Copilot experience across every editor their organization uses — and, critically, the same customization model as VS Code. The `.github/copilot-instructions.md`, `.github/instructions/`, `.github/prompts/`, `.github/agents/`, `.github/skills/`, and `.vscode/mcp.json` files that drive a VS Code workspace drive a JetBrains workspace too. There is no second source of truth to maintain.

This page covers what ships in the JetBrains plugin, how it diverges from VS Code, where customization primitives land in Preview versus Supported status, and the operational details — file paths, settings panels, release cadence — that JetBrains-first teams need to run Copilot confidently.

## Supported IDEs

The plugin is compatible with the full IntelliJ Platform lineup. Per the [official installation docs](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension?tool=jetbrains), Copilot works in:

- **IntelliJ IDEA** — Ultimate, Community, and Educational editions
- **Android Studio** — Google's Android Studio is built on IntelliJ IDEA Community; it receives the same plugin and the same customization primitives
- **PyCharm** — Professional, Community, and Educational editions
- **WebStorm**, **PhpStorm**, **RubyMine**, **GoLand**, **RustRover**, **CLion**, **Rider**
- **DataGrip** and **DataSpell** — database and data science workflows
- **JetBrains Client** and **Code With Me Guest** — remote pairing scenarios
- **MPS** (Meta Programming System) and **Writerside** (documentation authoring)

**Fleet is out of scope.** JetBrains Fleet is a separate product not built on the IntelliJ Platform; the `com.github.copilot` plugin does not install into it. **AppCode** was discontinued by JetBrains in December 2022 and is likewise not a supported target. **Android Studio** is supported, but Google's release train trails the IntelliJ Platform by one or two minor versions, so the plugin's minimum-IDE-build sometimes excludes the current Android Studio stable — verify compatibility on the [Marketplace versions page](https://plugins.jetbrains.com/plugin/17718-github-copilot/versions) before upgrading the plugin if Android Studio is the primary target.

Older JetBrains IDE versions are deprecated on a rolling basis. The [plugin changelog](https://plugins.jetbrains.com/plugin/17718-github-copilot) announced end of support for IDE versions **2024.2** and **2024.3**; teams locked to long-term support builds should verify compatibility against the Marketplace versions page before upgrading the plugin.

## What Ships in the Plugin

The JetBrains plugin exposes several top-level capabilities. Each one is a direct analog of the same capability in VS Code, with the same model selection, the same tool-calling infrastructure, and — for the primitives discussed further down — the same on-disk configuration files.

### Code Completions

Inline, as-you-type completions powered by the same backend as VS Code. Accept with Tab, dismiss with Escape, and cycle through alternatives with the plugin's configured shortcuts (Settings → Keymap → search for "Copilot"). Completions work in any language the JetBrains IDE recognizes, including Kotlin, Java, Python, TypeScript, Ruby, Go, C#, C++, Rust, PHP, Scala, and the database query languages in DataGrip.

### Ask Mode (Copilot Chat)

A conversational panel accessed from the right tool window bar via the Copilot Chat icon. Ask mode answers questions about the codebase, explains selected code, drafts commits, generates unit tests, and suggests refactors. It has read-only access to the workspace and can reference files, symbols, and selections explicitly attached to the turn.

### Agent Mode

Available from the same Chat panel via the mode selector. Agent mode plans multi-step tasks, creates and edits files, runs terminal commands, reads command output, and iterates based on errors it observes. Agent mode uses the same tool-calling loop and model roster as agent mode in VS Code. It is a full-parity feature on current JetBrains plugin versions per the [Copilot feature matrix for JetBrains](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=jetbrains).

### Planning (Plan Agent)

A specialized mode that produces a structured implementation plan before any code changes are made. Useful for larger refactors or features where developers want to review the proposed approach — file list, sequencing, risks — before authorizing the agent to execute it.

### Edit Mode

A middle ground between Ask and Agent: Copilot proposes multi-file edits in a reviewable diff, but does not run tools or commands. Useful for targeted refactors where the developer wants the editing power of agent mode without the autonomy.

### Checkpoints

Agent mode automatically creates a restore point before it begins making changes, and additional checkpoints at significant milestones. Developers can revert the workspace to any checkpoint if the agent drifts, without touching Git. Checkpoints are a local, plugin-managed snapshot layer distinct from version control.

### Code Review

Copilot-assisted review comments on pull requests, surfaced in the plugin when browsing PR state from the IDE.

## Keymap and Shortcuts

The plugin registers its own keymap group. Open **Settings → Keymap** and search for **"GitHub Copilot"** to see and rebind every action. The defaults worth memorizing:

- **`Tab`** — accept the current inline completion
- **`Escape`** — dismiss the current inline completion
- **`Alt+]` / `Alt+[`** — cycle to the next / previous completion alternative
- **`Alt+\`** — manually trigger an inline completion at the caret
- **`Ctrl+I`** (Windows/Linux) / **`Cmd+I`** (macOS) — open inline chat on the current selection
- **`Ctrl+Shift+A`** → type "Copilot" to fuzzy-find every Copilot action (install, sign in, open chat, toggle completions per-language, etc.)

Per-language completion toggles live at **Settings → Languages & Frameworks → GitHub Copilot** — useful for silencing completions in, say, SQL files while keeping them on in Kotlin.

## Customization Primitive Support

JetBrains parity is the active investment area for the Copilot team, and the feature matrix changes frequently. The table below is the **JetBrains-specific subset** — it includes features that don't appear in the cross-surface view (checkpoints, next-edit suggestions, vision, workspace indexing). For the canonical cross-surface comparison, see [Part III: Cross-Surface Primitive Support Matrix](../part-3-reference.md#cross-surface-primitive-support-matrix). For the upstream source of truth, consult the [official JetBrains feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=jetbrains). The snapshot below reflects April 2026 — verify before making pinning decisions. "Preview" means the feature ships and works, but its behavior may change without notice and glob-matching, trigger heuristics, or frontmatter fields are not guaranteed stable.

| Primitive | JetBrains status | Notes |
|-----------|------------------|-------|
| Always-on instructions (`.github/copilot-instructions.md`) | Preview | Repository-wide rules; single file per workspace |
| File-based instructions (`.github/instructions/*.instructions.md`) | Preview | Glob matching behavior may differ from VS Code |
| Prompt files (`.github/prompts/*.prompt.md`) | Preview | Invoked from chat with `/<name>` |
| Custom agents (`.github/agents/*.md`) | Preview | Mode selector exposure varies by plugin build |
| Agent skills (`.github/skills/`) | Preview | Auto-invocation heuristics are less mature than VS Code |
| MCP servers (`.vscode/mcp.json`) | ✅ Supported | Same config format as VS Code; MCP Registry UI available |
| Agent mode | ✅ Supported | Full parity |
| Edit mode | ✅ Supported | — |
| Chat | ✅ Supported | — |
| Checkpoints | ✅ Supported | — |
| Workspace indexing | ✅ Supported | Semantic code search for chat/agent context |
| Code completion | ✅ Supported | — |
| Next edit suggestions | Preview | — |
| Vision | Preview | Image attachments in chat |
| BYOK (bring your own key) | Preview | — |
| Hooks (`.github/hooks/*.json`) | ❌ Not supported | Runtime enforcement is VS Code / CLI only |
| Agent plugins (bundled package format) | ❌ Not supported | VS Code-specific |

The JetBrains 2025 rows in the matrix show how recent this parity push is — MCP arrived mid-2025, custom agents landed in Preview only on the latest 2025 build, prompt files and custom instructions moved from unsupported to Preview across the year, and workspace indexing was flipped on only in the newest build. Teams pinned to early-2025 plugin versions will see a materially smaller feature set than teams on current. Enable automatic plugin updates.

## Where Files Live on Disk

Repository-scoped customization uses the **same directory layout as VS Code**. That is the entire point: teams do not maintain a `jetbrains/` variant of their Copilot config.

| What | Path | Scope |
|------|------|-------|
| Always-on instructions | `.github/copilot-instructions.md` | Workspace |
| File-based instructions | `.github/instructions/*.instructions.md` | Workspace |
| Prompt files | `.github/prompts/*.prompt.md` | Workspace |
| Custom agents | `.github/agents/*.md` | Workspace |
| Agent skills | `.github/skills/<skill>/SKILL.md` | Workspace |
| MCP configuration | `.vscode/mcp.json` | Workspace |

JetBrains additionally supports a **machine-global** instructions file that applies across every workspace the signed-in user opens. Per the [JetBrains custom instructions docs](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions?tool=jetbrains), the global file lives at:

- **macOS:** `/Users/<username>/.config/github-copilot/intellij/global-copilot-instructions.md`
- **Windows:** `C:\Users\<username>\AppData\Local\github-copilot\intellij\global-copilot-instructions.md`
- **Linux:** `~/.config/github-copilot/intellij/global-copilot-instructions.md`

Global instructions layer **underneath** repository instructions — repo rules win on conflict — and are useful for personal preferences that should never be committed to a shared codebase (response style, preferred language, personal coding conventions).

## Configuration via the Settings UI

Most primitives can be authored either by hand (edit the Markdown file) or through the plugin's settings panel. The panel is reached via:

**Settings → Tools → GitHub Copilot → Customizations**

From there:

- **Copilot Instructions** — toggle between **Workspace** and **Global**; the editor writes to `.github/copilot-instructions.md` or the global path above.
- **Prompt Files** — click **Workspace** to create a new file under `.github/prompts/` (the plugin appends `.prompt.md`).

The settings page is a convenience layer over the filesystem. Editing the files directly with the IDE's file editor produces identical results and is the recommended approach when the files are already tracked in Git.

## MCP Configuration in JetBrains

[MCP](https://modelcontextprotocol.io) is the most-used integration point in JetBrains today because it is fully supported and reads the same `.vscode/mcp.json` the VS Code side uses. Per the [JetBrains MCP docs](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/extend-copilot-chat-with-mcp?tool=jetbrains), the plugin supports both remote and local MCP servers.

### Opening the MCP Configuration

1. Click the **Copilot** icon in the lower-right status bar.
2. Select **Open Chat**.
3. Switch the chat to **Agent** mode.
4. Click the tools icon ("Configure your MCP server") at the bottom of the chat window.
5. Click **Add MCP Tools** to open `mcp.json`.

### Example: Remote Server with PAT

```json
{
  "servers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp/",
      "requestInit": {
        "headers": {
          "Authorization": "Bearer YOUR_PAT_HERE"
        }
      }
    }
  }
}
```

### Example: Local stdio Server

```json
{
  "servers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

### MCP Registry

JetBrains Chat exposes the public **MCP Registry** UI: click the MCP icon in the chat window, browse available servers, and click **Install** next to each server to wire it up without hand-editing JSON. The registry writes into the same `mcp.json` the manual flow edits.

### Enterprise Policy

For Copilot Business and Copilot Enterprise subscribers, the **MCP servers in Copilot** policy governs whether end users can use MCP at all. The policy is **disabled by default** at the organization and enterprise level. Admins who want MCP available in JetBrains must enable it through the standard Copilot policy surface; Copilot Free, Pro, and Pro+ users are not governed by this policy.

## Prompt Files in JetBrains

Prompt files live in `.github/prompts/*.prompt.md` and are invoked from chat by typing `/` followed by the file's base name — for example, a file named `review-api.prompt.md` is invoked as `/review-api`. Users can attach additional files to the turn and append free-form context after the slash command. The [JetBrains prompt files docs](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions?tool=jetbrains#using-prompt-files) note that prompt files can reference other workspace files with standard Markdown links (`[label](../path/to/file.ts)`) or `#file:` syntax, and that paths are resolved relative to the prompt file itself.

Because prompt files are in Preview on JetBrains, teams relying on sophisticated template features (frontmatter, variable expansion, tool restrictions) should test each prompt in JetBrains before asserting parity — VS Code advances faster on this surface.

## IDE-Family Specifics

The plugin is one binary, but the host IDE's project model changes how agent mode behaves. Points JetBrains-family leads frequently trip on:

- **Rider (.NET).** Agent mode edits `.csproj`, `.sln`, and `Directory.Build.props` like any other file, but Rider's solution loader needs to re-read them before IntelliSense catches up — expect a brief "NuGet restore / reload solution" step after agent edits. Rider runs ReSharper's completion engine alongside Copilot; if completions feel sluggish, check **Settings → Editor → Code Completion** for conflicting shortcuts.
- **Android Studio.** The IntelliJ Platform version Android Studio ships on trails upstream. Workspace indexing and newer agent features may be gated behind a plugin build that Android Studio's current stable doesn't meet. If an instruction or prompt works in IntelliJ IDEA but not Android Studio, plugin-version mismatch is the first thing to check.
- **Gradle / Maven agent commands.** When agent mode runs `./gradlew` or `mvn` from its terminal tool, it uses the IDE's configured JDK and Gradle wrapper. On Windows the default shell is controlled by **Settings → Tools → Terminal → Shell path** (PowerShell vs. `cmd.exe` vs. Git Bash); mismatched quoting between the agent's command shape and the configured shell is a common cause of "command works in IntelliJ terminal but fails in agent mode."
- **Kotlin Notebooks (IntelliJ IDEA Ultimate) and DataSpell / Jupyter.** Cell-level completions and chat context window behave differently from flat `.kt` or `.py` files — notebook context is built per-cell and can miss state that was established only at runtime. Prefer Ask mode for notebook explain/refactor tasks; Agent mode's multi-file edits are less reliable across cells.
- **"Trust Project" dialog.** JetBrains blocks tool execution in *untrusted* projects. The first time a project is opened, Copilot agent mode's terminal and file-write tools are disabled until the project is trusted. This is the #1 cause of "why won't agent mode run anything?" on freshly cloned repos.

## Corporate Network, Proxies, and TLS

JetBrains routes Copilot's HTTPS traffic through the IDE's built-in HTTP client, so corporate-network configuration lives in **Settings → Appearance & Behavior → System Settings → HTTP Proxy** (manual, auto-detect, or proxy script). Two enterprise gotchas come up repeatedly:

- **Custom certificate authorities.** MITM inspection proxies typically present certificates signed by an internal CA. JetBrains stores trusted certs in **Settings → Tools → Server Certificates** (auto-accept is also toggled here). Copilot respects the IDE trust store; if sign-in fails with TLS errors, add the intercepting CA here and restart the IDE. In stubborn cases, import the CA into the JetBrains bundled JRE's `cacerts` or override with `-Djavax.net.ssl.trustStore=...` in **Help → Edit Custom VM Options**.
- **GHE.com / GHES endpoints.** Managed users on `ghe.com` enterprise tenants must set the enterprise URL in the plugin's authentication settings *before* signing in — device-flow auth against `github.com` will silently point at the wrong tenant otherwise. See the [GHE.com authentication guide for JetBrains](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/using-github-copilot-with-an-account-on-ghecom?tool=jetbrains#authenticating-from-jetbrains-ides).

## Logs and Diagnostics

When filing a bug at [`microsoft/copilot-intellij-feedback`](https://github.com/microsoft/copilot-intellij-feedback), attach the IDE log. Reach it with **Help → Show Log in Explorer** (Windows/Linux) or **Help → Show Log in Finder** (macOS); Copilot-specific entries are in the `github-copilot/` subdirectory alongside `idea.log`. Increase verbosity via **Help → Diagnostic Tools → Debug Log Settings** and add `#com.github.copilot` before reproducing. For agent-mode failures, the chat panel's **...** overflow menu often includes a "Copy diagnostics" action that bundles the relevant session state.

This is also the recommended path for support tickets — GitHub Support (`support.github.com`) handles account, billing, and service-wide issues, while plugin bugs belong in the public feedback repo.

## JetBrains AI Assistant vs. GitHub Copilot

JetBrains ships its own AI product — **JetBrains AI Assistant** — in the same IDEs. It is a separate plugin (`com.intellij.ml.llm`), a separate subscription sold by JetBrains, and a separate chat/completions surface. It can coexist with GitHub Copilot in the same IDE, but the two do not share configuration, history, or model selection. Users encountering a chat panel that doesn't understand `.github/copilot-instructions.md` are usually looking at AI Assistant's panel, not Copilot's. The Copilot panel is labelled "GitHub Copilot" and lives under the right tool window bar; AI Assistant has its own icon with a different gradient. Disable whichever plugin is not in use to avoid double-billing completion shortcuts.

## Settings Sync and EAP Channel

- **Settings Sync.** Copilot authentication state does not ride on JetBrains Settings Sync — users signing in on a new machine must complete the device-code flow again. Per-user preferences (keymap changes, enabled languages) *do* sync if Settings Sync is on.
- **EAP plugin channel.** For teams that want early access to parity features (new primitives moving from unsupported → Preview), the plugin has an Early Access Preview channel. Add `https://plugins.jetbrains.com/plugins/eap/17718` in **Settings → Plugins → ⚙ → Manage Plugin Repositories** to receive EAP builds. Note: EAP builds are unstable by design and are inappropriate for shared dev boxes or CI runners.

## What JetBrains Does Not Have (Yet)

Several primitives and diagnostic capabilities available in VS Code do not yet exist on the JetBrains side. Teams that depend on them should keep a VS Code path open for affected workflows, or do that work from the Copilot CLI (which has independent support for hooks-adjacent enforcement via GitHub Actions and external tooling).

- **Hooks** (`.github/hooks/*.json`) — runtime enforcement of allow/deny rules, command interception, and pre/post-tool scripts is not implemented. Teams that need deterministic gates must run those workflows in VS Code or layer enforcement outside the IDE (pre-commit, CI, MCP server-side checks).
- **[Agent plugins](https://code.visualstudio.com/docs/copilot/customization/agent-plugins)** (bundled customization packages) — the distribution format for shipping a cohesive bundle of instructions, prompts, agents, and MCP servers is VS Code-specific.
- **Agent debug logs parity** — JetBrains provides less visibility into the agent's step-by-step tool-call sequence than VS Code's timeline view. The IDE log (see **Logs and Diagnostics** above) is the fallback, but structured per-turn traces are a VS Code advantage.
- **Fine-grained glob differences** — file-based instructions apply, but the matching engine may not handle every VS Code glob edge case identically while the primitive is in Preview. If a `.instructions.md` file mysteriously fails to activate in JetBrains, simplify the `applyTo` pattern before assuming the feature is broken.

## Release Cadence and Upgrade Strategy

The plugin ships on GitHub's schedule, not JetBrains'. Updates land on the marketplace **multiple times per week** — often daily during active development windows. The plugin is published by GitHub under the license terms in the [GitHub Terms for Additional Products and Features](https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features#github-copilot).

Operational recommendations:

- **Enable automatic plugin updates** in Settings → Plugins. Older plugin builds frequently fall behind backend changes and may stop functioning for agent mode, MCP, or newer models.
- **Track the changelog.** The plugin's "What's New" section on the [marketplace listing](https://plugins.jetbrains.com/plugin/17718-github-copilot) lists bug fixes, deprecations, and new features per release. End-of-support announcements for older IDE versions land here first.
- **Pin the IDE to a supported minor** if the team cannot upgrade frequently. Deprecations (e.g., 2024.2/2024.3) usually ship with several weeks of lead time.
- **Report issues to the public feedback repo:** [`microsoft/copilot-intellij-feedback`](https://github.com/microsoft/copilot-intellij-feedback). This is the canonical place for plugin bugs; GitHub Support handles account, billing, and service-wide issues.

## Getting Started

1. Open **Settings → Plugins → Marketplace** in any compatible JetBrains IDE.
2. Search for **GitHub Copilot** and install.
3. Restart the IDE when prompted.
4. Open the **Tools** menu → **GitHub Copilot** → **Login to GitHub**.
5. In the "Sign in to GitHub" dialog, click **Copy and Open**. A device-activation page opens in the browser.
6. Paste the device code, click **Continue**, then **Authorize GitHub Copilot Plugin** to approve the requested permissions.
7. Return to the IDE and click **OK** on the confirmation dialog.
8. Open any project. The Copilot icon should appear in the right tool window bar and in the status bar.

An active Copilot subscription is required — Free, Pro, Pro+, Business, or Enterprise. Users on a **GHE.com** managed account need to configure an enterprise URL in the plugin settings before signing in; see the [GHE.com authentication guide](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/using-github-copilot-with-an-account-on-ghecom?tool=jetbrains#authenticating-from-jetbrains-ides).

## Verifying Custom Instructions Are Being Used

JetBrains does not surface injected instructions inline in the chat stream. To confirm that repository instructions or prompt files are reaching the model, expand the **References** list under any chat response — if `.github/copilot-instructions.md` (or a matching prompt/instruction file) was part of the prompt, it appears as a clickable reference. This is the same verification path documented for VS Code and is the only in-IDE signal that customization is active.

## Further Reading

- [GitHub Copilot plugin — JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot)
- [Installing GitHub Copilot in JetBrains IDEs](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension?tool=jetbrains)
- [Copilot feature matrix — JetBrains](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=jetbrains)
- [Repository custom instructions and prompt files in JetBrains](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions?tool=jetbrains)
- [Configuring MCP servers in JetBrains](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/extend-copilot-chat-with-mcp?tool=jetbrains)
- [Plugin feedback and issue tracker](https://github.com/microsoft/copilot-intellij-feedback)

---

[← Back to Foundations](../part-1-foundations.md)
