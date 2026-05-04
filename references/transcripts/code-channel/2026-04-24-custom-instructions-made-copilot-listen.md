---
video_id: dk2biPguo_E
title: "Custom Instructions: How I Really Made Copilot Listen! | Ep 2 of 8"
url: https://www.youtube.com/watch?v=dk2biPguo_E
channel: "@code (Visual Studio Code)"
published: 2026-04-24
speakers:
  - Reynald Adolphe
topics:
  - custom-instructions
  - instructions
  - coding-standards
  - accessibility
relevance: primary
---

# Custom Instructions: How I Really Made Copilot Listen!

Reynald Adolphe demonstrates creating custom instructions so GitHub Copilot follows coding standards, conventions, and accessibility expectations.

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] You've probably been lied to about
[0:00:01] custom instructions if you're not using
[0:00:03] them properly. They're way more powerful
[0:00:06] than people make them sound. We're going
[0:00:08] to break down what custom instructions
[0:00:09] really are,
[0:00:11] how they're meant to be used, and then
[0:00:13] demonstrate it. Let's take a look. A
[0:00:15] custom instruction is like a rulebook
[0:00:18] for the AI in VS Code. It's a markdown
[0:00:21] file where you define your coding style,
[0:00:24] conventions, and preferences, and the AI
[0:00:27] automatically follows them in every
[0:00:29] chat. On this page here are some
[0:00:31] detailed information regarding custom
[0:00:33] instructions with some examples, but
[0:00:36] let's go ahead and take a look at one in
[0:00:37] action from an existing project of mine.
[0:00:40] Here I have a calculator app, and this
[0:00:44] is one of the files associated with it,
[0:00:46] a JavaScript file. And what we're going
[0:00:48] to do
[0:00:50] is go to the customization UI by hitting
[0:00:53] this gear icon here. And if we look
[0:00:56] under custom instructions, you could see
[0:00:58] I currently have one called solid
[0:01:00] principles, which when we click, we
[0:01:03] could see exactly how the custom
[0:01:05] instructions should work, which is to
[0:01:06] apply the solid principles to my code
[0:01:09] whenever it's being created or
[0:01:12] refactored. Now, towards the end here, I
[0:01:15] did specify to let us know that it
[0:01:18] applied by having this confirmation
[0:01:20] section here, so it should tell us in
[0:01:22] the chat when it applied solid
[0:01:24] principles. So, let's ask it to refactor
[0:01:28] this script, and I'm not going to give
[0:01:30] it any specific ways to refactor it, but
[0:01:32] I'll just let it do it and then see if
[0:01:35] any of the solid principles have been
[0:01:37] applied. Can you go ahead and refactor
[0:01:40] this script as you see fit?
[0:01:44] And right off the bat, you could see as
[0:01:46] it's going through the process, it
[0:01:49] immediately told me that here's what I
[0:01:51] found analyzing the code against solid
[0:01:53] principles, and indicated some of the
[0:01:55] changes that it's going to apply to stay
[0:01:57] aligned with the solid principle. And it
[0:01:59] mentioned a few more principles, and now
[0:02:01] it's done. And what's great about this
[0:02:04] is as I continue building on this
[0:02:06] project, it will consistently do this,
[0:02:09] so I don't have to go back and think to
[0:02:11] myself, am I following the principles
[0:02:13] accordingly? Because according to my
[0:02:15] instructions, it will make sure that AI
[0:02:17] does it all the time. And if I check to
[0:02:20] make sure that my calculator works,
[0:02:22] looks like it still works. Now, why
[0:02:24] don't we go ahead and create one from
[0:02:26] scratch? So, if I bring up the agent
[0:02:30] customization UI, I can come over here
[0:02:33] and choose generate new instruction
[0:02:36] files, and I'm going to want to do it at
[0:02:38] the user level, and this will be for
[0:02:40] Copilot. And we'll call this
[0:02:42] accessibility.
[0:02:44] And now I can go ahead and create the
[0:02:47] description that I want and the details
[0:02:49] for accessibility. And this is an
[0:02:51] approach if I wanted to do this
[0:02:53] manually, but an easier way to do this
[0:02:56] is to simply ask Copilot. So, I'm going
[0:02:58] to discard this, and to do so, we could
[0:03:01] just back out and hit the trash can
[0:03:03] right here under accessibility. And if
[0:03:05] we go to chat and typed in {slash}
[0:03:08] create and hit instructions, and I
[0:03:11] entered for the user profile level to
[0:03:14] ensure all UI code meets WCAG
[0:03:18] standards, and then also to let me know
[0:03:20] in the chat when you did this so that I
[0:03:22] know that it worked. And now I don't
[0:03:24] need to manually do the work to specify
[0:03:27] how the instructions should be. I could
[0:03:29] let Copilot create it and then review it
[0:03:32] and modify it if I need to. I'll give it
[0:03:34] the permission that it needs to
[0:03:35] continue.
[0:03:37] Okay, so now I could see that it created
[0:03:40] the instructions files, and that it's
[0:03:43] also going to confirm whenever it
[0:03:45] applies the accessibility standards. So,
[0:03:47] by hopping over to the agent
[0:03:49] customizations UI, now I see my WCAG
[0:03:53] accessibility instructions, and look at
[0:03:55] all this that it created within just a
[0:03:58] few seconds. And the minute I did at the
[0:04:00] top, the description explains the
[0:04:03] purpose of the instruction. It tells the
[0:04:06] assistant when to use these
[0:04:08] accessibility rules, and the apply to
[0:04:11] field finds which file types the
[0:04:14] instruction should automatically target,
[0:04:16] such as HTML, CSS, view files, et
[0:04:19] cetera. And below are the remaining
[0:04:22] specific instructions, all created
[0:04:25] within seconds. So, let's go ahead and
[0:04:27] give it a shot. We have the way that my
[0:04:29] calculator currently looks, and ideally
[0:04:33] if I just ask it to update it to be more
[0:04:36] modern or something to the effect that
[0:04:39] it change that it changes the UI, it
[0:04:41] should also apply my custom
[0:04:43] instructions. So, I'll just ask, can you
[0:04:46] make the UI of my calculator look,
[0:04:51] actually instead of saying modern, let's
[0:04:53] just say like it's from an 80s arcade.
[0:04:59] So, if all goes well, theoretically
[0:05:01] because it's making some UI changes, it
[0:05:03] should also know to make sure that it is
[0:05:06] WCAG compliant. All right, it looks like
[0:05:10] it finished, and if I hit refresh, there
[0:05:12] you go. That really does look like it's
[0:05:14] from the 80s. And as you could see, it
[0:05:17] applied the WCAG standards, and we can
[0:05:19] look at the details right over here.
[0:05:21] Custom instructions for individual
[0:05:23] developers is very helpful, but for
[0:05:26] teams, it's even more powerful. Imagine
[0:05:29] every developer in the repo having
[0:05:31] Copilot follow the same coding
[0:05:33] conventions, naming stays consistent,
[0:05:35] formatting stays consistent,
[0:05:37] architectural patterns also consistent.
[0:05:40] This saves a lot of time, and instead of
[0:05:42] having to review AI output and
[0:05:44] correcting it later, it's all done up
[0:05:46] front with custom instructions. To learn
[0:05:48] more about other customization features
[0:05:50] produced by our community, check out
[0:05:52] awesome Copilot at this URL here.
[0:05:57] Ideally, you now feel more confident
[0:05:59] working with custom instructions to
[0:06:02] control your workflow. Let me know in
[0:06:04] the comments how you use custom
[0:06:06] instructions. If you're curious about
[0:06:09] going beyond instructions,
[0:06:11] agent skills are natural next concept to
[0:06:14] explore.
