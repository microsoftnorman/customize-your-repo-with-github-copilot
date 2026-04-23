# Eclipse

[← Where GitHub Copilot Runs](../where-github-copilot-runs.md) | [← JetBrains IDEs](jetbrains.md) | [Next: Xcode →](xcode.md)

*Updated: April 22, 2026.*

---

## What This Surface Is

Eclipse is a legitimate GitHub Copilot surface, but not a full-fidelity one for the entire repository customization model.

For current setup and support detail, use the official [Eclipse installation page](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-extension?tool=eclipse) and the [Eclipse feature matrix view](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=eclipse).

That distinction is the key to using it well.

The guide should not pretend Eclipse users are excluded from the story. It also should not pretend the support matrix is symmetrical with VS Code.

## Why It Matters

Eclipse still matters in real organizations:

- Java shops,
- Spring-heavy teams,
- Eclipse-based enterprise distributions,
- and specialized environments built on the Eclipse platform.

If the guide is serious about portability, it has to explain what survives here and what does not.

## What Carries Over

The parts that carry over most usefully are:

- Always-on Instructions,
- MCP,
- Custom Agents on current builds,
- and the cloud-side knowledge that does not depend on one IDE's local implementation.

That means Eclipse can still benefit from a repository that teaches GitHub Copilot how the codebase works.

## Where the Gaps Matter

Eclipse is where the portability story becomes selective.

The biggest practical gaps are the ones that reduce fine-grained authored guidance:

- File-based Instructions are not there,
- Prompts are not there,
- Skills are not there,
- and Hooks are not there.

That changes how a team should author the repository layer if Eclipse is an important consumer.

## What This Means for Authoring

If Eclipse matters, the root `.github/copilot-instructions.md` carries more weight.

Rules that would normally be split into narrower path-based or procedural artifacts elsewhere may need to be expressed at a higher level so Eclipse users still get the important behavior. This is one of the clearest examples of why portability does not mean identical capability.

## What Eclipse Is Best At

Eclipse is best treated as a consumer surface for:

- broad repository conventions,
- MCP-backed augmentation,
- and interactive agent or chat use inside Eclipse-based workflows.

It is not the best place to define the most advanced version of the repository's customization system.

## The Main Caveat

Eclipse has enough support to matter, but enough gaps that teams should design consciously around them.

If a repository depends heavily on path-scoped instruction logic, prompt-file workflows, or skill packaging, another surface should own the authoring story while Eclipse consumes the subset it supports.

## The Short Version

Eclipse belongs in the portability conversation, but as a constrained consumer rather than a reference authoring environment.

The right question is not whether it supports GitHub Copilot at all. The right question is which parts of the repository teaching layer survive intact.

## Where to Read Next

- Read [Xcode](xcode.md) next for the narrowest IDE support story in this section.
- Revisit [Always-on Instructions](../primitive-1-always-on-instructions.md) if Eclipse support makes you reconsider how much guidance should live at the root of the repository.
