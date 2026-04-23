---
video_id: aW2jlbbUREc
title: "Review agents work with Agent Debug Logs and Chat Debug View"
url: https://www.youtube.com/watch?v=aW2jlbbUREc
channel: "@code (Visual Studio Code)"
published: 2026-04-06
speakers:
  - Gwyneth Peña-Siguenza
topics:
  - agent-debug-logs
  - chat-debug-view
  - troubleshooting
  - token-usage
relevance: primary
---

# Review agents work with Agent Debug Logs and Chat Debug View

In this video we dive into what's happening under the hood. We'll look at Agent Debug Logs and Chat Debug View and identify any troubleshooting we need to do.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | In this session |
| 00:29 | A look at the Agent Debug Logs |
| 02:50 | Chat Debug View |
| 05:30 | Troubleshooting and Token Usage |
| 08:00 | In Summary |
| 08:32 | What's Next - DEMO: Build Your First App with Agent Mode |

## Key Topics Covered

- **Agent Debug Logs**
- **Chat Debug View**
- **Troubleshooting**
- **Token Usage**

## Links

- https://youtu.be/hmfldW7dmgw
- https://aka.ms/vsc-learn
- https://x.com/code
- https://aka.ms/VSCode/LinkedIn
- https://bsky.app/profile/vscode.dev
- https://github.com/microsoft/vscode

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] In the last video, we understood how we
[0:00:02] can keep tabs on all the sessions that
[0:00:04] we've got going on. So, this video,
[0:00:07] we're going to dive deep into agent
[0:00:09] debug logs and the chat debug view, so
[0:00:13] we can gain a better understanding of
[0:00:15] what exactly our agents are doing, what
[0:00:18] do the calls to the LLMs look like, and
[0:00:20] if there are any troubleshooting things
[0:00:23] that we want to accomplish with this
[0:00:24] information, we're also going to learn
[0:00:27] how to do that. So, let's dive right in.
[0:00:29] Now, what should we do if the outputs of
[0:00:32] our agents, the results of our agents
[0:00:34] are not quite what we expect, or we have
[0:00:37] an skill or instruction that isn't being
[0:00:40] used? Well, the good thing about VS Code
[0:00:42] and the GitHub Copilot extension is that
[0:00:44] they're both open source, so there's a
[0:00:46] level of transparency that we can look
[0:00:48] into what exactly is going on, besides
[0:00:52] the obvious like tool calls and output
[0:00:53] that we see per session, right? So, what
[0:00:56] I'm going to do is I'm going to select
[0:00:58] one of these. Let's create this creating
[0:01:01] a gitignore, and I'll click on this
[0:01:02] little three-dot icon, and I'm going to
[0:01:05] click now on show agent debug logs. And
[0:01:08] just to get a little bit more space,
[0:01:10] we'll move this over here. And these are
[0:01:13] logs specific to this session, right?
[0:01:16] So, this chat session that we've got
[0:01:17] going on, and we can click on each one
[0:01:19] of these and get more information as to
[0:01:22] what exactly happened in that action.
[0:01:25] Now, we see here towards the beginning
[0:01:28] of a session, it's more focused on
[0:01:30] loading, so loading instructions,
[0:01:32] agents, hooks, skills. And if you have
[0:01:35] some custom skills, it'll most likely be
[0:01:37] loaded in here, and it'll show you which
[0:01:38] ones and the sources where it went to
[0:01:42] look for those files as well.
[0:01:44] And then finally, we have the message
[0:01:46] that I provided, and then each tool call
[0:01:49] and call to the model.
[0:01:50] The calls to the models will include
[0:01:53] token information, so in case you're
[0:01:55] looking to, I don't know, optimize your
[0:01:58] token usage, it's very, very useful to
[0:02:01] have that information there as well,
[0:02:03] right? If we click back, so we are in
[0:02:06] logs right now, we click back to the
[0:02:07] name of the session, and we click back
[0:02:10] once more, we actually have a list of
[0:02:11] all the sessions. We're going to go back
[0:02:13] to the one that we actively have open,
[0:02:15] it's labeled as active here. And we have
[0:02:18] a summary, the session type, local,
[0:02:21] location, status, created, and last
[0:02:24] activity, model turns, how many tool
[0:02:26] calls, total tokens, errors, and then
[0:02:29] total events. You can also click on
[0:02:30] agent flow chart, and here it'll show
[0:02:33] you everything in this, for lack of a
[0:02:35] better way of explaining it, flow chart
[0:02:37] style, and you can click on to the items
[0:02:40] that have more calls inside of them or
[0:02:42] more steps inside of them here, and you
[0:02:44] can review that that way as well. So,
[0:02:45] this is quite helpful for you to
[0:02:47] understand exactly how these things are
[0:02:49] working. And we also have another view,
[0:02:51] so if we go and click back there as
[0:02:53] well, we click on the show chat debug
[0:02:56] view. This is more focused on giving you
[0:02:59] all the raw data that gets sent to
[0:03:02] LLMs, right? So, I'm going to uh we'll
[0:03:05] expand this over just a little to get
[0:03:06] more information here, and we can click
[0:03:09] on one, let's click on, for example,
[0:03:13] let's see, refactor, the refactor one
[0:03:14] was pretty big, right? So, refactor to a
[0:03:17] fast API, right? And I'll click on the
[0:03:19] first one here, and I'll move this over
[0:03:21] just to get more information here. So,
[0:03:23] we can see that this is from the panel,
[0:03:26] so the actual uh area where the chat
[0:03:28] session is open, and then from here, we
[0:03:30] can see the request message and the
[0:03:32] system and the user messages and then
[0:03:35] what the response was. So, we can click
[0:03:37] on system, and then this includes the
[0:03:39] system message, right? And this will
[0:03:41] also include, if we go to the user
[0:03:44] section, any customizations that we have
[0:03:47] here. Uh so, user memory, I don't have
[0:03:48] any preferences saved here. And then uh
[0:03:52] further down, it will have information
[0:03:54] about the like the current date and
[0:03:56] where things are running, and then also
[0:03:58] our request here, build a base62 encoder
[0:04:01] decoder using Python 3.13, right? That
[0:04:04] was our first request. And then
[0:04:06] essentially, this is detailing that chat
[0:04:08] session up until that refactor to a fast
[0:04:10] API. So, if we scroll all the way down,
[0:04:13] our last user request should be, let's
[0:04:16] uh scroll up here. So, our tool calls, I
[0:04:20] know we should be able to see our last
[0:04:22] user request here. Here we go, here we
[0:04:25] go. User request refactor to a fast API,
[0:04:27] right? we have the assistant message
[0:04:30] here, and then if we scroll down, we'll
[0:04:32] take a look at the actual scroll down,
[0:04:35] scroll down to the actual response we
[0:04:38] got here. Uh here is a summary of what
[0:04:41] changed, and then that response that we
[0:04:43] actually got after it ran all the tools,
[0:04:46] all the calls that it needed to to
[0:04:48] execute this refactor to a fast API. So,
[0:04:51] this is pretty neat, if you hover over
[0:04:53] one of these calls, you should be able
[0:04:56] to get information. Actually, it's in
[0:04:58] the uh list itself, right? It says here
[0:05:00] the model,
[0:05:01] how long it took, and then the total
[0:05:03] tokens there. Uh so, it's very helpful
[0:05:05] for you to understand uh you know,
[0:05:08] what's going on here. Additionally, if
[0:05:10] we start a new like uh we can stay in
[0:05:14] this chat, actually. I can include this
[0:05:16] as context, so I can say debug event
[0:05:18] snapshot and say how many tokens did I
[0:05:22] use in this session, right? Session,
[0:05:25] right? And then I'm going to actually
[0:05:27] start another one, and I'll say slash
[0:05:30] troubleshoot, and this will allow us to
[0:05:32] investigate unexpected chat agent
[0:05:34] behavior by analyzing direct debug logs
[0:05:37] in JSONL files, right? So, I'll use
[0:05:39] troubleshoot, and let's ask, where are
[0:05:42] you loading skills from, right? So, in
[0:05:46] case I have a skill that's not picking
[0:05:47] up on, perhaps I it's not seeing it, or
[0:05:50] am I loading it in the wrong area,
[0:05:52] right? So, let's see if we got a
[0:05:53] response. And our Yep, so you can see
[0:05:56] that the sessions that are unread have a
[0:05:58] little blue dot, right? And then we have
[0:06:01] a based on three model turns in this
[0:06:02] session, we have total here,
[0:06:05] grand total of this many tokens. And we
[0:06:09] spoke briefly about context, and we can
[0:06:12] see here that uh the user context is
[0:06:14] 1.6%, which is a little bit more than
[0:06:16] that really basic one, but let's look at
[0:06:19] the uh where was our uh fork, this one
[0:06:24] did a Let's look at a longer one. No, we
[0:06:27] want to look at No, this one's pretty
[0:06:30] simple. Okay, here. This one should have
[0:06:32] uh No, did we Okay, we're going to allow
[0:06:35] all commands, we'll let that run, and
[0:06:37] we'll take a look at the context window.
[0:06:38] So, anyway, back to our troubleshoot
[0:06:41] usage, right? Troubleshoot, where are
[0:06:42] you loading skills from?
[0:06:44] It was able to use the correct context
[0:06:47] and tell us, okay, user level, workspace
[0:06:50] level,
[0:06:51] skills that it loaded. All the skills
[0:06:53] came from here, right?
[0:06:56] Uh but in case, for example, you have a
[0:06:58] skill that's not loading, this is the
[0:06:59] place to check out, right? Okay, so it
[0:07:01] looks like this is now done, the
[0:07:06] uh create the front end, and we can now
[0:07:07] start to see that our user context, the
[0:07:10] messages, are starting to increase,
[0:07:13] right? The tool results are starting to
[0:07:15] increase, right? And as well as the
[0:07:18] files starting to increase, right? But
[0:07:20] then of course, VS Code and GitHub
[0:07:21] Copilot in the background are
[0:07:22] intelligently uh compacting things for
[0:07:25] us, right? So, even though this perhaps
[0:07:27] used, let's say, debug, uh
[0:07:30] how many tokens have I used in this
[0:07:34] session, right? We'll go ahead and get
[0:07:36] this breakdown. We can see that even
[0:07:38] though we've used a certain amount of
[0:07:41] tokens here, it's not going to be the
[0:07:43] exact same, so we have total 214,000,
[0:07:47] which obviously is different, right?
[0:07:48] Than our context window. And we have the
[0:07:51] awesome capability of GitHub Copilot in
[0:07:53] VS Code in the background compacting
[0:07:56] that for us, so really only the
[0:07:58] important implementation details are
[0:07:59] what are consuming our context window.
[0:08:01] All right, and that's how you can
[0:08:03] leverage the agent debug logs and the
[0:08:05] chat debug view to better understand how
[0:08:09] your agents are working. And that is it
[0:08:11] for this video. You now understand where
[0:08:13] to go and find information on how your
[0:08:17] agent is working and the calls to the
[0:08:19] LLM. And if you want to troubleshoot
[0:08:22] anything with your setup, or if your
[0:08:24] agent's not behaving in the way that you
[0:08:26] expect, you know where to get that
[0:08:28] granular insight to figure out what's
[0:08:30] going on. And the next video, we're
[0:08:32] going to put it all together and build
[0:08:35] something from scratch.
