---
video_id: -yKALFS5ewY
title: "How to use agents, skills, and instructions in Copilot CLI | Tutorial for beginners"
url: https://www.youtube.com/watch?v=-yKALFS5ewY
channel: "@GitHub"
published: 2026-04-16
speakers:
  - GitHub (Copilot CLI for Beginners series)
topics:
  - copilot-cli
  - custom-agents
  - skills
  - instructions
  - customization
relevance: primary
---

# How to use agents, skills, and instructions in Copilot CLI

Episode 6 of the GitHub Copilot CLI for Beginners series. Walks through setting up instructions, skills, and custom agents so Copilot CLI follows your team's coding standards — generating project-level instructions, automating pull requests with agent skills, and running specialized tasks like accessibility reviews.

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:04] In this episode of Get Up Copilot CLI
[0:00:06] for beginners, we're going to explore
[0:00:08] instructions files, agents, and skills,
[0:00:11] which all allow you to ensure that
[0:00:13] Copilot is following the exact same
[0:00:15] patterns and practices that your
[0:00:17] organization has laid out and that
[0:00:19] you're already following.
[0:00:23] Ensuring Copilot works with existing
[0:00:25] patterns and practices our organizations
[0:00:27] have set forth is key to success. To
[0:00:30] support this, Copilot has several
[0:00:32] capabilities between instructions files,
[0:00:35] custom agents, and agent skills to
[0:00:37] ensure you get the code and activities
[0:00:40] how do you have completed them if you
[0:00:42] did them manually. Let's explore each of
[0:00:44] these separately, then bring them
[0:00:46] together at the end to see how they help
[0:00:49] us form a cohesive strategy. Let's start
[0:00:52] with instructions. Sort of as the name
[0:00:54] would suggest, instructions are exactly
[0:00:56] that, instructions to Copilot. They
[0:00:59] provide Copilot the background of both
[0:01:01] what we're building and how we're
[0:01:03] building it. Defined in markdown files,
[0:01:05] instruction files come in two core
[0:01:07] varieties, a single centralized Copilot
[0:01:10] instructions file, which is project
[0:01:12] level, and dot instructions file, which
[0:01:15] allow you to target specific types of
[0:01:17] files like tests or code used to define
[0:01:20] APIs. Let's make a quick request of
[0:01:22] Copilot to see the impact of
[0:01:25] instructions files. I'll ask for an API
[0:01:27] to be generated, which in the case of my
[0:01:29] application is done using Python and
[0:01:32] Flask. We can see the response is
[0:01:34] relatively generic. It follows my
[0:01:36] existing patterns, but let's say our
[0:01:38] organization requires docstrings. Let's
[0:01:41] add a Copilot instructions.md
[0:01:44] file. The Copilot instructions file is
[0:01:46] global to that entire project and always
[0:01:48] in context. If we explain we always want
[0:01:52] docstrings, then send the same command,
[0:01:55] we see the impact of this. A docstring
[0:01:57] is now included with the function in the
[0:02:00] generated code. Copilot instructions is
[0:02:03] table stakes. Every project should have
[0:02:06] one. It's so important in fact that
[0:02:08] there's a slash command to generate
[0:02:09] them, slash init. This will give you a
[0:02:12] great starting point from which you can
[0:02:14] add specifics about your project. Now,
[0:02:16] dot instructions files allow you to get
[0:02:19] more specific, targeting individual
[0:02:21] types of files. In our Flask API, for
[0:02:24] example, we have specific requirements
[0:02:26] on how we want those files to be built.
[0:02:29] By adding the dot instructions files, we
[0:02:31] can break down our instructions into
[0:02:33] smaller chunks. The apply to section
[0:02:36] accepts a path, which will be used by
[0:02:38] Copilot to determine when to use that
[0:02:41] provided context. In our case, we've
[0:02:45] specified Python files in our server
[0:02:47] routes folder. As you might expect,
[0:02:50] there are common instructions you might
[0:02:51] want to add like how to create React
[0:02:53] components or Playwright tests. There's
[0:02:56] a collection of instructions files you
[0:02:58] can quickly add to your project at
[0:03:00] gh.io/awesome-copilot.
[0:03:04] Turning our attention to activities and
[0:03:06] tools we might want to provide Copilot
[0:03:09] are agent skills. Skills can be used to
[0:03:12] tell Copilot both how we want to create
[0:03:14] that code, but how we want to perform
[0:03:16] lower level tasks. They are defined with
[0:03:18] markdown files and even scripts in the
[0:03:21] .github/skills
[0:03:23] folder. We've got a skill here for
[0:03:25] creating contributions to a repository.
[0:03:28] It instructs Copilot to look for
[0:03:30] contribution guidelines and issue and
[0:03:33] pull request templates. If those exist,
[0:03:36] it will use those or use the templates
[0:03:39] we've given it as an example to ensure
[0:03:42] Copilot is doing its best work. Skills
[0:03:45] can be called by using them as slash
[0:03:47] commands, make contribution in our case,
[0:03:50] or dynamically through natural language.
[0:03:53] When we ask Copilot to make a pull
[0:03:55] request or PR, it automatically kicks
[0:03:58] off that skill following the guidance
[0:04:00] provided. It generates a new branch, an
[0:04:03] issue, logically groups commits, and
[0:04:06] eventually creates a PR using the
[0:04:09] template defined in the repository. And
[0:04:11] just like before, there are skills
[0:04:13] available that you can use in your
[0:04:15] projects at gh.io/awesome-copilot.
[0:04:20] Now, for larger tasks, we have custom
[0:04:22] agents. Custom agents, defined in
[0:04:24] markdown files either in .github/agents
[0:04:28] or by your organization, allow you to
[0:04:30] create specialized workers for
[0:04:32] particular scenarios. Let's take
[0:04:34] accessibility as an example.
[0:04:36] Accessibility is, of course, important
[0:04:39] and we always want to get it right.
[0:04:41] It can also require updates to numerous
[0:04:43] parts of our application and some
[0:04:45] specialized skills. Custom agents have
[0:04:48] their own context and are built for
[0:04:50] exactly this.
[0:04:51] Using the slash agent command, we see
[0:04:54] the list of agents that are available.
[0:04:57] Let's activate that accessibility agent
[0:04:59] and ask Copilot to perform a review
[0:05:02] identifying the most impactful updates
[0:05:04] that could be made to our code.
[0:05:07] Just as before, Copilot diligently
[0:05:09] performs the task, this time as the
[0:05:11] accessibility custom agent.
[0:05:14] Once it generates the suggestions, we
[0:05:16] can then ask it to apply them and off it
[0:05:18] goes.
[0:05:19] Instructions, skills, and agents are all
[0:05:22] defined as markdown files, and you might
[0:05:25] be wondering when to use each. It's
[0:05:27] important to highlight that these are
[0:05:29] built to be used in harmony with one
[0:05:31] another rather than in either/or
[0:05:34] approach.
[0:05:36] Instructions provide context on how best
[0:05:38] to generate code, the things Copilot
[0:05:41] should be considering as it modifies and
[0:05:43] updates the code base.
[0:05:45] Skills are tools in Copilot's toolbox
[0:05:48] for performing tasks like how it should
[0:05:50] approach running tests and recovering
[0:05:52] from failures or creating a PR to a
[0:05:55] project. And agents are built to handle
[0:05:58] more complex tasks like performing
[0:06:00] search engine optimization or an
[0:06:02] accessibility review, which might
[0:06:04] require updates to the entire project.
[0:06:07] Working together, these features ensure
[0:06:09] tasks are completed correctly, both what
[0:06:12] needs to be done and how it needs to be
[0:06:15] done.
