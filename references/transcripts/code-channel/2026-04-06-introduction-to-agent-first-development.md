---
video_id: uu4sf8z9n8c
title: "Introduction to Agent-First Development"
url: https://www.youtube.com/watch?v=uu4sf8z9n8c
channel: "@code (Visual Studio Code)"
published: 2026-04-06
speakers:
  - Gwyneth Peña-Siguenza
topics:
  - agent-mode
  - prompts
  - tools
  - context
  - model-selection
relevance: primary
---

# Introduction to Agent-First Development

In this video Gwyneth introduces and demos the 5 concepts you need to understand in order to kick off your first agent session!

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Introduction to the Agent-First Development series |
| 00:55 | Customizing your terminal |
| 01:50 | The 5 concepts you need to understand to get started |
| 02:30 | Harness |
| 03:30 | Model |
| 04:28 | Prompts |
| 05:17 | Tools |
| 08:00 | Context |
| 09:17 | In Summary |
| 09:42 | What's Next |

## Key Topics Covered

- **Agent Mode**
- **Prompts**
- **Tools**
- **Context**
- **Model Selection**

## Links

- https://youtu.be/WcN74XvZGes
- https://aka.ms/vsc-learn
- https://x.com/madebygps
- https://x.com/code
- https://aka.ms/VSCode/LinkedIn
- https://bsky.app/profile/vscode.dev
- https://github.com/microsoft/vscode

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Hi, welcome to this series of videos
[0:00:02] where our goal is to teach you
[0:00:05] everything you need to know to get
[0:00:06] started with agent first development
[0:00:08] with VS Code and GitHub Copilot. You may
[0:00:12] already know that writing code is
[0:00:14] changing. You can still of course write
[0:00:16] all your code manually and that might be
[0:00:18] ideal for specific use cases, but
[0:00:21] there's this new pattern where we're
[0:00:23] using agents to cover everything that is
[0:00:26] part of the software development life
[0:00:27] cycle. So, in this series of videos,
[0:00:30] we're going to teach you how to kick off
[0:00:31] your first agent session, how to
[0:00:34] understand tools and contexts and how to
[0:00:36] review the work that the agent is doing,
[0:00:39] how to review the changes, the different
[0:00:41] approval levels, the different reasoning
[0:00:43] effort levels, and a bunch of other
[0:00:46] things. So, let's kick things off today
[0:00:48] by talking about the five things you
[0:00:50] need to understand for a successful
[0:00:53] experience with your agents. One thing
[0:00:56] before we kick off here is my layout for
[0:00:59] VS Code might look a little different
[0:01:01] than yours, and we're all about
[0:01:03] customization with VS Code. So, I just
[0:01:05] wanted to show you quickly, you might
[0:01:06] see this view on the right and then this
[0:01:10] view on the left. If you actually click
[0:01:13] on these explorer area, right click, you
[0:01:16] can move the primary sidebar left, so
[0:01:19] you can swap them, right? And then doing
[0:01:22] the same thing, right click, you can
[0:01:24] move the primary sidebar right.
[0:01:27] Additionally, I also have my activity
[0:01:29] bar here. If I right click in this area,
[0:01:31] activity bar position, I can set this to
[0:01:34] default and you're most likely going to
[0:01:35] see this. To the side, I like having it
[0:01:38] up top, but you can move it however
[0:01:40] you'd like. And then if I move this to
[0:01:42] the left, that will also move to the
[0:01:44] left as well. So, just wanted to show a
[0:01:46] couple of customization options you have
[0:01:49] and that I've also taken advantage of.
[0:01:51] The reality is that these agents are not
[0:01:53] magic. You can't just throw one at your
[0:01:56] code base without instructions, without
[0:01:59] specificities on your code base and
[0:02:01] expect it to get 100% correct to your
[0:02:05] standard the task that you're trying to
[0:02:07] accomplish. But we can think of it sort
[0:02:10] of like a formula. There are five
[0:02:12] things: harness, model, context, tools,
[0:02:16] and prompts. And if you understand these
[0:02:18] five things, you're going to be well on
[0:02:20] your way to getting better and better
[0:02:22] results with your agents accomplishing
[0:02:24] the tasks that you want. So, let's dive
[0:02:27] into the first one here. Let's talk
[0:02:29] about the harness first. I have VS Code
[0:02:32] open and GitHub Copilot chat open here
[0:02:35] on the left side, and this is our
[0:02:37] harness. This what gives the model the
[0:02:40] ability to become an agent via the model
[0:02:43] selection, via the agent mode, via the
[0:02:47] tools that we enable it. The harness,
[0:02:51] you can think of it sort of like a a
[0:02:53] wiring harness in a car. The engine is
[0:02:56] what has all the power, but in order for
[0:02:59] the power to be distributed to different
[0:03:01] components, dashboard controls, etc. in
[0:03:04] your car, you need that harness, right?
[0:03:06] So, similar here. We have a model and
[0:03:09] its goal is to do the reasoning, do the
[0:03:11] generation of text and code, but in
[0:03:13] order for it to do this properly, it
[0:03:16] needs access to different tools, which
[0:03:18] we can configure. It needs access to the
[0:03:21] files in your code base to better
[0:03:23] understand what it needs to work on,
[0:03:25] etc., etc. So, the harness is what
[0:03:27] enables all of that, right? Taking it a
[0:03:29] step further, let's talk about the
[0:03:31] model. So, with GitHub Copilot, we are
[0:03:33] all about developer choice, and of
[0:03:35] course that includes the model options
[0:03:37] that you have. So, here I have the ones
[0:03:39] that I most frequently use, but if I
[0:03:41] typed in, for example, Codex, we would
[0:03:43] have that appear there as well. And then
[0:03:46] with every model, there's also a
[0:03:48] thinking effort. So, you have low,
[0:03:51] medium, and high, and this balances the
[0:03:55] speed of a response with the uh amount
[0:03:58] of reasoning, right? So, for
[0:04:00] straightforward boilerplate formatting,
[0:04:02] any quick, simple tasks, you can use
[0:04:05] low. If you want a balanced, you can use
[0:04:07] medium, so perhaps refactoring that's
[0:04:10] straightforward. Or if you have uh more
[0:04:12] of like an architectural type task, uh
[0:04:15] difficult debugging, you would want to
[0:04:16] set that to to high there, too. So, what
[0:04:19] I'm going to do is click on the Sonnet
[0:04:21] model. I'll have it set to high, which
[0:04:23] also happens to be the default thinking
[0:04:26] effort there, and I'm going to paste in
[0:04:28] a prompt, which is the next part of that
[0:04:31] formula of success, right?
[0:04:32] So, I'm going to go ahead and send this
[0:04:34] off. So, a good prompt would include
[0:04:37] enough details where the request that
[0:04:40] you have is not vague, but also enough
[0:04:43] for
[0:04:45] the model to not get overly stuck in the
[0:04:49] weeds and details of implementation,
[0:04:51] right?
[0:04:52] Now, the prompt I sent already, I can
[0:04:56] tell that I
[0:04:57] forgot to include something, but I'm not
[0:04:58] going to edit it now. I'll save that for
[0:05:00] the next video, and what I want to
[0:05:02] instead show you is
[0:05:04] uh some more parts of this formula of
[0:05:06] success, right?
[0:05:07] And it is asking us for permission to to
[0:05:10] run uh the uh
[0:05:12] command in our uh Z shell here,
[0:05:15] but what I want to do is actually expand
[0:05:16] here and talk a little bit about the
[0:05:18] tools,
[0:05:20] which is another part of our formula of
[0:05:21] success here, right? So, we see here
[0:05:24] that it says created four to-dos and ran
[0:05:26] command in terminal. And also, you see
[0:05:30] this little icon, which is a to-dos list
[0:05:32] icon, and then you see this little
[0:05:34] terminal command uh icon, right? And
[0:05:37] where this comes from is I'm going to
[0:05:39] actually expand this a little bit so we
[0:05:40] get our tool picker, and we're going to
[0:05:42] click on this.
[0:05:43] And we see here that we have the option
[0:05:46] to configure tools, and I have 152
[0:05:49] selected, which is probably not great.
[0:05:51] I'm going to
[0:05:52] just make sure I only have selected the
[0:05:55] ones that are ideal for this session. I
[0:05:58] don't need Azure MCP.
[0:06:00] I don't need bicep. Uh we can keep
[0:06:04] context seven. I don't need play right.
[0:06:06] We're going to just organize this a
[0:06:07] little bit more.
[0:06:09] I don't need GitHub Copilot or mermaid.
[0:06:13] Uh Python I will need. Container tools I
[0:06:15] also do not need. Okay, great. So, we
[0:06:16] see that list went down to
[0:06:18] 70 tools. I don't need Tavily either.
[0:06:20] 64.
[0:06:22] Uh pull requests, don't need them for
[0:06:24] right now, and then context seven. Okay,
[0:06:26] so we have uh 55 here.
[0:06:29] Now, these are just our built-in tools.
[0:06:32] Now, all of these other ones that I had
[0:06:34] just gone through, these are things that
[0:06:35] I've either installed via extensions or
[0:06:37] MCP service, etc., and we have videos
[0:06:40] down the line that will cover these, but
[0:06:42] we'll talk about the built-in ones. So,
[0:06:44] you see that to-do icon matches this
[0:06:46] tool here, right? And then we have that
[0:06:49] little command icon or command line or
[0:06:51] terminal icon, which matches this one
[0:06:52] here. And these are built-in tools that
[0:06:54] will allow the agent to either delegate
[0:06:57] tasks to other agents, open interactive
[0:07:00] with inner integrated browser pages,
[0:07:02] edit files, run commands, read files,
[0:07:05] search, manage to-dos, and use VS Code
[0:07:08] features, and or do web searches, right?
[0:07:12] So, because we have those all checked,
[0:07:13] and then you can expand to have a more
[0:07:15] granular
[0:07:17] configuration as to which tools from
[0:07:20] which category do you want enabled, but
[0:07:21] I want them all for now. And the agent
[0:07:24] was able to execute those
[0:07:27] uh actions and tools because we have
[0:07:29] them enabled here, right? Uh so, keep
[0:07:32] that in mind when you're trying to run a
[0:07:34] specific task, make sure you have the
[0:07:36] right tools set up there as well.
[0:07:38] Awesome. Now,
[0:07:40] the other thing that this project here
[0:07:43] is doing or this agent action here is
[0:07:45] doing is I'm going to actually create
[0:07:49] or we'll let it up
[0:07:51] run. So, I'll click allow here. I'll
[0:07:53] talk a little bit more about this allow
[0:07:54] button and this default approvals
[0:07:57] setting in the next video. But for now,
[0:07:59] I want to talk to you a little bit about
[0:08:01] context. So, we see here that the the
[0:08:04] agent has read and it read a specific
[0:08:07] directory, and by doing this, it's
[0:08:09] including that directory and whatever it
[0:08:12] found in it into its context. We can
[0:08:14] also manually provide context to an
[0:08:17] agent by or to this session particularly
[0:08:20] here by clicking on the plus icon here,
[0:08:24] and we have a variety of ways of
[0:08:27] attaching context to our prompt. So,
[0:08:30] files and folders, we have a couple of
[0:08:31] GitHub options, resources via MCP, which
[0:08:34] we will cover ahead in further videos,
[0:08:38] and a bunch of other areas as well,
[0:08:40] right? And additionally, you can use the
[0:08:42] pound symbol
[0:08:43] to provide the name of a file if you
[0:08:46] wanted to attach it as context as well.
[0:08:48] You can do that that way as well.
[0:08:50] And this is important because
[0:08:53] models are trained over lots and lots of
[0:08:56] information, but it isn't an expert in
[0:09:01] any niche, so you need to provide
[0:09:03] context, files, instructions, details on
[0:09:05] your code base so the agent can have
[0:09:07] specific results for your code base and
[0:09:11] not just function off the generalist
[0:09:13] knowledge that it has.
[0:09:15] And congrats, you've just kicked off
[0:09:17] your first agent session. We covered a
[0:09:20] lot in this video. We understand what a
[0:09:22] harness is. We understand the different
[0:09:23] models and reasoning effort level
[0:09:25] options that we have. We understand how
[0:09:27] to add context, how to enable or disable
[0:09:29] tools, and then of course, we kicked off
[0:09:32] work with a prompt. Now, you can see
[0:09:35] that our agent is already asking for
[0:09:38] approval for the next command in the
[0:09:40] work it's trying to accomplish. In the
[0:09:42] next video, we're going to talk about
[0:09:44] all of the permission levels and the
[0:09:46] different ways we can allow or skip a
[0:09:49] specific command that an agent is trying
[0:09:51] to run. So, stay tuned.
