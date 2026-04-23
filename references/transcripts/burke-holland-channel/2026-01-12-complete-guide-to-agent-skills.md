---
video_id: fabAI1OKKww
title: "The complete guide to Agent Skills"
url: https://www.youtube.com/watch?v=fabAI1OKKww
channel: "@BurkeHolland"
published: 2026-01-12
speakers:
  - Burke Holland
topics:
  - skills
  - prompts
  - instructions
  - custom-agents
relevance: primary
---

# The complete guide to Agent Skills

Burke Holland explains Agent Skills and how they fit alongside prompts, instructions, and custom agents.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Intro |
| 00:28 | Enabling Skills |
| 01:39 | Your First Skill |
| 09:11 | How skills actually work |
| 16:28 | Using pdf skill |

## Key Topics Covered

- **Skills**
- **Prompts**
- **Instructions**
- **Custom agents**

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Agent skills are here for Visual Studio Code.
[0:00:03] And if you're like me, you hear that and you think, please, please stop making me learn new things, please.
[0:00:12] I just want to live my life.
[0:00:14] The good news is, agent skills are actually pretty simple to understand and pretty powerful.
[0:00:19] So in this video, we're going to jump in, take a look at what they are, how they work.
[0:00:23] We'll build one together and then I'll explain the difference between skills and prompt files and instructions and custom agents.
[0:00:30] Let's do it.
[0:00:32] So skills at the most basic description are just another way to
[0:00:37] and provide instructions to the model.
[0:00:40] But they have some benefits over things like custom instructions in that they can bundle together
[0:00:46] scripts and templates in a bunch of different files to define a skill.
[0:00:50] And this doesn't make a lot of sense until you see when an action or build one, so let's do that.
[0:00:55] Now, the first thing we're going to need to do is we're working in Visual Studio Code,
[0:00:59] but we should point out that skills are a spec from an topic.
[0:01:03] And so they work in Cloud Code and other places.
[0:01:07] But here, we're all co-pilot all the time.
[0:01:09] Skills are also experimental at the time of this recording.
[0:01:12] So there will be some changes.
[0:01:14] But you can see here, you just need to toggle on skills and they won't be on by default.
[0:01:20] So if skills aren't working for you, make sure you toggle this on.
[0:01:22] Now, skills, like we said, are just other instruction files.
[0:01:27] That's really all they are.
[0:01:28] And so they just need to be in the right place.
[0:01:30] You can put them in GitHub skills, co-pilot skills,
[0:01:33] Cloud skills, the Cloud skills at the root of your project.
[0:01:37] And so for us, since we have an empty project here, let's just start like this and create a new
[0:01:42] folder.
[0:01:42] I will call it GitHub.
[0:01:44] And inside of that, we're going to put a skills folder.
[0:01:46] And then inside of that, we're going to create a skill and we're going to call it the Hello World
[0:01:49] skill.
[0:01:50] Yes, yes, doing Hello World.
[0:01:54] And then inside of this Hello World folder to define our skill, we're going to create a new file.
[0:02:00] And we just call it skill.md, just to mark down file here.
[0:02:05] Now, this file defines the skill.
[0:02:07] And there's some things that are required in this file.
[0:02:10] And that is some metadata at the top here.
[0:02:13] So you need a name and you need a description.
[0:02:16] And these things are required for the skill you have to have them.
[0:02:20] So I've added a name and a description here.
[0:02:22] And it's good to be descriptive as possible with the name and the description
[0:02:26] because of the way that skills are loaded and used, which we'll look at here in a second.
[0:02:32] Because the agent should have to pick these things up automatically when it needs them
[0:02:35] without you having to tell it in the chat, hey, you need to use this skill.
[0:02:40] Now that we have the metadata here, the next thing you want to do is start writing the
[0:02:44] instructions that give the skill to the model.
[0:02:48] So let's just start like this.
[0:02:49] We'll just say this is the Hello World skill.
[0:02:51] Use Hello World skill to respond to the user when, oh, and it's fixing my grammar for me.
[0:02:58] When they enter the phrase, hello world in the chat.
[0:03:00] And then when they do that, we want to respond with, and then we can say,
[0:03:07] hello world, this is my first skill.
[0:03:09] Yeah, that would work.
[0:03:10] Or even better, even more fun would be respond with, um, hello world.
[0:03:16] An asked yard.
[0:03:18] Much more fun.
[0:03:19] So let's try this here.
[0:03:21] Now we have created this skill.
[0:03:23] How do we actually use this?
[0:03:25] We'll open our chat and then in chat, let's just ask the chat what skills do you have?
[0:03:31] And we're going to make sure this is not attached.
[0:03:34] It is not attached.
[0:03:35] So let's send it and the model will look and examine and see if it has any skills here in the
[0:03:43] current workspace and then should report back and tell us exactly what the skills are.
[0:03:47] So my back says to domain specific skills, hello world is simple skill that responds when you
[0:03:52] enter the phrase, hello world.
[0:03:54] And then it's checking for additional skills, which we do not have.
[0:03:57] Thank you, Claude.
[0:03:58] You've done enough.
[0:03:59] Now, how do we actually use this skill?
[0:04:02] Well, all we should really have to do is say hello world, right?
[0:04:06] Because the point of skills is that they get picked up automatically by the model and it
[0:04:12] knows when to use the skill.
[0:04:14] So you can see here it says, I've read the hello world skill instructions and we'll respond
[0:04:18] appropriately and then we get hello world and ask yard, not bad.
[0:04:21] That's some pretty good ask yard.
[0:04:23] Now we could have done this in an instructions file.
[0:04:27] Yes, or a prompt file.
[0:04:29] Yes.
[0:04:29] So what's special about skills?
[0:04:32] So as we talked about skills, allow you to bundle a bunch of different files together.
[0:04:36] So in order to understand that, we kind of need to build something out here, make this a little
[0:04:40] bit more complicated.
[0:04:42] So in our skill file here, what I want to do is I want to have a script here.
[0:04:50] So what I want to do here is just get info about the users OS with OS, which is the node package
[0:04:58] for doing that.
[0:05:00] And I'm going to use haiku for this.
[0:05:01] I kind of like haiku.
[0:05:03] I think haiku gets a bad rap.
[0:05:05] Fast, accurate, perfect.
[0:05:07] Okay, so look, platform type release and architecture.
[0:05:11] I like it.
[0:05:12] So let's go ahead and keep this here.
[0:05:14] And then.
[0:05:16] So what we could do is say, you know, here's the workflow that we want this thing to follow.
[0:05:22] Workflow step one.
[0:05:23] Run the following scripts.
[0:05:28] To get system information.
[0:05:31] Respond with hello world and ask yard is step two.
[0:05:34] And then step three is provide the system information obtained from the script.
[0:05:39] So now we have kind of a workflow here.
[0:05:41] So we should get something a little bit more interesting.
[0:05:43] We do our hello world.
[0:05:44] So let's try this again.
[0:05:46] Hello world.
[0:05:47] And now.
[0:05:50] The skill should walk through our workflow and different.
[0:05:53] Do the different things that we've defined.
[0:05:56] Namely running the script in the terminal, which you can see it's doing right here.
[0:06:01] And then returning.
[0:06:03] Ask the art for hello world and then returning the system information as part of the hello world response.
[0:06:09] Let's see if we get all that and we do.
[0:06:10] So here's hello world.
[0:06:11] This is exactly what we asked for in the skill.
[0:06:13] Now in this format, this works just fine because there's just not a lot to it.
[0:06:19] But you can imagine if this was a really long skill, like we're teaching the AI maybe about
[0:06:24] how to write API endpoints for a company, this could start to get really long.
[0:06:28] And so what skills allow you to do is kind of modularize.
[0:06:31] So we're going to create a new folder here and call it scripts.
[0:06:33] And then inside of it, we're going to add a new file here called getls or get system info.js.
[0:06:42] And then we can add this information here, this whole script can come out and go into our script here.
[0:06:49] Right.
[0:06:50] And then we can reference that.
[0:06:54] We can reference this script with relative syntax relative path syntax, just like you would reference
[0:06:59] a normal mark, mark down file.
[0:07:01] So we can say run the script like this.
[0:07:05] Right.
[0:07:06] And then where's the script?
[0:07:07] The script is here in scripts and then get system info to obtain system information,
[0:07:13] respond with Hello World and ask yard and provide this system information obtained from the script.
[0:07:18] So now let's run this again.
[0:07:23] And we get the exact same thing, but this time it runs the script from the directory instead
[0:07:27] of having an inline end, the script.
[0:07:29] Fabulous take this a step further.
[0:07:31] And let's say that we want to have a template.
[0:07:35] So I'm going to create a new file here and we're just going to call it template.
[0:07:38] You don't have to capitalize these.
[0:07:40] This is just a pattern that you'll see a lot, but you don't have to capitalize.
[0:07:44] And then here we just have a template for a Hello World response in chat with system info.
[0:07:53] Let's see what a co pilot gives us here.
[0:07:55] Hello, you triggered the Hello World skill.
[0:07:57] Oh, look, ask yards coming in like that.
[0:08:01] It knows that we need this.
[0:08:02] Here's your system info.
[0:08:04] System info is here and then maybe like feel free to ask.
[0:08:07] Okay, right.
[0:08:08] So this is every time we hit Hello World, we want the model to respond with this format and only
[0:08:16] this format, right.
[0:08:17] And we could do that by coming into our skill and saying respond with respond with
[0:08:26] the template.
[0:08:30] And then again, we can just use that relative path syntax right here.
[0:08:35] And then here, we don't need this anymore.
[0:08:38] Right.
[0:08:39] So now we're getting the operating system info from the script,
[0:08:43] reusing the template to define what the response looks like.
[0:08:46] Let's give it another shot here.
[0:08:48] Right.
[0:08:48] There we go.
[0:08:49] Hello World.
[0:08:51] And look at that.
[0:08:52] We get it back in exactly the format that we defined.
[0:08:55] Hello, you've triggered the Hello World skill.
[0:08:56] Here's the ask yard.
[0:08:57] Here's your system information.
[0:08:59] Please feel free to ask if we need any further assistance.
[0:09:02] Right.
[0:09:02] The models are really, really good at following the skill and following our template,
[0:09:06] which is exactly what we've defined right here.
[0:09:09] So in a nutshell, this is what skills look like.
[0:09:14] Now you can do a lot of things here.
[0:09:16] Like you could provide your database schema in a markdown file or some other file and pass that
[0:09:20] into the skill.
[0:09:21] You can have multiple scripts in your skill.
[0:09:24] The possibilities are endless.
[0:09:26] Now, one of the interesting things about skills is that they're sort of progressively loaded so
[0:09:30] that they don't take up a lot of room in the context window.
[0:09:32] And in order to understand that, we need to have a look at the chat.
[0:09:37] So let's go to our chat debug view.
[0:09:39] And then we want to come all the way down to the bottom.
[0:09:41] And let's take a look at our Hello World, which starts right here, not there.
[0:09:45] But here, you can see Hello World.
[0:09:46] It's continued here.
[0:09:48] And then it looks like it's continued down there.
[0:09:49] So if you haven't watched my video on prompt files, instructions, and custom agents,
[0:09:54] I break down the system prompt in that video.
[0:09:57] That video.
[0:09:59] Anyway, you should watch that.
[0:10:01] But this is the system prompt.
[0:10:03] I'm going to scroll all the way down to the bottom.
[0:10:05] At the very bottom, what we'll see here is right here, you'll see skills.
[0:10:18] Here's a list of skills that contain domain-specific knowledge.
[0:10:21] And you can see the skill that we get here.
[0:10:23] It's Hello World.
[0:10:23] So it's just the name and the description and then a path to the file.
[0:10:27] So when you pass a request to the model, any skills you have are passed here.
[0:10:32] But none of the other files that we've defined are passed.
[0:10:37] Nor is the body of the skill.
[0:10:39] Only this right here gets passed on that first agent pass.
[0:10:44] Now on the second agent pass, let's go back to our debug view here.
[0:10:52] If we scroll all the way down to the bottom, we can see that the agent responds with,
[0:10:56] okay, I need to read the skill instructions and respond appropriately.
[0:11:00] And this is the file path that it needs to read.
[0:11:02] It wants to read the skill dot MD file.
[0:11:06] And it does that.
[0:11:06] That's a very next thing it does is it reads that file.
[0:11:09] And then if we come down again, so we're looking at the system prompt, the whole agent turn.
[0:11:14] So it calls it, right?
[0:11:16] It puts it's now in the prompt here as a tool call.
[0:11:22] You can see the response from the assistant is that it has read.
[0:11:26] And now it knows that it needs to run this script to get the terminal output,
[0:11:30] which is the very next thing it does.
[0:11:32] So it's progressively loading in these things that it needs.
[0:11:36] So these skills are super efficient.
[0:11:39] And if we keep coming down, you can see it reads the terminal, it reads the file.
[0:11:43] Let's go down to the bottom of this prompt and see.
[0:11:46] Now it sees this is the template.
[0:11:49] It's now read the template.
[0:11:50] And it knows how to include this all in the response.
[0:11:53] So you can see it's sort of progressively loading in these files and executing them as it needs to
[0:11:58] skills are very cool.
[0:12:00] That's how to create a very basic skill, right?
[0:12:03] You can do this right now.
[0:12:04] You can see they're very simple.
[0:12:06] I want to show you a more complex skill because the very next question you should be asking is,
[0:12:12] well, when should I use a skill?
[0:12:14] Let me show you.
[0:12:15] So technically speaking, there isn't anything that the agent can't do because it can run any command
[0:12:24] in your terminal.
[0:12:24] So technically, it can do anything.
[0:12:25] But there are things that it doesn't know how to do that it will try to figure out how to do
[0:12:29] and it may or may not get those things right.
[0:12:31] So for instance, I've added a PDF file here and this PDF file is for the Logitech MX console,
[0:12:40] which is what I pretty soon see it.
[0:12:43] It's this thing here.
[0:12:45] Very handy.
[0:12:46] You should pick one of those up.
[0:12:47] They're very nice.
[0:12:49] Now, I want to see what's inside this file.
[0:12:52] And so if we ask the AI to do this, we could just say what is in this file here.
[0:12:58] And if we send this prompt, let's actually see what happens.
[0:13:03] And I'm using Opus 4.5, which I consider to be currently the most capable model for coding here.
[0:13:10] So it looks like it's found the file.
[0:13:12] It's going to try to read it, but it can't.
[0:13:15] So essentially, there is no support for Pf's here.
[0:13:18] So what we can do is use a skill to teach co-pilot and cloud how to read PDFs.
[0:13:25] Now, how do we do that?
[0:13:27] Well, we could build our own skill or we can use some of the ones that already exist.
[0:13:31] So if you're the awesome co-pilot repo here on GitHub,
[0:13:35] GitHub.com slash GitHub slash awesome co-pilot, there are some skills here.
[0:13:41] And this list is growing.
[0:13:42] And then the other place is if you go to entropic slash skills,
[0:13:47] GitHub.com slash entropic slash skills.
[0:13:49] And you can see there's a few more in here and we're going to use this PDF skill here.
[0:13:54] So I've cloned that repo to my local machine.
[0:13:57] So I'm going to copy in the PDF skill from there.
[0:14:02] I cloned the repo and then I just copied in the PDF skill here.
[0:14:06] So you can see it's right here and you should recognize this format now after this video.
[0:14:10] So we have the skill dot in the file.
[0:14:11] Here's the metadata here.
[0:14:13] And then you can see it's quite long.
[0:14:15] There's a lot of different scripts in here.
[0:14:16] There's scripts in here.
[0:14:18] There's all kinds of PDF support here, not just reading PDFs,
[0:14:21] but it teaches the agent how to work with PDFs.
[0:14:25] So now let's go back and try our prompt again.
[0:14:29] Now that we have this PDF skill and see what the experience is like,
[0:14:33] now that we've taught the agent how to work with PDFs.
[0:14:37] And you can see it used the scripts in the skill to use some Python to extract the PDF
[0:14:42] contents here.
[0:14:43] And now it knows what the PDF is and we can just pass PDFs with our prompts now.
[0:14:48] Right.
[0:14:48] We've taught the agent a new skill with skills.
[0:14:53] Now that's how you build skills and use them.
[0:14:56] Let's talk for just a second about when to use instruction files versus prompt files versus custom
[0:15:01] agents versus skills.
[0:15:02] So admittedly agents are new and we're sort of still figuring out where everything fits together.
[0:15:09] We've come up with a lot of different ways of passing instructions models.
[0:15:13] And some of this stuff was invented before skills and skills take the
[0:15:17] place of some of those things.
[0:15:19] But I think generally speaking, you can think about it like this.
[0:15:22] If you have instructions that you need to pass with every single prompt to the model,
[0:15:26] like general information about the project, that should be an instructions file.
[0:15:31] If you have a short prompt that you find yourself reusing a lot,
[0:15:35] that should be a prompt file.
[0:15:37] If you want to tweak the way that the agent behaves.
[0:15:42] In other words, you're going to define specific workflows that you want it to follow every
[0:15:46] single time, that's a custom agent.
[0:15:50] Everything else is probably a skill.
[0:15:55] But again, remember that all of these are just building blocks to help you build out workflows
[0:16:01] that work for you and your team.
[0:16:02] There isn't really a right or wrong way to use these things.
[0:16:06] There are just different tools that you have in your toolbox to build out the optimal workflow.
[0:16:11] As the new agent skills support in Visual Studio Code, it's available today in VS Code
[0:16:17] Insiders and Stable.
[0:16:18] Make sure that you look for that experimental setting and turn that on.
[0:16:22] And you can start using them right away.
[0:16:24] Thanks for watching.
[0:16:25] And as always, happy coding.
