---
video_id: 03CfGf9iw_U
title: "Completely understand hooks in less than 20 minutes"
url: https://www.youtube.com/watch?v=03CfGf9iw_U
channel: "@BurkeHolland"
published: 2026-04-14
speakers:
  - Burke Holland
topics:
  - hooks
  - agent-mode
  - runtime-enforcement
relevance: primary
---

# Completely understand hooks in less than 20 minutes

Burke Holland gives a concise walkthrough of GitHub Copilot hooks, focusing on where they attach in the agent loop and how they enforce behavior outside the model.

## Key Topics Covered

- **Hooks** — Life-cycle interception points for agent sessions
- **Guardrails** — Blocking or shaping risky behavior before execution
- **Agent loop** — How hooks relate to tool calls and session flow

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Let's talk about hooks.
[0:00:02] It's a new mechanism for tying into different places
[0:00:05] in the age of life cycle in the Co-Pilot CLI,
[0:00:08] Visual Studio Code, and other places like Claude Code.
[0:00:11] In this video, we're gonna jump into what in the world
[0:00:13] they even are, how they actually work behind the scenes
[0:00:16] and why I think one of them, but only one,
[0:00:20] might be the most important tool in your AI toolbox.
[0:00:23] So if you're ready, let's do it.
[0:00:25] All right, so let's just start with what happens
[0:00:29] when you engage in a chat with the agents.
[0:00:32] So the first thing that you do is you send a prompt to the agent.
[0:00:36] And then the next thing that happens is that
[0:00:39] the agent loop then starts.
[0:00:41] And what this looks like is the first thing that it does
[0:00:44] is thinking and reasoning, and you see all those tokens
[0:00:47] come back in the chat.
[0:00:48] And then the next thing that it does is it does tool calls.
[0:00:53] So these are things like reading files, writing files,
[0:00:57] executing bash scripts, and it may do some tool calls
[0:01:02] or images to one tool call.
[0:01:03] It just depends on whatever tool calls the agent decides
[0:01:06] it needs to do.
[0:01:07] And then what will happen is maybe the agent decides
[0:01:12] that it needs to launch a sub agent.
[0:01:14] And that sub agent is really doing the same thing as the agent.
[0:01:18] It's reasoning and then making tool calls.
[0:01:22] And these things here, it's important to note
[0:01:24] that the agent and the sub agent,
[0:01:26] these are actually loops.
[0:01:28] So what happens here is this agent runs and runs and runs
[0:01:32] until it doesn't have any more tool calls to make.
[0:01:36] And when it doesn't have any more tool calls to make,
[0:01:38] then it's done.
[0:01:40] That's what's actually happening.
[0:01:41] That's how the agent knows its finish
[0:01:43] is when there's no more tool calls.
[0:01:44] And the sub agent works exactly the same way.
[0:01:47] They're actually loops.
[0:01:48] So this thing just runs over and over and over again.
[0:01:50] And then at some point, right, at the end of this thing,
[0:01:53] you get this like response where it tells you what it did
[0:01:56] or it's done, et cetera, right?
[0:01:58] And so this is what the actual chat process looks like here
[0:02:04] or kind of like at a high level.
[0:02:05] How it works.
[0:02:07] Let's just connect some of these arrows here.
[0:02:09] So I feel good about this.
[0:02:10] Good.
[0:02:11] Now, what hooks allow you to do are to execute events
[0:02:15] at various points in this right here,
[0:02:18] which we might call the agent life cycle.
[0:02:19] And keep in mind that this may continue, right?
[0:02:22] So you may have another prompt down here
[0:02:25] at the bottom.
[0:02:27] And then you get another agent loop.
[0:02:29] So like this whole thing starts over again, right?
[0:02:33] And this may be to you.
[0:02:34] It's all the same chat session.
[0:02:36] And the context of all of what happened up here
[0:02:40] gets passed down in here as well.
[0:02:42] But this right here is essentially the agent life cycle.
[0:02:45] And so hooks allow us to execute
[0:02:47] some commands at different points, as we said.
[0:02:50] So the first one is when you start a new session
[0:02:53] and send your first prompt
[0:02:55] an event called session start fires.
[0:02:58] So that's the first one.
[0:03:00] And then every time you send a prompt,
[0:03:03] there is a user prompt submitted event that fires.
[0:03:07] And these are the hooks.
[0:03:08] They're really just events, but they're called hooks.
[0:03:11] So user prompt submitted.
[0:03:12] And it's important to note that this user prompt submitted
[0:03:14] will fire again, right down here.
[0:03:17] If you do another prompt, it will fire again
[0:03:18] whereas session start only fires
[0:03:20] after the very first message in a session.
[0:03:23] And then the next one that happens is before tool calls,
[0:03:27] before and after, we have pre tool use
[0:03:33] and then we have one after it.
[0:03:34] And that hook is called post tool use, post tool use.
[0:03:41] And then for our sub agents here,
[0:03:43] we actually have events for those as well.
[0:03:45] So there's a hook for the sub agent
[0:03:47] that sub agent start.
[0:03:50] And I believe one for sub agent stop.
[0:03:55] Okay.
[0:03:56] And then we have one event here at the very end
[0:04:01] right here at the response,
[0:04:02] which is basically session and session end.
[0:04:08] And then we have one more hook that fires just kind of,
[0:04:12] it doesn't really have a place in the life cycle
[0:04:13] just wherever this might occur,
[0:04:15] which is just, it's either on error or error occurred.
[0:04:19] I think it's error occurred.
[0:04:20] And this just fires whenever there's an error in here.
[0:04:24] So what these hooks allow you to do
[0:04:25] is that you can handle any one of these.
[0:04:27] And some of these hooks are blocking
[0:04:30] and some of them are not.
[0:04:31] So for instance, sometimes all you can do
[0:04:34] is handle what happened,
[0:04:35] but in the case of hooks like pre tool use,
[0:04:37] you can actually say, based on whatever you decide
[0:04:41] in this hook, yes or no,
[0:04:42] you may or may not call this tool.
[0:04:44] And that's gonna be powerful here
[0:04:47] in a minute we talk about that.
[0:04:48] Okay, so at a high level, that's how it works.
[0:04:51] Let's jump in and build our first hook.
[0:04:53] All right, so I'm in Visual Studio Code here.
[0:04:55] And I wanna use the CLI,
[0:04:57] but we're also gonna use the chat in Visual Studio Code.
[0:05:00] Hooks are close enough, almost identical
[0:05:03] in the CLI and Visual Studio Code
[0:05:06] that they work the same way in both places.
[0:05:08] And actually it's easier to test using Visual Studio Code
[0:05:11] and we'll see why that is here in just a second.
[0:05:13] So first, let's go to user settings
[0:05:16] and just look for hooks.
[0:05:17] And we wanna make sure that hooks are enabled
[0:05:20] because right now they are in preview.
[0:05:23] And then if you want to use existing cloud hooks,
[0:05:25] you can turn that on.
[0:05:26] And then this custom agent hooks,
[0:05:28] we'll talk about that here in a second.
[0:05:31] But it's important to note that like,
[0:05:32] where do you hooks actually go?
[0:05:34] Well, they're just JSON files
[0:05:35] and they can go in your project,
[0:05:37] which are these settings here,
[0:05:38] either under.github or.cloud folders,
[0:05:41] or they can go in global folders, right?
[0:05:43] This is on your user profile.copilot or.cloud.
[0:05:47] So with those settings enabled,
[0:05:50] let's go back here and on the agents one,
[0:05:53] you can at the time of this recording
[0:05:56] actually specify hooks directly in your agent.
[0:06:01] We should see that here, yes, we can.
[0:06:03] And so we can specify hooks
[0:06:04] that we want this particular agent to execute.
[0:06:08] We won't actually do this in this video,
[0:06:10] but just know that this is an experimental mode
[0:06:12] at the moment and you can do this.
[0:06:15] So let's go ahead and work on creating our first agent.
[0:06:19] So the first thing we're gonna wanna do
[0:06:21] is create in our GitHub folder,
[0:06:24] a new folder, let's call it hooks.
[0:06:27] And then we just need a JSON file to define our hooks
[0:06:31] and because we're developers,
[0:06:33] we're gonna do it hello world,
[0:06:35] and it's just a JSON file, that's all it is.
[0:06:38] Now, because we've created this JSON file inside this hooks folder,
[0:06:42] Visual Studio Code is gonna know
[0:06:44] about the format of this file.
[0:06:46] So I'm gonna control space
[0:06:48] and then we wanna set version to one
[0:06:50] and then we can start defining our hooks here.
[0:06:54] Now for our hooks here, let's go ahead and start
[0:06:58] and let's do the user prompt submitted.
[0:07:01] And we're gonna start with this one
[0:07:02] because it's just easiest to test
[0:07:04] because it's gonna fire every single time we send a prompt.
[0:07:06] So just super easy to test.
[0:07:08] And notice that you can have multiple handlers here
[0:07:13] for any hook, right?
[0:07:14] So you can have multiple hooks
[0:07:16] and you can have multiple handlers.
[0:07:18] Okay, so let's start with our first one here.
[0:07:20] We're gonna define our first hook.
[0:07:22] So first we need a type
[0:07:23] and the only type that is currently out there right now
[0:07:26] is command easy enough.
[0:07:28] And then basically what do we wanna do
[0:07:30] when this command when this hook fires?
[0:07:32] And so we have bash and PowerShell, right?
[0:07:35] Obviously for cross platform,
[0:07:37] I'm gonna choose bash for this video.
[0:07:39] If you're on Windows, you would probably choose PowerShell
[0:07:42] and you'll still have a bunch of requests.
[0:07:44] So let's just go ahead and check out
[0:07:47] the Hello World.
[0:07:49] Why not?
[0:07:49] Okay, now let's go ahead and see
[0:07:53] how this hook is actually executed.
[0:07:56] So I'm gonna go back to the CLI here.
[0:07:59] Let's go ahead and collapse this.
[0:08:01] And I'm gonna start in the CLI.
[0:08:04] All right, we're gonna switch to a smaller model
[0:08:07] because these are hooks
[0:08:08] and so we don't really need model performance.
[0:08:10] These things are deterministic,
[0:08:12] which means we get to decide when they fire,
[0:08:13] not the model.
[0:08:14] So we can use a very small model for this.
[0:08:16] So the first thing that I wanna do here
[0:08:18] is I'm just gonna say hi.
[0:08:20] And let's see what happens.
[0:08:22] Well, we don't see any output from the hook.
[0:08:25] And if we try it inside of the Visual Studio code chat here,
[0:08:30] let's see what happens.
[0:08:32] Well, we don't see our Hello World message.
[0:08:35] And the reason for that is because it doesn't show up here
[0:08:37] or here, but if we go to the bottom panel here
[0:08:41] and we go to Output and we can look at chat hooks,
[0:08:45] then we'll actually see the Hello World, right?
[0:08:48] So if I do this again, we get another entry here.
[0:08:52] Now notice that this only works for Visual Studio code.
[0:08:56] So if I come and put something here in the CLI,
[0:08:59] if I say hi, nothing actually happens.
[0:09:04] This request came from the chat.
[0:09:05] The CLI doesn't actually log anything.
[0:09:07] And that's why when you're doing hooks,
[0:09:10] it's just easier to test with the VS code chat here.
[0:09:13] So you can see your output here.
[0:09:15] The other way that we could do it here
[0:09:17] is we could just pipe this somewhere else.
[0:09:19] So we could say let's send this to log a session.log.
[0:09:26] Okay, so we're just gonna log this out to a file.
[0:09:28] And I'm gonna change my tab size here
[0:09:30] just to make this, okay, perfect.
[0:09:36] Now let's go back and I'm gonna collapse this sidebar
[0:09:39] and let's use the CLI.
[0:09:41] And I'm just gonna say hi.
[0:09:42] And where do you think that session file is gonna go here?
[0:09:45] It actually doesn't go anywhere.
[0:09:47] And that's another thing to know is that with the CLI,
[0:09:50] every time you make a change to a hook,
[0:09:52] you need to reload the CLI.
[0:09:54] And you can do that with slash new,
[0:09:56] but in the VS code chat, you don't actually have to do that.
[0:10:00] So I'm just gonna say, if I come back here and say hi,
[0:10:04] you can see the file is created right here in session.log.
[0:10:09] So the file is created at the root of the project.
[0:10:12] So if you don't otherwise specify,
[0:10:14] the root of the project is where it's looking.
[0:10:17] If you wanted to specify,
[0:10:18] you could come and say current working directory here,
[0:10:21] and we could change this.
[0:10:21] And if we said it's in.github slash hooks,
[0:10:26] now if we run this, let's go back.
[0:10:33] And if we say hi, now our session log actually shows up
[0:10:37] in the hooks folder.
[0:10:39] So this is important to understand the path.
[0:10:40] And this really confused me when I was putting this video together.
[0:10:43] It's what, where does this actually execute?
[0:10:46] And what does this current working directory do?
[0:10:49] So what it does is it basically just says,
[0:10:51] execute this inside of this folder.
[0:10:54] And when you do that, then it becomes relative.
[0:10:58] And that's important when using scripts.
[0:11:00] So let's talk about scripts
[0:11:01] because that's how you're gonna handle this.
[0:11:04] So obviously you can't put your whole bash command in here.
[0:11:07] That wouldn't make sense at some point.
[0:11:09] It would be way too long.
[0:11:11] So what you could do instead though,
[0:11:12] is you could create a folder.
[0:11:14] So let's go into GitHub and say new folder.
[0:11:16] And let's call it scripts here.
[0:11:17] And if we wanted to,
[0:11:18] we could even put this inside of the hooks folder
[0:11:20] to make this a little cleaner.
[0:11:23] Let's create a new file.
[0:11:24] Just call it Hello World.
[0:11:27] Hello World.sh.
[0:11:29] And this will be our bash script.
[0:11:31] And the first thing we wanna do
[0:11:32] is make this script executable.
[0:11:35] And now we can echo out something like,
[0:11:39] hello from the script, hello from the script file.
[0:11:44] And we can send that to our session log.
[0:11:49] Okay, so to call this then,
[0:11:51] what we need to do is come back here,
[0:11:53] remove all of this here,
[0:11:55] and then we just need to pass the location
[0:11:58] of the scripts.
[0:11:59] Now, this will work because we've already specified
[0:12:02] that we're in the hooks folder.
[0:12:04] So we can just pass a relative path to the scripts.
[0:12:07] If we didn't have this, this would fail.
[0:12:09] This would have to be like this.
[0:12:11] It would have to be dot GitHub slash hooks like this
[0:12:15] and then slash scripts.
[0:12:18] But because we had the relative path there,
[0:12:20] we can just pass slash scripts and this will work.
[0:12:25] So let's go ahead and run this.
[0:12:26] So we'll just say hi, we're saying hi a lot.
[0:12:28] Oh, and look, so this is good,
[0:12:30] I made an error and Visual Studio code.
[0:12:33] It's really good about this,
[0:12:33] where it says warning from the user prompt submit hooks.
[0:12:36] We can take a look at this and it says permission denied.
[0:12:39] Oh, interesting.
[0:12:40] So what's going on here?
[0:12:41] Well, in Bash, you have to make a script executable
[0:12:44] by changing its properties with CH mod.
[0:12:48] So let's go ahead and do that.
[0:12:50] Let's go to the terminal.
[0:12:51] And we can just change it to executable
[0:12:53] with the CH mod command there.
[0:12:56] So let's go back.
[0:12:57] Let's try our hook again, say hi.
[0:13:00] All right, and this time we did not get a warning,
[0:13:02] which means it executed successfully.
[0:13:04] So let's go to our session log here.
[0:13:06] And there it is.
[0:13:08] Hello from the script file.
[0:13:10] Now, for each of these hooks that you have,
[0:13:13] you're going to get some input from the hook itself.
[0:13:16] So in our script file here,
[0:13:17] let's just define a variable.
[0:13:19] And then what we want to do is just get the input
[0:13:21] and in Bash, we can do it just like this.
[0:13:24] And then what we want to do is just output this
[0:13:27] to the session log here.
[0:13:29] So we're just going to echo our input
[0:13:31] into the session log here.
[0:13:34] Okay, now let's go ahead and run again.
[0:13:37] I just say hi.
[0:13:39] And this time we should see, yep, there it is.
[0:13:42] So here's the JSON that gets passed in
[0:13:45] as the input to this script.
[0:13:47] Now, this is really hard to read like this.
[0:13:49] So there's a built-in tool in Bash.
[0:13:52] And there's probably one for PowerShell as well.
[0:13:54] That's called JQ.
[0:13:56] So let's come back here.
[0:13:57] We're just going to ask you pretty print the input
[0:14:00] and it will automatically use JQ to do that
[0:14:02] into our session log here.
[0:14:04] Let's go back and say hi.
[0:14:06] Come back to our session log.
[0:14:07] And now look at that.
[0:14:09] Look at how nice this is.
[0:14:10] So we're getting the hook event name,
[0:14:12] a timestamp, an ID, a transcript path,
[0:14:16] which is actually going to the chat transcript.
[0:14:18] So you can get the whole thing.
[0:14:20] What the prompt was and then the current working directory,
[0:14:23] which we've already talked about.
[0:14:25] So pretty much every hook gets the same thing.
[0:14:28] Some hooks get different things.
[0:14:29] You have to look at the docs for that.
[0:14:31] So when you're in a hook, you can do things
[0:14:34] like send things back out to the agent.
[0:14:38] So to demonstrate a real world use case here,
[0:14:41] what we're going to do is change this
[0:14:42] from user prompt submitted.
[0:14:45] We're actually going to do on session start.
[0:14:48] And on session start, what we want to do is
[0:14:50] we're going to rename this a little bit
[0:14:52] to get ENV here.
[0:14:54] So let's do that.
[0:14:55] And let's rename this hello world script here to just,
[0:15:00] let's just say get ENV like this.
[0:15:03] Okay, if we want to actually send something back,
[0:15:06] what could we send back?
[0:15:07] Well, perhaps we would want the agent to know
[0:15:10] about the user's node version without having to ask.
[0:15:13] So for instance, right now if I say,
[0:15:15] what version of node is this user running?
[0:15:21] It will try and run a bash command to figure that out.
[0:15:24] But we can actually inject that into the session
[0:15:27] as part of the context you can see is doing right there.
[0:15:29] So let's go ahead and stop that.
[0:15:31] So what we want to do here is first get the users node version.
[0:15:36] All right, there it is.
[0:15:37] And then to pass it back,
[0:15:39] we just need to pass back JSON in the right structure.
[0:15:42] And hook output looks like this.
[0:15:46] Now for this, we don't need all these fields.
[0:15:48] We need the event name,
[0:15:50] but we don't need this deny here.
[0:15:52] We can't actually deny the hook.
[0:15:54] We can't deny the session start.
[0:15:55] We can deny a tool call,
[0:15:58] but we can't deny session start.
[0:15:59] So we're gonna take this out.
[0:16:01] And we're gonna take out this updated input.
[0:16:03] It's just this additional context that we want.
[0:16:07] And because I already have this typed up,
[0:16:10] we want it in a special format here
[0:16:11] because we're working in bash.
[0:16:13] Let me just copy it in.
[0:16:14] It looks like that's we're using the JQ library here
[0:16:18] to format this as output.
[0:16:21] And we're gonna echo it back out just like that.
[0:16:23] But you can see here, hook specific output, right?
[0:16:26] Event name, session start, additional context,
[0:16:28] the user's node version is.
[0:16:31] And then we're sending it back.
[0:16:32] So we're injecting context into the agent session.
[0:16:35] So let's make sure we started a new one.
[0:16:37] We're on high Q4 5.
[0:16:39] And now let's just ask,
[0:16:40] what version of node is the user running?
[0:16:45] And this time it just answers immediately, right?
[0:16:47] There's no tool call
[0:16:48] because we injected that context into the agent.
[0:16:52] And that's pretty powerful.
[0:16:54] It's one of the common uses for hooks
[0:16:55] is to just inject content into the agent.
[0:16:59] Now, as I talked about at the beginning of this video,
[0:17:02] I do wanna show you where I think this is actually useful
[0:17:05] because I don't know that it's useful to me at least
[0:17:07] to log things or inject context.
[0:17:10] But the pre tool use hook is powerful.
[0:17:12] And I wanna show you how I used it.
[0:17:14] The whole problem with AI right now
[0:17:17] is that it is non-deterministic.
[0:17:19] In other words, we don't know what it's gonna do.
[0:17:21] and it lies pathologically.
[0:17:23] And so we need gates that we can force the model through
[0:17:27] that will ensure that it does what it said that it did.
[0:17:30] And the pre tool use hook is brilliant for this.
[0:17:33] So I created one that forces the model
[0:17:37] to write code that successfully lense
[0:17:39] in order to write the code with a pre tool use hook.
[0:17:44] And we can go through that here
[0:17:45] and look at the actual code.
[0:17:47] It's a little bit long here,
[0:17:48] but essentially it uses that JQ library
[0:17:51] to run ESLent on the changed file.
[0:17:53] And if it doesn't lint, then it denies the right.
[0:17:56] And the model has to keep trying until it gets this right.
[0:18:00] So if we look at some of the output here,
[0:18:02] this was a large run on this project here.
[0:18:04] And you can see that it's trying to write
[0:18:06] this firebase admin right here,
[0:18:09] but it keeps failing the lint right here.
[0:18:12] So lint errors must be fixed
[0:18:13] before editing other files right here.
[0:18:15] It keeps failing the lint.
[0:18:17] So it looks at this.
[0:18:18] And it keeps going.
[0:18:20] It has to fix the lint errors.
[0:18:21] So it goes back, does some research.
[0:18:23] Try is again, fails again.
[0:18:25] Then it goes back and says,
[0:18:26] well, I gotta fix this,
[0:18:27] tries again, and it fails again.
[0:18:30] And it just keeps doing this
[0:18:31] until it gets it right in the file actually lint.
[0:18:35] And I think this is brilliant
[0:18:37] because this forces the AI to write code the way you would,
[0:18:42] which is that you write the code.
[0:18:43] And if there's red squigglies under it,
[0:18:45] you don't move on, you fix the errors.
[0:18:48] But AI will move on and just rationalize
[0:18:50] why that error is okay,
[0:18:52] or fix it in some hacky way.
[0:18:54] But the pre tool use hook forces it
[0:18:56] to write lintable code.
[0:18:59] And I think that's brilliant.
[0:19:00] I'm doing this on all of my projects now.
[0:19:03] I don't trust the AI to lint or test its code after it's done.
[0:19:06] I want it linted at the time that it writes the file
[0:19:10] or it cannot move on.
[0:19:11] You can't do anything else until it fixes that issue.
[0:19:14] That's your rundown on hooks in the Copilot CLI
[0:19:17] and Visual Studio code.
[0:19:19] You can use those today.
[0:19:21] Some of them are in experimental mode.
[0:19:23] So make sure you have all of that stuff toggleed on.
[0:19:25] But thanks for watching.
[0:19:27] And as always, happy coding.
