---
video_id: BsAHunfVwNs
title: "Multi-agent development in VS Code"
url: https://www.youtube.com/watch?v=BsAHunfVwNs
channel: "@code (Visual Studio Code)"
published: 2026-02-04
speakers:
  - Olivia Guzzardo McVicker
topics:
  - multi-agent
  - agent-sessions
  - sub-agents
  - cloud-agents
relevance: primary
---

# Multi-agent development in VS Code

See how to delegate tasks to multiple agents in VS Code - local, background, cloud, and even Claude and Codex - to tackle all of your coding tasks, with an updated user experience for managing them all.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Intro |
| 00:11 | Agent sessions welcome page |
| 00:49 | Tour of agent sessions |
| 02:51 | Parallel subagents |

## Key Topics Covered

- **Multi Agent**
- **Agent Sessions**
- **Sub Agents**
- **Cloud Agents**

## Links

- https://aka.ms/VSCode/109
- https://code.visualstudio.com/docs/copilot/agents/overview
- https://github.com/microsoft/vscode/issues
- https://x.com/code
- https://bsky.app/profile/vscode.dev
- https://aka.ms/VSCode/LinkedIn
- https://github.com/microsoft/vscode

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] The latest VS Code release brings a
[0:00:02] whole new experience for managing your
[0:00:03] agents, whether local, cloud,
[0:00:06] background, or even cloud or codecs.
[0:00:08] Let's dive in. The teams landed a lot of
[0:00:12] new changes to the agent experience in
[0:00:13] VS Code, so you can use multiple agents
[0:00:16] to tackle all of your coding tasks.
[0:00:18] There's a new agent sessions welcome
[0:00:20] experience that opens when you start up
[0:00:22] VS Code. It gives an overview of your
[0:00:24] agent sessions so you can jump right
[0:00:26] into them or see them at a glance and
[0:00:29] kick off a new agent session right away.
[0:00:32] You can also open the agent session
[0:00:34] sidebar at any time by clicking the chat
[0:00:36] icon in the command center. To see the
[0:00:38] agent sessions page at startup, you'll
[0:00:40] want to set the workbench startup editor
[0:00:42] setting to agent sessions welcome page
[0:00:44] as this is still an experimental
[0:00:46] setting. When I go to kick off an agent
[0:00:48] session, I can work with multiple types
[0:00:50] of agents. I can use a local agent to
[0:00:53] work interactively, a background agent
[0:00:55] for changes isolated in a git work tree,
[0:00:58] a cloud agent for changes running in the
[0:01:00] cloud that result in a PR, and even
[0:01:02] other providers like Claude or Codeex as
[0:01:04] local agents. Let's start with a local
[0:01:07] plan agent that will research and create
[0:01:09] a multi-step plan and ask to suggest
[0:01:11] improvements for making my app more
[0:01:13] accessible.
[0:01:15] We'll kick that off while I continue my
[0:01:17] work with other agents.
[0:01:19] I'm going to start a background agent so
[0:01:21] that it will work asynchronously via the
[0:01:23] co-pilot CLI in a git work tree. And
[0:01:25] this is an app I have for meal planning
[0:01:27] that I want to add a new page for likes
[0:01:29] and dislikes. Throughout this, I can
[0:01:32] track and check on my agents via the
[0:01:33] counter at the top of the editor. Filter
[0:01:36] by session status and maximize chat
[0:01:39] input while agents continue working.
[0:01:41] Next, I'm going to delegate some work to
[0:01:43] the cloud agent. And you can now use
[0:01:45] Copilot, Claude, or Codeex cloud agents.
[0:01:48] all with your single GitHub C-Pilot
[0:01:50] subscription. I'll stick with Copilot
[0:01:52] and ask it to make sure the readme is
[0:01:54] updated with the latest functionality.
[0:01:56] This will then kick off the co-pilot
[0:01:58] coding agent to create a pull request
[0:02:00] and if I had any pending changes, it
[0:02:02] would walk me through managing that.
[0:02:04] Once the pull request is created, I can
[0:02:06] view it using the GitHub pull request
[0:02:08] extension, then return to the agent
[0:02:10] sessions list to track my sessions in
[0:02:12] progress.
[0:02:13] The local plan agent finished its
[0:02:15] initial plan for improving
[0:02:16] accessibility. So now I can choose to
[0:02:19] keep iterating or start implementing the
[0:02:21] plan. Now I'll jump back to the
[0:02:23] background agent I kicked off to add a
[0:02:25] new page. I can then review the changes
[0:02:27] that were generated on the git work tree
[0:02:29] and after reviewing choose to apply the
[0:02:32] changes to my workspace which adds those
[0:02:34] changes in the source control view. I
[0:02:36] can then decide to run a co-pilot code
[0:02:38] review from here. walk through the
[0:02:40] comments and when ready I can use
[0:02:43] copilot to generate a commit message for
[0:02:45] a full copilot flow from prompt to push.
[0:02:49] One last feature that I will leave you
[0:02:50] with is the ability to run parallel sub
[0:02:52] aents. I'm going to kick off a local
[0:02:55] agent session asking to use sub aents to
[0:02:57] analyze my project's error handling
[0:02:59] across the front end, backend, and
[0:03:00] database layers. While that runs, a
[0:03:03] little bit more about sub aents. A sub
[0:03:06] aent is a context isolated agent that
[0:03:08] runs independently from your main chat
[0:03:10] session. This is beneficial because it
[0:03:12] means it keeps your context cleaner by
[0:03:14] dispatching jobs out to a sub agent.
[0:03:17] Then it just brings the result back to
[0:03:18] the main chat. And now you can run
[0:03:21] parallel sub aents making for even
[0:03:23] quicker results. So we can see here that
[0:03:25] multiple sub aents have spun up each
[0:03:28] tackling their specific part of the
[0:03:29] project and are all running at once with
[0:03:32] self-contained context that we can still
[0:03:34] follow.
[0:03:35] We're so excited to be on this journey
[0:03:37] of making VS Code your agent UX. The
[0:03:40] team's constantly shipping new features
[0:03:42] and would love any feedback. So, make
[0:03:44] sure to drop your thoughts in the
[0:03:45] comments or file an issue directly on
[0:03:47] the VS Code repo. As always, happy
[0:03:50] coding.
