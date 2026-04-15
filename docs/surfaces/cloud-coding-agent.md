# Copilot Cloud Coding Agent

[← Back to Foundations](../part-1-foundations.md)

---

The [Copilot cloud coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent) runs on GitHub's infrastructure — not in any IDE. Assign a GitHub issue to Copilot (or comment `@copilot` on an issue/PR), and it spins up a secure cloud environment, clones the repo, plans a solution, implements it, runs tests, and opens a pull request for human review.

## How It Works

The cloud agent reads all the customization primitives in this guide — `copilot-instructions.md`, skills, hooks, and memory — every time it works on a task. The quality of the repo's configuration directly determines the quality of the agent's output.

## Environment Setup

Define the agent's development environment in `.github/workflows/copilot-setup-steps.yml`:

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

This file must be on the default branch. When the agent starts a task, it runs these steps first — ensuring the environment matches what a human developer would use. Customize it for your language, package manager, and test framework.

## Key Characteristics

- **Autonomous but supervised** — the agent never merges or deploys; it opens PRs for human review
- **Iterative** — comment on the agent's PR to request changes and it will continue refining
- **Secure** — runs in an isolated container with scoped permissions
- **Primitives-aware** — reads instructions, skills, hooks, and memory on every task

## Availability

Available to Copilot Business and Enterprise plans, and to Pro/Pro+ for public repositories.

## Release Cadence

The cloud coding agent is a **server-side service** — updates deploy continuously without requiring any action from users. Monitor [github.blog/changelog](https://github.blog/changelog/label/copilot/) for announcements.

## Further Reading

- [About the Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)
- [Customizing the cloud agent environment](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-coding-agent)
- [Primitive 9: Agentic Workflows](../primitive-9-agentic-workflows.md) — How primitives feed into autonomous work

---

[← Back to Foundations](../part-1-foundations.md)
