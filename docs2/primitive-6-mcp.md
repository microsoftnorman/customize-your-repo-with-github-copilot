# Primitive 6: MCP

[← Back to The Eight Primitives](part-2-primitives.md) | [← Custom Agents](primitive-5-custom-agents.md) | [Next: Hooks →](primitive-7-hooks.md)

*Updated: April 22, 2026.*

---

## Where It Enters the Loop

MCP changes the loop at action selection and tool execution.

Instructions, Prompts, Skills, and Agents tell GitHub Copilot how to think. MCP changes what it can reach.

That is the central distinction to preserve. MCP is not more context. It is more capability.

## What This Primitive Is For

Use MCP when the task depends on systems outside the local workspace:

- issue trackers,
- GitHub APIs,
- databases,
- internal search services,
- browser automation,
- deployment systems,
- or any other tool surface the agent needs to call directly.

The question MCP answers is: "What real systems can the loop act on or inspect?"

## What This Looks Like in Practice

Without MCP, a prompt like "check the latest checkout failures and open the preview build" can only produce advice.

With MCP, the same request can become action:

- a GitHub server can inspect the issue or pull request,
- a browser server can open the preview deployment,
- and a database or internal API server can fetch the live context the agent needs.

That is the practical difference. MCP moves the loop from explanation to live reach.

## The Fastest Comparison That Matters

Instructions provide knowledge.

MCP provides reach.

If the repository says, "we use PostgreSQL," that is knowledge.
If the agent can actually query PostgreSQL, that is MCP.

That difference is large enough to change architecture, risk, and trust boundaries. This guide treats it as one of the cleanest dividing lines in the whole primitive set.

## Configuration Shape

In VS Code, repository-level MCP configuration usually lives in `.vscode/mcp.json`. User-level MCP configuration can also live in the developer profile. In remote development, a remote user configuration can run on the attached host instead of the laptop.

The current canonical references are VS Code's [Add and manage MCP servers](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) page, the [MCP configuration reference](https://code.visualstudio.com/docs/copilot/reference/mcp-configuration), and the [Model Context Protocol specification](https://modelcontextprotocol.io/).

That is the first boundary to keep straight: the file location is not the same thing as the execution location.

MCP servers can expose more than tools. In current VS Code guidance, a server can provide:

- tools for live actions,
- resources for read-only context,
- prompts for server-defined task templates,
- and apps for richer interactive UI inside chat.

That broader shape matters because the team is not only deciding what the agent can do. It is also deciding what live context enters the loop, which UI affordances appear, and which trust decisions users will have to make.

The operational details matter as much as the conceptual role. Bad instructions create poor output. Bad MCP configuration creates broken or risky capability.

## Local to What?

This is the part many teams get wrong on the first pass.

- In a normal local editor session, a local stdio server runs on the workstation.
- In a dev container, WSL session, SSH session, or Codespace, that same "local" server runs in the remote environment.
- In a GitHub-hosted Cloud Coding Agent flow, the runtime is GitHub-hosted. It cannot call a process running only on a developer laptop.

That is why reproducible MCP use depends on environment bootstrapping, not just on committing `.vscode/mcp.json`. The repo can describe the server. The runtime still has to be able to start it.

## The Smallest Working Path

Start with one server, one narrow task, and one verification step.

```json
{
	"servers": {
		"playwright": {
			"type": "stdio",
			"command": "npx",
			"args": ["-y", "@microsoft/mcp-server-playwright"]
		}
	}
}
```

Then verify three things in order:

1. The runtime can start the server.
2. The user has explicitly trusted the server.
3. GitHub Copilot can perform one narrow action, such as opening a known page and taking a screenshot.

If that fails, the first checks are not prompt quality. They are startup logs, missing runtime dependencies, trust state, and whether the server is running in the environment the agent actually controls.

For shell-first or automation-heavy teams, the same rule applies: script setup if needed, but validate the smallest safe tool call before assuming the workflow is now portable.

## Why It Feels Powerful So Quickly

Once the loop can reach live systems, the task stops being hypothetical.

The agent can:

- inspect real issues,
- query live data,
- interact with internal services,
- or verify behavior against external environments.

That is why MCP is often the point where teams first feel both the upside and the risk of agentic work at the same time.

## When to Use MCP Instead of a Skill

Use MCP when the missing piece is authenticated access or live system interaction.

Use a Skill when the missing piece is procedure, convention, or template.

Most serious integrations need both.

Example:

- MCP can connect to GitHub, Jira, or a database.
- A Skill can encode how the team triages issues, formats tickets, or interprets query results.

That pairing is one of the strongest recurring patterns in the current guide and in the local demo material.

## What Good MCP Use Looks Like

Good MCP use is narrow and intentional.

The team enables the systems the workflow actually needs, keeps secret handling explicit, and avoids flooding the loop with unnecessary tool descriptions.

That is why the current guide's advice to keep tool count low matters so much. More tools do not automatically make the loop smarter. They often make tool choice noisier.

Good segmentation usually follows three boundaries at once:

- trust boundary: which servers are safe to enable by default,
- runtime boundary: which servers can run locally, remotely, or only in cloud-hosted flows,
- audience boundary: which servers are for everyone, and which are for a smaller role such as release engineering or data operations.

That is a better architecture pattern than dumping every possible integration into one shared file.

## Trust Boundaries Matter Here More Than Anywhere Else

MCP is where prompt engineering stops being the whole conversation.

Once a server can expose live data or actions, the team needs to think about:

- credential scope,
- what the server is allowed to do,
- whether the output can contain prompt-injection content,
- and whether the workflow needs Hooks or infrastructure controls on top.

That is why MCP pairs naturally with both Skills and Hooks: one adds procedure, the other adds enforcement.

For enterprise rollout, the minimum control set is usually straightforward:

- separate dev, staging, and production access,
- keep server allowlists explicit,
- scope credentials to the narrowest environment and action set,
- classify which data may enter the prompt,
- and require a review path before a repo gains production-facing MCP reach.

For public repositories, add one more rule: `.vscode/mcp.json` is code-review-sensitive. It is capability-granting configuration, not passive documentation. Treat changes to it like changes to automation or deployment scripts.

## Surface Reality

`.vscode/mcp.json` is the primary repository path in VS Code. Other surfaces can support MCP without honoring the exact same repository setup flow.

That means cross-surface rollout should assume this sequence:

1. author the intended MCP contract in the repository,
2. verify how each target surface exposes or installs the server,
3. and document the fallback when the surface needs local or per-install setup.

For example, Xcode currently supports MCP, but it is still a local macOS surface with a narrower integration model. JetBrains and Visual Studio can use MCP, but the team should verify the exact plugin or IDE build they standardize on rather than assuming perfect VS Code parity from the file path alone.

## One Concrete Example

A strong real-world pattern is `MCP + procedure + guardrails`.

Example: a data team connects GitHub Copilot to a warehouse query server through MCP, uses a Skill to enforce how analysts frame and summarize production queries, and adds Hooks or external controls to block risky access paths. The same pattern works for frontend preview environments, release tooling, or issue triage. The shape stays constant: reach, procedure, enforcement.

## How It Composes with Other Primitives

| Primitive | Relationship |
|-----------|--------------|
| [Skills](primitive-4-skills.md) | Skills explain how to use the external capability consistently |
| [Custom Agents](primitive-5-custom-agents.md) | Agents define which role gets to use which reach |
| [Hooks](primitive-7-hooks.md) | Hooks constrain risky execution once the loop has real capability |
| [Agentic Workflows](agentic-workflows.md) | Workflows often consume the same MCP-style reach in a remote runtime |

## See It in Action

**See it in action:** [Extend Agents with MCP](https://www.youtube.com/watch?v=_g29UQjIAeI&t=33s) — Connor Peet demos MCP extending the agent loop with external tools, resources, and asynchronous tasks.

## Configuring MCP Servers

Start with the built-in MCP commands instead of hand-authoring `mcp.json`. The file has strict syntax for transport types, environment variable substitution, and secret references. VS Code ships built-in commands that scaffold servers correctly:

- **MCP: Add Server** (Command Palette) walks through adding a server interactively
- **MCP: Open User Configuration** opens `~/.vscode/mcp.json` for user-level servers
- **MCP: Open Workspace Folder Configuration** opens `.vscode/mcp.json` for repo-level servers

> 💬 **Try this prompt:**
> "Add a GitHub MCP server to `.vscode/mcp.json` using the official `@modelcontextprotocol/server-github` package over stdio. Read the token from the `GITHUB_TOKEN` environment variable so it is not committed."

**Workspace configuration (`.vscode/mcp.json`):**

```json
{
  "servers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github@2026.4.0"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_TOKEN}"
      }
    }
  }
}
```

Pin to a specific version. Unpinned `npx -y <package>` is a supply-chain risk.

**HTTP server:**

```json
{
  "servers": {
    "remote-server": {
      "type": "http",
      "url": "https://example.com/mcp",
      "headers": { "Authorization": "Bearer ${env:TOKEN}" }
    }
  }
}
```

**Variable syntax reference:**

| Syntax | Where | Resolves To |
|--------|-------|-------------|
| `${env:VAR}` | Workspace / user MCP | Local environment variable |
| `${env:VAR:-default}` | Workspace / user MCP | Environment variable with fallback |
| `${input:name}` | Workspace / user MCP | Prompts the user once per session |
| `${{ secrets.NAME }}` | Cloud agent custom-agent YAML | Repository `copilot` environment secret |
| `${{ vars.NAME }}` | Cloud agent custom-agent YAML | Repository `copilot` environment variable |

## Credential Management

- **Never hardcode secrets in `mcp.json`.** Use `${env:VAR_NAME}` for environment variables.
- **Use `.env` files for local development.** Point to them with the `envFile` field. Add `.env` to `.gitignore`.
- **Rotate credentials on a schedule.** Treat MCP server tokens like any other service credential.
- **Limit token scope.** Create tokens with the minimum permissions the server needs. A read-only GitHub token limits blast radius.

## Security: Tool Output and Prompt Injection

MCP tools return content that enters the model's context. That content can carry instructions — intentional or adversarial — that try to steer the agent.

Practical defenses:

- Treat tool output as untrusted input.
- Pin servers to specific versions and review updates.
- Prefer scoped tokens.
- Sandbox untrusted stdio servers (VS Code 1.111+, macOS and Linux).
- Do not echo tool output verbatim into security decisions.

## End-to-End Tutorial: GitHub MCP Server

### Step 1: Create the configuration

Create `.vscode/mcp.json` pinned to a specific version:

```json
{
  "servers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github@2026.4.0"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_TOKEN}"
      }
    }
  }
}
```

### Step 2: Create a narrowly scoped token

Create a [fine-grained personal access token](https://github.com/settings/personal-access-tokens/new):

- Scope to only the specific repositories the agent needs
- Grant the minimum permissions for the task (read-only if possible)
- Set an expiration

### Step 3: Export the token

```bash
export GITHUB_TOKEN="github_pat_..."
```

Or add to a `.env` file referenced by `envFile` in the server config.

### Step 4: Trust and verify

Open VS Code, reload the window, and check the MCP output channel. The server should start and list its tools. Run one narrow operation to confirm connectivity.

## MCP in GitHub Copilot CLI

The CLI comes with the GitHub MCP server pre-configured. Type `/mcp` in interactive mode to see configured servers and their tools. Add servers with `/mcp add`. CLI-specific configs are stored in `~/.copilot/mcp-config.json`.

Since the VS Code March 2026 releases, MCP servers configured in `.vscode/mcp.json` also work in Copilot CLI sessions. The same file serves both surfaces.

## Where to Read Next

- Read [Hooks](primitive-7-hooks.md) next for the enforcement layer that becomes more important once the loop has real reach.
- Read [Code Review](code-review.md) and [Agentic Workflows](agentic-workflows.md) later to see where the same repository knowledge gets reused in other runtimes.
