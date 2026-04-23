---
video_id: rJSsbHwkYAY
title: "Multi-model AI workflows in GitHub Copilot CLI"
url: https://www.youtube.com/watch?v=rJSsbHwkYAY
channel: "@BurkeHolland"
published: 2026-03-31
speakers:
  - Burke Holland
topics:
  - copilot-cli
  - multi-model
  - model-selection
  - orchestration
relevance: primary
---

# Multi-model AI workflows in GitHub Copilot CLI

Burke Holland shows how to compose multi-model workflows in GitHub Copilot CLI so different models can handle different parts of the same task.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Why not just pick one model? |
| 00:44 | Models and reasoning levels |
| 01:49 | Models calling models |
| 03:06 | Orchestrating multiple models |
| 06:06 | Built-in orchestration |
| 11:06 | Adversarial review |

## Key Topics Covered

- **Copilot CLI**
- **Model selection**
- **Orchestration**
- **Adversarial review**

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Which model is best?
[0:00:03] That is the question.
[0:00:04] But I don't think it's actually the right question.
[0:00:07] So even as I said that, if you've been using a lot of models,
[0:00:10] immediately you thought, well, it's opus or it's GPT.
[0:00:14] People have very strong opinions about this.
[0:00:16] But actually, different models are good at different things.
[0:00:19] So the right question is, what's the best model for this job?
[0:00:23] Unfortunately, if you're using GitHub co-pilot,
[0:00:26] you can use whichever model you like.
[0:00:28] So in this video, we're going to look at a few different ways
[0:00:30] that you can compose multi-model workflows,
[0:00:33] when and where to use those, and where it's actually already
[0:00:37] built into the co-pilot CLI, and you don't have to do anything at all.
[0:00:42] So if you're ready, let's do it.
[0:00:45] All right, so let's open up co-pilot
[0:00:47] inside of Visual Studio Code as we do.
[0:00:50] So I'm going to say co-pilot, and then what just
[0:00:52] passed dash, dash, yellow.
[0:00:54] And if you've seen my videos before, then you
[0:00:56] know that I alias this to just yellow.
[0:00:58] So it's just one simple command.
[0:01:01] OK, we're in the co-pilot CLI.
[0:01:04] We're in the co-pilot CLI.
[0:01:08] Any minute now, there we go.
[0:01:10] And OK, so we're currently using GPT-54 mini extra high.
[0:01:17] Let's swap right out of that.
[0:01:18] So I'm going to go over here to model,
[0:01:19] and let's go to sonnet.
[0:01:22] And then we have this new reasoning UI down here at the bottom.
[0:01:25] So now a progress bar, it used to be a second menu.
[0:01:28] It's now a progress bar.
[0:01:29] So let's go to, let's do medium reasoning on sonnet 4.6 here.
[0:01:35] And then what I want to do here, let's just start off
[0:01:39] and point out that just because you have sonnet 4.6
[0:01:42] is the model that you're using, doesn't
[0:01:44] mean that that has to be the model that you are restricted to.
[0:01:47] So for instance, if we wanted for this project here,
[0:01:51] which is quite large, but if we wanted to do a, let's say,
[0:01:54] we wanted to do a comprehensive security review
[0:01:58] of this application.
[0:02:00] Now normally, if we wanted to have 5.4 do this,
[0:02:03] we'd have to switch into that model with control S here.
[0:02:06] But what we can do instead is just say,
[0:02:09] do a comprehensive security review using GPT-54.
[0:02:14] We don't even need to know what the correct internal name
[0:02:17] of the model is.
[0:02:18] And co-pilot should be smart enough to figure this out
[0:02:22] and actually dispatch a subagent, which
[0:02:24] will go and use the 5.4 model to do this, which it does.
[0:02:28] And if we hit tasks here, and we go, look,
[0:02:31] here's our comprehensive security review.
[0:02:33] And at the very top here, we can see here in the details,
[0:02:37] subagent details, model, GPT-54 override.
[0:02:41] So we over-road the base model just by specifying
[0:02:44] that we wanted to use a different model.
[0:02:47] Now that you know that, that you can do that,
[0:02:50] things start to get pretty interesting, right?
[0:02:52] Because you can use any model you want at any time.
[0:02:55] So let's go ahead and clear this.
[0:02:58] Let's go ahead and stop this.
[0:02:59] So instead here, what I want to do is I want to now exploit
[0:03:03] the fact that we can use multiple models inside of the co-pilot
[0:03:07] CLI and see what sort of interesting things we can do.
[0:03:11] So if you watch my video on orchestration in Visual Studio
[0:03:14] code, then you know that you can create different agents.
[0:03:17] Now if we look at my agents here, if we look at my agents
[0:03:20] here, these are all the different agents
[0:03:23] that I've actually created.
[0:03:24] So you have a coder, a debugger, a designer, and a planner.
[0:03:28] And then we have this orchestrator agent.
[0:03:30] So let's pull that agent up.
[0:03:32] And if you aren't sure where your agents are,
[0:03:35] if they're not in the current workspace,
[0:03:37] they are most likely in this co-pilot in your home folder,
[0:03:41] dot co-pilot slash agents.
[0:03:43] And then we should see all of our agents.
[0:03:45] So let's pull up the orchestrator agent here.
[0:03:47] And we could do that just by clicking it.
[0:03:49] This is why we like to be in Visual Studio code,
[0:03:51] because we can just command click links and open files.
[0:03:53] And then view them.
[0:03:54] Let me get this nice mark down preview here.
[0:03:57] So let's close this.
[0:03:58] And yeah, let's just take a look here.
[0:04:03] So you can see here we have roles and models.
[0:04:04] We're going to plan using Sonnet 4.6 code using 5.3 codecs
[0:04:08] and design using Opus 4.6.
[0:04:11] I used to think Gemini 3.1 was better for design.
[0:04:13] I take that back.
[0:04:14] I think Opus 4.6 with the front end design skill
[0:04:17] is definitely the way to go.
[0:04:19] And then here's the execution.
[0:04:20] We're going to parallelize.
[0:04:24] In other words, figure out what tasks can be done at the same time
[0:04:27] and do them at the same time.
[0:04:28] Delegate to the right model and then verify
[0:04:31] that the work is done.
[0:04:32] Report back.
[0:04:34] And again, just by specifying the name of the model,
[0:04:37] even though I've used the internal model names here,
[0:04:39] you don't have to get this just right.
[0:04:41] The agent can usually figure it out.
[0:04:43] So let's go back here.
[0:04:45] And let's go back to the CLI.
[0:04:47] And now let's activate this orchestrator agent
[0:04:51] and do something a little bit more complex,
[0:04:54] like a demo that you've seen too many times
[0:04:57] and I apologize, you're going to see it again.
[0:04:59] But let's add dark mode to this application.
[0:05:04] I'm sorry for doing another dark mode demo,
[0:05:07] but it is easy to do.
[0:05:09] This is a requirement, thinking on my part.
[0:05:12] But it is going to require it to understand
[0:05:14] this application quite a bit.
[0:05:16] So first it's going to launch that planner agent
[0:05:18] to research the code base.
[0:05:21] And then it should launch either coders or designers.
[0:05:24] I don't honestly know what it will do.
[0:05:26] And then we'll be able to see those sub agents running.
[0:05:29] So let's hit tasks here and see.
[0:05:32] If we go to plan dark mode implementation here
[0:05:35] and you can see sonnet 4.6, it got on the override.
[0:05:38] Even though we're already using sonnet 4.6,
[0:05:40] it would have over rode with this sonnet 4.6.
[0:05:44] And then as it moves forward, it will delegate off
[0:05:47] to the coder agent or the designer agent will override again
[0:05:51] and use either GPT 53 or Opus 4.6.
[0:05:55] Now we could watch this cook.
[0:05:58] I have another video on orchestration,
[0:06:00] but I want to point out that I'm going to cancel this.
[0:06:03] I want to point out that this is kind of already built
[0:06:06] into the CLI in a lot of ways.
[0:06:09] So for instance, if I say,
[0:06:14] explore this application and tell me what it does
[0:06:17] and how it works.
[0:06:20] Let's go ahead and send that off.
[0:06:22] Now I've sent that off with sonnet 4.6 here
[0:06:25] and I probably should have cleared out the orchestrator agent,
[0:06:28] but hopefully it's smart enough.
[0:06:29] Okay, so you see this explore, explore app structure,
[0:06:32] this explore agent here.
[0:06:34] This is an actual, a built in agent
[0:06:37] inside of the co-pilot CLI and it always uses
[0:06:41] haiku 4.5 to do the exploration.
[0:06:44] So that isn't clear here from the UI,
[0:06:46] but that is what's happening behind the scenes.
[0:06:49] And in fact, if we cancel this,
[0:06:51] we should be able to just ask,
[0:06:52] what agent is used for the explore app structure?
[0:06:58] I'm curious, I don't actually know what it will say here,
[0:07:00] but I think it will out the explore agent
[0:07:02] as being haiku 4.5.
[0:07:04] Let's see here, it will right there.
[0:07:06] C default model haiku 4.5.
[0:07:08] So it's already happening actually behind the scenes,
[0:07:11] even though the orchestrator is specifying some of that
[0:07:14] as well.
[0:07:15] Let's switch out of the orchestrator agent,
[0:07:16] let's go back to the default.
[0:07:17] So we know what we're dealing with.
[0:07:20] Now, the other place that orchestration is built into the CLI,
[0:07:24] we actually recommend that you use the built-in orchestration
[0:07:28] is when you use the fleet command.
[0:07:30] So remember, if we look at my agents here,
[0:07:33] I've got a bunch of these installed.
[0:07:34] I've got the coder, the debug other, the designer,
[0:07:37] and the planner, and then some others.
[0:07:39] These agents are part of this little tiny orchestration
[0:07:43] framework that I called UltraLight here.
[0:07:45] And you can see they're down here,
[0:07:47] and you can install them.
[0:07:48] And even though you're installing them for VS Code,
[0:07:50] they will show up in the co-pilot CLI.
[0:07:53] So once you've installed those,
[0:07:56] if we go back to the CLI here,
[0:07:58] we can sort of back up here and try this a different way.
[0:08:01] So there's a slash command built-in called fleet,
[0:08:04] which enables a fleet of parallel sub-agents
[0:08:07] to go off and do the thing.
[0:08:10] Whatever the thing is that you're trying to do.
[0:08:13] The question is, what sub-agents are being used?
[0:08:15] Well, let's try it out and see.
[0:08:19] Let's go ahead and add dark mode to this application.
[0:08:25] So fleet is essentially GitHub Co-pilot CLI's orchestration
[0:08:29] framework.
[0:08:29] It's like the orchestrator that I created, but it's built-in.
[0:08:33] So what it's going to do is it's going to try
[0:08:34] to pick the best agent for the job.
[0:08:37] And where does it get those agents from the agents that you
[0:08:41] define?
[0:08:41] So in this case, it's starting with the Explorer agent,
[0:08:44] which we know is high Co-4.5.
[0:08:46] We know that now.
[0:08:48] And then it should kick it off to be implemented by,
[0:08:52] I'm assuming it's going to pick the coder agent.
[0:08:54] That just seems to make the most sense to me.
[0:08:57] But that's up to fleet.
[0:08:58] Fleet will actually figure out what can be parallelized,
[0:09:01] and it will then delegate out to the right agent.
[0:09:03] It's essentially doing the part of the orchestrator agent,
[0:09:06] but still using the agents that I defined.
[0:09:09] So if we look at the different agents,
[0:09:11] we have the debugger, the coder, the designer.
[0:09:13] It will pick the right one that I've put in here.
[0:09:16] But you have to create those agents for fleets
[0:09:19] to actually select them.
[0:09:20] But once you do, then fleet will select them here.
[0:09:23] So I'm curious to see what it's actually
[0:09:25] going to pick here in terms of which agent he is.
[0:09:29] So let's see.
[0:09:31] OK, so it picked the coder agent, which is exactly what
[0:09:33] I thought it would do.
[0:09:33] if we go into tasks here, let's look at one of these.
[0:09:37] OK, so it is not clear to me that fleet
[0:09:39] is actually using a different model.
[0:09:41] So I did a little bit more digging,
[0:09:43] and it looks like it actually is using 5.3 codec.
[0:09:46] So what I did was I looked at the usage here.
[0:09:48] And after the thing finished, you can see that on 5.3 codec.
[0:09:52] So we have 1.1 million tokens in and 18.2 thousand out.
[0:09:56] It means that it definitely used that up here
[0:10:00] to do all these coder agents.
[0:10:02] All these coder agents, they
[0:10:03] were using 5.3 codecs.
[0:10:05] It's just that it wasn't showing up in the tasks
[0:10:08] in the model override.
[0:10:10] So just remember, when you're creating your agents here,
[0:10:13] model up the top will specify the model that you want to use.
[0:10:18] Now you can see here there's a squiggly yellow line
[0:10:20] under this, and that's because the models are not
[0:10:23] specified the same way in Visual Studio Code
[0:10:26] and the co-pilot CLI.
[0:10:27] I'm sorry, I know that's confusing.
[0:10:30] But that just is the way that it is.
[0:10:31] And you'll know that you've got this wrong.
[0:10:34] If you have the wrong name here, when you go into your agent,
[0:10:38] like this in the co-pilot CLI, you'll
[0:10:40] see an error appear at the top.
[0:10:42] 5.3 codecs is not available.
[0:10:44] And if we fix that here and come back, exit out, go back in,
[0:10:52] you can see that error is now gone.
[0:10:53] So we know that all of our agents are good
[0:10:55] with the good models in the front matter.
[0:10:57] So fleet is built in orchestration for your agents
[0:11:02] in co-pilot CLI.
[0:11:03] It just works to get it for free.
[0:11:05] Now, one of the things that I always
[0:11:07] want to do is be honest with you.
[0:11:08] And so while you can use Sonnet and you can use Hiku
[0:11:12] and you can use GPT-54 or 5.3 codecs,
[0:11:15] I don't use any of those.
[0:11:17] I always use Opus, and I always use it as high reasoning.
[0:11:22] That's three premium requests.
[0:11:23] I am aware that I am somewhat spoiled
[0:11:26] in that I don't have to pay for these requests
[0:11:28] because I work here.
[0:11:30] It's not really fair, but that is the way that it is.
[0:11:33] And I just want to recognize that.
[0:11:35] So I'm somewhat very spoiled in the sense
[0:11:39] that I would recommend that you just
[0:11:40] set it if you can afford to.
[0:11:42] Set it at Opus 4.6.
[0:11:44] I just forget about it.
[0:11:46] I get the most mileage out of this.
[0:11:48] And in fact, I don't actually use other models
[0:11:50] except in one scenario.
[0:11:54] So I like Opus, but it isn't always correct.
[0:11:57] And sometimes a lot of the time, it
[0:11:59] can be very lazy and cut corners.
[0:12:01] So what I like to do is use multiple models
[0:12:03] to do something called adversarial review
[0:12:06] on the work that Opus does.
[0:12:08] So for instance, in the real world,
[0:12:10] if I was going to implement dark mode in this application,
[0:12:13] I would do it like this.
[0:12:15] I would first go to plan mode.
[0:12:17] I would use Opus, and I would say let's add dark mode
[0:12:20] to this application.
[0:12:23] I don't do anything anymore almost without a plan
[0:12:26] unless I'm asking a very simple question
[0:12:28] or just doing some brainstorming with the model.
[0:12:30] If I'm actually implementing anything at all,
[0:12:33] I always use a plan.
[0:12:35] We just get way better results if we have a plan before
[0:12:38] actually having the model implement what we want.
[0:12:41] And the reason for this is because of the way models work,
[0:12:44] each token is defined by or influenced
[0:12:48] heavily by the previous token.
[0:12:50] And so if you have a plan, then the model really
[0:12:53] has to adhere to that.
[0:12:54] If you don't have a plan, then it's kind of just making it
[0:12:56] up as it goes along, and it will have a tendency
[0:12:58] to hallucinate or just go completely off the rails.
[0:13:02] Planning stops that because it's just exploiting
[0:13:04] the way models work, which is that whatever is up here
[0:13:07] in the context is going to heavily influence what comes next.
[0:13:10] Okay, so our plan's done, and we're not going to accept it,
[0:13:13] we're going to exit the plan mode
[0:13:14] and say that we'll prompt ourselves.
[0:13:16] Now, to this adversarial review, we could ask for it,
[0:13:20] but what we're going to do instead is create a skill to do it.
[0:13:22] So it's easy to do in the future just by asking for it.
[0:13:26] So let's go ahead and create a new session here,
[0:13:28] and let's use the skill creator to do that.
[0:13:31] Now the skill creator, the skill creator comes from skills.sh,
[0:13:36] just like all the skills we use on this channel,
[0:13:38] and it comes from anthropic.
[0:13:40] So that's, I don't know why it's anthropic,
[0:13:43] but it's anthropic.
[0:13:45] That's the one you want.
[0:13:46] And then to use it, you can either just type skill creator
[0:13:49] like this, or you can just ask for it.
[0:13:52] So if we wanted to be specific,
[0:13:53] we could say skill creator here.
[0:13:55] So let's say skill creator, and then we could say,
[0:13:59] create a skill that uses adversarial review
[0:14:02] from multiple models based on whatever the user passes in
[0:14:07] and asks for a review for.
[0:14:09] Make sure to use Sonnet 4.6, Opus 4.6,
[0:14:12] GPT 5.4, and GPT 5.3, Codex.
[0:14:15] Have the models then review each other's results
[0:14:17] and come up with a definitive list of suggestions
[0:14:20] for improvements or changes.
[0:14:26] Okay, and then it calls the skill creator.
[0:14:28] And again, when using skills,
[0:14:30] we always wanna be very explicit
[0:14:33] with which skill we wanna use in the prompt,
[0:14:35] because models are atrocious at figuring out
[0:14:38] what skill you actually want to use dynamically.
[0:14:42] You can pretty much bet that they're not gonna do it.
[0:14:44] So if you want the front end design skill,
[0:14:46] you need to ask for it.
[0:14:47] If you want the skill creator, you gotta ask for it.
[0:14:50] Okay, should this be primarily for code review
[0:14:52] or general purpose?
[0:14:53] We want general purpose here.
[0:14:56] Okay, created the skill,
[0:14:57] and it even created some test cases for the skill.
[0:15:00] Review the rate, limiter, implementation
[0:15:02] for security issues and correctness.
[0:15:05] Yeah, let's go ahead, let's just go ahead
[0:15:06] and actually steal one of these.
[0:15:08] Now that the skill's been created,
[0:15:10] let's just actually check and make sure
[0:15:12] that it's there.
[0:15:13] It's running the evaluation test,
[0:15:14] but we don't wanna do that.
[0:15:15] Let's just look at skills here.
[0:15:17] And it was called adversarial review.
[0:15:19] I don't see it.
[0:15:20] So what that tells me is that it's there,
[0:15:23] but the CLI is not picking it up.
[0:15:25] So what I've noticed is that usually you have to go
[0:15:27] out of the CLI so we can just go back in here
[0:15:30] and I have it alias to yellow and then continue.
[0:15:34] Just let's just continue the very last session
[0:15:36] that we were in.
[0:15:37] It just picks up the very last session that we ran
[0:15:40] and we're right back at it here.
[0:15:42] And now we can see our adversarial skill is there.
[0:15:45] So let's start a new session here.
[0:15:50] And now let's go ahead and paste in the test case
[0:15:53] that it gave us, which was review the rate limiter
[0:15:56] implementation in this project for issues in correctness.
[0:16:00] Now I'm gonna send this, but my guess is it is not gonna use
[0:16:04] the adversarial review skill
[0:16:06] because we didn't specify it, but let's see.
[0:16:09] It doesn't.
[0:16:10] See, it's just kind of skipping.
[0:16:12] Now maybe it's gonna find that I'm curious.
[0:16:14] Let's wait and see if it finds the rate limiter code
[0:16:15] and actually uses this skill.
[0:16:17] My guess is it won't.
[0:16:18] It will just try to do it on its own.
[0:16:20] So interestingly enough, it used the code review skill,
[0:16:24] which is built into the co-pilot CLI.
[0:16:26] It didn't use the adversarial review at all.
[0:16:29] It's exactly what I'm talking about.
[0:16:30] But if we phrase this differently,
[0:16:32] if we said something like run an adversarial review on,
[0:16:37] and then I forget what the actual prompt was.
[0:16:41] And now if we send this, then it should pick it up
[0:16:45] and actually use the adversarial review skill.
[0:16:47] And there it is.
[0:16:48] That's exactly what I'm talking about.
[0:16:49] Have to be specific when it comes to skills,
[0:16:51] that's just how it is.
[0:16:52] And this is why MCP servers are sometimes better
[0:16:55] because models are much better at calling tools
[0:16:57] than they are calling skills.
[0:16:59] I actually think this will improve.
[0:17:00] In fact, I know it will.
[0:17:02] The gaps that we see in models today,
[0:17:04] you have to sort of assume that in six months,
[0:17:06] there won't be there anymore,
[0:17:07] but this is where we are right now on March 29th, 2026.
[0:17:12] In 24 hours, the entire world will be different.
[0:17:15] We'll reevaluate then.
[0:17:17] Okay, so it's launching rounds one through four
[0:17:19] independent reviews in parallel.
[0:17:22] Let's just hang on one more second
[0:17:23] and actually see what it comes up with here.
[0:17:26] What sub agents we get?
[0:17:28] Okay, the sub agents are up.
[0:17:30] Let's take a look at our tasks here
[0:17:32] and we've got five, four codecs and sonnet.
[0:17:34] Let's go into one of these just to make sure,
[0:17:35] yep, model override, perfect.
[0:17:37] So that works really well.
[0:17:39] That's an adversarial review skill.
[0:17:41] And I'm not gonna post that.
[0:17:43] You can create your own adversarial review skills.
[0:17:45] Super easy to do with the skill creator.
[0:17:47] So that's using multiple models in
[0:17:49] the GitHub co-pilot CLI.
[0:17:51] You can do that today.
[0:17:52] And remember, all you have to do is ask for it.
[0:17:54] It's really that simple, just in your prompts.
[0:17:56] And also remember that if you're using fleet,
[0:17:58] it will automatically scale out parallelize
[0:18:00] and then try to pick the right custom agents
[0:18:02] that you have defined for the job.
[0:18:04] That's a rundown of a multi-model used today
[0:18:07] inside of the GitHub co-pilot CLI.
[0:18:10] Thanks for watching.
[0:18:11] And as always, happy coding.
