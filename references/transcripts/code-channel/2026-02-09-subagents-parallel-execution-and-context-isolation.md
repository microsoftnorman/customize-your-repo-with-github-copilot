---
video_id: GMAoTeD9siU
title: "Subagents: Parallel Execution and Context Isolation"
url: https://www.youtube.com/watch?v=GMAoTeD9siU
channel: "@code (Visual Studio Code)"
published: 2026-02-09
speakers:
  - Harald Kirschner
  - James Montemagno
topics:
  - sub-agents
  - agent-sessions
  - custom-agents
  - context-isolation
  - model-selection
relevance: primary
---

# Subagents: Parallel Execution and Context Isolation

Harald Kirschner explains how VS Code uses subagents to parallelize context gathering, isolate agent state, and keep the main agent loop focused on higher-value reasoning and execution tasks.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Introduction and overview |
| 03:01 | Understanding agents and context |
| 08:04 | Sub-agents and context isolation |
| 13:51 | Daily development practices |
| 17:52 | Custom agents and orchestration |
| 24:22 | Model selection and performance |

## Key Topics Covered

- **Agent loops** — How prompts, tools, and context accumulate over a session
- **Subagents** — Why VS Code delegates context gathering and parallel work to isolated subagents
- **Context isolation** — How separate context windows reduce noise in the main agent thread
- **Custom agents** — How specialized personas and workflows fit into subagent orchestration
- **Model selection** — Why different models are used for different tasks in the agent loop

## Links

- v1.109 Release Notes: https://code.visualstudio.com/updates/v1_109
- Agents Overview: https://code.visualstudio.com/docs/copilot/agents/agents-tutorial
- Subagents Overview: https://code.visualstudio.com/docs/copilot/agents/subagents
- VS Code Insiders Podcast subscription: https://www.vscodepodcast.com/subscribe
- VS Code on GitHub: https://github.com/microsoft/vscode

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Welcome back everyone to the VS Code
[0:00:02] Insiders podcast, the behindthescenes
[0:00:05] look at your favorite code editor, VS
[0:00:07] Code. I have with me yet again Harold
[0:00:11] from the VS Code team. How's it going
[0:00:13] Harold?
[0:00:13] >> Hi James. Thanks for having me back.
[0:00:18] It's good to have you back. And I think
[0:00:19] there's been so much new change and so
[0:00:22] many new things that probably since the
[0:00:24] last time you were on, the team has
[0:00:26] added about 5,000 new features.
[0:00:28] Yes, this release. I was just showing it
[0:00:31] in a live stream. Just scroll through.
[0:00:33] It's like endless endless goodies and a
[0:00:36] lot of really powerful new features and
[0:00:38] the UX on top of it is amazing, too. So,
[0:00:41] it's been amazing how it's all coming
[0:00:43] together and how we can move so much
[0:00:45] faster now on the VS Code side, too. So,
[0:00:47] it's a lot.
[0:00:50] It's a lot. But I feel like one thing
[0:00:52] that I've really appreciated
[0:00:54] is that things feel a little bit more or
[0:00:57] do feel pretty natural in their
[0:00:59] evolution. So some of the things that
[0:01:01] are new features just end up lighting
[0:01:03] up, right? So for example, if I have MCP
[0:01:05] servers that now all of a sudden have
[0:01:06] MCP apps built into them for UI, they
[0:01:09] just show up, right? If I have different
[0:01:10] agents or different things, like the UI
[0:01:13] is pretty much still all there, but a
[0:01:14] little bit more cleaner, a little bit
[0:01:16] more based on the feedback coming in.
[0:01:17] and the tasks are coming in a little bit
[0:01:19] more. And like one of the topics today
[0:01:20] that we're going to talk about sub
[0:01:21] agents like kind of just happen
[0:01:24] automatically like I think that's kind
[0:01:26] of cool about this point in time with AI
[0:01:28] development is that there are a lot of
[0:01:31] things you can go crazy deep on and
[0:01:33] really customize but now more than ever
[0:01:35] like a lot of things just happen out of
[0:01:37] the box.
[0:01:39] >> Yeah, totally. I think I we have this
[0:01:41] planage now for a few. I think we've
[0:01:43] announced it at Universe last year was
[0:01:45] like the big big thing and it's one of
[0:01:48] these key elements
[0:01:50] that you don't have to customize much
[0:01:52] like just use plan mode and you get
[0:01:54] better results like you can iterate. You
[0:01:56] spend more time up front to gather
[0:01:58] context and align and like discuss and
[0:02:01] maybe let your assumptions be
[0:02:02] challenged. Um and then you don't have
[0:02:05] to create your own like eventually if
[0:02:07] you really wanted to you can make your
[0:02:08] own plan mode. Maybe you want to read
[0:02:10] like more more context from some MCP
[0:02:12] servers. Maybe your plan has to be super
[0:02:15] short. Maybe your plan has to be
[0:02:16] extremely long. So everybody wants to
[0:02:18] customize it, but like the out of the
[0:02:20] box experience like it's just a really
[0:02:23] nice experience plan mode and now with
[0:02:26] the latest experience is even better.
[0:02:27] But also where sub agents really help
[0:02:29] with that context
[0:02:31] um to to bring it in into the right
[0:02:34] places without overloading um where it
[0:02:37] just works. So you don't have to think
[0:02:38] about sub agents. It's just doing a
[0:02:40] really nice job context engineering for
[0:02:42] you.
[0:02:44] >> Well, let's talk about that a little bit
[0:02:45] first. And let's first start with just
[0:02:47] agents, right? I'm inside of agent, you
[0:02:49] know, agent mode with the agent agent or
[0:02:52] the plan agent and then this is the mode
[0:02:54] of the thinking that the agent is there
[0:02:56] and a lot of people hear a few words
[0:02:58] which is like what is an agent and what
[0:03:01] is context that it has. So removing
[0:03:04] anything about sub agents or anything
[0:03:06] like that, just kind of break down what
[0:03:08] an agent is, how it works, and what sort
[0:03:11] of that context engineering and context
[0:03:13] window things are basically.
[0:03:16] >> Yeah, I think it's really important to
[0:03:17] understand and if you understand it, you
[0:03:19] can use it more effectively. It's part
[0:03:20] of this I think kind of unraveling the
[0:03:23] black box. So the the agentic loop that
[0:03:27] runs inside VS code or copilot CLI
[0:03:30] basically all starts with you giving it
[0:03:33] a question
[0:03:35] and then the the agent loop takes that
[0:03:38] question takes its system prompt which
[0:03:41] basically gives it some idea of how it's
[0:03:42] how it's supposed to act how it's
[0:03:44] supposed to talk how it's supposed to
[0:03:46] reason about what it's solving some
[0:03:48] which also depends on different models.
[0:03:50] So there's a lot of tweaking in that
[0:03:51] area usually uh that we do and then it
[0:03:54] has access to tools and a way
[0:03:56] [clears throat] it calls tools and you
[0:03:58] see that if you open up your code it
[0:04:00] will start to to do thinking about what
[0:04:02] it's supposed to do. Now those those
[0:04:05] like thinking blocks move into like
[0:04:07] reasoning blocks that you see kind of
[0:04:09] open and close as it does that and
[0:04:11] that's one loop. Um and then it starts
[0:04:14] calling tools and all of that kind of is
[0:04:16] accumulating in a conversation. So you
[0:04:19] see the agent thinking oh the user asked
[0:04:21] me to find uh to explain something in
[0:04:24] the codebase then it will start like oh
[0:04:27] I should probably look at the codebase
[0:04:28] and then then it leads to the first tool
[0:04:30] call where it starts to do a grap search
[0:04:33] maybe to find that term and that's and
[0:04:35] that's where the agent that's like the
[0:04:38] first turn where it stops that's a tool
[0:04:39] call so that that gets handed to the
[0:04:41] editor and what's cool is VS Code has a
[0:04:44] bunch of really powerful search tools
[0:04:46] that are exposed to the agent so VS code
[0:04:49] will basically do that search. If it's a
[0:04:51] grab or semantic search, it will return
[0:04:54] that result to the agent and then
[0:04:56] continue the loop. So the loop pauses
[0:04:58] for a moment to do the search, then
[0:05:00] continue on. Then the agent continues
[0:05:02] with that new information like it ran
[0:05:04] the tool, it got the result, and that's
[0:05:06] added to the conversation. So now the
[0:05:08] agent has the system prompt, the user
[0:05:11] question, the thinking it did, the tool
[0:05:15] call it where it wanted to grab and then
[0:05:18] the response and it can continue from
[0:05:20] there. What's cool as well though that
[0:05:23] the agent can actually run parallel tool
[0:05:25] calls. It could say like grab for this,
[0:05:27] grab for that, grab for this and then
[0:05:29] the all these two calls come in at once
[0:05:32] and all the responses will be done by
[0:05:34] put into VS code and then it continues
[0:05:36] on. So pool calling is really powerful
[0:05:38] in a way that can scale. Uh but as you
[0:05:41] basically as you continue doing that um
[0:05:43] the agent gathers like which files then
[0:05:46] can read the files that's another tool
[0:05:47] call and all of that builds up in a
[0:05:50] large conversation basically and that's
[0:05:52] that's your context window. So once the
[0:05:54] agent has done a few of the tool calls
[0:05:55] it will have it will has a few file
[0:05:57] paths of where to look. It will have
[0:05:59] looked at the files maybe grabbed like
[0:06:01] the first few lines to understand the
[0:06:03] file for any files it found really
[0:06:05] useful. it started to read the full file
[0:06:07] and all of that is building up context
[0:06:10] to eventually answer a question like
[0:06:11] okay now I understand how this feature
[0:06:13] works um here's my explainer maybe it
[0:06:15] gives you a mermaid diagram because that
[0:06:16] just shipped and it can it can do
[0:06:19] interesting things with that context and
[0:06:21] maybe implement the feature right but
[0:06:23] that
[0:06:24] that um context buildup especially as it
[0:06:28] explores and learns about a topic um is
[0:06:32] is really interesting part to understand
[0:06:34] and Now we also in VS Code we have a
[0:06:37] little context indicator so you see in a
[0:06:39] conversation how much context the agent
[0:06:41] has built up. So it's less you reasoning
[0:06:44] about how long it takes. So it's much
[0:06:46] easier to understand how that agent loop
[0:06:47] works now. Um aside from all the tool
[0:06:49] calls but also the the context that's
[0:06:51] being added.
[0:06:54] Yeah. And the interesting part of that
[0:06:56] that I'm thinking is, you know, as this
[0:06:58] sort of context flows in and out and it
[0:07:02] builds up and these tools are being
[0:07:04] called, I think you made an interesting
[0:07:06] point, which is certain select parts of
[0:07:09] that information are important, but
[0:07:11] other ones aren't. And I think this is
[0:07:13] where that sort of idea of sub aents
[0:07:16] comes from which is hey if I'm having a
[0:07:18] long planning running session how much
[0:07:22] of what actually was researched and
[0:07:24] added to the context window is important
[0:07:26] right is it all that deep research is
[0:07:28] that gring all this other stuff what's
[0:07:30] the actual return so I think this is the
[0:07:32] case where how much context isn't needed
[0:07:37] in the main agent like in the main agent
[0:07:39] to actually get the job done and I think
[0:07:41] this is sort of where sub aents come in
[0:07:43] and people are going to start seeing
[0:07:44] this and why we wanted to talk about it.
[0:07:46] They probably already seeing it inside
[0:07:47] of VS Code and they see it literally
[0:07:49] will say sub agent running these things,
[0:07:51] right? Before you would just see all the
[0:07:52] tool calls which is cool to see. Now
[0:07:55] you're seeing sub agent doing this
[0:07:57] thingup. So how is that different than
[0:07:59] the main agent running and like when
[0:08:01] does that sub agent kick in?
[0:08:04] >> Yeah. So the sub agent basically is its
[0:08:06] own agent loop with its own context.
[0:08:10] And most often I think the best way to
[0:08:13] describe it is is you want to delegate
[0:08:16] something like if I I I get asked a lot
[0:08:19] by engineers like hey what how like
[0:08:22] inform this issue like find out like why
[0:08:25] people actually want this want this
[0:08:26] feature like do we need to do this
[0:08:28] feature and that's them offloading and
[0:08:31] like here here's a feature we might want
[0:08:33] to do like here's a here's a Reddit
[0:08:35] thread some people commented maybe
[0:08:37] there's some customers to talk to and
[0:08:39] then I come tag and like here's the
[0:08:41] reason why people like this. Um they're
[0:08:44] it's a it's a problem they are aware of.
[0:08:47] Uh it's a problem that that blocks them
[0:08:48] to do these other jobs. Um these are the
[0:08:52] kind of customers I talked to. Uh these
[0:08:55] are the kind of users. So basically like
[0:08:57] you don't need all the context of all
[0:08:58] the things I read like you just want to
[0:09:01] know the summary and that's what sub
[0:09:03] agents are really good at. So sub agent
[0:09:05] in planning for example is just being
[0:09:08] handed like look at how authentication
[0:09:11] is implemented um and how we would add a
[0:09:14] new provider to it and then the sub
[0:09:16] agent gets that task and it has all um
[0:09:19] in case of planning it has only read
[0:09:21] readon access to tools. So it can look
[0:09:23] at the codebase find files it doesn't do
[0:09:25] any edits because it's plan mode but it
[0:09:28] can do these things really efficiently.
[0:09:30] it can look at a lot of files, run this
[0:09:32] agent loop, isolate it from the main
[0:09:34] loop. So, it's own little agent loop uh
[0:09:36] that just runs on this one task and once
[0:09:39] it's done with the task, it just returns
[0:09:42] all the things it found to in a nicely
[0:09:45] brief summarized way to that planning
[0:09:48] agent main loop. So, it
[0:09:50] [snorts and clears throat] means that
[0:09:51] that the all the planning agent does it
[0:09:54] gives the task. So that's one piece of
[0:09:55] context like the the tool call to this
[0:09:58] to this sub agent tool like do this
[0:10:01] research and then all it gets back is
[0:10:03] like this is what I found. So all that
[0:10:05] file reading and directory listing and
[0:10:09] uh like testing hypothesis like oh off
[0:10:12] might be here no it's not over here like
[0:10:13] that's a different off or is that
[0:10:15] [clears throat] the right author I have
[0:10:15] two off files now which one should I
[0:10:17] pick like need more research. So there's
[0:10:19] a lot of divergent and converging
[0:10:21] exploration these agents do but all you
[0:10:23] get back is like this is what I found
[0:10:25] and then maybe some confidence with it
[0:10:27] as well. So that's that's the sub agent
[0:10:30] solution uh that context isolation to do
[0:10:33] is like a specific task and the example
[0:10:36] here is the easiest is read only right
[0:10:38] you can really easily paralyze um
[0:10:41] paralyze hard word um to to different
[0:10:44] sub agents because you can give them
[0:10:46] different areas to research great for
[0:10:48] code review for example that's another
[0:10:51] topic like you you don't want to read
[0:10:52] all the files like if you do one code
[0:10:54] preview on the main main loop you just
[0:10:57] run out of everything you might want to
[0:10:59] look at. But if you say, okay, one sub
[0:11:01] agent for um security, one sub agent for
[0:11:05] architecture, one sub agent checking
[0:11:07] code reviews, like checking the slop
[0:11:08] that AI potentially generates where it
[0:11:10] doesn't use existing um functionality,
[0:11:12] maybe that's a whole new utility for
[0:11:14] something you already had and you can
[0:11:16] they can all do their thing and it's
[0:11:19] different
[0:11:21] focus areas. So it's different ways how
[0:11:23] you would look for it and then return
[0:11:25] like security looks good. you might want
[0:11:27] to check this out. And then slop,
[0:11:29] there's a new function here. You don't
[0:11:30] need to create like they all just return
[0:11:32] their review findings. Um, and which
[0:11:35] means a you can run those isolated and b
[0:11:39] you can run them in parallel.
[0:11:42] And I think the important aspect here
[0:11:44] too and why sub agents are so important
[0:11:46] besides the isolation running them in
[0:11:48] parallel specialized task execution is
[0:11:50] that they each have their own context
[0:11:52] window. Right. like you were saying is
[0:11:54] you're me as developer I want to care
[0:11:57] about like that main circle that's being
[0:11:59] filled up the main context as it's going
[0:12:02] but these sub agents like you said just
[0:12:04] return back the results right here's the
[0:12:06] important thing back to the main agent
[0:12:07] so those sub aents and you can correct
[0:12:09] me if I'm wrong have isolated context
[0:12:12] windows as well that are sort of are
[0:12:13] they just like thrown away at the end of
[0:12:15] the day or how do those work
[0:12:17] >> yes that's I think a key aspect which
[0:12:20] somehat makes them challenging to use
[0:12:21] potentially that they start with zero
[0:12:24] context. All the context that they have
[0:12:26] is coming from either the custom agent
[0:12:29] definition if you use one or from the
[0:12:31] parent basically telling them the the or
[0:12:33] the agent orchestrator kind of the main
[0:12:36] agent to like this is your task and then
[0:12:38] they start from scratch and they try to
[0:12:40] do that task and then they answer and
[0:12:42] then they go away. So that's the kind of
[0:12:46] isolated one on oneot way that that
[0:12:49] these agents work. there's no user
[0:12:51] interaction. They won't ask you. They
[0:12:54] won't uh there's some um tool
[0:12:57] permissions that that could pop up if
[0:12:59] they don't have all the permissions yet.
[0:13:01] But that's I think something to keep in
[0:13:03] mind as well. The the very ephemeral
[0:13:06] memory. It's like a new conversation
[0:13:07] that you open in in your agent window.
[0:13:11] There's no context from what the other
[0:13:13] window was that you just did. It's a
[0:13:15] it's a new day for the AI. Hopefully
[0:13:17] your instructions are good and it says
[0:13:19] access to GitHub memory to understand
[0:13:21] what it what it should and shouldn't do,
[0:13:23] but other than that it's it's it's
[0:13:25] fresh.
[0:13:28] >> That makes a lot of sense. And I think
[0:13:29] like that's a good context for people to
[0:13:31] have, especially if you start to like go
[0:13:33] further with sub agents, start to create
[0:13:35] agents that you kind of outline and
[0:13:38] delegating tasks out to sub agents. But
[0:13:40] I think before we even move on to that,
[0:13:42] like I think from a day-to-day, I'm
[0:13:44] inside of VS Code. I'm using plan agent,
[0:13:48] the main agent, ask agent. Are there any
[0:13:52] things that I should just be aware of
[0:13:54] from like a prompting standpoint or a
[0:13:58] what's being shown? Like should I think
[0:14:01] about things differently now with these
[0:14:02] sub agents getting spun up? Should I
[0:14:04] change my terminology like in some how I
[0:14:07] write? right? Like if I tell it to use
[0:14:08] sub agents, like are there things just
[0:14:10] in my normal day-to-day development that
[0:14:12] I should be thinking about, you know,
[0:14:14] just in like the main loop?
[0:14:17] >> Yeah. So, I think the goal is
[0:14:21] everything you do will already be
[0:14:24] isolated and run in parallel as much as
[0:14:27] possible.
[0:14:29] uh right now it you can fall into that
[0:14:32] pit of success by using plan mode where
[0:14:34] the expiration that the agent's already
[0:14:36] doing um will be already run in a sub
[0:14:40] agent so you get that benefit of context
[0:14:42] isolation.
[0:14:44] So that's already an existing area. So
[0:14:45] plan mode is like if you're already not
[0:14:48] if you're not not doing it yet uh start
[0:14:50] doing it and you already get the sub
[0:14:51] agent benefit.
[0:14:53] The
[0:14:55] other way is like we once you ask the
[0:14:58] agent to do things in parallel and give
[0:14:59] it guidance on like then you don't
[0:15:03] necess need to mention sub agents or do
[0:15:05] any context engineering around it just
[0:15:07] mention oh like look at these things
[0:15:10] maybe
[0:15:11] runs parallel searches and we'll already
[0:15:13] start doing that as well uh eventually I
[0:15:16] think what we want to get and what we're
[0:15:18] having in our
[0:15:20] uh what I'm working on right now is that
[0:15:21] like out of the box if you have a larger
[0:15:24] more complex plan which multiple
[0:15:26] multiple phases that can run parallel
[0:15:29] then right now if you do that you
[0:15:31] probably already get parallel sub aents
[0:15:33] but it still requires you to like write
[0:15:34] out the plan in a way like annotating
[0:15:37] what can be run in parallel so that's
[0:15:38] something you can do in your planning as
[0:15:40] well as you maybe write specs or
[0:15:41] something else that is longer lift and
[0:15:44] executed through multiple iterations uh
[0:15:47] calling out what can be run parallel and
[0:15:49] the agent will will do that um as well
[0:15:51] very likely It's always indeterministic.
[0:15:53] So there's never like like the shorefire
[0:15:55] way. And that's that's on us to like
[0:15:57] it's one of my goals. Like I want to see
[0:15:59] everybody benefiting from sub agents
[0:16:01] heavily in their in the day-to-day that
[0:16:03] they run as well as possible. So you'll
[0:16:05] see a lot of improvements over the
[0:16:07] coming weeks and months in that area
[0:16:09] that it will just do it out of the box
[0:16:12] like magically like oh there's a back
[0:16:15] end and a front end and I can in
[0:16:17] implement them independently like here
[0:16:19] is like here's my front end sub aent
[0:16:20] implement here's my backend implement
[0:16:23] and in the end they they make sure like
[0:16:25] it all aligns because they have a good
[0:16:27] plan to start with and that's really
[0:16:28] where it all starts that's how work can
[0:16:32] run in parallel once you have a solid
[0:16:34] plan that has all the nitty-gritty
[0:16:36] details because otherwise paramentation
[0:16:39] is a really hard problem, right? Because
[0:16:41] like like just how you ask one team
[0:16:43] member like implement the front end and
[0:16:44] the other team member implement the back
[0:16:45] end and when they don't talk to each
[0:16:47] other, you probably don't end up with a
[0:16:49] product that works. So they and sub
[0:16:51] agents cannot really orchestrate that
[0:16:54] much. They still end up writing
[0:16:56] something and then they probably send it
[0:16:58] back to the main agent like I did it and
[0:16:59] then the main agent can say like yeah
[0:17:01] but I have two sub agents who did
[0:17:02] something very differently. So that
[0:17:04] orchestration bit needs a lot of upfront
[0:17:06] context building and planning.
[0:17:09] >> That makes a lot of sense. Well, let's
[0:17:11] get a little bit deeper here too that we
[0:17:13] have sort of like the the base layer
[0:17:15] down of agents and sub agents and
[0:17:17] context windows because I get a lot of
[0:17:19] questions, you know, next around a like
[0:17:22] inherently there's built-in, you know,
[0:17:24] the main agent, your ask agent, your
[0:17:27] plan agents, but I'm thinking about
[0:17:29] creating my own custom agents. I think
[0:17:32] what's interesting as I've been talking
[0:17:33] to a lot of developers is like there's a
[0:17:35] lot of new tools in our toolbox, right?
[0:17:37] We have instructions, we got prompts, we
[0:17:39] got MCP servers, we got skills, we got
[0:17:42] custom agents, we have all these things
[0:17:44] and they all were built to solve a
[0:17:47] problem and they're a solution. And
[0:17:48] sometimes those things and the solutions
[0:17:50] start to overlap a little bit too. But I
[0:17:53] want to talk about specifically custom
[0:17:56] agents because now that we have the
[0:17:58] ability to start to like think about
[0:17:59] orchestrating these agents like the main
[0:18:02] agent is doing one way and plan agent is
[0:18:04] doing another way but me as a team I may
[0:18:07] want to inherently think about sort of
[0:18:10] almost replacing that system prompt
[0:18:12] right and that's where those custom
[0:18:14] agents come in. So you talk a little bit
[0:18:16] about in our our year February of 2026,
[0:18:21] how should developers be looking at
[0:18:23] custom agents and how does that change
[0:18:25] actually with sub agents?
[0:18:29] >> Yeah. So there's an evolution here. So
[0:18:31] one is in the beginning we had chat
[0:18:34] modes which allowed you to customize
[0:18:38] like change the persona and the workflow
[0:18:41] of how the agent works. So plan mode
[0:18:43] easiest example code review another one
[0:18:46] like it's like distinctive workflows
[0:18:49] that you want to spend more time in that
[0:18:51] you maybe have multiple turns like code
[0:18:54] review is not a one shot you want to
[0:18:55] like oh like also look at this or uh
[0:18:58] take a deeper look into this. So they
[0:19:02] they have been there to like reduce this
[0:19:04] amount of tools the agent has access to
[0:19:06] and give it a more specific workflow and
[0:19:09] goal.
[0:19:11] um they have evolved into custom agents.
[0:19:13] Same same thing, new name uh but has
[0:19:16] kind of come out of the ecosystem of
[0:19:19] what we call things. Um and now with
[0:19:25] this release,
[0:19:27] custom agents can be used for sub
[0:19:29] agents. And what this means is that if
[0:19:31] you create a custom agent like deep code
[0:19:35] research which has like the way you want
[0:19:38] to look at a repo like I want to like
[0:19:41] start broad and but also look at other
[0:19:43] repos maybe it has like a cross repo
[0:19:45] awareness as well that you you're
[0:19:46] enforcing to resolve more of the
[0:19:48] dependencies right maybe there's like a
[0:19:51] specific thing like how you want how you
[0:19:53] would look at your repo to better
[0:19:55] understand it like look at this
[0:19:56] dependency folder first and then like
[0:19:58] maybe it's a monor repo So you could you
[0:20:00] could bring this into a custom agent and
[0:20:03] then with sub agents now you have a
[0:20:07] description in that custom agent use
[0:20:09] when trying to understand crossreo
[0:20:11] dependencies like that's that's your
[0:20:14] that's your um cross repo agent that you
[0:20:18] can then reuse. So crossreer agent with
[0:20:21] that description will then be invoked by
[0:20:24] your main agent the just the agent in VS
[0:20:26] code once a problem needs cross reper
[0:20:30] understanding. So you can see basically
[0:20:32] what happens like oh like explain how
[0:20:34] off works across these repos then the
[0:20:36] agent has a list of all the custom sub
[0:20:40] aents uh that are available and then it
[0:20:43] can call them and you call them in a sub
[0:20:45] aent way. You could do the same thing in
[0:20:48] a skill in an agent skill which we
[0:20:50] shipped but then you would need to
[0:20:53] handle that orchestration yourself.
[0:20:55] Maybe the agent skill says oh like use a
[0:20:58] sub agent and then query these things
[0:21:00] and then maybe in that workflow the
[0:21:02] agent also has other tools available
[0:21:04] because the skill cannot constrain
[0:21:06] tools. So suddenly gets it might get
[0:21:09] confused or distracted by what you're
[0:21:12] trying to do. So a custom agent is a
[0:21:14] very singlepurpose thing. All it will
[0:21:16] return is like the based on its
[0:21:18] workflow, based on its input and based
[0:21:20] on what you tell it how its output is.
[0:21:22] So it's a very that's that's what makes
[0:21:24] it so um composable
[0:21:27] and skills are composable too but skills
[0:21:29] will end up in your main context and
[0:21:31] when they describe a very strict
[0:21:33] workflow then there might be less
[0:21:36] adherence because they're in that in
[0:21:38] your context with all the other stuff
[0:21:39] that might be there. So there might be
[0:21:41] multiple skills. There might be like
[0:21:42] other custom instructions in the repo.
[0:21:44] It might just more more noise and less
[0:21:48] likely. There's some some blog post that
[0:21:51] got shared a lot from versel on skills
[0:21:54] versus agents.mmd. So skill still has to
[0:21:57] be discovered by the by the main agent
[0:22:01] like oh like I'm I'm working on the user
[0:22:04] is asking me about like this this kind
[0:22:06] of file type. Maybe it's like a Jupyter
[0:22:08] notebook and there's a skill for Jupyter
[0:22:10] notebooks. So it has to realize
[0:22:13] like that mapping like oh I need to look
[0:22:14] at the skill and then it needs to read
[0:22:16] the skill and then hopefully there's
[0:22:18] some strict adherence to whatever is in
[0:22:19] the skill how to work with Jupyter
[0:22:21] notebooks and then the counterpart how
[0:22:23] to compare it is like what if you put it
[0:22:25] into agents.mmd which is always in
[0:22:27] context if it's in the root of your
[0:22:30] workspace agent.mmd is always top of
[0:22:32] mind for uh for the agent when it does
[0:22:36] any task. So they found a lot more
[0:22:37] adherence of course because there's like
[0:22:39] an a context bit that's always injected
[0:22:41] in the agent versus another file it
[0:22:44] finds along the way as it works on the
[0:22:46] task. Um and then the same is with
[0:22:49] custom agents. Custom agents once you
[0:22:51] write them that's their persona. That's
[0:22:53] all they think about. So that's thing if
[0:22:55] you have something that has to be rock
[0:22:56] solid and really deter deterministic and
[0:22:59] a workflow you really want to get down
[0:23:02] to like the really the the right steps
[0:23:05] then that would be a custom agent.
[0:23:07] >> If it's something more composable where
[0:23:10] it's more guidance for the agent then
[0:23:12] that's that's more skill
[0:23:14] >> and maybe over time skills become
[0:23:16] stronger right we'll always work on
[0:23:19] making sure the agent follows it. Uh
[0:23:21] hopefully people write good skills
[0:23:23] because otherwise that that can like the
[0:23:25] stronger adherence there is the more
[0:23:26] likelihood it is to be a foot gun.
[0:23:30] That's pretty cool. Now one thing also
[0:23:32] that I want to point out too is like
[0:23:34] that
[0:23:36] custom agents can also have specific
[0:23:38] models assigned to them. So in that file
[0:23:41] I think that's also really unique is you
[0:23:42] might say okay these models whether it's
[0:23:45] Gemini or GPT or a claude model is is
[0:23:48] how like the speed the performance like
[0:23:51] the context that it needs might be a
[0:23:52] little bit different and I've actually
[0:23:54] found this a little bit I was I did a
[0:23:56] some a video on the new the plan agent
[0:23:58] updates where you can actually assign
[0:24:02] like a default model for the plan agent
[0:24:06] and then when you go to implement back
[0:24:08] to agent
[0:24:09] you can have a different model. So for
[0:24:11] example, you might be doing research and
[0:24:13] say I want to use something like maybe
[0:24:14] GBT52, but maybe I want to switch over
[0:24:17] to an implement model that's like an
[0:24:19] Opus or a Codeex model for example or a
[0:24:21] Gemini model. So I can use those small
[0:24:23] ones. So for example, in these small
[0:24:25] custom agents, maybe use like a flash
[0:24:27] model for example because they can run
[0:24:29] super fast on a specific task that you
[0:24:32] have. Is that like a a realworld use
[0:24:34] case there for specific models for
[0:24:36] specific use cases or how do you see
[0:24:38] that? Oh, totally. I think that's that's
[0:24:39] one of the key things like why you want
[0:24:41] to have a custom agent too is like that
[0:24:43] how much you control you have over that
[0:24:46] agentic loop and which model it runs in.
[0:24:48] And yeah, there's multiple like the
[0:24:51] three categories of models I think about
[0:24:53] is like one really fast mini models that
[0:24:56] are just good at automating tasks where
[0:24:59] you don't have to reason like here's a
[0:25:00] workflow like just write a commit like I
[0:25:03] have like a get commit push like just
[0:25:05] all the good stuff I do is all in in my
[0:25:08] in my problems and it's all switching to
[0:25:10] really fast models they don't want and
[0:25:12] then they're waiting for CI/CD to finish
[0:25:14] and then they report back right it's
[0:25:16] just like simple things like just like
[0:25:18] something I would probably put in the
[0:25:20] script in the past, but now they're way
[0:25:22] more adaptive by just running an agent
[0:25:24] that that runs the terminal for me. So,
[0:25:26] that'll be like a really fast one. Then
[0:25:28] the other ones um we do have more
[0:25:31] specialized like in in the middle ground
[0:25:34] where they're
[0:25:36] faster and but still doing a little bit
[0:25:39] more reasoning behind it. And that's
[0:25:40] like for code research is a great one.
[0:25:42] Like if you want to look at many files
[0:25:44] and figure out which ones are important
[0:25:46] for a task like what we talked about
[0:25:47] before, that's a that's good model. It's
[0:25:50] also where you could maybe even have
[0:25:51] some fine-tuned models um running
[0:25:53] eventually for on our site. Um and then
[0:25:57] it's like the really heavy planning
[0:26:00] task. And I for example have I'm
[0:26:02] experimenting with a workflow that's
[0:26:04] been really nice where I
[0:26:08] have a custom agent as an orchestrator.
[0:26:11] So you can switch to to this custom
[0:26:13] agent which is called loop because I ran
[0:26:15] out of names. Um [snorts] didn't give it
[0:26:17] a cool name. Uh but then loop as an
[0:26:21] orchestrator will have one really fast
[0:26:24] sub aent to gather context. So again
[0:26:27] like offloading that context of the main
[0:26:30] context loop for better name um to into
[0:26:34] another agent who just writes it to a
[0:26:36] file and that file becomes then the the
[0:26:39] memory for all the other follow-up
[0:26:40] stuff. Then there's a planning one which
[0:26:42] uses a larger model because for planning
[0:26:44] I want to look at kind of the the
[0:26:47] scratch pad that the first agent created
[0:26:48] which might have a lot of interesting
[0:26:50] information that was gathered really
[0:26:52] fast and then planning will look at that
[0:26:54] and do some more reasoning about it
[0:26:55] because that's the larger model with
[0:26:57] opus or 5.2 to codeex and and then next
[0:27:01] up is the implementation which runs
[0:27:03] because the plan is so detailed at this
[0:27:06] point I can take a really fast model
[0:27:08] that's really good at writing code um
[0:27:11] and just churns through it writes
[0:27:13] everything but once and they're actually
[0:27:15] running parallel because the plan
[0:27:17] already is outlined you can run these in
[0:27:19] parallel then because then the
[0:27:20] orchestrator then says okay I can run
[0:27:21] things in parallel here are five
[0:27:24] implement agents doing the work and then
[0:27:28] I'm going to run the code review agent
[0:27:29] which again runs a more expensive model
[0:27:31] to to look at all the code changes in
[0:27:34] context. So that's think the what I see
[0:27:37] right now where it's like and I see it
[0:27:39] happening I think the review takes a bit
[0:27:40] more time but then it's it's better at
[0:27:43] finding the edge cases and sending
[0:27:45] things back like where things diverge
[0:27:47] from the plan because as soon as you run
[0:27:48] things in parallel things might diverge.
[0:27:51] Um so that's that's been really
[0:27:53] interesting. So that's something to play
[0:27:54] around with. Also, you can optimize
[0:27:56] speed and cost and really balance like
[0:28:00] that quality because like right now if
[0:28:02] it's like every hour right everything in
[0:28:03] opus because it's the best model like
[0:28:04] it's not the right strategy. Uh you can
[0:28:07] with customs sub agents you can be more
[0:28:10] efficient and spend less time waiting
[0:28:12] especially in moments where you want to
[0:28:15] iterate fast and that's what I see I do
[0:28:18] in VS Code. I just want to I'm in this
[0:28:21] messy headsp space like I don't know
[0:28:23] what I'm really solving for then I just
[0:28:25] want to see it happening and I don't
[0:28:27] want Opus building a beautiful
[0:28:30] vibe coded UI. I just want to figure out
[0:28:32] like what is that critical thing I'm
[0:28:34] missing and iterate fast.
[0:28:39] Yeah, that's awesome. I love that sort
[0:28:41] of use case. I think talking about it,
[0:28:43] it's about real world about how you're
[0:28:44] developing and I'm the same way like
[0:28:46] really changing and thinking about the
[0:28:48] best model, the best tool, the best
[0:28:50] ability that you know VS Code has for
[0:28:53] that job. Harold, this has been awesome.
[0:28:54] I love going from the beginner all the
[0:28:56] way to this advanced scenario. We'll put
[0:28:58] links to everything in the show notes. I
[0:29:00] really appreciate you come coming on
[0:29:01] talking about sub agents because people
[0:29:03] are gonna start seeing them every single
[0:29:04] day. So, let us know. Give the team
[0:29:06] feedback on the VS Code GitHub. Um,
[0:29:09] yeah. and really appreciate it, Harold.
[0:29:12] >> Thanks so much, James. Thanks everybody.
[0:29:15] >> Awesome. Well, don't forget you can
[0:29:17] subscribe to the VS Code Insiders
[0:29:18] podcast on your favorite podcast
[0:29:20] application and of course you can go to
[0:29:22] vscodeodcast.com. Check out all the
[0:29:24] things. Make sure you follow us on
[0:29:25] YouTube, on Twitter, on your favorite
[0:29:27] socials for all the updates on VS Code
[0:29:30] every single day because insiders ships
[0:29:32] every single day with all goodies for
[0:29:33] your favorite code editor. That's going
[0:29:34] to do it for this VS Code Insiders
[0:29:36] podcast. Until next time, I'm James and
[0:29:38] happy coding.
