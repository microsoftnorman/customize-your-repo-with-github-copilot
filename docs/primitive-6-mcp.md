# MCP (Model Context Protocol)

[← Custom Agents](primitive-5-custom-agents.md) | [Part II Overview](part-2-primitives.md)

*Updated: April 17, 2026 · Validated against VS Code 1.116 and GitHub Copilot docs as of April 16, 2026.*

---

## Overview

MCP (Model Context Protocol) connects Copilot to external tools and live data sources. Instructions, prompts, and custom agents give Copilot knowledge. MCP lets Copilot take real actions against systems like GitHub, databases, issue trackers, and internal APIs.

**Loading:** Session start
**Best For:** Calling external APIs and reading live data from outside systems
**Ownership:** MCP server configuration is typically owned by the **Platform / DevEx team** for production integrations (databases, internal APIs), and by **Security** for approved-server allowlists. Individual developers may add personal MCP servers via user configuration.

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

### Configuring MCP Servers

Sound off before you steer — let Copilot draft the configuration. `mcp.json` has strict syntax for transport types, environment variable substitution, and secret references; a single misquoted value or the wrong `type` and the server fails to start. VS Code ships built-in commands that scaffold servers correctly:

- **MCP: Add Server** (Command Palette) walks through adding a server interactively — pick the transport type, paste the command or URL, and VS Code writes the JSON.
- **MCP: Open User Configuration** opens `~/.vscode/mcp.json` for user-level servers.
- **MCP: Open Workspace Folder Configuration** opens `.vscode/mcp.json` for repo-level servers.
- In Chat, describe the server in plain English and let Copilot write the block; it knows the schema for stdio, http, and sse transports.

See [Don't Hand-Type Primitives — Let the Helmsman Repeat the Order](part-2-primitives.md#dont-hand-type-primitives--let-the-helmsman-repeat-the-order) for the rationale.

> **💬 Try this prompt:**
>
> *Add a GitHub MCP server to `.vscode/mcp.json` using the official `@modelcontextprotocol/server-github` package over stdio. Read the token from the `GITHUB_TOKEN` environment variable so it's not committed.*

> **💬 Try this prompt:**
>
> *Configure an HTTP MCP server pointing at our internal search service at `https://search.internal/mcp` with a bearer token from the `SEARCH_TOKEN` environment variable. Add it to the workspace `.vscode/mcp.json`, not the user config.*

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

**Variable syntax reference:** MCP configuration supports the following substitution patterns in `env` values and HTTP `headers`:

| Syntax | Where | Resolves To |
|--------|-------|-------------|
| `${env:VAR}` | Workspace and user MCP | Local environment variable |
| `${env:VAR:-default}` | Workspace and user MCP | Environment variable with a fallback default |
| `${input:name}` | Workspace and user MCP | Prompts the user once per session |
| `$VAR` / `${VAR}` | Cloud agent / custom-agent MCP | Environment variable from the Copilot environment (Claude Code compatibility) |
| `${VAR:-default}` | Cloud agent / custom-agent MCP | Environment variable with a fallback default |
| `${{ secrets.NAME }}` | Cloud agent custom-agent YAML | Secret from the repository's `copilot` environment |
| `${{ vars.NAME }}` | Cloud agent custom-agent YAML | Variable from the repository's `copilot` environment |

The `${{ secrets.* }}` and `${{ vars.* }}` forms intentionally mirror GitHub Actions syntax and are recognized inside `.github/agents/*.agent.md` frontmatter for MCP server configuration. For full details, see the [custom agents configuration reference](https://docs.github.com/en/copilot/reference/custom-agents-configuration#mcp-server-environment-variables-and-secrets).

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

**For SSE (Server-Sent Events) servers:**
```json
{
  "servers": {
    "sse-server": {
      "type": "sse",
      "url": "https://example.com/mcp/sse",
      "headers": { "Authorization": "Bearer ${env:TOKEN}" }
    }
  }
}
```

The `http` transport uses the newer MCP streamable HTTP protocol. Use `sse` for servers that expose the older Server-Sent Events transport.

### Keep Your Tool Count Low

Copilot performs best with fewer tools available. Each tool's name, description, and schema consumes context and increases decision complexity. **The hard limit is 128 tools per request, but fewer is better. Disable servers not actively in use to keep the tool list focused.**

**Only run the MCP servers you actually need:**

- Working on frontend? Disable database MCP servers.
- Not deploying to Azure this sprint? Turn off Azure MCP.
- Done with a Jira integration? Remove it from config.

```jsonc
{
  "servers": {
    "github": { ... },
    "azure": { "disabled": true }  // Not deploying to Azure this sprint
  }
}
```

Fewer tools means faster, more accurate tool selection.

### Example Use Cases

- **"What's the status of issue #234?"** → GitHub MCP
- **"Show me all users who signed up this week"** → Database MCP
- **"Test this API endpoint"** → Fetch MCP
- **"Take a screenshot of the login page"** → Puppeteer MCP

### Instructions vs. MCP Comparison

| | Custom Instructions | MCP |
|-|---------------------|-----|
| **What** | Text context for AI | External tool access |
| **How** | Just knowledge | Actual capabilities |
| **Example** | "We use PostgreSQL" | Can query PostgreSQL |
| **Updates** | Manual | Real-time |

**Instructions provide knowledge. MCP provides capabilities.**

### MCP vs. Skills: Complementary, Not Competing

MCP servers and skills serve different purposes, but the two are complementary. **Use both together.**

- **MCP servers** provide *access* — authentication, API connections, external integrations
- **Skills** provide *knowledge* — templates, conventions, workflows, domain expertise

The best setups combine them: an MCP server handles "how to connect to Jira" while a skill handles "how our team formats Jira tickets."

**Quick guidance:** Reach for an MCP server when you need to authenticate or call an external API. Reach for a skill when you need to encode team conventions or workflows. Most serious integrations use both.

**Infrastructure and DevOps MCP servers** demonstrate how this pattern extends to operations workflows. If your team uses (or builds) MCP servers for infrastructure tools, the same skill-plus-MCP architecture applies:

| Use Case | MCP Server Would Provide | Pair With |
|----------|------------------------|-----------| 
| **Kubernetes** | Cluster state, pod logs, scaling, rollouts | Deployment skill for team conventions |
| **Terraform / IaC** | Plan, apply, state queries | Infrastructure review agent |
| **Cloud Provider** (Azure, AWS, GCP) | Resource management, metrics, cost data | Operations agent for infrastructure tasks |
| **Monitoring** (Datadog, Grafana, Prometheus) | Alerts, dashboards, metric queries | Triage skill for runbook-based workflows |

The same principle applies: the MCP server provides *access* to infrastructure APIs, while skills and instructions encode *how your team uses them*.

For a detailed exploration with practical examples (Git, Jira, file operations, incident response), see [Skills vs. MCP Servers: When to Use Which](primitive-4-skills.md#skills-vs-mcp-servers-when-to-use-which).

### Out-of-the-Box MCP Servers (Cloud Agent)

The Copilot cloud agent ships with two MCP servers pre-configured, with no setup required:

| Server | Scope | What It Provides |
|--------|-------|------------------|
| `github/*` | Read-only by default, scoped to the source repository | Issues, PRs, code search, commits, workflow runs, and other GitHub resources. Reference the whole server with `github/*` in a custom agent's `tools` list, or target a specific tool with `github/<tool-name>`. |
| `playwright/*` | Localhost only | Browser automation for testing and verification tasks (navigate, screenshot, inspect). Useful for cloud-agent workflows that validate a running preview deployment. |

Both servers are processed before any custom-agent or repository-level MCP configuration, so custom servers can override or extend the defaults. Authentication tokens issued to these servers are **scoped to the source repository**. They cannot reach other repos or org resources.

```yaml
---
name: triage-agent
tools: ['github/*', 'read', 'search']
---
```

For the full list of tools each out-of-box server exposes and the most current scopes, see the [custom agents configuration reference](https://docs.github.com/en/copilot/reference/custom-agents-configuration#tool-names-for-out-of-the-box-mcp-servers).

### Security Considerations: Tool Output and Prompt Injection

MCP tools return content that is fed back into the model's context window. That content can carry instructions, intentional or adversarial, that try to steer Copilot away from the user's request. A support-ticket description, a fetched web page, or a free-text database field can all become **prompt-injection vectors**.

Practical defenses when consuming MCP tools:

- **Treat tool output as untrusted input.** The MCP protocol does not sign or validate tool responses. Anything a server returns is, from the model's perspective, additional context.
- **Pin servers to specific versions and review updates.** A compromised or updated server can change the meaning of a tool response without changing its name.
- **Prefer scoped tokens.** Give the server the minimum permissions it needs. A read-only GitHub token limits the blast radius of a successful injection.
- **Sandbox untrusted stdio servers.** On macOS and Linux, VS Code 1.111+ can run local stdio servers in a restricted sandbox (see [Sandbox MCP Servers](#sandbox-mcp-servers) below).
- **Don't echo tool output verbatim into approvals.** When a hook or agent uses tool output to make a security decision, extract structured fields rather than concatenating text.

For MCP's overall threat model and the spec's stance on authentication and trust, see the [MCP specification](https://modelcontextprotocol.io).

### MCP in GitHub Copilot CLI

[GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) comes with the GitHub MCP server pre-configured. From the terminal, Copilot can merge pull requests, create issues, and manage repositories against GitHub.com without any extra setup.

**Adding MCP servers in the CLI:**

1. Type `/mcp add` in an interactive session
2. Fill in the server details using Tab to navigate between fields
3. Press Ctrl+S to save

CLI-specific server configurations are stored in `~/.copilot/mcp-config.json` (or the location specified by `XDG_CONFIG_HOME`). The CLI uses the same JSON structure as VS Code's `mcp.json` for server definitions.

**Checking available MCP tools:** Type `/mcp` in interactive mode to see configured servers and their available tools.

**Shared configuration with VS Code:** Since the VS Code March 2026 releases, MCP servers configured in `.vscode/mcp.json` also work in Copilot CLI and Claude agent sessions. The same file serves all three surfaces, so teams that maintain a workspace `mcp.json` get CLI and agent parity for free.

### Beyond Tools: Resources, Prompts, and Apps

MCP servers expose more than just tools. Three additional capability types extend what servers can provide:

#### MCP Resources

MCP servers can give direct access to **resources** — structured data that can be used as context in chat prompts. For example, a file system MCP server might expose files and directories, or a database MCP server might provide access to table schemas.

To add a resource from an MCP server to a chat prompt: select **Add Context** > **MCP Resources** in the Chat view, then choose a resource type.

Resources are useful when Copilot needs reference data without executing a tool call — schema definitions, configuration files, or documentation that informs the conversation.

**See it in action:** [Extend Agents with MCP](https://www.youtube.com/watch?v=_g29UQjIAeI&t=230s) — Connor Peet demos a site-builder MCP server returning project metadata and a sketched layout as resources that flow directly into chat context.

#### MCP Prompts

MCP servers can provide preconfigured **prompts** for common tasks, invoked in chat as slash commands. The format is `/mcp.servername.promptname` — type `/` in the chat input to see available MCP prompts alongside regular prompt files and skills.

MCP prompts may request input parameters. They serve a similar purpose to prompt files but are defined and maintained by the MCP server rather than stored in the workspace.

#### MCP Apps (Interactive UI)

MCP Apps let tools return **interactive UI components** that render directly in chat. Instead of text-only responses, tools can display drag-and-drop lists, visualizations, or forms.

When an MCP server supports apps, the UI appears inline in the chat conversation and the user interacts with it directly. Reordering a task list, configuring settings, or reviewing structured data all land better as UI than as text.

**See it in action:** For a live demo, watch Connor Peet in [Extend Agents with MCP](https://www.youtube.com/watch?v=_g29UQjIAeI).

### Tool Sets

As MCP server count grows, so does the list of available tools. **Tool sets** group related tools for easier management and reference. Instead of toggling individual tools on and off, select or reference an entire tool set.

Tool sets are defined alongside other tool configurations. Learn more about [creating and using tool sets](https://code.visualstudio.com/docs/copilot/agents/agent-tools#_group-tools-with-tool-sets).

### Sandbox MCP Servers

VS Code 1.111+ supports running local stdio MCP servers in a restricted sandbox on macOS and Linux. The sandbox limits file system and network access, reducing the risk of a malicious or buggy server affecting the host machine.

This is useful in two scenarios:

- **Evaluating untrusted servers** — Run a community MCP server in the sandbox before granting it full access. If it behaves well, promote it to unrestricted.
- **Enforcing security policies** — Teams can require sandbox mode for all non-approved MCP servers, limiting blast radius even if a server is compromised.

Sandbox mode is a VS Code-level feature, not part of the MCP protocol itself. It applies only to local stdio servers. HTTP servers connect over the network and are not sandboxed by this mechanism.

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

This maintains a consistent MCP environment across workstations. Useful for developers who work from multiple machines.

---

## Credential Management

MCP servers frequently require API keys, tokens, or other credentials. Follow these practices to keep secrets out of version control:

- **Never hardcode secrets in `mcp.json`.** Use `${env:VAR_NAME}` to reference environment variables.
- **Use `.env` files for local development.** Point to them with the `envFile` field in your server configuration. Add `.env` to `.gitignore`.
- **Rotate credentials on a schedule.** Treat MCP server tokens like any other service credential. Rotate them on a cadence and revoke immediately if compromised.
- **Limit token scope.** Create tokens with the minimum permissions the MCP server needs. A GitHub MCP server that only reads issues does not need `repo` write access.
- **MCP server authors are responsible for secure credential handling.** The MCP protocol does not enforce credential security. It passes environment variables straight to the server process, so review how a server uses credentials before granting sensitive tokens.

For VS Code’s secret storage and environment variable handling, see [Variables reference](https://code.visualstudio.com/docs/reference/variables-reference).

---

## End-to-End Tutorial: Adding a GitHub MCP Server

This walkthrough covers every step from zero to a working [GitHub MCP](https://github.com/github/github-mcp-server) integration.

### Step 1: Create the Configuration File

Create `.vscode/mcp.json` in your workspace root. Pin the server package to a specific version so `npx` can't silently pull in a new release between sessions:

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

Replace `2026.4.0` with the version you actually verified. Check the package's releases page and update deliberately. Unpinned `npx -y <package>` is a supply-chain risk; the agent will run whatever the package currently resolves to.

### Step 2: Create a Narrowly Scoped Token

Create a [fine-grained personal access token](https://github.com/settings/personal-access-tokens/new) rather than a classic PAT:

- **Resource owner** — the account or org that owns the target repositories.
- **Repository access** — select only the specific repositories you need the agent to reach, not "All repositories."
- **Permissions** — grant only what your workflow requires. A read-only triage tool needs `Contents: Read` and `Metadata: Read`; a tool that opens issues adds `Issues: Read and write`. Avoid `Administration`, `Secrets`, and `Actions` unless the workflow truly requires them.
- **Expiration** — set the shortest expiration that fits your workflow; rotate when it expires.

Classic PATs with `repo` scope grant read/write access to every repository the user can see — a blast radius that rarely matches what an MCP server actually needs.

### Step 3: Set the Environment Variable

Export the token into your shell, **not** into `mcp.json`:

**macOS/Linux:**
```bash
export GITHUB_TOKEN=ghp_your_token_here
```

**Windows (PowerShell):**
```powershell
$env:GITHUB_TOKEN = "ghp_your_token_here"
```

For persistence, add the variable to your shell profile or use VS Code's `envFile` field pointing to a `.env` file.

**🚨 Don't commit the token.** Before your next commit:

1. Confirm `.env` (and any other local secret file) is listed in `.gitignore`.
2. Run `git status` — no `.env`, no `mcp.local.json`, no files containing `ghp_` or `github_pat_` should appear as tracked.
3. `grep -RniE 'ghp_[a-z0-9]{36}|github_pat_[a-z0-9_]{22,}' .` should return zero matches in your working tree.
4. If you use GitHub Codespaces, store the token as a [Codespaces secret](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces) scoped to the target repositories. It is injected as an environment variable and never touches the repo.

`${env:GITHUB_TOKEN}` is the only reference that should appear in `mcp.json`.

### Step 4: Start the Server

1. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Run **MCP: List Servers**
3. The GitHub server should appear. Click **Start** if it isn't running
4. Verify the server shows a green status indicator

### Step 5: Use It

Open Copilot Chat and try:

> **💬 Try this prompt:**
>
> *What are the open issues labeled "bug" in this repository?*

Copilot discovers the GitHub MCP tools, calls the appropriate one, and returns live data from the GitHub API.

### Step 6: Combine with a Skill

For team-consistent workflows, pair the MCP server with a skill that encodes your conventions. See [Skills vs. MCP Servers](primitive-4-skills.md#skills-vs-mcp-servers-when-to-use-which) for the hybrid pattern.

---

[← Custom Agents](primitive-5-custom-agents.md) | [Next: Hooks →](primitive-7-hooks.md)
