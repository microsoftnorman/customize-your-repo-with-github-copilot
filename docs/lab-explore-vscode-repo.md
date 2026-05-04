# Lab: Explore How VS Code Configures GitHub Copilot

[← Back to Guide](../ReadMe.md) | [When to Customize (If Required)](when-to-customize.md)

*Updated: May 4, 2026.*

---

This hands-on lab walks through a pinned snapshot of the `microsoft/vscode` repository to see how the team that builds VS Code: a 15-year-old, 600K+ line TypeScript codebase: configures GitHub Copilot in real code. The point is not to copy their setup. The point is to inspect a working configuration and see what a minimalist, high-signal setup looks like at scale.

The lab is pinned to commit `81e19a693faea10313612a2f5e31f4e61b0f7f98`. That keeps the file names, counts, and examples stable even as the live VS Code repository continues to evolve.

**Prerequisites:** Git, VS Code, and the GitHub Copilot extension installed.

**Time:** 15–20 minutes. No building or compiling required.

---

## Step 1: Clone the Pinned Snapshot

The VS Code repo is large. A filtered, shallow checkout keeps this fast while still landing on the exact commit used by the lab:

```powershell
$commit = "81e19a693faea10313612a2f5e31f4e61b0f7f98"
git clone --filter=blob:none --no-checkout https://github.com/microsoft/vscode.git
cd vscode
git fetch --depth 1 origin $commit
git checkout $commit
code .
```

VS Code will open the workspace at the pinned commit. Wait for the file tree to populate.

---

## Step 2: Open the Always-on Instructions File

Open the file `.github/copilot-instructions.md`.

```text
.github/copilot-instructions.md
```

This is the single file that loads into GitHub Copilot Chat and agent interactions in this repository. Inline completions use a separate pipeline, so test instruction behavior in Chat or agent mode rather than ghost text.

### What to Notice

**It is roughly 150 lines long.** That is the entire always-on instruction set for one of the largest TypeScript projects in the world. Not 500 lines. Not 1,000. About 150.

**It is organized into four sections:**

| Section | What It Covers |
|---------|---------------|
| Project Overview | Architecture layers, root folders, where to find things |
| Validating TypeScript Changes | Build commands, compilation checks, test scripts |
| Coding Guidelines | Indentation (tabs), naming, strings, style, code quality |
| Learnings | A single entry about test assertion style |

**It does not explain TypeScript.** There is no section on how `async/await` works, how to write interfaces, or how to structure modules. The model already knows TypeScript. The instructions only cover what is specific to *this* codebase.

**It encodes decisions that would surprise a newcomer:**

- "We use tabs, not spaces": a deliberate choice that contradicts most TypeScript projects
- "NEVER use `npm run compile`": a trap that looks obvious but catches every new contributor
- "Use `IEditorService` to open editors instead of `IEditorGroupsService.activeGroup.openEditor`": a pattern that looks wrong but is correct here
- "Service dependencies MUST be declared in constructors": an architectural invariant

> 💬 **Try this prompt:**
> Open GitHub Copilot Chat and ask: "What are the coding conventions in this project?" Watch how the answer reflects the instructions file rather than generic TypeScript advice.

---

## Step 3: Explore the File-Based Instructions

Open the `.github/instructions/` directory in the Explorer panel, or list the files:

```text
.github/instructions/
```

The VS Code team uses approximately 15 file-based instruction files. Each one targets a specific area of the codebase:

| File | Purpose |
|------|---------|
| `accessibility.instructions.md` | Rules for accessible UI contributions |
| `chat.instructions.md` | AI feature gating rules |
| `disposable.instructions.md` | Disposable lifecycle patterns |
| `notebook.instructions.md` | Notebook editor conventions |
| `observables.instructions.md` | Observable pattern rules |
| `sessions.instructions.md` | Agent sessions window conventions |
| `telemetry.instructions.md` | Telemetry event naming |
| `tree-widgets.instructions.md` | Tree view component rules |

### The Minimalist Pattern

Open any one of these files. Notice how each file has a YAML frontmatter block with an `applyTo` glob pattern. That pattern determines *when* the file activates: only when the developer is working on matching files.

This is the key structural insight: **the always-on file stays small because topic-specific rules live in their own files and only load when relevant.** The context budget is not wasted on accessibility rules when the developer is editing the terminal, or on telemetry conventions when building a new tree widget.

---

## Step 4: Explore the Prompts

```text
.github/prompts/
```

The pinned VS Code snapshot has 17 reusable prompts: slash commands that any contributor can invoke:

| Prompt | What It Does |
|--------|-------------|
| `build-champ.prompt.md` | Guides build champion duties |
| `fix-error.prompt.md` | Structured error diagnosis workflow |
| `find-duplicates.prompt.md` | Finds duplicate issues |
| `implement.prompt.md` | Implementation planning |
| `plan-deep.prompt.md` | Deep planning mode |
| `plan-fast.prompt.md` | Quick planning mode |
| `setup-environment.prompt.md` | Environment bootstrapping |
| `update-instructions.prompt.md` | Self-tuning: updates the instructions files |

Notice `update-instructions.prompt.md`: the team has a prompt specifically for asking GitHub Copilot to improve its own configuration. That is the feedback loop from the guide, built directly into the repo.

> 💬 **Try this prompt:**
> Open a prompt file and read its contents. Notice how it references specific tools, skills, or workflows. These are not vague instructions: they are concrete procedures.

---

## Step 5: Explore Skills, Agents, and Hooks

### Skills (`.github/skills/`)

The pinned VS Code snapshot has 21 skills: packaged procedural knowledge:

| Skill | Domain |
|-------|--------|
| `accessibility` | Accessible UI validation |
| `auto-perf-optimize` | Performance workflow |
| `chat-perf` | Chat performance pipeline |
| `cpu-profile-analysis` | CPU profiling |
| `fix-ci-failures` | CI repair procedures |
| `fix-errors` | Error diagnosis patterns |
| `heap-snapshot-analysis` | Memory analysis |
| `hygiene` | Code hygiene checks |
| `memory-leak-audit` | Memory leak detection |
| `unit-tests` | Test authoring conventions |
| `update-screenshots` | Screenshot diffing |

### Agents (`.github/agents/`)

Three custom agents:

| Agent | Purpose |
|-------|---------|
| `data.md` | Data querying agent |
| `demonstrate.md` | Demo/Playwright automation |
| `sessions.md` | Agent sessions window |

### Hooks (`.github/hooks/`)

One hooks file:

```text
.github/hooks/hooks.json
```

The team uses hooks sparingly: a single JSON file for runtime enforcement.

---

## Step 6: Count the Primitives

Here is the full inventory of what this pinned 600K-line, 15-year-old codebase snapshot uses:

| Primitive | Count |
|-----------|-------|
| Always-on Instructions | 1 file, ~150 lines |
| File-based Instructions | ~15 files |
| Prompts | 17 files |
| Skills | 21 skills |
| Custom Agents | 3 agents |
| Hooks | 1 file |

### What This Tells You

**The always-on file is minimal.** It covers architecture, build validation, and coding style. Nothing else. No essays about TypeScript best practices. No duplicated lint rules. No generic advice.

**Complexity lives in the right places.** The heavy procedural knowledge (how to fix CI, how to analyze a heap snapshot, how to audit for memory leaks) is in skills, not crammed into a giant instructions file. Skills load only when invoked.

**File-based instructions handle the long tail.** Domain-specific conventions (accessibility, telemetry, notebooks) activate only when the contributor touches those files.

**The team trusts the model.** The instructions do not explain how TypeScript works. They explain how *this project* works. That is the entire philosophy: encode the delta between general knowledge and local knowledge.

---

## Step 7: Ask GitHub Copilot About the Repo

With the repo open in VS Code, try these prompts to see the configuration in action:

> 💬 **Try this prompt:**
> "How should I handle disposables in this codebase?"

GitHub Copilot should reference the disposable patterns from the instructions: `DisposableStore`, `MutableDisposable`, registering immediately after creation: rather than giving generic TypeScript advice.

> 💬 **Try this prompt:**
> "I want to add a new setting to the editor. Where should I start?"

Watch how the response references the layered architecture, `src/vs/editor/`, and the contribution model: all from the instructions file.

---

## Takeaways

1. **150 lines is enough** for a massive legacy codebase if those lines encode the right decisions.
2. **Structure beats volume.** Splitting topic-specific rules into file-based instructions keeps the always-on file focused.
3. **Skills carry the weight.** Complex procedural knowledge belongs in skills, not in a wall of instructions text.
4. **Trust the model.** Do not teach it the language. Teach it the project.

---

## Clean Up

When done exploring, delete the clone:

```powershell
cd ..
Remove-Item -Recurse -Force vscode
```

