---
video_id: 0XoXNG65rfg
title: "Level Up Your VS Code Productivity (Mastering AI Workflows)"
url: https://www.youtube.com/watch?v=0XoXNG65rfg
channel: "@BurkeHolland"
published: 2025-12-09
speakers:
  - Burke Holland
topics:
  - instructions
  - prompts
  - custom-agents
  - workflows
relevance: primary
---

# Level Up Your VS Code Productivity (Mastering AI Workflows)

Burke Holland deconstructs VS Code AI workflows, including the instruction hierarchy, prompt files, custom agents, and workflow composition.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Intro |
| 03:56 | Custom Instructions |
| 06:57 | Prompt Files |
| 12:08 | Custom Agents |
| 15:08 | Building a Workflow |

## Key Topics Covered

- **Instructions**
- **Prompt files**
- **Custom agents**
- **Workflow design**

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] For a long time, I have wondered what the difference is
[0:00:02] between prompt files, custom instructions,
[0:00:05] and custom agents in Visual Studio Code.
[0:00:08] And it's a question I hear a lot.
[0:00:10] So in this video, we're gonna dive in,
[0:00:12] we're gonna take a look at all of those things,
[0:00:14] how they work together to completely understand
[0:00:16] when and where to use them.
[0:00:17] Are you ready?
[0:00:19] Let's go.
[0:00:20] Before we actually look at custom instructions
[0:00:22] or prompt files or custom agents,
[0:00:25] it's really important for you to understand
[0:00:27] how the agent system prompt works in Visual Studio Code.
[0:00:31] And this is important because you're gonna need to know
[0:00:33] where in fact these instructions get inserted
[0:00:36] into that prompt.
[0:00:36] So let's run through that just real quick.
[0:00:40] So if we were to type some sort of a message,
[0:00:42] just say hello world here and send it to the chat,
[0:00:45] it gets sent.
[0:00:46] But let's take a look at what actually happens
[0:00:49] behind the scenes here.
[0:00:50] Behind the scenes,
[0:00:52] Co-pilot composes a prompt,
[0:00:54] and it starts with a system prompt.
[0:00:57] Like this here.
[0:00:58] And the system prompt starts off with some core identity
[0:01:03] and global rules.
[0:01:04] And this is just very generic stuff.
[0:01:07] In fact, I think there's only two or three lines.
[0:01:09] It's like you are an intelligent AI coding assistant,
[0:01:12] kind of this just generic identity.
[0:01:15] And then underneath that, there's general instructions.
[0:01:18] And these instructions can vary by model
[0:01:21] because the models have various quirks.
[0:01:23] So for instance, if a model is very aggressive
[0:01:26] about writing the code out to the chat
[0:01:28] when it should just be writing it to the file,
[0:01:31] there might be an instruction never print out
[0:01:32] code blocks with file changes.
[0:01:34] And then underneath that, there's tool use instructions.
[0:01:37] And these are instructions for the model
[0:01:39] about how to use the tools that are included in Co-pilot like
[0:01:45] the edit tool or the terminal tool
[0:01:47] or the to-do list tool, any of the built-in tools.
[0:01:51] And then underneath that, there's some output format
[0:01:54] instructions that just tell the agent how to format
[0:01:58] the output for tokenization in the chat
[0:02:00] so that things like the little file pills
[0:02:03] that you'll see in Visual Studio Code
[0:02:05] actually show it correctly.
[0:02:07] Now, the next thing that happens is a user prompt
[0:02:10] gets added to the message that sent to the model.
[0:02:13] It hasn't been sent yet.
[0:02:15] The user message contains the environment info.
[0:02:18] So information about the user's operating system, et cetera.
[0:02:21] And it also includes workspace info
[0:02:23] and it literally looks like this.
[0:02:25] It's kind of your project structure in text format.
[0:02:29] Project name folders files.
[0:02:32] And then another user prompt gets added to the message,
[0:02:37] which has still has not yet been sent.
[0:02:39] And that contains context info,
[0:02:42] like the current date and time,
[0:02:44] list of open terminals that you have.
[0:02:46] It also contains any files that you have added to the chat.
[0:02:52] Now, in our case, we didn't have any files added to the message,
[0:02:55] but if we were to add files like that,
[0:02:58] then they would show up here
[0:02:59] right here into this editor context.
[0:03:01] And then finally, we have the hello world.
[0:03:05] And then all of this gets sent up to the model
[0:03:09] and the model responds with this assistant message.
[0:03:12] And all of these things together are the context window.
[0:03:16] So the context window is just being built up here.
[0:03:18] We have one and then another one gets added.
[0:03:21] And then another one gets added here.
[0:03:24] And then all of this gets sent.
[0:03:26] And then the response comes back.
[0:03:27] And then this gets added.
[0:03:29] And now this is the whole context window here, right?
[0:03:32] All of this.
[0:03:33] And if we were to add another user message,
[0:03:36] this would just get added here
[0:03:38] and would become part of the context.
[0:03:40] Okay, so now you understand what actually happens
[0:03:44] when you send a prompt.
[0:03:45] Now, the question is,
[0:03:47] what are custom instructions,
[0:03:49] prompt files and custom agents
[0:03:50] and where do they actually go in this prompt?
[0:03:54] So let's take a look at that.
[0:03:56] It's probably best if we start with something
[0:03:59] like custom instructions.
[0:04:02] So the most canonical use for custom instructions
[0:04:06] is to contain high level information
[0:04:09] about your project that might help the model
[0:04:11] do a better job giving you answers.
[0:04:14] So for instance, in Visual Studio Code,
[0:04:18] if you click the gear here,
[0:04:19] we can generate chat instructions.
[0:04:23] And this will do exactly what I just said.
[0:04:25] It will create an instructions file
[0:04:27] that has the high level information,
[0:04:29] your project architecture, any patterns you can use.
[0:04:32] You can actually go and read this prompt here.
[0:04:35] So you can see exactly what it's being asked to write.
[0:04:38] But we recommend this for every project.
[0:04:41] And this is probably the most common use case
[0:04:45] for custom instructions.
[0:04:46] Once we've generated these custom instructions,
[0:04:49] if we were to send another message,
[0:04:52] you'll see when we do that,
[0:04:54] the custom instructions automatically get passed right there.
[0:04:57] There they are.
[0:04:58] So this file is being passed as part of the context.
[0:05:01] So the question is,
[0:05:02] where exactly does that show up in the prompt?
[0:05:06] So in our diagram here,
[0:05:08] custom instructions show up right here in the system prompt.
[0:05:12] And they're actually added right here.
[0:05:16] So they're the last thing in the agent system prompt.
[0:05:22] And it should be noted that the co-pilot instructions
[0:05:25] will always be the last thing in the agent system prompt.
[0:05:29] Because you can create as many instruction files as you like.
[0:05:33] So let me give you an example.
[0:05:36] This site is called Awesome Co-pilot.
[0:05:38] And it is full of community contributed prompt files,
[0:05:42] custom instructions and custom agents.
[0:05:44] It is a treasure trove of custom instructions
[0:05:48] that you can look at for inspiration.
[0:05:50] So we could go here and find some instructions that we like.
[0:05:54] So here's a table of all the different ones
[0:05:56] that are available.
[0:05:57] So let's go down here and let's pick maybe next JS best practices
[0:06:04] for LLM.
[0:06:05] So if we click install,
[0:06:07] this will install the file in Visual Studio Code.
[0:06:11] We can go ahead and accept it.
[0:06:12] It asks us where we want to put it.
[0:06:14] We can put it in the user data folder,
[0:06:16] which makes it globally available.
[0:06:18] Or we can put it in the dot get up slash instructions folder,
[0:06:22] which means it will only be available in this project,
[0:06:25] which is exactly what I'm going to do.
[0:06:27] And now if you look, we'll see we have an instructions folder
[0:06:30] and a next JS instructions inside.
[0:06:33] And if we were to pass another prompt here,
[0:06:36] now probably guess what's going to happen,
[0:06:38] both of those files actually get passed.
[0:06:41] And just to clarify, remember that the next JS instructions
[0:06:46] will always come before the copilot instructions file
[0:06:51] that always comes last.
[0:06:53] So at a high level, that's custom instructions.
[0:06:57] Now let's talk about prompt files.
[0:06:58] Prompt files are reusable prompts
[0:07:01] that you can define and then use right in the chat.
[0:07:05] Now why would you do this?
[0:07:06] Well, let me give you an example.
[0:07:08] If we want to define a prompt file,
[0:07:10] you can go to configure prompt files.
[0:07:13] And you can see that I've got a bunch of different prompt files
[0:07:16] here.
[0:07:16] So let's go ahead and look at this one here,
[0:07:19] which is called remember.
[0:07:20] So I'm going to look at the remember prompt.
[0:07:22] And in the remember prompt,
[0:07:24] this is a prompt that I have that just builds up a memory file.
[0:07:28] So I can tell the AI at any time
[0:07:30] to just remember something and it will do that.
[0:07:33] Now you can see up here in the front matter
[0:07:35] that I can specify the agent down here.
[0:07:38] We're just going to stick with the agent.
[0:07:40] But then we can also list added description.
[0:07:42] But then the other very powerful thing here
[0:07:44] is that we can also add a model.
[0:07:46] And you can see we get IntelliSense for all of the models
[0:07:49] that we have available.
[0:07:51] Many of these are on open router.
[0:07:53] Some of them are built in.
[0:07:54] I'm going to use a small model for this
[0:07:56] so that I don't waste premium request.
[0:07:58] And what this means is when I use this prompt file,
[0:08:01] it will automatically move us over to the correct model.
[0:08:05] So let me show you what I mean.
[0:08:07] So let's say the model keeps making the same mistake
[0:08:09] trying to use a use effect on server components,
[0:08:12] which you cannot do in next JS.
[0:08:14] And so we just want it to remember not to do that.
[0:08:16] So we can use that prompt file with just the slash here.
[0:08:20] And then paste in our message.
[0:08:23] And when we send this, you'll notice that we're on
[0:08:25] Claude Opus 4.5, which is a premium model at 3x.
[0:08:30] But when we send it, it actually get sent with GPT 4.1
[0:08:33] because that's what we specified in the prompt file right here.
[0:08:39] GPT 4.1.
[0:08:41] And now it's created an instructions file for us.
[0:08:44] And this instructions file will be added automatically
[0:08:48] to every single request.
[0:08:49] So you can see here how I'm kind of starting to build up
[0:08:52] workflows using actually both prompt files
[0:08:55] and custom instructions.
[0:08:58] Now let's go back to our diagram.
[0:09:00] And let's take a look at where actually in the system
[0:09:04] prompt these prompt files actually show up.
[0:09:08] So the answer is they don't, not in the system prompt.
[0:09:12] They actually show up down here in the user prompt.
[0:09:17] So in the user prompt, what happens is these prompt files,
[0:09:22] their contents get added right here at the very top.
[0:09:27] So even before the context info, we'll have prompt files.
[0:09:31] And then we're going to have just the contents of the prompt file
[0:09:34] that was used.
[0:09:36] And then what happens is down here in this message,
[0:09:39] it says, follow the instructions in.
[0:09:44] And then it points back up to the contents of that prompt file.
[0:09:48] But it actually uses a special syntax to do that.
[0:09:51] It's pointing to it by name, even though it's actually
[0:09:54] included in the user prompt.
[0:09:56] And then after that, it has your system message,
[0:10:00] which would be, use effects can only be used in client
[0:10:05] components.
[0:10:07] So that's where prompt files come in.
[0:10:09] And so if we have a lot of messages,
[0:10:11] they may be way, way, way down in the list.
[0:10:14] We may be way down here.
[0:10:16] Each time you use a prompt file, it's part of the user prompt,
[0:10:20] not part of the system prompt.
[0:10:23] Now, the question that you're going to ask is,
[0:10:25] does the placement of the prompt within the message hierarchy
[0:10:30] actually matter?
[0:10:32] And the answer to that is, I don't know.
[0:10:35] However, context rot is a real thing.
[0:10:39] And the basic idea here is that as the context window grows
[0:10:43] and gets longer, the performance of the model
[0:10:46] degrades.
[0:10:47] Now, this has gotten better over time
[0:10:49] as the article dives into here.
[0:10:51] It's improved.
[0:10:53] But you can still see here that as the context window grows,
[0:10:56] for example, a 32,000 token prompt, accuracy drops dramatically.
[0:11:02] Even Claude 35 Sonic goes from 88% to 30% accuracy.
[0:11:08] So it's important to remember that as your prompt is growing
[0:11:12] here, so if we have a system prompt and a user prompt
[0:11:16] and a user and then an assistant message
[0:11:18] and then a user prompt and then we have another assistant
[0:11:21] message because we haven't started a new chat.
[0:11:23] So we just keep going and going and going.
[0:11:26] It doesn't really matter if you're using custom
[0:11:28] instructions or prompt files.
[0:11:30] The performance or the accuracy of the model
[0:11:33] is just going to degrade.
[0:11:35] And this is one of the reasons that the token windows
[0:11:39] or the context windows in VS Code
[0:11:41] are limited at a certain point.
[0:11:44] And that is to maintain performance.
[0:11:46] So it's hard to answer the question,
[0:11:48] would you be more accurate to pass your instructions
[0:11:51] as a prompt file or a custom instruction?
[0:11:54] The best thing to do is instead of worrying about the positioning,
[0:11:57] just use them as they are designed, which
[0:11:59] is to help you compose workflows and not
[0:12:02] worry about their position in the prompt.
[0:12:04] Now, let's talk about one last thing
[0:12:06] and that's custom agents.
[0:12:08] Custom agents used to be called custom modes.
[0:12:12] And I built one a while back that was called beast mode.
[0:12:15] That was designed to help GPT 4.1 perform better.
[0:12:19] And the idea here is that you can pass instructions
[0:12:21] to sort of override or augment the default agent behavior.
[0:12:27] So let's take a look at these.
[0:12:29] What I want to look at is one of the ones that we're now
[0:12:31] shipping in Visual Studio Code, which is the plan mode.
[0:12:35] So you can actually click on configure custom agents
[0:12:38] and you can look in our built-in plan mode here.
[0:12:41] So let's take a look at the plan mode.
[0:12:43] You can see that in the name and the description
[0:12:46] and then there's these tools.
[0:12:48] And then there's these things called handoffs, which
[0:12:50] we'll get to in just a second.
[0:12:52] And then you can see that it's very much like we're writing
[0:12:57] an agent prompt.
[0:12:58] This is very different from custom instructions.
[0:13:00] If we look at the custom instructions, this is different.
[0:13:03] It's just giving it information.
[0:13:05] This is giving it an identity.
[0:13:07] So it's very much like an agent system prompt.
[0:13:11] And then it's going to go through and it uses a workflow
[0:13:15] to start a planning process with the user.
[0:13:18] The first step is to gather context and research.
[0:13:21] and present a concise plan for iteration
[0:13:23] and then handle user feedback.
[0:13:25] And then it will give you the option to either implement
[0:13:29] the plan or to put the plan right out to the editor.
[0:13:33] And it does that via handoffs.
[0:13:35] So let's actually run this and take a look
[0:13:37] at what this actually looks like in action.
[0:13:39] So I'm going to pick a model that's
[0:13:41] a little bit better at planning here.
[0:13:43] I'm using our built-in plan mode.
[0:13:45] So let's do something that is always done in these demos.
[0:13:47] We're just going to add dark mode to an app.
[0:13:49] I don't know why that's the prompt that's always used.
[0:13:52] But it's because it's visual and it's
[0:13:53] because something we can see.
[0:13:55] So we're going to let Haiku go through and work through this plan.
[0:13:59] You can see this.
[0:13:59] And then we'll come back and talk about what
[0:14:01] is actually happening here.
[0:14:03] OK, so we're using this new plan agent.
[0:14:05] And we've sent this prompt what is actually
[0:14:07] happening behind the scenes.
[0:14:10] Let's go back and take a look at our diagram.
[0:14:13] So what happens when you use a custom agent is this?
[0:14:17] It actually gets added to the system prompt here.
[0:14:21] So let's make some more room.
[0:14:23] And the custom agent is always added here
[0:14:27] below your custom instructions.
[0:14:30] So that's the order.
[0:14:33] In the system prompt, the custom instructions
[0:14:35] will be added to the end of the system prompt
[0:14:36] and then the custom agent instructions
[0:14:39] are added to the end of the system prompts there.
[0:14:41] The last thing in the agent system prompt.
[0:14:47] So now let's take a look at how we can use custom instructions,
[0:14:50] prompt files, and custom agents to compose
[0:14:53] a gensick workflows because that's what they are.
[0:14:56] There isn't really a right or wrong way to use them.
[0:14:59] They're just building blocks for composing
[0:15:01] your own workflows.
[0:15:02] But that doesn't really make any sense in the abstract.
[0:15:05] It's going to help you if you see how someone else has done it.
[0:15:08] So what I want to do now is show you how I compose workflows.
[0:15:12] So what I'm going to do is I'm going to use a prompt file for planning.
[0:15:15] I have a custom planning prompt file.
[0:15:18] And then I'm going to ask it to refactor
[0:15:19] the UI of this application to be more clean and modern.
[0:15:23] And you'll notice the first thing that it does
[0:15:24] is it switches us over to Opus 4.5
[0:15:27] because that's what I've defined in the prompt file.
[0:15:31] We can actually take a look at that.
[0:15:32] If we go here, here's my prompt file.
[0:15:35] You can see I've defined the model.
[0:15:37] And then my prompt file is for planning
[0:15:39] is very similar to the built in agent.
[0:15:42] But my prompt file actually instructs the agent
[0:15:45] to work in the concept of a branch.
[0:15:48] So the plan is really defining one PR or one branch.
[0:15:53] And it's just defining the high level steps.
[0:15:55] So it's going to do things that the built in
[0:15:58] plan custom agent does like researching the code base
[0:16:03] and asking me questions.
[0:16:05] But the plan format that it spits out
[0:16:07] is a little bit different because this
[0:16:08] is just one of the building blocks.
[0:16:12] And it'll make more sense here in a second.
[0:16:14] OK.
[0:16:14] So planning mode is done.
[0:16:15] And we have one file here that's been created.
[0:16:18] And I have it create the file automatically.
[0:16:20] It does have some questions.
[0:16:22] But they're their mild, not anything
[0:16:24] that I really need to address.
[0:16:26] But you can see it just breaks things down into step.
[0:16:28] Step one, do this.
[0:16:29] Step two, do this.
[0:16:30] The idea is that each one of these steps is a commit.
[0:16:33] And commits should be small and testable.
[0:16:36] And commits will build up and create a single PR
[0:16:40] that we can then submit.
[0:16:42] We don't have any code, though.
[0:16:43] So the next step is to actually get code.
[0:16:46] So let's go ahead and keep this.
[0:16:47] And because we don't want context wrought,
[0:16:50] let's start a new chat session here.
[0:16:52] Clear the context.
[0:16:54] So now what I'm going to do is something a little bit unique.
[0:16:58] Instead of actually implementing the plan,
[0:17:00] I am going to have it generate a document based on that plan.
[0:17:06] And then I'm just going to pass the plan file here.
[0:17:09] So in this case, I'm using a generate prompt
[0:17:12] and passing in the plan that we just created.
[0:17:15] And I'll explain what it's doing.
[0:17:18] So the generate prompt takes the plan.
[0:17:21] And then it writes all of the code required
[0:17:25] to implement this plan.
[0:17:27] But it doesn't write that code in the project.
[0:17:29] It actually writes it in a markdown file step by step.
[0:17:35] And the reason why I'm doing this
[0:17:36] is because I'm trying to maximize my premium model usage.
[0:17:41] I've used Claude Opus 4.5 twice now.
[0:17:44] It is a 3x multiplier.
[0:17:46] This six premium requests.
[0:17:49] I want to make sure that I'm getting the most bang for my buck.
[0:17:53] So I'm actually going to use a smaller model to implement
[0:17:56] and a bigger model to write the code.
[0:17:59] The smaller model will implement it,
[0:18:01] but the bigger model writes it.
[0:18:03] So in just a second, we'll take a look at this implementation
[0:18:06] plan and you can see exactly how this works.
[0:18:09] It's not complicated.
[0:18:10] The implementation plan that gets generated is long.
[0:18:14] It's very long.
[0:18:15] This one's almost 2,000 lines long.
[0:18:18] But you can see that every single piece of code that
[0:18:21] is needed to accomplish this job is actually in this file.
[0:18:25] But what's more important here is that they're all
[0:18:28] broken up into steps.
[0:18:29] And each step has a checkbox here.
[0:18:33] So now that we have that, we're going
[0:18:34] to clear the context window again, making the best use
[0:18:38] of our context.
[0:18:38] And now we're going to use a custom agent, which
[0:18:41] is just called implement.
[0:18:43] And all we have to do is then pass in the implementation
[0:18:46] plan here like this and give it a simple prompt.
[0:18:51] And then we just send it.
[0:18:52] And you can see it automatically moves
[0:18:54] to the VS Code prime or Raptor prime, which is a five mini
[0:18:59] variant.
[0:19:00] And it's the model that I like to use for implementation.
[0:19:03] So we'll go ahead and send that off.
[0:19:06] Now as this smaller model works on this document,
[0:19:09] it's going to implement what's in the document just verbatim.
[0:19:13] It isn't actually writing any code.
[0:19:15] It's just implementing the code that the large model
[0:19:18] wrote.
[0:19:19] And this strategy lets you sort of one shot with a huge model
[0:19:24] and then implement and iterate with a small free model.
[0:19:28] And this model will keep going until it's completed,
[0:19:30] whatever step it's on in the implementation plan.
[0:19:33] And then it will stop.
[0:19:35] And it will return control to me so that I can test,
[0:19:38] make sure that I like it.
[0:19:39] And then I will just stage and commit.
[0:19:42] And then I will just redo what I did,
[0:19:45] use the implement agent, pass at the implementation document.
[0:19:48] And it will just pick up with step two and continue.
[0:19:51] And I will just iterate with it like that
[0:19:53] until we get to the end of the implementation
[0:19:55] and everything's working.
[0:19:56] And then I have a pull request that I feel really good about.
[0:20:00] Okay, so now you have a really good understanding
[0:20:03] of how things work behind the scenes
[0:20:06] for the agent in VS Code.
[0:20:08] You understand the agent system prompt
[0:20:10] and how the user prompts are added on
[0:20:12] and where custom instructions and prompt files
[0:20:14] actually go in that prompt.
[0:20:17] Go forth and create AI workflows that work for you.
[0:20:20] I'll put links to mine below
[0:20:22] and check out the awesome Copilot repo
[0:20:25] where you'll find in my workflows plus tons
[0:20:28] of other prompt files instructions and custom agents
[0:20:31] that you can use today.
[0:20:32] And as always, happy coding.
