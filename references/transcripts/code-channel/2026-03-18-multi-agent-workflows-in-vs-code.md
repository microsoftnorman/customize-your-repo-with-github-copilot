---
video_id: J5KTpq7hVn4
title: "Multi-agent workflows in VS Code"
url: https://www.youtube.com/watch?v=J5KTpq7hVn4
channel: "@code (Visual Studio Code)"
published: 2026-03-18
speakers:
  - Kayla Cinnamon
topics:
  - multi-agent
  - agent-sessions
  - parallel-work
  - documentation
relevance: primary
---

# Multi-agent workflows in VS Code

With multi-agent support in VS Code, you can work on multiple tasks in parallel - no more waiting for one to finish before starting the next. In this video, we'll show you how to run agents side by side to tackle tasks like implementing color themes, adding storage functionality, and creating documentation, all at the same time.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Intro |
| 00:08 | Project overview |
| 01:00 | Working with multiple agent sessions |
| 03:11 | Results and tips |
| 05:00 | Outro |

## Key Topics Covered

- **Multi Agent**
- **Agent Sessions**
- **Parallel Work**
- **Documentation**

## Links

- https://code.visualstudio.com/docs/copilot/agents/overview
- https://x.com/code
- https://bsky.app/profile/vscode.dev
- https://aka.ms/VSCode/LinkedIn
- https://github.com/microsoft/vscode

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Did you know that you can run multiple
[0:00:01] sessions at once in VS Code all using
[0:00:04] different models and all working in
[0:00:05] parallel? Let's take a look at how that
[0:00:07] works.
[0:00:08] So, here we are in VS Code and I already
[0:00:10] have a session that I ran to get the
[0:00:12] project started. This project is a log
[0:00:15] analyzer where you can drop in log files
[0:00:18] and they will use the Copilot SDK to
[0:00:20] analyze them and give you information on
[0:00:23] what's happening in the log files in a
[0:00:24] more summarized view. Now, there are a
[0:00:26] few things that I want to do with this
[0:00:27] project that I can do in parallel using
[0:00:30] multiple sessions in VS Code. The first
[0:00:32] is that I want to add a bunch of
[0:00:33] different color schemes for the page and
[0:00:36] the second is that I want to store any
[0:00:37] log files that I've dropped in here so I
[0:00:40] can compare to ones in the past to see
[0:00:42] if the same issue has been occurring and
[0:00:44] it's already found a similar log item
[0:00:46] from an issue that's been filed
[0:00:48] potentially weeks ago. And then lastly,
[0:00:50] it could be nice to have some
[0:00:51] documentation about this website so if
[0:00:53] people want to come and use it, they
[0:00:54] could see what it means to have
[0:00:56] patterns, anomalies, and root causes
[0:00:58] within their log files. So, I started
[0:01:00] this project using a session and then
[0:01:03] when I ran the log file in the website,
[0:01:06] it kicked off a Copilot SDK session
[0:01:09] which is connected to the GitHub Copilot
[0:01:12] CLI.
[0:01:13] So, if we open this session, you could
[0:01:15] see here at the bottom that this is
[0:01:17] connected to a Copilot CLI session.
[0:01:20] Okay, to start, let's do a new session
[0:01:22] for adding color schemes. So, I'm going
[0:01:24] to use Claude Sonnet 4.6 for this
[0:01:26] because this task isn't necessarily
[0:01:28] in-depth and doesn't require a ton of
[0:01:29] research. So, we can say come up with a
[0:01:32] few different
[0:01:36] color schemes for this website.
[0:01:39] Let's have the user select one at the
[0:01:42] top right
[0:01:44] of the page.
[0:01:47] Make sure the theme applies to all
[0:01:49] pages.
[0:01:51] And then we can send that off. Now, this
[0:01:52] is working and we can go back to our
[0:01:55] main view of all of our sessions and add
[0:01:57] a new one and keep going. So, now we
[0:02:00] want to have a back end to store any log
[0:02:02] files that have previously been dropped.
[0:02:04] I'm going to change my model to Claude
[0:02:05] Opus 4.6 cuz I think this is going to be
[0:02:07] more of an in-depth task and it maybe I
[0:02:10] want to plan as well. So, I'll change
[0:02:12] this to plan.
[0:02:14] And we can say I want to store
[0:02:17] any log files that have previously been
[0:02:20] analyzed
[0:02:22] by this tool
[0:02:24] so we can find similarities
[0:02:27] between ones that have been looked at
[0:02:31] before. Come up with an architecture
[0:02:33] plan that's as simple as possible.
[0:02:38] Okay. And then lastly, we want
[0:02:40] documentation. So, I'm going to jump
[0:02:41] back again and we can change the model
[0:02:43] to something different like GPT-4. I
[0:02:47] don't think we need plan either. We
[0:02:48] could just go straight to agent and we
[0:02:50] can say
[0:02:51] I want to have thorough
[0:02:53] documentation
[0:02:55] to teach users how to use this website
[0:02:59] and what each of the fields mean when
[0:03:02] looking at their log analyses.
[0:03:06] Add some markdown pages to this repo.
[0:03:11] Now, when you're working with multiple
[0:03:12] sessions, I recommend not working on the
[0:03:15] same pieces of the code base all at once
[0:03:17] because you might run into some
[0:03:18] conflicts, but adding color schemes with
[0:03:21] a back end for file storage along with
[0:03:23] documentation shouldn't really have much
[0:03:25] overlap. Another way you could do this
[0:03:27] locally without contributing directly to
[0:03:29] the branch itself is you can switch to
[0:03:31] the Copilot CLI here at the bottom and
[0:03:33] then you can choose work tree and this
[0:03:35] will create a work tree off of your
[0:03:36] branch so you won't have conflicts
[0:03:38] within the sessions themselves.
[0:03:41] And now it looks like the color scheme
[0:03:42] one has finished. We can take a look at
[0:03:43] how that did.
[0:03:45] And now back on the website, we can see
[0:03:46] that it added these different color
[0:03:49] scheme options which is cool
[0:03:51] and we can click through them which is
[0:03:52] nice as well. It also looks like the
[0:03:54] architecture plan is finished and we can
[0:03:56] look through the results of that, figure
[0:03:58] out if this is the plan that we want to
[0:04:00] actually implement, and the
[0:04:01] documentation looks like it's done, too.
[0:04:03] So, now I just did three different
[0:04:04] things that have been on my to-do list
[0:04:06] all within a couple minutes and nothing
[0:04:08] conflicted with each other because
[0:04:09] they're all touching different pieces of
[0:04:10] the code base. So, when you're in VS
[0:04:12] Code, you can leverage multiple sessions
[0:04:14] in parallel to get work done and you can
[0:04:17] leverage all the different models that
[0:04:18] VS Code has available as well to use the
[0:04:21] model that's most tailored to the task
[0:04:23] that you want to complete. And if you
[0:04:24] want to be really hands-off, you can
[0:04:26] change the approval method to bypass
[0:04:29] approvals or even autopilot so
[0:04:31] everything just works on its own and you
[0:04:33] don't have to be pinged every time
[0:04:34] Copilot needs a decision. So, that's
[0:04:36] something else you can take into account
[0:04:38] when you're running multiple sessions at
[0:04:39] once and you want to get a lot of work
[0:04:40] done all at the same time.
[0:04:43] Here are the docs that were created and
[0:04:45] then the architecture plan as well which
[0:04:47] has the key decisions that I can look
[0:04:49] through and if I like this plan, I can
[0:04:51] simply click start implementation or
[0:04:53] start with autopilot and then this will
[0:04:55] start working for me
[0:04:56] all while those other sessions are
[0:04:58] working, too.
[0:04:59] So, go ahead and get started using
[0:05:00] multiple sessions in VS Code, see how
[0:05:02] you do, and let us know in the comments
[0:05:04] what you've been able to achieve.
