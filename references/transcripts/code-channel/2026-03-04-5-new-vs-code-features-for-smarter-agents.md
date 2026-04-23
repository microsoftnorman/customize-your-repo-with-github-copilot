---
video_id: MvwcWWp1NFs
title: "5 New VS Code Features for Smarter Agents"
url: https://www.youtube.com/watch?v=MvwcWWp1NFs
channel: "@code (Visual Studio Code)"
published: 2026-03-04
speakers:
  - Olivia Guzzardo McVicker
topics:
  - skills
  - message-steering
  - browser-tool
  - hooks
  - agents
relevance: primary
---

# 5 New VS Code Features for Smarter Agents

Working with agents just got more practical! In this video, we break down 5 of the top features from the latest VS Code release, which let agents adapt to how you work, and not the other way around.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Intro |
| 00:26 | Agent Skills on demand |
| 00:59 | Message steering |
| 01:30 | Integrated browser |
| 01:52 | Fork a conversation |
| 02:12 | Hooks |
| 02:41 | Recap |

## Key Topics Covered

- **Skills**
- **Message Steering**
- **Browser Tool**
- **Hooks**
- **Agents**

## Links

- https://aka.ms/VSCode/110
- https://github.com/pierceboggan/vscode-contributor-website
- https://x.com/code
- https://bsky.app/profile/vscode.dev
- https://aka.ms/VSCode/LinkedIn
- https://github.com/microsoft/vscode

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] The latest VS Code release just dropped
[0:00:02] and I'm going to show you five of my
[0:00:03] favorite features that you can try right
[0:00:05] now. Let's go. I'm going to be adding a
[0:00:09] feature to this VS Code contributor
[0:00:10] website that Pierce, the VS Code product
[0:00:12] lead, created, which showcases community
[0:00:15] contributors by scraping release notes
[0:00:17] from the VS Code docs repository. I want
[0:00:20] to add a top contributor spotlight to
[0:00:22] the site. And there are some guidelines
[0:00:23] that I want the agent to follow when
[0:00:25] creating the design. So we have this
[0:00:27] front-end design agent skill that helps
[0:00:29] guide the agent to create a design to
[0:00:31] our specifications and avoid AI slop.
[0:00:34] And now we can quickly reference this
[0:00:36] agent skill using a slash command in our
[0:00:38] prompt. So along with slashforend
[0:00:41] design, I will prompt to add a top
[0:00:43] contributor spotlight hero card with
[0:00:45] some details for the design and specify
[0:00:47] to open the web page when done and
[0:00:49] verify its changes. And this will
[0:00:52] automatically follow the instructions
[0:00:53] that are defined in our front-end design
[0:00:55] skill. Then we'll let the agent get to
[0:00:57] work. Now, often you send a prompt and
[0:01:00] think, "Oh, wait. There are some more
[0:01:02] details I should add or some
[0:01:03] clarifications." Just like if you were
[0:01:06] having a conversation with someone, this
[0:01:08] is where the new message steering
[0:01:09] feature comes into play. While the agent
[0:01:12] is working, I can send a follow-up
[0:01:13] message like specifying more details on
[0:01:16] how I want this design to look with a
[0:01:18] fun shimmer animation. and the agent
[0:01:21] will take it into account mid response.
[0:01:24] No more stopping the current chat or
[0:01:26] waiting for the agent to finish before
[0:01:27] providing those follow-ups. Now, as that
[0:01:30] finishes implementing those changes, you
[0:01:32] will notice that the new integrated
[0:01:34] browser immediately opens as I told the
[0:01:36] agent to open the web page and verify
[0:01:38] changes in my initial prompt. With this
[0:01:41] latest release, the integrated browser
[0:01:43] is so powerful. Able to navigate to the
[0:01:45] page, verify the page content, and use
[0:01:48] other tools like clicking elements and
[0:01:50] running playwright code autonomously.
[0:01:53] The next feature I want to show is the
[0:01:54] ability to fork conversations. I can
[0:01:57] type /fork to create a new session with
[0:01:59] the full conversation history and
[0:02:01] explore an alternative design that's
[0:02:03] more minimal. for example. This is a
[0:02:06] great way to create a new branch of the
[0:02:08] conversation without losing the original
[0:02:10] context.
[0:02:12] The final feature I want to show is hook
[0:02:14] support. Hooks let you execute custom
[0:02:17] shell commands at key life cycle points
[0:02:19] in your agent sessions. So you can add
[0:02:21] automations directly into how you work
[0:02:23] with agents. Here's a great example that
[0:02:26] we have set up in this repo. A hook that
[0:02:28] fires on stop of an agent session and
[0:02:31] autocommits your pending changes. That
[0:02:33] means you do not have to worry about
[0:02:35] losing any of the work generated.
[0:02:37] Committing can be baked into your
[0:02:39] agentic flow.
[0:02:42] In just a couple of minutes, you saw me
[0:02:43] add a feature using an agents go on
[0:02:45] demand, steer the agents response
[0:02:47] mid-flight, verify the result in an
[0:02:50] integrated browser, fork the
[0:02:52] conversation, and autocommit my changes
[0:02:54] using a hook. And that's just the start
[0:02:56] of what's new in VS Code. Make sure to
[0:02:58] check out the full release notes to
[0:03:00] learn more. Happy coding.
