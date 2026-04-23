---
video_id: GsEPS1yHaHQ
title: "The GitHub Copilot SDK IS INSANE! Put Copilot INSIDE Your Apps!"
url: https://www.youtube.com/watch?v=GsEPS1yHaHQ
channel: "@JamesMontemagno"
published: 2026-01-22
speakers:
  - James Montemagno
topics:
  - copilot-sdk
  - copilot-cli
  - tool-calling
  - session-management
relevance: primary
---

# The GitHub Copilot SDK IS INSANE! Put Copilot INSIDE Your Apps!

James Montemagno explores the GitHub Copilot SDK, including session management, model switching, streaming, and tool calling inside custom applications.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Copilot Everywhere, New SDK |
| 02:32 | Copilot CLI Walkthrough |
| 07:01 | Copilot SDK Explained |
| 09:01 | SDK Interactive Demo |
| 13:52 | Podcast Metadata Generator |

## Key Topics Covered

- **Copilot SDK**
- **Copilot CLI**
- **Tool calling**
- **Custom apps**

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] GitHub Co-Pilot is everywhere.
[0:00:02] I use it every single day to write code in VS Code
[0:00:05] and in Visual Studio 2026.
[0:00:07] But that's not the only place I use it.
[0:00:09] I'm constantly delegating tasks and assigning issues
[0:00:12] to the coding agent in the cloud.
[0:00:14] And actually most of the time directly from my phone
[0:00:16] with the GitHub mobile app where I can pull it up,
[0:00:18] pull up a repo, give it an idea, and it gets to work.
[0:00:21] I'm constantly asking questions on kiddup.com
[0:00:24] and even working across code bases in Xcode and IntelliJ.
[0:00:28] when I have to work in Swift or Kotlin libraries.
[0:00:30] So truly I take GitHub Co-Pilot with me
[0:00:32] everywhere on every single machine
[0:00:34] across every single code base.
[0:00:36] Now one thing I find myself doing more and more
[0:00:39] is running these background tasks
[0:00:41] and booting up multiple instances
[0:00:43] of the GitHub Co-Pilot CLI.
[0:00:46] Now this thing has been updating all the time
[0:00:49] nearly every single day.
[0:00:50] They've recently added planning mode, cloud delegation,
[0:00:53] custom agents, sub agents, and so much more.
[0:00:56] So if you tried out the Co-Pilot CLI before
[0:00:59] and haven't picked it up in a while,
[0:01:01] give it another go and update to the latest version.
[0:01:03] I'll link to the change log below.
[0:01:05] Now I also build AI into my apps,
[0:01:07] often leveraging Microsoft Foundry
[0:01:09] so I can build and deploy AI at scale.
[0:01:12] But what if I wanted to actually integrate
[0:01:14] the GitHub Co-Pilot agent,
[0:01:17] the one that powers the CLI directly into my apps
[0:01:19] and services that I build for myself and for others?
[0:01:22] Like wouldn't that be a crazy concept
[0:01:25] directly have access to GitHub Co-Pilot
[0:01:27] through your own applications?
[0:01:29] Well that's exactly what the brand new Co-Pilot SDK
[0:01:32] enables you to do.
[0:01:34] You can integrate the Co-Pilot SDK into your apps
[0:01:37] to manage and communicate directly
[0:01:39] with the Co-Pilot CLI,
[0:01:40] pragmatically this is crazy.
[0:01:42] We're talking about full session management,
[0:01:45] access to models across all providers,
[0:01:48] tool calling, streaming results, and so much more.
[0:01:51] It unlocks so much potential of apps and ideas,
[0:01:55] leveraging the Co-Pilot CLI.
[0:01:58] Now this new Co-Pilot SDK just stealth launch
[0:02:01] into technical preview,
[0:02:02] and in minutes I started building and leveraging it
[0:02:05] to create some astonishing apps
[0:02:07] to really help streamline my workflow.
[0:02:09] So what I want to do today is take a look at it in action
[0:02:12] and what I built and how you can get started
[0:02:15] using the Co-Pilot SDK to leverage all of this power
[0:02:18] of the Co-Pilot CLI.
[0:02:20] So let's get into it.
[0:02:32] All right, let's go ahead and level set a little bit here.
[0:02:33] First you have a GitHub Co-Pilot.
[0:02:35] This is your main hub, this is your subscription,
[0:02:37] this is your AI Co-Pilot,
[0:02:39] to help you with all things software development.
[0:02:41] You've seen it inside a VS Code, Visual Studio,
[0:02:43] and Telije, all the places out there that I've talked about.
[0:02:46] And this really enables you to be hyper productive
[0:02:49] and pull in the latest and greatest,
[0:02:51] including MCPs, skills, agents, and so much more
[0:02:55] to iterate rapidly on your code base.
[0:02:58] Now beyond that, there's a bunch of agents as well.
[0:03:00] So of course you can plug into the GitHub coding agent
[0:03:03] to delegate work and assign to other agents as well
[0:03:06] that you have super focused on specific tasks.
[0:03:08] This is sort of the mission controller
[0:03:09] which I love doing and assigning work.
[0:03:12] And then you have the Co-Pilot CLI, right?
[0:03:13] And this is all part of the same GitHub Co-Pilot ecosystem.
[0:03:17] And nearly two basically have GitHub Co-Pilot directly
[0:03:20] inside of your terminal via the CLI.
[0:03:23] And you have the same exact things, MCP servers,
[0:03:25] skills, agents, all those goodies all inside of there, right?
[0:03:29] So it's all available, dipping, starting up different instances,
[0:03:32] a whole bunch of things.
[0:03:33] You can just have as many of them as you want.
[0:03:35] So let's first just take a look here, right?
[0:03:38] So here I am inside of my terminal
[0:03:40] and I'm inside of this, my switch library app that I've been building.
[0:03:44] I'm gonna say Co-Pilot.
[0:03:45] And then I'm also say dash dash banner here.
[0:03:48] So you can see the cool Co-Pilot banner come up.
[0:03:50] Boop, there it is.
[0:03:51] Cool.
[0:03:52] So the first thing we're gonna see here
[0:03:53] is like, do we trust the files in this folder?
[0:03:55] And I'm gonna say yes.
[0:03:57] So from here, I'm logged in.
[0:03:59] You can also do slash log in, log out there.
[0:04:02] And then you can just ask it anything.
[0:04:04] So you could say, can you give me an overview of this app, right?
[0:04:10] So this is that sort of normal experience here.
[0:04:13] This is going in, it's gonna take a look at the codebase
[0:04:16] in this interactive CLI experience.
[0:04:19] It's gonna understand the read me, the package JSON, the list here.
[0:04:24] And this is gonna say, this is my switch.
[0:04:26] It's a progressive web app, tracking switch games.
[0:04:29] And it gives me a bunch of overview of the architecture,
[0:04:32] including React app, Azure Functions backend,
[0:04:34] super base integration, and a lot more.
[0:04:37] Now I can do other things.
[0:04:38] So I could say, here's library.
[0:04:41] So I could say, what is this file all about?
[0:04:45] So you can reference files, give it context,
[0:04:48] obviously asked for modifications as well.
[0:04:50] So here, this is gonna break down the library page components for me.
[0:04:54] And then give me an overview of exactly what this page is gonna do
[0:04:59] and how it makes up the library inside of the application.
[0:05:03] Now beyond this though, we can do other things
[0:05:06] besides app mentions of different files.
[0:05:09] You can also use slash commands.
[0:05:11] So here we're at directories, we can browse like agents,
[0:05:15] we can obviously clear the conversation,
[0:05:17] compact the conversation, which it also does automatically.
[0:05:20] You can delegate the work as well.
[0:05:22] So we could delegate something off to the coding agent from here.
[0:05:26] You can share your entire session in a guest or a markdown.
[0:05:30] You can obviously log in log out, add MCPs, you have different models,
[0:05:34] plan mode, here in models, you can go in and just say, what model do you want?
[0:05:38] So whether it's a cloud model, a GPT model, a Gemini model, you're good to go.
[0:05:44] I could also come and say plan.
[0:05:46] So here I can implement kind of create a plan ahead of time.
[0:05:49] So say, how would I implement a NES theme in the app?
[0:05:55] So now this is gonna go into that plan mode agent, if you will,
[0:05:59] that we're sort of used to as well.
[0:06:01] So we're gonna say, all right, let's put this plan together.
[0:06:04] Again, it's gonna understand, ask me questions,
[0:06:07] understand the code base here, we're looking at the user preferences,
[0:06:10] understand the theming, and then it's gonna do some clarifying questions here
[0:06:15] for the different theme approach that's going on.
[0:06:17] Should it be NES, be a third theme, visual, scoping, and a lot more?
[0:06:22] So I could say here delegate, create, create, create the NES theme, and best pick options for me.
[0:06:37] There we go.
[0:06:38] So this is now gonna go off, it's gonna say, hey, we're gonna create a pull request
[0:06:42] based on your local changes and then you would draft pull request and it's gonna get to work, right?
[0:06:47] So now it's gonna summarize the conversation, start a copilot encoding agent session for me and get to work.
[0:06:52] So I could have it implemented locally on my machine, just right directly inside of here.
[0:06:56] Or I could go off and just fire this off and delegate and get onto something else.
[0:07:01] Okay, let's talk a little bit though.
[0:07:03] Now that you have a grasp of the CLI and the power inside of it, the actual SDK.
[0:07:08] So this is on getup.com slash getup slash copilot SDK.
[0:07:12] This is multi-platform SDK leveraging getup copilot agent into your apps and services.
[0:07:17] So it's available in node Python, go, and in C sharp for.net developers and you'd be good to go.
[0:07:24] And of course you need the copilot CLI.
[0:07:26] So from here though, this is sort of the architecture of how it works.
[0:07:29] You have your application, use integrate the client SDK and then over JSON RPC,
[0:07:33] it'll communicate back and forth with the copilot CLI that will be running in server mode on either your machine or some,
[0:07:41] remote connection external CLI server, whatever you have on it.
[0:07:46] And it's crazy simple.
[0:07:47] So if you go into any of the library, so here for.net, there's a test, there's a source,
[0:07:52] and you can take a look at it.
[0:07:53] So it's just a new get package getup.com.
[0:07:56] And this is really neat.
[0:07:58] You just create a copilot client, you start it up, and then you start a session.
[0:08:03] So in this case, I'm going to start a new session with GPT-5.
[0:08:07] And we'll actually see how to see all the different models as well.
[0:08:12] Here you get in on, so session.on, and you get different events in this queue that will just output different data.
[0:08:20] And then you'll set the result when it's done.
[0:08:22] So this idle event means it's done.
[0:08:23] And then you just send it questions over and over again.
[0:08:26] So you have this loop over and over again.
[0:08:28] And there's tons of stuff inside here.
[0:08:29] So you can get the path, I think it's the CLI arguments.
[0:08:32] If you want to use standard IO, the logging level,
[0:08:35] and restarts, environment variables, loggers, and a lot more.
[0:08:39] So you have tons of capabilities here.
[0:08:41] So here, there's tons to configure, such as models, tools that you wanted to call.
[0:08:46] You can list out available tools, different providers, including bring your own key.
[0:08:51] If you want streaming inside of it, you can just ping it.
[0:08:54] You do a whole bunch of stuff inside here.
[0:08:55] This is really, really cool.
[0:08:57] The power of this thing.
[0:08:59] So let's get back over to the CLI.
[0:09:01] This is probably delegating and doing some stuff.
[0:09:03] But I created a little hello world of the SDK.
[0:09:08] So I do this all in C sharp.
[0:09:09] So I'm going to say .NET run here.
[0:09:12] And what I wanted to do is sort of show off this interactive mode.
[0:09:16] So the first thing here, we're going to see it's a Copilot SDK interactive demo.
[0:09:20] All the source code will be available, put in the show notes.
[0:09:22] And it's going to say what models do you want.
[0:09:24] So here are the same exact models that we saw earlier in the Copilot CLI
[0:09:28] listing them out.
[0:09:29] So I could detect quad sawnet, high-coot,
[0:09:32] GPT here.
[0:09:33] So let's do GPT 5.2.
[0:09:37] Perfect.
[0:09:38] OK.
[0:09:39] Now from here, I've come up with a few different demos.
[0:09:42] So we can see that first.
[0:09:43] It has selected GPT 5.2.
[0:09:45] It's starting the session.
[0:09:47] And it's even going to ping it as a unique session ID here.
[0:09:50] So that's kind of cool.
[0:09:51] And we have some kind of code focus.
[0:09:54] I want to say, hey, imagine you're building your own sort of application
[0:09:59] on top of the CLI to help you triage your work,
[0:10:02] to performance your work, delegate out tasks,
[0:10:03] and do a bunch of stuff based on how your team works.
[0:10:06] And you're like, do your own stuff.
[0:10:08] Here, I can just type any message.
[0:10:10] I can type in a demo.
[0:10:11] I can change models.
[0:10:12] I can say what's 2 plus 2, question mark,
[0:10:16] and then it should hopefully come back with 4.
[0:10:18] So this is going to send it off.
[0:10:20] And boom, Copilot comes back 2 plus 2 equals 4.
[0:10:23] Cool.
[0:10:24] But let's look at some other things.
[0:10:25] Like maybe a code review.
[0:10:26] So you can maybe automate some code review happening on your machine.
[0:10:29] So I'm going to say demo 1.
[0:10:31] There we go.
[0:10:33] And now this is going to go off.
[0:10:35] It's going to say, hey, review this code.
[0:10:36] And this is doing a new database.
[0:10:38] It's doing query.
[0:10:39] And it's going to say, hey, listen, you can prevent SQL injection.
[0:10:43] Avoid creating a database per call.
[0:10:45] Dispose resources, async cancellation, user service.
[0:10:51] And actually gives you this code quality coming in.
[0:10:54] So you're going to get that same exact experience.
[0:10:56] But it's from my application that's streaming in automatically.
[0:10:59] And again, it's using my GitHub Copilot log in.
[0:11:04] It's using my account, which is nice.
[0:11:08] So let's do another one.
[0:11:09] You may be performance, for example.
[0:11:11] So I'm going to say demo 6.
[0:11:12] Demo 6 here.
[0:11:14] And this is going to go off and ask for just like best performance
[0:11:17] for improving a.net web application.
[0:11:19] And again, if you're just scripting, you're
[0:11:20] into like figuring this out.
[0:11:21] This is really crazy powerful to come in and create your own application.
[0:11:25] So this is going to show me exactly how to do performance improvements based
[0:11:29] on the knowledge tree that's coming in.
[0:11:30] I can provide additional comments, code suggestions, URLs.
[0:11:35] I could also come in and give it tools and MCP server.
[0:11:40] Like you can't like that up as well, which is awesome.
[0:11:43] OK, so we got to exit it out.
[0:11:45] And let's see exactly how that was created.
[0:11:48] So I'm going to come into VS code here.
[0:11:50] And what I want to show you is just kind of how easy it is.
[0:11:53] So this is the program.
[0:11:55] So we can see that a bunch of sort of ASCII artwork here.
[0:11:58] And the first thing we do is we have output some lines.
[0:12:02] And we do this CLI check for status.
[0:12:06] So again, what's cool here is that we're inside of this file.
[0:12:10] So I can check the copilot status.
[0:12:12] I can just check environment variables.
[0:12:14] See if the GitHub token is set.
[0:12:16] Else I can go off and see if it is installed.
[0:12:18] So I can go to definition here.
[0:12:20] And we can see that it's just going to start up a process.
[0:12:23] Look for copilot version and understand what's installed.
[0:12:26] Here it's going to double check to see if I'm authenticated
[0:12:29] or not inside of here.
[0:12:31] And then from there, once I have the status,
[0:12:33] it's going to select the model asynchronously.
[0:12:36] And the model selector, yeah, you guessed it,
[0:12:38] goes off and just kind of queries and sends the same command
[0:12:41] of dash dash model to the CLI to grab that back for me
[0:12:45] automatically so that I can select the model.
[0:12:48] Now, what's really cool here is that when I start the conversation,
[0:12:52] I'm able to go in, ping it just to make sure it has a connection.
[0:12:55] I create the session.
[0:12:57] I say I'm going to stream in the results.
[0:12:58] You saw it bobbin in there back and forth.
[0:13:01] And then I go in and I have this loop basically of going in
[0:13:04] and just reading the line and understanding what I want to select.
[0:13:09] So I don't want to select a new model.
[0:13:11] Do I just type something?
[0:13:12] Do I clear it?
[0:13:13] Or do I have a demo specifically in here?
[0:13:15] And when I select a demo, I just have the simple chat helper.
[0:13:18] And all it's doing is what we saw before.
[0:13:20] It has the copilot session.
[0:13:22] It's going to say session on.
[0:13:24] And then it's going to output.
[0:13:26] So there's delta events, main messages inside of here.
[0:13:30] We have some error logging.
[0:13:32] And then I just send the message off to it and stream the results back
[0:13:35] into my application.
[0:13:36] So it's really, really simple just to go off and pull all these in.
[0:13:40] And these demo prompts are just that.
[0:13:41] They're prompts, just like you would prompt anything.
[0:13:43] So we can see all the prompts that are going in pretty straightforward
[0:13:46] inside this one to just send that prompt off, give it additional context,
[0:13:50] anything I may need to send it.
[0:13:52] But let's talk about something a little bit more unique, right?
[0:13:55] Because if you have code, I could just do this in VS code.
[0:13:57] What about when to create an application leveraging the copilot CLI
[0:14:00] to do something that I do every single day?
[0:14:03] So something I do every single day for like merge conflict or the VS code
[0:14:06] podcast is a generate different titles, descriptions, YouTube chapters,
[0:14:12] and things like that.
[0:14:14] So I created a podcast and metadata generator,
[0:14:17] leveraging the copilot CLI.
[0:14:20] So if I go in, let me go in here and see what I have here.
[0:14:23] So we go into CD source.
[0:14:25] I've created a blazer web app and a council web app to show this off.
[0:14:31] So I'm going to go and boot up the council first.
[0:14:34] And let's say dot net run.
[0:14:36] Now this is using Spectre council.
[0:14:39] And this is going off.
[0:14:40] And here they have this podcast metadata generator.
[0:14:43] And we can see that I again have the CLI installed and it's ready to use.
[0:14:46] So inside of here, I'm able to do a few things.
[0:14:48] So I want to have very similar settings.
[0:14:50] So I can change the model that I want to use.
[0:14:52] It's using the same exact things.
[0:14:54] I'll use five to I can change output directories, podcast information,
[0:14:58] episode contacts or settings.
[0:15:00] So if I want to generate like eight different titles, for example,
[0:15:05] and I'll say maybe 15 words max, description, lengths, chapter settings,
[0:15:10] I have all these settings that are saved for me.
[0:15:12] So let me save settings.
[0:15:13] Let me go back here.
[0:15:15] And the power of this is I can load up a transcript.
[0:15:18] And then from that transcript, leverage the copout CLI through the SDK
[0:15:22] to generate all this stuff for me.
[0:15:23] So I'm going to say browse for files and I have one in here
[0:15:27] from the most recent merge conflict, which is a pretty deep dive episode.
[0:15:31] So there's a pretty long transcript.
[0:15:33] So I'm going to send this.
[0:15:35] I'm just going to say, do I want to add any contacts?
[0:15:36] I'm going to say no.
[0:15:38] And then from here, I can go ahead and generate all the metadata, generate titles,
[0:15:43] convert it's in SRT, generate descriptions.
[0:15:46] Let's go ahead and do title here.
[0:15:48] So again, this is now starting that session up.
[0:15:50] It's going to go and prompt off and then give that over to the copilot CLI.
[0:15:54] So now I have all of these inside of here.
[0:15:56] So this is all about CI CD for Mac app.
[0:15:59] So let's do this one.
[0:16:01] Cool.
[0:16:02] And then I can generate descriptions.
[0:16:04] So this is now going to go off and generate these descriptions in real time here.
[0:16:08] Like in the copy and paste inside of YouTube and fireside where I host the podcast.
[0:16:15] So here we can see everything coming in on these different descriptions.
[0:16:19] I can go in.
[0:16:19] I can view the results.
[0:16:21] I can view the titles that were here.
[0:16:23] I can view the descriptions that were here.
[0:16:26] I can go back and generate chapters, for example, that's a long one.
[0:16:29] That's a really complex process.
[0:16:31] So I'm creating these system prompts that go off and generate and do this work for me.
[0:16:35] And then it's going to come back and generate this, which is really, really neat.
[0:16:39] Like the ability to do this previously would mean I would need to spin up and
[0:16:43] talk to different APIs and spin up my own back end and foundry for example.
[0:16:49] But now I'm able to just send the prompts off leverage the CLI and then get it back.
[0:16:53] So we're able to get this all here.
[0:16:55] So this is really neat.
[0:16:56] Look at this.
[0:16:56] So not only the generate five chapters, it gave me sort of like,
[0:17:01] the YouTube chapters, a copy paste format here, which is really cool into seeing everything.
[0:17:08] And then from there, I can save the results, export it a lot more.
[0:17:11] But I didn't stop there because if we go into the Blazor one,
[0:17:16] I can dot net run that and I created a full web application.
[0:17:21] And this web application is you guessed it is a Blazor web app.
[0:17:25] So I'm just going to go ahead and tap on that.
[0:17:26] Let's go back over to Edge here, paste it in here, perfect.
[0:17:30] And we have this full podcast meditative generator.
[0:17:33] Now, as the Blazor server applications, it's a server.
[0:17:35] It can actually connect to the SDK to the CLI, but we can see the same exact thing.
[0:17:40] We have settings and we can see all of the different models here.
[0:17:43] And it's going to pick the same one that I had because it's legitimately like the same exact setting file
[0:17:49] that's shared between the two there.
[0:17:51] And then I can generate stuff.
[0:17:52] So let's go ahead and pick a file here.
[0:17:54] Let me go into that data file.
[0:17:56] I'm going to pick that transcript again.
[0:17:58] And then here we go.
[0:17:59] So now we have a visual overview.
[0:18:00] So let me just go ahead and do titles and short description and YouTube chapters as well.
[0:18:05] So now it's going to go off.
[0:18:06] I have this entire, this is communicating over the SDK
[0:18:10] to the CLI and it's going to pull these all in.
[0:18:12] We can see here are the outputs coming in, the generating, the chapters that are coming in in real time.
[0:18:18] Chapter stick a while because they're pretty complex.
[0:18:20] I would say, but it's coming in and I can see the results and I can toggle through them.
[0:18:24] This nice beautiful GUI.
[0:18:26] But what I love about this is that I'm using the same exact code between the council app and the web application
[0:18:33] and communicating directly to the CLI through the SDK.
[0:18:37] And the crazy part is I built all three of these applications under one hour, all using the GitHub
[0:18:45] Copilot CLI to generate these applications to communicate through the SDK to the CLI, which is crazy.
[0:18:51] So here are all the chapters coming in.
[0:18:53] I can see the descriptions coming in and then I can generate more or just go ahead and export these as well.
[0:18:59] So like this is just mind boggling to me to be able to come in, generate and create these powerful workflows,
[0:19:06] powerful AI applications that are leveraging the CLI in this type of way.
[0:19:11] And honestly as a developer, this is a complete game changer for me to be able to do this and create these powerful applications.
[0:19:19] So I just think that having all of these models at your fingertips directly through your GitHub Copilot subscription like this,
[0:19:27] leveraging the CLI with the SDK is crazy powerful.
[0:19:30] And you absolutely have to try it out to actually feel the power of this simple streamline SDK leveraging the absolute craziness of the
[0:19:40] Copilot CLI.
[0:19:41] All right, there you go.
[0:19:42] That is a look.
[0:19:44] And not only what the Copilot CLI is, but how you can start to leverage the power of the Copilot agent directly into your apps and services with the brand new technical preview,
[0:19:55] copilot SDK.
[0:19:57] The team is revving on this nonstop, not only on the CLI, but on the SDK and they want your feedback.
[0:20:03] So get to work start building some cool things.
[0:20:05] I started pulling this in and building in seconds.
[0:20:08] I'm going to link to all the repos below and all the change logs and everything that you need.
[0:20:12] And honestly, took an app to kind of leverage AI and put it in to production in
[0:20:18] honestly, 20, 30 minutes.
[0:20:20] It was mine boggling and have access to all those models at your fingertips, all leveraging your
[0:20:25] copilot subscription is absolutely astonishing.
[0:20:28] So anyways, check it out today.
[0:20:29] Let me know what you think in the comments below and get to building.
[0:20:32] So until next time, happy coding.
[0:20:34] Thanks for watching.
