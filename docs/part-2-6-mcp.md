# MCP (Model Context Protocol)

[← Custom Agents](part-2-5-custom-agents.md) | [Part II Overview](part-2-primitives.md)

---

## Overview

MCP (Model Context Protocol) provides external gateway capabilities for Copilot. While instructions, prompts, and custom agents provide Copilot with knowledge, MCP enables Copilot to take real actions and access live data from external systems.

**Loading:** Session start
**Best For:** External gateways

> **Scope:** This section covers how GitHub Copilot *consumes* MCP servers — configuration, tool discovery, and invocation. It does not cover MCP server security, authentication implementation, or building custom MCP servers. For those topics, see the [MCP specification](https://modelcontextprotocol.io).

### How MCP Servers Expose Tools

MCP servers expose capabilities as **tools** that Copilot can discover and invoke. When Copilot starts a session with an MCP server configured, it queries the server for its available tools.

**The discovery flow:**

1. **Copilot connects** to the MCP server at session start
2. **Server responds** with a list of tools, each with:
   - Tool name (e.g., `create_issue`, `query_database`)
   - Description (helps Copilot decide when to use it)
   - Input schema (JSON Schema defining required parameters)
3. **Copilot adds tools** to its available capabilities
4. **During conversation**, Copilot matches user requests to tool descriptions
5. **When invoked**, Copilot constructs the parameters and calls the tool

**Example tool definition (from server's perspective):**

```json
{
  "name": "create_issue",
  "description": "Create a new GitHub issue in a repository",
  "inputSchema": {
    "type": "object",
    "properties": {
      "owner": { "type": "string", "description": "Repository owner" },
      "repo": { "type": "string", "description": "Repository name" },
      "title": { "type": "string", "description": "Issue title" },
      "body": { "type": "string", "description": "Issue body (markdown)" }
    },
    "required": ["owner", "repo", "title"]
  }
}
```

**What Copilot sees:** A tool called `create_issue` that it can call when users want to create GitHub issues. Copilot reads the description and schema to understand when and how to use it.

**What you see:** When Copilot decides to use the tool, it shows you the tool name and parameters before execution, giving you a chance to approve or modify.

### Instructions vs. MCP Capabilities

These two primitives are complementary:

- **Instructions** = What Copilot KNOWS ("Use parameterized queries")
- **MCP** = What Copilot CAN DO (Execute a database query and return results)

A configuration might include an instruction stating "always use our inventory API" alongside an MCP server that enables Copilot to actually call that API.

### Configuring MCP Servers

MCP servers are configured in dedicated `mcp.json` files:

**Workspace Configuration (.vscode/mcp.json):**
```json
{
  "servers": {
    "my-mcp-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@example/mcp-server"],
      "env": {
        "API_KEY": "${env:API_KEY}"
      }
    }
  }
}
```

**User Configuration:** Use Command Palette > **"MCP: Open User Configuration"** to edit `~/.vscode/mcp.json`.

**Additional fields for stdio servers:** `cwd` (working directory), `envFile` (path to .env file).

**For HTTP servers:**
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

### Keep Your Tool Count Low

Copilot performs best with fewer tools available. Each tool's name, description, and schema consumes context and increases decision complexity. **Aim for fewer than 70 total tools across all MCP servers.**

**Only run the MCP servers you actually need:**

- Working on frontend? Disable database MCP servers.
- Not deploying to Azure? Turn off Azure MCP.
- Finished with Jira integration? Remove it from config.

```json
{
  "servers": {
    "github": { ... },
    "azure": { "disabled": true }  // Not deploying to Azure this sprint
  }
}
```

Fewer tools means faster tool selection, less context consumed, and more accurate tool invocation.

### Example Use Cases

- **"What's the status of issue #234?"** → GitHub MCP
- **"Show me all users who signed up this week"** → Database MCP
- **"Test this API endpoint"** → Fetch MCP
- **"Take a screenshot of the login page"** → Puppeteer MCP

### Instructions vs. MCP Comparison

This is an important distinction:

| | Custom Instructions | MCP |
|-|---------------------|-----|
| **What** | Text context for AI | External tool access |
| **How** | Just knowledge | Actual capabilities |
| **Example** | "We use PostgreSQL" | Can query PostgreSQL |
| **Updates** | Manual | Real-time |

**Instructions provide knowledge. MCP provides capabilities.**

### MCP vs. Skills: Complementary, Not Competing

MCP servers and skills serve different purposes, but teams sometimes wonder which to use. The short answer: **use both together.**

- **MCP servers** provide *access* — authentication, API connections, external integrations
- **Skills** provide *knowledge* — templates, conventions, workflows, domain expertise

The best setups combine them: an MCP server handles "how to connect to Jira" while a skill handles "how our team formats Jira tickets."

**Quick guidance:**
- Need to authenticate or call external APIs? → MCP server
- Need to encode team conventions or workflows? → Skill
- Need both access AND conventions? → Use both

**Infrastructure and DevOps MCP servers** demonstrate how this pattern extends to operations workflows. If your team uses (or builds) MCP servers for infrastructure tools, the same skill-plus-MCP architecture applies:

| Use Case | MCP Server Would Provide | Pair With |
|----------|------------------------|-----------| 
| **Kubernetes** | Cluster state, pod logs, scaling, rollouts | Deployment skill for team conventions |
| **Terraform / IaC** | Plan, apply, state queries | Infrastructure review agent |
| **Cloud Provider** (Azure, AWS, GCP) | Resource management, metrics, cost data | Operations agent for infrastructure tasks |
| **Monitoring** (Datadog, Grafana, Prometheus) | Alerts, dashboards, metric queries | Triage skill for runbook-based workflows |

The same principle applies: the MCP server provides *access* to infrastructure APIs, while skills and instructions encode *how your team uses them*.

For a detailed exploration with practical examples (Git, Jira, file operations, incident response), see [Skills vs. MCP Servers: When to Use Which](part-2-4-skills.md#skills-vs-mcp-servers-when-to-use-which).

### MCP in GitHub Copilot CLI

[GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) comes with the GitHub MCP server pre-configured, enabling interaction with GitHub.com resources — merging pull requests, creating issues, and managing repositories — directly from the terminal.

**Adding MCP servers in the CLI:**

1. Type `/mcp add` in an interactive session
2. Fill in the server details using Tab to navigate between fields
3. Press Ctrl+S to save

Server configurations are stored in `~/.copilot/mcp-config.json` (or the location specified by `XDG_CONFIG_HOME`). The CLI uses the same JSON structure as VS Code's `mcp.json` for server definitions.

**Checking available MCP tools:** Type `/mcp` in interactive mode to see configured servers and their available tools.

This means MCP configurations benefit developers across both VS Code and the CLI. While the configuration files are stored in different locations (`.vscode/mcp.json` for VS Code, `~/.copilot/mcp-config.json` for CLI), teams can standardize on the same MCP servers across both surfaces.

---

[← Custom Agents](part-2-5-custom-agents.md) | [Next: Hooks →](part-2-7-hooks.md)
