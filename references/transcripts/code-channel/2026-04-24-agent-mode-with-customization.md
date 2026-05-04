---
video_id: Bb45ZoKfJf0
title: "Agent Mode with Customization | Ep 8 of 8"
url: https://www.youtube.com/watch?v=Bb45ZoKfJf0
channel: "@code (Visual Studio Code)"
published: 2026-04-24
speakers:
  - Reynald Adolphe
topics:
  - agent-mode
  - customization
  - prompt-files
  - custom-instructions
  - skills
  - custom-agents
  - hooks
relevance: primary
---

# Agent Mode with Customization

Reynald Adolphe demonstrates building an app with prompt files, custom instructions, Agent Skills, Custom Agents, and hooks working together.

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] So, you may have seen quite a few videos
[0:00:02] about customization features such as
[0:00:06] prompt files, custom instructions,
[0:00:09] skills, custom agents, hooks.
[0:00:12] But, what better way to really
[0:00:13] understand how they all work together by
[0:00:16] building an app and actually
[0:00:17] implementing them. So, in this video,
[0:00:20] that's what we're going to do. Let's go
[0:00:22] ahead and make this happen. So, let's
[0:00:24] build an app and it's going to be
[0:00:25] called, as the name implies here, a repo
[0:00:28] analyzer, which is going to take in the
[0:00:31] URL from a GitHub repo and then assess
[0:00:34] the code to grade the quality of it from
[0:00:37] a scale of 1 to 10. And during the
[0:00:39] process of us building it and using it,
[0:00:43] we're going to leverage some of the
[0:00:44] customizations that we created.
[0:00:46] Specifically for agents, we're going to
[0:00:49] use the arcade app builder, which is
[0:00:52] going to have this app follow a 80s
[0:00:56] retro theme. In terms of skills, we're
[0:00:59] going to leverage an update read me so
[0:01:01] that whenever we add a feature to the
[0:01:04] app, it updates the read me. When the
[0:01:07] app is being built, we have custom
[0:01:08] instructions that are going to make sure
[0:01:11] that solid principles are applied. We
[0:01:14] also have a prompt file that's going to
[0:01:16] allow us to simplify code for open files
[0:01:19] to essentially eliminate bloated and
[0:01:21] verbose code.
[0:01:23] And last but not least, we have a hook
[0:01:26] that we'll test out whenever we want to
[0:01:29] make a modification to a file and this
[0:01:32] hook will automatically format it. The
[0:01:34] value that all of this brings is that
[0:01:38] these are all situations that are going
[0:01:40] to be saving us time because we didn't
[0:01:43] have to specify to follow solid
[0:01:46] principles because we have custom
[0:01:48] instructions. We don't need to create a
[0:01:51] new agent to tell it to follow an 80s
[0:01:53] theme because we have an agent that's
[0:01:56] going to handle that. We don't need to
[0:01:58] remember to tell it to update our read
[0:02:00] me because we have a skill that's going
[0:02:02] to handle that. So, because of all this,
[0:02:04] during the course of our workflow, it
[0:02:06] inherently saves us time. So, let's go
[0:02:09] ahead now and we're going to switch this
[0:02:11] agent to arcade app builder and give it
[0:02:15] a request. Can you go ahead and create
[0:02:18] an app that will take in the URL from
[0:02:21] GitHub repo, it will analyze the code,
[0:02:24] and I won't bother reading the rest, but
[0:02:26] it's essentially what I told you
[0:02:27] regarding the grading system and it
[0:02:29] gives giving us recommendations also to
[0:02:32] make it have a higher grade next time
[0:02:34] around. So, let's give it a go. I will
[0:02:37] build a GitHub repo analyzer app with
[0:02:40] the arcade aesthetic.
[0:02:47] All right, looks like it's done. Let's
[0:02:49] go ahead and run the app and see how
[0:02:51] it's working.
[0:02:55] I'll go ahead and open up our integrated
[0:02:57] browser. And all right, this is a start.
[0:02:59] It's definitely using the arcade theme,
[0:03:02] but the app looks so simple.
[0:03:05] I wonder how powerful it actually is.
[0:03:07] All right, it's got a little validation
[0:03:09] here if I didn't enter anything.
[0:03:11] But, let me go ahead and pull up a real
[0:03:14] repo that's out there from GitHub and
[0:03:17] see how it scores it. This is a budget
[0:03:19] app that I created a few months ago. So,
[0:03:22] I'm going to use this URL here. All
[0:03:25] right, well, there you go. So, it rates
[0:03:26] at 4.3, could definitely use some
[0:03:29] improvement. And right below are
[0:03:31] recommendations to help increase the
[0:03:34] score. Add a license, add contributing
[0:03:36] file, to improve docs, etc. Pretty cool.
[0:03:39] All right, so
[0:03:41] let's create a read me. Create a read me
[0:03:44] for this project. And ideally it has
[0:03:46] some information about how this project
[0:03:48] works and it will test adding a feature
[0:03:50] to it and see if the read me gets
[0:03:52] updated. And actually right now you
[0:03:54] could see it's using the skill to update
[0:03:56] read me right off the bat. So, I almost
[0:03:59] don't even need to try to update it
[0:04:01] because I wanted to test the skill
[0:04:03] itself. And it looks like it it is using
[0:04:05] it. So, this is the read me that it
[0:04:07] generated with some information here.
[0:04:10] And let's see
[0:04:12] where it references dark mode. Let's say
[0:04:14] I want to remove the dark mode feature.
[0:04:21] That button I just pressed is the dark
[0:04:23] mode light mode feature. Let's go ahead
[0:04:24] and remove that. And this is just for
[0:04:26] the sake of testing to see if our read
[0:04:28] me gets updated to indicate that that
[0:04:31] has been removed or if there's just no
[0:04:33] mention of dark mode anymore.
[0:04:39] While it's doing this, we could look to
[0:04:41] see when it was building the app,
[0:04:43] it did make sure that it applied WCAG
[0:04:46] standards, but most importantly, it also
[0:04:51] followed solid principles. And right now
[0:04:54] it looks like it's done. Let me go ahead
[0:04:56] and refresh. It looks like that feature
[0:04:59] is no longer there. If I go into the
[0:05:01] read me, the dark mode light mode
[0:05:03] feature is no longer referenced. So, the
[0:05:06] read me was updated, which is excellent.
[0:05:08] So, let's take a look at our
[0:05:09] customization UI. We've tested a couple
[0:05:12] of things so far. We've verified that
[0:05:14] our skill for updating the read me
[0:05:17] works. We've verified that the solid
[0:05:20] principles got applied.
[0:05:22] Basically, it mentioned it in the chat.
[0:05:24] Our agent clearly worked for arcade app
[0:05:28] builder. So, from now there's two more
[0:05:30] things we could quickly test. Our prompt
[0:05:33] to simplify code to see if that works
[0:05:36] and then also our hook by modifying a
[0:05:39] read me and then seeing if it formats
[0:05:41] it.
[0:05:42] Now, it doesn't have to be just the read
[0:05:45] me, but it's the simplest thing I want
[0:05:47] to go ahead and test. So, let's go ahead
[0:05:49] and just change this formatting here a
[0:05:52] little bit, make this uneven, and let's
[0:05:55] make a change. Can you go ahead and
[0:05:57] modify the read me so that the name is
[0:06:00] not just repo analyzer, but it says
[0:06:04] fantastic repo analyzer? And boom, it
[0:06:08] renamed it to fantastic repo analyzer
[0:06:10] and you could see that that
[0:06:11] automatically formatted the lines 11 and
[0:06:16] 12. So, the last thing that I'll go
[0:06:17] ahead and test is whether or not our
[0:06:21] code is bloated and if it could be a
[0:06:24] little bit more efficient. And the code
[0:06:26] that we're concerned about is this
[0:06:28] JavaScript file. So, let's go ahead and
[0:06:31] use our prompt file to simplify code and
[0:06:35] this will simplify reduce bloated code
[0:06:38] in open files and should also tell us
[0:06:41] what changes it made. And again, what
[0:06:43] makes this an excellent prompt file is
[0:06:47] because the act of simplifying the code
[0:06:49] is something that you can find yourself
[0:06:52] repeatedly doing for multiple files
[0:06:56] while you're building a project. So,
[0:06:58] it's not something you want to keep
[0:06:59] prompting over and over. You could have
[0:07:02] that prompt file right at your
[0:07:03] fingertips. And look at this. Now I have
[0:07:06] the full picture. Let me identify
[0:07:08] simplification opportunities. And here
[0:07:10] you go. The jingle function is dead
[0:07:12] code. Seems I could remove some of that.
[0:07:15] Security anti-patterns is dead code. And
[0:07:18] it's still working, but we get to see
[0:07:20] like all the things that it's detecting
[0:07:22] right now. And now it looks like
[0:07:24] it is done. And here's what was
[0:07:26] simplified and removed these dead code.
[0:07:30] It used a single one-line helper.
[0:07:32] Simplified set status by replacing an if
[0:07:35] else and then some more simplification
[0:07:37] in addition to some hoisting. Very cool.
[0:07:40] So, there you go. Lots of customization
[0:07:42] features put into action during the
[0:07:45] building of an app built from scratch.
[0:07:48] And hopefully this helps simplify for
[0:07:50] you the whole picture of how all these
[0:07:52] customization features work together
[0:07:54] during your workflow. I hope that this
[0:07:57] video helped you see how all these
[0:08:00] customizations come together in a real
[0:08:02] workflow. But before you go, let me know
[0:08:05] in the comments what combination of
[0:08:08] features you would use to customize a
[0:08:12] project or what have you used in the
[0:08:15] past.
[0:08:16] Thanks for joining and I will see you in
[0:08:19] the next one.
