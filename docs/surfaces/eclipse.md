# GitHub Copilot in Eclipse

[← Back to Foundations](../part-1-foundations.md)

---

GitHub Copilot for Eclipse is a first-party plugin published by Microsoft on the [Eclipse Marketplace](https://marketplace.eclipse.org/content/github-copilot) and on a dedicated [Azure-hosted p2 update site](https://azuredownloads-g3ahgwb5b8bkbxhd.b01.azurefd.net/github-copilot/). It brings the Copilot experience (completions, chat, agent mode, and [MCP](https://modelcontextprotocol.io)) into the Eclipse IDE and Eclipse-based distributions (Spring Tool Suite, JBoss Developer Studio, IBM Developer for z/OS, SAP ABAP Development Tools, eGovFrame, and others that inherit from the Eclipse Platform). The plugin has been [announced to go open source under the MIT license](https://devblogs.microsoft.com/java/ghc-eclipse-is-going-open-source/) and ships updates on an approximately monthly cadence alongside the rest of the Copilot IDE family.

This page covers what the plugin does and does not ship today, how to install it reliably in corporate networks where the default update site is often blocked, which customization primitives are available in Preview versus Supported status, and the operational details that Eclipse-first teams need: Java runtime requirements, proxy and certificate handling, Node.js language server architecture, and log locations.

## Plugin Identity and Distribution

| Field | Value |
|-------|-------|
| Plugin name | GitHub Copilot |
| Vendor | GitHub (published by Microsoft) |
| Marketplace listing | [marketplace.eclipse.org/content/github-copilot](https://marketplace.eclipse.org/content/github-copilot) |
| Primary p2 update site | `https://azuredownloads-g3ahgwb5b8bkbxhd.b01.azurefd.net/github-copilot/` |
| Nightly p2 update site | `https://azuredownloads-g3ahgwb5b8bkbxhd.b01.azurefd.net/github-copilot-eclipse-nightly/` |
| License | Commercial (requires a Copilot subscription); plugin source moving to MIT |
| Feedback tracker | [github.com/microsoft/copilot-eclipse-feedback](https://github.com/microsoft/copilot-eclipse-feedback) |
| Community discussion | [GitHub Copilot for Eclipse discussions](https://github.com/orgs/community/discussions/151288) |
| Release cadence | Approximately monthly, with entries on the [GitHub Blog changelog](https://github.blog/changelog/label/copilot/) |

The plugin's minimum Eclipse version is **2024-03 (4.31)**, and the [Marketplace listing](https://marketplace.eclipse.org/content/github-copilot) advertises support across the 2024-03 through 2025-12 (4.38) release train. Distributions based on older Eclipse Platform builds (for example, 4.25 or custom corporate distributions) are not supported. Requests to relax this constraint are tracked in the feedback repo but are not planned.

## Supported IDEs and Distributions

Any IDE built on the Eclipse Platform 4.31 or newer can install the plugin from the Marketplace or the p2 update site. In practice this includes:

- **Eclipse IDE:** every package (Java, JEE, C/C++, PHP, Rust, etc.) from 2024-03 onward
- **Spring Tool Suite (STS) 4:** when rebased on a supported Eclipse Platform version
- **JBoss Developer Studio / Red Hat CodeReady Studio:** on supported platform versions
- **IBM Developer for z/OS and IBM Engineering Workflow Management:** Eclipse-based distributions
- **SAP ABAP Development Tools (ADT):** with caveats on agent mode for ABAP workspaces (see [Known Issues](#known-issues))
- **eGovFrame** (Korean government framework): when rebased on 2024-03 or newer

**Eclipse Theia** is a separate, Chromium-based IDE framework that ships its own Copilot integration. It is not the same plugin as `com.microsoft.copilot.eclipse.*` covered here. Theia's Copilot support is documented in the [Theia project](https://theia-ide.org/) and operates under Theia's own extension model.

**Che, Orion, and other browser-based Eclipse derivatives** are not supported targets for this plugin.

## Installation

There are three supported installation paths. Pick the one that works for your network.

### 1. Eclipse Marketplace (recommended)

From a running Eclipse: **Help → Eclipse Marketplace…** → search for `GitHub Copilot` → click **Install** on the GitHub Copilot tile. Eclipse handles p2 resolution and restart prompts.

This path requires the Marketplace client (bundled in every package since 2015) and outbound HTTPS to both `marketplace.eclipse.org` and the Azure-hosted artifact CDN. If the Marketplace client is missing, install it first from **Help → Install New Software…** using `https://download.eclipse.org/mpc/` as the update site.

### 2. Install New Software (for restricted networks)

If the Marketplace client cannot reach Eclipse's servers (common behind corporate proxies that whitelist only a subset of domains), install directly from the p2 site:

1. **Help → Install New Software…**
2. Click **Add…** and enter:
   - Name: `GitHub Copilot`
   - Location: `https://azuredownloads-g3ahgwb5b8bkbxhd.b01.azurefd.net/github-copilot/`
3. Check **GitHub Copilot** under the category that appears, click **Next**, accept the license, and restart Eclipse.

Include the trailing slash. The URL must be HTTPS. The Azure Front Door endpoint occasionally returns `ResourceNotFound` responses if reached through a proxy that rewrites the Host header or if the p2 cache has a stale artifact reference. If you see `Can't download artifact ... com.microsoft.copilot.eclipse.feature_<version>.jar` or a `PKIX path building failed` error, jump to [Networking, Proxies, and Certificates](#networking-proxies-and-certificates).

### 3. Nightly Builds

For early access to unreleased features, use the nightly update site:

```
https://azuredownloads-g3ahgwb5b8bkbxhd.b01.azurefd.net/github-copilot-eclipse-nightly/
```

Nightlies carry the `_nightly` suffix on bundle versions (for example `0.12.0.202511030212_nightly`) and are not recommended for production development workflows. File any regressions to the [feedback tracker](https://github.com/microsoft/copilot-eclipse-feedback/issues).

### Signing In

On first launch after install, the plugin surfaces a **Sign In to GitHub** action in the bottom-right status bar of the Eclipse workbench. The sign-in flow uses the GitHub device code grant:

1. Click the Copilot status-bar icon → **Sign In to GitHub**
2. Click **Copy Code and Open**. The device code is placed on your clipboard and `https://github.com/login/device` opens in your default browser
3. Paste the code, click **Continue**, approve the **Authorize GitHub Copilot Plugin** prompt
4. Return to Eclipse; the status bar transitions to "Copilot Ready"

If the Eclipse side does not transition after browser authorization completes, the most common cause is an HTTPS interception proxy (Zscaler, Netskope, Palo Alto GlobalProtect) that the embedded Node.js language server cannot traverse. See [Networking, Proxies, and Certificates](#networking-proxies-and-certificates).

## Architecture

The Eclipse plugin is thin. The heavy lifting is done by a bundled **Copilot Language Server**: a Node.js process that the plugin spawns and communicates with over the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) via JSON-RPC (using `org.eclipse.lsp4j`). The same language server binary powers Copilot's JetBrains, Xcode, and neovim integrations. The Eclipse plugin's job is to translate Eclipse editor events, selections, workspace changes, and chat UI actions into LSP messages.

Practical implications:

- **Node.js is bundled.** You do not need a system Node.js install. The `language-server.js` entry point ships inside the plugin's `resources/` directory. A runtime error reading `Unable to locate language-server.js` indicates a corrupted install — reinstall the feature.
- **Java 21 is required.** Eclipse 2024-03 and newer require Java 17 for the IDE itself, but the Copilot plugin has a narrower floor and the community has reported issues on older JDKs. Pin `-vm <path-to-jdk-21>` in `eclipse.ini` if mixing JREs.
- **Network traffic originates from the Node.js process, not the JVM.** Any proxy or CA configuration in `eclipse.ini` only applies to Eclipse's own HTTP client. The Copilot Language Server reads `HTTPS_PROXY`, `HTTP_PROXY`, `NO_PROXY`, and `NODE_EXTRA_CA_CERTS` environment variables the way Node.js normally does.

## What Ships in the Plugin

Each capability has a direct analog in VS Code and JetBrains, using the same model roster and tool-calling infrastructure. Availability varies by plugin version and Eclipse version. Always cross-check against the [Copilot feature matrix for Eclipse](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=eclipse).

### Code Completions

Inline, as-you-type completions. Accept with **Tab**, dismiss with **Escape**, cycle alternatives with the shortcuts registered under **Window → Preferences → General → Keys** (search for "Copilot"). Completions work across any language Eclipse opens as a text document: Java, Kotlin, Python (PyDev), C/C++ (CDT), JavaScript/TypeScript (Wild Web Developer), PHP, Groovy, Rust, Go, and database query languages.

**Known quirk:** completions always insert with `\n` line endings regardless of the file's existing convention or the Eclipse preference for new files. On Windows projects configured for CRLF this can produce mixed line endings that trip static analyzers; fix by running **Source → Convert Line Delimiters To → Windows** after accepting large completions.

### Ask Mode (Copilot Chat)

A conversational panel opened via **Window → Show View → GitHub Copilot → Chat** or by clicking the Copilot status-bar icon. Ask mode answers questions, explains selected code, drafts refactors, and generates unit tests. It has read-only access to the workspace plus whatever you explicitly attach (files, selections, open editor).

**Editor selection context** is automatic as of the February 2026 release. Selected code in the active editor is sent with every chat turn without needing to re-attach it manually.

### Agent Mode

Available from the chat mode selector. Agent mode plans multi-step tasks, creates and edits files, and runs terminal commands through an integrated execution sandbox. As of the February 2026 release the plugin also ships:

- **Todo List tool:** agent mode maintains a structured checklist in-view, checking items off as it completes them
- **Agent max requests preference:** configurable cap on the number of LLM turns before agent mode pauses and asks the user to type `continue`

**URI scheme limitation:** agent mode only operates on workspace resources whose URIs use the standard `file://` scheme. ABAP projects from SAP ADT use a `semanticfs://` URI scheme and fail with `Copilot currently does not support URI with scheme: semanticfs`. Ask mode works for ABAP; agent mode does not. This is tracked as an open issue in the [feedback repo](https://github.com/microsoft/copilot-eclipse-feedback/issues).

### Model Context Protocol (MCP)

Full MCP client support for connecting external tools and data sources. As of the February 2026 release the plugin also includes an **MCP Registry**: a curated browser for discovering and installing MCP servers without hand-editing configuration. Open via the chat view toolbar.

MCP server configuration is read from the plugin's preference store (**Preferences → GitHub Copilot → MCP Servers**). There is no equivalent to VS Code's `.vscode/mcp.json` auto-discovery yet; per-workspace MCP configuration must be re-entered per Eclipse installation.

### Custom Agents (Preview)

Custom agent definitions following the [frontmatter-based `.md` format](https://docs.github.com/en/copilot/reference/custom-agents-configuration) are recognized on the two most recent Eclipse releases (2025-12 and 2025-09 at time of writing). See the [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=eclipse) for the authoritative per-version support grid.

### Custom Instructions (Preview)

Repository-level `.github/copilot-instructions.md` is in Preview across all supported Eclipse versions. Behavior and glob-match semantics may change without notice.

### Commit Message Generation

The **Git Staging** view (EGit) gains a Copilot button that drafts commit messages from the staged diff. Commit instruction customization is available under **Preferences → GitHub Copilot → Commit Instructions**. Use it to bind the plugin's output to your team's commit convention (Conventional Commits, Gitmoji, custom formats).

### Chat View UX

As of the February 2026 release, the chat view supports font-size shortcuts (`Ctrl+=` / `Ctrl+-` on Windows/Linux, `Cmd+=` / `Cmd+-` on macOS), undo/redo in the composer, a refreshed dark theme, and a new native Eclipse toolbar for chat view actions. If the new toolbar buttons do not appear after updating, delete `<workspace>/.metadata/.plugins/org.eclipse.e4.workbench/workbench.xmi` and restart. This is a known first-run workaround published in the [changelog](https://github.blog/changelog/2026-02-17-mcp-registry-and-more-improvements-in-copilot-in-eclipse/).

## Customization Primitive Support

The [Copilot feature matrix for Eclipse](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=eclipse) is the authoritative reference. The table below is the **Eclipse-specific subset**: it includes Eclipse-only items (BYOK status on current builds, next-edit suggestions, vision, workspace indexing). For the canonical cross-surface comparison, see [Part III: Cross-Surface Primitive Support Matrix](../part-3-reference.md#cross-surface-primitive-support-matrix). The snapshot below reflects April 2026 on the latest Eclipse release.

| Primitive | Eclipse status | Notes |
|-----------|----------------|-------|
| Always-on instructions (`.github/copilot-instructions.md`) | Preview | Repository-wide rules, single file per workspace |
| File-based instructions (`.github/instructions/*.instructions.md`) | Not supported | Tracked on feature matrix; no shipping date |
| Prompt files (`.github/prompts/*.prompt.md`) | Not supported | Not on current roadmap per the feature matrix |
| Custom agents (`.github/agents/*.md`) | Supported on 2 most recent Eclipse releases | Preview-style behavior; re-check per plugin update |
| Agent skills | Not supported | No Eclipse implementation in progress |
| MCP | Supported | MCP Registry ships in February 2026 release |
| Hooks | Not supported | VS Code exclusive |
| Memory | Cloud-side (GitHub) | Available; learned knowledge works because it is server-side |
| BYOK (bring your own key) | Preview on latest | Per feature matrix |
| Next edit suggestions | Preview on 2 most recent Eclipse releases | Tab-to-jump edit propagation |
| Vision (image input) | Supported | Image attachment to chat turns |
| Workspace indexing | Supported | Local semantic index for chat retrieval |

**Not supported and not on the roadmap as of April 2026:** agent skills, prompt files, file-based instructions, checkpoints, Java Upgrade Agent, Copilot code review. Teams that rely heavily on file-based instructions or prompt files in VS Code should expect to maintain those primitives for VS Code-using teammates while the always-on `copilot-instructions.md` carries the shared rules.

## Networking, Proxies, and Certificates

Behind a corporate TLS-intercepting proxy, the Copilot Language Server often fails to reach GitHub's APIs. This is the most common failure mode on the Eclipse plugin. Symptoms include:

- `FetchError: unable to get local issuer certificate` on chat send
- `Sign in failed: ... unable to get local issuer certificate` after the browser completes device-code authorization
- `PKIX path building failed` when p2 tries to read the update site (this one is on the JVM side)
- `Failed to start copilot language server` at startup with no detail

The plugin's JVM-side HTTP calls honor the standard Eclipse network settings at **Preferences → General → Network Connections**. The Node.js language server does not. To fix Node-side TLS, set environment variables **before launching Eclipse** so the launched Node child process inherits them:

**Windows (PowerShell, per-user):**

```powershell
[Environment]::SetEnvironmentVariable('NODE_EXTRA_CA_CERTS', 'C:\certs\corporate-root-ca.pem', 'User')
[Environment]::SetEnvironmentVariable('HTTPS_PROXY', 'http://proxy.corp:8080', 'User')
```

**macOS / Linux (`~/.zshrc` or `~/.bashrc`):**

```bash
export NODE_EXTRA_CA_CERTS=/etc/ssl/certs/corporate-root-ca.pem
export HTTPS_PROXY=http://proxy.corp:8080
```

Export the proxy's root CA as a PEM file and point `NODE_EXTRA_CA_CERTS` at it. Importing the certificate into the system trust store is not sufficient. Node.js does not read the Windows Trust Store or the macOS Keychain by default.

After changing environment variables, fully quit Eclipse (not just restart the plugin) and relaunch so the Node.js child process inherits the new environment.

For p2 update-site failures (`PKIX path building failed`), import the same CA into the JVM's cacerts keystore, or configure Eclipse to use the platform trust store by adding `-Djavax.net.ssl.trustStoreType=Windows-ROOT` (Windows) or `-Djavax.net.ssl.trustStoreType=KeychainStore` (macOS) to `eclipse.ini`.

## Logs and Diagnostics

When things go wrong, diagnose in this order:

1. **Error Log view:** **Window → Show View → Error Log**. Filter by plugin `com.microsoft.copilot.eclipse.*`. Double-click entries to see stack traces; the relevant ones typically originate in `CopilotUi`, `LanguageServerSettingManager`, or `ShowStatusBarMenuHandler`.
2. **Copilot output channel:** from the Chat view toolbar, open the Copilot log output. This contains the JSON-RPC traffic between the plugin and the Copilot Language Server.
3. **`.log` file:** `<workspace>/.metadata/.log` contains the raw Eclipse log. Grep for `copilot` or for `NullPointerException` stack frames in `com.microsoft.copilot.*`.
4. **Workbench reset:** if the plugin's UI elements (menus, toolbars, status bar) fail to render after an update, delete `<workspace>/.metadata/.plugins/org.eclipse.e4.workbench/workbench.xmi` and restart. Eclipse rebuilds the workbench model from scratch. This is a supported workaround published by the plugin team.
5. **Clean restart:** run `eclipse -clean` once after any major plugin upgrade to force p2 and OSGi to rebuild their caches.

## Known Issues and Workarounds

The issues below are frequently reported on the [Marketplace reviews](https://marketplace.eclipse.org/content/github-copilot) and the [feedback tracker](https://github.com/microsoft/copilot-eclipse-feedback/issues).

- **`semanticfs://` URIs unsupported in agent mode:** SAP ABAP projects fail with `Copilot currently does not support URI with scheme: semanticfs`. Use ask mode; there is no workaround for agent mode at this time.
- **LF line endings on Windows:** inline completions always insert `\n` regardless of file convention. Manually convert with **Source → Convert Line Delimiters To** after large accept operations.
- **`NullPointerException` on status-bar menu:** `this.languageServerSettingManager is null` thrown from `ShowStatusBarMenuHandler`. Workaround published in the reviews: **Window → Perspective → Customize Perspective → Menu Visibility** → uncheck **Copilot**, then open **Window → Show View → GitHub Copilot → Chat** to fully initialize the plugin, then re-enable the menu.
- **p2 `ResourceNotFound` on Azure Front Door:** the artifact CDN occasionally returns 404 for specific feature JARs when reached through a rewriting proxy. Retry without the proxy, or use the Marketplace client instead of the raw p2 URL.
- **Device-code sign-in stuck after browser approval:** almost always a CA issue; see [Networking, Proxies, and Certificates](#networking-proxies-and-certificates).
- **Missing `language-server.js`:** corrupted install. Uninstall the feature completely (**Help → About Eclipse → Installation Details → Installed Software → Uninstall**), restart, then reinstall.

## Release Cadence and Feedback

Updates ship approximately monthly. Each release has a [GitHub Blog changelog entry](https://github.blog/changelog/label/copilot/); for example, the [MCP Registry and more improvements release from February 2026](https://github.blog/changelog/2026-02-17-mcp-registry-and-more-improvements-in-copilot-in-eclipse/). Release version tags also appear on the [feedback repo's Releases page](https://github.com/microsoft/copilot-eclipse-feedback/releases).

For feature requests, bug reports, and regressions:

- **File issues** at [github.com/microsoft/copilot-eclipse-feedback/issues](https://github.com/microsoft/copilot-eclipse-feedback/issues)
- **Discuss** in the [GitHub Copilot for Eclipse community discussion](https://github.com/orgs/community/discussions/151288)
- **Browse announcements** on the [Microsoft for Java Dev Blog](https://devblogs.microsoft.com/java/), which covers both Java/Eclipse and JetBrains plugin news

The plugin is moving to [open source under the MIT license](https://devblogs.microsoft.com/java/ghc-eclipse-is-going-open-source/), hosted under the `microsoft` GitHub organization. Once the source repo is public, pull requests will be the preferred feedback channel for bug fixes.

## Further Reading

- [Eclipse Marketplace: GitHub Copilot](https://marketplace.eclipse.org/content/github-copilot)
- [Installing Copilot in Eclipse](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension?tool=eclipse): official GitHub docs
- [Copilot feature matrix for Eclipse](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=eclipse)
- [copilot-eclipse-feedback repository](https://github.com/microsoft/copilot-eclipse-feedback): issues, releases, terminal dependency guide
- [GitHub Copilot for Eclipse Is Going Open Source](https://devblogs.microsoft.com/java/ghc-eclipse-is-going-open-source/): MIT licensing announcement
- [MCP Registry and more improvements in Copilot in Eclipse](https://github.blog/changelog/2026-02-17-mcp-registry-and-more-improvements-in-copilot-in-eclipse/): representative monthly changelog
- [Microsoft for Java Dev Blog](https://devblogs.microsoft.com/java/): ongoing coverage of the Eclipse and JetBrains Copilot plugins

---

[← Back to Foundations](../part-1-foundations.md)
