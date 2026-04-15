# Copilot SDK

[← Back to Foundations](../part-1-foundations.md)

---

The [Copilot SDK](https://github.com/github/copilot-sdk) (public preview) packages the same agent runtime that powers Copilot CLI and the cloud coding agent as libraries for Node.js/TypeScript, Python, Go, .NET, and Java. Use it to embed Copilot's agentic capabilities — tool invocation, multi-turn sessions, streaming, and reasoning — in custom tools, internal platforms, and CI pipelines.

## When to Use the SDK

The SDK is for teams building their own surfaces. If the use case fits inside VS Code, CLI, or GitHub Actions, use the existing primitives instead — they require zero custom code.

| Scenario | Example |
|----------|---------|
| Internal developer tools | A team portal that generates boilerplate or provisions environments |
| CI/CD integration | A pipeline step that triages build failures using agent intelligence |
| Custom chat interfaces | A Slack bot or web UI that delegates coding tasks to the agent runtime |
| Platform engineering | A self-service platform for infrastructure changes described in natural language |

## Release Cadence

The SDK is in **public preview** — expect breaking API changes between versions. Pin dependency versions and monitor the [SDK repository](https://github.com/github/copilot-sdk/releases) for updates.

## Getting Started

```text
npm install @github/copilot-sdk        # Node.js / TypeScript
pip install github-copilot-sdk          # Python
go get github.com/github/copilot-sdk/go # Go
dotnet add package GitHub.Copilot.SDK   # .NET
```

## Further Reading

- [Copilot SDK repository](https://github.com/github/copilot-sdk) — Source code, API reference, and examples
- [Copilot SDK public preview announcement](https://github.blog/changelog/2026-04-02-copilot-sdk-in-public-preview/)
- [Primitive 10: Copilot SDK](../primitive-10-copilot-sdk.md) — Full documentation in this guide

---

[← Back to Foundations](../part-1-foundations.md)
