# Video Transcripts: @code (Visual Studio Code) YouTube Channel

Source: https://www.youtube.com/@code

This directory contains transcripts and metadata from VS Code YouTube channel videos relevant to this guide. These serve as primary source material for verifying features, discovering new information, and linking to demos.

## How to Use

The Doc Maintainer agent searches these files when running the **Check Video Sources** workflow. Each file contains:
- YAML frontmatter with video metadata (ID, URL, speakers, topics)
- Agenda/timestamps for navigating to specific demos
- Full transcript text (when populated)

## How to Add Transcripts

Use the repository script to fetch a full timestamped transcript and append it to a stub file:

```powershell
python scripts/fetch-transcript.py <video_id> references/transcripts/code-channel/<stub>.md
```

The script uses `youtube-transcript-api` (install once with `pip install youtube-transcript-api`) and writes one `[H:MM:SS] text` line per caption snippet under the `<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->` marker.

For videos without a prepared stub, create one with the standard frontmatter, then run the script to populate it.

## Index

### Week of Apr 14-20, 2026

| Date | Video | Topics | File |
|------|-------|--------|------|
| Apr 20 | [Inside The Agent Loop with Pierce Boggan](https://www.youtube.com/watch?v=ENxVTtLW_Bc) | Agent loop, sub-agents, model selection | 2026-04-20-inside-the-agent-loop-with-pierce-boggan.md |
| Apr 16 | [VS Code Terminal Agent Tool Updates](https://www.youtube.com/watch?v=0Eq8m63Z5J0) | Terminal agent, interactive input, agent sessions | 2026-04-16-vs-code-terminal-agent-tool-updates.md |
| Apr 9 | [VS Code Release Highlights - March 2026](https://www.youtube.com/watch?v=bZJAxvGmRO8) | Autopilot, browser debugging, chat customization | 2026-04-09-vs-code-release-highlights-march-2026.md |

### Week of Mar 31-Apr 6, 2026

| Date | Video | Topics | File |
|------|-------|--------|------|
| Apr 6 | [Introduction to Agent-First Development](https://www.youtube.com/watch?v=uu4sf8z9n8c) | Agent mode, prompts, tools, context | 2026-04-06-introduction-to-agent-first-development.md |
| Apr 6 | [Your first agent session in action](https://www.youtube.com/watch?v=WcN74XvZGes) | Agent sessions, permissions, tool calls | 2026-04-06-your-first-agent-session-in-action.md |
| Apr 6 | [Reviewing and controlling agent changes](https://www.youtube.com/watch?v=oFSJs6RnFt4) | Steering, checkpoints, reviews | 2026-04-06-reviewing-and-controlling-agent-changes.md |
| Apr 6 | [Agent sessions and where agents run](https://www.youtube.com/watch?v=0CsKOO7d35I) | Agent modes, cloud agents, parallel work | 2026-04-06-agent-sessions-and-where-agents-run.md |
| Apr 6 | [Review agents work with Agent Debug Logs and Chat Debug View](https://www.youtube.com/watch?v=aW2jlbbUREc) | Agent debug logs, troubleshooting | 2026-04-06-review-agents-work-with-agent-debug-logs-and-chat-debug-view.md |
| Apr 6 | [DEMO - Build your first app with agent mode](https://www.youtube.com/watch?v=hmfldW7dmgw) | Agent mode, plan mode, end-to-end demo | 2026-04-06-demo-build-your-first-app-with-agent-mode.md |
| Apr 1 | [Create and install an F1 inspired MCP Server in VS Code](https://www.youtube.com/watch?v=ZPaF_6mSp8I) | MCP, FastMCP, Python | 2026-04-01-create-and-install-an-f1-inspired-mcp-server.md |

### Week of Mar 16-22, 2026

| Date | Video | Topics | File |
|------|-------|--------|------|
| Mar 18 | [Multi-agent workflows in VS Code](https://www.youtube.com/watch?v=J5KTpq7hVn4) | Multi-agent workflows, parallel sessions | 2026-03-18-multi-agent-workflows-in-vs-code.md |
| Mar 16 | [Autopilot Mode with Justin Chen](https://www.youtube.com/watch?v=ne9l0S-JNE8) | Autopilot, approvals, workflows | 2026-03-16-autopilot-mode-with-justin-chen.md |

### Week of Mar 2-8, 2026

| Date | Video | Topics | File |
|------|-------|--------|------|
| Mar 6 | [GPT-5.4 just landed in VS Code!](https://www.youtube.com/watch?v=A8LiOBd5AgQ) | GitHub Copilot, model upgrades, planning | 2026-03-06-gpt-5-4-just-landed-in-vs-code.md |
| Mar 4 | [5 New VS Code Features for Smarter Agents](https://www.youtube.com/watch?v=MvwcWWp1NFs) | Skills, message steering, browser, hooks | 2026-03-04-5-new-vs-code-features-for-smarter-agents.md |

### Week of Feb 17-23, 2026

| Date | Video | Topics | File |
|------|-------|--------|------|
| Feb 23 | [Welcome to VS Code Live: Agent Sessions Day!](https://www.youtube.com/watch?v=njbObo0fyhM) | Agent Sessions Day kickoff, Copilot, Codex, Claude | 2026-02-23-welcome-to-vs-code-live-agent-sessions-day.md |
| Feb 23 | [Agent Sessions Day — Closing with Kai Maetzel](https://www.youtube.com/watch?v=0JPODfK8t5o) | Team workflows, model selection, prototyping | 2026-02-23-agent-sessions-day-closing-with-kai-maetzel.md |
| Feb 19 | [Agent Sessions Day](https://www.youtube.com/watch?v=tAezuMSJuFs) (full livestream) | All primitives, agents, MCP, skills, BYOM, CLI | 2026-02-19-agent-sessions-day.md |
| Feb 20 | [Agent Sessions Day — Keynote](https://www.youtube.com/watch?v=2-Q_sdJ5H2c) (segment) | Keynote, AI SDLC | — (segment of above) |
| Feb 20 | [How VS Code Builds with AI](https://www.youtube.com/watch?v=ee-obY-4rqk) (segment) | AI workflows, VS Code team practices | — (segment of above) |
| Feb 20 | [A Unified Agent Experience](https://www.youtube.com/watch?v=YmpjvZ3xkx8) (segment) | Agent sessions, cloud agents, Codex | 2026-02-19-unified-agent-experience.md |
| Feb 20 | [Extend Agents with MCP](https://www.youtube.com/watch?v=_g29UQjIAeI) (segment) | MCP, MCP Apps, interactive UI | 2026-02-19-extend-agents-with-mcp.md |
| Feb 20 | [The Browser in your Editor](https://www.youtube.com/watch?v=xjprgyqp9Z0) (segment) | Browser tool, DevTools, agent context | — (segment of above) |
| Feb 20 | [Bring Your Own Model in VS Code](https://www.youtube.com/watch?v=VBSVSxs16_I) (segment) | BYOM, BYOK, model selection | — (segment of above) |
| Feb 20 | [Customize your agents](https://www.youtube.com/watch?v=flpKLkZla2Q) (segment) | Custom agents, skills, instructions, prompts | 2026-02-19-customize-your-agents.md |
| Feb 20 | [Copilot CLI in VS Code](https://www.youtube.com/watch?v=_l3UO1oUoec) (segment) | CLI, terminal agent | 2026-02-19-copilot-cli.md |
| Feb 20 | [How we ship models](https://www.youtube.com/watch?v=nD1U_wggrQM) | Model evals, Copilot, reliability | 2026-02-20-how-we-ship-models.md |
| Feb 20 | [Live coding with Burke, Pierce, and Olivia](https://www.youtube.com/watch?v=MVwkFbYa1Xg) (segment) | Agent workflows, vibe coding | — (segment of above) |
| Feb 20 | [Let it Cook - This changes EVERYTHING](https://www.youtube.com/watch?v=uquSQY10AGM) | Latest Copilot updates | 2026-02-20-let-it-cook-everything.md |

### Week of Feb 10-14, 2026

| Date | Video | Topics | File |
|------|-------|--------|------|
| Feb 13 | [Let it Cook: Agent Steering, Hooks, CLI](https://www.youtube.com/watch?v=FjvtWeG6EEo) | Steering, queueing, hooks, CLI | 2026-02-13-let-it-cook-agent-steering.md |
| Feb 13 | [Kafka + MCP](https://www.youtube.com/watch?v=KRBqLjRjX70) | Real-world MCP, Confluent/Kafka | 2026-02-13-kafka-mcp.md |
| Feb 11 | [1.109 VS Code Release Highlights](https://www.youtube.com/watch?v=LGx8YieBjIA) | MCP Apps, skills, subagents, browser | 2026-02-11-vs-code-release-highlights-1-109.md |

### Week of Feb 3-9, 2026

| Date | Video | Topics | File |
|------|-------|--------|------|
| Feb 4 | [Multi-agent development in VS Code](https://www.youtube.com/watch?v=BsAHunfVwNs) | Multi-agent sessions, sub-agents, cloud agents | 2026-02-04-multi-agent-development-in-vs-code.md |
| Feb 9 | [Subagents: Parallel Execution and Context Isolation](https://www.youtube.com/watch?v=GMAoTeD9siU) | Sub-agents, context isolation, custom agents, model selection | 2026-02-09-subagents-parallel-execution-and-context-isolation.md |

## Topic Cross-Reference

Use this to find which transcripts cover specific guide sections:

| Guide Section | Relevant Transcripts |
|---------------|---------------------|
| Custom Agents | [Customize your agents](https://www.youtube.com/watch?v=flpKLkZla2Q) — Courtney Webster; [Subagents: Parallel Execution and Context Isolation](https://www.youtube.com/watch?v=GMAoTeD9siU) — Harald Kirschner; [Inside The Agent Loop with Pierce Boggan](https://www.youtube.com/watch?v=ENxVTtLW_Bc) — Pierce Boggan, James Montemagno |
| MCP | [Extend Agents with MCP](https://www.youtube.com/watch?v=_g29UQjIAeI) — Connor Peet; [Kafka MCP](https://www.youtube.com/watch?v=KRBqLjRjX70) — Reynald Adolphe, Viktor Gamov; [Create and install an F1 inspired MCP Server in VS Code](https://www.youtube.com/watch?v=ZPaF_6mSp8I) — Liam Conroy Hampton |
| Skills | [Customize your agents](https://www.youtube.com/watch?v=flpKLkZla2Q) — Courtney Webster; [5 New VS Code Features for Smarter Agents](https://www.youtube.com/watch?v=MvwcWWp1NFs) — Olivia Guzzardo McVicker |
| Hooks | [Let it Cook (Feb 13)](https://www.youtube.com/watch?v=FjvtWeG6EEo) — Pierce Boggan, James Montemagno; [5 New VS Code Features for Smarter Agents](https://www.youtube.com/watch?v=MvwcWWp1NFs) — Olivia Guzzardo McVicker |
| Foundations / AI SDLC | [Welcome to VS Code Live: Agent Sessions Day!](https://www.youtube.com/watch?v=njbObo0fyhM) — Kyle Daigle; [Agent Sessions Day — Closing with Kai Maetzel](https://www.youtube.com/watch?v=0JPODfK8t5o) — Kai Maetzel, James Montemagno; [Agent Sessions Day Keynote](https://www.youtube.com/watch?v=2-Q_sdJ5H2c) — Harald Kirschner; [How VS Code Builds with AI](https://www.youtube.com/watch?v=ee-obY-4rqk) — Pierce Boggan, Peng Lyu; [Introduction to Agent-First Development](https://www.youtube.com/watch?v=uu4sf8z9n8c) — Gwyneth Peña-Siguenza; [Inside The Agent Loop with Pierce Boggan](https://www.youtube.com/watch?v=ENxVTtLW_Bc) — Pierce Boggan, James Montemagno |
| Model Selection | [Bring Your Own Model in VS Code](https://www.youtube.com/watch?v=VBSVSxs16_I) — Sandeep Somavarapu; [How we ship models](https://www.youtube.com/watch?v=nD1U_wggrQM) — Visual Studio Code team; [GPT-5.4 just landed in VS Code!](https://www.youtube.com/watch?v=A8LiOBd5AgQ) — Olivia Guzzardo McVicker; [VS Code Release Highlights - March 2026](https://www.youtube.com/watch?v=bZJAxvGmRO8) — Reynald Adolphe; [Inside The Agent Loop with Pierce Boggan](https://www.youtube.com/watch?v=ENxVTtLW_Bc) — Pierce Boggan, James Montemagno |
| Prompts | [Introduction to Agent-First Development](https://www.youtube.com/watch?v=uu4sf8z9n8c) — Gwyneth Peña-Siguenza; [Reviewing and controlling agent changes](https://www.youtube.com/watch?v=oFSJs6RnFt4) — Gwyneth Peña-Siguenza; [DEMO - Build your first app with agent mode](https://www.youtube.com/watch?v=hmfldW7dmgw) — Gwyneth Peña-Siguenza |
| Sub-agents | [Subagents: Parallel Execution and Context Isolation](https://www.youtube.com/watch?v=GMAoTeD9siU) — Harald Kirschner; [Multi-agent development in VS Code](https://www.youtube.com/watch?v=BsAHunfVwNs) — Olivia Guzzardo McVicker; [Multi-agent workflows in VS Code](https://www.youtube.com/watch?v=J5KTpq7hVn4) — Kayla Cinnamon; [Inside The Agent Loop with Pierce Boggan](https://www.youtube.com/watch?v=ENxVTtLW_Bc) — Pierce Boggan, James Montemagno |
