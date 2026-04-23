---
video_id: 0CsKOO7d35I
title: "Agent sessions and where agents run"
url: https://www.youtube.com/watch?v=0CsKOO7d35I
channel: "@code (Visual Studio Code)"
published: 2026-04-06
speakers:
  - Gwyneth Peña-Siguenza
topics:
  - agent-sessions
  - agent-modes
  - cloud-agents
  - parallel-work
relevance: primary
---

# Agent sessions and where agents run

In this video we'll walk through how to keep tabs on all the work we've asked the agent to do!

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | In this session |
| 00:21 | Session view |
| 02:09 | Options for where to run this session |
| 03:40 | Agent modes and when to use them |
| 04:18 | Using Cloud agents for async work |
| 06:08 | Running multiple agent sessions at once |
| 07:05 | In Summary |
| 07:20 | What's Next - Review agents work with Agent Debug Logs and Chat Debug View |

## Key Topics Covered

- **Agent Sessions**
- **Agent Modes**
- **Cloud Agents**
- **Parallel Work**

## Links

- https://youtu.be/aW2jlbbUREc
- https://aka.ms/vsc-learn
- https://x.com/madebygps
- https://x.com/code
- https://aka.ms/VSCode/LinkedIn
- https://bsky.app/profile/vscode.dev
- https://github.com/microsoft/vscode

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] So in the last video, we were able to
[0:00:02] edit a prompt we sent and steer the
[0:00:05] direction of the agent's work. We
[0:00:07] reviewed checkpoints and forking a
[0:00:10] session and a bunch more.
[0:00:12] Now we have a bunch of sessions. So in
[0:00:14] this video, we're going to focus on how
[0:00:16] we can keep tabs on all the work that is
[0:00:19] going on. So let's dive right in. We
[0:00:21] have been creating a couple of sessions.
[0:00:25] We started with one and then we created
[0:00:29] a fork. We see here forked, right? And I
[0:00:32] want to take some time to review the
[0:00:34] session view which we have here, right?
[0:00:36] So we can switch between the sessions by
[0:00:40] obviously clicking on the name.
[0:00:42] If you right-click, you have options to
[0:00:45] archive, rename, or delete. Right? In
[0:00:48] case you are completely done with the
[0:00:49] session, you can archive it.
[0:00:51] Deleting will, of course, delete all the
[0:00:53] history. So keep that in mind. And then
[0:00:56] renaming for your organizational
[0:00:59] preferences, you can rename if you'd
[0:01:01] like your session here as well. I can
[0:01:03] also go ahead and click into the plus
[0:01:07] sign here and create a new session. Or
[0:01:10] you have this new session button here as
[0:01:12] well. And if we expand to the right
[0:01:15] here, this plus sign, we have a new chat
[0:01:18] or new Copilot CLI session, which will
[0:01:21] allow us to kick off a GitHub Copilot
[0:01:24] CLI session inside of VS Code. We'll see
[0:01:27] that shortly launch into the GitHub
[0:01:31] Copilot CLI. We're not only about
[0:01:33] developer choice when it comes to the
[0:01:35] model, to the thinking capacity / level,
[0:01:39] but also the UX. If you're more of a
[0:01:41] terminal-based person, the Copilot CLI
[0:01:44] has your back for that. But if you want
[0:01:46] to work primarily inside of the VS Code
[0:01:49] and in this type of UI, that works as
[0:01:51] well, right? So I'm just going to close
[0:01:52] this. We're going to have videos
[0:01:53] covering the GitHub Copilot CLI in
[0:01:55] depth, so I won't touch too much upon
[0:01:58] that here. Now additionally, we can
[0:02:00] create sessions in a bunch of different
[0:02:03] areas, right? I'm going to actually
[0:02:04] delete this here and I'm going to click
[0:02:06] on the plus sign, create a new session
[0:02:08] here. We have a variety of places where
[0:02:12] we can sort of have the work of the
[0:02:14] session run, right? So if I click on
[0:02:15] this local, we have the option to run
[0:02:17] this locally, which is what we've been
[0:02:19] doing, Copilot CLI, which will delegate
[0:02:21] tasks to a background agent running
[0:02:24] locally on our machine, but it's running
[0:02:26] with a GitHub Copilot CLI. And then we
[0:02:28] can also run this on the GitHub
[0:02:31] platform. So the actual compute is not
[0:02:34] on your computer, it's running in the
[0:02:36] platform, which is something we can kick
[0:02:39] off now if we do like, right? So let's
[0:02:41] think of a task. So what I'm going to
[0:02:43] first do is take a look at our changes
[0:02:46] here and we can probably commit
[0:02:50] everything, but I see we have some files
[0:02:53] that shouldn't be in our version
[0:02:54] control. This probably wouldn't have
[0:02:56] happened if we had some custom
[0:02:57] instructions, but we are actually going
[0:03:00] to cover customization for agents in the
[0:03:02] next video. So I won't talk too much
[0:03:04] about that, but all I'll say here is
[0:03:06] look at and I'm going to say changes,
[0:03:09] which includes the information on the
[0:03:10] changes as context. We have some test
[0:03:14] files that should not be included.
[0:03:18] Create a gitignore and appropriate
[0:03:22] gitignore for our project.
[0:03:26] Fantastic. And I'll go ahead and send
[0:03:28] that over. Now, this is again just
[0:03:30] running locally. We're using the changes
[0:03:33] as context here. But another thing I
[0:03:36] wanted to show you while we're here
[0:03:37] before we kick off a cloud session is we
[0:03:40] have different modes and we're going to
[0:03:42] use a different mode when we move into
[0:03:45] the last video where we'll put
[0:03:46] everything together.
[0:03:47] But plan mode will turn the agent into
[0:03:52] just the planner. It'll have a back and
[0:03:54] forth with you, outline a plan of attack
[0:03:57] for the work that you want to implement.
[0:03:59] Ask mode will make the agent be more
[0:04:02] sort of like traditional chatbot. And
[0:04:04] then agent is the actual mode that will
[0:04:06] allow work to be done, right? So keep
[0:04:09] those in mind. If you're just starting,
[0:04:11] stick with ask and plan mode, have a
[0:04:12] back and forth, and when you're ready,
[0:04:14] go ahead and implement with agent mode.
[0:04:17] Great. So I'm going to go ahead here and
[0:04:20] type in initial commit and then I'll
[0:04:22] just push everything over to our
[0:04:24] repository. I'm going to hit plus here
[0:04:27] and we again see that our sessions are
[0:04:29] getting added into our list of sessions
[0:04:32] here and I'm going to switch over to
[0:04:34] cloud. And then I will say write a read
[0:04:38] read me for our project. Go ahead and
[0:04:42] send that off. And I'm going to go back
[0:04:44] here to our file explorer and we do have
[0:04:48] a read me, but it's empty at the moment.
[0:04:51] So I'm going to click on our GitHub
[0:04:53] extension and we see here that we now
[0:04:56] have a new pull request. I'm going to
[0:04:59] open that up as well. And then just to
[0:05:00] get some more space here, I'll move this
[0:05:02] over here. I'll move this over here. And
[0:05:05] we see that a pull request that is
[0:05:07] labeled as work in progress, add read me
[0:05:08] file for project documentation, has
[0:05:11] started. So Copilot has kicked off this
[0:05:13] work, but this is actually running on
[0:05:15] github.com. If we go ahead and open this
[0:05:18] again, we can see that the work is in
[0:05:20] progress. It has a little bit of a spin
[0:05:22] spinner icon here and we can see this
[0:05:25] working here and let me show you what it
[0:05:26] looks like in github.com. I am in
[0:05:29] github.com in my repository. If I click
[0:05:31] on agents, we'll be able to see that
[0:05:34] agent session running as well here,
[0:05:36] right? And we can see all the work that
[0:05:39] is happening. That pull request is also
[0:05:41] in here. I can click on this here. From
[0:05:44] here, we are also able to click on the
[0:05:46] view session and see the work of the
[0:05:49] agent running. See the model. We can see
[0:05:51] how many premium requests this took and
[0:05:54] all the tool costs and such, we can also
[0:05:57] see them similar to how we would in VS
[0:05:59] Code. Now of course, the benefit here is
[0:06:02] I can just have this running and then
[0:06:03] create a new session and then focus on
[0:06:06] other work that I would want to do. For
[0:06:07] example, can I'm just going to make sure
[0:06:10] I switch this to local. Can we create a
[0:06:14] simple front end with HTML and static
[0:06:19] templates? We want just a field. There
[0:06:22] we go. I have to type in the URL to
[0:06:27] shorten. There we go. We can go ahead
[0:06:29] and send this off. And then the work
[0:06:32] that is happening in this session, we're
[0:06:34] able to view. So if we move over to this
[0:06:36] cloud one and then we hover over this
[0:06:38] one, we see that this one is also doing
[0:06:41] work and this is running locally. We
[0:06:43] click on this one, we hover over the
[0:06:46] other one, we can see this one is
[0:06:47] running in the cloud as well. This is a
[0:06:50] way that you can sort of run things
[0:06:53] async on the GitHub platform. Again, you
[0:06:56] can also leverage the the Copilot CLI if
[0:06:59] you'd like to. So I'll hit plus here,
[0:07:01] the Copilot CLI, and then we also have
[0:07:03] third-party agents that you can leverage
[0:07:05] as well. That is it for this video. You
[0:07:06] now know how to move about different
[0:07:09] sessions, how to kick off different
[0:07:11] sessions at the same time. You also
[0:07:13] understand that you can kick off a
[0:07:14] session locally, in the cloud, in the
[0:07:17] Copilot CLI, and a bunch more. So in the
[0:07:20] next episode of this series, what we're
[0:07:23] going to cover is how we can really get
[0:07:26] under the hood and fully understand the
[0:07:28] different calls and actions that our
[0:07:30] agents are doing and how to understand
[0:07:33] the actual calls that are happening to
[0:07:35] the LLMs and a bunch more information.
[0:07:37] So I'll see you in the next video.
