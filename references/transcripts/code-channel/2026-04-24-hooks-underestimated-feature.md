---
video_id: ZsyiRa91XZg
title: "Hooks: The Underestimated Feature | Ep 5 of 8"
url: https://www.youtube.com/watch?v=ZsyiRa91XZg
channel: "@code (Visual Studio Code)"
published: 2026-04-24
speakers:
  - Reynald Adolphe
topics:
  - hooks
  - lifecycle-events
  - automation
  - validation
relevance: primary
---

# Hooks: The Underestimated Feature

Reynald Adolphe demonstrates creating and modifying hooks that run commands at agent-session lifecycle events.

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] It seems that nobody talks enough about
[0:00:02] hooks.
[0:00:04] But they might be one of the most
[0:00:06] powerful features in VS Code right now.
[0:00:09] So, in this video, we'll break down what
[0:00:12] hooks are and how to use them to
[0:00:14] automate your workflow. So, without any
[0:00:17] further ado, let's do this. Hooks enable
[0:00:20] you to execute custom shell commands at
[0:00:23] lifecycle points during agent sessions.
[0:00:26] You want to use hooks to automate
[0:00:28] workflows and for security policies,
[0:00:32] validate operations, and integrate with
[0:00:35] external tools. Now, right here in the
[0:00:37] VS Code documentation, there's a few
[0:00:40] solid bullet points explaining why we'd
[0:00:42] want to use hooks. And actually, the
[0:00:44] second one is the one that I'm going to
[0:00:46] demonstrate in a real project,
[0:00:49] specifically for running a formatter. In
[0:00:51] fact, if we scroll down, that is one of
[0:00:53] the examples that they use, specifically
[0:00:56] with Prettier. And in this example, it
[0:00:58] creates a hook that runs Prettier after
[0:01:01] every file edit. One thing I do want to
[0:01:03] mention that integral to hooks are the
[0:01:06] lifecycle events because these are where
[0:01:09] you can indicate where the hook should
[0:01:12] be invoked. So, it could be for when
[0:01:15] there's a start session, a user prompt
[0:01:17] submit, etc. In our case, it's going to
[0:01:20] be for post tool use, which is
[0:01:23] appropriate for running a formatter. But
[0:01:25] let's go ahead and create one from
[0:01:26] scratch. All right. So, to create a
[0:01:28] hook, let's go ahead and check our agent
[0:01:32] customizations. Right now, there's
[0:01:33] currently no hooks there.
[0:01:35] But let's go ahead and select a generate
[0:01:38] hook. And here, I'm going to paste in
[0:01:41] what I want, which is to create a hook
[0:01:43] that's a user-level Copilot hook that
[0:01:46] automatically runs Prettier. And it
[0:01:47] should also be using post tool use hook
[0:01:50] with the shell script. Copilot goes to
[0:01:52] work, modifies the files that are
[0:01:54] needed, and we'll wait for it to finish
[0:01:57] and take a look to see what it created.
[0:01:59] All right, looks good. And it does
[0:02:01] mention
[0:02:03] right over here to test it to make sure
[0:02:04] that we reload.
[0:02:06] So, let's go ahead and reload the
[0:02:08] window. And let's take a look at the
[0:02:10] hook that it created. And this looks all
[0:02:13] right. I don't think we really need
[0:02:16] the timeout. I remember
[0:02:18] I didn't see that in the documentation.
[0:02:22] So, I'll get rid of that. Notice line 7,
[0:02:24] 18, and 20 are not formatted, but the
[0:02:28] hook should fix that. So, to see that,
[0:02:30] we'll ask it to make a change now. Can
[0:02:32] you go ahead and modify the wording for
[0:02:35] the first paragraph in the readme?
[0:02:40] I'll keep the default
[0:02:42] for that. We don't need to be too picky
[0:02:43] about the way it rewords it. And there
[0:02:46] you go. It reworded it and also
[0:02:49] formatted the document as we expected.
[0:02:53] So, the hook was properly invoked. To
[0:02:56] learn more about other customization
[0:02:58] features produced by our community,
[0:03:00] check out awesome Copilot at this URL
[0:03:03] here.
[0:03:05] I hope that this video showed you how
[0:03:07] hooks can quietly handle work for you in
[0:03:11] the background. Let me know in the
[0:03:13] comments
[0:03:14] what kind of hooks you'd create.
