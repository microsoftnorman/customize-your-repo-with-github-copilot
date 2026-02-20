---
name: check-video-sources
description: Checks the @code YouTube channel for new videos, manages local transcripts, finds demo timestamps, and identifies new information for the guide. Use when the user asks to check videos, review transcripts, find demos, says "what's new on the channel?", or wants to link demo videos to guide sections.
metadata:
  author: customize-your-repo
  version: "1.0"
---

# Check Video Sources

## When to Use This Skill

Use this skill when:
- User asks to check for new videos from the VS Code YouTube channel
- User wants to find demo timestamps for specific features
- User asks "what's new on the channel?" or "check the videos"
- User wants to add demo links to guide sections
- User mentions transcripts, video sources, or YouTube content
- User wants to verify a feature against a video demo

## Video Source

**Channel:** Visual Studio Code (@code)
**URL:** https://www.youtube.com/@code
**RSS Feed:** https://www.youtube.com/feeds/videos.xml?channel_id=UCs5Y5_7XK8HLDX0SLNwkd3w

## Transcript Storage

**Location:** references/transcripts/code-channel/
**Index:** references/transcripts/code-channel/README.md

### File Naming Convention

{YYYY-MM-DD}-{slug}.md where the date is the publish date and slug is a short descriptive name.

Examples:
- 2026-02-19-agent-sessions-day.md
- 2026-02-13-let-it-cook-agent-steering.md
- 2026-02-13-kafka-mcp.md

### Transcript File Format

Every transcript file must include YAML frontmatter:

```yaml
---
video_id: tAezuMSJuFs
title: "VS Code Live: Agent Sessions Day"
url: https://www.youtube.com/watch?v=tAezuMSJuFs
channel: "@code (Visual Studio Code)"
published: 2026-02-19
speakers:
  - Speaker Name
topics:
  - topic-keyword
relevance: primary  # or secondary
---
```

Frontmatter fields:

| Field | Required | Description |
|-------|----------|-------------|
| video_id | Yes | YouTube video ID |
| title | Yes | Full video title |
| url | Yes | Full YouTube watch URL |
| channel | Yes | Always "@code (Visual Studio Code)" |
| published | Yes | Publish date (YYYY-MM-DD) |
| speakers | Yes | List of speaker names |
| topics | Yes | List of topic keywords for search |
| relevance | Yes | primary (directly covers guide topics) or secondary (tangentially related) |
| segment_videos | No | For livestreams: map of segment names to separate video IDs |

After frontmatter, include:
1. **Title heading**  # {Video Title}
2. **Summary**  One paragraph describing the video
3. **Agenda/Timestamps**  Table linking to specific moments (for long videos)
4. **Key Topics Covered**  Bullet list of main subjects
5. **Links**  URLs mentioned in the video
6. **Full Transcript**  The complete transcript text (user pastes this)

## Instructions

### Step 1: Check for New Videos

Fetch the YouTube RSS feed:

`
https://www.youtube.com/feeds/videos.xml?channel_id=UCs5Y5_7XK8HLDX0SLNwkd3w
`

Parse the feed entries. Each <entry> contains:
- <yt:videoId>  the video ID
- <title>  video title
- <published>  publish date
- <media:description>  video description (often contains the agenda)

Filter to videos published in the last 3 weeks.

### Step 2: Compare Against Existing Transcripts

Read references/transcripts/code-channel/README.md for the current index.

List files in references/transcripts/code-channel/ and check video_id in each file's frontmatter.

Identify new videos that don't have corresponding transcript files.

### Step 3: Assess Relevance

For each new video, check whether its title and description mention topics covered by the guide:

**Primary relevance keywords:** custom agents, instructions, copilot-instructions, file-based instructions, prompts, prompt files, skills, agent skills, MCP, model context protocol, hooks, coding agent, agent mode, sub-agents, handoffs, BYOM, bring your own model

**Secondary relevance keywords:** VS Code, Copilot, AI coding, agent, agentic, vibe coding, CLI

Skip videos that are purely about unrelated topics (e.g., themes, keybindings, non-AI extensions).

### Step 4: Create Transcript Files for New Videos

For each relevant new video:

1. Create a new file at references/transcripts/code-channel/{date}-{slug}.md
2. Populate YAML frontmatter from the RSS data
3. Add a summary section extracted from the video description
4. If the description contains timestamps/agenda, include them as a table
5. Add the ## Full Transcript section with a comment instructing the user to paste the transcript

### Step 5: Search Existing Transcripts

Use grep/search to find mentions of features, settings, or patterns in transcript files.

Cross-reference against the Topic Cross-Reference table in the README.

Identify timestamps where specific features are demoed  these can be linked from the guide.

### Step 6: Identify Demo Links for the Guide

Map transcript content to guide sections:

| Guide File | Potential Demo Links |
|------------|---------------------|
| docs/part-2-5-custom-agents.md | Videos about custom agents, agent skills, handoffs, sub-agents |
| docs/part-2-6-mcp.md | Videos about MCP servers, MCP apps, external integrations |
| docs/part-2-4-skills.md | Videos about agent skills, skill creation |
| docs/part-2-7-hooks.md | Videos about hooks, security enforcement |
| docs/part-1-foundations.md | Keynotes, overview talks, AI SDLC discussions |
| docs/part-2-1-always-on-instructions.md | Videos about copilot-instructions.md |
| docs/part-2-2-file-based-instructions.md | Videos about .instructions.md files |
| docs/part-2-3-prompts.md | Videos about prompt files |

Demo links in the guide use this format:

```markdown
**See it in action:** [Video Title](https://www.youtube.com/watch?v={id}&t={seconds}s)  Speaker demos {what is demoed}.
```

Place the link after the section's opening paragraph or after the **Loading/Best For** metadata.

### Step 7: Update the README Index

After creating new transcript files, update references/transcripts/code-channel/README.md:

1. Add entries to the appropriate week's table in the Index section
2. Update the Topic Cross-Reference table if new videos cover guide topics
3. Keep weeks in reverse chronological order (newest first)

### Step 8: Present Findings

Report to the user with these sections:

- **New videos found:** List with titles, dates, and relevance assessment
- **Transcript coverage gaps:** Videos that exist but lack transcript text (user needs to paste)
- **Demo links to add:** Specific guide sections that should link to video demos, with timestamps
- **New information found:** Features, patterns, or announcements in transcripts not yet covered by the guide

Do not apply changes to guide docs automatically. Present findings and let the user decide.

## Edge Cases

- **YouTube RSS feed is unavailable:** Report the failure and search existing local transcripts only.
- **Video page requires login:** YouTube video pages redirect to login for automated fetch. Use the RSS feed for metadata and instruct the user to paste transcripts manually.
- **Livestream with multiple segments:** Create one master transcript file for the full stream. Reference individual segment videos in the segment_videos frontmatter field and in the agenda table.
- **Duplicate content:** If a segment is available both as part of a livestream and as a standalone clip, use the livestream as the primary file. Note the standalone clip URL in the agenda table.
- **Transcript not yet pasted:** Mark the file as having a coverage gap. The file is still useful for metadata, timestamps, and linking even without the full transcript.
