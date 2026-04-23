---
video_id: WcN74XvZGes
title: "Your first agent session in action"
url: https://www.youtube.com/watch?v=WcN74XvZGes
channel: "@code (Visual Studio Code)"
published: 2026-04-06
speakers:
  - Gwyneth Peña-Siguenza
topics:
  - agent-sessions
  - permissions
  - tool-calls
  - context-window
relevance: primary
---

# Your first agent session in action

In this video we'll look at Permissions, Tool Calls and the Context Window.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | In this video |
| 00:28 | Permissions and Levels of Approval |
| 03:16 | Tool Calls |
| 03:55 | Context Window |
| 06:19 | Summary |
| 06:37 | What's next - Reviewing and controlling agent changes |

## Key Topics Covered

- **Agent Sessions**
- **Permissions**
- **Tool Calls**
- **Context Window**

## Links

- https://youtu.be/oFSJs6RnFt4
- https://aka.ms/vsc-learn
- https://x.com/madebygps
- https://x.com/code
- https://aka.ms/VSCode/LinkedIn
- https://bsky.app/profile/vscode.dev
- https://github.com/microsoft/vscode

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] In the last video, we kicked off our
[0:00:02] first agent session. And in this video,
[0:00:05] we're going to understand the different
[0:00:06] levels of permissions that we can
[0:00:09] execute our agents with, so we can have
[0:00:12] full control over the level of autonomy.
[0:00:15] Additionally, we're going to understand
[0:00:17] what tool calls are and take a look at
[0:00:19] some of the calls that the agent is
[0:00:21] doing. And then finally, we're going to
[0:00:23] understand what a context window is. All
[0:00:27] right, so let's dive right in. All
[0:00:28] right, so in the last video, we kicked
[0:00:30] off some work and we ended up seeing
[0:00:33] this command that wants to run in the
[0:00:36] terminal. By the way, you can see the
[0:00:38] terminals that the agent is using by in
[0:00:41] the terminal area clicking on the hidden
[0:00:43] terminals. And if there are various
[0:00:45] ones, you'll see a list, but since there
[0:00:47] is just one in this case, uh it opened
[0:00:50] right away there.
[0:00:51] Okay, so we clicked allow on that first
[0:00:54] command, right? But I want to dive
[0:00:56] deeper into the permissions and how we
[0:00:59] can use this lab functionality here.
[0:01:02] First, the reason why we are even being
[0:01:05] asked to allow specific commands that
[0:01:08] are popping up here is because we have
[0:01:10] this set to default approvals. And if I
[0:01:12] click on this,
[0:01:13] we see that we have the option to select
[0:01:17] three approval levels. So, default
[0:01:19] approvals will have Copilot use your
[0:01:21] configured settings. A bypass approvals
[0:01:24] will mean that all tool calls are auto
[0:01:27] approved and retries are also done
[0:01:30] automatically. And then autopilot, which
[0:01:33] is in preview, will auto approve all
[0:01:35] tool calls and continue the task until
[0:01:39] it is done. So, the difference between
[0:01:41] these two is they both auto approve all
[0:01:43] tool calls. However, in this approval
[0:01:46] level, the bypass one, if there is any
[0:01:50] clarification that the agent needs, it
[0:01:52] will ask you for that. Whereas in the
[0:01:54] autopilot approval level, it will answer
[0:01:58] those questions on its own. And the goal
[0:02:00] is to get to the end of the task, no
[0:02:02] matter what. Different options here. I'm
[0:02:04] going to keep this to default approvals
[0:02:06] and in future videos, we'll use the
[0:02:07] other levels.
[0:02:09] Now, also, when it comes to approving
[0:02:11] individual commands, if we click on the
[0:02:13] drop down here on the right side of the
[0:02:15] allow, we have a couple of options.
[0:02:18] We can allow all commands that start
[0:02:20] with UV in this session, in this
[0:02:23] workspace, or always allow. Or we can
[0:02:26] allow similarly this exact command in
[0:02:29] the session, in this workspace, or
[0:02:31] always allow this exact command. We can
[0:02:34] also allow all commands in the session.
[0:02:36] So, for example, let's say, all right, I
[0:02:39] want to
[0:02:39] go ahead and allow this command and any
[0:02:41] other prompts to allow a command, just
[0:02:45] auto approve it, we can select that here
[0:02:48] as well. And I'm just going to click
[0:02:50] allow once more here and we'll see
[0:02:53] what's going on here. All right, looks
[0:02:54] like it wrote some tests for us as well.
[0:02:58] Now, like I mentioned, there is a change
[0:03:00] I want to make here, but before we do
[0:03:03] that, I do want to show you
[0:03:05] a couple things. Now, this agent has
[0:03:08] been running and we saw in the previous
[0:03:10] video that there are already some tool
[0:03:11] calls that we reviewed there. And we see
[0:03:14] that it has reviewed files, it's uh done
[0:03:17] some updates here, it's edited, it's
[0:03:19] created using those built-in tools. And
[0:03:22] then you can also in the chat use the
[0:03:24] pound symbol and call tools yourself.
[0:03:26] So, read, right, we can run command, you
[0:03:30] can also search, I believe. And I think
[0:03:34] there's also web search here as well.
[0:03:37] Yes, you can call those tools manually
[0:03:38] if you want. But the whole goal of
[0:03:42] agentic programming, agent-first
[0:03:44] development is that you tell the task
[0:03:46] and the agent goes and figures out which
[0:03:49] tools to use instead of you explicitly
[0:03:51] telling them. But that is an option if
[0:03:52] you if you want, right? Uh before we
[0:03:54] make any edits here, I do want to talk a
[0:03:56] little bit about the context window.
[0:03:59] Remember I was talking about context
[0:04:01] being the information that the agent
[0:04:03] collects along the way or that you
[0:04:05] provide to the agent. Well, that is
[0:04:08] important to keep in mind when we are
[0:04:10] talking about the context window. So,
[0:04:12] every model has a context window and
[0:04:15] this essentially measures how much
[0:04:17] information the model can have in memory
[0:04:19] before sort of just starting to forget
[0:04:22] some of the earlier messages that you've
[0:04:24] had, right? So, for example, this one is
[0:04:27] 200,000 tokens. A token roughly converts
[0:04:30] to a word in English. In any other
[0:04:34] language, it's the conversion is
[0:04:37] slightly different, but we can, for the
[0:04:38] sake of this video, say one word is one
[0:04:40] token, right? As your context window
[0:04:42] starts to fill up, this will change into
[0:04:45] red. Right now, it tells us we have a
[0:04:46] 10% usage of the context window and
[0:04:49] it'll show us the system is using this
[0:04:52] breakdown. So, the system instructions,
[0:04:53] these are any built-in guidelines for
[0:04:56] the agent itself. And then the tool
[0:04:58] definitions, that includes all the
[0:04:59] definitions of the tools that are
[0:05:01] selected to run in the session, which is
[0:05:04] why it's important to only use the tools
[0:05:06] or have enabled the tools that you
[0:05:07] really need. Back to the context window,
[0:05:10] we also have user context, which
[0:05:11] includes all the messages we have
[0:05:13] provided and the responses that the
[0:05:15] agent has given us and then any results
[0:05:17] from the tools. So, this could be like
[0:05:19] terminal output, reading of files, etc.
[0:05:22] We also have this compact conversation.
[0:05:25] Uh the way this works is this is
[0:05:26] manually invoking the summarization of
[0:05:29] your entire chat history and keeping
[0:05:31] just the most important details. That
[0:05:33] way, this uh
[0:05:36] context usage or context windows usage
[0:05:38] can get compacted. VS Code and GitHub
[0:05:40] Copilot are going to be doing this
[0:05:43] intelligently in the background
[0:05:45] uh to mitigate this issue of the context
[0:05:47] window being filled up. But you can also
[0:05:50] manually invoke it by clicking here or
[0:05:52] you can also use slash compact here as
[0:05:55] well if you want to. Now, because this
[0:05:57] is a relatively small and
[0:06:00] straightforward session, the majority is
[0:06:03] being used by the system and uh not by
[0:06:06] our user context. But as we continue to
[0:06:08] add functionality to this code, uh we'll
[0:06:11] start to see these numbers grow and grow
[0:06:13] and perhaps the compact conversation is
[0:06:15] something we'll need to manually invoke
[0:06:16] later, but we are good for now. And that
[0:06:19] is it for this video. You understand the
[0:06:21] different levels of approval for the
[0:06:24] commands your agent is going to run. You
[0:06:26] also understand tool calls and how to
[0:06:29] see the calls that your agent is doing.
[0:06:31] And then finally, you understand context
[0:06:33] window and how to see what is consuming
[0:06:35] your context window. In the next video,
[0:06:38] we're going to see how we can review the
[0:06:40] changes that our agent has made and what
[0:06:43] should we do if we want to change the
[0:06:45] direction of work. All right, I'll see
[0:06:48] you in the next one.
