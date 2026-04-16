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

### Week of Feb 17-20, 2026

| Date | Video | Topics | File |
|------|-------|--------|------|
| Feb 19 | [Agent Sessions Day](https://www.youtube.com/watch?v=tAezuMSJuFs) (full livestream) | All primitives, agents, MCP, skills, BYOM, CLI | 2026-02-19-agent-sessions-day.md |
| Feb 20 | [Agent Sessions Day — Keynote](https://www.youtube.com/watch?v=2-Q_sdJ5H2c) (segment) | Keynote, AI SDLC | — (segment of above) |
| Feb 20 | [How VS Code Builds with AI](https://www.youtube.com/watch?v=ee-obY-4rqk) (segment) | AI workflows, VS Code team practices | — (segment of above) |
| Feb 20 | [A Unified Agent Experience](https://www.youtube.com/watch?v=YmpjvZ3xkx8) (segment) | Agent sessions, cloud agents, Codex | 2026-02-19-unified-agent-experience.md |
| Feb 20 | [Extend Agents with MCP](https://www.youtube.com/watch?v=_g29UQjIAeI) (segment) | MCP, MCP Apps, interactive UI | 2026-02-19-extend-agents-with-mcp.md |
| Feb 20 | [The Browser in your Editor](https://www.youtube.com/watch?v=xjprgyqp9Z0) (segment) | Browser tool, DevTools, agent context | — (segment of above) |
| Feb 20 | [Bring Your Own Model in VS Code](https://www.youtube.com/watch?v=VBSVSxs16_I) (segment) | BYOM, BYOK, model selection | — (segment of above) |
| Feb 20 | [Customize your agents](https://www.youtube.com/watch?v=flpKLkZla2Q) (segment) | Custom agents, skills, instructions, prompts | 2026-02-19-customize-your-agents.md |
| Feb 20 | [Copilot CLI in VS Code](https://www.youtube.com/watch?v=_l3UO1oUoec) (segment) | CLI, terminal agent | 2026-02-19-copilot-cli.md |
| Feb 20 | [Live coding with Burke, Pierce, and Olivia](https://www.youtube.com/watch?v=MVwkFbYa1Xg) (segment) | Agent workflows, vibe coding | — (segment of above) |
| Feb 20 | [Let it Cook - This changes EVERYTHING](https://www.youtube.com/watch?v=uquSQY10AGM) | Latest Copilot updates | 2026-02-20-let-it-cook-everything.md |

### Week of Feb 10-14, 2026

| Date | Video | Topics | File |
|------|-------|--------|------|
| Feb 13 | [Let it Cook: Agent Steering, Hooks, CLI](https://www.youtube.com/watch?v=FjvtWeG6EEo) | Steering, queueing, hooks, CLI | 2026-02-13-let-it-cook-agent-steering.md |
| Feb 13 | [Kafka + MCP](https://www.youtube.com/watch?v=KRBqLjRjX70) | Real-world MCP, Confluent/Kafka | 2026-02-13-kafka-mcp.md |

## Topic Cross-Reference

Use this to find which transcripts cover specific guide sections:

| Guide Section | Relevant Transcripts |
|---------------|---------------------|
| Custom Agents | [Customize your agents](https://www.youtube.com/watch?v=flpKLkZla2Q) — Courtney Webster |
| MCP | [Extend Agents with MCP](https://www.youtube.com/watch?v=_g29UQjIAeI) — Connor Peet; [Kafka MCP](https://www.youtube.com/watch?v=KRBqLjRjX70) — Reynald Adolphe, Viktor Gamov |
| Skills | [Customize your agents](https://www.youtube.com/watch?v=flpKLkZla2Q) — Courtney Webster |
| Hooks | [Let it Cook (Feb 13)](https://www.youtube.com/watch?v=FjvtWeG6EEo) — Pierce Boggan, James Montemagno |
| Foundations / AI SDLC | [Agent Sessions Day Keynote](https://www.youtube.com/watch?v=2-Q_sdJ5H2c) — Harald Kirschner; [How VS Code Builds with AI](https://www.youtube.com/watch?v=ee-obY-4rqk) — Pierce Boggan, Peng Lyu |
| Model Selection | [Bring Your Own Model in VS Code](https://www.youtube.com/watch?v=VBSVSxs16_I) — Sandeep Somavarapu |
