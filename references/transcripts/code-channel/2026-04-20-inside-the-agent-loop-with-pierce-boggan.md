---
video_id: ENxVTtLW_Bc
title: "Inside The Agent Loop with Pierce Boggan"
url: https://www.youtube.com/watch?v=ENxVTtLW_Bc
channel: "@code (Visual Studio Code)"
published: 2026-04-20
speakers:
  - Pierce Boggan
  - James Montemagno
topics:
  - agent-loop
  - sub-agents
  - model-selection
  - customization
  - tools
relevance: primary
---

# Inside The Agent Loop with Pierce Boggan

Dive into the heart of VS Code’s agent loop as James and Pierce unravel how agents, sub-agents, tools, and harnesses work together to power your coding experience. Learn how the agent loop has evolved, why different models are used for specific tasks, and how you can customize or optimize your own workflows. Perfect for anyone curious about the magic behind AI-driven code assistance!

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Introduction and Agent Loop Overview |
| 06:17 | Tools, Modes, and Agent Optimization |
| 16:31 | Subagents and Harnesses Explained |
| 21:44 | Why Use Different Models for Subagents? |
| 27:13 | Customization, Trade-offs, and Closing Thoughts |

## Key Topics Covered

- **Agent Loop**
- **Sub Agents**
- **Model Selection**
- **Customization**
- **Tools**

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Welcome back everyone to the VS Code
[0:00:02] Insiders podcast, your one-stop shop for
[0:00:05] everything VS Code, your favorite code
[0:00:07] editor in the entire world. I'm James
[0:00:09] Monte Magno, and with me, back for the
[0:00:11] 18th time, I don't know, 20th time. We
[0:00:12] only have like 20 podcast episodes, so
[0:00:14] it can't be that many. Here's Brian,
[0:00:15] how's it going, buddy?
[0:00:16] It's going great.
[0:00:18] I'm going to put your face directly into
[0:00:20] my teleprompter, so now it's just like,
[0:00:21] wow, I can stare directly into your
[0:00:23] soul. I love it.
[0:00:25] I love it. I'm here in a garage, you're
[0:00:27] here in like some new setup. What is
[0:00:28] going on? You're like at Yeah, I finally
[0:00:31] moved into a real office after all this
[0:00:32] time. I got out of my basement, so um I
[0:00:35] figured it was time for the upgrade in
[0:00:36] 2026. You're so grown up, I love it.
[0:00:39] Very nice. Looks good.
[0:00:41] Uh
[0:00:42] Looks good. Uh today, so we're kind of
[0:00:43] building on a bunch of
[0:00:46] exciting enhancements that have really
[0:00:48] come over the last several months, uh in
[0:00:51] and around how developers are working
[0:00:53] with agents, actually how the agents are
[0:00:54] working with themselves and other
[0:00:56] things. We had Harold on a while ago
[0:00:57] talking about sub agents, and we ended
[0:00:59] up kind of going into even custom agents
[0:01:01] and orchestration,
[0:01:03] and I think that's a really cool like
[0:01:04] advanced scenario. However, what I've
[0:01:06] noticed is that there seems to be I send
[0:01:09] a prompt, and inherently, there seems to
[0:01:12] be this loop happening that is that is
[0:01:15] churning, and at the end of the loop,
[0:01:16] there's a response that comes back, and
[0:01:18] that loop has changed dramatically over
[0:01:21] the last, you know, 6 7 8 months as sort
[0:01:25] of agentic development has evolved, and
[0:01:27] this agent loop, if you would call it
[0:01:29] that, has really evolved, and I think we
[0:01:31] get tons of questions on Twitter and on
[0:01:33] Reddit about what is this thing, what is
[0:01:35] that, what is that? Oh, is that the
[0:01:36] model? I didn't pick that model. What's
[0:01:38] this model? And and what about my
[0:01:39] context window? And what's going what's
[0:01:41] going on here, right?
[0:01:43] And I think because things are evolving
[0:01:45] so quickly, and we get updates every day
[0:01:47] or every single week,
[0:01:49] for me at least, like just happening,
[0:01:51] right? And and I I can dive through the
[0:01:53] documentation to figure out what's going
[0:01:54] on, but then I have these questions as
[0:01:56] like, what is a sub agent actually
[0:01:58] doing, and how does it actually work,
[0:02:00] and should I actually care? Like, so I
[0:02:02] want to dive deeper into the agent loop,
[0:02:04] and maybe you can peel back the layers
[0:02:05] of of of what I just said as far as like
[0:02:08] how the agent loop maybe has
[0:02:10] started, how it evolved, and where it's
[0:02:12] at today, and where it's going.
[0:02:14] Yeah. I mean, it's such a big topic. I
[0:02:17] literally, it's funny that this was the
[0:02:18] topic for today because I just got back
[0:02:20] from visiting a customer, and I did a
[0:02:22] 6-hour presentation.
[0:02:24] So, we'll try not to have a 6-hour
[0:02:26] podcast, cuz there's a lot you can dive
[0:02:28] into here.
[0:02:30] Um but yeah, you're right, like
[0:02:32] we talk about this agent loop. So, what
[0:02:33] is it? So, I'm going to use some like
[0:02:35] approximations, they may not be exactly
[0:02:37] correct, uh but I think they're
[0:02:39] helpful for understanding mentally how
[0:02:41] this thing works. Um
[0:02:43] so, imagine you just basically have a
[0:02:44] giant while loop, right? Um and uh
[0:02:48] that while loop starts when you hit
[0:02:49] enter on your first prompt.
[0:02:52] Um and
[0:02:53] basically, what's happening in this loop
[0:02:54] is every there's many many interactions
[0:02:56] with the model, right? Um and in each
[0:02:59] interaction, you basically uh it's just
[0:03:02] an API request to a model, right? Uh and
[0:03:04] within that API request, there's several
[0:03:06] components. Uh so, you have uh the
[0:03:08] system prompt.
[0:03:10] Uh this [snorts] is actually dynamically
[0:03:11] built for every single kind of
[0:03:14] combination of things you pick in the
[0:03:15] picker. So, if you're picking a
[0:03:17] different model, a different family,
[0:03:19] that's giving you a different set of
[0:03:20] prompts, actually. Um so, there is no
[0:03:22] one prompt for Copilot. There is some
[0:03:24] basic uh responsible AI safety prompts
[0:03:26] that every single
[0:03:28] uh Copilot request has, but outside of
[0:03:29] that, uh it's dynamically built and
[0:03:31] optimized specifically for that model.
[0:03:33] So, we work a lot with the model
[0:03:34] providers in advance of shipping the
[0:03:36] model to really tune the prompts for the
[0:03:38] best possible results. Um so, there's a
[0:03:40] huge feedback loop that happens
[0:03:41] pre-launch on that, and then also a huge
[0:03:43] feedback loop that happens post-launch
[0:03:45] on that. So, we'll do like things like
[0:03:46] AB experiments, test alternative prompts
[0:03:49] based on hypotheses we have, and there's
[0:03:51] a huge kind of pre-launch optimization
[0:03:53] loop with offline evaluations, and then
[0:03:55] uh post-launch uh improvement loop with
[0:03:57] online evaluations. So, you have the
[0:03:59] system prompt, right?
[0:04:01] Then, you have uh other things we append
[0:04:03] to that. So, explicit context, things
[0:04:06] you mentioned like you're like at
[0:04:07] hello.tsx, that's that's mentioned. We
[0:04:10] have implicit context that we include.
[0:04:12] So, if you have an editor
[0:04:14] uh like a file open in the editor, and
[0:04:16] you start an agent session, we consider
[0:04:18] that to be pretty high signal that like
[0:04:20] your thing might relate to the the the
[0:04:22] editor you have open, right? So, we
[0:04:24] attach that. Uh if you have running
[0:04:26] terminals, things like dates, right?
[0:04:28] Your environment information, your you
[0:04:29] know, terminal configuration, things
[0:04:30] like that are auto-attached.
[0:04:32] Um
[0:04:33] then you have tools, right? So, this is
[0:04:35] really the foundation of the agent loop.
[0:04:37] When you think about like chat, um chat
[0:04:40] was like you send a prompt yes to the
[0:04:41] model, so from that perspective, it's
[0:04:43] similar to what we have today, but then
[0:04:45] the model can just send me back a text
[0:04:46] response. And now, actually, what
[0:04:48] happens is there is a set of built-in
[0:04:50] tools,
[0:04:51] um as well as uh tools that you can add
[0:04:54] for things like NCP and other things. Um
[0:04:57] and basically, you can say to the model,
[0:05:00] you can pick one of these tools, or you
[0:05:01] can give me back a text response. So,
[0:05:03] like maybe it's searching, maybe it's uh
[0:05:06] creating a file, maybe it's editing a
[0:05:07] file, right? Uh maybe it's calling the
[0:05:10] GitHub NCP server, and each of those
[0:05:11] tools has a schema and a description.
[0:05:13] So, it says, this is what this tool
[0:05:15] does, um here's the parameters, right?
[0:05:17] So, then the model, if it says, okay,
[0:05:19] the first thing I think I need to do is
[0:05:20] search. Okay, well, we'll use the search
[0:05:22] tool, and then the model will fill in
[0:05:24] those parameters, and then pass that
[0:05:26] back to us, and we'll execute the tool.
[0:05:27] So, then you have tools, right? And then
[0:05:29] we have your user prompt, right? And so,
[0:05:31] that's sent to the model. Uh so, that's
[0:05:33] that's kind of the basic foundation. And
[0:05:35] then, what's happening in the agent loop
[0:05:37] is that's just continuously going,
[0:05:38] right? So, the model is given the
[0:05:40] outputs of the previous thing and able
[0:05:42] to iterate on it. So, okay, we do a
[0:05:44] search. Okay, so now we have a list of
[0:05:46] files we could potentially read. Okay,
[0:05:48] now the agent might call the tool to
[0:05:49] read some of these files. Okay, now we
[0:05:51] have the right context. Okay, now I
[0:05:53] think I have the information I need so
[0:05:55] that I can go place and edit in a file.
[0:05:57] Okay, I'll call the edit tool, right?
[0:05:59] Okay, now I think I'm done, so I'm going
[0:06:00] to respond with that kind of some text
[0:06:02] to the user summarizing what happened.
[0:06:04] Uh and then the agent will basically
[0:06:05] return like a stop message and say,
[0:06:08] "Hey, I'm done." And then that's when
[0:06:09] like the conversation in VS Code wraps
[0:06:12] up, and and you're able to send it out
[0:06:13] of prompt. So, that's the the basic
[0:06:15] foundation of the agent loop.
[0:06:17] Makes a lot of sense. There's actually a
[0:06:18] lot of things happening pre,
[0:06:20] you know, before the actual user prompt,
[0:06:23] right? And I think it feels as though,
[0:06:26] you know, the set of tools and options
[0:06:30] have grown, right? Cuz not only do you
[0:06:31] have bypass, do you have autopilot mode,
[0:06:34] do you have just normal interaction
[0:06:35] mode, do you have planning mode, do you
[0:06:36] have custom agents, do you have ask
[0:06:37] mode, do you have these normal agent
[0:06:39] interactive mode, right? And then,
[0:06:40] inside that, you have all the models and
[0:06:42] reasoning levels and all these different
[0:06:43] things. So, it's fascinating to kind of
[0:06:45] learn about this, and then also, like
[0:06:48] you said, all the tools that are
[0:06:49] available. What I've noticed a lot is
[0:06:51] those agents are going off, and there's
[0:06:53] a lot of like research and investigation
[0:06:55] happening, right? And this is kind of
[0:06:56] always happens. Like, okay, I need to go
[0:06:58] figure out how to add this button
[0:06:59] somewhere. Well, where am I going to put
[0:07:00] it? What file is it? It's greps around
[0:07:02] and reads around and reads files, um
[0:07:06] in general, but I think in that loop
[0:07:08] that you're talking about, it feels as
[0:07:10] though
[0:07:12] is that all happening in a in just one
[0:07:14] single agent, one single thing? Because
[0:07:17] I feel as though
[0:07:19] there's branches that are happening that
[0:07:21] I'm seeing, cuz I'm a big like reader,
[0:07:23] right? Like, I love to read what's
[0:07:24] happening in the chat. Like, oh, and
[0:07:26] drop-downs, they collapse, and there's
[0:07:28] little output here, and it's doing this
[0:07:29] thing, it's doing that thing. So, who
[0:07:30] who is calling what in this agent loop?
[0:07:33] Like, who is deciding
[0:07:35] what gets called?
[0:07:37] Uh the model is deciding based off the
[0:07:39] context it's given. And it's just
[0:07:40] iterating over the previous output and
[0:07:42] appending that to the message. Um
[0:07:44] so, like I think the foundations that we
[0:07:47] just said are very important. There is
[0:07:48] much more advanced techniques that we
[0:07:50] can talk about now, like, okay, when you
[0:07:52] start thinking about sub agents and
[0:07:53] orchestration and all these things, how
[0:07:55] do these things actually work? Uh how do
[0:07:57] all these customizations work? When I
[0:07:58] have a skill versus an instruction
[0:08:00] versus
[0:08:01] uh a prompt file, like
[0:08:03] the the reality is all of these things
[0:08:05] are just modifying that basic construct
[0:08:07] in different ways, right? So, uh let's
[0:08:09] think about something basic like an
[0:08:10] instruction. It is text that is appended
[0:08:13] to your prompt. If it's a global
[0:08:15] instruction, it's always appended. If it
[0:08:17] is a
[0:08:18] an instruction file where you have the
[0:08:19] glob pattern, it's selectively appended,
[0:08:21] right?
[0:08:23] Uh if you have a skill, right?
[0:08:24] Basically, in the prompt, uh the model
[0:08:27] is given a list of skills, just like
[0:08:28] it's given a list of tools. It can
[0:08:30] choose to go read that skill. And then,
[0:08:31] what happens?
[0:08:33] It's just appending text, right? And
[0:08:35] then this is more context for the model
[0:08:37] to make its decision, right? Um
[0:08:39] what happens when you have NCP servers?
[0:08:42] Well, this is just appending the
[0:08:44] built-in tool list, right? That you see
[0:08:46] um in the agent loop. So, now you've
[0:08:48] given the model more tools. And I think
[0:08:52] when we think about like harnessing and
[0:08:54] like all the decisions we have to make,
[0:08:55] there's a actually an enormous amount of
[0:08:56] tradeoffs we have to make as a product
[0:08:58] team to decide
[0:08:59] what are the different strategies we
[0:09:00] want to use, right? So, um
[0:09:04] sure, we can add a million things to the
[0:09:05] prompt, right? But this fills context,
[0:09:08] right? Sure, we can add like, I see some
[0:09:10] people like, I want to have a thousand
[0:09:12] tools, a tool for everything. Okay,
[0:09:13] well, going back to the foundations for
[0:09:15] how these models work,
[0:09:17] the model has to make a choice, right?
[0:09:19] It has to decide between these all these
[0:09:21] options you give, which is the most
[0:09:22] optimal. And just like a human, when you
[0:09:24] give people more choices, their ability
[0:09:26] to pick the right choice degrades,
[0:09:28] right? Uh and so, there's an enormous
[0:09:29] amount of optimization going in from our
[0:09:32] side that you don't actually see, and we
[0:09:33] don't really talk about, we should talk
[0:09:35] about, uh but we don't talk about very
[0:09:37] much around like tool optimization,
[0:09:39] like, what are the right tools, how many
[0:09:40] tools should we have? Uh we have custom
[0:09:42] models that will basically take the tool
[0:09:44] list, if you did have 1,000 tools, and
[0:09:47] basically refine that to like, these are
[0:09:49] the tools we actually think are
[0:09:50] important for this session based off
[0:09:51] what the model says. Some of these tools
[0:09:53] also have their own like custom models
[0:09:55] we built behind the scenes. So, like you
[0:09:56] mentioned context gathering. Right? We
[0:09:58] have a custom model for agentic code
[0:10:00] retrieval. Uh because that it turns out
[0:10:02] if you don't have the right context, you
[0:10:03] don't know where to place an edit, which
[0:10:04] is pretty important for the agent loop,
[0:10:06] right?
[0:10:06] >> Yeah. Yeah. There's a lot of kind of
[0:10:08] micro decisions you make with these
[0:10:10] things and like then as someone
[0:10:12] prompting, it's it's kind of helpful to
[0:10:14] know when you do certain things, what
[0:10:16] does that mean? So, if you tell the
[0:10:17] model to do something and then you're
[0:10:18] like, "No way, do something else."
[0:10:20] right?
[0:10:21] Going back to those first principles,
[0:10:22] right? Each of those messages are just
[0:10:24] getting appended to the end as text,
[0:10:26] right? So, it's possible that the model
[0:10:28] is smart enough to say,
[0:10:30] "Hey, I understand the last message the
[0:10:32] user sent me was correcting a previous
[0:10:33] thing."
[0:10:34] We can also understand how now in this
[0:10:37] history of text, the model in in the
[0:10:40] same request API request has two
[0:10:41] different instructions, right?
[0:10:44] This is generally good that the agent is
[0:10:45] building on the last thing it did,
[0:10:46] right? I wanted to build on the I wanted
[0:10:48] to make an edit based off the context
[0:10:49] that we have gathered, right?
[0:10:51] >> Exactly, yeah. It can also lead to bad
[0:10:52] behaviors, right? Uh so, that's when the
[0:10:55] agent starts going down a really bad
[0:10:56] path, that's why it's important to kill
[0:10:57] it, back up and and understand why do
[0:10:59] you think it's going down this path
[0:11:00] because the previous token that the
[0:11:03] model gets informs the next token,
[0:11:04] right? Um
[0:11:06] so yeah, there's a there's a whole bunch
[0:11:08] of really interesting things there in
[0:11:09] terms of like how this agent loop this
[0:11:12] is optimized and all the choices we
[0:11:13] make. I I think on the VS Code team, we
[0:11:15] have
[0:11:15] you know, 15, 20 people probably who are
[0:11:17] working exclusively on this problem,
[0:11:19] right? Uh building the best harness that
[0:11:21] we can so that you get really, really
[0:11:22] good code quality results from this
[0:11:23] thing.
[0:11:24] Uh with Opus 4 6, James, I think we're
[0:11:26] getting 90% of Opus 4 6 code in our
[0:11:29] harness committed.
[0:11:31] Um this is this is pretty amazing. Uh
[0:11:33] GPT-4 1, when I first started on this
[0:11:35] team, we were 52, 53%. So, this is the
[0:11:38] improvement we see in 1 year.
[0:11:40] Um so, there's an enormous amount of
[0:11:41] work that goes in not just to partnering
[0:11:43] with our model friends, but optimizing
[0:11:44] those prompts so that we in tools so
[0:11:46] that we give you the best results.
[0:11:47] Yeah, I think like this loop and it's
[0:11:49] what's fascinating and why this is so
[0:11:50] important is because
[0:11:52] what people may not know is is is that
[0:11:55] work in the harness is really custom
[0:11:57] tailored not only to the tools, but to
[0:12:00] the model and that evolves over time,
[0:12:02] right? These these evaluations, these
[0:12:04] prompts that we've talked about on the
[0:12:06] pod before, but in general when you
[0:12:08] think about it,
[0:12:09] like today's a launch day, Opus 4 7 came
[0:12:11] out when we're recording this pod
[0:12:13] Yes.
[0:12:13] >> like to say like today is like the worst
[0:12:15] day to use that model because it's a
[0:12:17] brand new model. Like everyone's going
[0:12:18] to be trying to use it cuz it's so
[0:12:19] capacity and then
[0:12:21] >> Yes. the system prompt, it's fresh. It's
[0:12:24] it's it's a newborn. It's it's an infant
[0:12:26] state, right? And there's yet been time
[0:12:29] to go work and and hone it, but you
[0:12:32] really see within a few weeks, even like
[0:12:34] that first week, you know, the the
[0:12:35] system prompt like things how are are
[0:12:37] working, yeah, how it works with tools,
[0:12:39] how things work with all the models work
[0:12:40] different, even incrementally from like
[0:12:42] 4 5 to 4 6 to 4 7, right? You know, in
[0:12:44] in a in a in a 5 3 to the 5 3 Codex, all
[0:12:46] think a little bit different. But then
[0:12:48] it quickly evolves over time.
[0:12:51] Yeah, definitely. Um like of course we
[0:12:53] try our best pre-launch. We you we
[0:12:55] usually get access to the model several
[0:12:57] weeks, if not uh
[0:12:58] several months before.
[0:13:00] Um and then we're working with kind of
[0:13:02] people from Anthropic, Gemini, uh
[0:13:05] OpenAI, xAI, etc. to like really refine
[0:13:08] those prompts based off what we're
[0:13:11] seeing basically in our harness. So, we
[0:13:12] run a ton of we have our own uh kind of
[0:13:14] SWE-bench equivalent called VS
[0:13:15] SWE-bench. It's built on custom
[0:13:17] problems. It doesn't have all the
[0:13:18] pollution issues that SWE-bench has now.
[0:13:20] I don't even think the labs actually use
[0:13:21] SWE-bench anymore because of all the
[0:13:23] pollution we see in the training data
[0:13:25] for this benchmark. So, we built our
[0:13:26] own. Um and then basically we have a ton
[0:13:28] of different cases and we run many many
[0:13:31] runs, not just one,
[0:13:32] but many many runs to to reduce variance
[0:13:35] and you spot patterns. You look at what
[0:13:37] we call the agent trajectory. Uh so,
[0:13:39] that's basically the path at which the
[0:13:41] agent takes to solve your problem.
[0:13:43] Right? So, it's not even just did we
[0:13:45] solve your problem, yes no. That's a
[0:13:47] very simplistic way of looking at
[0:13:48] something like resolution rate at
[0:13:49] benchmark. No, we're we're actually
[0:13:51] going and saying like, "What is the path
[0:13:52] the model took and was that an optimal
[0:13:55] path?
[0:13:55] How can we influence the path the model
[0:13:57] takes? How can we get you to that really
[0:13:59] good resolution rate in fewer steps,
[0:14:01] right? Uh so that you get actually
[0:14:03] really high quality results, but instead
[0:14:04] of waiting 1 hour, right? You're
[0:14:06] waiting, you know, 1 minute, right? And
[0:14:08] so, those are the sorts of things we do
[0:14:10] and every problem kind of brings its own
[0:14:11] thing. So, we do a lot of optimization
[0:14:13] there. And then as you say, like we do
[0:14:15] the best we can, but offline evaluations
[0:14:16] are always flawed, right? It's a very
[0:14:18] small subset of data as much as we try
[0:14:20] to improve the the cases that we have.
[0:14:23] Um so then post-launch as you say, like
[0:14:26] the there's capacity things like both on
[0:14:28] our end and upstream providers, right?
[0:14:30] Um and we have to kind of figure out
[0:14:32] what demand looks like. It's different
[0:14:34] for every single model. It's hard to
[0:14:35] predict demand in an agentic world where
[0:14:37] people run now 10 agents at once, right?
[0:14:39] Um and more and more people are using it
[0:14:41] agents every day. So, demand prediction
[0:14:43] is very difficult. Um and then also like
[0:14:46] to your point like
[0:14:48] when it's out there, we can do things
[0:14:49] like run AB tests and and basically
[0:14:51] actually know in the wild what is
[0:14:53] better, right? Not a hypothetical in our
[0:14:55] in our offline evaluation cases, but
[0:14:56] actually know what's better. Uh and of
[0:14:58] course the model providers also have
[0:14:59] their own updates they make to the
[0:15:00] models and so they see things and
[0:15:02] improve stuff like that. Um so yeah,
[0:15:04] like that's all part of the continuous
[0:15:06] loop that's happening. So, there's like
[0:15:08] continuous work on models that have we
[0:15:10] have already shipped to optimize them.
[0:15:11] There's new models in the queue we're
[0:15:13] working on optimizing. There's generic
[0:15:15] kind of prompt and tool optimizations
[0:15:17] that are constantly happening. And then
[0:15:19] for many of these things, there's also
[0:15:20] custom, you know, purpose-built models
[0:15:22] actually being created by our data
[0:15:23] science team to go and actually solve
[0:15:25] really hard problems there.
[0:15:26] Yeah, it's crazy. There's there's a lot
[0:15:28] of little tiny things that are happening
[0:15:30] that I think people don't actually even
[0:15:32] realize. Like when you start a chat,
[0:15:34] like it update the name of the chat.
[0:15:36] Like that's a that's pretty sure it's a
[0:15:37] custom Right? Yeah, we're passing the
[0:15:39] conversation history to a a cheap model,
[0:15:41] admittedly, cuz there's no reason to use
[0:15:43] Opus for this. We need to get
[0:15:45] uh we need to get a title back very
[0:15:46] quickly and it's okay if it's not
[0:15:47] exactly the perfect title. Um
[0:15:49] >> But yeah, that's an LLM call, right? So,
[0:15:51] there's there's a lot of other things
[0:15:52] always happening in the product that
[0:15:53] maybe like you don't appreciate.
[0:15:55] Yeah. There's like some random if
[0:15:57] statement like uh that generated the
[0:15:59] title in this way based off this
[0:16:00] heuristic. That's actually going and
[0:16:01] hitting a model, right? So, Yeah. It's
[0:16:04] and and some of the things that become
[0:16:06] like second nature to me, which is like,
[0:16:07] oh, I just like, you know, click a
[0:16:09] button to like generate a commit
[0:16:10] message, generate a PR, click a little
[0:16:13] button. And those are all things
[0:16:14] happening and those are also things that
[0:16:16] are tweaking. They're they're they're
[0:16:17] they have their own little tiny agent
[0:16:18] loop of things that are happening as
[0:16:20] well, right? Yeah. And that that are
[0:16:22] just transparent to you, those AI edits
[0:16:24] and there's actually like modifying code
[0:16:26] and editing code by hand, right? There's
[0:16:28] tons of things happening in the next
[0:16:29] edits and the suggestions. I think
[0:16:32] the biggest question we get part of this
[0:16:33] agent loop, which is more of the
[0:16:35] advanced scenario that we've seen it
[0:16:37] time and time again, which is why I
[0:16:38] really wanted to talk about the agent
[0:16:39] loop, was part of when the agent is
[0:16:42] figuring out
[0:16:44] if it should do something or if it
[0:16:45] should delegate work. And when I mean
[0:16:48] delegate work, I mean to sub-agents.
[0:16:51] Yes.
[0:16:51] >> Now, we got this question recently on
[0:16:55] Twitter. Uh I forgot about exactly who
[0:16:56] it was from. I had we had a big
[0:16:57] conversation. Um and I was pulling up
[0:16:59] docs from OpenAI, our documentation, the
[0:17:02] Claude code docs, like all the different
[0:17:03] docs, right? And understanding here's
[0:17:04] how these models work, how these
[0:17:06] harnesses work. When I say harness,
[0:17:08] like like the
[0:17:09] >> It's I guess describe harness.
[0:17:12] It it's kind of a a rough definition,
[0:17:13] but it's like all the things that
[0:17:14] combine to basically make that agent
[0:17:16] loop. So, like the the prompts that we
[0:17:18] have, the context that it's able to
[0:17:20] gather, uh the tools that we provide it,
[0:17:22] like the custom models behind the
[0:17:23] scenes. That's all the the magic that
[0:17:25] actually gets you good results. Yeah.
[0:17:27] So, CLI has a harness, VS Code has a
[0:17:30] harness, VS has a harness, other coding
[0:17:32] agents have harnesses, harnesses in
[0:17:34] general. And that's why you get
[0:17:35] different behavior between different
[0:17:37] things cuz there's different harnesses,
[0:17:38] different prompts. So, the question we
[0:17:39] got was, "Hey,
[0:17:41] I chose
[0:17:43] um I think Opus 4 6 or maybe 5 or or
[0:17:46] OpenAI uh you know, GPT-5 4 or Codex and
[0:17:51] I see a bunch of work being done. I see
[0:17:53] this loop happening and then I see a
[0:17:56] bunch of sub-agents exploring, grabbing
[0:18:00] code, doing things, Yes. but it's using
[0:18:03] a different model. It's using Haiku or
[0:18:05] it's using a mini model, for example.
[0:18:09] And the question I got was,
[0:18:11] "How is this actually working? Why is it
[0:18:14] using different models?
[0:18:16] And
[0:18:17] what is is is the VS Code team pulling a
[0:18:20] fast one over my eyes?" That's That's
[0:18:22] how That's how it read. It didn't
[0:18:23] actually how it It didn't That wasn't
[0:18:25] what was written, but that was my
[0:18:26] interpretation. Like, "Hey, are you guys
[0:18:28] pulling one over my eyes here because
[0:18:30] you guys pulling a bait and switch? I
[0:18:31] thought I'm 3x in over here. Now you're
[0:18:33] 0.33 and over here. What's going on? And
[0:18:36] what's the advantage?" I think at the
[0:18:37] end of the day,
[0:18:39] Yeah.
[0:18:39] we could talk about the solution, but
[0:18:41] actually talking about the problem, the
[0:18:43] why is more important than like how it
[0:18:45] actually works.
[0:18:46] Yeah, that's that's correct. Um well,
[0:18:48] first like we're
[0:18:51] all of our incentives on on the VS Code
[0:18:53] and GitHub Copilot teams are to build
[0:18:55] the best possible experience for you,
[0:18:56] right? So, so that is our North Star
[0:18:58] goal and we will like we will not pull
[0:19:00] fast one on you because that is not what
[0:19:02] we are as a team incentivized to do,
[0:19:04] right? I I don't want to do this, right?
[0:19:06] Um that's ever been part of our culture
[0:19:08] in in GitHub or VS Code. Um yeah, so
[0:19:10] like going back to to basic primitives,
[0:19:13] right? Um
[0:19:14] let's just talk about sub-agents and
[0:19:16] then we'll get into the specific case of
[0:19:17] this sub-agent, right? Um so like for
[0:19:20] instance, um
[0:19:23] going back to the basic mechanism for
[0:19:24] agent loop. So, a sub-agent is basically
[0:19:26] like this main agent can decide, "I want
[0:19:29] to go uh basically do this workflow, run
[0:19:32] this agent loop again with fresh
[0:19:34] context. I want to tell it what to do as
[0:19:37] a goal." So, the main agent is basically
[0:19:39] prompting this other agent to go do
[0:19:40] something with fresh context.
[0:19:43] The agent will run its own kind of loop,
[0:19:45] like just like the main one. Uh and then
[0:19:47] it will just like a function, it has a
[0:19:49] result and it will return back to main
[0:19:51] thread, right? Uh so, that's essentially
[0:19:53] what a sub agent is. So how does it
[0:19:54] work? How does it decide when to call a
[0:19:57] sub agent?
[0:19:58] Well, let's go back to basic mechanisms.
[0:20:01] A sub agent is just a tool the model can
[0:20:03] choose to use. So
[0:20:05] the model can selectively say
[0:20:08] I want to use the run sub agent tool,
[0:20:11] right? It can choose to
[0:20:12] to to select this in the magic agent
[0:20:15] loop, right? And that will be returned
[0:20:17] back to VS Code in this case. And then
[0:20:19] VS Code will go spin a sub agent, right?
[0:20:22] Based off the input parameters that has
[0:20:24] been
[0:20:25] filled by the model, right?
[0:20:27] So it is just basically a tool call,
[0:20:29] right? Which is interesting. This is why
[0:20:31] it's so interesting to understand the
[0:20:32] basic mechanisms. So then how do you
[0:20:34] actually get it to call a sub agent?
[0:20:36] So then it's it's kind of basic pro-
[0:20:38] prompting, right? Like
[0:20:40] you could be very explicit in your user
[0:20:41] prompt that you want sub agents to be
[0:20:43] used for certain things. We could have
[0:20:46] things in our prompts that are quite
[0:20:50] explicit about using sub agents. That's
[0:20:52] also a possibility, right? So like the
[0:20:54] system prompt could be very aggressive
[0:20:56] about saying we want to use sub agents
[0:20:57] for these sorts of things. And some
[0:20:59] features do, right? Like if you've ever
[0:21:00] used
[0:21:01] inside of Copilot CLI or
[0:21:04] research or things like this.
[0:21:06] Again, same basic mechanism. It's just
[0:21:08] aggressively prompted to really rely on
[0:21:10] the sub agent strategy, right?
[0:21:12] Which really allows you to keep that
[0:21:14] main agent loop super fresh cuz remember
[0:21:16] we're just appending the result of all
[0:21:18] the conversations to the main loop.
[0:21:20] Well, if you're doing all that in the
[0:21:21] main process, right? Your main process
[0:21:22] gets very convoluted. The agent will get
[0:21:25] confused. You'll have to compact the
[0:21:26] conversation which you generally do want
[0:21:28] to try and avoid cuz you're going to
[0:21:29] lose some fidelity. So sub agents are
[0:21:31] really a strategy. So then okay, now
[0:21:34] getting back to original question.
[0:21:35] Explore sub agent.
[0:21:37] So I mentioned we do a lot of kind of
[0:21:39] investigation into these trajectories,
[0:21:41] right?
[0:21:42] What is the path the agent takes? You
[0:21:45] inspect this a lot and you think about
[0:21:46] like how can we make this better? And
[0:21:48] better has different characteristics,
[0:21:49] right? It could be higher output
[0:21:51] quality, right? We could bump up all the
[0:21:55] you know, thinking effort on all the
[0:21:57] models to max things. We could
[0:22:00] have it run 100 sub agents,
[0:22:01] self-validate all its work, right?
[0:22:03] There's a trade-off you make as a
[0:22:04] product team because that that would be
[0:22:06] kind of a terrible customer experience
[0:22:07] for a synchronous partnership, right?
[0:22:10] And so the idea is like how can we get
[0:22:12] to the highest possible resolution rate
[0:22:14] while still making like the experience
[0:22:16] feel somewhat interactive, right? You
[0:22:17] know what's going on with this agent.
[0:22:18] Like you're going to want to provide
[0:22:20] feedback at the right points, right? You
[0:22:22] don't want it to be overly chatty. You
[0:22:24] also don't want it to be too terse cuz
[0:22:25] you have no idea what's going on. And so
[0:22:26] there's a whole bunch of knobs that are
[0:22:28] actually product decisions you make in
[0:22:30] the prompts and tools, right? To go and
[0:22:31] do that. So for So you mentioned like at
[0:22:35] the beginning of every turn, yes, we go
[0:22:36] search things. You need context. So
[0:22:38] thinking more about that problem what
[0:22:40] actually is happening there, right?
[0:22:42] Well, as you say, it's it's mostly
[0:22:44] choosing to either do run run in term-
[0:22:47] run in terminal and grep, right? Or use
[0:22:49] one of our search tools and gather
[0:22:51] context in that way. Or it's hitting our
[0:22:53] semantic search endpoint and doing
[0:22:55] agentic code retrieval, right?
[0:22:57] But it's a very simplistic thing, right?
[0:22:59] It's just okay, I need to run grep. I
[0:23:01] need to gather context.
[0:23:03] And something like Opus is a is a very
[0:23:05] heavy reasoning model. It it is very
[0:23:07] powerful, but it is also quite slow,
[0:23:09] right?
[0:23:10] And so basically what we found is like
[0:23:13] well, considering
[0:23:14] actually when you think about the agent
[0:23:16] turn
[0:23:17] the quality of results, yes, it does
[0:23:19] depend on the context within reason, but
[0:23:21] like it's much more determined by what
[0:23:22] happens after that. Like how does the
[0:23:24] model operate over the context it's
[0:23:26] gathered? So in the case of the explore
[0:23:28] sub agent, we decided to use Haiku cuz
[0:23:31] the performance characteristics were
[0:23:32] much better in terms of time to first
[0:23:33] token and how quickly it was able to
[0:23:34] execute things like grep searches,
[0:23:37] right? And so it can run super super
[0:23:39] fast. And basically we found that it
[0:23:42] didn't actually degrade the quality when
[0:23:44] we did this pattern
[0:23:46] of the overall resolution rate going
[0:23:47] back to those offline emails. So you can
[0:23:49] basically speed up the agent turn by
[0:23:51] creating a sub agent, keeping all the
[0:23:52] nasty context of gathering stuff in that
[0:23:55] sub agent, right? Doing it with Haiku
[0:23:57] which is extremely fast. It's just
[0:23:58] running a ton of greps. Returning that
[0:24:00] back and then Opus is actually able to
[0:24:02] use his big brain and kind of reason
[0:24:03] over all the context we gathered. So
[0:24:05] basically it's one of those like magic
[0:24:07] things where like we were essentially
[0:24:08] able to speed up the entire turn
[0:24:11] by not sacrificing quality at all.
[0:24:13] That's that's actually like the
[0:24:14] goldmine, right? And so this is why we
[0:24:16] really are looking deeply at all these
[0:24:18] trajectories for opportunities like that
[0:24:19] for optimization. So that's actually
[0:24:20] what's happening there. It's like
[0:24:22] yes, we could have used Opus, but like
[0:24:24] it was maybe going to make your turn 30%
[0:24:26] slower, 40% slower. And we can give you
[0:24:29] the exact same resolution rate with a
[0:24:31] model that's much faster and give you
[0:24:32] faster turns. So those are the sorts of
[0:24:34] kind of things we are exploring behind
[0:24:36] the scenes. I definitely think we can do
[0:24:38] a better job of kind of explaining our
[0:24:39] rationale for these sorts of things.
[0:24:41] That's totally fair feedback. We need to
[0:24:43] make sure in the UX it's quite clear
[0:24:44] when these things are happening. That's
[0:24:45] totally fair feedback. But that's kind
[0:24:47] of like how we got there and and kind of
[0:24:49] the justification for for these sorts of
[0:24:50] things like these special purpose sub
[0:24:53] agents that we've started building into
[0:24:55] our agent loop.
[0:24:56] It makes a lot of sense because even me
[0:24:58] when I'm writing prompts to do specific
[0:25:00] things at work, I will specifically in
[0:25:02] my prompt
[0:25:05] front matters specify like a Haiku or
[0:25:08] GPT mini model because they're super
[0:25:10] quick and I'm not doing super complex
[0:25:12] things inside of it, right? I don't need
[0:25:14] that big rationale. I think of it as
[0:25:17] you know,
[0:25:18] I need to eat some cereal, right? And I
[0:25:22] have the bowl, I have the cereal, I have
[0:25:23] the milk in there. Things are good. I'm
[0:25:25] in a good place. All the all the all the
[0:25:27] the the loop is ready. Like the harness
[0:25:29] is ready. It's it's it's got my my bowl,
[0:25:31] but I need a utensil to eat said cereal.
[0:25:35] This is a terrible analogy, but you I'm
[0:25:36] going to tell you you can tell me if it
[0:25:37] works.
[0:25:39] >> [laughter]
[0:25:39] >> So I can go one of two routes to get to
[0:25:41] the same conclusion. I could bring a
[0:25:43] Swiss Army knife that can do a thousand
[0:25:45] things and has like all the capabilities
[0:25:48] and all the really advanced things. And
[0:25:50] there is a spoon in there that I could
[0:25:52] open. I'd have to find it. Like I'd have
[0:25:53] to go deeper into it. Now when I use
[0:25:55] this tool, it might also get in my way
[0:25:57] cuz it has other things that are coming
[0:25:58] up and poking me. Or I could just go
[0:26:00] grab a spoon.
[0:26:02] Which is going to give me the same exact
[0:26:03] result as that Swiss Army knife which
[0:26:05] has a spoon, but it does one thing and
[0:26:07] it does that one thing really good. And
[0:26:08] like the sub agent with this specific
[0:26:10] model can do that one thing really
[0:26:11] really Well, obviously that model does a
[0:26:13] lot of things really well, but in this
[0:26:14] case it's super focused in on it, right?
[0:26:17] Well, and like I I think in this
[0:26:19] particular case it's like that is a
[0:26:20] product choice we're making for our plan
[0:26:22] mode is we think it gives you really
[0:26:23] good results. But if you decide, hey, I
[0:26:26] actually don't want that to happen for
[0:26:27] plan mode, you know, for whatever
[0:26:29] reason, I I think that I should we
[0:26:30] should choose a different strategy. The
[0:26:32] really cool thing about VS Code is like
[0:26:34] you can take our built-in, you know,
[0:26:35] modes like plan mode. You can literally
[0:26:37] go in and copy the exact, you know, it's
[0:26:40] just a custom agent, right? You can go
[0:26:42] copy the exact prompt and tools that
[0:26:44] uses and you can just modify it to how
[0:26:46] you and your team works. So if you're
[0:26:47] like, I don't like that. That's a really
[0:26:49] cool thing about VS Code. You can go
[0:26:50] change and basically build your own plan
[0:26:51] mode. Now I have full confidence that
[0:26:53] our plan mode is going to give you
[0:26:55] really really good results because we
[0:26:56] have a whole group of people who work on
[0:26:58] optimizing it, right? And making sure it
[0:27:00] does give good results. But I also at
[0:27:02] the same time believe like I mean, we
[0:27:04] see this in in resolution rate. Like
[0:27:06] certainly Opus is the is the strongest
[0:27:07] model in terms of, you know, if you were
[0:27:09] to take the average of all of your
[0:27:11] resolution rates, it's going to do the
[0:27:12] best. But we see tons of problems in our
[0:27:15] in our harness where Opus isn't the
[0:27:17] best. Where GPT-4 is the best. Where
[0:27:20] Opus might be one of the worst models
[0:27:21] actually.
[0:27:22] And so there is an extreme amount of
[0:27:24] variance. And so I do also at the same
[0:27:26] time appreciate like you may have some
[0:27:28] specialized things you want in your plan
[0:27:29] mode. And for your specific like team
[0:27:31] and company and project, those might be
[0:27:33] the right things. But generally I feel
[0:27:35] like the choices we make for things like
[0:27:37] our plan mode and agent loop are
[0:27:39] optimizing for the overall experience
[0:27:40] like the P50 median experience. It's
[0:27:42] certainly possible you may need to go
[0:27:43] and tweak it yourself. And that's the
[0:27:45] cool thing is you can, right? So
[0:27:48] yeah, I like that we have like an
[0:27:49] opinion and we try to give you the best
[0:27:51] results, but you can always go to your
[0:27:52] own thing if you feel like you need to.
[0:27:54] Yeah, it's like
[0:27:55] I go back to my spoons analogy. There's
[0:27:57] a general spoon design, but you might
[0:27:59] you might want a different, you know,
[0:28:02] width or like different style, a
[0:28:04] different color of spoon for said cereal
[0:28:07] consumption. And like it's out there for
[0:28:09] you can go do it, right? You can go you
[0:28:11] can go pick off the shelf
[0:28:13] another spoon that someone built or you
[0:28:14] could you could build your own spoon.
[0:28:16] You could put it together. You could get
[0:28:18] into your
[0:28:19] your welding shop.
[0:28:21] It's like I'm going to
[0:28:22] I'm going where it's like spoons
[0:28:24] basically. That's what I'm saying. How
[0:28:25] many spoons do you got? And you just
[0:28:26] need one good spoon. And we got many
[0:28:27] many spoons and they all have different
[0:28:29] capabilities. I think that's really
[0:28:31] important. So
[0:28:32] now in general though
[0:28:34] um
[0:28:35] when these
[0:28:37] the the thing that you said for these
[0:28:38] sub agents where the it's basically like
[0:28:40] work trees are isolated
[0:28:43] code branches basically, right? It's an
[0:28:45] isolated thing. And you can think of a
[0:28:46] sub agent as an isolated context window,
[0:28:49] right? Is that Is that the same analogy?
[0:28:51] Yeah, I mean it's it's Imagine if you
[0:28:54] were to just create a new chat and run
[0:28:56] like I want you to gather context in
[0:28:58] this new chat. And then you were to ask
[0:28:59] in that chat, please summarize the
[0:29:01] context that you just gathered for this
[0:29:03] is my goal. Please please pick only the
[0:29:05] most relevant details. Then imagine you
[0:29:07] were to copy paste all that from that
[0:29:08] other chat you created back into the
[0:29:10] main chat. That's essentially what's
[0:29:11] happening at like a
[0:29:14] high level with the sub agent pattern,
[0:29:16] right? Is it's just basically going and
[0:29:17] creating a new chat, doing this thing
[0:29:20] with a prompt based off where the agent
[0:29:22] is at in his main loop and then
[0:29:23] returning back some result based off my
[0:29:25] goal.
[0:29:27] Yep. That makes sense. Yeah, exactly.
[0:29:29] Yeah. I like it.
[0:29:31] I think that's the biggest question that
[0:29:34] that people get. Now in VS Code you can
[0:29:35] override that as well, that
[0:29:37] functionality, right? Everything's super
[0:29:39] customizable, correct? That's right.
[0:29:41] Yeah. If there's any if you want to
[0:29:43] disable the run sub agent tool, you can
[0:29:45] literally do that, right? So all these,
[0:29:48] you know, this is why it's a
[0:29:49] it is a lot to to keep up with. I I
[0:29:52] totally agree, but if you can understand
[0:29:54] the basics of the agent loop, then you
[0:29:56] can really start to reason much more
[0:29:58] about like, "Okay, well, I don't like
[0:29:59] subagent or why does subagent work?" Or
[0:30:01] like these sorts of things. You can go
[0:30:02] turn it off, you can turn it on. You can
[0:30:04] aggressively prompt it to do that. And
[0:30:07] none of these strategies is like
[0:30:08] foolproof, right? There's there's
[0:30:09] different tradeoffs you make, right? Um
[0:30:11] and so like you may decide you want to
[0:30:13] make a different set of tradeoffs,
[0:30:15] right? So like a big one is like, "Do I
[0:30:17] put a lot of things in my rule file?"
[0:30:19] Like I was working with a customer and
[0:30:20] they had like a lot of custom things
[0:30:22] that were in like their uh Confluence uh
[0:30:25] instance, right? And they're like, "Do
[0:30:26] we represent that as a as an as a rule
[0:30:29] or do we use the tool?"
[0:30:30] So like well there's a tradeoff there,
[0:30:31] right? Like you could put it in every
[0:30:33] single prompt, but then it's in every
[0:30:34] single prompt and of course then you are
[0:30:35] responsible for keeping that that uh
[0:30:38] information up to date in the prompt,
[0:30:40] right? Um so that's that's its own set
[0:30:42] of problems, right? Could be could be
[0:30:43] advantageous.
[0:30:44] Or you could add the Confluence tool,
[0:30:46] right? It can go search. But now the
[0:30:49] agent has to decide when to invoke your
[0:30:51] tools, so you'll need some strong
[0:30:52] prompting on when it needs to go to your
[0:30:54] tool. That tool description needs to be
[0:30:55] good, right? Um and also you're adding
[0:30:58] more latency to your entire agent loop,
[0:31:00] right? Because you're having to go run
[0:31:01] more tools as part of the thing. So the
[0:31:03] total turn time is going to get longer.
[0:31:05] But if that gets you to a faster result
[0:31:07] in the end because you pay the tax of
[0:31:09] going and getting the right context and
[0:31:11] the agent doesn't have to iterate as
[0:31:12] much later in the loop, maybe that's a
[0:31:15] that's a price worth paying, right? And
[0:31:16] so these are the sort of engineering
[0:31:17] decisions like when you understand the
[0:31:19] basics of the agent loop, you can start
[0:31:21] to reason about, "Well, like
[0:31:22] you know, we could put it in the prompt
[0:31:24] or we should be doing a tool or maybe
[0:31:25] you find some hybrid strategy that
[0:31:26] really works for you over time." But
[0:31:28] like understanding those basics helps
[0:31:29] you to better reason about the tradeoffs
[0:31:31] that you're making.
[0:31:33] No, that makes a lot of sense. Yeah, I
[0:31:35] think it's it's good to kind of talk
[0:31:37] through
[0:31:38] like how things are working and why
[0:31:40] they're working this way. And of course
[0:31:41] this may evolve over time, too, but at
[0:31:43] least in the day of April 2026, this is
[0:31:46] like how things are evolving in general.
[0:31:48] So that's really neat. I think that
[0:31:51] talking about the loop, diving here,
[0:31:53] there's a lot more happening. We could
[0:31:54] go for hours, but we're not going to. So
[0:31:56] what we want to do is kind of
[0:31:57] >> six hours earlier this week.
[0:31:59] So we're going to cut the pod here, but
[0:32:00] what we want you to do is like let us
[0:32:02] know. Reach out to me and Pierce on uh
[0:32:04] Twitter or write into the show or just
[0:32:06] leave feedback in any of the VS Code um
[0:32:08] subreddits or things like that and and
[0:32:10] let us know if you have more questions
[0:32:12] on this agent loop, we'll dive deeper
[0:32:13] through it. I'll bring out some people
[0:32:15] from the team that are working on these
[0:32:16] evals and going as well. So uh Pierce,
[0:32:18] thanks for coming on and talking about
[0:32:19] the the deepness uh of the agent loop. I
[0:32:22] know we just scratched the surface.
[0:32:24] Yeah, definitely. And you know, the
[0:32:25] other cool thing about VS Code is if you
[0:32:27] always want to go inspect this for
[0:32:28] yourself, there's commands, you know,
[0:32:29] developer show chat debug log, uh
[0:32:31] developer show agent debug log.
[0:32:33] Confusingly, there's two different ones,
[0:32:35] but um you can see like basically a
[0:32:37] flowchart of like how your agent is
[0:32:39] going, all the different tool calls. Um
[0:32:41] so you can look at this trajectory, as I
[0:32:43] called it, yourself and go dig in and
[0:32:44] see exactly what's happening.
[0:32:46] Totally. Yep. I love it. All right,
[0:32:48] Pierce, well thanks for coming on. We'll
[0:32:50] dive deeper in the future on more of
[0:32:51] this stuff, but don't forget you should
[0:32:53] subscribe on your favorite podcast
[0:32:54] application, tell your friends, tell
[0:32:56] your coworkers. And of course you can
[0:32:57] check out the YouTube @code, which has
[0:33:00] over a million subscribers
[0:33:02] uh as well. And we also put us there as
[0:33:05] well, so you can see our faces. And
[0:33:06] here's the new office. All right, that's
[0:33:07] going to do it for this
[0:33:09] VS Code Insiders podcast. Until next
[0:33:10] time,
[0:33:12] happy coding.
