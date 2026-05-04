---
video_id: d37Y28uU2JY
title: "Stop Prompting So Much. Do This Instead! | Ep 6 of 8"
url: https://www.youtube.com/watch?v=d37Y28uU2JY
channel: "@code (Visual Studio Code)"
published: 2026-04-24
speakers:
  - Reynald Adolphe
topics:
  - prompt-files
  - prompts
  - reusable-prompts
  - slash-commands
relevance: primary
---

# Stop Prompting So Much. Do This Instead!

Reynald Adolphe demonstrates prompt files for reusable workflows in VS Code.

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] If you're constantly repeating prompts,
[0:00:02] you're doing too much. There's a better
[0:00:04] way that most people still aren't using.
[0:00:07] In this video, we're going to learn
[0:00:08] about what prompt files are and the
[0:00:11] right way to use them.
[0:00:13] Let's jump right in. Prompt files are
[0:00:15] reusable markdown files that define
[0:00:18] instructions or context for chat
[0:00:21] sessions. You reference them in chat to
[0:00:24] provide consistent, repeatable prompts
[0:00:27] across your team or workflow. Here what
[0:00:30] we're looking at is the VS Code
[0:00:31] documentation that covers prompt files
[0:00:35] in detail. But let's go ahead and take a
[0:00:37] look at an example to see it in action.
[0:00:39] Now, what we're looking at is a
[0:00:41] script.js file for a calculator app. And
[0:00:44] as you can see on the left-hand side
[0:00:46] here under the explorer, there's quite a
[0:00:48] few other files associated with it. One
[0:00:50] of which is under a GitHub folder for
[0:00:53] prompts, you'll see quiz open files. And
[0:00:57] this is a prompt file that I've created
[0:01:00] that will allow me to have VS Code quiz
[0:01:03] me on the code for the open files. And
[0:01:05] this is a great way for me to study new
[0:01:07] code that Copilot had created for me.
[0:01:10] So, if I hit {slash} and type in Q,
[0:01:14] you'll see that there's quiz open files.
[0:01:16] And when I execute this, it generates
[0:01:19] basically tech questions for the code
[0:01:21] that it sees in its context. And as you
[0:01:23] can see, it does this in a
[0:01:25] multiple-choice format. And this is a
[0:01:28] result of the prompt file that I
[0:01:29] created. And what makes this great as a
[0:01:31] prompt file is during the course of
[0:01:33] development, this is an action that I
[0:01:36] might want to repeat several times. And
[0:01:38] I would not want to repeat this prompt
[0:01:41] because there's a lot of detail that's
[0:01:43] involved with the prompt. When we open
[0:01:45] the UI for agent customizations by
[0:01:48] clicking the cog icon, and I'll go back
[0:01:50] to just reopen it to show you. The cog
[0:01:52] icon was right here to open
[0:01:54] customizations. I can simply hop over to
[0:01:57] prompts and see the prompt files that
[0:01:59] are available, the built-in ones and the
[0:02:01] custom ones that I created, such as quiz
[0:02:03] open file. And you can see the work that
[0:02:06] it's supposed to do, to quiz me on the
[0:02:08] code in currently open files, and to
[0:02:11] generate five multiple-choice questions.
[0:02:13] And then there's several rules involved.
[0:02:16] So, this is all information that I would
[0:02:18] not want to have to keep on repeating.
[0:02:20] If this was a prompt I would just want
[0:02:22] to do once per project, then there's no
[0:02:24] sense in creating a prompt file. But
[0:02:26] because this is something I might want
[0:02:28] to do for several files within a
[0:02:30] project, if it's not for the script
[0:02:31] file, maybe it's for the index file,
[0:02:33] maybe it's for the package.json,
[0:02:35] and I'd want to be quizzed on any one of
[0:02:37] those, it makes perfect sense to have a
[0:02:40] prompt file such as this. But now let's
[0:02:42] turn our attention to creating a new one
[0:02:44] from scratch.
[0:02:45] Let's say I wanted to create a prompt
[0:02:48] file for minimizing bloated code. So,
[0:02:51] for example, we're looking at the
[0:02:54] script.js file.
[0:02:56] Maybe this could be refactored to be
[0:02:58] shorter, or maybe not. But it would be
[0:03:00] nice to have a prompt that can do that
[0:03:03] work and then explain to me what it did.
[0:03:05] Why don't we go ahead and hit {slash}
[0:03:08] and start typing in create. And now we
[0:03:10] have our options to create from several
[0:03:12] customization features. One is to create
[0:03:15] a prompt, and then I'll say
[0:03:17] to simplify and reduce bloated code and
[0:03:20] tell me what you did. And we'll be more
[0:03:22] specific here for this particular
[0:03:24] scenario, so it doesn't just do it for
[0:03:26] the whole project and say for open
[0:03:30] files.
[0:03:32] So, it looks like it went ahead and did
[0:03:34] it. As I look through the details, it
[0:03:36] looks like it did it at the workspace
[0:03:38] level. So, now if we go to our agent
[0:03:41] customizations, we should see it right
[0:03:44] under workspace, simplify code. And it's
[0:03:47] literally as easy as that. And we could
[0:03:49] have now at this point review it and
[0:03:51] modify it accordingly or ask Copilot to
[0:03:53] modify it. Now, there is one thing that
[0:03:55] I'd like to have it change is instead of
[0:03:58] as a at the workspace level, I'm going
[0:04:00] to have it move it to be at the user
[0:04:03] level so that I could use this nice
[0:04:05] prompt in other projects. Thanks for
[0:04:07] creating the prompt file, but can you
[0:04:10] change it so that it's at the user level
[0:04:14] so that I can use it for other projects
[0:04:17] and not just for this one? All right, so
[0:04:20] now it moved it to my user profile. And
[0:04:23] we see it under built-in now.
[0:04:26] So, let's go ahead and
[0:04:28] give this a shot.
[0:04:30] Simplify and reduce bloated code. I'm
[0:04:33] actually really excited to see what it
[0:04:35] does
[0:04:37] because this way you could make note of
[0:04:39] which models tend to be a little bit
[0:04:40] more efficient versus others. And when I
[0:04:44] say more efficient, I mean in terms of
[0:04:46] the way that it writes code that is not
[0:04:48] bloated. Okay, looks like it's made some
[0:04:51] changes here and it describes exactly
[0:04:54] what it did to simplify the code.
[0:04:56] Starting out with the extracting and
[0:04:58] some hoisting and some code replaced in
[0:05:01] addition to simplification of some
[0:05:03] keyboard handlers. Nice. And again, the
[0:05:05] reason why this makes sense to be a
[0:05:07] prompt file because as you continue
[0:05:09] building your projects, this is
[0:05:11] something you'd want to use over and
[0:05:13] over. So, in short, the reason why this
[0:05:15] matters is instead of having to rewrite
[0:05:18] prompts, you can define them once and
[0:05:20] reuse them across your project, which
[0:05:22] means faster workflows and consistent AI
[0:05:25] behavior. To learn more about other
[0:05:27] customization features produced by our
[0:05:30] community, check out awesome Copilot at
[0:05:33] this URL here.
[0:05:35] Hope this video helps you rethink how
[0:05:38] you interact when prompting. Before you
[0:05:41] go, let me know in the comments what
[0:05:42] prompt files have you created. Thanks
[0:05:45] for joining and I will see you in the
[0:05:47] next one.
