---
video_id: os2eqa69gko
title: "Mastering AI with VS Code's New Agent Customizations"
url: https://www.youtube.com/watch?v=os2eqa69gko
channel: "@JamesMontemagno"
published: 2026-04-07
speakers:
  - James Montemagno
topics:
  - custom-agents
  - skills
  - instructions
  - prompts
  - hooks
  - mcp
relevance: primary
---

# Mastering AI with VS Code's New Agent Customizations

James Montemagno demos the unified chat customizations surface for agents, skills, instructions, prompts, hooks, MCP servers, and plugins in VS Code.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Chat Customizations Intro |
| 01:23 | Unified Customizations Panel |
| 02:27 | Agents Overview |
| 03:07 | Create A New Agent |
| 04:59 | Skills And Extensions |
| 05:33 | Instructions And Prompts |
| 08:51 | Hooks Automation |
| 10:03 | MCP Servers Marketplace |
| 11:12 | Plugins Bundles |

## Key Topics Covered

- **Custom agents**
- **Skills**
- **Instructions and prompts**
- **Hooks and MCP**

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Vias code is your home for agentic development and his packed full of different capabilities to help you boost your AI development such as you know custom agents skills
[0:00:10] instructions prompts hooks plugins and so much more and the brand new chat
[0:00:15] Customizations brings them all together into a central location and there's streamline ways to create them all with AI as well
[0:00:23] So what I want to do today is dive into this brand new feature and capability
[0:00:27] They're really streamlines the entire process and really helps you in every single data development. So let's get into it
[0:00:33] All right here. I am inside of Vias code
[0:00:45] I'm in one of my Azure functions which actually runs the GitHub a change log
[0:00:50] So this actually does automation and calls out to Microsoft foundry a whole bunch of goodies now previously
[0:00:56] If you were looking to set up your chat customizations
[0:00:58] You'd have to go through this dot and get up folder inside of here
[0:01:01] We'd have things like agents instructions prompt skills
[0:01:05] And of course your other get up things like workflow is for example now on top of actual
[0:01:11] customizations inside of
[0:01:13] The actual project you might have sort of user setting different
[0:01:17] Agents or instructions or prompts as well and you have to go figure out where those are at and bring them all together
[0:01:23] Well now you can just go into this gear over here
[0:01:25] Which is going to be in the chat and you'll see open customizations and when you do that
[0:01:30] You're going to see the brand new chat customization. I'm going to make it pretty big here just so we can zoom in and see it
[0:01:36] And what we're going to see on the left hand side are agents
[0:01:39] skills
[0:01:41] instructions
[0:01:42] prompts
[0:01:43] hooks
[0:01:44] MCP servers and plugins now I'm not going to walk through all of them inside of here
[0:01:49] And if you want to break down of these different things
[0:01:50] I'll actually link over to Kila cinnamon's video on this. It was absolutely epic
[0:01:55] So definitely check that out
[0:01:56] But I also want to point out here that you are able to see local
[0:02:01] Copilot CLI and cloud as well
[0:02:03] So these are able to bring these all in and that's the cloud code agent inside of the chat agent here as well
[0:02:10] So you can see that here. So if you're wondering when you come down here under local
[0:02:14] You'll see copilot CLI and then you'll see cloud as well
[0:02:17] So that means that you're able to see all of those customizations and you're even to see which ones are available just for the copilot
[0:02:23] CLI and what are available there. So that's really really nice
[0:02:26] I'm going to focus on local here
[0:02:28] But what we can see is at first we have agents
[0:02:30] And I want to break down here and show you that they're not just ones that are inside of your folder
[0:02:34] And this was so important about this chat customization it is showing me here at the custom agents that I have the debug mode
[0:02:40] I tap on that I can see the deep debug mode to come in here to actually solve problems on it in that specific agent
[0:02:48] Task researcher and then we're going to see some that are from extensions and that are built in
[0:02:53] So here of course we see that I have the dotnet upgrade assistant modernization tool thingy here
[0:02:59] That gives me ways to easily migrate my projects
[0:03:02] And then I have built in one such as ask explore which is a sub agent and plan
[0:03:07] I can come over to the top right and I can see that I can generate an agent
[0:03:11] Which is using an AI prompt or here I can say new agent here as well
[0:03:16] So if I say new agent it's going to bring me over into the chat over here
[0:03:21] And you can see slash create and it's going to say what job should this agent do and how I'll say this agent should only
[0:03:29] focus on
[0:03:31] Azure functions in c sharp
[0:03:35] I'm going to send that off
[0:03:37] Now what this is doing is this is sending off a prompt and in fact if you go back to the chat
[0:03:41] Customizations and you go to prompts
[0:03:44] We can see that if I go down to built in we have a bunch of prompts that are from the team
[0:03:48] Such as create agent create hook create instructions create prompt create skill and my favorite in it
[0:03:54] And of course plan as well
[0:03:55] So there's all these ones that are built in
[0:03:57] Now if we look at that create agent
[0:03:59] We can see exactly what the VS code team had in mind here
[0:04:02] So what it's going to do is it's going to create a custom agent for a specific job
[0:04:06] And it's going to ask you specifically what job to do
[0:04:09] It's going to go find a bunch of things specifically here clarify needs and create a custom agent for me
[0:04:15] So let's see
[0:04:16] So it says should this agent appear
[0:04:19] only
[0:04:20] In the agent picker or sub agent only I'm going to say show and picker only
[0:04:25] Do you want the terminal execution enabled? Yes
[0:04:28] Let's say refuse out of scope here
[0:04:31] And then it's going to go and create my agent file for me automatically
[0:04:34] So this is really really cool
[0:04:35] So if you're looking to have a customization especially if one one that already knows and understands your code
[0:04:42] You can go ahead and create that
[0:04:43] So this is going to have and created a brand new one for me
[0:04:46] So let me go back to chat customizations
[0:04:48] Back to agent I have my c-sharp azure function specialist here
[0:04:53] Just gives me a bunch of information here which is really really nice
[0:04:55] I could go ahead and refine that add more information
[0:04:59] Now let's go dive into skills here because these again are coming not only from the workspace
[0:05:03] So these are ones that are in the project
[0:05:05] And I can see that I can go over
[0:05:06] And I can copy the path to this or I can delete this right from here
[0:05:10] I can see that here I have some that are coming from plugins that I'm using such as the co-pawd SDK
[0:05:16] Some from the .NET plugin system here and some from extensions
[0:05:20] So if you've been wondering oh what skills or have available or what are 17 skills
[0:05:24] Well extensions can contribute skills or instructions or prompts
[0:05:28] And we see a bunch that are plugged in here as well such as troubleshoot for example
[0:05:33] Same with instructions
[0:05:34] Here we have two different instructions one for the main agent instruction
[0:05:39] And one that is specific guidance
[0:05:42] Based on just like c-sharp so I have a c-sharp function guidance here that I've given given this as well
[0:05:48] That is scope to specific context
[0:05:52] And then again I can tap on one of those I can see everything that goes into there
[0:05:55] And of course I can go in and I can create a new instruction
[0:05:58] A new instruction for the user space or even a new agent's .md file as well
[0:06:03] If you're using multiple agents as well and don't want to cope out of the instruction
[0:06:07] You can do that and of course if you hit this button here
[0:06:09] This is going to auto generated as well for you which is super nice
[0:06:12] Same with prompts prompts are all built in I have a bunch here
[0:06:15] I have a bunch of different work items and azure devops
[0:06:18] And I have a bunch of prompts here to help me specify those
[0:06:21] So I can go in see all this information
[0:06:23] Like you would expect as well
[0:06:25] And then create one as well which is really nice
[0:06:27] I do want to point out one here which is in it which is built in from the team
[0:06:31] This is really really nice and something that you can use over and over again
[0:06:35] as your project evolves and what this will do is it will continuously either create
[0:06:40] Or update workspace instructions for ai coding agent so over here as well
[0:06:45] So this will create this here either in your kobob instruction or agents.md
[0:06:50] So if I come back over here into my chat
[0:06:53] And I just say slash in it
[0:06:56] I'll say update my instructions based on recent
[0:07:01] Changes to the project
[0:07:04] Now what's great here is that this is going to go off
[0:07:06] It's going to go take a look on that system prompt
[0:07:08] So if we take a look here again at that slash in it
[0:07:12] We can see that we have a discoverability of any conventions
[0:07:16] It's going to explore the codebase
[0:07:18] Breakdown different functionality generate or merge iterate
[0:07:21] It's going to ask for feedback clarify those different instructions as well
[0:07:25] And now it's going through and seeing if there's anything that needs to be updated inside of here
[0:07:30] So this is a really really cool understanding what's in the project
[0:07:33] So as your project evolves or maybe add more projects
[0:07:37] That may be our for tasks or for something else
[0:07:39] You want to update these different instructions
[0:07:41] And the team has really been focusing and narrowing on making nice tight
[0:07:46] Instructions specifically for those co-opilot instructions or agents.md
[0:07:52] So I'm going to add a lot of those cook here
[0:07:53] And let's see the update that it has
[0:08:04] Okay, perfect. Here we go
[0:08:05] So here we can see that it updated a little bit here expanded manual validation guidance
[0:08:11] Let's take a look at the changes here pretty minimal
[0:08:13] But it added a little bit of code specifically that you know if there's automated tests gave it additional data clarification
[0:08:19] Different posting modes which is very very nice and anything that might have been a little outdated there
[0:08:25] We can also see if we keep scrolling that it gave us some important notes
[0:08:29] Maybe to continue further on
[0:08:31] See it says here that there's a new function like should we ignore that
[0:08:34] Should we do something else on it and then it also gives us these
[0:08:38] Suggestions for the next customizations like create instructions for the notify or flow or validate flow or change log formatting for example
[0:08:45] So this is really really nice that it's automatically giving me hints on maybe what I want to do next
[0:08:51] Alright, let's pop back over here into hooks now
[0:08:53] I actually don't have any hooks here and hooks allow you to go in
[0:08:58] And actually create different lifecycle events
[0:09:00] So if I say create hooks here
[0:09:02] I could for example say
[0:09:04] Let's create a hook when
[0:09:07] this finishes
[0:09:11] Turn to prompt me to
[0:09:14] Commit the code right and if I go ahead and look at my different hooks in my project
[0:09:21] So if I go over here
[0:09:22] I can see that I can say configure hooks
[0:09:25] And I have a bunch of different hooks for both local and the co-pile Cli
[0:09:29] And ones that are unique as well. So whenever the session starts
[0:09:32] User prompt has been submitted
[0:09:34] pre-tool use post-tool use sub agent stops and can even see compaction events as well
[0:09:40] So those are pretty advanced. I haven't really doubt dove deep into the
[0:09:44] Hooks yet
[0:09:45] But we can see that it's going to go ahead and create this hooks file for me
[0:09:48] And you could also just ask it what hook should you create for example
[0:09:52] So here it's going to remind me
[0:09:54] You know to do a commit on stop for example and go ahead and rev that for me
[0:09:58] Which is really really nice and they can run different scripts. So that's pretty cool
[0:10:02] Alright, let's dive back in while that's finishing up
[0:10:05] And I want to show off mcp servers and plugins because there's some unique functionality here
[0:10:10] First we can see that I have my github and my Microsoft docs mcp server
[0:10:14] And some coming from the extensions for the co-pilot mod for dot net
[0:10:19] I can go ahead and right-click on this for example
[0:10:22] It's coming in on the user space and I can disable this for the workspace
[0:10:25] If I want to that's really nice if you had a global mcp server
[0:10:29] You can disable it for a specific workspace if you desire
[0:10:32] Right from there and you can also start you can show the configuration configure model access and a lot more
[0:10:38] You can of course add one which will bring this up and did you know that you can drag this around if it's up here
[0:10:43] You can move it to the middle for example
[0:10:45] Where is where I like it and it'll snap. That's pretty cool
[0:10:47] You can go and add it
[0:10:49] You can also browse the marketplace which will show you all of the different mcp servers coming from the github registry
[0:10:55] So things like playwright
[0:10:57] Unity fire crawl
[0:10:59] notion the azure mcp server super base and a lot more
[0:11:03] So if you want to just go through dive through you can one-click get more information
[0:11:08] Install or install on the workspace, which is super cool
[0:11:12] Now finally I'll show off plugins because there's some additional functionality here too
[0:11:16] Plugins are sort of like a collection of different agent skills and instructions prompts hooks and all these things together
[0:11:22] You can get so for example if I go over here and I said
[0:11:26] .net slash skills
[0:11:28] That's a repo that has a bunch of different plugins available
[0:11:32] Once for.net data diagnostics. I'm a spill nugit upgrade Maui AI and a lot more to this is ever growing
[0:11:40] You can see that I have some installed here
[0:11:42] I can also enable or disable these for the workspace for example
[0:11:45] Like for example here I might go in and say you know what I can disable this for the workspace
[0:11:50] Because I'm not using the co-pilot SDK in this project
[0:11:52] So I can manage that right from here
[0:11:54] I can also browse the marketplace
[0:11:56] So I can add things like work IQ and different azure ones and awesome co-pilot
[0:12:00] And a bunch of ones that are coming here from different sort of plug-in marketplaces
[0:12:05] You can add your own marketplace
[0:12:07] So if you want to dad like I think there's like the Versalomarket place or the
[0:12:10] The skills different marketplace out there you can add them as well and pull them in which is super cool
[0:12:15] And it really brings these all together
[0:12:18] And again, you can dive through for the co-pilot CLI or cloud
[0:12:21] This is really going to be your home for all things with the chat and AI together
[0:12:28] And I really absolutely love it
[0:12:29] Not only is it just here's what it is
[0:12:31] But you can dive in deeper and understand exactly everything that's going on
[0:12:35] Make modifications here
[0:12:37] And of course you can even make a full screen pop it out
[0:12:39] Do whatever what you want which is so so nice when working with this
[0:12:43] And that is a complete overview of chat customizations
[0:12:46] I love it dive through it and definitely give the team feedback
[0:12:50] All right, there you go
[0:12:50] That's the brand new chat customizations available today inside of VS Code
[0:12:55] All you got to do is hit that gear and you are off to the races
[0:12:58] I love this thing and not only does it give you that unified view
[0:13:02] But at the same time you are now easily able to browse the different MCPs or plug-ins for example
[0:13:08] And even easily create them and prompt create them as well
[0:13:12] I really love this
[0:13:13] And I'm starting to see these different sort of slash commands come up
[0:13:16] And be prompted after I create one thing inside of the chat
[0:13:21] And every single time I do this it really helps me streamline my process
[0:13:24] So if you're looking to get started hit that gear button
[0:13:27] But even before that just do slash in it on your project
[0:13:30] It's going to take care of everything for you to set up those custom instructions
[0:13:34] And walk you through some other chat customizations
[0:13:37] All right, that's going to do it for this video if you liked it, thumbs up,
[0:13:39] Jam that subscribe button
[0:13:41] And until then, happy coding and thanks for watching
