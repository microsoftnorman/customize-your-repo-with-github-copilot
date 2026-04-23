---
video_id: 0Eq8m63Z5J0
title: "VS Code Terminal Agent Tool Updates"
url: https://www.youtube.com/watch?v=0Eq8m63Z5J0
channel: "@code (Visual Studio Code)"
published: 2026-04-16
speakers:
  - James Montemagno
topics:
  - terminal-agent
  - agent-sessions
  - interactive-input
  - tool-updates
relevance: primary
---

# VS Code Terminal Agent Tool Updates

In this video, we walk through the latest improvements to terminal tools for agent sessions: foreground terminal support, better handling of interactive input, progress messages, and smarter background notifications. These updates make working with REPLs, installers, and long‑running commands faster and more seamless.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Intro to Terminal Tools for Agent Sessions |
| 00:25 | Demo |
| 03:33 | Recap |

## Key Topics Covered

- **Terminal Agent**
- **Agent Sessions**
- **Interactive Input**
- **Tool Updates**

## Links

- https://aka.ms/VSCode/116
- https://x.com/code
- https://bsky.app/profile/vscode.dev
- https://aka.ms/VSCode/LinkedIn
- https://github.com/microsoft/vscode

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Today, we're in my garage, and we're
[0:00:02] going to dive into some brand new
[0:00:03] terminal upgrades inside of VS Code that
[0:00:06] make agent workflows feel smoother,
[0:00:08] faster, and way more natural. Now, these
[0:00:11] updates give agents clear awareness of
[0:00:13] what's happening in your terminal,
[0:00:15] whether it's in the foreground or the
[0:00:16] background. Better control of the
[0:00:18] session you're actively using, and
[0:00:20] seamless ways for you to jump in
[0:00:22] whenever you want to. So, let's go ahead
[0:00:24] and take a look. Okay, let's first
[0:00:25] understand how the agent works directly
[0:00:27] with the terminal, specifically when it
[0:00:29] needs input. I'm going to have it go
[0:00:32] ahead and run a PowerShell script to ask
[0:00:34] me what my name is.
[0:00:35] And then, what I'm going to do is go
[0:00:37] ahead and print that back. So, the very
[0:00:39] first thing here is it's going to
[0:00:40] request that it runs the PowerShell
[0:00:43] snippet directly in the terminal. I'm
[0:00:44] going to say allow.
[0:00:46] Now, at this point, a few things are
[0:00:47] going to happen. We can first see that
[0:00:49] in the bottom left here in the terminal
[0:00:51] pane, that there is a hidden terminal
[0:00:53] visible here. Now, it's hidden. Now, I
[0:00:56] could go ahead and expose that, and
[0:00:57] we'll run the same exact experiments
[0:00:58] again to see what happens when I do
[0:01:00] that. But, since it's hidden, it's in
[0:01:02] the background, we can see that it has
[0:01:04] identified that the terminal is paused
[0:01:06] on the read host prompt, and it's going
[0:01:08] to go now go ahead and collect the
[0:01:10] information back. So, I'm going to say
[0:01:11] what is the name? I'm going to say James
[0:01:12] Monte Magno.
[0:01:14] And now, it's going to send that back to
[0:01:16] the terminal automatically, and then
[0:01:18] it's going to read the expected outputs
[0:01:20] back from the terminal for me. So, here
[0:01:21] we go. It's completed it, and it says,
[0:01:23] "Hello, James Monte Magno."
[0:01:25] Now, if we go ahead and tap on that
[0:01:26] hidden terminal, we can see the exact
[0:01:29] PowerShell scripts that were executed.
[0:01:32] Okay, let's go ahead and run this
[0:01:33] experiment one more time. I'm going to
[0:01:35] start over at the top. I'm going to run
[0:01:36] the same exact PowerShell scripts here.
[0:01:39] Now, in this case, you may want to drop
[0:01:42] down into the terminal to go ahead and
[0:01:44] enter those. So, here, it's going to go
[0:01:46] ahead and prompt me one more time,
[0:01:47] specifically to run that PowerShell
[0:01:49] script. It's going to steer and
[0:01:51] understand that it needs the input. And
[0:01:53] then, it's going to go ahead and prompt
[0:01:54] me for my name again.
[0:01:56] Now, in this case, even though it's
[0:01:58] prompted me, I can take over if I want
[0:02:01] to. I can go ahead and one click into
[0:02:03] that hidden terminal. And now, we can
[0:02:06] see that the agent has identified that
[0:02:09] I'm in control, that I'm going to go
[0:02:11] ahead and enter my name. So, now I'm
[0:02:12] just going to say James Monte Magno, and
[0:02:15] hit go.
[0:02:16] And what's really neat about this is
[0:02:18] that the agent has now been notified
[0:02:21] automatically that that background
[0:02:23] terminal has been updated by me, and is
[0:02:26] now printing it back out here. This
[0:02:28] extends into many other scenarios. So,
[0:02:30] for example, let me go ahead and say run
[0:02:33] npm init.
[0:02:36] And now, when I do this, it needs to
[0:02:38] understand a lot of different
[0:02:39] information when npm init is run for
[0:02:42] this project. It can not only just
[0:02:44] identify a single command to run,
[0:02:48] and the single entry,
[0:02:50] but it can go ahead and identify a bunch
[0:02:52] of different items to prompt back to me.
[0:02:55] Here we go. It has identified nine
[0:02:57] different questions, the package name,
[0:02:59] version, description, entry point, and a
[0:03:01] lot more. So, I'm going to say, "What's
[0:03:03] the name?" Yeah, Tiny Tool Town.
[0:03:05] Version, I can just hit enter here for
[0:03:07] the default, or I can enter the tiniest
[0:03:10] tool town ever.
[0:03:13] And when I'm done here, it will go ahead
[0:03:16] and send all of this information
[0:03:17] directly back into the terminal with all
[0:03:20] those questions answered.
[0:03:23] I can go ahead and expose that terminal
[0:03:25] now that it's gone ahead and entered
[0:03:26] those, and I can see it happen in real
[0:03:28] time, entering that information back
[0:03:31] into the tools, which is really, really
[0:03:32] neat.
[0:03:34] Okay, let's recap what we just saw.
[0:03:36] Instant, smarter prompt detection, so
[0:03:38] agents can respond right when the
[0:03:40] terminal needs input.
[0:03:42] Full support for the foreground
[0:03:44] terminal, letting agents interact
[0:03:45] directly with the one you're actually
[0:03:47] working in. And a new focus terminal
[0:03:50] option that makes it effortless to take
[0:03:52] over for sensitive or hands-on commands.
[0:03:56] These are just some of the brand new
[0:03:57] terminal features available in the
[0:03:58] latest version of VS Code. So, update
[0:04:01] today, give it a try, and as always,
[0:04:04] happy coding.
