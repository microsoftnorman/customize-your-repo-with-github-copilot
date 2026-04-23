# GitHub Copilot Cloud Agent

[← Back to Foundations](../part-1-foundations.md)

*Updated: April 22, 2026 · Validated against VS Code 1.116 and GitHub Copilot docs as of April 16, 2026. The cloud agent is a continuously-updated server-side service, so always cross-check the [official docs](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent) for the latest capabilities.*

---

The [Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent) (formerly **Copilot coding agent**) runs on GitHub's infrastructure, not in any IDE. Start a task from the **Agents panel** on [github.com/copilot/agents](https://github.com/copilot/agents), assign a GitHub issue to Copilot, or mention `@copilot` on an issue or PR. The agent spins up an ephemeral GitHub Actions-powered environment, clones the repo, reads your customization primitives, explores the code, makes changes on a branch, and optionally opens a pull request for human review.

**Official docs:** [About Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)

**Code to study:** [GitHub Copilot CLI repository](https://github.com/github/copilot-cli) and [GitHub Copilot SDK repository](https://github.com/github/copilot-sdk) for the closest public agent-runtime code and examples.

**See it in action:** [A Unified Agent Experience](https://www.youtube.com/watch?v=YmpjvZ3xkx8&t=402s) — VS Code Team demos starting a cloud session from VS Code, letting it run remotely, and reviewing the resulting PR back in the editor.

## How It Works

The cloud agent reads all the customization primitives in this guide (`copilot-instructions.md`, skills, hooks, custom agents, and Copilot Memory) every time it works on a task. The quality of the repo's configuration directly determines the quality of the agent's output.

### What It Can Do

Official capabilities (per [About Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)):

- Research a repository
- Create implementation plans
- Fix bugs
- Implement incremental new features
- Improve test coverage
- Update documentation
- Address technical debt
- Resolve merge conflicts

### Research, Plan, Iterate

As of April 1, 2026, the Agents panel on github.com supports an end-to-end [research → plan → iterate](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/research-plan-iterate) flow **within a single session**. The agent doesn't auto-open a PR until you click **Create pull request**. These phases are prompted in natural language, not toggled as discrete modes:

| Phase | How to invoke | Outcome |
|-------|---------------|---------|
| **Deep research** | Open the Agents panel and ask a question (e.g., *"Investigate performance issues in this app."*) | Read-only grounded findings report; no file changes |
| **Planning** | Follow up with *"Create a plan to implement the most impactful performance improvements."* | Structured plan you can iterate on with follow-up prompts |
| **Iteration** | Ask *"Implement the plan we agreed upon."* The agent pushes commits to a `copilot/BRANCH-NAME` branch | Diff you can review, request refinements on, or finalize as a PR |

To skip straight to a PR (the pre-April behavior), include "Create a pull request to …" in the initial prompt, assign an issue to Copilot as the assignee, or mention `@copilot` on an existing PR. Research/plan/iterate is **GitHub.com only**. Integrations (Azure Boards, Jira, Linear, Slack, Teams) only support direct PR creation.

**See it in action:** [A Unified Agent Experience](https://www.youtube.com/watch?v=YmpjvZ3xkx8&t=171s). Josh Spicer demos plan mode as a lightweight, read-only research and planning step before swapping into agent mode to implement the plan.

## Environment Setup

Define the agent's development environment in [`.github/workflows/copilot-setup-steps.yml`](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment):

```yaml
name: "Copilot Setup Steps"
on: workflow_dispatch

jobs:
  copilot-setup-steps:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4
      - name: Install dependencies
        run: npm ci
      - name: Build
        run: npm run build
      - name: Verify tests pass
        run: npm test
```

This file must be on the default branch. When the agent starts a task, it runs these steps first, so the environment matches what a human developer would use. Customize it for your language, package manager, and test framework.

## Key Characteristics

- **Autonomous but supervised.** The agent never merges or deploys; it opens PRs for human review.
- **Iterative.** Comment on the agent's PR (or continue the Agents-panel session) to request changes and it will keep refining.
- **Secure.** Runs in an isolated, ephemeral GitHub Actions container with scoped permissions.
- **Primitives-aware.** Reads instructions, skills, hooks, custom agents, and Copilot Memory on every task.
- **Single-repo, single-branch per run.** One task, one branch, one pull request. Cross-repo work must be split into multiple tasks.

## Entry Points

**See it in action:** [A Unified Agent Experience](https://www.youtube.com/watch?v=YmpjvZ3xkx8&t=402s). Josh Spicer demos starting a cloud session from the VS Code target picker, closing the laptop while it runs, and reviewing the resulting PR back in the editor.

| Entry point | Use it for |
|-------------|------------|
| **Agents panel / tab** on github.com | Deep research, planning, iterating before creating a PR |
| [github.com/copilot/agents](https://github.com/copilot/agents) | Standalone agents hub; same capabilities as the panel |
| Assigning **Copilot** as issue assignee | Autonomous runs that go directly to a PR |
| `@copilot` mention in issue or PR comment | Ad-hoc tasks and change requests on open PRs |
| **VS Code**, **GitHub Mobile**, **Copilot Chat** | Delegate cloud agent tasks without leaving your current surface. [GitHub Mobile](https://github.blog/changelog/2026-04-08-github-mobile-research-and-code-with-copilot-cloud-agent-anywhere) added full research/code flows in April 2026. |
| **Security campaigns** | Assign code-scanning alerts to the cloud agent to get auto-remediation PRs |
| **Integrations** (Jira, Linear, Azure Boards, Slack, Teams) | Create PRs directly from external tools (no research/plan phase) |

## Customization

The cloud agent respects the same primitives as the IDE agent, plus two cloud-specific forms:

| Primitive | Source |
|-----------|--------|
| **Custom instructions** | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, and organization-level instructions |
| **MCP servers** | Configured via the repo's [cloud-agent MCP configuration](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/extend-cloud-agent-with-mcp). Extend the agent with GitHub data, issue trackers, observability, or internal tools. |
| **Custom agents** | [Specialized agent personas](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents) (e.g., a frontend agent, a docs agent, a testing agent) with their own prompts and tools |
| **Hooks** | [Shell hooks](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-hooks) that run at key lifecycle points. Useful for validation, logging, security scanning, or workflow automation. |
| **Agent Skills** | [Packaged capabilities](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) following the agentskills.io specification |
| **Copilot Memory** (public preview, Pro/Pro+) | Automatic repository-level learning the agent carries between sessions. See [About agentic memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory). |

## Availability

Copilot cloud agent is available on Copilot **Pro**, **Pro+**, **Business**, and **Enterprise** plans in all GitHub-hosted repositories, except repositories owned by managed user accounts and repositories where it has been explicitly disabled. Business and Enterprise subscribers need an administrator-enabled policy before use; repository owners can opt individual repos out.

### Per-Organization Enablement

Enterprise administrators can enable the cloud agent on a per-organization basis using **custom properties** ([April 15, 2026](https://github.blog/changelog/2026-04-15-enable-copilot-cloud-agent-via-custom-properties)). Instead of a global on/off switch, admins set repository custom properties (e.g., `copilot-agent-enabled: true`) and create a policy that grants cloud agent access only to repositories matching those properties. Phased rollouts become practical: start with an initial team's repos, add repositories as the policy is validated, and maintain an allowlist of approved repositories.

### Model Selection

When using the cloud agent on github.com, users can select which underlying model powers the agent. Third-party models (including Claude and OpenAI models) are available alongside GitHub's default, and [model selection applies to Claude and Codex custom agents](https://github.blog/changelog/2026-04-14-model-selection-for-claude-and-codex-agents-on-github-com) per-session. Use a larger model for architectural refactors and a faster model for routine bug fixes.

### Enterprise Controls

The cloud agent runs in GitHub's infrastructure, so enterprises can govern it without touching developer machines.

| Control | Detail |
|---------|--------|
| **Commit signing** | As of April 3, 2026, the cloud agent supports signed commits on PRs it opens. Repositories with branch protection rules requiring signed commits now accept agent-authored PRs without exceptions. |
| **[Firewall allowlists](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall)** | Organization admins can restrict which network destinations the cloud agent's container can reach. Supply a list of allowed domains; anything outside the list is blocked at the network layer. |
| **Custom runners** | Enterprise customers can route cloud agent jobs to [**self-hosted runners**](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment#using-self-hosted-github-actions-runners) (large, GPU-equipped, or network-isolated fleets) instead of GitHub-hosted runners. This keeps source code and build artifacts inside the enterprise perimeter. |

### Merge Conflict Resolution

As of [April 13, 2026](https://github.blog/changelog/2026-04-13-fix-merge-conflicts-in-three-clicks-with-copilot-cloud-agent), the cloud agent can resolve merge conflicts on PRs it has opened. Comment `@copilot resolve conflicts` on a PR with a merge conflict and the agent will pull the latest base branch, rebase or merge, and push the resolved commits, respecting any conflict-resolution conventions encoded in `copilot-instructions.md` or skills.

### Costs

The cloud agent consumes **GitHub Actions minutes** (for the ephemeral environment) and **Copilot premium requests** (for the model calls). Within the monthly allowance for both, cloud agent work incurs no additional charge. See [GitHub Copilot billing](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-copilot/about-billing-for-github-copilot#allowance-usage-for-copilot-cloud-agent) for overage rules.

### Usage Metrics

Organization owners and enterprise administrators can track cloud agent adoption through the [Copilot usage metrics API](https://docs.github.com/en/copilot/concepts/copilot-usage-metrics/copilot-metrics), which now surfaces cloud agent active users, PR lifecycle metrics, and median time-to-merge for agent-authored PRs.

## Known Limitations

| Limitation | Impact |
|------------|--------|
| **One repo per task** | The agent cannot make changes across multiple repositories in a single run. Split cross-repo work into coordinated tasks. |
| **One branch, one PR per task** | Each task produces a single `copilot/…` branch and at most one PR. |
| **Default MCP scope is single-repo** | The bundled Copilot MCP server only sees issues and PRs in the task's repo. Configure [additional MCP servers](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/extend-cloud-agent-with-mcp) for broader context. |
| **Does not honor content exclusions** | Copilot [content exclusions](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot) do not apply to the cloud agent; it can see and modify excluded files. |
| **Incompatible rulesets block access** | Branch protection rules that restrict commit authors can block the agent. Add Copilot as a [ruleset bypass actor](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository#granting-bypass-permissions-for-your-branch-or-tag-ruleset) when needed. |
| **GitHub-hosted repos only** | Repositories stored on other platforms are not supported. |

## Release Cadence

The cloud agent is a **continuously-updated server-side service**. New capabilities ship weekly. Always check the official sources below for the latest features:

- [Changelog (Copilot label)](https://github.blog/changelog/label/copilot/): announcements and release notes
- [About Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent): authoritative capability reference
- [Cloud agent how-to articles](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent): tasks, customization, and integrations

## Hands-On Practice

GitHub maintains an interactive [Expand your team with Copilot cloud agent](https://github.com/skills/expand-your-team-with-copilot/) Skills exercise. Try the end-to-end flow on a disposable repo before rolling it out to your team.

## Further Reading

- [About Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)
- [Research, plan, and iterate on code changes](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/research-plan-iterate)
- [Extending the cloud agent with MCP](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/extend-cloud-agent-with-mcp)
- [About custom agents](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents)
- [Responsible use of Copilot cloud agent](https://docs.github.com/en/copilot/responsible-use/copilot-cloud-agent)
- [Agentic Workflows](../agentic-workflows.md): how primitives feed into autonomous work

---

[← Back to Foundations](../part-1-foundations.md)
