---
video_id: -BhfcPseWFQ
title: "After This Video, You'll Actually Understand Agent Orchestration"
url: https://www.youtube.com/watch?v=-BhfcPseWFQ
channel: "@BurkeHolland"
published: 2026-02-10
speakers:
  - Burke Holland
topics:
  - orchestration
  - custom-agents
  - planning-agent
  - coder-agent
relevance: primary
---

# After This Video, You'll Actually Understand Agent Orchestration

Burke Holland gives a practical explanation of agent orchestration, including planning agents, coder agents, and orchestrator-style coordination.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Introduction |
| 00:36 | What is orchestration? |
| 03:38 | Orchestration with custom agents |
| 05:38 | Orchestrator Agent |
| 07:23 | Planning Agent |
| 07:57 | Coder Agent |
| 10:10 | Orchestration in action |

## Key Topics Covered

- **Orchestration**
- **Custom agents**
- **Planning agents**
- **Coder agents**

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] agent orchestration. Otherwise known as what? Yes, the latest hot trend for vibe coders or
[0:00:08] agentic engineers is here. In this video, we're going to take a look at what it is, how it works,
[0:00:14] and whether or not you should use it today. And as always, please remember, all we have right now
[0:00:19] are new features and ideas. And we're kind of figuring out how things work in real time.
[0:00:24] So don't feel compelled to understand and use all of this stuff. In the end, use what's right
[0:00:29] whatever works, whatever makes you productive. That's the right thing. You're ready? Let's go.
[0:00:36] Now the best way to understand agent orchestration is just to look at it from what you're doing
[0:00:41] today. So in your editor of choice, maybe you send a chat command. What does this project do?
[0:00:49] And then you can send another chat command. And maybe this one is research design for iOS apps.
[0:00:58] And on this one, you're going to send it to a background agent. And so now you have two agents
[0:01:02] going at the same time, a local agent and a background agent. And maybe you even have a cloud agent.
[0:01:08] Now in this scenario, you are the orchestrator. You are running all of these different agents
[0:01:14] and maybe you're using opus for some and cloud for others and GPT five for others.
[0:01:18] But in an agent orchestration scenario, you actually have one agent that calls others. And this is
[0:01:24] possible because of the recent tooling that has arrived for both the CoPilot CLI and Visual Studio
[0:01:31] code. So if we were to go to the CoPilot CLI here, so let's just fire that up. So the most naive
[0:01:40] way that we could orchestrate agents here is to just have them call each other. And we can do
[0:01:45] that just by saying it like this. Review the code in this project for accuracy and improvements
[0:01:55] and security flaws. When you're done with your findings, run them by both GPT five, two codecs and
[0:02:02] Jiven I three pro iterate with these two models to see what their ideas are, what their findings
[0:02:07] are and then come back with a complete plan on what we can do to improve this project.
[0:02:15] Now I'm going to send this prompt. And in this case, believe it or not, this is all we have to do
[0:02:20] in the CoPilot CLI. It will actually pick up the different models we want to use. And it doesn't
[0:02:26] even matter that it got it wrong here. And it said GPT five, two codecs with the K, whatever that is,
[0:02:32] it should actually figure this out on its own and then delegate to these different agents. Let's
[0:02:37] see if it does that. So you see here it says, now I have the full code base. Let me launch three
[0:02:42] parallel reviews is running GPT five, two codecs in Gemini three pro. And it's doing this
[0:02:47] all at the same time. So most people don't know this is possible. But yes, you can in CoPilot have one
[0:02:54] model call other models. You don't have to use just one in the chat session. You can use all of
[0:02:59] them. And that's exactly what's happening here. All right. So I sped that up. But you can see what
[0:03:04] happened here. It called the general purpose GPT five, two codecs agent here. And the general
[0:03:10] purpose Gemini three pro preview agent here. Now what these are is something called sub agents. And
[0:03:16] these are available in both the CLI and in Visual Studio code. And they are super powerful
[0:03:21] because sub agents can be called by the main agent. But sub agents can have whatever model you
[0:03:27] want them to have. And then as you can see it went through, it created a plan here for us. And it's
[0:03:33] quite a long plan. We're not going to look at it because this is a real project that I'm working on
[0:03:36] that I want to show you. Now you can probably see that this opens up a lot of possibilities.
[0:03:43] First and foremost, if you have an agent that can call other agents, then essentially you could
[0:03:49] just build your own dev team, right? Like you could have a team lead and architects and coders and
[0:03:54] designers and planners and PMs. I mean, why not? You can have as many sub agents as you want.
[0:04:00] And so that is the general idea behind agent orchestration is that you have agents orchestrating other
[0:04:06] agents. So let's actually see how this works in practice in a real project. So here's a real project
[0:04:13] that I'm working on. It is a replacement for the Gemini app on iOS because there are features that
[0:04:18] the Gemini app doesn't have. I'm tired of waiting for them and it's 2026. So you can just build
[0:04:23] your own. And so we can make a picture of cats playing volleyball, just like this, send it. And this
[0:04:31] will interact with the Gemini API. It's just a chat app, but it's done the way that I like
[0:04:36] specifically in this app. I can edit history, edit my prompts and reset them. For whatever reason,
[0:04:42] you can't do that today in the Gemini app. So I just made it so that you could. So we can edit
[0:04:48] this dog's playing volleyball. Now, what we want to do here is create the web experience for
[0:04:55] this, this app because sometimes you use AI on your phone and then you go back to the web and you
[0:05:01] use it there. And so we want to create the web experience. We're going to use agent orchestration
[0:05:05] to do that. Now, we talked about how Visual Studio Code has custom agents and those custom agents
[0:05:10] are here. And you can define these custom agents just by clicking configure custom agent. So what
[0:05:16] we're going to do is we're going to create an orchestration framework that has an orchestrator with
[0:05:22] a planner, a designer and a coder. And we're going to use all three of the big models to do this.
[0:05:27] Sonnet, GPT52, GPT52, Codex and Gemini 3 Pro. So let's jump in and take a look at this
[0:05:36] first orchestrator custom agent. The orchestrator's entire job is just to orchestrate work between
[0:05:43] different agents. It doesn't actually do any work itself other than that. It's like a PM or a
[0:05:49] logistics coordinator. So you can see here, the first thing that we do in our custom agent is configure
[0:05:54] the tools and it only has to. It has the ability to call sub agents with the agent tool and it has a
[0:06:00] memory and memory is new in copilot. You can use that today. And you can see here, we just scroll
[0:06:06] down. The prompt is fairly simple. You're a project orchestrator. You break down complex requests
[0:06:11] into tasks and delegate them to specialist sub agents. You coordinate work, but you never
[0:06:18] implement anything yourself. And then this is important. For Visual Studio Code, we need to tell
[0:06:24] the orchestrator exactly what the name of the different sub agents it can use are. They are planner,
[0:06:31] coder and designer. And we'll take a look at these. And then we have a workflow. It's fairly
[0:06:37] understand plan, break it down in the steps, delegate it to the sub agents, coordinate between the agents
[0:06:44] depending on the work that was done and then report the results back. Now we have some rules down here
[0:06:50] lower that tell this orchestrator agent. Don't tell sub agents how to do work because these agents
[0:06:58] really, really, really want to do the work. And so what I noticed is that the main orchestrator agent
[0:07:03] really wants to tell the sub agents exactly what to do, wants to give them the line to change,
[0:07:07] exactly what to change. These models think they know everything. And so you have to really go out of
[0:07:11] your way to make sure that they don't do that. So that's essentially what the rest of this prompt
[0:07:15] does. But you can see it's not terribly long. That's the orchestrator. So let's look at the planner.
[0:07:22] The planner custom agent, as you can see right here, let's jump into that, has all of the tools.
[0:07:27] It can do pretty much anything. You create plans. You do not write code. And you can see,
[0:07:32] and this is key here, this model line five two. So this is how the agent knows which model to use.
[0:07:40] So when the orchestrator calls the sub agent, this sub agent is just going to use GPT five two.
[0:07:45] So we're using five two for planning. You can see these prompts are not very long.
[0:07:49] Props don't need to be long and complicated to get the job done. They just need to do the job.
[0:07:54] So now let's take a look at our coder. The coder agent uses GPT five two codecs. That's
[0:08:02] what that model's good at is writing code. It's really good at writing code. That's all this agent
[0:08:06] does. And you can see here, it's got a lot of tools and it has an MCP server called context seven.
[0:08:11] And context seven is very simple. It has one tool. Just allows the agent to go and read the docs.
[0:08:16] And so here in the prompt, this is pretty simple, except for this block right here. And this
[0:08:22] block is meant to counter the fact that the orchestrator is probably going to try to tell this agent
[0:08:27] what to do. And we're basically telling it, don't do that question everything you're told,
[0:08:32] make your own decisions. And then here are just some mandatory coding principles that I use
[0:08:37] for the coding agent. You don't have to have these, but I like to include these. And these are
[0:08:42] very generic terms like prefer flat explicit code over abstractions or deep hierarchies. Right.
[0:08:48] We're just trying to keep the code clean and simple. And so you're more than welcome to use these,
[0:08:53] but you don't have to. Now let's take a look at the designer, the designer handles all of the
[0:09:00] UI UX and styling because as it turns out, not all of these models are the same when it comes to
[0:09:05] design. And in fact, Theo has a great video on this that you should check out where he looks at
[0:09:10] which model is best for design. Spoiler alert, he doesn't think that it's Gemini 3 pro. I tend to
[0:09:16] disagree. I tend to get better results with the Gemini 3. So that's what we're going to use.
[0:09:20] The designer prompt probably the most simple of all, the model we're specifying Gemini 3 pro.
[0:09:25] I get way better results with design with Gemini 3 pro. I don't use Gemini for hardly anything else,
[0:09:31] but for design unbeatable. And then here, look, I'm doing it again. You are the designer. Don't let
[0:09:37] the orchestrator tell you how to do your job because the orchestrator is going to try to do that.
[0:09:41] Instead, it goes to create the best possible user experience and interface designs focusing on
[0:09:48] usability, accessibility, and aesthetics. Conceptually speaking, the design agent needs to have
[0:09:55] full creative autonomy here. So we don't want to give it a lot of guardrails. We really want to let
[0:09:59] it do what it does, which is design. So that is essentially the whole orchestration framework. It's
[0:10:04] ultra light. It's very small, but I want to show it to you in action. And what we're going to do is
[0:10:09] we're going to use this orchestration framework to build a web experience for the mobile app that
[0:10:15] we have. Now before we actually use this orchestrator agent, it's important to point out that what
[0:10:21] model should you use for the orchestrator? I use Claude sonnet 4 5. And the reason that I do this is that
[0:10:27] Claude sonnet 4 5 is very agintic, right? It's almost like a Labrador, right? It's like, it's just
[0:10:34] super eager always trying to do things. And so we want to harness that. We want that energy. We want
[0:10:40] the agency that sonnet 4 5 has, but we don't want it writing any code. It's not good at writing code.
[0:10:46] I would not recommend that you have sonnet 4 5 right code. GPT 5 2 codecs is just way better at that.
[0:10:52] So we want the agency of sonnet. And we want the coding chops of codecs. And that's what we're going
[0:10:59] to do here to get that. We're going to have a sonnet be the orchestrator. Now what we're going to do
[0:11:05] is we're going to create the web experience for the mobile app. And we're going to send it in and
[0:11:10] try to one shot it. Probably won't be able to do that because it's quite complex, but let's see what
[0:11:15] our little orchestration framework can do. We want to create a web experience for this mobile app.
[0:11:22] We want it to look exactly like the mobile app or brother, borrow the same design aesthetics
[0:11:28] from the mobile app. It should use Firebase. The mobile app is already using Firebase. Feel free
[0:11:34] to use the Firebase CLI to get the resources that you need or to stand up any resources that you need.
[0:11:44] Now I'm going to send this prompt and let this thing go. This is going to take some time.
[0:11:49] And then we'll come back when it's done. Examine the chat history and then take a look at what
[0:11:54] it's actually produced and see if orchestration works. All right, it finished. And that did take
[0:12:03] some time, but let's scroll back up through the chat here. And I just want to show you a few things
[0:12:07] because this is pretty fascinating. So from our prompt here, you can see the first thing that it's
[0:12:12] doing is it's calling the planner agent just like it's supposed to. And that's going to use
[0:12:17] GPT 5-2. And if we look at the planner agent, you can see the prompt that actually gets sent.
[0:12:22] The user wants to create a web experience for their iOS, Gemini, chat app, here are the requirements.
[0:12:30] It's basically taking what I asked and boosting that prompt and then it asks for a plan. And it
[0:12:36] gets the plan back. Now after the planning agent is finished, it reviews the plan, reads it,
[0:12:43] and then delegates it to the designer to create a web design system. And again, we can dig in here
[0:12:49] and see the prompt. It's telling the designer a little bit of information about the application and
[0:12:54] then telling it to create if we scroll down here, create a design system for this web application.
[0:13:02] And it puts it here in a Markdown document right there. There it is. There's a design system
[0:13:07] complete with CSS styles and everything. Now it's Gemini 3 Pro doing its job. Now after the designer,
[0:13:14] it starts to coordinate with the coder and then it calls the coder. And then in the coder,
[0:13:20] it says, build a complete web application for the better Gemini chat app and it passes in the
[0:13:26] plan here. And then down here, you can see it uses the web design system that was created by the
[0:13:34] designer. Now if we scroll back up, go through here. You can see that now that we're inside the
[0:13:42] coder agent, it's using the context seven MCP tool to create documentation. And it just keeps going
[0:13:49] and going and then eventually finishes. Let's go ahead and collapse this, compiles a list,
[0:13:55] and then tells you what it has actually created here. Now here's the most fascinating thing about
[0:14:01] all of this. Do you see the context window indicator down here? Look at this. Do you see how much
[0:14:09] context window we have not used? It created 2,707 lines of code and we've only used 10.8k of the
[0:14:18] context window. How is that possible? That's the magic of subagents. They have an isolated context
[0:14:24] only used what's theirs. And then once the subagent is done because it has its own context window,
[0:14:30] that's gone. It doesn't pollute the main context window. It just gets the result of what the subagent
[0:14:36] does. Now let's see if this actually worked and see if we have a working web app.
[0:14:43] All right, here's the app. Let's go ahead. Can we sign in with Google? We can. Brilliant. Let's go ahead
[0:14:49] and click that. Okay. Let's start a new conversation. All right. So already we have some issues.
[0:14:57] Again, we can probably open up our dev tools here and copy those errors out here and then
[0:15:03] take them back in and work with our orchestration framework to actually make this functional.
[0:15:08] But let's talk about this for a second in some improvements that we could probably make here.
[0:15:12] So one of the things that I noticed is that when it created the plan, it didn't really pass
[0:15:18] much of the plan to the coder. It's sort of just passed a high level overview of the plan. So
[0:15:24] we might want to update the planner to say save your plan in a document and always pass that document
[0:15:29] to the coder. Another thing that I noticed is that it ran one coder agent to do all of the work
[0:15:35] would have been better if it had sliced up the work into discrete chunks and then given that to
[0:15:39] five coder agents running at the same time because subagents can run in parallel. You can do that.
[0:15:46] We have some tweaks to make to our orchestrator prompt here. If you would like to try this
[0:15:50] ultra light orchestration framework today, you can do that. It's here and the link below the video.
[0:15:56] Then you just need to install each one of these. Just click on the button that will open
[0:16:01] Visual Studio code and install the agent for you. These agents are exactly the same ones that we
[0:16:06] saw in this video. But remember what I've created here isn't the end of all, be all. It's just
[0:16:13] an example of how you can use a single agent to orchestrate multiple sub agent. But how you put it
[0:16:20] together is however it works best for you. Choose the models that work for you that make you the
[0:16:27] most productive. There's also other agent orchestration frameworks out there. So really, really
[0:16:32] complex ones. You may have heard of them, gas town, GSD and some others. You probably want to take
[0:16:38] a look at those as well. And that is basically agent orchestration. You can use this today at a very
[0:16:45] simple level. You don't have to have a hundred agents all out there doing various things all of the
[0:16:49] same time checking each other's code, reviewing each other's pull requests. That'd be nice.
[0:16:54] But where we are today is that if you could get one agent to delegate work out to a bunch of
[0:16:59] sub agents who are very good at different things, that's a great start when it comes to agent
[0:17:04] orchestration. Good luck and as always, happy coding.
