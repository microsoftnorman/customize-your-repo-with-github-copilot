# MCP (Model Context Protocol)

[← Custom Agents](primitive-5-custom-agents.md) | [Part II Overview](part-2-primitives.md)

---

## Overview

MCP (Model Context Protocol) provides external gateway capabilities for Copilot. While instructions, prompts, and custom agents provide Copilot with knowledge, MCP enables Copilot to take real actions and access live data from external systems.

**Loading:** Session start
**Best For:** External gateways

**Official docs:** [MCP servers](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)

**See it in action:** For a live demo, watch Connor Peet in [Extend Agents with MCP](https://www.youtube.com/watch?v=_g29UQjIAeI). For a real-world MCP integration, watch Reynald Adolphe and Viktor Gamov in [AI-Powered Kafka Development with Confluent + MCP](https://www.youtube.com/watch?v=KRBqLjRjX70).

**Scope:** This section covers how GitHub Copilot *consumes* MCP servers — configuration, tool discovery, and invocation. It does not cover MCP server security, authentication implementation, or building custom MCP servers. For those topics, see the [MCP specification](https://modelcontextprotocol.io).

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

For a comparison of instructions vs. MCP capabilities, see the [Instructions vs. MCP Comparison](#instructions-vs-mcp-comparison) table below.

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

**Additional fields for stdio servers:** `envFile` (path to .env file).

**The `dev` key:** For MCP servers under active development, use the `dev` object to specify a file watch pattern and enable debugging:

```json
{
  "servers": {
    "my-dev-server": {
      "type": "stdio",
      "command": "node",
      "args": ["dist/server.js"],
      "dev": {
        "watch": "src/**/*.ts",
        "debug": true
      }
    }
  }
}
```

**Input variables:** Use `${input:variableName}` to prompt the user for values at startup. This is useful for configuration that varies per developer:

```json
{
  "servers": {
    "database": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@example/db-mcp"],
      "env": {
        "DB_HOST": "${input:databaseHost}",
        "DB_PORT": "${input:databasePort}"
      }
    }
  }
}
```

When the server starts, VS Code prompts for `databaseHost` and `databasePort` values. Combine with `${env:VAR}` for secrets that should come from the environment.

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

**For HTTP (streamable) servers:**
```json
{
  "servers": {
    "streamable-server": {
      "type": "http",
      "url": "https://example.com/mcp",
      "headers": { "Authorization": "Bearer ${env:TOKEN}" }
    }
  }
}
```

The `http` transport uses the newer MCP streamable HTTP protocol. Use `sse` for servers that support Server-Sent Events, and `http` for servers that support the streamable HTTP transport.

### Keep Your Tool Count Low

Copilot performs best with fewer tools available. Each tool's name, description, and schema consumes context and increases decision complexity. **The hard limit is 128 tools per request, but fewer is better. Disable servers not actively in use to keep the tool list focused.**

**Only run the MCP servers you actually need:**

- Working on frontend? Disable database MCP servers.
- Not deploying to Azure? Turn off Azure MCP.
- Finished with Jira integration? Remove it from config.

```jsonc
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

For a detailed exploration with practical examples (Git, Jira, file operations, incident response), see [Skills vs. MCP Servers: When to Use Which](primitive-4-skills.md#skills-vs-mcp-servers-when-to-use-which).

### MCP in GitHub Copilot CLI

[GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) comes with the GitHub MCP server pre-configured, enabling interaction with GitHub.com resources — merging pull requests, creating issues, and managing repositories — directly from the terminal.

**Adding MCP servers in the CLI:**

1. Type `/mcp add` in an interactive session
2. Fill in the server details using Tab to navigate between fields
3. Press Ctrl+S to save

CLI-specific server configurations are stored in `~/.copilot/mcp-config.json` (or the location specified by `XDG_CONFIG_HOME`). The CLI uses the same JSON structure as VS Code's `mcp.json` for server definitions.

**Checking available MCP tools:** Type `/mcp` in interactive mode to see configured servers and their available tools.

**Shared configuration with VS Code:** Since the VS Code March 2026 releases, MCP servers configured in `.vscode/mcp.json` also work in Copilot CLI and Claude agent sessions automatically. The same configuration file serves all three surfaces — no separate setup required. Teams that maintain a workspace `mcp.json` get CLI and agent parity for free.

### Beyond Tools: Resources, Prompts, and Apps

MCP servers expose more than just tools. Three additional capability types extend what servers can provide:

#### MCP Resources

MCP servers can give direct access to **resources** — structured data that can be used as context in chat prompts. For example, a file system MCP server might expose files and directories, or a database MCP server might provide access to table schemas.

To add a resource from an MCP server to a chat prompt: select **Add Context** > **MCP Resources** in the Chat view, then choose a resource type.

Resources are useful when Copilot needs reference data without executing a tool call — schema definitions, configuration files, or documentation that informs the conversation.

#### MCP Prompts

MCP servers can provide preconfigured **prompts** for common tasks, invoked in chat as slash commands. The format is `/mcp.servername.promptname` — type `/` in the chat input to see available MCP prompts alongside regular prompt files and skills.

MCP prompts may request input parameters. They serve a similar purpose to prompt files but are defined and maintained by the MCP server rather than stored in the workspace.

#### MCP Apps (Interactive UI)

MCP Apps enable tools to return **interactive UI components** that render directly in chat. Instead of text-only responses, tools can display drag-and-drop lists, visualizations, forms, and other interactive elements.

When an MCP server supports apps, the UI appears inline in the chat conversation, enabling direct interaction to complete tasks more efficiently. This is particularly useful for tools that benefit from visual manipulation — reordering items, configuring settings, or reviewing structured data.

**See it in action:** For a live demo, watch Connor Peet in [Extend Agents with MCP](https://www.youtube.com/watch?v=_g29UQjIAeI).

### Tool Sets

As MCP server count grows, so does the list of available tools. **Tool sets** group related tools for easier management and reference. Instead of toggling individual tools on and off, select or reference an entire tool set.

Tool sets are defined alongside other tool configurations. Learn more about [creating and using tool sets](https://code.visualstudio.com/docs/copilot/agents/agent-tools#_group-tools-with-tool-sets).

### Sandbox MCP Servers

VS Code 1.111+ supports running local stdio MCP servers in a restricted sandbox on macOS and Linux. The sandbox limits file system and network access, reducing the risk of a malicious or buggy server affecting the host machine.

This is useful in two scenarios:

- **Evaluating untrusted servers** — Run a community MCP server in the sandbox before granting it full access. If it behaves well, promote it to unrestricted.
- **Enforcing security policies** — Teams can require sandbox mode for all non-approved MCP servers, limiting blast radius even if a server is compromised.

Sandbox mode is a VS Code-level feature, not part of the MCP protocol itself. It applies only to local stdio servers — HTTP servers connect over the network and are not sandboxed by this mechanism.

### Chat Customizations Editor (Preview)

VS Code 1.111+ includes a unified **Chat Customizations** editor that consolidates management of instructions, MCP servers, and other Copilot configuration in one place. The editor also lets teams browse MCP and plugin marketplaces directly from VS Code, making it easier to discover and add servers without editing JSON files manually.

Open it via Command Palette > **"Chat Customizations"**.

### Centrally Control MCP Access

Organizations can centrally manage access to MCP servers via GitHub policies. This enables administrators to:
- Restrict which MCP servers team members can use
- Enforce approved server lists across repositories
- Block unapproved external integrations

Learn more about [enterprise management of MCP servers](https://code.visualstudio.com/docs/enterprise/ai-settings#_configure-mcp-server-access).

### Synchronize MCP Servers Across Devices

With [Settings Sync](https://code.visualstudio.com/docs/configure/settings-sync) enabled, MCP server configurations can be synchronized across devices. To enable MCP server synchronization, run **Settings Sync: Configure** from the Command Palette and ensure **MCP Servers** is included in the list of synchronized configurations.

This maintains a consistent MCP environment across workstations — useful for developers who work from multiple machines.

---

## End-to-End Tutorial: Adding a GitHub MCP Server

This walkthrough covers every step from zero to a working GitHub MCP integration.

### Step 1: Create the Configuration File

Create `.vscode/mcp.json` in your workspace root:

```json
{
  "servers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_TOKEN}"
      }
    }
  }
}
```

### Step 2: Set the Environment Variable

Export your GitHub personal access token (requires `repo` scope):

**macOS/Linux:**
```bash
export GITHUB_TOKEN=ghp_your_token_here
```

**Windows (PowerShell):**
```powershell
$env:GITHUB_TOKEN = "ghp_your_token_here"
```

For persistence, add the variable to your shell profile or use VS Code's `envFile` field pointing to a `.env` file (which should be gitignored).

### Step 3: Start the Server

1. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Run **MCP: List Servers**
3. The GitHub server should appear — click **Start** if it isn't running
4. Verify the server shows a green status indicator

### Step 4: Use It

Open Copilot Chat and try:

> **💬 Try this prompt:**
>
> *What are the open issues labeled "bug" in this repository?*

Copilot discovers the GitHub MCP tools, calls the appropriate one, and returns live data from the GitHub API.

### Step 5: Combine with a Skill

For team-consistent workflows, pair the MCP server with a skill that encodes your conventions. See [Skills vs. MCP Servers](primitive-4-skills.md#skills-vs-mcp-servers-when-to-use-which) for the hybrid pattern.

---

[← Custom Agents](primitive-5-custom-agents.md) | [Next: Hooks →](primitive-7-hooks.md)
