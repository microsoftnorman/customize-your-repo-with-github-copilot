---
video_id: flpKLkZla2Q
title: "Customize your agents"
url: https://www.youtube.com/watch?v=flpKLkZla2Q
channel: "@code (Visual Studio Code)"
published: 2026-02-19
speakers:
  - Courtney Webster
topics:
  - custom-agents
  - instructions
  - prompts
  - skills
  - agent-plugins
relevance: primary
---

# Customize your agents

Courtney Webster walks through the customization primitives: instructions, prompts, skills, custom agents, and agent plugins — with live demos in VS Code.

## Key Topics Covered

- **Instructions** — Always-on rules that shape Copilot's behavior
- **Prompts** — Reusable task templates (slash commands)
- **Skills** — Portable capabilities agents can invoke
- **Custom Agents** — Specialized personas with scoped tools
- **Agent Plugins** — Bundled customization packages

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Welcome to the customize your agent
[0:00:02] session at agent sessions day. It's a
[0:00:04] bit of a mouthful, but I'm Courtney, a
[0:00:06] PM on the VS Code team. And the intent
[0:00:08] of this session is for you to leave with
[0:00:11] kind of like a handbook, a playbook for
[0:00:14] how you can customize GitHub C-Pilot for
[0:00:16] your team, their tools, the workflows
[0:00:18] that you guys uh you guys do every day.
[0:00:21] Um, and then how to onboard and where to
[0:00:23] start with them. So, lots to cover in
[0:00:25] this session. Let's go ahead and jump
[0:00:27] in.
[0:00:29] So here's a lot of information on this
[0:00:31] slide about the different options that
[0:00:33] we have in VS Code. So we won't get to
[0:00:35] cover all of them in depth. There's lots
[0:00:36] of great resources um on our docs and on
[0:00:39] our YouTube channel for you to use. But
[0:00:42] um a highle overview for you to keep in
[0:00:44] your back pocket to reference. We have
[0:00:46] instruction files and instruction files
[0:00:49] are kind of like global context files.
[0:00:51] Um, I consider these always on and you
[0:00:55] can have the ones that load for every
[0:00:57] session that are really great for things
[0:01:00] like your codebased guardrails. So, your
[0:01:02] overall architecture um like coding
[0:01:05] guidelines, things like that. Or you can
[0:01:07] have file-based instructions, which are
[0:01:10] patterns um and des uh pattern and
[0:01:12] description match for specific areas. So
[0:01:15] like um Python files only have a certain
[0:01:18] set of descriptions or your test files
[0:01:20] have a certain set of descriptions as
[0:01:21] well and these are used u matched using
[0:01:23] glob patterns. Uh we also have prompts
[0:01:26] which are really just those slash
[0:01:28] commands that you see in chat um best
[0:01:30] for your oneshot workflows. So shooting
[0:01:32] off um making tests or creating a PR
[0:01:36] things like that. We also have custom
[0:01:39] agents. Really cool. You can either
[0:01:41] reference them in the chat dropown or
[0:01:43] via sub aents which we'll touch on later
[0:01:45] in the session. And these are best for
[0:01:46] your constrained workflows. So if you
[0:01:49] want to have um specific tools or a
[0:01:51] model um you don't have to reprompt and
[0:01:53] reconfigure this every time but you can
[0:01:55] just work within a custom agent. We also
[0:01:58] have skills which is something that's
[0:02:00] newer. These are similar to instruction
[0:02:02] files so there's a little bit of overlap
[0:02:04] there but um these the big diff
[0:02:06] differentiator for these is that these
[0:02:08] load on demand. So rather than them
[0:02:10] being always on, always included in your
[0:02:13] context, um they'll load dynamically
[0:02:15] when they're most relevant to what the
[0:02:16] agent's working on. Um these are best
[0:02:18] for reusable capabilities. We have hooks
[0:02:22] as of our last stable release, which is
[0:02:24] awesome. And these are life cycle
[0:02:26] triggers. Um and basically just
[0:02:28] contextual automation is the best way to
[0:02:31] best way to think about it. So rather
[0:02:32] than you having to be mindful of um what
[0:02:36] the agent should do at session start,
[0:02:38] session stop, tool, pre-tool use, post
[0:02:41] tool use, you can automate that with
[0:02:43] hooks. And then Connor had a great
[0:02:45] session on MCP earlier today, so I won't
[0:02:47] spend too much time, but I did want to
[0:02:50] put it on this slide so you have it for
[0:02:51] reference, but I definitely recommend
[0:02:52] going back and checking out his session
[0:02:54] on MCPS. So these are all the different
[0:02:57] ways that you can influence and steer
[0:02:59] how the AI will write code for you um
[0:03:02] and work with you in your codebase. Um
[0:03:05] we have system prompts to make Copilot
[0:03:08] generally successful. Um but like I
[0:03:10] said, it doesn't have all of the
[0:03:12] knowledge um to work best for you and
[0:03:14] your team and their workflows. And
[0:03:16] that's what all of these different
[0:03:18] customization options are best for.
[0:03:21] Uh so to start we'll dive deep a little
[0:03:24] deeper for instructions. Like I said
[0:03:26] these are always on context and they can
[0:03:28] be global or file specific. So in this
[0:03:30] example here I have ones that are
[0:03:32] specific to Python files. So they're
[0:03:34] only going to be included or pulled in
[0:03:36] when you need um when the agent needs
[0:03:38] context for working on Python files. Uh
[0:03:41] some best practices here are to be
[0:03:43] specific. So don't just say you want a
[0:03:46] testing framework but say you're using
[0:03:48] piest for example for u python
[0:03:50] instructions. You should also include
[0:03:52] reasoning where relevant so that the
[0:03:54] agent knows exactly why it should be
[0:03:56] doing what it should be doing so it
[0:03:58] doesn't go off the rails. Um I also like
[0:04:01] to opt for code examples where relevant
[0:04:03] so that it can source relevant
[0:04:05] information. Um and like I said just
[0:04:07] have very specific um instructions on
[0:04:09] like what it should be doing and what it
[0:04:11] should be looking at. And then to avoid
[0:04:13] any context bloat, also skip any rules
[0:04:15] that llinters or formatterers already
[0:04:17] enforce because these are always on and
[0:04:19] so you don't want to, like I said, bloat
[0:04:22] the context window with things that are
[0:04:23] already covered elsewhere.
[0:04:26] Um, similar to instructions are skills.
[0:04:30] The main difference here, like I said in
[0:04:32] the overview, is that rather than them
[0:04:34] being always on, they're loaded
[0:04:36] dynamically. So the agent is only going
[0:04:38] to pull them in when it feels like it's
[0:04:40] relevant. And we'll see this in action
[0:04:42] in a little bit in VS Code, but I think
[0:04:44] that's the best way that I can
[0:04:46] conceptually separate those two since
[0:04:48] there is a considerable amount of
[0:04:49] overlap. Um, and skills can also include
[0:04:52] scripts, examples, and other resources
[0:04:55] as well. So, it's a good way to like add
[0:04:56] capabilities to the agent rather than
[0:04:58] just having a generic always on context.
[0:05:02] Um, so it tailor capabilities for domain
[0:05:05] specific tasks without repeating the
[0:05:07] context and then we'll load them in on
[0:05:08] demand.
[0:05:10] So, let's go jump into VS Code really
[0:05:13] quick and we will talk about
[0:05:19] skills versus um instructions and kind
[0:05:23] of how we can monitor what's being
[0:05:24] pulled in in VS Code because I think
[0:05:26] it's it's um it's interesting to talk
[0:05:29] about these these concepts in a way
[0:05:32] that's very abstract, but if you can't
[0:05:34] tell in VS Code actually what's being
[0:05:36] pulled in, is it working? like are these
[0:05:40] kind of like fluffy abstract concepts um
[0:05:43] are in my repo, but whether or not
[0:05:44] they're actually working is a whole
[0:05:45] different story. Uh so in VS Code, we
[0:05:48] have my arcade app. Um I love to just
[0:05:51] play with this, you know, when I'm bored
[0:05:53] and build on it when I can. Um so it has
[0:05:56] a classic snake game, 2048, which has
[0:05:58] been my game of choice recently, Tetris,
[0:06:01] and then the good old Flappy Bird as
[0:06:04] well. Um, and then we'll see that I
[0:06:07] already have a copilot instructions file
[0:06:09] in here and it covers um like
[0:06:13] architecture elements um has some build
[0:06:17] and test things, conventions, but it's
[0:06:20] it's relatively short. And then I also
[0:06:23] have a in my skills folder, I have a
[0:06:25] debug skill. So, I was finding that um a
[0:06:29] lot of times when Copilot was building
[0:06:31] out new games, we were running into this
[0:06:33] like similar debugging issues. And so,
[0:06:36] uh Copilot helped me create a skill that
[0:06:38] was specific for like looking for
[0:06:40] problems that are relevant to these
[0:06:43] games that I was building. Um so, if we
[0:06:46] just ask Copilot like what is this repo?
[0:06:50] We'll be able to see um off the bat it's
[0:06:53] pulling in my instructions file here. So
[0:06:55] this is um it's just describing to me
[0:06:57] what this repo is, but it's also looking
[0:06:59] at it or instructions. Um so it's a good
[0:07:01] way to demonstrate that always on
[0:07:02] context that we talked about. The other
[0:07:05] cool way to kind of monitor this is in
[0:07:08] the um chat debug log. If you don't see
[0:07:11] this in your activity bar, you can also
[0:07:13] go into the command pallet and look up
[0:07:15] chat debug and it'll open the same view.
[0:07:17] And essentially this gives you the
[0:07:19] opportunity to see all of the tool
[0:07:21] calls, all of the the um background
[0:07:25] for what's being um passed to and from
[0:07:28] the models. So you can see that if I
[0:07:31] click on what is this repo, that's my
[0:07:33] chat request. Um we have the system
[0:07:36] prompt. And then if I also look up for
[0:07:38] copilot
[0:07:40] instructions is I think what the thing
[0:07:42] is called. Yeah. So it's it's pulling in
[0:07:43] my instruction files as well. But if I
[0:07:46] am trying to fix a specific bug in my in
[0:07:50] my game, I say, "Help
[0:07:52] me debug an issue where my key strokes
[0:07:58] aren't always
[0:08:01] working." And I fire that off to the
[0:08:04] agent. I'll close this out. Um, but you
[0:08:07] can see it's picking up my skill
[0:08:08] automatically. So, this debug skill is
[0:08:11] being pulled in. It's reviewing it. And
[0:08:13] then we can also in the the debug logs,
[0:08:16] I believe it might be this one. Yeah.
[0:08:17] So, it's reading my my skill file, which
[0:08:20] is super cool. It's doing it
[0:08:21] automatically just based on the naming
[0:08:23] and the description of the of the um
[0:08:27] skill file, which is just all formatted
[0:08:29] and markdown. Um so, yeah, that's just a
[0:08:33] little bit about skills versus
[0:08:35] instructions, how to access them. Uh
[0:08:38] going back into our slides, the next
[0:08:42] thing that I want to cover is
[0:08:44] um prompts. And prompts are those slash
[0:08:47] commands that we see. They're best for
[0:08:49] one um oneshot workflows. And so similar
[0:08:52] to skills and similar to instructions,
[0:08:54] this is another markdown file. Um all of
[0:08:56] this is really just boiling down to
[0:08:58] markdown files if you haven't caught on
[0:09:00] already. Um, but the cool thing about
[0:09:02] prompts is that you can just instead of
[0:09:04] asking the agent every time to um like
[0:09:07] reprompting and reconfiguring your
[0:09:09] tools, you can just put this all into a
[0:09:11] prompt file and then it makes it really
[0:09:12] easy to just like fire it off and forget
[0:09:15] it. Um, so it is best for common tasks.
[0:09:19] Um, think like clean up my PR before I
[0:09:22] before I create my PR slash test to
[0:09:24] generate tests. Um, and and they're
[0:09:27] stored and accessible via the chat
[0:09:29] input.
[0:09:31] Um the other sort of user invoked um
[0:09:36] idea that we have for custom
[0:09:38] customizations is custom agents and I
[0:09:41] always describe these as role-based
[0:09:43] personas. So on this screen I have an
[0:09:45] example of our plan agent. This is built
[0:09:48] into VS code and you can access this
[0:09:51] file this markdown file um in VS Code
[0:09:54] yourself. I can show you how to do that.
[0:09:57] But basically these again markdown files
[0:09:59] but this is specifically outlining a
[0:10:02] planner on your team for example. So
[0:10:04] their whole job is to just create a plan
[0:10:06] for how to actually execute not actually
[0:10:08] execute. And it has a certain um tools.
[0:10:11] It can have a certain model that it's
[0:10:13] using. Um and then also does the cool
[0:10:15] thing about with handoffs. So you can
[0:10:17] see that um part of the metadata in this
[0:10:20] markdown file has a handoff section and
[0:10:23] it will basically take from the plan and
[0:10:26] then push into implementation
[0:10:29] which is actually like executing on the
[0:10:31] plan. And this can be automated where
[0:10:32] like it doesn't have any it doesn't
[0:10:34] require any manual work on your part as
[0:10:37] the user. It'll just pass off
[0:10:39] automatically or if you want to have
[0:10:40] that kind of like checkpoint guardrail
[0:10:42] feature, you can manually click a button
[0:10:44] to pass it off. Um, so you may want to
[0:10:48] create custom agents for like a security
[0:10:51] reviewer, uh, a very like specific type
[0:10:53] of planner or a solution architect or
[0:10:55] any other specialized role that you see
[0:10:57] your team kind of like having. Um, and
[0:11:01] then each persona has its own behavior
[0:11:04] tools and instructions and it allows you
[0:11:06] to constrain the behavior.
[0:11:09] And as I mentioned at the beginning,
[0:11:12] custom sub aents can either be
[0:11:14] specifically invoked via the dropdown or
[0:11:17] as sub aents. And sub aents is a really
[0:11:19] cool concept that I think some of our
[0:11:21] other presenters have already touched
[0:11:23] on. But what I really want to talk about
[0:11:25] here is that sub aents run in their own
[0:11:28] context window. So, we recently added
[0:11:30] the the context widget um at the in the
[0:11:33] chat input box that shows you how the
[0:11:34] context context window is being used and
[0:11:37] consumed throughout your chat request.
[0:11:39] Um and sub agents basically run in a
[0:11:41] contained context window. This works
[0:11:43] really great because that means it's
[0:11:44] getting input from the orchestrator
[0:11:46] agent. It's doing all of the research,
[0:11:48] all of the digging, and then it's only
[0:11:50] returning what is relevant back to the
[0:11:52] orchestrator and all of that additional
[0:11:54] search context isn't included and isn't
[0:11:56] bloating your context window. Um, so it
[0:11:58] really helps with like parallel par
[0:12:00] parallelization of tasks. Um, and the
[0:12:04] the main agents context really stays
[0:12:06] clean and focused, but it can make your
[0:12:08] workflows move a lot faster. Um, and so
[0:12:12] I'm going to talk about what this looks
[0:12:14] like in VS Code.
[0:12:17] Let's go back to my VS Code. I'm going
[0:12:20] to close out of all of these funky tabs
[0:12:24] so we have a better idea. But if we go
[0:12:27] back to my agents,
[0:12:31] um,
[0:12:33] here I have an accessibil accessibility
[0:12:35] agent, a game maker agent, a janitor
[0:12:37] agent. I have all sorts of different
[0:12:38] agents here. Um, and they have different
[0:12:41] tool configurations and then prompts
[0:12:44] involved in them as well. But if I want
[0:12:46] to go I'll start a new chat. Um,
[0:12:48] speaking of clean context,
[0:12:51] um, I can have this
[0:12:54] say, um, since I have a Game Maker
[0:12:57] agent, I can set here or, um, I can
[0:13:13] have it say, create a new mind sweeper.
[0:13:18] game. What else do I have in my agents
[0:13:21] drop down? Um, what else can I have it
[0:13:24] do?
[0:13:27] Check
[0:13:28] for oops accessibility
[0:13:34] concerns in my project and
[0:13:39] clean up any dead code.
[0:13:44] instead or redundant code.
[0:13:48] Um, okay. So, with sub aents, you don't
[0:13:52] have to necessarily tell the agent to
[0:13:54] run it as a sub agent. You can typically
[0:13:57] it'll figure it out by itself, but for
[0:13:59] purposes of this demo, um, and just to
[0:14:01] ensure that we get to see this in
[0:14:03] action, I'm going to say, um, but run
[0:14:06] these as sub aents.
[0:14:10] Okay, fingers crossed this works.
[0:14:13] live demo. We'll see. Okay, so it's
[0:14:15] thinking um it looks like it's saying
[0:14:17] like it's picking up the agents, the
[0:14:19] experts that it um these different
[0:14:21] to-dos rely on. That's a good sign. Oh,
[0:14:25] okay. Perfect. So, now we see that these
[0:14:28] are running in parallel. So, this is
[0:14:30] what you're looking for. It's kind of
[0:14:31] the shimmer um in chat specifically. Um
[0:14:35] and we have the game maker agent, the
[0:14:37] accessibility expert, and then the
[0:14:39] universal janitor. And we see each of
[0:14:41] them working stream n at this top level.
[0:14:44] And we can expand these and see all of
[0:14:47] the work that it's doing in parallel.
[0:14:50] And then one of these might finish
[0:14:53] faster than the others and they'll keep
[0:14:55] working. I imagine the game maker agent
[0:14:57] is going to work for quite some time. Um
[0:15:00] creating a mind sweeper game, but cool.
[0:15:01] Yeah, the accessibility agent is done.
[0:15:04] And it looks like
[0:15:06] let's see what it reports back. So this
[0:15:08] is the audit report that it's sending
[0:15:10] back. Um, and this is getting sent back
[0:15:14] to this main orchestrator agent to then
[0:15:16] go like actually execute on. Um, if the
[0:15:18] accessibility agent didn't already do
[0:15:20] that. So that's cool. Um, whereas the
[0:15:23] the janitor agent is going to take a
[0:15:26] little bit longer. Looks like already
[0:15:29] added 535 lines of code. It's working
[0:15:31] fast. Let's see.
[0:15:34] Okay,
[0:15:36] cool. Well, I am going to let that roll
[0:15:40] a little bit longer and then go back to
[0:15:43] um our PowerPoint. Looks like we lost
[0:15:47] it. Let's see if I can reopen it.
[0:15:53] Let's see. Um because the last thing
[0:15:55] that I want to talk about is brand new
[0:15:56] in VS Code and it's relevant to hooks.
[0:16:00] So, um, for hooks, they're new and are
[0:16:05] the latest VS Code, um, release, the
[0:16:09] latest VS Code stable release. Um, and
[0:16:11] like I said before, it's great to
[0:16:12] enforce policies, um, at different times
[0:16:16] in the process, the agent execution
[0:16:19] process, for example.
[0:16:23] Let's get back to our PowerPoint slide.
[0:16:26] Sorry. Um, so it's a deterministic way
[0:16:30] to do code-driven automation. Um, so
[0:16:32] what this means in practice is that it
[0:16:34] helps you enforce any security policies.
[0:16:36] So if you want to before a tool goes off
[0:16:39] and fetches something, it can run some
[0:16:42] sort of like security check to make sure
[0:16:43] it's not fetching from um dangerous
[0:16:46] URLs. It can automate code quality after
[0:16:48] agents make edits. Um, it can audit make
[0:16:52] create audit trails um control approvals
[0:16:54] and things like that. And VS Code has um
[0:16:57] supports a bunch of different life cycle
[0:16:59] triggers that you can use with hooks.
[0:17:02] And so it ranges from the session start
[0:17:04] to the session stop, the agent, the sub
[0:17:06] aent start and stop, which we we saw in
[0:17:09] our previous demo, and then tool use,
[0:17:11] compaction, all things like that. And
[0:17:14] then they're all triggered
[0:17:14] automatically. So you don't even think
[0:17:16] have to think about the workflows that
[0:17:17] are being supported with hooks. Um it'll
[0:17:20] just be wired up and then run for you.
[0:17:24] Um, so what I want to show in VS Code is
[0:17:27] that we can observe hooks in our So it
[0:17:34] looks like this is still running, which
[0:17:35] is great because then we can observe
[0:17:36] hooks running potentially as part of
[0:17:38] this. We don't have a great UI for
[0:17:40] observing hooks in our um in this chat
[0:17:44] view, but we can look at the output
[0:17:46] channel um output show output channels
[0:17:50] in the command pallet. There's a lot of
[0:17:52] different output channels that we
[0:17:54] support. Um, which is really nice
[0:17:57] because it helps debug. Um, but yeah,
[0:18:00] this one I is what I'm looking for,
[0:18:02] which is the copilot chat hooks.
[0:18:05] Where did it go?
[0:18:11] This one.
[0:18:13] So, let me close this and expand so I
[0:18:17] can have a
[0:18:22] um a look at this output channel.
[0:18:25] So as we see all of this all of these
[0:18:27] hooks are hooked hook hooked up to like
[0:18:30] trigger automatically. Um so we see the
[0:18:34] um input that's going into it is just
[0:18:36] JSON and then it completes and there's
[0:18:39] an output to let it know if it should
[0:18:42] continue in the life cycle process. Um
[0:18:44] and then this is runs every single time.
[0:18:46] So this is like the 141st time that the
[0:18:49] hook ran. And that way you know that
[0:18:50] your hooks are like hooked up properly.
[0:18:52] Your hooks are hooked up properly. Um
[0:18:54] and that they're actually working as you
[0:18:56] expect.
[0:18:58] Um and hooks are also you can find them
[0:19:01] in your GitHub folder. Um where is my
[0:19:03] hook that I have?
[0:19:07] Um so the one that I have is basically
[0:19:09] post tool use making sure that it's
[0:19:11] formatting correctly. So it just uses um
[0:19:14] like a formatting a formatter um to go
[0:19:17] through and enforce those rules after
[0:19:19] the the agent makes changes and then we
[0:19:21] can monitor that in our output channel.
[0:19:25] Um so where I want to leave you with
[0:19:27] today because I know this was a a really
[0:19:30] big uh lots of content that we covered
[0:19:34] but I think our the best place to start
[0:19:36] is with our instruction files. So, these
[0:19:40] are always on. The biggest bang for your
[0:19:42] buck probably to set the guard rails.
[0:19:44] Um, you can access this via slashinit.
[0:19:47] Um, another slash command, which is
[0:19:49] great. Um, and that's a great place to
[0:19:51] start. If you haven't already, I would
[0:19:53] definitely recommend going to the
[0:19:54] awesome co-pilot repo where you can see
[0:19:56] a bunch of examples from the community
[0:19:58] and from our team of what works well.
[0:20:00] Um, and then kind of add different
[0:20:02] customizations as you see fit and as
[0:20:04] they come up. Um, definitely don't try
[0:20:05] to tackle them all at once because it is
[0:20:07] a lot to cover, but um, just tackle it
[0:20:10] piece by piece and then that way GitHub
[0:20:13] Copilot is customized for you and you're
[0:20:15] getting the most out of your agents.
[0:20:17] Thanks.
