---
video_id: LGx8YieBjIA
title: "1.109 VS Code Release Highlights"
url: https://www.youtube.com/watch?v=LGx8YieBjIA
channel: "@code (Visual Studio Code)"
published: 2026-02-11
speakers:
  - Reynald Adolphe
topics:
  - mcp
  - skills
  - sub-agents
  - browser-tool
  - release-highlights
relevance: primary
---

# 1.109 VS Code Release Highlights

Reynald Adolphe summarizes the VS Code 1.109 release with a strong focus on Copilot and agent features, including MCP Apps, agent skills, subagents in parallel, and third-party coding agents.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Introduction |
| 00:10 | Ask Questions |
| 00:39 | Support for MCP Apps |
| 01:52 | Agent Skills Generally Available |
| 02:58 | Subagents in Parallel |
| 04:19 | Integrated Browser (Preview) |
| 05:07 | Third Party Coding Agents (Preview) |

## Key Topics Covered

- **MCP Apps**
- **Skills**
- **Subagents**
- **Integrated Browser**

## Links

- https://aka.ms/VSCode/109
- https://youtu.be/GMAoTeD9siU

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] The latest release of VS Code is here, and it is packed full of new features to help streamline your work and boost your productivity.
[0:00:08] So let's go ahead and take a look.
[0:00:10] Now, when you're in plan mode or just working with an agent, the agent can now use the Ask Questions tool to ask clarifying questions during chat conversations.
[0:00:20] It presents one or more directly in the chat with single or multi-select options, free text input, and recommended answers highlighted for quick decisions.
[0:00:30] This is an experimental feature and to enable it just go to the settings and search for chat ask questions.
[0:00:39] Also, this release VS Code has added support for MCP apps, which now means that your favorite MCP servers can now present a rich interactive user interface.
[0:00:49] So for example, without it, if I wanted to ask chat to sort these tasks, it will take a guess at what it thinks is important to me.
[0:01:00] And in fact, in this case, it gives me several options.
[0:01:03] But instead of me having to go back and forth in the chat, it would be nice for it to just give me a UI with the options, and then I can just order it to my pleasing.
[0:01:13] So right over here is MCP apps playground that I cloned, which gave me access to several tools, particularly right over here.
[0:01:22] MCP apps playground, and one of them, this sort is what we're going to invoke.
[0:01:29] So now that I have it running, I'm going to enter in the same command to sort these tasks by priority.
[0:01:36] And it gives me this UI now so that I can drag up or drag down different items, which is a lot quicker than having to type to tell the chat what order that I want my tasks in.
[0:01:52] Agent skills are now enabled by default.
[0:01:55] Skills provide the AI specialized capabilities you define.
[0:01:59] So for example, I have the fine one here to convert mark down to HTML.
[0:02:04] And to run it, in my case, just ask chat, convert the read me to HTML.
[0:02:10] We can then take a peek at the read me mark down and boom.
[0:02:16] Right there, it created the HTML, which we can peek at also.
[0:02:21] To create a skill, all you need to do is click on the gear icon and choose skills.
[0:02:27] And from there, just choose new skill.
[0:02:30] And you can indicate the location to create the skill, give it a lower case name, and then go ahead and define it.
[0:02:37] Now I'll delete this since I already have one for converting mark down to HTML, but also know that within settings.
[0:02:47] By entering skills, you have the option to define multiple locations where your skills are loaded from.
[0:02:54] Right below is where it's checked by default that skills are enabled.
[0:02:58] Subagents can now run in parallel, which can significantly speed up tasks that can be split into independent tasks.
[0:03:06] To provide more visibility into what the different subagents are doing, the chat conversation now shows details such as what tasks it's doing.
[0:03:15] The custom agent used for the subagent and whichever tool is currently used.
[0:03:21] You can expand the chat information to show the full details of what's going on, including the full initial prompt it was provided with and the results it returned.
[0:03:32] In my scenario, I asked it to find duplicate patterns, identify unused exports and dead code, review error handling consistency, and to check for security vulnerabilities.
[0:03:44] And then to compile the findings into a prioritized action plan, and here are the results.
[0:03:51] For more on this topic, check out this episode of VS Code Insider's podcast here.
[0:03:55] You are now able to select a bracket and string content with a simple double click.
[0:04:01] So for example, if I highlight right over here this opening curly brace, it immediately highlights the content within there.
[0:04:09] And the same thing would happen if I come over here with this opening bracket, which allows me to quickly highlight its content.
[0:04:17] Small but powerful.
[0:04:19] VS Code now has a new integrated browser that you can access from the command palette by entering browser open integrated browser.
[0:04:27] So from here I can enter a URL such as for my read me, and I could choose to add an element to the chat for context.
[0:04:37] So if I want to have the chat have focus on the title here features, it immediately added a screenshot, and then I could ask whatever questions I want related to it.
[0:04:49] And under the lip scenes there's even a section here for developer tools to use like you've done in the past and manipulate variables.
[0:04:57] But what's even cooler, we can now log on to sites that require authentication, even if we're dealing with two factor.
[0:05:06] And also with this release you can now use Claude and Codex with your local or cloud agents all with the same GitHub co-pilot subscription.
[0:05:17] But there's so much more, so definitely check out the release notes.
[0:05:21] So those were some of my favorite features from this release note.
[0:05:25] Let me know what some of yours were in the comments.
[0:05:27] And also make sure you check out this video here too.
