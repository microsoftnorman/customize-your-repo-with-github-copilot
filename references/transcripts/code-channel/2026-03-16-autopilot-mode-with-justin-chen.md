---
video_id: ne9l0S-JNE8
title: "Autopilot Mode with Justin Chen"
url: https://www.youtube.com/watch?v=ne9l0S-JNE8
channel: "@code (Visual Studio Code)"
published: 2026-03-16
speakers:
  - Justin Chen
  - James Montemagno
topics:
  - autopilot
  - permissions
  - workflows
  - chat-ui
relevance: primary
---

# Autopilot Mode with Justin Chen

Justin and James deep-dive into Autopilot and the evolving VS Code chat UX—why shimmers and collapsed containers declutter conversations, and why the input bar split and new permissions picker matter. Learn how Autopilot (Insiders preview) can auto-approve tools, answer prompts, iterate until a task_complete signal or max retries, and when to use default vs bypass approvals; practical tips for safe, hands-off workflows and feedback.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Intro and Banter |
| 03:30 | Chat UI: Shimmers and Collapsing |
| 10:00 | Input Toolbar Changes |
| 15:30 | Permissions Picker Overview |
| 21:00 | Autopilot Mode Deep Dive |
| 25:30 | Plan Mode, Workflows, and Dogfooding |

## Key Topics Covered

- **Autopilot**
- **Permissions**
- **Workflows**
- **Chat Ui**

## Links

- https://code.visualstudio.com/updates/v1_110
- https://podcasts.apple.com/us/podcast/id1833924784
- https://open.spotify.com/show/3S2fExHkmbfQwwYw4a56yQ
- https://music.amazon.com/podcasts/bd5f1efc-cdae-49c8-8ec7-c9b48b00ce46/vs-code-insiders-podcast
- https://castbox.fm/channel/id6720052?country=us
- https://overcast.fm/itunes1833924784/vs-code-insiders-podcast
- https://pca.st/itunes/1833924784
- https://www.vscodepodcast.com/subscribe
- https://x.com/code
- https://bsky.app/profile/vscode.dev
- https://aka.ms/VSCode/LinkedIn
- https://github.com/microsoft/vscode

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Welcome back everyone to the VS Code
[0:00:02] Insiders podcast. The behind thescenes
[0:00:05] look at your favorite code editor, VS
[0:00:07] Code. I'm James Monttoagno, your host.
[0:00:09] And with me, the one, the only software
[0:00:11] engineer on the VS Code team. Well,
[0:00:12] there's more than one. Justin Chen is
[0:00:14] here. How's it going, Justin?
[0:00:15] >> Good. How's it going? I think I'm pretty
[0:00:18] excited to talk about autopilot today.
[0:00:21] >> Yeah, I'm super stoked. You and I were
[0:00:23] planning on starting to record this
[0:00:26] podcast about 20 minutes ago, but then
[0:00:28] we just geeked out on Pokemon and and
[0:00:30] the Nintendo Museum and Potopio and
[0:00:33] everything like that. So those
[0:00:37] >> and people may notice that you're a
[0:00:39] little bit of a Pokemon fan. Just a
[0:00:40] little bit.
[0:00:40] >> Just a little. Just a little. I don't
[0:00:42] know if you can tell. And also the giant
[0:00:44] VS Code sign in the background as well.
[0:00:47] >> The two of them together is beautiful. I
[0:00:50] love it. Um, I I myself also a huge
[0:00:52] Pokemon fan. So, I'm excited to to geek
[0:00:54] out and and play some Poctopia together.
[0:00:56] So, um, today is going to be a little
[0:00:59] bit special because there's been
[0:01:01] honestly like a crazy amount of amazing
[0:01:04] new features inside of VS Code and we
[0:01:05] try to like talk about some of the
[0:01:07] deeper things inside of here. And I
[0:01:09] think what's been really fascinating,
[0:01:11] Justin, is kind of how the chat has
[0:01:14] evolved quite a bit and how developers
[0:01:18] are focusing on interacting, working
[0:01:21] with tools, and now there's so many
[0:01:23] tools, skills, agents, MCPs, like
[0:01:25] actual, you know, tool, normal tool
[0:01:27] calling, things like that. Like what's
[0:01:29] your day-to-day in this space and what's
[0:01:31] your main area that you're focused on on
[0:01:33] the VS Code team?
[0:01:34] >> Yeah. Yeah. The main thing I've been
[0:01:36] working on recently is just the general
[0:01:38] chat UI and UX um and just general chat
[0:01:42] experience because I think there's a lot
[0:01:45] that goes into like what you see when
[0:01:48] the chat is like rendering or a lot of
[0:01:50] like tools that you can utilize um to to
[0:01:53] properly I guess
[0:01:56] I guess use the agent to the better the
[0:01:58] best the best extent as possible. Um,
[0:02:02] yeah, I work mostly on UI, rendering,
[0:02:05] um, a couple of the UX features with the
[0:02:07] input box, um, editing previous
[0:02:09] requests, checkpoints, just a little bit
[0:02:11] of everything. Um, to kind of make your
[0:02:13] experience in chat in the chat panel a
[0:02:16] little bit better.
[0:02:17] >> I really feel like for me, as I use the
[0:02:19] chat, as the team's been evolving these
[0:02:21] features, everything you just mentioned,
[0:02:23] like I use I use like steering, I go
[0:02:24] back, I edit previous requests, like I'm
[0:02:26] looking at the output, like the
[0:02:28] streaming input that's coming in. I've
[0:02:29] noticed a few things before we get to
[0:02:31] autopilot is like it feels as though and
[0:02:34] maybe you can distill this out since
[0:02:36] you're in this area. It feels like the
[0:02:37] chat is less chatty recently. You know
[0:02:40] what I mean? Like like it's a lot more
[0:02:41] like a lot more like uh shimmers. You
[0:02:44] know what I mean? Like what is
[0:02:45] happening? What is evolving in that
[0:02:46] space?
[0:02:47] >> Yeah. I think it it's partially maybe
[0:02:49] some of the quirks of the models, but I
[0:02:51] think one thing that we've been working
[0:02:52] on is just kind of making
[0:02:55] making that chat not so annoying, I
[0:02:58] guess, and making it a little bit more
[0:02:59] consistent as you go through and look at
[0:03:01] it. So, for example, the shimmers,
[0:03:02] right? A lot of the thinking, a lot of
[0:03:04] the reasoning text, a lot of the tool
[0:03:06] calls, um, a lot of these things are
[0:03:08] getting collapsed into containers now
[0:03:09] and they'll just collapse away once
[0:03:11] you're done. So, as you kind of scroll
[0:03:12] through your chat, you you might notice
[0:03:13] that there are a lot of these like drop
[0:03:15] downs that contain a lot of information
[0:03:17] inside, but maybe it's something that as
[0:03:19] a user you don't actually need to care
[0:03:21] about.
[0:03:23] >> That's cool. Yeah, I I've been I'm a big
[0:03:25] and Pierce knows this. I'm a big like
[0:03:26] reader of the chat. I love to understand
[0:03:28] like what the agents are doing. I almost
[0:03:31] need a slow mode, you know, like on
[0:03:32] YouTube you can do like slow mode if
[0:03:33] there like can I get a slow No one would
[0:03:35] use it besides me, so don't add it for
[0:03:37] me. Maybe I'll add an extension. But I
[0:03:39] have noticed that like how is like the
[0:03:41] reception of that been? Have you seen
[0:03:43] like good feedback as far as like
[0:03:44] minimizing the chat or even as you're
[0:03:45] using it every single day?
[0:03:47] >> I think it's been pretty good. Um I
[0:03:49] think it feels pretty good for it to be
[0:03:50] consistent. I think something that we
[0:03:52] had a couple months ago was that we had
[0:03:54] check marks all over the place. I think
[0:03:56] some of our tool calls would show up on
[0:03:57] the surface when like maybe it's a
[0:04:00] little bit annoying to see 10 read tool
[0:04:02] calls back to back to back to back,
[0:04:03] right? And I think just collapsing some
[0:04:05] of this stuff away, making it a little
[0:04:06] bit more minimal, making it more
[0:04:07] consistent, removing the check marks,
[0:04:09] adding stuff like um the collapsed
[0:04:12] thinking mode where it just shows one
[0:04:14] tool call or the current tool call
[0:04:15] happening at the time. Um I think the
[0:04:17] reception has been pretty good and it
[0:04:18] makes the chat feel kind of alive still
[0:04:21] with the with showing work progress, but
[0:04:23] also a little bit more minimal.
[0:04:25] >> That's cool. And I also noticed Pier
[0:04:27] showed off that you can customize the
[0:04:28] text of the shimmers of like what it's
[0:04:30] doing too.
[0:04:32] >> Yes. Yes. Um, I've been a pretty big fan
[0:04:34] of that. I I wanted to see the texts
[0:04:37] bribing the hamster in in chats. Like,
[0:04:41] my internet's not going fast enough, so
[0:04:43] I got to feed the hamster more.
[0:04:44] >> There you go. And now you can. So, I
[0:04:46] love it. Um, I've also noticed like that
[0:04:48] clarity has been helpful because
[0:04:50] sometimes when there's so much happening
[0:04:51] and scrolling in the chat, you you know,
[0:04:54] I can read like those those things the
[0:04:56] thinking and the reasoning, but like
[0:04:57] sometimes I'm like, "Oh, did it actually
[0:04:59] like execute my skill?" And like now
[0:05:00] it's actually pretty clear because those
[0:05:03] things are autoclaps. I'm like I can I
[0:05:05] can actually see like the action it's
[0:05:07] taking and not necessarily having to
[0:05:09] read every single thing. So it feels
[0:05:10] like those actions are much more
[0:05:11] important.
[0:05:12] >> Yeah. Yeah. It it'll always clap down
[0:05:14] and summarize. It's an LLM gener
[0:05:16] generated title regardless. So sometimes
[0:05:18] it's not 100% accurate of what it
[0:05:20] actually did or like maybe it's trying
[0:05:22] to summarize a lot of stuff at the same
[0:05:23] time. But normally it'll let's say you
[0:05:25] had like four reads and it like read a
[0:05:27] skill. will try to say something like
[0:05:28] reviewed and like updated this and this.
[0:05:32] >> So help out with just kind of skimming
[0:05:34] through the chat and seeing what it
[0:05:36] tried to do.
[0:05:37] >> Now it seems like that chat bottom
[0:05:39] window is ever evolving. Like it is
[0:05:41] always changing. Especially if you're on
[0:05:42] insiders, you're rocking insiders. Every
[0:05:44] day it's different. I'm pretty sure that
[0:05:46] between local background CLI cloud that
[0:05:50] background copilot CLI CLI work tree has
[0:05:53] changed the verbiage like a hundred
[0:05:55] times which I love by the way but
[0:05:58] there's a bunch of new things can you
[0:06:00] walk through at least when we're
[0:06:02] recording this in the year of of March
[0:06:05] 12th 2026 like what has changed in the
[0:06:08] bottom input windows like for developers
[0:06:10] to kind of know about um in both stable
[0:06:13] and obviously in insiders and like why
[0:06:15] is that evolving and uh what should they
[0:06:18] know be before we go to the brand brand
[0:06:20] new hotness?
[0:06:22] >> Yeah. Yeah. I think the main thing is
[0:06:23] that we've split the toolbar that used
[0:06:27] to be in the input box into two
[0:06:29] different toolbars now. And the reason
[0:06:31] we wanted to do this is because there
[0:06:32] are some things that are more applicable
[0:06:34] towards the session and then some things
[0:06:36] that are more applicable towards the
[0:06:37] request. So that's the main like
[0:06:40] differentiation between the two
[0:06:41] toolbars. Um, I think the permissions
[0:06:44] toolbar, the permissions picker is the
[0:06:47] main thing that's new and adding this
[0:06:49] additional thing just would have made
[0:06:50] that input bar too large anyway. So,
[0:06:52] from a UX perspective, it made sense to
[0:06:54] split it out, but also kind of gives you
[0:06:56] a good mental image of what's actually
[0:06:58] happening in the session because the
[0:07:00] things at the bottom include the um like
[0:07:03] the the agent harness. So, it'll be
[0:07:04] either like local, copilot, um, CLI,
[0:07:07] cloud, or cloud. Um, and then the other
[0:07:10] one in there is the permissions picker,
[0:07:12] which I just talked about. So, that's
[0:07:13] the main new thing we have now.
[0:07:16] >> No, it makes a lot of sense. I like
[0:07:17] actually that didn't make sense to me
[0:07:21] why I moved until you just said it,
[0:07:22] which is like the reason because actual
[0:07:24] the context of those different um those
[0:07:27] different fields are important, right?
[0:07:29] Because you're when you're inside of a
[0:07:30] local session, you are adding context,
[0:07:32] you are picking the agent, you are
[0:07:33] picking the model, you are calling the
[0:07:34] tools, but it's always a local session
[0:07:36] once you pick that, right? uh in general
[0:07:39] u for that whole state. Well, let's talk
[0:07:40] about that permission picker because uh
[0:07:42] it's going to be brand new because
[0:07:44] everything else has been there kind of
[0:07:45] and it's evolved and changed around a
[0:07:47] little bit but it's brand new um and if
[0:07:50] people have used like the copilot CLI
[0:07:51] some of these things uh may be uh new to
[0:07:54] them but also some of these features
[0:07:55] have been in the product but now exposed
[0:07:57] in the UI a little bit more. So when
[0:08:00] people go into VS Code on the bottom of
[0:08:02] the chat window they're going to see
[0:08:03] that local background you know CLIcloud
[0:08:07] you know agent where it's running but
[0:08:10] they're going to see this permissions.
[0:08:11] What is this permissions? What's in it
[0:08:14] and what should people care about it
[0:08:17] right now today?
[0:08:19] >> Yeah. So I want to talk briefly about
[0:08:22] like the main reason we wanted to expose
[0:08:23] it. I think people just didn't really
[0:08:25] know that we had global autoproof,
[0:08:27] right? It's it's something that if you
[0:08:28] go into your settings right now and you
[0:08:30] search YOLO mode or YOLO, it does show
[0:08:32] up. How many people are actually
[0:08:33] clicking this? I'm not entirely sure,
[0:08:35] but I I would constantly get questions
[0:08:37] like, "Oh, do you guys actually have
[0:08:38] yellow mode?" Yes, we do. And this is
[0:08:39] just a way to surface it. Um, and just
[0:08:42] to try to solve that friction between
[0:08:44] approvals, like having to constantly say
[0:08:45] allow, allow, allow. And the the three
[0:08:48] things that we currently have in the
[0:08:50] permissions picker are the one that you
[0:08:52] might see on startup, it's called
[0:08:53] default approvals. We have something
[0:08:55] called bypass approvals. And the last
[0:08:57] one is enabled currently by default only
[0:08:59] in STA in insiders and will be slowly
[0:09:02] rolled out in stable as we continue to
[0:09:04] run evaluations on it as well as do some
[0:09:08] evaluation on like how cost is going to
[0:09:11] work. Um and the third one is autopilot.
[0:09:14] So I can briefly talk about what those
[0:09:17] three different things mean. Um I guess
[0:09:19] first one with default approvals, it's
[0:09:22] basically as if nothing changed, right?
[0:09:24] It's going to use your default settings,
[0:09:26] it's going to use your configured
[0:09:27] settings. I believe the the description
[0:09:29] there says like copilot will use your
[0:09:30] configured settings. Um, and what that
[0:09:33] really means behind the scenes is if you
[0:09:35] haven't changed anything in in the user
[0:09:36] settings, if you haven't changed
[0:09:38] anything in like the workspace settings
[0:09:39] or enterprise hasn't set anything, it
[0:09:42] will prompt you to allow certain tools
[0:09:45] to happen as you're going through the
[0:09:47] chat. Um, but it will also
[0:09:50] take a look at what settings you have
[0:09:52] set, including any of the edit auto
[0:09:54] approved settings, which are I think
[0:09:55] they're like pattern based rules for
[0:09:57] file edits. So certain files will get
[0:09:59] edited, certain files won't. It'll take
[0:10:00] a look at terminal auto approved
[0:10:02] settings like um I believe with terminal
[0:10:04] auto approve, we have like safe commands
[0:10:07] like cd or like cats or um grap. I think
[0:10:10] these are some some terminal tools that
[0:10:12] are automatically approved but some of
[0:10:14] them are not like RM or curl or um eval
[0:10:17] etc etc. So um these terminal tools will
[0:10:21] get prompt you you will get prompted to
[0:10:22] allow them in the session based on that
[0:10:25] setting and then the last one is with
[0:10:26] URLs um with like fetches like it'll
[0:10:30] it'll double check do you want to fetch
[0:10:31] from this URL specifically. So these
[0:10:33] settings are just all settings that you
[0:10:35] can find in the in the settings UI if
[0:10:37] you just search auto approve I believe.
[0:10:39] Um but yeah, any setting related to auto
[0:10:41] approve will be um followed in this
[0:10:44] default approvals mode. Um and it it's
[0:10:48] already once again I already mentioned
[0:10:49] it's already pretty good. Um you can
[0:10:52] configure it to be very specific in this
[0:10:54] mode. But then that brings us to the
[0:10:56] question of what if I really just don't
[0:10:58] want to deal with approvals at all.
[0:11:02] Right? And that's where bypass approvals
[0:11:03] come in. Um I think the description in
[0:11:06] bypass approval says um allow all tools
[0:11:10] are auto approved um something like that
[0:11:12] and basically what it means is that we
[0:11:15] are automatically approving
[0:11:18] most tools. The only tools that actually
[0:11:20] won't be approved are stuff like ask
[0:11:23] questions or anything that requires
[0:11:25] explicit user um input. So, for example,
[0:11:27] the ask questions tool as well as any
[0:11:29] terminal commands that might require you
[0:11:32] to type like yes or no or terminal
[0:11:33] commands that require user input. So,
[0:11:35] those are the two things that um will
[0:11:38] will stop um and not be auto approved,
[0:11:40] but pretty much everything else will
[0:11:41] automatically be approved. And this is
[0:11:43] just an enhancement on the existing
[0:11:46] global auto approved setting. Um
[0:11:49] it it's we're kind of in a weird state
[0:11:51] right now where we have this permission
[0:11:53] picker and still the setting. But the
[0:11:54] idea is that when you have it set in the
[0:11:56] permissions picker, it applies to that
[0:11:58] request on that session and it ignores
[0:12:00] any existing settings you might have
[0:12:02] set. So anything that you set with all
[0:12:05] those auto approved settings that I just
[0:12:07] mentioned will get completely ignored if
[0:12:09] you have bypass approvals on. It will
[0:12:10] just automatically
[0:12:12] continue on on to calls. It'll auto
[0:12:15] retry on errors. That's that was like a
[0:12:16] big one as well. And then it will um
[0:12:20] still prompt you for certain things that
[0:12:22] require user input.
[0:12:23] >> Um and I super
[0:12:25] >> Yeah, and that's super nice too,
[0:12:27] especially if you're working like inside
[0:12:28] of a sandbox or like a code space. Like
[0:12:30] I was working on I did a pull request
[0:12:33] for I did a pull request, Justin. I
[0:12:35] don't know if you want to approve it,
[0:12:36] but I did a pull request to the VS Code
[0:12:38] uh repo and you know in the chat there's
[0:12:41] a gear
[0:12:43] >> and right now it's a huge drop down list
[0:12:45] of a bunch of stuff. What I really
[0:12:46] wanted to do is bring up the new um
[0:12:49] customization UI.
[0:12:51] >> Right. Right.
[0:12:52] >> So I did a pull request and I was like I
[0:12:55] don't know anything about the VS Code
[0:12:56] codebase. Don't really care about it uh
[0:12:58] as far as like learning where every
[0:13:00] single thing is. But I wrote a big plan
[0:13:02] and I was like hey let's plan this out.
[0:13:04] And I was like, "Cool, do a bunch of
[0:13:06] stuff." And then just like keep going,
[0:13:08] right? Just keep going, keep doing
[0:13:09] stuff, figuring it all out, write the
[0:13:11] tests, validate the stuff. And that was
[0:13:13] nice because it wasn't necessarily like
[0:13:14] doing a lot of what you're saying of
[0:13:16] like having to run tons of terminal
[0:13:17] commands or running a bunch of web
[0:13:19] stuff, but it was like running tests. It
[0:13:21] was checking the output where I would
[0:13:23] have to be validating every single time.
[0:13:24] But I was in a code space. So I was like
[0:13:26] in a in a just a cloud environment where
[0:13:28] I was in a safe environment. And that
[0:13:30] was super nice. um just in general or
[0:13:33] you know or for example you know I guess
[0:13:35] with bypass tools you can still limit
[0:13:37] the tools that it has right so if you're
[0:13:39] just working with MCPS and you're like I
[0:13:40] only want able to do these things it can
[0:13:42] only follow those tools which is kind of
[0:13:43] nice too
[0:13:44] >> exactly yeah
[0:13:46] >> yeah um and I guess to kind of roll on
[0:13:49] to the third picker that we have now and
[0:13:52] that's the cool shiny new thing that
[0:13:55] we've been working on so this was
[0:13:56] actually inspired by copilot CLI so
[0:13:59] autopilot is actually a mode that
[0:14:00] copilot CLI
[0:14:01] already has existing and it was
[0:14:04] something I wanted to bring over to VS
[0:14:05] Code because I think the application
[0:14:07] it's pretty much the same whether you're
[0:14:09] in local chat or using the copil CLI in
[0:14:11] VS Code. Um I think generally if you're
[0:14:16] if you trust the agent if you're in a
[0:14:18] safe environment I think it's a great
[0:14:21] tool to just create a great plan and
[0:14:23] then let it run let it run its course
[0:14:24] and you can kind of like shift tasks and
[0:14:26] do a couple different things. But yeah,
[0:14:28] the idea behind it um it's currently
[0:14:30] still in preview um as I mentioned at
[0:14:32] the beginning insiders only at this
[0:14:34] point in time. You can enable it with
[0:14:36] the chat.pilot
[0:14:39] setting in stable but it won't be
[0:14:41] defaulted to true there. Um and the
[0:14:44] premise of autopilot is that it has
[0:14:46] everything that bypass approvals has and
[0:14:47] a little bit more. The idea is that it
[0:14:50] will try to iterate autonomously until
[0:14:52] it's until it thinks that it's done with
[0:14:54] the task and the inspiration as I
[0:14:59] mentioned CLI. I think um cloud code
[0:15:01] also has something similar called like a
[0:15:02] rough loop. Um but it will actually do a
[0:15:06] couple additional things like auto
[0:15:07] replying to questions. So if the ask
[0:15:09] questions tool gets run, it'll auto
[0:15:11] reply to those questions. Um if it's a
[0:15:14] user input required anything whether
[0:15:16] it's the terminal or with um the ask
[0:15:19] question tool that requires user like to
[0:15:20] type an answer in a free form box or
[0:15:23] something like that it'll respond by
[0:15:24] saying that the user isn't there to act
[0:15:26] on its visibility. And then lastly it
[0:15:29] will retry and like kind of try and
[0:15:33] continue depending on the state of where
[0:15:37] it thinks it currently is. We have this
[0:15:39] thing called the task complete tool
[0:15:41] which is just saying hey don't call this
[0:15:43] tool unless the task is actually
[0:15:44] complete and obviously it's a I dumbed
[0:15:46] it down a little bit but the idea is
[0:15:48] that we check to see if that task
[0:15:49] complete tool was ever called otherwise
[0:15:52] we just continue to let it iterate let
[0:15:53] it iterate it we we do have a max
[0:15:55] continuations um I believe right now we
[0:15:58] say like max reiterate like five times
[0:16:01] um the idea is to make this configurable
[0:16:02] down the line but at the moment we're
[0:16:04] just kind of hard coding it at that
[0:16:06] point Um, yeah. I mean, it's just a cool
[0:16:10] thing to set off on its own. I don't
[0:16:12] want you I don't want the agent to ask
[0:16:13] me anything. I don't want the agent to
[0:16:16] to have to require any user input. I'll
[0:16:19] just let it run its course, finish the
[0:16:21] job, and yeah, I think it's just pretty
[0:16:24] cool to to not have to look at the agent
[0:16:26] turn by turn and be like, oh, I have to
[0:16:27] approve all this and and now I just let
[0:16:29] it run its course.
[0:16:30] >> So, you said it is different. So the is
[0:16:33] the thinking then different between
[0:16:35] bypass like bypass and default basically
[0:16:37] runs the same system prompt but you're
[0:16:39] saying autopilot has some extra juice to
[0:16:42] it basically and if I'm understanding it
[0:16:45] correct like is that extra juice in the
[0:16:47] way that it's thinking in the way that
[0:16:49] it's looking at the task list like is it
[0:16:53] validating its work is it is it
[0:16:55] implementing something and then
[0:16:56] revalidating it and then like like is it
[0:16:59] like code reviewing it like is is that
[0:17:01] the type of loop loop that it's doing
[0:17:03] until it's done.
[0:17:05] >> Yeah. So, unfortunately at the moment
[0:17:07] it's not that smart. I think we we're
[0:17:08] doing some eval. We're trying to see
[0:17:10] where we can improve it like stuff of
[0:17:11] like code review or stuff of like
[0:17:13] forcing iterations. But right now,
[0:17:15] realistically, we just have a slightly
[0:17:17] modified system prompt letting it know
[0:17:19] that it's an autopilot, letting it know
[0:17:21] that the user is not going to be there
[0:17:23] to answer any questions or to to to
[0:17:26] like yeah, basically answer any
[0:17:28] questions or answer any like user
[0:17:30] required inputs that we might show. Um,
[0:17:32] but the main thing is just with like
[0:17:33] this task complete tool. The idea is
[0:17:35] that the task complete tool will just be
[0:17:37] the the source of like ground truth
[0:17:39] where yes, you called it, we know we're
[0:17:42] done. We haven't called it. Let's try to
[0:17:43] continue until we actually are finished.
[0:17:46] Um, and I see a lot of times in like my
[0:17:50] own testing that um sometimes it'll
[0:17:52] it'll work its way down and then it'll
[0:17:54] finish, but then you'll notice that the
[0:17:56] task isn't complete and it'll be like,
[0:17:58] "Oh, let me try again." And then maybe
[0:18:00] in that try again, it'll actually try to
[0:18:01] run some tests or it'll try to do some
[0:18:03] more reads or read some calls. There are
[0:18:06] a couple cases where it doesn't need to
[0:18:08] do anything else and it'll just return
[0:18:09] like, oh, hey, I'm actually done and
[0:18:11] then it'll actually finish.
[0:18:13] >> Got it. I see. And then there's some
[0:18:15] models that what I've noticed too, maybe
[0:18:17] this is where this autopilot comes in.
[0:18:19] Some models like to do like one or two
[0:18:22] things and then stop and be like hey you
[0:18:23] want to check out this work and then
[0:18:25] just say like continue or like do do you
[0:18:27] want me to validate it right like and
[0:18:29] the answer is like probably like yeah
[0:18:30] run the build. So in this case you're
[0:18:33] saying it'll just continuously go
[0:18:35] through that list it's not going to stop
[0:18:37] basically it's just going to keep going.
[0:18:38] >> Exactly. Yeah. Um we have um some like I
[0:18:42] mean we're all open source so you can
[0:18:44] actually go and look at what part Task
[0:18:46] Complete tool says. I think it says
[0:18:47] something along like I mean I have it
[0:18:48] pulled up here but says something along
[0:18:50] the lines of like yeah signal when the
[0:18:52] task is completely done. Um like don't
[0:18:55] like provide a summary when you're
[0:18:56] finished like you must call this tool
[0:18:58] only when task is complete. Verify that
[0:19:01] your changes work like double check that
[0:19:03] there aren't any like remaining to-dos.
[0:19:05] And then on the case of continuation, we
[0:19:07] mention oh like um because you haven't
[0:19:10] called this tool yet, make sure that you
[0:19:13] verify that the tool is complete or that
[0:19:15] the the task has been complete using
[0:19:17] this tool and then it'll continue to
[0:19:19] iterate and then it'll actually mark a
[0:19:20] test on.
[0:19:21] >> So yeah, cool.
[0:19:22] >> Yeah, still playing around with it and
[0:19:24] and and like once again trying to do
[0:19:26] some eval on it, doing some a lot of
[0:19:28] self-hosting on it. Um, but generally I
[0:19:31] think it's it's a great tool regardless
[0:19:33] because it still does all the bypass
[0:19:36] approval stuff and you can be a lot more
[0:19:37] handsoff um instead of just like
[0:19:40] disabling the ask questions tool or
[0:19:42] something.
[0:19:43] >> That makes sense. I've also noticed that
[0:19:45] uh there's integration with plan mode as
[0:19:47] well with autopilot. Like I've noticed I
[0:19:50] don't know if it happens every time or
[0:19:51] not but on occasion I see like run with
[0:19:54] autopilot like how is that integration
[0:19:57] working?
[0:19:58] >> Yeah. Yeah. So if so there are two ways
[0:20:00] that uh there are two kind of entry
[0:20:02] points. So the first one is if you start
[0:20:06] plan mode in autopilot it will well plan
[0:20:10] mode normally doesn't really like ask
[0:20:12] for approvals except for like with ask
[0:20:14] questions tool. But if you start the
[0:20:16] plan mode with autopilot it'll go
[0:20:18] through it'll know that it's in
[0:20:19] autopilot. It'll answer the questions
[0:20:21] automatically and then once it's done
[0:20:24] planning it will automatically hand off
[0:20:26] to the agent. So it'll go plan in
[0:20:28] autopilot and then immediately start
[0:20:30] implementation. The alternative is if
[0:20:33] you start it in regular like approvals,
[0:20:37] it will still end at the end of the when
[0:20:40] it when it's done planning, but then
[0:20:41] there will be that handoff option to
[0:20:43] start in autopilot in which you click on
[0:20:45] it and then it'll turn that session into
[0:20:46] autopilot.
[0:20:48] >> So you said you've been dog fooding and
[0:20:50] doing some internal stuff. How are you
[0:20:52] using autopilot and how are you seeing
[0:20:54] it? like when are you making the
[0:20:55] distinction of the different modes
[0:20:57] personally?
[0:20:58] >> Yeah. Yeah. Um, honestly, it's been like
[0:21:02] 99% autopilot. I guess part of it is the
[0:21:05] dog fooding and then part of it is like
[0:21:07] in terms of like what I'm trying to get
[0:21:10] done. It's just more convenient if I
[0:21:12] just never have to take a look at maybe
[0:21:13] I'm just taking a look at what happens
[0:21:15] at the end, reviewing the code at the
[0:21:16] end. Um
[0:21:19] there there are very there are certain
[0:21:21] applications where it's like maybe it's
[0:21:22] better to use bypass approvals instead
[0:21:24] of autopilot. But yeah, personally for
[0:21:25] me like if I'm just setting off like
[0:21:27] three or four different like sessions to
[0:21:30] take a look at like a bug here or a bug
[0:21:32] there. Um just having it run in
[0:21:34] autopilot where it'll automatically
[0:21:36] verify either either like I attach a
[0:21:38] link to a GitHub um PR or a link to a
[0:21:40] GitHub issue and I'm like oh it'll
[0:21:42] automatically fetch it. It'll
[0:21:43] automatically do any like it'll
[0:21:46] automatically do any like terminal tool
[0:21:47] calls for me. It'll automatically create
[0:21:48] work trees for me, stuff like that. It's
[0:21:50] just way way easier for me to just go
[0:21:52] through and then go through the
[0:21:54] different work trees. Um, and they're
[0:21:55] all in autopilot. So, I just look at the
[0:21:57] final results.
[0:21:59] >> Oh, that's really cool. I didn't know
[0:22:00] that it would spawn off work trees for
[0:22:02] you as well. That's really
[0:22:03] >> neat. I'm prompting it I'm prompting it
[0:22:05] to do so. And especially with our
[0:22:07] sessions app, that's something that you
[0:22:09] can do now as well. But it's not that's
[0:22:10] not like an autopilot exclusive thing.
[0:22:12] Yeah. I sometimes people forget like if
[0:22:14] you just tell it to do the thing, it'll
[0:22:16] go and do the thing. Yeah.
[0:22:17] >> Like it if you just tell it to go create
[0:22:19] it, oh, cool. I'll create work trees for
[0:22:21] you. Go. Do you are you using it for
[0:22:24] like a single issue? Are you kind of raw
[0:22:26] looping it where you're like, "Hey, I
[0:22:27] have this, you know, project. Go look at
[0:22:29] the repo, go through all the issues and
[0:22:31] do the thing fully and create work trees
[0:22:33] and do the just do it or are you just
[0:22:34] kind of working on one thing at a time?"
[0:22:36] Um, I'm kind of doing one thing at a
[0:22:38] time and just doing multiple sessions of
[0:22:41] it and just being very hands-off. I
[0:22:43] think I could let it just take a look at
[0:22:45] the GitHub um or our our VS Code issue
[0:22:48] our VS Code repo and just be like I have
[0:22:50] all these issues assigned to me like
[0:22:52] let's try to solve all of them. Um, I
[0:22:54] think personally I I don't want to shift
[0:22:56] like bad code. So, I do want to look to
[0:23:00] see what it's actually doing um at the
[0:23:02] end of the day and not just like accept
[0:23:06] uh just like randomly. So,
[0:23:09] unfortunately, it's not something I'd
[0:23:10] want to do yet, but it is definitely
[0:23:12] something you could try. You could try.
[0:23:14] I I might try it later on today and just
[0:23:16] say like, "Oh, this range of issues. I
[0:23:18] have a range of issues from the last
[0:23:19] week. Let's just like take a look at all
[0:23:20] these, see what is easy to fix, see
[0:23:22] what's not, and just like bump it all
[0:23:23] into one PR."
[0:23:25] >> That's cool. Yeah, I've been uh I've
[0:23:27] been experimenting uh uh around with it
[0:23:30] a lot because we we track a lot of work
[0:23:31] in GitHub and we have a lot of different
[0:23:33] like project settings and we have a
[0:23:35] bunch of like um like different
[0:23:38] requirements and like I need to like go
[0:23:39] grab like YouTube stats. I need all this
[0:23:41] stuff and I find like I've created some
[0:23:43] skills to like go and say, "Okay, here's
[0:23:45] what I need you to do like for my
[0:23:47] backlog work tracking." And I just say
[0:23:50] like let it rip and then it's going to
[0:23:52] call and it's going to run a bunch of
[0:23:53] like PowerShell scripts. It's going to
[0:23:54] run a bunch of this, but it's kind of in
[0:23:56] this frame where it knows that it needs
[0:23:57] to just like only do these things. And I
[0:23:59] found that super nifty because the auto
[0:24:02] approved tools, maybe this is a Daniel
[0:24:04] feedback, seems to be like really good
[0:24:05] where I can be like, "Oh yeah, run all
[0:24:07] the GH commands like just go for go to
[0:24:09] town, right?" Or just like go web
[0:24:10] request, go to town, right? For specific
[0:24:12] URLs like oh yeah, it's fine to go look
[0:24:14] at github.com um or like you know
[0:24:17] Microsoft learn documentation. But then
[0:24:19] there's other ones like for like uh
[0:24:22] PowerShell scripts. It's like it it's
[0:24:24] like every little little indication
[0:24:26] without like running all. So I'm just
[0:24:27] like, "Okay, go for it." Right? And
[0:24:29] sometimes you I think the other nice
[0:24:30] thing is sometimes at least for me how I
[0:24:33] feel is like I don't want to get in this
[0:24:35] pattern with the default of just always
[0:24:38] saying, "Oh yeah, just approve that,
[0:24:40] approve all approve all just in the
[0:24:41] workspace and the workspace and the
[0:24:42] workspace because then it feels like
[0:24:43] it's almost diminishing the point of the
[0:24:47] approvals because it's then you got to
[0:24:49] go manage going back." So I'm like,
[0:24:50] okay, I often do for this session. So
[0:24:53] that's kind of nice too that these are
[0:24:54] session based in general. Um, this is
[0:24:56] really cool. I didn't know exactly how
[0:24:58] it worked. So it's kind of good if
[0:24:59] people are going to see this like, okay,
[0:25:00] how's this use on it? Uh, I guess if
[0:25:03] people want to give feedback, what's the
[0:25:04] best way for people to give feedback on
[0:25:06] autopilot mode?
[0:25:07] >> Yeah. Yeah. I mean, Pearson and I have
[0:25:09] been posting on Twitter. We always get a
[0:25:10] bunch of feedback there. But the easiest
[0:25:12] way usually is just creating an issue on
[0:25:14] issue in the VS Code repo. Um, we'll
[0:25:17] definitely see I think it'll probably
[0:25:18] get auto assigned to me. Um, but
[0:25:21] anything feedback related, whether you
[0:25:23] it's not looping the way it's supposed
[0:25:25] to or you don't really understand how it
[0:25:27] works. I mean, feel free. I'll chime in
[0:25:29] on the issue. Um, but that's probably
[0:25:30] the best way to find us.
[0:25:32] >> Very cool. Well, Justin, thank you for
[0:25:33] coming on and talking through uh this
[0:25:35] autopilot mode. If you haven't tried it
[0:25:36] out, go check it out. I've been using
[0:25:38] like every single day. Um, I really love
[0:25:40] it. So, and we'll keep getting more
[0:25:42] updates, whatever is next in this in
[0:25:44] this world. I love it. And uh yeah, we
[0:25:46] have some some really cool stuff coming
[0:25:48] out from the team. You guys are crushing
[0:25:49] it with these weekly releases, too. So,
[0:25:50] get up there by the time this out. Maybe
[0:25:52] it'll already be in stable. We'll see.
[0:25:53] Um Justin, thank you so much for coming
[0:25:54] on. I really appreciate it.
[0:25:56] >> Yeah, thank you.
[0:25:57] >> All right, cool. Thanks everyone for
[0:25:58] tuning in to this VS Code Insiders
[0:26:00] podcast. Don't forget you can subscribe,
[0:26:01] like, of course, on the YouTube. We're
[0:26:03] on our own to 1 million YouTube
[0:26:05] subscribers, so check that out. There's
[0:26:06] a sweet 1M on the top of
[0:26:08] code.visisualstudio.com.
[0:26:10] That's pretty sweet uh subpage. Go check
[0:26:12] that out. And also, of course, you could
[0:26:13] listen to us as well. So you don't have
[0:26:15] to like watch me interview people all
[0:26:17] the time. You can just subscribe to the
[0:26:18] VS Code Insiders podcast on your
[0:26:20] favorite podcast application. Spotify,
[0:26:22] Apple Podcast, Pocketcast. That's my
[0:26:24] favorite. That's me though. That's going
[0:26:26] to do it for this VS Code Insiders
[0:26:27] podcast. So until next time, happy
[0:26:29] coding.
