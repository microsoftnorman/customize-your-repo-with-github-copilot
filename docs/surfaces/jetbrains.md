# JetBrains IDEs

[← Where GitHub Copilot Runs](../where-github-copilot-runs.md) | [← Visual Studio](visual-studio.md) | [Next: Eclipse →](eclipse.md)

*Updated: April 22, 2026.*

---

## What This Surface Is

JetBrains IDEs are the strongest non-VS Code proof that the repository layer is portable across a major editor family.

That matters because JetBrains users do not want a second-rate adaptation. They want the same repository rules, prompts, and agent posture to follow them into IntelliJ IDEA, PyCharm, WebStorm, Rider, and the rest of the platform family.

## What Works Here Right Now

JetBrains is broad enough to matter, but still preview-heavy in exactly the places teams most want to standardize too early.

For current support state, use the [JetBrains slice of the Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=jetbrains). For installation and compatibility guidance, use the official [JetBrains setup page](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension?tool=jetbrains).

| Status | Primitives |
|--------|------------|
| Supported | MCP |
| Preview | Always-on Instructions, File-based Instructions, Prompts, Skills, Custom Agents |
| Not supported as a standard path | Hooks, Memory as an IDE-chat feature |

Plugin version matters. Treat preview rows as pilot-only until the exact IDE and plugin build the team relies on have been tested.

## Why It Matters

JetBrains is important because many teams standardize on it for language-specific depth and workflow consistency.

If the repository layer only worked well in VS Code, the portability story would be much weaker than this guide claims. JetBrains is where that claim is tested under real pressure.

## What Carries Over Well

JetBrains can consume a large portion of the authored layer, but the mature and preview rows should not be spoken about as if they were the same thing.

That shared layout is the main strategic win. The repository does not need a second JetBrains-specific tree just to express its Copilot rules.

## Where the Edges Still Are

The main caveat is maturity.

Some of the most important repository-driven surfaces in JetBrains are still preview-heavy, and support depth can vary by plugin build and IDE version. That does not make the model unusable. It means teams should test the exact behaviors they depend on rather than assuming perfect parity from the file layout alone.

That warning matters even more in PyCharm and Android Studio. Python notebooks, SQL workflows, Kotlin, Jetpack Compose, and Gradle-heavy projects can all benefit from the repository layer, but the team should verify the exact plugin build and remote-development shape it will actually use.

## What JetBrains Is Best At

JetBrains is a strong fit when the team wants:

- IntelliJ-platform project awareness,
- language-specific tooling depth,
- a serious agent and chat experience inside the IDE they already use,
- and the ability to share one repository customization story across multiple JetBrains products.

This is especially valuable for mixed-language organizations where one repository strategy needs to serve several IDEs at once.

## What to Trust First

The safest operating model is simple:

- keep the always-on layer clean and high-value,
- use MCP when the integration itself is already supported,
- treat Prompts, Skills, and Custom Agents as version-pinned pilots,
- and test the actual workflow in the actual product, whether that is IntelliJ IDEA, PyCharm, WebStorm, Rider, or Android Studio.

For Python and data-stack teams, verify what portability means in practice for `.py`, `.ipynb`, `.sql`, and MCP-backed database workflows. For Android teams, verify Kotlin, Gradle, and Compose workflows in Android Studio rather than assuming generic IntelliJ guidance is enough.

## Where VS Code Still Wins

VS Code still matters as the reference authoring surface because it tends to get new customization capabilities first and exposes the full system more clearly.

The right way to interpret that is not "JetBrains is behind, so do not use it."

It is: author where visibility is best, then verify the consumer behavior where your team actually works.

## The Most Useful Operational Rule

For JetBrains teams, the repository itself should remain the source of truth.

That means:

- keep the `.github/` structure clean,
- avoid editor-specific duplication,
- and treat any preview-only gaps as support constraints, not as reasons to fork the customization model.

If the team needs stronger enforcement or more predictable automation than the current plugin build provides, use [GitHub Copilot CLI](copilot-cli.md) or the [Cloud Coding Agent](cloud-coding-agent.md) for that part of the workflow and keep the repository layer shared.

## The Short Version

JetBrains is one of the strongest demonstrations that GitHub Copilot customization can survive outside the VS Code ecosystem.

It is a serious runtime and authoring surface, but one that still rewards careful parity testing around newer primitives.

## Where to Read Next

- Read [Eclipse](eclipse.md) next for a surface where portability is more selective and the gaps matter more.
- Revisit [Prompts](../primitive-3-prompts.md) and [Custom Agents](../primitive-5-custom-agents.md) if the team wants to understand which authored surfaces are most likely to need parity testing in JetBrains.
