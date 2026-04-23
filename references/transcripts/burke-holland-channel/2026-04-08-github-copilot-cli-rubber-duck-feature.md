---
video_id: VgwrtU_dTUU
title: "GitHub Copilot CLI's Rubber Duck Feature is Kind of Genius"
url: https://www.youtube.com/watch?v=VgwrtU_dTUU
channel: "@BurkeHolland"
published: 2026-04-08
speakers:
  - Burke Holland
topics:
  - copilot-cli
  - multi-model
  - rubber-duck
  - code-review
relevance: primary
---

# GitHub Copilot CLI's Rubber Duck Feature is Kind of Genius

Burke Holland explains GitHub Copilot CLI's Rubber Duck feature and how a second model reviews generated work before it ships.

## Key Topics Covered

- **Copilot CLI**
- **Multi-model review**
- **Rubber Duck**
- **Code quality**

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] RubberDuck is a brand new coding agent for the GitHub Co-Pilot CLI from GitHub research.
[0:00:05] Let's check it out.
[0:00:06] The whole idea behind RubberDuck is that you have a model from a different family critique
[0:00:09] the work of the model that you're using.
[0:00:12] If you're using a Claude family model that you get a critique from GPT-54, now to use
[0:00:17] this, make sure that experimental mode is toggled on.
[0:00:20] When you do this, the CLI will restart and then rubberDuck is just enabled.
[0:00:24] How do you use it?
[0:00:26] It kind of just works.
[0:00:28] Here's how.
[0:00:29] In this case, I'm using Sonnet 4.6 medium and I have a plan to add analytics to an application
[0:00:34] I'm working on and it touches a bunch of files.
[0:00:37] It's kind of a complex feature.
[0:00:39] So when I say build it, it does the thing that an agent does where it's reading files
[0:00:43] and it's thinking about things, blah, blah, blah, but then interestingly down here,
[0:00:48] you can see the first thing it does before it actually does anything is it gets a rubber.
[0:00:52] Critique of the implementation.
[0:00:54] This rubberDuck is an agent type that's now built into the CLI.
[0:00:58] I noticed that mine used contact seven and to get a MCP server to look up next JS documentation.
[0:01:04] I happen to have that MCP server installed and it just used it.
[0:01:08] The other thing I noticed is that here, which is quite interesting, the rubberDuck agent
[0:01:12] is not blocking.
[0:01:13] So you can see that it's taking a while.
[0:01:15] So it starts implementing and just waits for the review to come back when it does and when
[0:01:18] it comes back, it finds a few things that Sonnet then adopts and this one right here just
[0:01:22] kills me because this is just classic AI slop.
[0:01:26] So this proxy not middleware.
[0:01:27] So what happened here in next JS 1622 middleware was renamed to proxy.
[0:01:32] It's very simple, but that would have caused an error just straight away code would not
[0:01:37] have worked at all.
[0:01:38] The rubberDuck caught that and then gave it back to Sonnet and Sonnet adopted that change.
[0:01:45] Now the other way that you can use this is you can ask for it.
[0:01:48] So in this case, I have a plan and then I just ask, can I please get a rubberDuck review
[0:01:51] on this plan and that's all you have to do.
[0:01:54] The research team of a GitHub ran this on Sweet Bench Pro and noticed that they got, look
[0:01:58] at this, Clodson at 4.6 paired with rubberDuck running GBT 5.4 achieved a resolution rate approaching
[0:02:05] Opus 4.6 running alone, closing 74.7% of the performance gap between Sonnet and Opus,
[0:02:13] which is really interesting.
[0:02:15] Now you'll get this rubberDuck automatically in three places.
[0:02:17] One is after drafting a plan, after a complex implementation, and most interestingly, after
[0:02:23] writing unit tests before running them, because Ai are notorious for writing unit tests
[0:02:28] to just make it pass instead of writing the unit tests correctly.
[0:02:32] And so the rubberDuck is here to make sure that doesn't happen.
[0:02:35] Even more interesting is this paragraph right here, which is that the agent will automatically
[0:02:39] use the rubberDuck if it gets stuck or it's in a loop to try to get itself unstuck.
[0:02:44] And that is the new rubberDuck functionality from research for the Co-Pilot CLI available
[0:02:49] today with the experimental mode on.
[0:02:53] And as always, happy coding.
