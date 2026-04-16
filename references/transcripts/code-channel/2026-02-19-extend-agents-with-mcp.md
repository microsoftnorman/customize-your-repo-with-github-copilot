---
video_id: _g29UQjIAeI
title: "Extend Agents with MCP"
url: https://www.youtube.com/watch?v=_g29UQjIAeI
channel: "@code (Visual Studio Code)"
published: 2026-02-19
speakers:
  - Connor Peet
topics:
  - mcp
  - model-context-protocol
  - tool-integration
relevance: primary
---

# Extend Agents with MCP

Connor Peet demonstrates how the Model Context Protocol extends agents with external tools and data sources — covering server configuration, tool discovery, and live integration demos.

## Key Topics Covered

- **MCP overview** — How servers expose tools and resources
- **Configuration** — `.vscode/mcp.json` setup
- **Tool discovery** — How agents find and invoke MCP tools
- **Demos** — Real MCP servers in action

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Yeah. So, um I'm here to talk about
[0:00:01] extending your your agent with MCTP. Um
[0:00:04] and MCP is probably this thing you've
[0:00:06] heard of, you know, like you can plug
[0:00:08] things into your agent loop. So, uh BY
[0:00:13] was talking about like being able to
[0:00:14] like deploy your app to places and so
[0:00:16] that's something that you could do with
[0:00:17] MTP like Azure has a great MTP server.
[0:00:20] There's like super basease. There's all
[0:00:21] the um all the places that Cloudflare
[0:00:23] has an MTP server. So um you're probably
[0:00:25] familiar with like that as a concept is
[0:00:27] a thing you can use to uh make your like
[0:00:30] agent loop um a better a better and more
[0:00:33] capable but um it's more than just tools
[0:00:35] and so uh like a lot of those things
[0:00:37] like deploying things you could think of
[0:00:39] you know you could also use a commanding
[0:00:41] tool for that as well and like agents
[0:00:42] can you can use commanding tools really
[0:00:44] well as uh too um they can uh have
[0:00:48] knowledge of like you know tools that
[0:00:50] have been around they can also like
[0:00:51] figure out themselves pretty well um uh
[0:00:53] how to use any given CLI. But um the
[0:00:57] thing about MCP is that it's more than
[0:00:58] just tools. And actually tools were the
[0:01:00] kind of the first thing that uh came
[0:01:02] around when MCP was first created about
[0:01:05] a year and a quarter ago. Um so that uh
[0:01:08] came with tools and then resources and
[0:01:09] sampling and then there have been a lot
[0:01:11] of like cool things since then and I'm
[0:01:13] going to go through some of them today.
[0:01:15] Um so um there there are several things
[0:01:19] that MCP does um over you know just the
[0:01:21] CLI or over just like a basic like a
[0:01:24] tool call. Uh like one of those is
[0:01:26] dealing with resources. And so um uh um
[0:01:29] MTV um MTB tools can return resources
[0:01:32] like to you. So it can like generate
[0:01:33] images um and those can be like
[0:01:35] interpreted by your uh by your agent
[0:01:38] loop and you can also provide uh those
[0:01:40] as well to your um MC MCP MCP tool
[0:01:43] calls. Um um also recently um as of the
[0:01:47] like last the the 2025
[0:01:50] uh like 1125 like revision there is
[0:01:53] notion of of async tasks and so um
[0:01:57] something that like a lot of agent that
[0:01:59] a lot of agent loops uh struggle with is
[0:02:01] dealing with like tasks like like a dev
[0:02:03] server that start like in the background
[0:02:05] and we have like uh you have various
[0:02:07] ways and like detections that if we see
[0:02:10] you know uh like you're running a dove
[0:02:12] server in terminal we can like detach
[0:02:14] from that and like not block on that. Uh
[0:02:16] but but in MTP those those kinds of
[0:02:18] things are first class workflows and so
[0:02:20] um going back again to like deploying a
[0:02:23] site you know uh you might have a task
[0:02:25] that creates a VM which could take like
[0:02:27] 5 to 10 minutes and you don't want your
[0:02:29] agent loop to be blocked on that. And so
[0:02:30] that's something that an MCP server can
[0:02:32] represent really well um um like as a
[0:02:35] task that's running in the background
[0:02:37] that the agent loop can though can go
[0:02:40] and check on check in on again um after
[0:02:42] it's finished. Um and there's also the
[0:02:45] notion of like listations and so um MCB
[0:02:48] servers can ask you for information as
[0:02:51] well as sampling which is a way for them
[0:02:52] to uh make their own requests back to
[0:02:55] the LLM and actually have a quick demo
[0:02:58] that shows some of these. So, um I just
[0:03:00] put together a really quick I've justifi
[0:03:03] coded like MTP server that um that that
[0:03:06] helps create a website. And so I'm going
[0:03:08] to start by you know uh saying I'm
[0:03:10] making a a a portfolio site that has all
[0:03:13] my tools code in it. Um and so that's
[0:03:16] going to just call this tool. I'm going
[0:03:18] to just allow all tools um in the
[0:03:20] session just to make it nice and easy.
[0:03:22] Oh no. Uh one second. Let me pull I
[0:03:24] think I have to uh pull this up again.
[0:03:28] Uh,
[0:03:31] I have like uh five different VS code
[0:03:35] windows for doing demos of the session.
[0:03:37] So, I think I didn't start that one. All
[0:03:39] right, let's try that again real quick.
[0:03:41] Let's start this again and hopefully
[0:03:42] it'll all be good this time.
[0:03:46] There we go. So, we started a a new
[0:03:48] project and this also like returned a
[0:03:50] resource. It's just kind of a resource.
[0:03:52] It just says like this is um my
[0:03:54] portfolio and it has some like draft uh
[0:03:57] uh a metadata around it. But now I can
[0:04:00] start uh showing off one of the new
[0:04:02] features which is elicitation or or
[0:04:04] newish as of November. Um so I'm going
[0:04:07] to go go ahead and say start designing
[0:04:10] my layout. And so what this is going to
[0:04:13] do is that it's going to have the model
[0:04:15] ask me oh I think I'm I think I think
[0:04:17] I'm out of date. You normally this would
[0:04:19] show in chat but we can go ahead and and
[0:04:21] do that. And this um opens a um a web
[0:04:25] page hosted by the the MCP server which
[0:04:27] lets me like kind of sketch out my
[0:04:29] design. So you know I could have like a
[0:04:30] rectangle here for my content. I can
[0:04:32] have like a an app bar maybe like a
[0:04:35] navigation maybe sidebar there and I'll
[0:04:37] say done. Uh so now we see that actually
[0:04:40] comes back inside the tool call. So that
[0:04:42] comes back as a resource from that tool
[0:04:44] call. You see my beautiful design there.
[0:04:46] Um you you also have um you know if you
[0:04:48] have like Figma assets for example you
[0:04:51] can like save these um assets as well.
[0:04:53] So I can go ahead and download those if
[0:04:55] we want to. I can save them here into my
[0:04:57] test site folder. And there they are. Um
[0:05:00] so now uh let's say I want to go ahead
[0:05:02] and configure my site. So configure my
[0:05:04] site. And this is going to show a
[0:05:07] slightly different mode of elicitation
[0:05:08] where it's basically a form a form based
[0:05:10] listation where it's going to ask me um
[0:05:13] essentially um and and a kind of a quick
[0:05:16] pick flow uh what I want to do. So I'll
[0:05:18] I'll do a creative site. I'll do a
[0:05:20] single page site. Sure that color sounds
[0:05:22] great. And I'll do that as my maximum
[0:05:24] content. And that's let's uh skip the
[0:05:26] animations for now. Um I can also I can
[0:05:29] also I can also ask select my features.
[0:05:31] And so I want to say this is a contact
[0:05:32] form and I can go ahead and do that. Um,
[0:05:36] now we should actually be about good to
[0:05:37] go. So let's go go ahead and ask it to
[0:05:40] generate content. So this is actually
[0:05:42] going to go through the MCP server and
[0:05:43] the MCP server is going to use the
[0:05:45] sampling feature um uh to actually make
[0:05:48] its own requests going back to the uh
[0:05:51] model. So uh you first of all is first
[0:05:54] of all like you had a prompt just
[0:05:56] because you know if you have a premium
[0:05:57] model selected you don't want to like
[0:05:58] have a server like using a premium
[0:06:00] request premium premium request like
[0:06:03] without you knowing about it but I can
[0:06:04] go ahead and um allow that and then that
[0:06:07] will go ahead and uh create that content
[0:06:09] for me. Um so it's going to go make
[0:06:13] those pages. Um I think maybe the server
[0:06:16] is being a being being a bit lazy here,
[0:06:18] but uh that's kind of the overall flow
[0:06:20] of some of these features. And and if we
[0:06:22] go to the um the log of of um requests
[0:06:27] that it made, we should be able to see
[0:06:29] that. And we you see that it made these
[0:06:31] requests to server and ask for these
[0:06:33] different contents.
[0:06:35] So that's kind of what we had um as of
[0:06:40] um like last release or sorry as of the
[0:06:44] the release back in December. Uh but the
[0:06:46] the cool new thing that we came and the
[0:06:49] cool new thing that's come recently is
[0:06:50] is MT is MTP apps. Oops. Oh yeah. Um,
[0:06:54] and I'll actually start by showing a a
[0:06:56] quick demo from a story book, which is
[0:06:59] um an an MTV an MTP server that's
[0:07:02] oriented around like designing uh
[0:07:03] different components on the web. Um, and
[0:07:05] how they used um MTP apps, MCP apps in
[0:07:08] their scenario.
[0:07:11] Um so essentially what they do that's a
[0:07:14] transcript for this because uh I'mware
[0:07:17] of time. Um
[0:07:20] uh they use MCP apps to actually show uh
[0:07:23] like interactive content inside of chat.
[0:07:25] So uh MCP apps essentially give the um
[0:07:28] MCP server a way to uh uh like have
[0:07:32] their their like own content uh like
[0:07:35] which is uh shown inside of chat. And so
[0:07:38] the very basic way is just you know you
[0:07:40] have to call interol like returns like
[0:07:42] data and the data is uh shown inside of
[0:07:45] a response but these are actually fully
[0:07:47] interactive things as well. Um and so
[0:07:49] there's a few other cool things that you
[0:07:50] can do with apps. So I'm going to go
[0:07:52] ahead and swap to the window if I can
[0:07:54] find the window. Here we go. Um so um in
[0:07:59] this repo I have um some pull requests
[0:08:01] and so I want to like review those but
[0:08:03] but I don't know like what I want to do
[0:08:05] first and so I'm going to ask the model
[0:08:06] to please use the uh list sort um
[0:08:11] uh uh tool which has which has an MCP
[0:08:14] app attached to it. And what this does
[0:08:17] is actually lets me have a like
[0:08:19] interactive list here. And I can drag
[0:08:21] around this list and I can say maybe I
[0:08:23] want to say I want to like view this PR
[0:08:26] first. And so I'll drag that to the top.
[0:08:27] And then in this app I have a button to
[0:08:29] say I want to save the order. Um and so
[0:08:32] then uh so then it prefills my next
[0:08:37] message with uh that resulting order. So
[0:08:39] that's a nice way that I can like really
[0:08:41] easily kind of like interact with this
[0:08:42] and otherwise I'd have to like you know
[0:08:44] copy and paste things around. Um, but
[0:08:46] this gives me a very natural way to to
[0:08:49] do that interaction. So, needs to do
[0:08:51] that and then it's going to probably
[0:08:52] like call GitHub and go ahead and start
[0:08:54] doing that. Oh no, I have to change I'll
[0:08:58] change two different model. Let's just
[0:08:59] do 41.
[0:09:01] Um, yeah. So, that's one thing. Um, one
[0:09:05] other kind of cool thing um from this
[0:09:07] MTP server that I'm using, which is just
[0:09:09] a kind of demo server, is that um I have
[0:09:12] the script here that does some
[0:09:13] benchmarking. And this just like runs
[0:09:15] some benchmarking on some of the code in
[0:09:17] this repo. Um, but I want to say that I
[0:09:20] want to then analyze this code. So I
[0:09:22] think I have something in my history.
[0:09:24] Let's see. So I can ask model. I'm going
[0:09:26] to swap swap over swap over ta coup
[0:09:28] here. I'm going to ask it to run this
[0:09:31] benchmark and then analyze the result.
[0:09:33] So it's going to go ahead and take a
[0:09:35] second to read that
[0:09:38] and build my server or build my um
[0:09:41] project.
[0:09:42] I can figure out how to do that
[0:09:47] and then run the benchmark and and so we
[0:09:50] see that it completes here. Um and so
[0:09:52] normally I'd have to then I think
[0:09:54] there's a CPU profile somewhere in in
[0:09:56] here. Um but what but yeah what it
[0:09:58] actually did is that um because it
[0:10:01] created a CPU profile file that was
[0:10:03] actually a given to a tool that exposes
[0:10:06] an a tool that exposes anmcp app and
[0:10:09] actually uh let me visualize that like
[0:10:12] directly inside of chat here. So I can
[0:10:14] oops I don't want to close that I just
[0:10:15] want to collapse that sidebar.
[0:10:18] So I can then like go in I can see like
[0:10:20] this is the time it took to do these
[0:10:22] different things. I can click on say I
[0:10:24] want to like analyze like this this call
[0:10:26] frame a bit more and looks like actually
[0:10:28] creating this um broken circuit error
[0:10:31] actually took like the majority of time
[0:10:32] in this one in this one test case and so
[0:10:35] I I'll go ahead and click over into that
[0:10:38] if click works and then I can go ahead
[0:10:40] and hit analyze and so that's going to
[0:10:43] then uh basically prefill again give a
[0:10:46] prompt to um analyze like that that to
[0:10:49] analyze like to analyze to analyze that
[0:10:51] frame in the call stack
[0:10:52] Um, and so it's going to give me like
[0:10:54] some good give some good like
[0:10:56] suggestions you fix these things. And
[0:10:58] then um, it looks like I think these are
[0:11:00] probably pretty good things. It's it's
[0:11:02] using a singleton error instead of
[0:11:03] creating a new one every time because
[0:11:05] because collecting because collecting a
[0:11:07] call stack is kind of expensive in
[0:11:08] JavaScript. Um, and that should fix the
[0:11:10] issue. So,
[0:11:12] uh those are are both um nice ways that
[0:11:17] you can use apps to kind of like
[0:11:18] visualize and um and kind of create like
[0:11:23] interactions with um your data um inside
[0:11:26] your agent view. So, it's really good
[0:11:27] for the human in loop kind of things
[0:11:29] where you have like data that's messy or
[0:11:31] data that you can't that's like not
[0:11:32] really like easy to like manipulate
[0:11:35] otherwise. can actually now have a a
[0:11:37] rich app that you can interact with in
[0:11:39] in very in very easy ways to do these
[0:11:41] things.
[0:11:43] Uh hop over here again.
[0:11:46] Trying to figure out how to go try to
[0:11:47] figure out how to go to my next slide
[0:11:48] with the YouTube video up. There we go.
[0:11:51] Um yeah, so the so apps so apps so apps
[0:11:55] um um as we shown can do a few things.
[0:11:57] They can show the results. They can
[0:11:59] actually also attach data to they can
[0:12:02] also attach data to your context. um and
[0:12:05] they can send messages on your behalf,
[0:12:07] which is what um um I showed in those
[0:12:09] two in those two examples. But one
[0:12:11] really cool thing they can also do is
[0:12:12] they can actually also call tools on the
[0:12:14] MT on the the MTP server itself. And and
[0:12:17] you can use that to do some really
[0:12:18] interesting and you can use that to do
[0:12:19] some really interesting interactions. So
[0:12:22] um and both the two apps that I just
[0:12:25] demoed those uh showed you visual and
[0:12:27] then you could interact with it and but
[0:12:29] but then
[0:12:31] the agent loop at that point was kind of
[0:12:32] done. But you can actually do a more
[0:12:34] advanced flow where you can actually
[0:12:36] have the um the MCP tool wait for
[0:12:40] interaction and adapt to happen before
[0:12:43] uh
[0:12:45] before it returns uh control back to
[0:12:46] model. Um
[0:12:49] so um I have this this flow diagram but
[0:12:52] it's probably easy
[0:12:55] to show it to you. So um I just like
[0:12:57] vibe coded. I just like one shot this uh
[0:12:59] color picker um um MCP. You can see my
[0:13:02] vibe coding right here. Um it was it has
[0:13:05] two requests. Um and essentially what
[0:13:07] this is going to do is that it's is a
[0:13:10] has a tool called uh pick color and
[0:13:12] that's just going to show a color picker
[0:13:14] and and how MCP app is is declared is
[0:13:17] that the tool has like metadata right
[0:13:20] here which has a URI of a resource on
[0:13:22] that server which presents that MCP apps
[0:13:25] UI. Um, and then what I actually did
[0:13:27] here is I have a second cool is I have a
[0:13:30] second tool called called confirm color.
[0:13:32] And this is only going to be visible to
[0:13:33] the app itself. Um, and then when this
[0:13:36] is called, it's going to like confirm uh
[0:13:39] um the color like was picked. And then
[0:13:41] my pick color tool is going to wait on
[0:13:43] that appending pick to actually resolve.
[0:13:46] So I can go ahead and uh do that. I'm
[0:13:50] going to use haiku because I'm asking
[0:13:51] about a haiku and I'll ask it to pick
[0:13:54] and ask it and ask it to pick my my
[0:13:56] favorite color and then write a then
[0:13:57] write a write a haiku about it if it's
[0:14:01] going to work. Ah, no.
[0:14:05] I I'm I'm going to have to ask me for my
[0:14:07] favorite color.
[0:14:09] Let's try this.
[0:14:12] Well, that's not very useful. Uh
[0:14:16] using the pick color tool. As I said,
[0:14:19] this is bad coded and like not tuned.
[0:14:21] Um, there we go. So now it's actually
[0:14:23] going to use that tool and we can see
[0:14:24] that the tool is actually still running
[0:14:26] as far as VS code is concerned. But I
[0:14:28] can now go and um and interact with it.
[0:14:31] Um, I like a nice dark green color. So
[0:14:32] I'm going can going to go ahead and pick
[0:14:34] that. And then and then once I hit
[0:14:36] confirm, it's going to send that
[0:14:37] response back to the model. And the
[0:14:39] model's going to hopefully write
[0:14:40] something very uh nice about my Yep,
[0:14:42] there we go. And just like that. Yes,
[0:14:45] this is Yeah, this is actually all vibe
[0:14:47] coded just using a skill which uh a
[0:14:49] Brook just talked about. So, there is um
[0:14:51] actually just pulled down a skill uh
[0:14:53] from um
[0:14:56] there we go from um this this MTP this
[0:14:59] MTP apps playground repo that another
[0:15:00] team member uh made and I just like
[0:15:02] pulled this down. I said, "Hey, copilot,
[0:15:04] here's the skill. Uh here's what I want
[0:15:06] and then go do it." So, that's how um
[0:15:10] that's how that that's how that app was
[0:15:11] made.
[0:15:13] Um so, without a
[0:15:15] We're about out of time, but um in
[0:15:17] essence like those are are the ways like
[0:15:19] you can use MTP to uh to to interact in
[0:15:23] in rich ways like with the model and if
[0:15:24] you're and if you're a developer of an
[0:15:27] MCP server definitely check out MTP apps
[0:15:29] um they're supported in VS Code and I
[0:15:31] think uh Claude and Openi and Open AI
[0:15:34] also support them now. So try them out,
[0:15:36] give them a shot and um and yeah, build
[0:15:38] something cool. That's that's all for
[0:15:40] me. So I'll pass it off to whoever's
[0:15:42] next.
