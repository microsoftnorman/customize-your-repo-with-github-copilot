# GitHub Copilot in Visual Studio

[← Back to Foundations](../part-1-foundations.md)

---

[GitHub Copilot for Visual Studio](https://marketplace.visualstudio.com/items?itemName=GitHub.copilotvs) is the first-party AI assistant for the Windows-based Visual Studio IDE. It ships as a recommended component in the Visual Studio Installer and is installed by default with every workload. This page is the definitive reference for teams using Copilot inside **Visual Studio 2022 (17.x)** and **Visual Studio 2026 (18.x)** on .NET, C++, and game development projects.

## Positioning

Copilot in Visual Studio is a different product from Copilot in VS Code or JetBrains Rider. It is built by the Visual Studio team in partnership with GitHub, and it integrates with tooling that only Visual Studio exposes: the .NET debugger, the profiler, the Windows Forms designer, the C++ toolchain, MSBuild, the Test Explorer, and the Git tooling. Core capabilities (chat, agent mode, MCP, custom instructions, prompt files) are the same customization primitives you find in VS Code, but the surface area, feature cadence, and keyboard map are distinct.

Choose Copilot in Visual Studio when:

- The team works primarily in solutions (`.sln`), project files, and MSBuild.
- .NET debugger, profiler, designer, or database tooling is part of the daily loop.
- C++ with MSVC, Windows SDK, or game engines (Unreal, Unity native) is the target platform.
- Enterprise policy requires Visual Studio for tooling compliance (WinForms/WPF maintenance, MFC, XAML).

Choose Copilot in VS Code when breadth of extensions, web/JS/TS workflows, or the full set of customization primitives (skills, hooks, agent plugins) matters more than deep .NET/C++ tooling. Choose Copilot in JetBrains Rider when the team is already standardized on Rider.

## Version Matrix

GitHub publishes the canonical [Copilot feature matrix for Visual Studio](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=visualstudio). The table below summarizes feature availability on the two product lines as of April 2026. Use the linked matrix for the authoritative per-servicing-release breakdown.

| Feature | VS 2022 17.10–17.12 | VS 2022 17.13 | VS 2022 17.14+ | VS 2026 18.0–18.3 | VS 2026 18.4+ |
|---|---|---|---|---|---|
| Code completions | ✓ | ✓ | ✓ | ✓ | ✓ |
| Chat | ✓ | ✓ | ✓ | ✓ | ✓ |
| Ask mode | ✓ | ✓ | ✓ | ✓ | ✓ |
| Edit mode | ✓ | ✓ | Closing down | ✓ | Closing down |
| Agent mode | ✗ | Preview | ✓ | ✓ | ✓ |
| MCP | ✗ | Preview | ✓ | ✓ | ✓ |
| Custom instructions (`copilot-instructions.md`) | ✓ | ✓ | ✓ | ✓ | ✓ |
| File-based instructions (`*.instructions.md`) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Prompt files | ✗ | ✗ | ✗ | ✗ | ✓ |
| Custom agents (`.agent.md`) | ✗ | ✗ | ✗ | ✗ | ✓ (Preview) |
| Agent skills | ✗ | ✗ | ✗ | ✗ | ✓ (18.4.1+) |
| Checkpoints | ✓ | ✓ | ✓ | ✓ | ✓ |
| BYOK | ✗ | ✗ | ✗ | ✗ | ✓ |
| Workspace indexing | ✗ | ✗ | ✗ | ✗ | ✓ |
| Next edit suggestions | ✓ | ✓ | ✓ | ✓ | ✓ |
| Vision (image attachments) | Preview | ✓ | ✓ | ✓ | ✓ |
| Copilot code review | ✓ | ✓ | ✓ | ✓ | ✓ |
| Copilot memories | ✓ | ✓ | ✓ | ✓ | ✓ |
| Cloud coding agent integration | ✗ | ✗ | ✗ | Preview (18.1) | ✓ |

**Edition notes.** Copilot is available across Visual Studio Community, Professional, and Enterprise editions on equal terms; there is no edition gating for Copilot features themselves. Copilot is **not** included in a Visual Studio subscription — it is a separate GitHub subscription (Free, Pro, Business, or Enterprise). Enterprise policy features (content exclusions, MCP allowlists, telemetry controls, preview feature toggles) are governed at the GitHub organization level, not the Visual Studio edition level.

## Installation and Sign-in

Copilot components are bundled into every workload. To verify or re-install:

1. Open the **Visual Studio Installer**.
2. Select **Modify** on the Visual Studio 2022 or 2026 instance.
3. Under **Individual components**, confirm **GitHub Copilot** is checked.
4. Complete the installation and launch Visual Studio.

To sign in:

1. Open Visual Studio and select the **profile icon** in the upper right.
2. Choose **Add an account → GitHub**.
3. Complete the browser OAuth flow. The account must have a GitHub Copilot subscription (Free, Pro, Business, or Enterprise).

The Copilot status badge on the Visual Studio title bar indicates connection state and surfaces quick settings.

### Organization and enterprise policy

For organization-managed accounts, administrators control Copilot behavior from the **GitHub Copilot dashboard** at the organization or enterprise level. Relevant policies include:

- **Editor preview features** — governs agent mode, MCP usage, and other preview capabilities. When disabled, users on that subscription cannot use agent mode or MCP servers in Visual Studio.
- **Public code matching** — controls whether completions that match public repositories are allowed or filtered.
- **Content exclusions** — path and repository-level rules that prevent Copilot from sending certain files to the model.
- **MCP server allowlist** — restricts which MCP servers the organization permits.

See [Admin controls for GitHub Copilot](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-admin) for the full administrator reference.

### Proxy and firewall

Visual Studio honors the system proxy for Copilot network traffic. Organizations running an HTTPS inspection proxy must trust the proxy's root certificate in the Windows certificate store. Required endpoints include `api.githubcopilot.com`, `*.githubusercontent.com`, and the token/auth endpoints at `github.com`. For remote MCP servers, outbound HTTPS to those servers must also be permitted.

## Inline Completions (Code Completions)

As code is typed, Copilot streams ghost-text suggestions in the editor. Completions are syntax-highlighted with reduced opacity to distinguish them from committed code.

### Accepting and cycling suggestions

| Action | Shortcut |
|---|---|
| Accept full suggestion | `Tab` |
| Reject suggestion | `Esc` |
| Trigger suggestion manually (or next) | `Alt+.` |
| Cycle to previous suggestion | `Alt+,` |
| Accept next word | `Ctrl+Right Arrow` |
| Accept next line | `Ctrl+Down Arrow` |
| Click-to-accept partial | Hover inside suggestion and click at the cut point |

The default accept key can be remapped from `Tab` to `Right Arrow` under **Tools → Options → Text Editor → Inline Suggestions**.

### Behavior tuning

**Tools → Options → Text Editor → Inline Suggestions** exposes:

- **Inline Suggestions Invocation** — switch from automatic to manual. In manual mode, suggestions appear only when invoked with `Alt+.` or `Alt+,`.
- **Show inline suggestions only after a pause in typing** — adds a debounce delay so completions do not flash while typing.
- **Use colorized text for code completions** — disable to fall back to the legacy single-color ghost text.

### Per-language enable/disable

Completion enablement is controlled at the Copilot badge menu on the title bar. Open the badge → **Completions** → toggle for **all languages** or for the current language only. The setting is persisted per user.

## Copilot Chat

Copilot Chat in Visual Studio has two surfaces:

- **Chat window** — opened from **View → GitHub Copilot Chat**. Best for open-ended questions, multi-turn dialogs, and tasks that span multiple files.
- **Inline chat** — right-click in the editor and select **Ask Copilot → Chat**, or use the editor's context menu. Best for tightly scoped edits on the current selection; displays suggestions as an inline diff.

### Context references

Chat inputs accept `#` references to attach specific context. When typing `#`, Visual Studio provides IntelliSense for valid reference types.

| Reference | Scope |
|---|---|
| `#file:path` | A specific file in the solution |
| `#solution` | The whole solution as context |
| `#selection` | The current editor selection |
| `#terminalSelection` | Currently selected text in the integrated terminal |
| `#prompt:name` | Invoke a stored prompt file |

Attach references via `+ Add Reference` in the chat input or via the `#` IntelliSense picker. MCP-provided resources and prompts also surface in these pickers once a server is connected.

### Slash commands

Type `/` in the chat input to open the command palette. Built-in slash commands:

| Command | Purpose | Chat window | Inline chat |
|---|---|---|---|
| `/doc` | Add documentation comments to selected/specified code | ✓ | ✓ |
| `/explain` | Explain selected/specified code | ✓ | ✓ |
| `/fix` | Propose a fix for problems in the selection | ✓ | ✓ |
| `/generate` | Generate code for a described task | ✓ | ✓ |
| `/generateInstructions` | Analyze the repository and produce a `copilot-instructions.md` file | ✓ | ✗ |
| `/help` | Help on using Copilot Chat | ✓ | ✓ |
| `/optimize` | Analyze and improve runtime of the selection | ✓ | ✓ |
| `/savePrompt` | Save the current prompt as a `.prompt.md` file under `.github/prompts/` | ✓ | ✗ |
| `/tests` | Generate unit tests for the selected code | ✓ | ✓ |

Starting with Visual Studio 2022 17.13, typing a slash command expands it into a natural-language prompt so the context it will include is visible before sending.

### GitHub Copilot actions

The editor's right-click menu exposes preconfigured Copilot actions that map to slash commands: **Explain**, **Generate Tests**, **Generate Comments**, **Optimize Selection**, and **Add to Chat**. Of these, **Optimize Selection** is unique in that it shows results as an inline diff rather than routing to the chat window.

## Ask, Edit, and Agent Modes

Copilot Chat supports three interaction modes. Switch between them from the mode dropdown next to the chat input.

| Mode | Behavior | When to use |
|---|---|---|
| **Ask** | Copilot answers questions and can propose code, but applies nothing automatically. | Exploration, explanations, and when zero unsolicited edits are required. |
| **Edit** | Copilot proposes multi-file edits that the user reviews in a batch. | Coordinated changes across a small number of files when full autonomy is not wanted. |
| **Agent** | Copilot autonomously plans, edits, runs tools, and iterates until the task is done. | Multi-step tasks that cross files, require running builds/tests, or benefit from tool use. |

**Edit mode** is being phased out (`closing down` in the feature matrix). It remains present in mid-cycle VS 2022 releases but is subsumed by agent mode going forward. Agent mode is the recommended modality for any multi-file work in current Visual Studio releases.

MCP tools are **only available in agent mode**. Ask mode cannot invoke MCP servers.

## Agent Mode

Agent mode requires **Visual Studio 2022 17.14 or later**, or any Visual Studio 2026 release. It evolved from Copilot Edits with a greater ability to iterate on errors, use tools, and apply code changes automatically.

### How it works

1. The user enters a high-level prompt (for example, "Add pagination to the `/orders` endpoint, including integration tests").
2. Copilot determines relevant files from the open solution.
3. Copilot invokes tools — built-in or from connected MCP servers — to edit files, run terminal commands, execute builds, and run tests.
4. Copilot requests confirmation before running a terminal command or a non-built-in tool.
5. As edits stream into the editor, Copilot monitors outcomes (compiler errors, test failures) and iterates until the goal is met or input is needed.

### Approval model

Each tool invocation prompts for confirmation. The **Allow** dropdown offers three scopes:

- **This session** — auto-approve for the current chat session.
- **This solution** — auto-approve for any session in this solution.
- **Always** — auto-approve on every invocation.

Reset all approvals under **Tools → Options → GitHub → Copilot → Tools**. Terminal commands warrant extra scrutiny: the agent runs them with the same permissions as Visual Studio itself, and they are **not** restricted to the solution directory.

### File visibility

Agent mode can read and modify only files that are:

- Part of the open solution, **or**
- Located in the solution directory or a subdirectory.

Files matched by organization content exclusions are never sent. Terminal commands, however, inherit the Visual Studio process's full filesystem permissions.

### Checkpoints and revert

Each prompt that produces edits creates a **checkpoint**. Select **Restore** next to any checkpoint to revert all changes made since that point. Stepwise undo/redo of individual agent edits is not supported — revert operates at the checkpoint granularity. For finer control, review the **Total changes** list and accept or discard file-by-file.

### Planning (Preview)

Planning mode (preview in Visual Studio 2022 17.14) lets the agent decompose complex requests into structured, trackable tasks. When active, Copilot:

- Generates a user-facing Markdown plan that shows goals and progress.
- Maintains an internal JSON plan (`plan-{sessionId}.json`) for step tracking.
- Uses dedicated internal tools (`plan`, `adapt_plan`, `update_plan_progress`, `record_observation`, `finish_plan`).

Plans are stored under `%LOCALAPPDATA%\Temp\VisualStudio\copilot-vs` and deleted at session end unless saved manually. Enable planning at **Tools → Options → GitHub → Copilot → Copilot Chat → Enable Planning**.

### Built-in agents

Agent mode ships with specialized built-in agents that integrate with specific Visual Studio features. Invoke them with `@` syntax or via the agent picker in VS 2026 Insiders.

| Agent | Purpose |
|---|---|
| `@debugger` | Diagnoses exceptions using call stacks, variable state, and diagnostic tools. |
| `@profiler` | Connects to Visual Studio profiling to identify bottlenecks and propose targeted fixes. |
| `@test` | Generates unit tests tuned to the project's testing framework. |
| `@modernize` | (.NET and C++ only) Assesses, plans, and executes framework/dependency upgrades. |
| `@vs` | General Visual Studio IDE assistant. |

### Interrupting a run

Click **Cancel** in the chat window to stop an agent run. Canceling halts running tools and terminal commands. To stop a build specifically, select **Build → Cancel** or press `Ctrl+Break`.

## Model Picker and BYOK

Visual Studio exposes a model picker at the bottom of the Copilot Chat window. The dropdown lists frontier models hosted by GitHub Copilot (names and exact availability evolve with each servicing release). Use the picker to switch models mid-conversation.

### BYOK (Bring Your Own Key)

BYOK is available in **Visual Studio 2026** only. With BYOK, teams can connect an API key from a supported model provider and use that provider's models inside Copilot Chat alongside the GitHub-hosted selection. BYOK respects organization policy — administrators can disable it. Configure BYOK from the model picker's **Manage models** entry.

The set of supported providers and specific model SKUs is published on the GitHub Copilot product pages and the Visual Studio release notes rather than frozen in documentation; consult the in-product model picker for the current list.

## MCP Servers

Visual Studio is a first-class MCP client starting in **VS 2022 17.14** (generally available) and in all Visual Studio 2026 releases.

### Configuration discovery

Visual Studio looks for MCP configuration in the following locations, in order:

1. `%USERPROFILE%\.mcp.json` — global for all solutions.
2. `<SOLUTIONDIR>\.vs\mcp.json` — per-solution, per-user; not source-controlled.
3. `<SOLUTIONDIR>\.mcp.json` — per-solution; the recommended source-controlled location.
4. `<SOLUTIONDIR>\.vscode\mcp.json` — shared with VS Code.
5. `<SOLUTIONDIR>\.cursor\mcp.json` — shared with Cursor.

The cross-tool discovery is deliberate: teams that work across VS Code and Visual Studio can share a single `mcp.json` in either `.vscode` or `.mcp.json`.

### Supported transports and features

- **Transports:** `stdio`, server-sent events (`sse`), and streamable HTTP (`http`).
- **Capabilities:** tools, prompts, resources, sampling.
- **Roots:** the current solution folders are advertised to servers via MCP `roots`.
- **Authorization:** OAuth providers are supported per the MCP authorization specification, in addition to the Visual Studio keychain.

### Example configuration

```json
{
  "servers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

Save the file. A CodeLens **Authentication Required** banner appears above the server block; click it to OAuth in. Then open Copilot Chat, switch to **Agent** mode, and enable the server's tools from the tool picker.

### Adding servers from the UI

- **Install from the web** — one-click install links (for example, `vs-open.link/mcp-install?...`) register servers in the user's `%USERPROFILE%\.mcp.json`.
- **Add from chat** — click the green `+` in the chat tool picker and fill in the name and connection details.
- **Extensions → MCP Registries…** — browse and install servers from the GitHub MCP server registry.

### Enterprise MCP governance

MCP usage respects organization allowlists set on the GitHub Copilot dashboard. When an allowlist is configured, Visual Studio blocks servers outside the list and surfaces an organization-policy error. Visual Studio 2026 18.3 and later expose **enterprise-level MCP governance** controls to administrators, including per-server scopes and audit surfaces.

### Tool lifecycle

When a server is discovered, Visual Studio performs a handshake, queries the tool list, and subscribes to `notifications/tools/list_changed`. If the server advertises a change, prior approvals are reset to prevent "rug-pull" attacks. New tools are **disabled by default** and must be enabled manually.

## Custom Instructions

Visual Studio supports both always-on and file-based instructions. Both formats require explicit enablement in options.

### `.github/copilot-instructions.md`

The always-on instructions file lives at the repository root under `.github/copilot-instructions.md`. Enable it at **Tools → Options → All Settings → GitHub → Copilot → Copilot Chat → Enable custom instructions to be loaded from `.github/copilot-instructions.md` files and added to requests**. When active, Visual Studio attaches the file to every request and lists it in the response's **References** panel. The file is not visible in the chat input itself.

### `.github/instructions/*.instructions.md` (file-based)

Visual Studio supports file-based instructions with `applyTo` glob targeting. Format:

```markdown
---
description: C# coding conventions
applyTo: '**/*.cs'
---

- Use PascalCase for public members, camelCase for private fields and locals.
- Add a newline before the opening brace of any block.
- Ensure the final `return` in a method is on its own line.
```

The same **Enable custom instructions** option in Copilot Chat settings controls both `copilot-instructions.md` and `.github/instructions/*.instructions.md` loading. Visual Studio automatically selects matching instruction files based on the files under discussion and attaches them as references.

### User-level preferences

Personal preferences — the ones that should follow the developer across repositories — live at `%USERPROFILE%\copilot-instructions.md`. Repo-level instructions in `.github/copilot-instructions.md` still apply alongside user-level preferences, so team standards are not overridden.

### Generating instructions

Use `/generateInstructions` in chat to have Copilot analyze the project structure, coding patterns, and frameworks, and produce an initial `.github/copilot-instructions.md` file. Treat the output as a starting point rather than a finished artifact; review and edit before committing.

## Prompt Files

Prompt files are supported in **Visual Studio 2026 (latest release)**. They are not yet supported on Visual Studio 2022.

Prompt files are Markdown files with `.prompt.md` extension stored in `.github/prompts/` at the repository root. Invoke them by typing `/` in the chat input — custom prompts appear at the top of the IntelliSense list with a bookmark icon. They can also be referenced with `#prompt:name` to embed one prompt into another.

Create prompt files in two ways:

- **Manually.** Create `.github/prompts/my-task.prompt.md` with optional YAML frontmatter and a Markdown body.
- **From chat.** Run `/savePrompt` after a useful prompt, name the file, and Visual Studio writes it to `.github/prompts/`.

See the examples section below for concrete prompt file templates.

## Memory

Visual Studio supports **Copilot memories** — repository-scoped memory that observes preferences during chat and can automatically write them into `%USERPROFILE%\copilot-instructions.md` or the repo-level instructions file. Memories are surfaced as references on responses that use them, and users can review, accept, or reject proposed additions before they are persisted. Memory is governed by the same enablement checkboxes as custom instructions.

## Primitive Support Matrix

| Primitive | Visual Studio 2022 17.14+ | Visual Studio 2026 (current) |
|---|---|---|
| Always-on instructions (`copilot-instructions.md`) | ✓ Supported | ✓ Supported |
| File-based instructions (`*.instructions.md`) | ✓ Supported | ✓ Supported |
| Prompt files (`*.prompt.md`) | ✗ Not supported | ✓ Supported |
| Skills | ✗ Not supported | ✓ Supported (18.4.1+) |
| Custom agents (`*.agent.md`) | ✗ Not supported | ✓ Supported (18.4+, Preview) |
| MCP servers | ✓ Supported | ✓ Supported |
| Hooks | ✗ Not supported | ✗ Not supported |
| Memory (Copilot memories) | ✓ Supported | ✓ Supported |
| Agent plugins (bundled packages) | ✗ Not supported | ✗ Not supported |
| Agentic workflows (`.github/workflows/*.md`) | Runs on GitHub Actions, independent of the IDE | Runs on GitHub Actions, independent of the IDE |

Agentic workflows are a GitHub platform feature; they execute in GitHub Actions and do not require any specific IDE. They are listed here for completeness.

## What's Not Supported in Visual Studio

- **Hooks** — runtime enforcement of agent behavior through the hook framework is a VS Code–only primitive.
- **Agent plugins** — the bundled customization package format is VS Code–only.
- **Prompt files on Visual Studio 2022** — available only in Visual Studio 2026 (current release).
- **Custom agents on Visual Studio 2022** — require Visual Studio 2026 18.4 or later.
- **BYOK on Visual Studio 2022** — Visual Studio 2026 only.
- **Workspace indexing on Visual Studio 2022** — Visual Studio 2026 only.
- **Agent picker UI** — currently available only in the Visual Studio 2026 Insiders builds; stable builds use `@` syntax.

The gap between VS Code and Visual Studio is closing with each Visual Studio 2026 servicing update, but feature cadence in Visual Studio remains slower than in VS Code Insiders because features ship with Visual Studio updates rather than through a separate weekly extension.

## Tailoring `copilot-instructions.md`

Because always-on instructions are the primitive with the broadest Visual Studio version support, they carry disproportionate weight. The following three examples target common Visual Studio audiences.

### Example 1 — Modern .NET / ASP.NET Core

```markdown
# Copilot Instructions — .NET Team

## Tech Stack
- .NET 10, C# 14, nullable reference types enabled solution-wide
- ASP.NET Core Minimal APIs with FluentValidation
- EF Core 10 with SQL Server; migrations via `dotnet ef`
- xUnit + FluentAssertions + Testcontainers for integration tests

## Code Style
- `sealed` classes by default; unseal only when inheritance is a documented design decision
- Prefer `record` over `class` for DTOs
- Async all the way down — no `.Result` or `.Wait()` on Tasks
- One type per file; file name matches type name
- File-scoped namespaces

## Examples

✅ Preferred:
```csharp
public sealed record CreateOrderRequest(Guid CustomerId, IReadOnlyList<LineItem> Items);

public static async Task<IResult> CreateOrderAsync(
    CreateOrderRequest request,
    IOrderService orders,
    CancellationToken ct)
{
    var result = await orders.CreateAsync(request, ct);
    return result.IsSuccess
        ? Results.Created($"/orders/{result.Value.Id}", result.Value)
        : Results.BadRequest(result.Error);
}
```

❌ Avoid:
```csharp
public class CreateOrderRequest { public Guid CustomerId; public List<LineItem> Items; }

public static IActionResult CreateOrder(CreateOrderRequest r, IOrderService s) {
    return new OkResult(s.CreateAsync(r).Result);
}
```
```

### Example 2 — Enterprise WinForms / WPF + EF6

```markdown
# Copilot Instructions — Line-of-Business App

## Context
- WinForms on .NET Framework 4.8 being migrated to .NET 8 WinForms
- EF6 on SQL Server; migrations are code-first and reviewed by DBAs
- Async is introduced gradually — do not blanket-convert existing sync code
- UI thread marshaling via `Control.BeginInvoke` / `SynchronizationContext`

## Rules
- Never edit `*.Designer.cs` manually. If a control change is required, describe it and ask for designer steps.
- Preserve `[DefaultValue]` and `ShouldSerialize*` members on custom controls — they are required for CodeDOM serialization.
- Use `TableLayoutPanel` / `FlowLayoutPanel` for new dialogs; avoid absolute `Location` math.
- EF6 queries must project to DTOs before `.ToList()` — no returning `IQueryable` across layers.
- All new code must compile with nullable reference types opt-in (`<Nullable>enable</Nullable>`), file-by-file, after review.

## Testing
- Unit tests: MSTest v2 in a separate `*.Tests` project.
- Integration tests run against LocalDB; do not touch the shared dev database.
```

### Example 3 — Game Dev (Unreal Engine / C++)

```markdown
# Copilot Instructions — Game Client (Unreal)

## Engine & Toolchain
- Unreal Engine 5.4, C++20 where the engine permits
- MSVC v143, Windows SDK 10.0.22621
- Build via UnrealBuildTool; do not invoke `cl.exe` directly

## UE-Specific Rules
- All `UCLASS`, `USTRUCT`, `UENUM`, `UFUNCTION`, `UPROPERTY` macros must be on their own line above the member.
- Use `TObjectPtr<T>` for new `UPROPERTY` references; only use raw `UMyType*` when matching existing API.
- Prefer `FName` for string identifiers, `FString` for user-facing text, `FText` for anything localized.
- Logging: `UE_LOG(LogGame, Verbose, ...)` — never `printf`, never `std::cout`.
- No STL containers for gameplay code — use `TArray`, `TMap`, `TSet`.

## Performance
- Hot paths run on the game thread; do not allocate in `Tick`.
- Prefer `ParallelFor` over `std::thread` for data-parallel work.

## Don't
- Do not add new third-party dependencies without updating `.uplugin` / `.uproject` and flagging the license.
- Do not modify generated `*.generated.h` files.
```

## Prompt File Examples

All three examples target Visual Studio 2026 (prompt files are not yet supported on Visual Studio 2022).

### Minimal API endpoint scaffold

`.github/prompts/new-endpoint.prompt.md`:

```markdown
---
description: Scaffold a new Minimal API endpoint with validation and tests
---

Create a new Minimal API endpoint for `${input:resourceName}`:

1. Endpoint handler in `src/Api/Endpoints/${input:resourceName}Endpoints.cs`
2. `FluentValidation` validator for the request record
3. xUnit integration test in `tests/Api.Tests/Endpoints/${input:resourceName}EndpointsTests.cs`
4. Use `IResult` return types, not `IActionResult`
5. Include cancellation-token plumbing end-to-end

Follow the conventions in #file:.github/copilot-instructions.md.
```

### xUnit test generation

`.github/prompts/xunit-tests.prompt.md`:

```markdown
---
description: Generate xUnit + FluentAssertions tests for the current selection
---

Generate xUnit tests for ${selection} using the following conventions:

- Test class per type under test, named `${TypeUnderTest}Tests`
- `[Fact]` for single-scenario tests, `[Theory]` + `[InlineData]` for parameterized
- Arrange/Act/Assert blocks separated by blank lines
- Assertions via FluentAssertions (`result.Should().Be(...)`)
- Use `AutoFixture` to construct inputs when available
- Mock dependencies with `NSubstitute`
- One behavior per test; no multi-scenario tests

Place the file at `tests/${ProjectName}.Tests/${TypeUnderTest}Tests.cs`.
```

### Roslyn analyzer + code-fix scaffold

`.github/prompts/roslyn-analyzer.prompt.md`:

```markdown
---
description: Scaffold a Roslyn analyzer with a matching code fix
---

Create a Roslyn analyzer and code fix named `${input:analyzerName}` that reports when `${input:pattern}` appears.

Deliverables:
1. `src/Analyzers/${input:analyzerName}Analyzer.cs` — `DiagnosticAnalyzer` with `[DiagnosticAnalyzer(LanguageNames.CSharp)]`.
2. `src/Analyzers/${input:analyzerName}CodeFixProvider.cs` — `CodeFixProvider` with `[ExportCodeFixProvider(LanguageNames.CSharp)]`.
3. Diagnostic descriptor registered with a stable ID like `TEAM0001`, `Info` or `Warning` severity, and a localizable message.
4. Unit tests in `tests/Analyzers.Tests/` using `Microsoft.CodeAnalysis.CSharp.Testing.XUnit` — both analyzer and code-fix tests, covering positive, negative, and trivia-preservation cases.
5. Entry in `AnalyzerReleases.Unshipped.md`.

Follow the conventions in #file:.github/copilot-instructions.md.
```

## Keyboard Shortcuts Cheat Sheet

Default Visual Studio keybindings on Windows. Remap any of these under **Tools → Options → Environment → Keyboard**.

| Action | Shortcut |
|---|---|
| Open Copilot Chat window | `View → GitHub Copilot Chat` (no default key) |
| Open inline chat | Right-click → **Ask Copilot** |
| Accept completion | `Tab` |
| Dismiss completion | `Esc` |
| Trigger / next completion | `Alt+.` |
| Previous completion | `Alt+,` |
| Accept next word | `Ctrl+Right Arrow` |
| Accept next line | `Ctrl+Down Arrow` |
| Cancel build (to interrupt an agent-initiated build) | `Ctrl+Break` |

Visual Studio 2026 18.5 introduced **customizable Copilot keyboard shortcuts** — the set of remappable actions is larger, and Chat/Agent-specific commands now appear as named commands in the keyboard options page.

## Settings and Telemetry

Copilot settings live under **Tools → Options → GitHub → Copilot**. Key sections:

- **Copilot Chat** — enable agent mode, enable custom instructions (`copilot-instructions.md` and `.instructions.md`), enable planning, project-specific .NET instructions (for example, auto-attach WinForms expert on WinForms projects).
- **Tools** — reset MCP tool confirmations, manage per-tool approval scope.
- **Copilot** (top-level) — telemetry, public code matching override, chat history retention.

Enterprise policy at the GitHub organization level governs:

- Whether preview features (including agent mode and MCP) are available.
- The MCP server allowlist.
- Content exclusions (paths, repos, file patterns).
- Model availability and BYOK enablement.
- Whether completions that match public code are allowed.

Telemetry controls follow the broader Visual Studio diagnostic data settings at **Help → Privacy → Manage diagnostic data collection settings**. Copilot respects those settings for telemetry but transmits prompts and context to the model provider as required for inference.

## Limitations and Known Issues

- **Feature cadence is tied to Visual Studio servicing releases** — new capabilities typically arrive monthly rather than weekly. Expect lag behind VS Code for brand-new Copilot features.
- **Hooks and agent plugins** are not supported. Teams that rely on these primitives in VS Code must fall back to runtime enforcement via CI, MCP-provided guards, or agent-side instructions.
- **Stepwise agent undo** is not supported; revert granularity is the checkpoint.
- **Terminal command sandboxing** — agent-invoked terminal commands run with full Visual Studio process permissions. Review each terminal command before approval.
- **Plan persistence** — agent-mode planning artifacts live under `%LOCALAPPDATA%\Temp\VisualStudio\copilot-vs` and are cleared at session end unless saved manually.
- **Agent picker** — the visual agent picker is currently exclusive to Visual Studio 2026 Insiders; stable builds rely on `@` syntax.
- **MCP server discovery across `.vs` and `.vscode` folders** — configuration in `.vs/mcp.json` is per-user and not source-controlled; teams that want shared configuration must use `.mcp.json` at the solution root.

Check the [Visual Studio 2026 release notes](https://learn.microsoft.com/en-us/visualstudio/releases/2026/release-notes) and [Visual Studio 2022 release history](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-history) for current known issues.

## Release Cadence

Copilot features ship as part of Visual Studio servicing updates, not through a separate extension. Cadence:

- **Visual Studio 2026** — monthly updates; each minor (18.x.0) adds features, point releases (18.x.y) fix bugs and patch security. Recent examples: 18.0 GA Nov 2025, 18.1 Dec 2025 (MCP Authentication, Elicitations/sampling), 18.2 Jan 2026 (NuGet MCP server), 18.3 Feb 2026 (enterprise MCP governance), 18.4 Mar 2026 (custom agents, `find_symbol` tool), 18.5 Apr 2026 (agent skills, cloud agent integration, customizable shortcuts).
- **Visual Studio 2022** — continues to receive monthly servicing updates on the 17.14 branch. Newer Copilot primitives (prompt files, custom agents, agent skills, BYOK, workspace indexing) are not being back-ported to 17.x.

Track changes at the [Visual Studio 2026 release notes](https://learn.microsoft.com/en-us/visualstudio/releases/2026/release-notes) and the [GitHub Copilot changelog](https://github.blog/changelog/label/copilot/).

## Getting Started Checklist

1. Install or update to **Visual Studio 2026** (recommended) or **Visual Studio 2022 17.14** with the latest servicing release.
2. Confirm the **GitHub Copilot** component is installed via the Visual Studio Installer.
3. Sign in with a GitHub account that has a Copilot subscription (**profile icon → Add an account → GitHub**).
4. Open **Tools → Options → GitHub → Copilot → Copilot Chat** and enable:
   - **Enable custom instructions** (for `copilot-instructions.md` and `.instructions.md`).
   - **Enable Agent mode in the chat pane**.
   - Planning, if you want structured multi-step runs (optional, preview).
5. Add `.github/copilot-instructions.md` to the repository with the team's conventions. Use `/generateInstructions` as a starting point, then edit.
6. For teams that use VS Code too, place shared MCP configuration at `.mcp.json` (solution root) so both editors discover it.
7. Pilot agent mode on a small, well-defined task ("Add input validation to the `POST /orders` endpoint and update its tests") and review the checkpoint flow.
8. Review and approve the first few MCP tool invocations individually before granting solution-scoped approval.
9. On Visual Studio 2026, author a first prompt file for a high-frequency task (`/savePrompt` after a successful chat).
10. Document the adoption decisions — which modes are encouraged, which MCP servers are approved, which models are preferred — in the repository's contributing guide.

## Further Reading

- [Visual Studio Marketplace — GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilotvs)
- [Copilot feature matrix — Visual Studio](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=visualstudio)
- [Get started with GitHub Copilot completions](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-extension)
- [GitHub Copilot Chat for Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-chat)
- [Customize chat responses and set context](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-chat-context)
- [Get started with Copilot agent mode](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-agent-mode)
- [Use MCP servers in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/mcp-servers)
- [Built-in and custom agents](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents)
- [Admin controls for GitHub Copilot](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-admin)
- [GitHub Copilot app modernization for .NET](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-app-modernization/overview)
- [Visual Studio 2026 release notes](https://learn.microsoft.com/en-us/visualstudio/releases/2026/release-notes)
- [Visual Studio 2022 release history](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-history)
- [GitHub Copilot changelog](https://github.blog/changelog/label/copilot/)
- [awesome-copilot repository — curated agents and instructions](https://github.com/github/awesome-copilot)

---

[← Back to Foundations](../part-1-foundations.md)
