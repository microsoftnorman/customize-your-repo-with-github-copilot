---
video_id: YmpjvZ3xkx8
title: "A Unified Agent Experience"
url: https://www.youtube.com/watch?v=YmpjvZ3xkx8
channel: "@code (Visual Studio Code)"
published: 2026-02-19
speakers:
  - VS Code Team
topics:
  - cloud-agent
  - coding-agent
  - unified-experience
relevance: primary
---

# A Unified Agent Experience

Overview of how the Copilot coding agent (cloud) unifies with local VS Code agent workflows — covering handoffs, continuity, and when to use which surface.

## Key Topics Covered

- **Cloud coding agent** — When and how to use it
- **Continuity** — Handoff between local and cloud
- **Entry points** — Starting cloud sessions from issues, PRs, and VS Code

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Uh our last release uh 1.109 was full of
[0:00:04] agents. Um I can even show you here if
[0:00:07] you look at our release notes and you
[0:00:08] search for agents there's over 99 hits
[0:00:10] um on our last release notes and that's
[0:00:13] only for the last release. Uh so there's
[0:00:15] lots to talk about um and in this
[0:00:17] session in particular I am aiming to
[0:00:20] talk about uh how to collaborate with
[0:00:22] agents in VS code. So, in our agents
[0:00:25] documentation, um we have um kind of
[0:00:30] divided up agents into four categories
[0:00:32] here. Um and I'm going to kind of try
[0:00:36] and walk you through uh the use case
[0:00:38] scenarios for every uh kind of agent
[0:00:41] that we have in VS Code. Um kind of what
[0:00:43] they mean, how uh I would use them in my
[0:00:46] day-to-day work. Um, and the uh kind of
[0:00:51] the way we're going to kind of hack
[0:00:52] around with that is I have this game
[0:00:54] called Tank Game. Uh, it's a Bluetooth
[0:00:57] game. It's it is on the app store for
[0:00:59] free. And um, what you do is you can
[0:01:01] grab your closest friends around you and
[0:01:04] uh, play a little game. Um, so I I kind
[0:01:08] of like to play this on the bus or on
[0:01:10] trains or in uh, flights when I don't
[0:01:12] have an internet connection. Want to
[0:01:14] kill some time. So, uh, today what we're
[0:01:17] going to do is we're going to use agents
[0:01:18] and we're going to try and add some more
[0:01:19] features into this game. Um, so yeah,
[0:01:23] this kind of collaboration chart that we
[0:01:26] have, um, this, uh, kind of describes
[0:01:30] all of the modalities that you can um,
[0:01:33] use in VS Code and how um, an agent maps
[0:01:36] to that. So we have agents that are that
[0:01:38] are more local um that give you kind of
[0:01:40] an interactive um kind of feedback loop
[0:01:43] and then we have agents um that uh only
[0:01:47] operate in the cloud and that you can
[0:01:49] give some feedback to in certain points
[0:01:51] along its life cycle. Um and if that's
[0:01:54] confusing um we have a lot of
[0:01:56] documentation on it and I'm going to run
[0:01:57] through every single option that we have
[0:01:59] in VS Code today. Um so to start um I
[0:02:03] think the agent that everyone is most
[0:02:05] familiar with in VS Code right now is
[0:02:07] the local agent. So this is the the one
[0:02:10] um that runs on your machine. It uses
[0:02:13] our own agent harness um to um write
[0:02:18] code for you uh and also answer
[0:02:19] questions of course. Um and it's uh the
[0:02:21] experience that we've had for the
[0:02:22] longest time in VS Code. So uh to enable
[0:02:25] it you choose uh under the target picker
[0:02:28] here you choose local. Um, and uh, we
[0:02:31] have a few kind of modes here. Um, we
[0:02:34] have agent mode, um, which allows the
[0:02:37] agent to edit files in your workspace.
[0:02:38] So, I'm in my tank game workspace up
[0:02:40] here, and I'm able, uh, to edit, uh, to
[0:02:43] tell the agent to edit code and make
[0:02:44] changes on my behalf. And I'll see these
[0:02:46] happen live uh, in VS Code. We also have
[0:02:50] this mode here, which I quite like. It's
[0:02:51] called plan mode, which I'm sure has
[0:02:53] been talked about a lot today because
[0:02:54] everyone loves it. Uh, plan mode is a
[0:02:57] great way to
[0:02:59] use the agent to formulate your
[0:03:01] thoughts. Um, so I don't have a plan of
[0:03:03] what I want to build today. So I'm going
[0:03:04] to ask the agent, uh, look at my
[0:03:07] codebase and, uh, tell me some cool
[0:03:10] features to implement.
[0:03:13] Implement implement.
[0:03:16] And we're going to let that go for a
[0:03:18] moment. Um, and it's going to look
[0:03:20] through my codebase. Uh you can see here
[0:03:22] that my session is running um on the
[0:03:24] lefth hand side with this in progress.
[0:03:26] It's going to analyze. It's going to use
[0:03:28] a sub agent to kind of run through my
[0:03:30] codebase. If I want to see what the
[0:03:31] agent is doing um I can expand this and
[0:03:34] I can see that it's reading all these
[0:03:35] files. Um and kind of the cool part um
[0:03:40] in the last few releases of VS Code is
[0:03:42] in the past we only allowed you to run a
[0:03:44] single one of these local sessions on
[0:03:46] your machine. But now as you can see
[0:03:48] here we have uh we have this button new
[0:03:50] session that allows you to open a new
[0:03:52] session. Um and you can see on the lefth
[0:03:54] hand side my existing session is still
[0:03:56] running. So this is a super powerful
[0:03:58] feature that I think is a little bit
[0:04:00] hidden right now in VS Code but really
[0:04:02] allows you to take full advantage of the
[0:04:04] agent. Um and especially for plan mode
[0:04:08] um where files in your workspace aren't
[0:04:10] being touched um there's really um no
[0:04:14] risk of collision at this point. So, um
[0:04:17] you can see earlier I asked um the agent
[0:04:20] to launch my simulator for me. Um and
[0:04:24] that uh ran concurrently with my
[0:04:26] previous request as well. Um so we're
[0:04:28] going to allow it to look through. It's
[0:04:30] going to look for uh any uh notes I have
[0:04:33] in the codebase of what I had been
[0:04:35] planning to do in the past. Um
[0:04:39] and yeah, we'll let that run for a
[0:04:40] second. The other thing I want to show
[0:04:42] is that alongside local, we now have uh
[0:04:45] thirdparty integrations uh with other
[0:04:47] agents. So claude down here you can see
[0:04:51] um can be selected as well as codeex
[0:04:52] which comes through uh the codeex
[0:04:54] extension um which I might not have the
[0:04:56] latest installed but uh claude for
[0:04:59] instance uh so this is we'll use the
[0:05:01] cloud SDK um that comes from anthropic
[0:05:03] and it will give you a similar
[0:05:06] experience to cloud code. Um so you can
[0:05:08] see uh the models that are available
[0:05:10] here. Um as well as um some options of
[0:05:14] how you want the agent to behave. Do you
[0:05:15] want it to ask you before edits? Do you
[0:05:17] want it to make edits autonomously or do
[0:05:19] you want to enter its plan mode? Um so
[0:05:22] these all again run locally on your
[0:05:23] machine. If you close your laptop lid,
[0:05:25] uh these will stop running. Um but uh
[0:05:28] yeah, let's let's use this plan mode and
[0:05:30] see what it comes up with. Um suggest
[0:05:32] some cool features.
[0:05:35] So again, so this this experience here
[0:05:38] was using uh the uh the agent harness
[0:05:41] that's built by the VS Code team. Um
[0:05:42] whereas this um experience here when you
[0:05:45] select Claude is is using the agent
[0:05:47] harness built by Anthropic. Um
[0:05:50] and yeah, we'll let that uh continue.
[0:05:53] But let's see uh some of the ideas that
[0:05:55] it had. So some quick wins. Maybe this
[0:05:56] is good for a live stream. Uh fire rate
[0:05:59] limiter. Uh yeah, as you can see right
[0:06:01] now, uh you can shoot as much as you
[0:06:03] want. Um, so that sounds like kind of a
[0:06:05] nice one um to tackle. Let's uh
[0:06:10] um let's actually do it in the same
[0:06:13] thread. Um because what we can do is we
[0:06:15] can then swap to agent mode and we can
[0:06:18] say um
[0:06:20] implement uh number one and this agent
[0:06:25] will go and uh it will actually write
[0:06:27] the code for me now that we swapped to
[0:06:28] agent mode. Cool. So let's let that run
[0:06:32] for a moment. Uh the next kind of agent
[0:06:34] that I want to describe um which you've
[0:06:36] seen here in this picker uh is the cloud
[0:06:38] agent. Um and to do that I've already
[0:06:40] got one that has run in the background.
[0:06:42] The way you kind of enter cloud mode is
[0:06:45] that you click uh right here. Um and now
[0:06:48] any sessions that you create from this
[0:06:51] uh input here will run on the cloud
[0:06:53] through uh your copilot subscription. Um
[0:06:57] and it'll create a PR uh on the repo
[0:07:00] that you choose. So this is a repo
[0:07:02] that's on GitHub. Um and uh when I
[0:07:07] initiate a task here, it will run in the
[0:07:09] cloud. So I can start the session, close
[0:07:11] my laptop, uh come back later, open open
[0:07:14] my laptop and then see the changes that
[0:07:17] uh happened in the cloud. Um so one of
[0:07:19] them that I wanted to get working was I
[0:07:20] wanted to get tvOS working. Um because
[0:07:22] this app works great on iPhones and
[0:07:23] iPads, but the tvOS integration is it is
[0:07:26] not quite complete. So I asked uh cloud
[0:07:30] agent uh before I started the session uh
[0:07:33] just tell me what's needed uh to get
[0:07:36] cloud agent working. Um sorry to get
[0:07:39] tvOS working. Uh and it ran for a bit
[0:07:42] and then at the end here you see it
[0:07:43] summarized my changes. It said um was a
[0:07:46] non-functional stub which I knew. Um and
[0:07:50] it made some changes to the TVS specific
[0:07:52] game controller which seems like the
[0:07:54] correct uh change here. um and
[0:07:57] summarizes a few more changes that it
[0:07:58] made. And then right down here, you can
[0:08:00] see all of the files um that it changed.
[0:08:04] Uh so if I wanted to review this and
[0:08:07] understand what's going on, I can read
[0:08:09] uh the diff here. Um and yeah, super
[0:08:14] powerful. um the way and of course um if
[0:08:17] I wanted to just view the PR and approve
[0:08:19] it from here, I can look at it here and
[0:08:23] uh I could set it ready for review and
[0:08:25] merge it into my codebase. And the way
[0:08:26] that I have this all set up is that um
[0:08:29] when I use uh the cloud agent um it'll
[0:08:33] automatically attempt to publish uh to
[0:08:36] um my subscription uh to my uh phone, so
[0:08:42] to my iPhone. Um, and if I open up the
[0:08:44] PR, it looks like we had one error,
[0:08:47] which is a great
[0:08:49] way to Yeah. So, if I open up the PR
[0:08:52] here, we can see that on GitHub. Uh, we
[0:08:55] have the PR. This is live here. And if
[0:08:58] there was any errors with archiving, we
[0:09:01] can actually take a look at them. And
[0:09:04] yeah, I think this is not something that
[0:09:08] is the agent's fault. I think it was my
[0:09:09] fault with the build. But yeah, you can
[0:09:10] see here I can merge this in and it'll
[0:09:12] go to um my kind of test flight build
[0:09:15] moving forward. So super powerful. Um I
[0:09:18] love to use the cloud agent when I have
[0:09:21] an idea and I want something kind of
[0:09:23] prototyped, but I don't really want to
[0:09:25] be super hands-on. I want to allow the
[0:09:27] agent to come up with some ideas for me
[0:09:29] and then I'll pull down the changes. Um
[0:09:32] which you can do here with this check
[0:09:33] out button or the supply button. And uh
[0:09:35] you can kind of play with the changes
[0:09:37] more and continue in other agents or
[0:09:39] even just add a follow-up here. So um
[0:09:42] let's see make sure um Apple
[0:09:46] remotes work. Okay. So this will send a
[0:09:49] follow-up uh to the PR um and you can
[0:09:53] even just see it
[0:09:55] um that it ends up right here as a
[0:09:57] comment and uh it's already been started
[0:09:59] uh by copilot. So all this is integrated
[0:10:01] nicely within VS Code. you never need to
[0:10:03] leave it um until uh you want to
[0:10:05] actually take a look at the PR or you
[0:10:07] can stay in this experience here and do
[0:10:09] all of uh your PR management from VS
[0:10:12] Code. Cool. So that is the cloud agent.
[0:10:14] Uh so this one works um in a sense that
[0:10:18] it's not interactive um you just
[0:10:21] interact with it at the end of each uh
[0:10:23] task. Whereas when we looked back um to
[0:10:26] our suggest cool features, well, this is
[0:10:29] this one's already done, but we were
[0:10:30] able to see
[0:10:33] um all of the work that it was doing. We
[0:10:35] could have stopped and steered it at any
[0:10:37] point. Um
[0:10:39] so actually uh let's say matches the
[0:10:43] movement interval. Uh make the interval
[0:10:46] longer. So we'll just let it um kind of
[0:10:50] think about that. And then once we do
[0:10:52] that, we'll say um and then rerun
[0:10:57] the app. So I have some custom
[0:11:00] instructions um in this repo here
[0:11:04] that we'll close that for now. And then
[0:11:07] we'll open up some of my custom
[0:11:09] instructions. So this one in particular
[0:11:11] uh tells uh the agent how to launch the
[0:11:15] simulator to launch these two uh apps
[0:11:17] right here. So there's instructions on
[0:11:20] Yep. And you see it already did it. Um,
[0:11:22] this has been relaunched. And we can see
[0:11:26] right on our screen here, the app is
[0:11:28] running. Um,
[0:11:30] and uh, yeah, this guy got disconnected,
[0:11:33] but once they connect again, you can see
[0:11:35] that we're now limited um, by how much
[0:11:38] how fast we can click. So that feature
[0:11:40] worked and I didn't write any code.
[0:11:43] Awesome. So the um so I think local
[0:11:45] agent works great when you have a single
[0:11:47] task or you have tasks that are totally
[0:11:49] isolated inside of your repo. I think uh
[0:11:52] our next experience kind of really
[0:11:54] shines when you want uh to do multiple
[0:11:57] tasks on your machine at the same time
[0:11:58] and want them isolated from each other.
[0:12:00] So that experience is our background
[0:12:02] agent. So this implements the copilot
[0:12:04] CLI under the hood and it allows us to
[0:12:07] use isolated work trees. So that's a
[0:12:09] feature from git that allows um to
[0:12:13] create clones essentially of your
[0:12:15] repository uh on your machine. So every
[0:12:18] time I start the background agent, it'll
[0:12:20] create a git work tree and it will use
[0:12:23] uh that git work tree for uh the for all
[0:12:27] of the code changes that it does so that
[0:12:29] I can run three, four, five, 10 of these
[0:12:31] in the background and all of them uh
[0:12:35] don't conflict with each other. So,
[0:12:38] let's um say uh let's see what were some
[0:12:42] other cool ideas that we had
[0:12:45] in our repo. Um
[0:12:48] so, we had powerups. That's a fun one.
[0:12:51] Um so, let's say
[0:12:55] uh add powerups.
[0:12:59] And this will ask you if you already
[0:13:01] have changes in your current workspace
[0:13:03] and you want to kind of copy or move
[0:13:05] them over into your work tree. Say you
[0:13:06] started a a task then you realized you
[0:13:09] wanted to background it. Uh you could
[0:13:10] move your changes uh if you wanted to
[0:13:12] share changes between your current
[0:13:13] workspace and this work tree. You could
[0:13:15] copy them. Uh for my case um because the
[0:13:18] changes are unrelated uh that are
[0:13:19] currently in my workspace. I'm just
[0:13:21] going to skip changes here. And you can
[0:13:23] see from this message that we've created
[0:13:24] a an isolated work tree. Um, so this is
[0:13:27] the hint here that all the work that's
[0:13:29] going to be done in this session is
[0:13:32] going to be done in the background. And
[0:13:35] um, yeah, you can see how it's reading
[0:13:37] files that are outside of um, my current
[0:13:40] workspace. Um, they're actually being
[0:13:43] read from the work tree. So this will
[0:13:44] continue doing work and the nice part is
[0:13:46] that it won't uh, conflict with any of
[0:13:49] the work uh, that we are currently doing
[0:13:51] for our other features. Um, so we can
[0:13:53] have a bunch of these running. As you
[0:13:55] can see, we have now uh a cloud session
[0:13:58] running, we have a cloud session
[0:14:00] running, and we have a background
[0:14:01] session running. And all these are
[0:14:02] managed right here from the sessions
[0:14:04] panel uh which I'll probably talk about
[0:14:06] a little later. Although the cool thing
[0:14:07] here is that, you know, if you're
[0:14:09] running lots and lots of sessions, it
[0:14:11] might get a little overwhelming
[0:14:12] sometimes to organize. So, we have this
[0:14:14] nice control up at the top of the screen
[0:14:16] here. So, at the top of the screen, uh
[0:14:18] you can filter by all your unreads. So,
[0:14:20] I haven't read this yet. Um,
[0:14:22] so looks like
[0:14:25] um
[0:14:27] it created a plan. It wants me to look
[0:14:29] at the plan.
[0:14:32] That looks good. Let's let's continue.
[0:14:34] Uh, let's continue. Yeah. So, it wanted
[0:14:38] me to confirm the plan before I
[0:14:39] continued. And you can see here that uh
[0:14:41] now if I filter by in progress, I see
[0:14:43] only the sessions that are in progress.
[0:14:45] And that just toggles this filter right
[0:14:46] up here. Um, so super helpful. I really
[0:14:49] like this when I'm running 10, you know,
[0:14:51] VS Code sessions. If I'm working on VS
[0:14:53] Code, it's nice to just filter it down
[0:14:55] here and see exactly what needs my
[0:14:57] attention. Um, and if there's any
[0:14:58] unread, what's already finished, and
[0:15:00] that I can, um, either merge or review
[0:15:04] or continue, um, prompting.
[0:15:07] So, yeah, that's the three kind of main
[0:15:12] blocks. We have local, which either are
[0:15:14] local harness, and uh, cloud and codeex.
[0:15:17] We have background which is still
[0:15:19] running on your machine uh but uses the
[0:15:20] copilot CLA CLI to run these in isolated
[0:15:23] work trees and uh cloud here um which
[0:15:27] then uses um
[0:15:30] uh the cloud of course uh hosted by
[0:15:32] GitHub and I can actually show that a
[0:15:34] little more um in depth here because we
[0:15:38] have our agents view on github.com
[0:15:41] and you can see exactly how it connects
[0:15:42] here. I have lots of sessions that I've
[0:15:45] run. Um, and this tvOS one, uh, you can
[0:15:49] see is running at the top. We'll see our
[0:15:50] prompt even. Yeah, make sure Apple
[0:15:53] remotes work. Okay, you can see exactly
[0:15:55] the tool calls, uh, from here as well,
[0:15:57] all of the work that it's doing. So,
[0:15:59] this is really handy, right? You can use
[0:16:01] uh like the GitHub mobile app or just
[0:16:04] sign into github.com from a different
[0:16:05] machine, say, um, and still access and
[0:16:08] continue to steer um, the sessions that
[0:16:12] you're working on. Um, but of course my
[0:16:14] favorite spot to uh control them is uh
[0:16:16] through VS Code. And then it allows you
[0:16:18] really nicely to
[0:16:20] uh move um the code into your editor if
[0:16:24] you want to edit it yourself or if you
[0:16:25] want to understand the code better,
[0:16:26] explore it. You know, we have really
[0:16:28] powerful features inside of VS Code that
[0:16:30] allow you to explore code that is
[0:16:32] generated by agents. Um and actually one
[0:16:35] thing that's um super new actually in
[0:16:38] the last release which I really love to
[0:16:40] use now is in cloud. So I kind of
[0:16:42] glossed over these options here. Um
[0:16:45] cloud uh of course we have our co-pilot
[0:16:47] harness. So that's the co-pilot coding
[0:16:48] agent that's been in the release for a
[0:16:51] few months now or that has been in the
[0:16:53] product for a few months now. Uh we also
[0:16:55] have these two new options claude and
[0:16:56] codeex. So uh of course we're under the
[0:17:00] cloud umbrella here. So these are all
[0:17:01] running off of our machine. Um but as
[0:17:04] was announced I think at GitHub Universe
[0:17:06] um last year um there are partner agents
[0:17:10] um from Anthropic and OpenAI that allow
[0:17:12] you to use uh their coding harnesses um
[0:17:16] but in the cloud. So you can see here
[0:17:20] that I can choose cloud or codeex as
[0:17:22] well. And now when I start my cloud
[0:17:25] sessions, let's actually get another
[0:17:27] good idea from the app here or from the
[0:17:29] session. a projectile on projectile
[0:17:32] collision. That sounds kind of fun. So,
[0:17:34] let's do that. Um,
[0:17:38] when I send this uh request now and I
[0:17:42] choose to delegate, um, you'll see that
[0:17:46] you'll get information on it's starting
[0:17:47] to delegate. It's then creating the pull
[0:17:49] request in the background for you. And
[0:17:52] once it creates the pull request, it
[0:17:54] will fetch those details and swap your
[0:17:56] session over to here. And now you can
[0:17:58] see uh that if we open the pull request,
[0:18:02] it is not run by copilot anymore, but
[0:18:04] it's actually run by anthropic. Um so
[0:18:08] this is quite a similar experience. It's
[0:18:10] all quite integrated in VS Code and in
[0:18:11] github.com. Um but the difference is um
[0:18:15] it is now using uh a like an agent
[0:18:19] harness that's built uh directly by
[0:18:21] anthropic instead of uh by a third
[0:18:24] party. So this is really handy if you
[0:18:27] want to evaluate um how how different
[0:18:30] agent harnesses work. I think that's the
[0:18:33] biggest value here is maybe some agent
[0:18:34] harnesses are good at some problems and
[0:18:36] some are good at others. And I think the
[0:18:38] beautiful part about VS Code is that we
[0:18:40] have access to all sorts of you know
[0:18:42] cutting edge technologies. Um so you can
[0:18:45] use anthropics tooling and what they
[0:18:48] believe is the best path forward. You
[0:18:50] can use open AIS you can use our
[0:18:52] co-pilot harnesses. Um, and you can
[0:18:54] really get the best of all that's
[0:18:56] available to you right now, uh, in the
[0:18:57] world of AI. So, we'll let this run. Uh,
[0:19:00] you can check up on, um, the repo later
[0:19:04] on and see, uh, exactly what these, um,
[0:19:09] what these projects uh, or how these
[0:19:12] tasks get resolved. Um, but yeah, super
[0:19:16] handy. I've been enjoying uh, the cloud
[0:19:18] agent a lot. Um, and you can see there's
[0:19:20] a lot of pull requests on this repo
[0:19:21] already uh that are utilizing um the
[0:19:24] cloud cloud agent.
[0:19:27] Let's see. So, let's go back here. Okay,
[0:19:29] we have a u message here. And you can
[0:19:32] see all this is nicely kind of
[0:19:33] communicated through the top uh agent
[0:19:36] sessions bar here. So, I saw that there
[0:19:38] was um an approval needed. Um so,
[0:19:40] because this is writing um to a uh
[0:19:44] particular path, it wanted me to approve
[0:19:46] it. And let's see. what this is doing.
[0:19:50] Uh yeah, this
[0:19:53] this is
[0:19:56] adding some files. Okay, so this looks
[0:19:58] good. So we'll let that continue on. And
[0:20:00] you can see uh the confirmation is left.
[0:20:03] Uh we can filter here and see all of the
[0:20:04] work that's being done. All of these are
[0:20:06] happening in parallel and they're all
[0:20:08] happening isolated from each other. Um
[0:20:10] which is super powerful. allows me to
[0:20:13] know that I uh all of these changes will
[0:20:16] not conflict with each other, which I
[0:20:17] think is the kind of really the goal
[0:20:19] that we had uh last month with the
[0:20:21] release is allowing both you as a
[0:20:24] developer to have an option of what
[0:20:26] tools you use as well as giving you the
[0:20:28] ability to run multiple agents at once.
[0:20:31] And that's exactly where this kind of UI
[0:20:34] shines here where um you can see all of
[0:20:38] your sessions on the lefth hand side,
[0:20:40] all of uh the action on the right hand
[0:20:42] side and it's very easy with one click
[0:20:44] to then open up this panel here and
[0:20:46] actually view the changes and understand
[0:20:48] them as the developer. Um yeah, the one
[0:20:51] last thing that I'll show is that um we
[0:20:54] have one more experience. You can see we
[0:20:56] have some notifications here um which
[0:20:58] I'll close for the moment. We have one
[0:21:02] final experience which allows you to
[0:21:05] um continue on. Um so of course we have
[0:21:09] I've shown you today um from the new
[0:21:11] session um how to create a new session
[0:21:14] from cloud from local from background.
[0:21:16] Um but if you start a session in local
[0:21:19] and then want to move it either to the
[0:21:20] background or to cloud we have this
[0:21:22] experience here called agent handoff and
[0:21:24] there's a nice uh link to documentation
[0:21:26] down here um that allows you to read
[0:21:28] more about that. Um, but this allows you
[0:21:31] to start a conversation maybe in plan
[0:21:33] mode in VS Code. Um, so I think we
[0:21:35] started this one in plan mode. Um, and
[0:21:38] then we got some ideas and then I could
[0:21:40] say uh continue um implementing the high
[0:21:45] value uh ideas and I I could continue in
[0:21:49] either background or cloud here. Um, so
[0:21:52] super powerful. Allows me um to really
[0:21:57] use all of the tooling in any way that I
[0:21:58] want. Um, which is I think the most
[0:22:01] important part about uh developer tools
[0:22:04] is allowing you to use it however you
[0:22:06] think will make you most productive.
[0:22:08] Cool. Well, I hope this was all helpful
[0:22:09] today. Um, again, I am Josh and uh yeah,
[0:22:13] hope to see you again soon. Thanks.
