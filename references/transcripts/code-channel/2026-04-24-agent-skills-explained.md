---
video_id: mPjTZviv23s
title: "Agent Skills Explained in 5 Minutes | Ep 3 of 8"
url: https://www.youtube.com/watch?v=mPjTZviv23s
channel: "@code (Visual Studio Code)"
published: 2026-04-24
speakers:
  - Reynald Adolphe
topics:
  - agent-skills
  - skills
  - reusable-workflows
  - documentation
relevance: primary
---

# Agent Skills Explained in 5 Minutes

Reynald Adolphe demonstrates creating and modifying an Agent Skill for reusable workflows in VS Code.

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] It seems like most people are using
[0:00:01] agent skills wrong or just not at all.
[0:00:05] Well, in this video, we're going to
[0:00:06] break down what agent skills are and how
[0:00:09] to properly use them in your workflow.
[0:00:12] So, let's go ahead and jump right in.
[0:00:14] Agent skills are folders of
[0:00:16] instructions, scripts, and resources
[0:00:19] that GitHub Copilot can load when
[0:00:22] relevant to perform specialized tasks.
[0:00:24] These skills are an open standard that
[0:00:26] work across multiple AI agents,
[0:00:29] including GitHub Copilot in VS Code,
[0:00:32] Copilot CLI, and Copilot Cloud Agent.
[0:00:36] The documentation here goes into detail
[0:00:38] with some examples of some skills, but
[0:00:40] let's go ahead and take a look at an
[0:00:42] existing project. Now, I have here a
[0:00:44] calculator app, but if we go into this
[0:00:48] gear here to open up customizations, we
[0:00:51] can see right off the bat some skills
[0:00:53] that are available under extensions and
[0:00:56] then some built-in skills. And some of
[0:00:58] these may look familiar to you if you've
[0:01:00] reviewed some of our other videos, but
[0:01:03] if we, for example, chose create prompt,
[0:01:06] we can see what's going on here behind
[0:01:08] the scenes in terms of what's inside the
[0:01:10] skill.md file. We can see the
[0:01:12] description, which is to create a
[0:01:14] reusable prompt for common task, but
[0:01:17] also on line seven, you can see that the
[0:01:18] related skill is agent customization and
[0:01:21] indicates to load and follow prompt.md
[0:01:24] for template and principles. And then,
[0:01:26] of course, specific details that the
[0:01:28] skill must abide to, such as extracting
[0:01:31] from conversation, clarifying if it's
[0:01:33] needed, and iterations. So, if we went
[0:01:36] into chat and entered {slash}
[0:01:39] create, this is what allows us to create
[0:01:42] a reusable prompt, such as to perform
[0:01:46] code review. And you can see right here,
[0:01:48] it says to read the skill for agent
[0:01:50] customization. And also, it's prompting
[0:01:53] us, where should this code review prompt
[0:01:55] be saved? And for now, I'll say
[0:01:58] workspace and just accept the default
[0:02:00] for the rest of these prompts here. So,
[0:02:02] now it's created the prompt. What I
[0:02:04] would like to do is to create a skill
[0:02:09] that will update a readme file whenever
[0:02:12] a feature is added to my project. So,
[0:02:16] this skill will theoretically update my
[0:02:19] readme file with the details of whatever
[0:02:22] feature that I added. And look at this,
[0:02:25] this is great. It's asking me if I want
[0:02:27] to be from our workspace and personal. I
[0:02:30] actually forgot to mention personal, so
[0:02:33] I've selected that. And this is great.
[0:02:36] It's asking me for should be just a
[0:02:37] feature list or more details. I'm fine
[0:02:40] with the first, and I want it to do it
[0:02:42] automatically, so I'll leave number one.
[0:02:44] We'll give it the permission that it
[0:02:46] needs. While it's creating the skill, I
[0:02:47] could try to think of a feature that I
[0:02:49] might want to add to test this out. So,
[0:02:51] I think I know an idea for a feature,
[0:02:54] but in the meanwhile, let's go ahead and
[0:02:56] take a look at our skill that was just
[0:02:58] created.
[0:02:59] Update readme. All right. That looks
[0:03:03] good.
[0:03:04] I think I might want to add a
[0:03:05] confirmation here to tell me in the chat
[0:03:08] that it updated it so that I don't have
[0:03:10] to just check the readme each time. Can
[0:03:13] you update that skill so that it
[0:03:17] mentions in the chat that the readme has
[0:03:19] been updated?
[0:03:24] There's a notification right there. So,
[0:03:26] this is the readme that we have here.
[0:03:28] So, let's go ahead and add a feature to
[0:03:31] this
[0:03:32] arcade calculator and see what happens.
[0:03:35] Can you add a feature to the calculator
[0:03:37] so that when I switch from
[0:03:40] dark mode to light mode, that it plays a
[0:03:43] short
[0:03:44] jingle that reflects dark mode or light
[0:03:48] mode? Now, I have no idea what type of
[0:03:50] jingle it's going to decide what's
[0:03:52] representative of dark mode and light
[0:03:53] mode, but it was the first thing that
[0:03:55] came to the top of my head.
[0:03:57] So, I'm excited to see what it comes up
[0:03:59] with. And most importantly, that the
[0:04:01] readme gets updated with this
[0:04:02] information. Add jingle methods to auto
[0:04:05] manager. Okay. Light mode jingle,
[0:04:09] ascending C5, E5, G5. All right. Well,
[0:04:12] it says it added the feature
[0:04:14] and updated the readme. Let's check out
[0:04:16] the readme.
[0:04:17] But, I didn't hear the sound, but line
[0:04:20] 11 is where it updated it. I can see
[0:04:22] that right there. So, let's go ahead and
[0:04:24] just make sure that it fixes it so we
[0:04:26] actually hear the sound and then call it
[0:04:28] a day. I don't hear a jingle when I
[0:04:31] Before I even do that, let me try
[0:04:33] refreshing
[0:04:36] the UI. Now I hear it. Okay.
[0:04:40] I just needed to refresh and it works.
[0:04:43] All right, cool. To learn more about
[0:04:45] other customization features produced by
[0:04:47] our community, check out awesome Copilot
[0:04:50] at this URL here.
[0:04:53] So, we covered what agent skills are and
[0:04:55] how to use them effectively in your
[0:04:58] workflow. Let me know in the comments,
[0:05:00] what skills have you used? If you're
[0:05:03] wondering how this involves into
[0:05:04] something more structured, custom agents
[0:05:07] are worth checking out.
