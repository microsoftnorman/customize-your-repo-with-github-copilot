# GitHub Copilot SDK

[← Back to Guide](README.md) | [← Agentic Workflows](agentic-workflows.md) | [Next: GitHub Copilot Code Review →](code-review.md)

*Updated: April 22, 2026.*

---

## What This Page Covers

The Copilot SDK is the same agent runtime carried into application code.

For current API shape, language support, and preview status, use the official [GitHub Copilot SDK repository](https://github.com/github/copilot-sdk) rather than this chapter.

If Agentic Workflows are the GitHub-hosted form of remote execution, the Copilot SDK is the version a team embeds and owns directly.

That makes this page less about file formats and more about where the agent loop lives when the application, not GitHub or an editor, becomes the host.

## Why This Matters

The earlier chapters teach how to shape repository knowledge. The SDK chapter answers the next portability question:

**What if the team needs GitHub Copilot behavior in a surface GitHub does not already provide?**

Examples include:

- an internal developer portal,
- a CI helper service,
- a Slack or web-based engineering assistant,
- a platform workflow runner,
- or a custom evaluation and measurement tool.

This is where the runtime becomes an application concern instead of only a user-surface concern.

## How It Reuses the Primitive Layer

The strongest conceptual point here is continuity.

The SDK does not replace the repository-level teaching layer. It gives that layer another place to run.

That means the repo still benefits from:

- explicit instructions,
- packaged procedures,
- role definitions,
- and the same architectural clarity that makes local Copilot behavior better.

The host changes. The value of repository knowledge does not.

## What Changes When the Application Owns the Runtime

When a team uses the SDK, it is taking ownership of concerns that a built-in surface normally hides:

- tool definitions,
- session management,
- streaming,
- permissions,
- observability,
- and often authentication or BYOK strategy.

That means the SDK belongs to teams that are building a platform or product, not just configuring one.

## When the SDK Is the Right Tool

Use the SDK when the agent needs to live inside a custom application or service the team controls directly.

Good fits:

- internal developer tooling,
- custom operational assistants,
- bespoke workflow runners,
- organization-specific eval systems,
- or interfaces where the agent is a product capability rather than a feature in someone else's UI.

If the workflow fits naturally inside VS Code, GitHub Copilot CLI, the Cloud Coding Agent, or GitHub Actions, the SDK is usually unnecessary overhead.

## How It Differs from MCP

MCP extends what an existing agent can reach.

The SDK changes where the agent lives.

That is the cleanest distinction.

Use MCP when the surface already exists and just needs external tools.
Use the SDK when the team is building a new surface or runtime host.

Many mature systems will use both.

## How It Differs from Agentic Workflows

Agentic Workflows are repository automation inside GitHub's execution model.

The SDK is the choice for application-owned execution.

The split is not only technical. It is organizational:

- Agentic Workflows keep the workflow close to the repository.
- The SDK moves the runtime closer to product or platform code.

## Why This Page Stays High Level

The SDK is a fast-moving preview surface, and its API details belong in the official SDK materials rather than in a long-lived repository guide.

The [Getting Started guide](https://github.com/github/copilot-sdk/blob/main/docs/getting-started.md) is the best official next step once the architectural decision is made.

That is why this chapter is intentionally architectural. It should help a reader decide whether the SDK belongs in their solution space at all, not try to become a competing API reference.

## Supported Languages

| Language | Install | Package |
|----------|---------|---------|
| **Node.js / TypeScript** | `npm install @github/copilot-sdk` | [@github/copilot-sdk](https://www.npmjs.com/package/@github/copilot-sdk) |
| **Python** | `pip install github-copilot-sdk` | [github-copilot-sdk](https://pypi.org/project/github-copilot-sdk/) |
| **Go** | `go get github.com/github/copilot-sdk/go` | [github/copilot-sdk/go](https://github.com/github/copilot-sdk/tree/main/go) |
| **.NET** | `dotnet add package GitHub.Copilot.SDK` | [GitHub.Copilot.SDK](https://www.nuget.org/packages/GitHub.Copilot.SDK) |
| **Java** | Maven dependency | [github/copilot-sdk](https://github.com/github/copilot-sdk) |

## Example: Agent Runtime

The SDK exposes the same agent loop used by the Copilot CLI. Developers define tools and the runtime handles orchestration.

*API names and signatures may differ from the current SDK — consult the [SDK repository](https://github.com/github/copilot-sdk) for the latest reference.*

```typescript
import { CopilotAgent, defineTool } from '@github/copilot-sdk';
import fs from 'node:fs/promises';

const listFiles = defineTool({
  name: 'list_files',
  description: 'List files in a directory',
  inputSchema: {
    type: 'object',
    properties: {
      path: { type: 'string', description: 'Directory path' }
    },
    required: ['path']
  },
  execute: async ({ path }) => {
    const files = await fs.readdir(path);
    return { files };
  }
});

const agent = new CopilotAgent({
  tools: [listFiles],
  systemPrompt: 'You are a project scaffolding assistant.'
});

const response = await agent.run('Create a new TypeScript project with tests');
```

## Concrete Use-Case Scenarios

| Scenario | Example |
|----------|---------|
| **Internal developer tools** | A team portal that scaffolds projects or provisions environments |
| **CI/CD integration** | A pipeline step that triages build failures |
| **Custom chat interfaces** | A Slack bot delegating coding tasks to the Copilot runtime |
| **Platform engineering** | A self-service platform for infra changes described in natural language |

## The Most Useful Mental Model

The shortest useful explanation is this:

**The SDK is what teams use when they need the agent loop as an application building block rather than as a feature inside an existing GitHub Copilot surface.**

## Where to Read Next

- Read [GitHub Copilot Code Review](code-review.md) next for another environment that consumes repository knowledge without being a primitive.
- Revisit [MCP](primitive-6-mcp.md) if the line between extending an existing surface and embedding a new runtime is still unclear.
