---
video_id: Y7MPeZTIgqo
title: "Let's Build a Custom Agent! | Ep 4 of 8"
url: https://www.youtube.com/watch?v=Y7MPeZTIgqo
channel: "@code (Visual Studio Code)"
published: 2026-04-24
speakers:
  - Reynald Adolphe
topics:
  - custom-agents
  - agent-mode
  - security-reviewer
  - specialized-agents
relevance: primary
---

# Let's Build a Custom Agent!

Reynald Adolphe demonstrates creating a specialized custom agent in VS Code, including a security reviewer agent mode.

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Are custom agents really powerful? What
[0:00:02] makes something a custom agent? In this
[0:00:05] video, we're going to break down what
[0:00:07] custom agents are and how to use them by
[0:00:10] building one from scratch and show
[0:00:13] exactly the best way to use one in a
[0:00:15] real workflow. So, let's go ahead and
[0:00:19] jump right in. Custom agents enable you
[0:00:21] to configure the AI to adopt different
[0:00:24] personas tailored to specific
[0:00:26] development roles and tasks. So, for
[0:00:29] example, you might create agents for a
[0:00:32] security reviewer, planner, solution
[0:00:35] architect, or other specialized roles.
[0:00:38] And each persona can have its own
[0:00:40] behavior, available tools, and
[0:00:43] instructions. Now, this here is the
[0:00:45] documentation for custom agents on VS
[0:00:48] Code's uh website. Well, let's go ahead
[0:00:51] and take a look at an existing project.
[0:00:54] So, right here, I'm in a project for an
[0:00:56] arcade-themed calculator. And what I'd
[0:00:59] like to show you is under agents, we
[0:01:02] have one that I created called security
[0:01:05] reviewer and then some built-in ones.
[0:01:08] And this is an excellent example of a
[0:01:10] custom agent right here that's going to
[0:01:12] be used when reviewing code for security
[0:01:15] vulnerabilities, auditing for secrets
[0:01:18] and credential leaks, and a lot more.
[0:01:20] So, let's go ahead and test this
[0:01:23] security reviewer, which is under
[0:01:25] workspace. I go into the chat using the
[0:01:29] at sign, enter in security reviewer, ask
[0:01:32] it to review this file for
[0:01:34] vulnerabilities, and focus on our
[0:01:37] JavaScript file. Actually, let me stop.
[0:01:40] We want to make sure that this is in
[0:01:42] agent mode. Give it another shot. So, as
[0:01:45] you can see, it gives us a lot of
[0:01:46] information here starting off with a
[0:01:50] review of the results, and then it
[0:01:52] categorizes some concerns starting from
[0:01:55] a level of low. And I assume if we had
[0:01:58] more that was serious, it would have
[0:01:59] like probably medium and high, but we
[0:02:02] only have low right now, which is pretty
[0:02:05] good. But, let's go ahead and create a
[0:02:08] new custom agent. And I want to try
[0:02:11] something new. Why don't we have Copilot
[0:02:14] suggest a custom agent for us? So, I'm
[0:02:17] going to ask, "Based on my current
[0:02:19] project, what custom agent can I create
[0:02:22] for my video demo?" And that's exactly
[0:02:24] the video that you're watching right
[0:02:25] now. Can you tell me a prompt to tell
[0:02:28] Copilot to create one? And tell me why
[0:02:31] it makes a good custom agent. This is
[0:02:35] very meta here because while creating an
[0:02:38] example, I'm actually using Copilot to
[0:02:41] assist me. And one of the reasons I want
[0:02:43] to show this is because
[0:02:45] as you're developing your projects, it's
[0:02:48] good to get into the habit of thinking
[0:02:51] of Copilot as a way of helping you on
[0:02:53] many different levels, not just writing
[0:02:56] code. So, let's see what it came up with
[0:02:58] here. It says, "Create an arcade-themed
[0:03:00] scientific calculator with sound
[0:03:02] effects, theme toggling, and solid
[0:03:04] architecture. My recommendation is a
[0:03:06] domain-specific
[0:03:08] agent that knows your calculator's
[0:03:10] architecture, retro aesthetics, and
[0:03:12] coding pattern." So, this is what it
[0:03:14] suggested here, a prompt to create an
[0:03:17] agent called arcade feature builder. It
[0:03:19] should be a specialist for my arcade
[0:03:22] calculator. It knows the code base, uses
[0:03:26] HTML, etc. And I won't read the whole
[0:03:28] thing, but let's take a look at why it
[0:03:31] makes a great custom agent. It has clear
[0:03:34] domain focus, architectural awareness,
[0:03:37] visually compelling for a demo, minimal
[0:03:40] tools, and shows the why for custom
[0:03:42] agent. So, that's interesting, but let
[0:03:44] me ask it a follow-up question. That
[0:03:46] sounds great, but can I create another
[0:03:50] app using this custom agent that will
[0:03:54] apply the themes? All right, so it looks
[0:03:56] like it modified it so that it can be
[0:03:59] used for another app. And then we could
[0:04:01] test it out with one of these other apps
[0:04:03] here. So, I'll copy this and let's make
[0:04:06] it happen. Create that custom agent
[0:04:08] called arcade app builder. All right, so
[0:04:11] it looks like it's done. Now, the last
[0:04:13] time I used the custom agent, I had
[0:04:17] referenced it by using like the at
[0:04:19] symbol, but the simplest way to actually
[0:04:21] do it is to actually hit the drop-down
[0:04:23] and then select the agent after it's
[0:04:25] been built. So, right now, let's go
[0:04:27] ahead and choose arcade app builder. And
[0:04:30] I like one of the suggestions that I had
[0:04:32] here. Let's just say uh tip calculator
[0:04:35] just to keep in the theme of
[0:04:37] calculators. While it's working, let's
[0:04:39] go ahead and take a look at our agent
[0:04:42] customizations, and we see our arcade
[0:04:45] app builder here. If we take a look
[0:04:47] inside, we could see the description in
[0:04:50] addition to the tools that it's
[0:04:52] referencing and a lot more information
[0:04:54] regarding the system design such as
[0:04:56] typography, color palette for both dark
[0:04:59] mode and light mode, visual effects,
[0:05:02] lots of information here. And it's
[0:05:04] really nice that it's all in one
[0:05:06] location. Let's go ahead and circle back
[0:05:08] and see where we're at. All right, the
[0:05:09] tips calculator is ready at tip
[0:05:12] calculator, and it has all these
[0:05:14] features listed here. So, let's go ahead
[0:05:16] and ask it to run the tip calculator. I
[0:05:20] opened it in my other browser, but I
[0:05:23] just copied the URL
[0:05:26] and just going to go ahead and paste it
[0:05:27] into integrated browser here in VS Code.
[0:05:31] And there you go. Look at that. So, now
[0:05:33] I have a new app that leverage all the
[0:05:37] characteristics of my previous app
[0:05:39] because of the custom agent, which is
[0:05:41] great. It even makes a sound. So, for
[0:05:43] $55, I'd give it a tip
[0:05:46] of 15%, maybe 25% if I'm feeling
[0:05:50] generous, and there you go. To learn
[0:05:52] more about other customization features
[0:05:54] produced by our community, check out
[0:05:56] awesome Copilot at this URL here.
[0:06:01] So, I hope this gave you a solid feel
[0:06:03] for what custom agents can do. Let me
[0:06:06] know in the comments what kind of custom
[0:06:08] agents have you created. If you're
[0:06:10] interested in making things happen
[0:06:13] automatically without asking, hooks are
[0:06:16] something to look into. Thanks for
[0:06:17] joining, and I will see you in the next
[0:06:19] one.
