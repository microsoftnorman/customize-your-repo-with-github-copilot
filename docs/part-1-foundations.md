# Part I: Foundations

[← Back to Guide](../ReadMe.md)

*Updated: April 22, 2026 · Validated against VS Code 1.117 and GitHub Copilot docs as of April 22, 2026.*

---

## What is GitHub Copilot?

**Official docs:** [GitHub Copilot](https://docs.github.com/en/copilot) · [Supported AI models](https://docs.github.com/en/copilot/reference/ai-models/supported-models) · [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)

[GitHub Copilot](https://github.com/features/copilot) is GitHub's platform for AI-assisted software development. In the simplest case, it answers questions and suggests code. In the more advanced case, it plans multi-step work, runs tools, edits files, and checks its own results. That second behavior is what this guide means by *agentic* (see [Key Terms](#key-terms) below). Copilot is not a single tool in a single editor. It is a platform that spans IDEs, the terminal, GitHub.com, CI/CD pipelines, and custom applications.

**See it in action:** [Agent Sessions Day Keynote](https://www.youtube.com/watch?v=2-Q_sdJ5H2c&t=0s) — Harald Kirschner frames Copilot as an agentic platform that spans IDEs, the terminal, GitHub.com, and CI/CD.

### What This Guide Teaches

Out of the box, Copilot is a generic platform. It knows how to write code, review PRs, and execute tasks. It knows nothing about *your* codebase, your conventions, your architecture, or your team's decisions. This guide covers the **eight customization primitives**, plus two platform extensions, that transform Copilot from a generic platform into one that understands your repository. Each primitive is a configuration file or integration that shapes what Copilot knows, how it behaves, and what it can do. Not sure where to start? The [Quick Decision Guide](part-3-reference.md#quick-decision-guide) maps common scenarios to the right primitive.

### Before You Go Deeper

Use this checklist before spending time on customization:

- Sign in to GitHub Copilot on one supported surface.
- Confirm that Chat works at least once in a real repository.
- Pick one host for the first pass. If the team is new, use VS Code for the examples in this guide.
- Make sure the repository already builds and tests without AI help. Customization works best when the repo has a stable baseline.

If Copilot is not installed or enabled yet, start at [github.com/features/copilot](https://github.com/features/copilot). Already familiar with GitHub Copilot? Skip the rest of this chapter and jump straight to [Part I: Why Customize →](part-1b-why-customize.md).

### Key Terms

These terms appear throughout the guide:

| Term | Meaning |
|------|---------|
| **Agentic** | A mode of AI operation where the model works autonomously. It plans steps, calls tools, runs commands, checks its own work, and iterates. Contrast with a single-turn assistant that answers one question and waits. "Agentic coding" is Copilot doing multi-step engineering work on your behalf. |
| **Agent** (three meanings; watch context) | (1) **Agentic mode**: Copilot operating autonomously, planning steps, calling tools, and iterating. (2) **Custom agent**: a user-authored `.agent.md` persona that configures Copilot's behavior, tools, and system prompt for a specific role. (3) **Copilot itself**, used as shorthand for the product (e.g., "the agent opened a PR"); most common when discussing the cloud coding agent or CLI. When ambiguity matters this guide uses the fuller form; elsewhere, context disambiguates. |
| **Primitive** | A configuration file type that customizes Copilot. Think of a primitive as a Lego brick: each one has a specific shape (file path + format) and a specific purpose (always-on rules, task templates, personas, etc.). This guide covers all eight primitives. |
| **Context window** | The total amount of text the model can consider at once. Instructions, code, and conversation all compete for this space. |
| **Inline suggestions** | Ghost text (autocomplete) that appears as you type. A separate pipeline from Copilot Chat. |
| **MCP** | [Model Context Protocol](https://modelcontextprotocol.io): a standard for connecting AI agents to external tools and data sources. |
| **`.github/`** | A conventional folder at the root of a Git repository that GitHub tools read for configuration. Copilot's customization primitives (instructions, prompts, skills, agents, hooks) live here so they travel with the repo and apply to everyone who clones it. |
| **`.vscode/`** | A per-project folder that holds VS Code configuration (settings, tasks, launch configs, MCP servers). Unlike `.github/`, files here are VS Code-specific and are often checked in to share project-level editor settings with the team. |
| **Command Palette** | VS Code's keyboard-driven command menu, opened with `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS). Type a command name (e.g., "Chat: Open Chat Customizations") to run it. Most of the Copilot actions described in this guide can be reached from here. |

**Important:** The customization primitives in this guide affect **Copilot Chat and agent interactions only**. They do not change inline suggestions (ghost text/autocomplete), which operate on a separate pipeline. For convention-aware code generation, use Chat-based interactions.

### Core Capabilities

Copilot assists developers across six interaction patterns:

**See it in action:** [How VS Code Builds with AI](https://www.youtube.com/watch?v=ee-obY-4rqk&t=0s). Pierce Boggan and Peng Lyu demo the VS Code team's real workflows across chat, agentic coding, and code review.

| Pattern | What It Does | Where It Runs |
|---------|-------------|---------------|
| **Code completion** | Predicts the next lines as you type. Ghost text for boilerplate, repetitive patterns, and finishing thoughts already started. | IDEs (VS Code, JetBrains, Eclipse, Visual Studio, Xcode) |
| **Chat** | A conversational interface for asking questions, generating code, explaining concepts, and working through problems interactively. | IDEs, GitHub.com |
| **Agentic coding** | Copilot plans multi-step tasks, calls tools, edits files, runs terminal commands, and iterates on results autonomously. | VS Code, Copilot CLI, cloud coding agent |
| **Code review** | Automated first-pass review of pull requests. Surfaces bugs, security issues, and convention violations, steered by the same [instruction files](primitive-2-file-based-instructions.md) you use in chat. See [Code Review](code-review.md) for the customization guide. | GitHub.com, GitHub Mobile, GitHub CLI, VS Code, Visual Studio, JetBrains, Xcode |
| **Agentic Workflows** | [Continuous AI](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/): coding agents run inside GitHub Actions on schedules, events, or on demand. Describe intent in Markdown; the agent executes it. Handles triage, docs sync, code simplification, test improvement, and reporting, all with sandboxed execution and human review before merge. | GitHub Actions (technical preview) |
| **Custom integration** | Embed the Copilot agent runtime in your own tools, platforms, and pipelines via the [Copilot SDK](copilot-sdk.md). | Your applications (Node.js, Python, Go, .NET, Java) |

**Agentic coding** is the most significant capability and where customization has the most impact. When Copilot operates as an agent, whether in VS Code, at the terminal, or running on GitHub's cloud infrastructure, the quality of instructions, skills, and guardrails in the repository directly determines the quality of the output.

The execution model behind that behavior deserves its own chapter. See [The Agent Loop](agent-loop.md) for the detailed mental model: how context is assembled, how tools and subagents fit, where hooks attach, and why model selection can vary across different parts of the same workflow.

For the subagent portion of that mental model, pair that chapter with [VS Code Insiders Podcast Episode 19: Subagents: Parallel Execution and Context Isolation](https://www.vscodepodcast.com/19) and the official @code video [Subagents: Parallel Execution and Context Isolation](https://www.youtube.com/watch?v=GMAoTeD9siU&t=0s). Harald Kirschner explains why delegated work stays useful only when the parent agent gets the result, not the entire exploratory trail.

Agentic coding has three permission levels:

| Level | Behavior |
|-------|----------|
| **Default** | Agent suggests actions; developer approves each one |
| **Bypass Approvals** | Skip confirmations for low-risk actions |
| **Autopilot** (preview) | Fully autonomous. Agent approves its own actions, retries on errors, and works until task completion. |

### Model Selection

Copilot supports **multi-model hot-swapping**: switch between models during a session to match the task. Popular models include:

| Model | Provider | Strengths |
|-------|----------|-----------|
| **Claude Opus 4.7** | Anthropic | Deep reasoning, multi-file refactors, nuanced code review |
| **Claude Sonnet 4.7** | Anthropic | Strong reasoning at lower cost; a good default for most tasks |
| **GPT-5.4** | OpenAI | Broad knowledge, strong type annotations, fast iteration |
| **GPT-5.4 mini** | OpenAI | Speed over depth; ideal for simple completions and quick questions |
| **GPT-5.3-Codex** | OpenAI | Code-specialized; optimized for generation and editing tasks |
| **Gemini 3.1 Pro** | Google | Concise, pragmatic solutions with large context windows |

This is not the full list. Copilot supports 20+ models across OpenAI, Anthropic, Google, and xAI, including code-specialized and fine-tuned variants. For the complete, up-to-date list with availability by plan and surface, see [Supported AI models in GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/supported-models).

Model selection matters more than most people realize. A frontier model with extended thinking will outperform an older or lighter model on complex tasks. **Thinking effort** is now configurable: control how deeply reasoning models think before responding, balancing response quality and latency.

Different models interpret the same instructions differently. Claude models tend toward thoroughness and may add defensive checks not explicitly requested. GPT models often produce more concise output and lean toward established patterns. Gemini models favor pragmatic solutions with minimal boilerplate. When switching models, review whether existing instructions produce the expected behavior. Some rules may need adjustment for a new model's defaults.

VS Code 1.117 adds **BYOK (Bring Your Own Key)** for Copilot Business and Enterprise. Organizations can let developers use their own approved model-provider keys in chat while keeping policy control on GitHub.com. BYOK applies to VS Code Chat and agents, not inline code completions.

**See it in action:** For a live demo of model configuration, watch Sandeep Somavarapu in [Bring Your Own Model in VS Code](https://www.youtube.com/watch?v=VBSVSxs16_I&t=0s).

### Plans

| Plan | Who It's For |
|------|-------------|
| **Copilot Free** | Individual developers; limited access to core features |
| **Copilot Pro / Pro+** | Individual developers; full access including agent mode, memory, and premium models |
| **Copilot Business** | Teams. Centralized management, policy controls, and org-wide customization |
| **Copilot Enterprise** | Large organizations. Enterprise governance, SSO, audit logging, **data residency in the US and EU** (as of April 13, 2026), and **FedRAMP High authorization** for US government workloads |

Not every primitive is available on every plan. The core customization files (instructions, file-based instructions, prompts, skills, custom agents, and MCP) work on all plans, including Free. Features with additional requirements:

| Feature | Availability |
|---------|--------------|
| **Hooks** | Pro, Pro+, Business, Enterprise |
| **[Memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory)** | Pro, Pro+ (on by default), Business, Enterprise (admin enables) |
| **Cloud Coding Agent** | Pro/Pro+ (public repos only), Business, Enterprise |
| **Agentic Workflows** | Technical preview; Business, Enterprise |

For the complete, up-to-date availability matrix, see the [Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix).

### Who Owns What?

The cleanest operating model is to split control by blast radius:

| Decision area | Best owner | Why |
|---------------|------------|-----|
| Plan selection, model allowlists, BYOK policy, Memory enablement | Enterprise or organization platform team | These choices affect cost, compliance, and what surfaces are even allowed to run |
| MCP approval rules, high-permission agent policy, hook rollout standards | Platform and security together | These are trust-boundary decisions, not local convenience settings |
| Repo instructions, prompts, skills, and role-specific agents | Repository owners or application teams | These encode local architecture, workflow, and review expectations |
| File-scoped conventions for subtrees in a monorepo | The team that owns those paths | The people closest to the code should own the narrowest rules |

That gives a practical cascade: central teams define the allowed envelope, then repositories fill it with local context.

### Enterprise Policy Hierarchy

Copilot configuration operates within a hierarchy of policies: **enterprise → organization → repository**. Each level can constrain the levels below:

- **Enterprise policies** restrict which models are available, whether Memory is enabled, and which Copilot features are accessible across all organizations
- **Organization settings** enforce or restrict specific primitives and control which MCP servers team members can use
- **Repository-level customization** operates within the boundaries set above. Instructions, prompts, skills, and agents are authored per-repo but subject to org and enterprise policies.

A repository cannot override an enterprise policy. If the enterprise disables Memory, no repo in any organization under that enterprise can use it. If the org restricts MCP server access to an approved list, repos in that org can only configure approved servers.

For details, see [Managing Copilot policies](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization) and [Enterprise AI controls](https://docs.github.com/en/admin/managing-github-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise).

---

## Where GitHub Copilot Runs

Copilot runs across many surfaces. The customization primitives in this guide are **file-based and IDE-agnostic**: they live in the repository, not in any specific editor's configuration. A `.github/copilot-instructions.md` file works regardless of which surface a developer uses.

| Surface | What It Is | Release Cadence |
|---------|-----------|-----------------|
| [**VS Code**](surfaces/vscode.md) | The primary IDE experience. Full primitive support, agent plugins, built-in since v1.116. | Weekly stable releases |
| [**Visual Studio**](surfaces/visual-studio.md) | Built for .NET teams. Agent mode, MCP, and custom instructions; prompt files and custom agents on current 2026 releases. | Monthly (tied to VS releases) |
| [**JetBrains**](surfaces/jetbrains.md) | IntelliJ, PyCharm, WebStorm, GoLand, Rider, Android Studio, and friends. | Multiple updates per week |
| [**Xcode**](surfaces/xcode.md) | For iOS and macOS developers. Code completion, Chat, agent mode, and MCP via a standalone app. | Via GitHub releases |
| [**Eclipse**](surfaces/eclipse.md) | Java enterprise teams. Open-source MIT plugin with MCP and agent mode. | ~Monthly |
| [**GitHub Copilot CLI**](surfaces/copilot-cli.md) | The full agentic experience in the terminal. GA since February 2026. | Weekly updates (auto-update) |
| [**Cloud Coding Agent**](surfaces/cloud-coding-agent.md) | Autonomous agent on GitHub's infrastructure. Assign issues; get PRs back. | Continuous (server-side) |
| [**Copilot SDK**](copilot-sdk.md) | Embed the agent runtime in your own tools and applications (public preview). | Preview; pin versions |

For a consolidated per-surface reference (primitive support, authoring UX, and the gotchas that bite teams in each IDE), see [Where GitHub Copilot Runs: IDE Surfaces](surfaces.md). For the authoritative, continuously-updated feature matrix, see the [GitHub Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix).

This guide uses VS Code for examples because it has the most complete primitive support and the clearest authoring and inspection workflow. If the audience is new to GitHub Copilot customization, start there first.

For most organizations, the rollout order should be: standardize in VS Code first, add GitHub Copilot CLI for terminal-heavy teams once trust boundaries are clear, then expand to the other IDEs where repository portability matters more than feature parity.

---

## Next: Why Customize

That covers what Copilot is and where it runs. The next chapter covers *why* customization matters, how to roll it out to a team, and how to measure whether the investment is paying off.

[Continue to Part I: Why Customize →](part-1b-why-customize.md)
