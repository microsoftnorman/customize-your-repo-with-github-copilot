---
video_id: IxZCSOfMob8
title: "The Plan Agent Improvements in VS Code are INCREDIBLE"
url: https://www.youtube.com/watch?v=IxZCSOfMob8
channel: "@JamesMontemagno"
published: 2026-02-05
speakers:
  - James Montemagno
topics:
  - plan-mode
  - interactive-questions
  - sub-agents
  - model-selection
relevance: primary
---

# The Plan Agent Improvements in VS Code are INCREDIBLE

James Montemagno highlights recent VS Code plan agent improvements, including interactive questions, default plan and implement models, and parallel subagents.

## Key Topics Covered

- **Plan agent**
- **Interactive questions**
- **Model selection**
- **Parallel subagents**

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Plan Mode inside of Visual Studio Code is one of my favorite features when I'm developing with AI.
[0:00:05] Not only because I often have an idea, but it's not really fully fleshed out.
[0:00:09] The great part about Plan Mode is it gives you a detail analysis and has questions along the way.
[0:00:14] In the latest release of VS Code, there is game-changing features not only to help you answer those questions
[0:00:20] to really drill down in those details, but also handling the handoff and implementation as well.
[0:00:26] So I want to show you today some of my favorite brand new features to Plan Mode inside of VS Code.
[0:00:30] So let's check it out.
[0:00:31] Okay, here I am inside the latest VS Code.
[0:00:34] And I'm a Visual Studio Wallpapers website here, which allows me to browse, desktop phone, and even watch Wallpapers for VS and VS Code.
[0:00:41] Well, I love this website that I built out.
[0:00:42] I really love a new favorites feature or even like a search feature, for example, that would be really, really nice.
[0:00:48] So let's go ahead and go into Plan Mode.
[0:00:50] So I'm going to pop over here.
[0:00:52] And the first thing I want to do is call out that I can just start a new sort of local session here with Copilot, a background session,
[0:00:59] power by the GitHub Copilot CLI, Cloud Session, then I could delegate out that word to the Cloud Agent.
[0:01:05] Or I could actually start a new session here with the Cloud Agent SDK or even the Codex extension, for example.
[0:01:10] But I'm just going to do it here locally.
[0:01:12] And we're going to change our mode over here into Plan.
[0:01:15] And I first want to call out here that it switched automatically to GPT52, because I like to use different models for different agents pretty much.
[0:01:23] So let's go ahead and get this to work.
[0:01:25] So I'm going to say, I would like to add a new favorites feature for people to favorite a wallpaper and have a dedicated page can do it all locally.
[0:01:40] No user accounts, right?
[0:01:43] I'm going to go ahead and send that off.
[0:01:45] So now this is going to get to work.
[0:01:46] And I can actually see that we have a few sessions already here when I was sort of looking at user accounts.
[0:01:51] This one here it says adding a new favorites feature and it's in progress.
[0:01:55] And I can see up top here that it's actually a session in progress.
[0:01:58] So here's going to get to work.
[0:02:00] And sub agents are going to start to sort of parse this.
[0:02:02] And a bunch of sub agents are going to spin up on their own little context of reading files and understanding things.
[0:02:08] And then that will report back to the main agent.
[0:02:11] But I also love is that I can just do, you know, new session.
[0:02:13] And I could say, let's plan out a search feature for the website.
[0:02:19] So I could just spin up yet another plan going on and see it over here.
[0:02:23] So that's going to get to work.
[0:02:24] All right.
[0:02:25] So the sub agents are reading, they're gripping, they're looking for different things and understanding the code base.
[0:02:31] And I always sort of go into plan mode first, mostly because I kind of have an idea in my head, but it's not fully flashed out.
[0:02:39] And I may not know every single parts of the code base that I even want or need to touch.
[0:02:44] So all these sub agents are going to pull together what the implementation may look like.
[0:02:50] And it's also going to ask me questions along the way.
[0:02:53] So now that it understands here, it's going to ask a few questions.
[0:02:57] So it says, hey, I got a few questions for you.
[0:02:59] So we can update the plan.
[0:03:01] So all right, cool.
[0:03:02] What do we want to know here?
[0:03:03] So it's considering some questions.
[0:03:05] And this is really cool.
[0:03:07] So I'm writing the flow.
[0:03:08] It's going to say what collections should support favoriteing.
[0:03:12] So here I'm just going to say, yeah, let's just do, yeah, all of them.
[0:03:15] That's cool.
[0:03:16] Go to the next question.
[0:03:18] Where should the favorite toggle live in the preview on each grid tile?
[0:03:21] Let's do preview.
[0:03:23] I think that makes the most sense.
[0:03:25] And then on a favorites page, what should clicking a favorite item do?
[0:03:30] Should it open the wallpaper's preview model, navigate to the corresponding gallery page.
[0:03:36] So let's just do the other model.
[0:03:37] That sounds fine.
[0:03:38] And submit it back.
[0:03:39] That brand new interactive questions to really help the planning is super nice.
[0:03:46] I no longer need a read a bunch of things.
[0:03:48] I can do multi-select.
[0:03:49] I don't need to type in one, two, three, four, for example, into here.
[0:03:52] And this is now going to flesh out the rest of the feature.
[0:03:55] So that alone is a huge dramatic win when I'm planning out features.
[0:04:01] And here it is.
[0:04:02] We have our full planned out feature here.
[0:04:04] OK, cool.
[0:04:05] So now that this is here, I can do a few things.
[0:04:08] I can open an editor, which is going to give me a prompt file that I could save locally
[0:04:11] and execute later.
[0:04:12] I could go in and actually continue in the background or continue in the cloud.
[0:04:16] But I'm just going to go ahead and start implementation.
[0:04:18] And I want to point out one thing that happened really quick there, which is that the
[0:04:22] local agent moved over into Asia mode and switched over to GPT-5 to Codex as a new feature
[0:04:30] in this release.
[0:04:31] So let me show you how I did all this while that gets to work.
[0:04:34] I'm going to go into settings.
[0:04:35] And the first thing that we're going to do is search for default model.
[0:04:41] And here in default model, there's several that you can now pick and choose from.
[0:04:45] So there's a default inline chat.
[0:04:47] So this is the default model that I've chosen, which is Gemini 3 Flash.
[0:04:51] So I'm kind of usually sectioning off a tiny bit of code.
[0:04:54] And then down here, we also have an implement agent and a plan agent and even
[0:05:00] sub agents as well that you can go ahead and choose those names.
[0:05:03] So here I chose GPT-5 to Copilot and GPT-5 to Codex Copilot to go ahead and do.
[0:05:10] So if you have a favorite model that you want, or you can just leave a blank and
[0:05:13] use the same model everywhere, which is great.
[0:05:16] And then additionally, if I go into questions here, and here you can see all you have to do
[0:05:22] is make sure that the ask questions is enabled right there.
[0:05:26] Honestly, these two features alone really pull together how I plan and
[0:05:32] integrate in my workflow.
[0:05:33] And now we can see Codex is getting to work here, the 5-2 Codex.
[0:05:37] And we can see all of the to-do's list that it was put together and the files changed.
[0:05:41] So honestly, these are game-changing features when planning out and
[0:05:45] implement features with VS Code.
[0:05:47] All right, there you go.
[0:05:47] There's some of my favorite features brand new inside of VS Code.
[0:05:50] Download it, enable it, check them all out today.
[0:05:53] I showed you all the different settings you need to enable if they're not
[0:05:55] enabled for you already.
[0:05:56] So go turn them on, go deeper on your planning with VS Code.
