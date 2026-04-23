# Visual Studio

[← Where GitHub Copilot Runs](../where-github-copilot-runs.md) | [← Cloud Coding Agent](cloud-coding-agent.md) | [Next: JetBrains IDEs →](jetbrains.md)

*Updated: April 22, 2026.*

---

## What This Surface Is

Visual Studio is the deep .NET and C++ IDE surface for GitHub Copilot.

It is not trying to be VS Code. Its value is not breadth across every customization feature. Its value is that the agent lives next to the debugger, profiler, solution model, Test Explorer, MSBuild, and the Windows-heavy workflows many teams cannot replace.

## What Works Here Right Now

If a team is using Visual Studio tomorrow, the safest primitives to trust first are Always-on Instructions, Prompts, and MCP.

Use the [Visual Studio slice of the Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=visualstudio) to verify support status, and the official [Visual Studio installation guide](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension?tool=visualstudio) for current setup details.

| Status | Primitives |
|--------|------------|
| Supported | Always-on Instructions, Prompts, MCP |
| Preview | Custom Agents |
| Not supported as a normal Visual Studio path | Skills, Hooks, Memory as an IDE-chat feature |

That makes Visual Studio a serious runtime for repository customization, but not the broadest authoring surface.

## Why It Matters

Surface choice is not only about feature count. It is also about where the development work actually happens.

For teams building or maintaining large .NET, C++, desktop, or game-development systems, Visual Studio is often the real operating environment. A customization strategy that ignores that reality is not serious.

## What Carries Over

Visual Studio can consume a meaningful part of the same repository layer, especially the high-value repository guidance that lives near the repo root.

That means a repository authored with GitHub Copilot in mind can still teach useful behavior here, even if the authoring experience is not as broad as VS Code.

## What Makes Visual Studio Distinct

The biggest difference is that the surrounding IDE capabilities matter more than the customization story alone.

Visual Studio is the right surface when the task depends on:

- the solution and project model,
- Windows-specific tooling,
- .NET debugging and profiling,
- the C++ and MSVC toolchain,
- or enterprise workflows already centered on Visual Studio.

That context often outweighs the fact that VS Code moves faster on some customization surfaces.

## Where It Diverges from VS Code

Visual Studio is a strong consumer, but not the reference authoring environment for this guide.

The practical rule is simple:

- author the repository layer where support is strongest,
- verify how Visual Studio consumes that layer,
- and do not assume every newer VS Code authoring affordance has an equivalent here.

That is not a weakness in the guide. It is the reality of multi-surface Copilot adoption.

## The Practical Operating Model

For Visual Studio teams, one distinction matters immediately: repository root is where the durable customization lives, while `.sln` and `.csproj` files are how the work is organized inside the IDE.

That means the usual pattern is:

- keep GitHub Copilot guidance in the repo,
- open the real solution in Visual Studio,
- and verify that the guidance still helps inside Solution Explorer, MSBuild, NuGet restore, and Test Explorer workflows.

For .NET-heavy teams, a good first test is a multi-project solution with one API project, one domain library, and one xUnit or NUnit test project. Ask GitHub Copilot to make a change that crosses those boundaries and check whether the repo rules still hold inside the solution model.

For Python or SQL-heavy teams using Visual Studio, treat the repo layer as portable but verify the workflow in the actual tooling mix the team uses. Visual Studio is strongest when the surrounding Windows or .NET toolchain is the real reason the team is there.

## What It Is Best At

Visual Studio is strongest when repository guidance needs to operate inside mature IDE workflows for:

- enterprise .NET applications,
- C++ codebases,
- desktop and Windows UI stacks,
- and teams that already depend on Visual Studio's diagnostic and project tooling.

In those contexts, good repository customization reduces friction even if the files were originally authored elsewhere.

## The Main Caveat

If a team wants the broadest possible access to every primitive, plugin-style extension point, and emerging authoring workflow, VS Code remains the better control surface.

If a team wants GitHub Copilot where the .NET or C++ work actually lives, Visual Studio is the better runtime surface.

It is also effectively a local Windows surface. If the team needs stronger automation, runtime enforcement, or remote-first authoring, use [GitHub Copilot CLI](copilot-cli.md) or the [Cloud Coding Agent](cloud-coding-agent.md) as the fallback operating surface and keep the repository files as the durable source of truth.

## The Short Version

Choose Visual Studio when the surrounding IDE depth is the deciding factor.

Treat it as a serious consumer of repository knowledge and a credible MCP surface, not as the place where the full customization story is easiest to design from scratch.

## Where to Read Next

- Read [JetBrains IDEs](jetbrains.md) next for a different parity story: broader repository portability, but more preview-state edges.
- Revisit [File-based Instructions](../primitive-2-file-based-instructions.md) if the goal is path-specific guidance that should survive across both VS Code and Visual Studio.
