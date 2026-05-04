---
video_id: oyMMotLlcgQ
title: "Instructions vs Skills vs Hooks & More Explained By Copilot Itself | Ep 7 of 8"
url: https://www.youtube.com/watch?v=oyMMotLlcgQ
channel: "@code (Visual Studio Code)"
published: 2026-04-24
speakers:
  - Reynald Adolphe
topics:
  - customization
  - instructions
  - prompt-files
  - skills
  - custom-agents
  - hooks
  - comparisons
relevance: primary
---

# Instructions vs Skills vs Hooks & More Explained By Copilot Itself

Reynald Adolphe demonstrates using GitHub Copilot to compare customization primitives and build reusable learning references.

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] There are quite a few important
[0:00:01] customization options in VS Code and
[0:00:05] it's easy to get them confused. So, in
[0:00:08] this video, we'll actually break down
[0:00:11] each of them and then compare them so
[0:00:13] that we could see how they all would fit
[0:00:16] together and how they're meant to be fit
[0:00:18] together.
[0:00:19] So, let's go ahead take a look. So, on
[0:00:21] the VS Code documentation site, we have
[0:00:23] quite a bit of information that covers
[0:00:25] custom instructions, prompt files,
[0:00:28] custom agents, agent skills, and hooks,
[0:00:31] which is all great. But, sometimes it's
[0:00:34] nice to have different resources for
[0:00:36] learning topics. And what I want to show
[0:00:38] you is in addition to reviewing content
[0:00:42] that's in the docs is actually using
[0:00:44] Copilot in a few different ways to learn
[0:00:47] the differences between them because
[0:00:50] there are some overlaps, but it's nice
[0:00:52] to get a good deep idea of what the core
[0:00:55] differences are between them and then
[0:00:57] also see some examples. So, let's hop on
[0:00:59] over to VS Code and take a look. But,
[0:01:01] before we do, let's go ahead and just
[0:01:04] screen capture the topics. I'm going to
[0:01:06] drop it in and let me go ahead and take
[0:01:08] a look to show you what Copilot is going
[0:01:11] to see. And we could ask it to give us a
[0:01:13] summary of what each of these are. Can
[0:01:16] you go ahead and explain to me what each
[0:01:19] of these features are in a short
[0:01:22] paragraph?
[0:01:25] And what's nice here is it gives us a
[0:01:27] concise explanation for each of these
[0:01:30] features of custom instructions, which
[0:01:32] is telling us that it's reusable rule
[0:01:34] files that guide Copilot's behaviors,
[0:01:37] also for prompt files, and let's see the
[0:01:39] fine reusable parameterized requests,
[0:01:42] and nice summaries for the last three
[0:01:44] also. Now, something else we could ask
[0:01:46] it is to please create a chart with each
[0:01:50] of these and then in the chart have a
[0:01:53] column that explains the differences or
[0:01:58] anything you think is relevant. So, I
[0:02:00] could use it as a reference chart so I
[0:02:03] know when to use each. And now in
[0:02:06] addition, we have this chart here that
[0:02:08] has the feature name, what it is, when
[0:02:11] to use it, associated file extension,
[0:02:15] the scope, and even an example. And
[0:02:17] right below, we have some key
[0:02:19] differences at a glance. Instructions
[0:02:21] versus prompt files, which tells you
[0:02:23] that instructions are passive whereas
[0:02:26] prompt files are active and follows the
[0:02:28] same pattern for differentiating the
[0:02:31] others such as instructions versus
[0:02:33] custom agents, custom agents versus
[0:02:36] agent skills, and hooks versus
[0:02:38] everything else. So, as you can see
[0:02:39] here, it's smart enough to pick what are
[0:02:42] the pairs that people tend to confuse
[0:02:45] and there are definitely people that
[0:02:47] often confuse prompt files and
[0:02:49] instructions and instructions versus
[0:02:52] custom agents, custom agents versus
[0:02:55] agent skills. Now, one more thing I'd
[0:02:57] like to ask it, which is a different way
[0:02:58] of learning, is to just quiz yourself.
[0:03:01] So, let's go ahead and ask it. Can you
[0:03:04] go ahead and give me 10 different
[0:03:07] questions that give me a scenario and I
[0:03:11] need to choose through multiple choice
[0:03:13] which is the proper feature that I
[0:03:17] should use. And the features would be
[0:03:19] choosing either custom instructions
[0:03:22] versus prompt files versus skills, etc.
[0:03:26] And actually, let's change this to four
[0:03:28] questions because we could get the idea
[0:03:30] of the functionality with just that. And
[0:03:33] there you go, a third way to get
[0:03:35] familiar with the content through
[0:03:37] quizzes. So, if we look at the first
[0:03:38] one, it tells us that our situation is
[0:03:40] we notice that every time Copilot
[0:03:43] generates React components, it uses
[0:03:45] class components instead of functional
[0:03:47] components with hooks, but we want
[0:03:49] Copilot to always default to functional
[0:03:52] components. And when we look at our
[0:03:55] options, it sounds like it should be
[0:03:56] instructions. And if we scroll down
[0:04:00] for under details,
[0:04:01] that is exactly what the answer is and
[0:04:04] has an explanation of why. This is great
[0:04:06] and I just wanted to show you these
[0:04:08] different three ways that you could use
[0:04:09] Copilot to really understand differences
[0:04:12] when topics get confusing. So, now let's
[0:04:15] go ahead and try to have it consolidate
[0:04:18] all this information into an HTML file
[0:04:21] so that we could reference later. Can
[0:04:23] you go ahead and consolidate all this
[0:04:26] information that you produced for me
[0:04:28] such as the explanations of the
[0:04:31] features, the chart that you created,
[0:04:34] and the quiz all in an HTML file so I
[0:04:37] could reference later? Let's just clean
[0:04:39] up
[0:04:40] this just make sure it's understanding
[0:04:42] me properly. Usually figures it out.
[0:04:49] All right.
[0:04:50] Created this file, Copilot feature
[0:04:52] reference. Let's go ahead and take a
[0:04:55] look. Let's see how it looks. And it
[0:04:57] looks nice. The summary of each,
[0:04:59] beautiful chart, the differences between
[0:05:01] the features, what it is, when to use
[0:05:04] it, etc. Followed by the key differences
[0:05:07] and then an interactive quiz. So, now I
[0:05:10] think you should better understand how
[0:05:12] all of these customization features
[0:05:15] work together. Let me know in the
[0:05:17] comments how you would explain the
[0:05:21] differences between prompt files,
[0:05:25] custom instructions, skills, custom
[0:05:27] agents, and hooks
[0:05:29] in your own words to a colleague. To
[0:05:32] really drive the point home, there's no
[0:05:34] better way than to actually build an app
[0:05:37] together and put them to practice like
[0:05:40] in this video here. Thanks for joining
[0:05:43] and I will see you in the next one.
