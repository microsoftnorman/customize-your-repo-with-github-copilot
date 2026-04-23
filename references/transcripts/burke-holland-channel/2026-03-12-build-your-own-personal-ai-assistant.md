---
video_id: PEtM45hG-5A
title: "You can build your own personal AI assistant - it's super easy"
url: https://www.youtube.com/watch?v=PEtM45hG-5A
channel: "@BurkeHolland"
published: 2026-03-12
speakers:
  - Burke Holland
topics:
  - copilot-sdk
  - copilot-cli
  - autopilot
  - fleet
  - custom-agents
relevance: primary
---

# You can build your own personal AI assistant - it's super easy

Burke Holland walks through building a personal AI assistant with the GitHub Copilot SDK, background tasks, and agent-style workflows.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Intro - Is the personal AI hype real? |
| 00:44 | Demo of Max |
| 03:43 | Let's build it |
| 07:02 | Compacting and plan mode |
| 11:38 | Building with Autopilot and Fleet |
| 17:08 | Running real tasks in the background |

## Key Topics Covered

- **Copilot SDK**
- **Plan mode**
- **Autopilot**
- **Fleet mode**

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Openclaw. You've no doubt heard about it by now. It is this personal AI agent assistant thing that people are buying
[0:00:07] Mac minis and they're putting it on there and then depending on who you are or who you listen to it's either
[0:00:13] Changing your life and automating everything or it's completely over height and in this video
[0:00:18] I want to show you how you can build your own
[0:00:21] Personal AI assistant on the Co-pilot SDK how easy it is to do that and then I'm going to make a strong argument to you about why you
[0:00:29] Absolutely should do that and I'm going to show you one that I built and how I actually think it is changing my life and
[0:00:36] Helping me automate a lot of the tasks in my day today and so if you're ready
[0:00:42] Let's do it. So I think the best way to start this video is really to just show you what I built now again
[0:00:47] This video is not about what I built. It's about what you can build
[0:00:51] But this is what will be sort of trying to build here in this video and it's called max
[0:00:56] I'll leave a link to this if you just want to see what I've done here and
[0:01:00] Max is my personal AI assistant and so
[0:01:04] We can talk to Max over telegram here and telegram is what we're going to be using in the video today to
[0:01:09] Converse with his assistant from anywhere
[0:01:11] So we'll just send a hello message here and you'll see that Max is typing and then
[0:01:17] momentarily we get a response from Max now
[0:01:21] um
[0:01:22] For the rest of the demo here. I'm actually going to talk to Max over telegram in the web because it doesn't work so well
[0:01:30] For me to give it commands on the phone
[0:01:33] Just on the little
[0:01:35] Running the phone on the desktop here like I'm doing on the Mac what's built into Mac OS so let's switch over to the web real quick
[0:01:41] Okay, so let's take a look at some of the other things that this bot can do I can say for instance
[0:01:48] Hey Max I was working on a draft of a blog post yesterday. Could you just go ahead and give me the link to that draft?
[0:01:59] All right, and then there's the blog post that I was working on this is the one and then it can do things like check my email
[0:02:05] Hey Max do I have any emails that look pretty important saying the last 48 hours that I haven't looked at yet
[0:02:16] And Max says he's checking and yes, I did say he and I do call it Max
[0:02:20] Okay, he's checking he'll be back shortly and what Max is doing is using background workers and all of this is powered by
[0:02:27] The Co-Pilot SDK. It's checking my personal Gmail
[0:02:30] And it's going to come back and give us an answer here
[0:02:33] And so what I want to do here is kind of show you how to build out this integration with telegram with github as you've seen here
[0:02:40] This is my personal blog running on github here and with google workspace
[0:02:45] So that's what we're doing
[0:02:47] This video now before we get started you don't need to have a very complex machine to run this right?
[0:02:53] So I'm actually running this on a little B link machine that's over here on the side
[0:02:59] It's a little bit bigger than this one here
[0:03:00] But I think this is just fine and I'm running on the cub or on the coob
[0:03:04] I'm actually not sure how to pronounce this
[0:03:07] But it is a really really nice Linux setup. It's on Ubuntu. It has a really nice UI great window switching
[0:03:15] And then Max is back with our email here and actually had to give it a little direction here
[0:03:19] I was messing around with this yesterday
[0:03:21] demoing and trying to get it to use a browser
[0:03:23] So I had to guide a little bit
[0:03:24] But it looks like I have this kitty alert for my son who logged in and then
[0:03:29] Some GCP projects which are going to be shut down
[0:03:31] Everything else is linked in alerts, Reddit notifications, bank balance
[0:03:35] Want me to pull up the details of the other two?
[0:03:37] Yeah, I guess I could say how much is in my checking account
[0:03:39] But we won't do that on this video
[0:03:42] So okay, let's get started and actually build out this personal assistant with telegram
[0:03:48] And with email functionality, we're going to do that on the co-pilot SDK
[0:03:52] All right, so we're logged into the GitHub co-pilot CLI
[0:03:55] I'm using an individual studio code as I always do
[0:03:59] And we're going to use a custom agent today
[0:04:02] This custom agent is one that I've created
[0:04:04] If you watch the orchestration video, then you will notice since called anvil
[0:04:09] And I'm working inside of a Docker container here
[0:04:11] So we have a clean environment
[0:04:12] So let me just grab this
[0:04:14] And then let's paste it in
[0:04:15] And if you remember, we can sort of suspend the co-pilot CLI by pressing control Z
[0:04:22] And that just suspends it
[0:04:24] We can paste our commands here
[0:04:25] Okay, plug in as installed and then remember we do fg
[0:04:29] To bring the CLI back
[0:04:31] And now we can look for agents
[0:04:33] And we may need to restart the CLI to pick that agent up
[0:04:37] Let's see if that's true
[0:04:41] Slash agents
[0:04:43] Yes, and now we see it
[0:04:44] And if you want to know about what anvil does, I recommend watching that
[0:04:48] Orchestration video where we talk about anvil
[0:04:52] But basically essentially it does a couple of things
[0:04:55] It uses context 7 mcp server to search for docs
[0:04:59] It really tries to get the agent to fetch on the web
[0:05:02] It has some guiding principles
[0:05:03] And then it gets the CLI to use multiple models to actually write code
[0:05:08] So it uses opus, gimani3pro
[0:05:11] And gpt53
[0:05:14] I should update it to 5.4 because 5.4 is out now
[0:05:17] Now you don't need the anvil agent to do that
[0:05:20] But I do everything on anvil now
[0:05:22] So that's what I'm going to be using here in this video
[0:05:25] So the first thing that we're going to do here is we're going to get
[0:05:28] Co-pilot CLI to learn everything that it can about the co-pilot SDK
[0:05:32] And we're going to use this new research
[0:05:34] Command that's built into the CLI and the rich is going to have it research
[0:05:38] github slash
[0:05:39] co-pilot SDK
[0:05:41] And that is the repository for the co-pilot SDK
[0:05:44] It contains all the code
[0:05:45] All of the docs
[0:05:46] Essentially, I want the CLI to know everything it can possibly know about the co-pilot SDK
[0:05:54] So that it doesn't try to do things that don't exist in the sdhay or right code that won't work
[0:05:59] So while this is running, let me sort of explain what the co-pilot SDK is and what it does
[0:06:04] It essentially wraps the co-pilot CLI and allows you to embed it in your project or your code
[0:06:11] So instead of having to call the CLI commands directly what your code could do
[0:06:15] It's an sdk that just makes it super easy to do that
[0:06:18] So you can add essentially the co-pilot CLI to any project
[0:06:22] And that is what is powering max here
[0:06:24] Right? This is how max knows how to execute commands, how it knows about github
[0:06:28] Is because it can do anything that the co-pilot CLI can do which is a lot
[0:06:33] Right? You get the whole co-pilot CLI harness plus all the tools like file editing
[0:06:38] Get a mincp, just get that for free which means out of the box your agent can do almost anything
[0:06:43] So again, pretty exciting
[0:06:45] It's so much fun to build one of these
[0:06:47] Oh, let's check on the research
[0:06:49] Okay, so here's our full report right here
[0:06:52] And if we click on this, here it is, you can see it's quite lengthy
[0:06:55] And that's good
[0:06:56] I wanted to know everything about the sdk and it looks like it's learned a lot
[0:07:00] Now the next thing that we want to do here is I want to switch out of plan mode
[0:07:05] And I want to instead
[0:07:08] I want to look at and see
[0:07:11] How much of the context window how we actually used?
[0:07:13] So 132k of 200k, so 66% of the context window
[0:07:20] Okay, it's good to know because we're going to reset the context window
[0:07:23] And if you've watched some of my other videos, you'll have heard me say maybe that the context window is like a room
[0:07:28] It's not a memory. It's a room
[0:07:30] So the more cluttered it gets, the harder it is for the ai-at-a even function
[0:07:34] It's just confused
[0:07:36] And so we're going to do that right now
[0:07:37] So what we're going to do is hit compact
[0:07:39] And what compact is going to do is it's going to basically tell the ai hey
[0:07:43] Summarize everything we've done and learned in this session
[0:07:47] And then it's going to start a new session and attach that as the context for that session
[0:07:52] So it has some recollection of what happened here
[0:07:54] Again, it's like moving to a different room and taking just the stuff from this room that you need with you to the new
[0:08:00] Clean room
[0:08:02] Okay, compaction is complete
[0:08:03] And then we have this file here
[0:08:05] Which this file is actually here this full report home node
[0:08:08] Copilot session state
[0:08:10] Blah blah blah blah blah
[0:08:11] We actually wanted in this project
[0:08:12] And the easiest way to get it in this project is to click here
[0:08:16] So I've already oh, I'll do it again
[0:08:18] Don't we're going to command click
[0:08:20] And then if we open a sidebar
[0:08:22] Just drag it in
[0:08:23] And boom it's right there and the reason why we do that so let's close these out is because now we're going to actually implement
[0:08:30] We're going to want to make a plan on this knowledge of the SDK
[0:08:34] So I'm going to shift tab into plan mode here and I'm going to say
[0:08:37] Um something very simple about what I want to do
[0:08:42] I used to try to explain to the ai everything that I wanted in one prompt and that's a big mistake
[0:08:47] It's better to be as vague as you can
[0:08:50] And let plan mode help you build out the details. So let's walk through it
[0:08:53] I want to build a personal assistant on the copilot sdk that I can communicate with over telegram
[0:09:02] And then I'm going to use the at sign and I'm going to specifically mention our research here
[0:09:07] The Martown file
[0:09:08] And then I'm going to go ahead and send it and I'm going to let the plan mode ask me clarifying questions
[0:09:15] To actually put together a really detailed plan and that will help us
[0:09:20] Be
[0:09:21] That will help us get a better result with higher confidence at the end here instead of building something that might be broken right out of the gate
[0:09:28] So let's see what plan mode does here
[0:09:30] Okay, so the first question is which language do we want to use? It says python and node is recommended
[0:09:35] That's what's in our dev container python
[0:09:38] There's also a go sdk and really you know you can use any of these languages that you want
[0:09:44] I I starting to think that it's more important that you know how to put the pieces together versus
[0:09:48] The programming language so just because we don't know go doesn't mean we couldn't use go
[0:09:53] Even though that wasn't recommended but we're going to use what's recommended
[0:09:56] Which is just tight script and JavaScript but consider
[0:09:59] That you may not need to understand the programming language to actually build something depending on what you're doing
[0:10:04] You may disagree very strongly with that statement
[0:10:07] But just consider whether or not there's any truth there. Okay, how should the copilot sdk authenticate?
[0:10:13] So GitHub token via environment variable so it looks like simplest requires a copilot subscription
[0:10:23] Here what I'm going to do is because I don't really understand all I want it to do is
[0:10:27] Just let the user log in to the copilot
[0:10:30] CLI
[0:10:31] Okay, because when the sdk is actually used you have to be logged into the CLI and if you're not then it needs to know how to handle that
[0:10:40] So what's the scope do you want for a personal copilot sdk supports custom tools and CP servers hooks and sub agents
[0:10:47] So what we want is
[0:10:49] Full feature tools and see I want everything that the CLI has all of its powers
[0:10:55] I want those powers and this personal assistant
[0:10:58] How should copilot sessions map
[0:11:00] Um one persistent session per telegram user
[0:11:04] One session per telegram chat. Nope. Yeah, we want the persistent session
[0:11:08] Okay, which telegram body you prefer. I don't know anything about telegram bots
[0:11:12] But I'm going to choose this first one here type script first modern well maintained that sounds promising to me
[0:11:20] All right, now you see our agent helping out here where it's using context 7 and it's actually looking up copilot sdk
[0:11:27] documentation
[0:11:29] So it has the research that it's done. It's looking at documentation. It just looked at documentation for gramey
[0:11:35] So it's just doing a lot of research here
[0:11:38] Okay, so our plan is ready and I'm going to go ahead and choose number one
[0:11:42] Which is accept plan and build on autopilot plus fleet
[0:11:46] If you watch the raw video fleet is where it deploys a bunch of sub agents
[0:11:51] To take care of things and it tries to continue working until it gets all the way to the end
[0:11:56] So this is going to take a minute to complete
[0:11:59] We'll fast forward and come back and talk about the results
[0:12:02] So I will see you in just a second
[0:12:05] Okay, it's done and you can see there's a lot more files in our project now especially in the source folder here
[0:12:11] Okay, so update built a fully featured telegram personal assistant on the github copilot sdk awesome
[0:12:17] Now the question is how do we run it? Okay, so to run copy ev.example to env
[0:12:25] Okay, so here's env.example. So I think we can just rename this right to env perfect and then
[0:12:32] add your telegram bot token
[0:12:36] Ensure copilot off login is done and then run npm run
[0:12:41] Dev okay, so let's go ahead and get this telegram bot token. Let's ask now before we do that
[0:12:48] I'm going to switch to a smaller model here like haiku
[0:12:52] And I'm just going to say let's get switched out of autopilot. Where can I get the telegram bot token
[0:12:58] I actually know how to do this, but let's just assume for a second. We have no idea how to sub telegram bot
[0:13:04] I want to see a lot of walk us through that. Okay, so we need to open telegram and search for bot father
[0:13:09] Starting new conversation create a new bot follow the prompts. Okay, and then we need to paste in our tokens
[0:13:15] Into this file here, right? And it looks like our telegram bot token is what we want
[0:13:22] And we want to paste that into our env file
[0:13:25] There okay, so in telegram if we just search for bot father you'll find it right here
[0:13:31] It's very popular and then what can this bot do and then let's start a chat in now we want to do new bot
[0:13:39] All right a new bot. What are we going to call it? We can call it anything
[0:13:42] Let's just call it personal assistant and
[0:13:45] Then we're going to have to choose a unique name for it and somebody called this BERC's
[0:13:50] Let's just call this BERC's personal assistant
[0:13:54] demo bot and then it has to end with bot or underscore bot as it shows the example there
[0:14:00] And then we get this key that we need so we're going to copy this right here
[0:14:05] So I'm going to control see copy that and then paste that in right there as per the instructions
[0:14:10] And then we can click on this and that will actually add the bot
[0:14:14] So here's the bot and we can start in now our
[0:14:18] Personal assistant isn't running so we need to start the personal assistant. So let's go back here
[0:14:24] And it looks like the default model the default model. You know, I'm going to recommend that we use a sonnet
[0:14:31] Four six it's a very good model sonnet four six
[0:14:36] And uh, okay, so then let's come back here
[0:14:39] We want to start this and it says I think we just did impiam run
[0:14:44] Dev I forget. Let's see was an impiam run
[0:14:48] Excuse me. So if you don't know we could just do impiam run. So it's like impiam run dev. So impiam run dev
[0:14:58] starting the personal assistant
[0:15:00] telegram bot starting
[0:15:03] Stent start to begin chatting. Okay, so in theory if we come back to telegram here
[0:15:07] We should be able to say hello
[0:15:12] Okay, and we got a thinking response right away, which I think came from here. Yes
[0:15:18] Create a session. Okay
[0:15:21] There it is. So just like that we're up and running with telegram and we have a bot
[0:15:26] I'm here. I'm the co-pilot CLI your terminal assistant
[0:15:29] I can help you and of course it thinks it's a coding assistant
[0:15:32] So we would need to go back and work on this
[0:15:34] But um, this is great. So out of the box, you know, we get access to things like github
[0:15:39] So we could say something like
[0:15:41] Could you please go check on the simple react snippets repo and tell me if there's any
[0:15:45] PRs there that I need to take a look at
[0:15:49] And that's just one of my projects
[0:15:50] And so let's just see if this bot can go off and do something useful for us without any other
[0:15:55] configuration on our end
[0:15:56] And it looks like it wants to know where it's at
[0:15:59] So we have some work to do on the bot here, but I think it's just simple react snippets
[0:16:05] See if it can take care of this task force here
[0:16:09] And I'm curious actually what model this is we said sonnet 4 6 in the
[0:16:14] Configuration but let me just ask what model are you
[0:16:21] Because these are responses are pretty quick. I'm high cou four five. Okay. I know wonder switch to
[0:16:28] Sonnet 4 6
[0:16:30] And wonder if it can do that
[0:16:35] Don't have the okay, so we'd have to go build this ability into the agent
[0:16:39] But you can see
[0:16:40] We've already got something that's up and running
[0:16:42] And we did that just by building on the co-pilot SDK
[0:16:46] So now the question though is how overhyped or not overhyped are these bots and for me
[0:16:53] I find it really useful and the reason is because I can use this bot to do work
[0:16:57] Both when I'm at my desk and when I'm not and I can do a lot of things a synchronously
[0:17:01] So let me give you a practical example of how I would use this in my daily life
[0:17:07] So here at Microsoft part of what I do in community sometimes is we run
[0:17:12] AMAs on Reddit. So if we go to the github co-pilot subreddit here
[0:17:17] Get a co-pilot subreddit one of the things that you'll see is that we did an AMA
[0:17:21] Right here to celebrate 50,000 members. We had a blast doing this
[0:17:25] You can say it's quite long with a lot of questions that I answers from the team
[0:17:30] And so what we would want to do now is figure out what is it that people are asking and what do they want
[0:17:36] And then we want to compile that into a report for the product team so they can see this is what people are asking for
[0:17:42] This is why we do the AMAs is so that we can figure out what it is that people are actually interested in and what do they want
[0:17:49] Because it may not be what we think people want
[0:17:52] So this is how I would use the bot to do that
[0:17:55] Hey Max can you please go out and take a look at the Reddit AMA that we did last week on our slash github co-pilot
[0:18:02] Find the main themes and insights stuff the product team is going to want to know about
[0:18:07] Based on the questions that people asked compile that into a Google document and then just drop the link here in the chat
[0:18:17] Okay, so it's off working on it now
[0:18:20] I'm gonna go off and do something else when it comes back
[0:18:22] It's gonna notify me and I find that working over chat like this is really nice because I'm gonna get a notification when it's done
[0:18:28] But at this point, I'm gonna continue on and do something else here
[0:18:32] So I'm gonna say Max I believe I gave you access to Twitter slash X the other day
[0:18:38] Is that access actually working? Can you just check?
[0:18:44] And you'll notice I'm referring to things that happened days ago
[0:18:47] In the past right and the memory is a big part of what makes the bot or the assistant actually helpful because
[0:18:54] It can take you know parts of things that you're saying remember things that happened before put those together
[0:18:58] And actually give you an answer so that you're talking to it the way that you would talk to a human being
[0:19:03] You don't want to have to redescribe the situation every single time
[0:19:06] So it's gonna check on that. It's gonna get back and then while it does that
[0:19:09] I'm gonna do one more thing
[0:19:11] Max last week I published a video on the co-pilot
[0:19:17] Autopilot and fleet versus a Ralph loop
[0:19:20] Can you make me a YouTube thumbnail?
[0:19:22] 16 by 9 for that video
[0:19:27] And I'm gonna send that off as well
[0:19:28] So it looks like x-axis is working connected and authenticated without issues so I can say great
[0:19:36] Can you do a search on x-then under your account and just find like what are the big AI topics?
[0:19:41] Everyone is talking about today. What are the things I need to know about?
[0:19:46] We're gonna send that one as well
[0:19:47] So you can see there's multiple things happening here at one time
[0:19:51] And if we wanted to see what those different things are
[0:19:53] There's a workers command
[0:19:54] And we can see the reddit analysis is actually currently running in the background
[0:19:59] And I'm surprised we don't see one for the x as well
[0:20:03] There it is right there. It was just a little delayed
[0:20:06] So the ama analysis is running the x and analysis is running and while it's doing that
[0:20:11] I can move on to other things
[0:20:12] So actually find that these bots are super powerful
[0:20:16] The question is just what can they do?
[0:20:18] And of course because of skills here
[0:20:20] You can really have them do anything at all
[0:20:22] You just need to add a skill for it
[0:20:24] And I had to come back and re-record this because I forgot to show you the results
[0:20:27] Because I don't, everyone you think that I'm just blowing smoke
[0:20:31] We just show you what the agent brought back for the things that we asked it to do for my
[0:20:35] Real-life job here
[0:20:36] So you can see here the ama analysis is done
[0:20:38] And has been added to a document just like I asked for
[0:20:41] Here's everything that's hot on x-day including vide coding and apparently
[0:20:46] Models are lying to people
[0:20:47] No surprise there
[0:20:49] And then I had to uh
[0:20:50] I had to nudge it a little bit made of a steak but there's my youtube thumbnail
[0:20:53] Right not quite what I wanted I could work with that
[0:20:55] But just so you can see that the bot is actually delivering
[0:20:58] The things that I need to do the job
[0:20:59] And if you look at my last video it looks a lot like that thumbnail
[0:21:02] Because Max made that thumbnail
[0:21:04] So I would encourage you build your own
[0:21:07] Personal assistant if nothing else it's a ton of fun
[0:21:10] And remember you can take a look at mine which is called Max
[0:21:13] Which I've put quite a bit of work into there's a terminal UI and a telegram UI
[0:21:19] But if you just want to see some of the things that I've done
[0:21:22] You can take a look at that and how I've put that together
[0:21:24] But build your own personal assistant on the co-pilot SDK
[0:21:28] It's a ton of fun
[0:21:29] You can use it from anywhere you can make it do anything
[0:21:31] And start automating parts of your life
[0:21:34] I think that you'll find that maybe you're out for a walk somewhere
[0:21:36] You'll remember something about a repository
[0:21:38] And instead of having to come back to your computer to use co-pilot
[0:21:42] You can just talk to your personal assistant because you are talking to co-pilot when you do that
[0:21:47] Thanks for watching this video
[0:21:48] I really like these personal assistants and I don't think they're over height
[0:21:52] I think they're actually really cool
[0:21:53] Go build your own
[0:21:55] And as always
[0:21:56] Happy Cody
