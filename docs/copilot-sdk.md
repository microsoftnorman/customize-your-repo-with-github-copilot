# GitHub Copilot SDK

[← Agentic Workflows](agentic-workflows.md) | [Part II Overview](part-2-primitives.md)

*Updated: April 16, 2026 · Validated against the [Copilot SDK public preview](https://github.blog/changelog/2026-04-02-copilot-sdk-in-public-preview/) as of this date.*

---

## Scope of This Page

This page is a **brief orientation** to the Copilot SDK — what it is, when to reach for it, and how it fits alongside the eight primitives. It is **not** a full SDK guide. API surface area, authentication flows, tool-definition schemas, streaming semantics, error handling, and language-specific idioms live in the official SDK documentation and change frequently during public preview.

For anything beyond "should I use this, and where does it sit in the stack," go straight to the source:

- [github.com/github/copilot-sdk](https://github.com/github/copilot-sdk) — Canonical repository, per-language READMEs, API reference, and examples
- [Public preview announcement](https://github.blog/changelog/2026-04-02-copilot-sdk-in-public-preview/) — Release notes and capability scope at launch
- [github.blog/changelog (Copilot label)](https://github.blog/changelog/label/copilot/) — Ongoing SDK updates

---

## Overview

The eight customization primitives shape Copilot where it already runs — in the editor, in the terminal, and on GitHub. The Copilot SDK lets developers bring that same agent runtime into their own applications and workflows.

The [Copilot SDK](https://github.com/github/copilot-sdk) is the production-tested runtime that powers [GitHub Copilot CLI](https://github.com/github/copilot-cli) and the Copilot cloud agent, packaged as libraries for five languages. Instead of building agent orchestration from scratch — tool routing, context management, permission handling, streaming — teams embed the runtime directly and focus on domain logic.

**Status:** Public preview (April 2, 2026)
**Best For:** Embedding Copilot agent capabilities in custom tools, internal platforms, CI pipelines, and developer workflows
**Location:** External dependency — installed via package managers, not configured in-repo

**Official docs:** [Copilot SDK](https://github.com/github/copilot-sdk) · [Changelog](https://github.blog/changelog/2026-04-02-copilot-sdk-in-public-preview/)

---

## When to Use the SDK

Use the Copilot SDK when the agent needs to run *outside* the surfaces GitHub already provides (VS Code, CLI, cloud agent, GitHub Actions).

| Scenario | Example |
|----------|---------|
| **Internal developer tools** | A team portal that generates boilerplate, runs migrations, or provisions environments using Copilot's reasoning |
| **CI/CD integration** | A pipeline step that uses agent intelligence to triage build failures or generate changelogs |
| **Custom chat interfaces** | A Slack bot or web UI that delegates coding tasks to the Copilot agent runtime |
| **Platform engineering** | A self-service platform where teams request infrastructure changes described in natural language |

If the use case fits inside VS Code, CLI, or GitHub Actions, use the existing primitives instead — they require zero custom code.

---

## Supported Languages

| Language | Install | Package |
|----------|---------|---------|
| **Node.js / TypeScript** | `npm install @github/copilot-sdk` | [@github/copilot-sdk](https://www.npmjs.com/package/@github/copilot-sdk) |
| **Python** | `pip install github-copilot-sdk` | [github-copilot-sdk](https://pypi.org/project/github-copilot-sdk/) |
| **Go** | `go get github.com/github/copilot-sdk/go` | [github/copilot-sdk/go](https://github.com/github/copilot-sdk) |
| **.NET** | `dotnet add package GitHub.Copilot.SDK` | [GitHub.Copilot.SDK](https://www.nuget.org/packages/GitHub.Copilot.SDK) |
| **Java** | Maven dependency | [github/copilot-sdk](https://github.com/github/copilot-sdk) |

---

## Key Capabilities

### Agent Runtime

The SDK exposes the same agent loop used by Copilot CLI: receive a prompt, reason about the task, invoke tools, iterate on results, and return a response. Developers define tools (functions the agent can call) and the runtime handles orchestration.

*The examples below are illustrative. API names and signatures may differ from the current SDK — consult the [SDK repository](https://github.com/github/copilot-sdk) for the latest API reference.*

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

### Multi-Turn Sessions

The SDK maintains conversation context across turns, enabling interactive workflows where the user and agent iterate on a task:

```typescript
const session = agent.createSession();

// First turn
const plan = await session.send('Analyze this codebase and suggest improvements');

// Follow-up turn with full context
const result = await session.send('Implement suggestion #3');
```

### Streaming

Token-by-token streaming supports responsive UIs where the agent's reasoning and output appear in real time:

```typescript
const stream = agent.stream('Explain the authentication flow in this codebase');

for await (const chunk of stream) {
  process.stdout.write(chunk.text);
}
```

### Permission Framework

Gate sensitive operations so the agent requests approval before executing them:

```typescript
const deployTool = defineTool({
  name: 'deploy',
  description: 'Deploy to staging',
  permissions: { requiresApproval: true },
  execute: async (params) => { /* ... */ }
});
```

### Bring Your Own Key (BYOK)

Enterprises can use their own API keys for supported model providers (OpenAI, Anthropic, Azure) instead of routing through GitHub's infrastructure. This gives teams control over cost, privacy, and provider selection:

```typescript
const agent = new CopilotAgent({
  tools: [/* ... */],
  modelProvider: {
    type: 'anthropic',
    apiKey: process.env.ANTHROPIC_API_KEY,
    model: 'claude-opus-4.7'
  }
});
```

### Observability

Built-in [OpenTelemetry](https://opentelemetry.io/) support provides distributed tracing across agent sessions — useful for debugging complex workflows and understanding tool invocation patterns in production.

---

## SDK vs. Other Primitives

The SDK complements the in-repo primitives rather than replacing them.

| Factor | Use In-Repo Primitives | Use the SDK |
|--------|----------------------|-------------|
| **Where it runs** | VS Code, CLI, cloud agent, GitHub Actions | Your own applications and services |
| **Configuration** | Markdown/JSON files in the repo | Code in your application |
| **Who builds it** | Anyone who can write Markdown | Developers building tools and platforms |
| **Authentication** | Handled by GitHub/VS Code | Your app manages auth (GitHub token or BYOK) |
| **Tool access** | VS Code tools, MCP servers, built-in skills | Custom tools you define in code |
| **Best for** | Customizing Copilot's existing surfaces | Embedding Copilot in new surfaces |

### SDK vs. MCP

MCP and the SDK solve different integration problems:

- **[MCP](https://modelcontextprotocol.io)** connects Copilot (running in VS Code or CLI) to external tools and data sources. The agent stays in its existing surface; MCP extends what it can reach.
- **The SDK** brings the agent runtime itself into a new application. The agent runs inside your code.

Use MCP when the agent needs to *call* your system. Use the SDK when your system needs to *be* the agent.

### SDK + Customization Primitives

SDK-powered applications can still benefit from the repo-level primitives. When the SDK agent operates on a repository, it can read `copilot-instructions.md`, discover skills, and apply the same conventions that guide Copilot in VS Code. The primitives travel with the repository — any agent that works on the code benefits from them.

---

## Getting Started

1. **Install the SDK** for your language (see table above)
2. **Authenticate** with a GitHub token (Copilot subscription required) or configure BYOK
3. **Define tools** — functions the agent can call during its reasoning loop
4. **Create an agent** with a system prompt and tool list
5. **Run or stream** a prompt and handle the response

For detailed setup, API reference, and examples, see the [Copilot SDK repository](https://github.com/github/copilot-sdk).

---

## Limitations

The Copilot SDK is in public preview. Current constraints:

| Limitation | Detail |
|-----------|--------|
| **Preview status** | APIs may change. Pin dependency versions and monitor the changelog |
| **Copilot subscription required** | Unless using BYOK, a Copilot Pro, Pro+, Business, or Enterprise subscription is needed |
| **Premium request quotas** | SDK calls consume Copilot premium requests. BYOK users pay their model provider directly |
| **No built-in VS Code tools** | The SDK doesn't include VS Code's file editing, terminal, or search tools — define your own equivalents |
| **Model availability** | Available models depend on your subscription tier and region |

---

## Further Reading

- [Copilot SDK repository](https://github.com/github/copilot-sdk) — Source code, API reference, and examples
- [Copilot SDK public preview announcement](https://github.blog/changelog/2026-04-02-copilot-sdk-in-public-preview/) — Changelog entry
- [MCP (Model Context Protocol)](primitive-6-mcp.md) — Connect Copilot to external tools (complementary to the SDK)
- [Agentic Workflows](agentic-workflows.md) — Run coding agents in GitHub Actions (alternative for CI/CD use cases)
- [Custom Agents](primitive-5-custom-agents.md) — Define specialized personas for the agent runtime

---

[← Agentic Workflows](agentic-workflows.md) | [Next: Part III - Reference →](part-3-reference.md)
