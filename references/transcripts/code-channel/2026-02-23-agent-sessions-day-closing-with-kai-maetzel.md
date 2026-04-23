---
video_id: 0JPODfK8t5o
title: "Agent Sessions Day — Closing with Kai Maetzel"
url: https://www.youtube.com/watch?v=0JPODfK8t5o
channel: "@code (Visual Studio Code)"
published: 2026-02-23
speakers:
  - Kai Maetzel
  - James Montemagno
topics:
  - agent-sessions
  - model-selection
  - ai-sdlc
  - prototyping
relevance: primary
---

# Agent Sessions Day — Closing with Kai Maetzel

James Montemagno closes Agent Sessions Day with Kai Maetzel by discussing how the VS Code team builds with agents, when to use different models, and how fast prototyping is changing their internal workflows.

## Key Topics Covered

- **Agent Sessions**
- **Model Selection**
- **Team Workflows**
- **Prototyping**

## Links

- https://aka.ms/vscode/109
- https://aka.ms/vscode/insiders
- https://aka.ms/vscode/live
- https://aka.ms/vscode/109blog
- https://aka.ms/awesome-copilot

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Thank you so much, Olivia.
[0:00:01] Hope everyone's having an absolutely amazing agent session's day.
[0:00:05] I'm James Montimagno.
[0:00:06] I get to close out agent sessions day by sitting down with the one and only Kai to talk
[0:00:11] about not just sort of the present of what's happening in VS Code, but also the future
[0:00:15] and how the team has evolved and some pro tips as well.
[0:00:18] So without further ado, let me bring on Kai.
[0:00:20] That's so odd, it's just an honor just to get like a few minutes and we kind of want
[0:00:24] to end the day.
[0:00:25] I want to ask you a few questions.
[0:00:26] I'll say a sound Kai.
[0:00:27] All right.
[0:00:28] That sounds good.
[0:00:29] Perfect.
[0:00:30] Well, you know, the team has been shipping tons.
[0:00:31] Like I just love opening up insiders every morning and there's a bunch of goodies nonstop.
[0:00:36] Just like, you know, the UI is changing, adopting and it just honestly just moving so fast,
[0:00:41] which I actually love and even insiders is not just moving but also stable as well.
[0:00:47] So I think about it this way.
[0:00:48] And the first question I want to ask you is like has agents kind of continue to evolve
[0:00:54] inside of VS Code and how do developers, you know, work with them.
[0:00:58] It's just like the experiences like how do you see it evolving over the next few months
[0:01:04] and sort of the vision of agents kind of being everywhere?
[0:01:09] Yeah.
[0:01:11] I mean, first of all, right, I think they all hit this moment where we realize the capability
[0:01:16] of agents or the models that are actually being used by those agents, right, really, really
[0:01:22] increased.
[0:01:23] And that really changed the nicks of how we spend our time, right?
[0:01:27] How much agentic coding we actually do compared to, you know, the traditional kind of coding,
[0:01:35] writing our code ourselves using NES and completions and these kinds of things, right?
[0:01:40] So that really drastically shifted, right?
[0:01:43] And I think that kind of move will really persist, right?
[0:01:46] And will actually spread like wildfire through the developer community, right?
[0:01:51] Right now we only have a few people who are really agentic first, right?
[0:01:55] And I mean, the as an industry not just the VS VS Code, right?
[0:01:59] But that clearly will change, right?
[0:02:01] And that means the interactions that you have in VS Code proper, like for example, each
[0:02:06] in session management and so on become more primary actions than the actual code editing
[0:02:12] or code reviewing part, right?
[0:02:14] So I think that's really number one, right?
[0:02:16] That that is such something that without any doubt, right?
[0:02:21] Really, really will will continue.
[0:02:24] And it will be like a, like a wave, right?
[0:02:26] There will be significant, right?
[0:02:29] So I think that's number one.
[0:02:30] Number two is people will actually realize that on the one hand models are extremely strong,
[0:02:36] but they have personal preferences and, you know, at what point do they actually accept
[0:02:43] code so that it, let's say it gets on, let's take the extreme point gets auto committed,
[0:02:49] right?
[0:02:50] And all the things that you really feel as someone who runs a project that need to
[0:02:55] happen until you feel good about this, right?
[0:02:58] And that goes like, okay, have a solid plan to start with a solid implementation plan,
[0:03:04] then a solid implementation, then verification and validation, right?
[0:03:09] Then code reviews of all different kinds of, you know, performance, security, all of this,
[0:03:15] right?
[0:03:16] And then really have the agents going through all of the step by step by step, right?
[0:03:20] And then in the end, you feel really comfortable and say, okay, now either I, you still
[0:03:25] go and do some, some review here, well, I feel comfortable that this actually pushes
[0:03:29] out, right?
[0:03:30] What level of tests do I need, right?
[0:03:32] And so on.
[0:03:33] So I think that is where most of the, how should I say, the fine tuning, what the, you
[0:03:39] know, figuring out really what your personal workflow should look like, right?
[0:03:44] What your teams workflow should look like.
[0:03:46] I think that's a lot of the kind of building your own custom agents, right?
[0:03:51] And again, we have this whole infrastructure for building custom agent, you've seen that
[0:03:54] today.
[0:03:55] And so I think that's, that's something that really, you know, a lot of people that invest
[0:04:01] a lot of time.
[0:04:02] And then based on this, I think, they're all done a lot.
[0:04:05] Right?
[0:04:06] And by, I mean, a lot, a lot of what are best practices, what really works, right?
[0:04:11] I think people will start sharing these kinds of ideas among each other, right?
[0:04:15] So we'll see some ecosystem for people who really start, you know, saying, hey, you know,
[0:04:20] I have this particular agent that does this kind of thing really, really well.
[0:04:23] And if you combine it with those other tools that someone else to trade that actually creates
[0:04:28] really good benefits.
[0:04:30] Yeah.
[0:04:31] That's really cool.
[0:04:32] Like I think, you know, when plan, the plan agent was introduced as sort of this first, like
[0:04:37] light bulb moment where you were just like prompting the AI, you can actually work with it,
[0:04:42] iterate with it.
[0:04:43] Really evolve through.
[0:04:45] And kind of what I'm hearing you say is like these agents that we think of today is, oh,
[0:04:49] we have a plan agent.
[0:04:50] We actually have the coding agent.
[0:04:52] But we're actually saying like really in the workflow of how do we turn these agents
[0:04:57] into the full sort of life cycle, right?
[0:05:00] So not just planning implementation, but reviewing, but testing and having that loop.
[0:05:04] Like do you really see like that how we evolve as engineers inside of VS code writing
[0:05:08] code is like, we'll be toggling or do you think we'll be orchestration between all of
[0:05:13] that?
[0:05:14] I think there will be orchestration.
[0:05:15] And the interesting thing is when I say custom agents, right, I'm not necessarily saying
[0:05:19] that there needs to be explicit custom agent as an entity, right?
[0:05:27] Because models get better.
[0:05:28] The next model generation will do some of this by itself and so on.
[0:05:32] But what I really mean is, as I mentioned before, is the workflow I think a piece of code
[0:05:37] needs to go through from an idea to be implemented to be verified and reviewed and
[0:05:42] you know, performance-read security review.
[0:05:46] Verify that it really did what it's supposed to do compared to let's say the plan or the
[0:05:51] thicmers that were part of the plan and so on, right?
[0:05:54] So I think that's really how that needs to come.
[0:05:58] And the easiest way to think through this one is actually through what I would say
[0:06:03] actors, right?
[0:06:05] Let's say I gave my code review agent, I give it the name James, right?
[0:06:09] And I was saying, James needs to review the code and then I'm quite right.
[0:06:13] It's an easy way for me as a human to think through this one, right?
[0:06:16] It's not so very technical, it's very approachable.
[0:06:19] And I think they'll see a lot of this, right?
[0:06:21] So that the humanize these kinds of interactions flows, right?
[0:06:26] Well, not just thinking about this, like, oh, this is a more advanced kind of CI flow or
[0:06:30] something, right?
[0:06:31] Well, I think we will think in actors and that makes it very approachable to us as humans.
[0:06:37] Makes it very easy to give feedback and improve certain kinds of things, right?
[0:06:41] And again, right, you can build this today, the infrastructure is there.
[0:06:45] You can build this today.
[0:06:46] And I think you will see more of this.
[0:06:48] That's very cool.
[0:06:49] Yeah, we've seen how we say all the agents, but also hooks coming out sort of this
[0:06:53] workflow, these handoffs as well.
[0:06:55] Now, like this, well, recently, recently, it appears that posted something about how he's
[0:06:58] using a kind of custom review agent, but having multiple actually one for each different
[0:07:03] model.
[0:07:04] Here's a Gemini, here's a code X, here's a cloud.
[0:07:07] And I set this up and I recently just really found that having models, just like I would
[0:07:13] have you review my code, everyone's going to review it a little bit different.
[0:07:16] Everyone's going to critique in a little bit different in those personalities are very
[0:07:20] unique.
[0:07:21] So I'd encourage everyone to kind of put that kind of actor hat on and say, hey, listen,
[0:07:25] let's run with these different models and kind of put on these hats.
[0:07:29] Let's go see what happens.
[0:07:31] Now, you're putting them against each other, but kind of in a way, but it's just like if
[0:07:34] you're getting multiple code reviews from all of your best friends, you have all of these
[0:07:39] agents and models ready to kind of help you code review and do so much more obviously.
[0:07:43] Yeah, absolutely.
[0:07:45] They do have different qualities, right?
[0:07:47] And we see this.
[0:07:48] And so there is real benefit out of them.
[0:07:50] And when you actually let's say, oh, put right some code and you let code X review the
[0:07:55] code and so on, right?
[0:07:57] Like, code X for example, right?
[0:07:58] Yeah, I just set this conversation right before I came to you is very good at trying to
[0:08:06] figure out if there's, you know, the code has good performance or not.
[0:08:10] And if how performance can be improved, right?
[0:08:12] It doesn't speculate.
[0:08:13] It really goes in and saying, no, no, we've got to do this the right way.
[0:08:16] Let's create the benchmark here and then perform the after, right?
[0:08:19] And figure out what we can do.
[0:08:21] And it's really good at this.
[0:08:22] Why wouldn't you use that particular property of a model in order to review your code, right?
[0:08:28] And I think the beauty here is that we in light with GitHub as our service provider, right?
[0:08:34] Really have this multi model story, right?
[0:08:37] We can use it.
[0:08:38] It's there for everyone, right?
[0:08:41] And so we can really use the best possible model for each job and we can make sure that
[0:08:46] they together actually create a good job side.
[0:08:49] So as I said, people will experiment with this, right?
[0:08:52] We'll see more in the community.
[0:08:54] But I think we will also then change rate.
[0:08:56] What comes out of the box and how that behaves.
[0:08:59] That's awesome.
[0:09:00] I'm excited to see it continue to evolve and the team has absolutely just been like,
[0:09:03] destroying it and crashing.
[0:09:04] And I also love every single morning, like I said, waking up.
[0:09:07] Let's talk about VS code itself, right?
[0:09:09] You know, like really the competitive AI landscape is not just models.
[0:09:12] It's editors.
[0:09:13] It's the whole world of coding and the integrations as well.
[0:09:16] You know, how do you and the team really ensure that VS code really stays super committed
[0:09:21] to its kind of core principles of being open and extensible in the sort of AI first landscape?
[0:09:27] Yeah.
[0:09:28] I mean, like you just said, it's one of our core values.
[0:09:33] So and how do we make sure that we are not violating our own values all by checking with
[0:09:40] them from time to time, right?
[0:09:43] I think that their core part of our development process, right?
[0:09:47] And since, for example, right, the open source, all of our code in the core pilot extension,
[0:09:53] right?
[0:09:54] And so I think that really was obvious that this is where we're going.
[0:09:58] All right.
[0:09:59] So agent loops can be contributed.
[0:10:00] Right?
[0:10:01] We have a bring your own key providers and so on.
[0:10:04] So I think there's a good fair playing field here, right?
[0:10:09] And as I just mentioned with the custom agents, for example, right?
[0:10:12] I also think there's a lot of wisdom in the community, right?
[0:10:15] So that we want to see really flourishing.
[0:10:18] I think that that's number one, right?
[0:10:21] And that together with, you know, as I said, the multi model story that we have, right?
[0:10:27] I think that puts us in a very interesting spot, right?
[0:10:30] We have access to top and the line models, right?
[0:10:35] And we really verify that they all work really well, that you can bring them to users,
[0:10:42] right?
[0:10:43] And that together with the community and also us tracking what's happening across the board,
[0:10:48] right?
[0:10:49] And going with the flow, that's very important, right?
[0:10:52] And then I say going with the flow, it has a lot also to do with, you know, we always
[0:10:56] have been dog-fugers, right?
[0:10:57] You know that, right?
[0:10:58] So we all these use the SQL to Dell V-Ease code.
[0:11:01] Now we're using agents in order to develop the SQL and improve the agentic experience
[0:11:06] and so on.
[0:11:07] That means we are building our own custom agents and they're we realize, oh, there's something
[0:11:10] is missing and we push things forward, right?
[0:11:13] And so that experience from self-hosting, dog-defooting, the experience from, you know,
[0:11:20] what happens around us in the industry, what we hear from our community customers would
[0:11:24] be seeing issues, right?
[0:11:26] That really makes us, you know, moving it, make sure that, you know, people are, you know,
[0:11:31] people have a really good experience.
[0:11:33] As always, I also feel like there's this, you know, the extension ecosystem and opening
[0:11:37] up those extensions to really bring in more we've seen, like, you know, not just, you know,
[0:11:41] bring your own model, being able to bring your own prompts and be able to extend the
[0:11:46] VS code itself, right?
[0:11:47] I think it's like really kind of magical that sort of like the things that are built into
[0:11:52] the box, you as a developer, like you can have the Kai extension that does things that
[0:11:56] Kai wants, right?
[0:11:57] And I, I told us a lot of teams that have come to me, but yeah, but I really wanted to
[0:12:01] do this where my team operates this way and I said, well, build an extension for it, like,
[0:12:05] you can almost do kind of anything.
[0:12:07] How does the team think about that extensibility part, like opening up, like the core of
[0:12:14] VS code, right?
[0:12:15] To enable anyone to build an extension or hooks into VS code, like how does that thought
[0:12:20] process kind of changed kind of over this last year or two?
[0:12:25] I think what changed is what does customization look like, right?
[0:12:33] And before it was always an extension, right?
[0:12:37] And then right, the early extensibility was prompt files, for example, right?
[0:12:46] But also MCP solvers, right?
[0:12:49] And now there's more, there's custom agents as we talked about, there are hooks, right,
[0:12:53] that come into it.
[0:12:55] So I think it's more around the, pretty much a bundling of how you instruct the model, what
[0:13:03] MCP solvers you want to need, right?
[0:13:06] Maybe you need an extension in order to implement a particular kind of tool that you want
[0:13:10] your agent to use, right?
[0:13:12] So I think that's the most common case where people still build extension as we know them,
[0:13:17] right?
[0:13:19] Yeah, right.
[0:13:20] And this funded up kind of creates a new experience for you, right?
[0:13:25] And it allows you to implement the workflow that your team really needs, right?
[0:13:29] But over time, I would actually say that building in a pure extension, as you know it,
[0:13:36] right, is a little bit less of a need as compared to the old days, right?
[0:13:45] It's very more building your rock flows with custom agents, MCP servers and so on, right?
[0:13:50] And now that MCP servers also can create UI within the chat, right?
[0:13:55] There's an additional level of interactive experiences that you can build.
[0:14:02] So yeah, but if you really want to take over, right, you still can create the custom, custom
[0:14:07] edits or custom view all of this, right?
[0:14:10] And there are partners who actually do that.
[0:14:12] And there's a lot more building blocks that you can extend out basically.
[0:14:16] Yeah, that's fair.
[0:14:18] Yeah, I want to ask you a little bit here.
[0:14:21] Just how like the team has evolved over the last few months, the last year, the process is you
[0:14:29] talked a little bit about how the team is developing agents.
[0:14:31] Can you just kind of talk a little bit more about how the VS Code team and its core is actually,
[0:14:36] like you said, adopting these processes and how that sort of impacted the team's workflow.
[0:14:42] Yeah, I mean, there's actually a lot that happened here.
[0:14:48] But let's give you a very simple example, right?
[0:14:51] So you start out and you use an agente workflow in order to create code, right?
[0:14:56] So at the very moment you do this, right?
[0:14:58] So there's, and it's quite standard now that this is automatically reviewed by different models.
[0:15:05] And then only even all of the review comments are actually addressed by this other
[0:15:11] model made, right?
[0:15:12] Then you even look at secure.
[0:15:15] Right?
[0:15:16] And then there are some other folks who actually have built their own complete custom
[0:15:21] Robflows as a set, right, with a whole bunch of different agents and how they interact
[0:15:25] and so on for particular tasks, right?
[0:15:27] Well, not just building the VS Code, we have the engineering system behind the scenes, right?
[0:15:31] That's allows us to do what we do.
[0:15:33] Right?
[0:15:34] And the, for example, replace one component of this engineering system.
[0:15:39] And the person who did that build a whole kind of, you know, army of little agents that,
[0:15:45] you know, have all different rules and responsibilities and, you know, this whole thing
[0:15:49] got rebuilt.
[0:15:51] And, and I think that is something that as a set rate, we learn what we, what we do here,
[0:15:56] we bring this back into the product with different days of extensibility, for example.
[0:16:03] And what is it that really needs to be there to, to allow people to do the same thing?
[0:16:09] That's one, the other one is speed, right?
[0:16:13] And it is quite mind-boggling when you think through this one, right?
[0:16:17] It was always like, there was no shortage of good ideas.
[0:16:20] It was all about execution, right?
[0:16:22] And if you didn't execute the none of your ideas method, right?
[0:16:28] And that is, to some degree, changing, right?
[0:16:32] Because implementation can be done or can be achieved relatively quickly, right?
[0:16:38] And if you just think about this logically looking forward to bed, right?
[0:16:43] Another two, three, four months, right?
[0:16:45] New model, straps and so on.
[0:16:48] Then the time of execution actually shrinks.
[0:16:51] So then you have a lot of time to have good ideas, but then too many good ideas, right?
[0:16:57] This is like, also doesn't draw, right?
[0:16:59] So now it shifts very radically to what is it actually that you built?
[0:17:05] And how do you bring this to users?
[0:17:07] And then you have multiple variations of this.
[0:17:10] So how do you let people play with those different variations and then learn from them?
[0:17:15] And then say, no, this idea here is actually the best.
[0:17:17] Let's go forward with this one, right?
[0:17:20] And then how do we communicate to the outside?
[0:17:23] What we are actually doing, right?
[0:17:25] Because the use to publish it, we still do this.
[0:17:28] That's why it's a region plan, right?
[0:17:30] But if most of the time is actually spent in discussing what you want to do compared to actually
[0:17:36] implementing this, then plans are, you know, and plan that covers an iteration is extremely
[0:17:43] hard because, you know, all of the ideas you have, you might have implemented in a few
[0:17:47] days, right?
[0:17:48] Clearly there's already some long running and so on, right?
[0:17:51] But if you just think about UI changes and so on, right?
[0:17:55] And the actual implementations time shrinks very much.
[0:17:59] And that means you have to adapt as a team how you think about things, how you operate.
[0:18:04] And I think that that really is all happening, right?
[0:18:08] And I think it's happening not just in our team.
[0:18:11] Again, right?
[0:18:12] I think that's really universally happening right now.
[0:18:18] Yeah, and I see, especially because I'm so active watching every single team here at Microsoft
[0:18:23] really adopt and ramp up and new workflows all spurring up all the time in the building
[0:18:28] box continue to evolve.
[0:18:29] You see these continuous light bulb moments happening faster and faster and faster.
[0:18:34] So I want to end it with one kind of fun question for you, Kai, which is like, you know,
[0:18:39] someone today is opening up VS code.
[0:18:41] What's kind of Kai's pro tip basically, like to get the most out of it.
[0:18:46] The thing that you do kind of maybe every day or something that maybe is your favorite
[0:18:50] kind of unknown hidden feature or all of those, whatever you want to go into.
[0:18:56] Oh, I mean, for me personally, right?
[0:19:02] As I said, I'm part of that whole transition into more and more agentic flows.
[0:19:07] And what I realized is that I really, I think I already wolf it in some of my answers earlier,
[0:19:15] right?
[0:19:16] I have an easier time thinking in personalities and actors.
[0:19:21] And so for me, it's much easier to think through this.
[0:19:25] What is trusted code for me?
[0:19:27] And for some of my private personal projects that I'm running, I developed these kinds
[0:19:32] of rock flows in order to see how things are going.
[0:19:35] And it's really easy.
[0:19:36] And it's not hard.
[0:19:39] And it feels like a lot of work needs to go into this, right?
[0:19:42] But it's not really you can actually evolve these things incrementally while you're
[0:19:47] rocking.
[0:19:48] You can use actually, you know, the agentic capabilities in order to evolve the custom
[0:19:54] agents, right?
[0:19:55] You point them at your agent files and ask for modifications and additions and these kinds
[0:19:59] of things.
[0:20:01] And that is just how should I say this is really important, right?
[0:20:06] Because in the beginning, it was all about, you know, the code is the one thing that is
[0:20:11] the most important that you have, right?
[0:20:13] And we removed a lot of other artifacts.
[0:20:16] And now it's actually somewhat not the other way around, but artifacts now is what is
[0:20:21] your project all about?
[0:20:23] What are the customizations in the the workflow, for example, or the hooks that you want
[0:20:28] to have run and so on.
[0:20:29] And you might not have a single line of code at this moment.
[0:20:33] And then you go and actually, you know, start developing your code.
[0:20:38] I think that's that's one of those, right?
[0:20:40] We're really having this in mind, right?
[0:20:41] That customization is the thing that actually brings you to success.
[0:20:46] That's awesome.
[0:20:47] And the last one is we're still humans, right?
[0:20:55] I have to say, I don't get a, you know, a kick out of writing a spec for for an hour
[0:21:02] or something, right?
[0:21:03] That does not what makes me happy.
[0:21:06] I like to, you know, rock incrementally, right?
[0:21:10] My mind is a little bit messy when it comes to this.
[0:21:13] One idea builds on top of the other and so on.
[0:21:16] And what I realized is I, I cannot assume that the code that comes out of this kind of
[0:21:21] incremental process is actually worthwhile.
[0:21:24] So what I'm doing is I did, I incremental this something in, I developed something incrementally.
[0:21:31] Then I create pretty much a spec out of this using H and then saying, you know, give me
[0:21:35] this mark on spec and then I just do a little bit of edits there.
[0:21:38] And then I give it again to do a model and say, now implement the sole thing, right?
[0:21:44] So the first thing is a prototype and the second thing is the thing that I actually want
[0:21:48] to write and I think, yeah, you know, try this up.
[0:21:51] Maybe you also get a good result of this.
[0:21:55] I like that a lot and yeah, stop doing the things that don't make you happy spend more
[0:21:58] time on the thing that do make you happy.
[0:21:59] I think that's a perfect place to end.
[0:22:01] Kai, thank you so much for your time.
[0:22:02] I really appreciate it.
[0:22:04] Thank you for having me and thank you for running agent session day for us.
[0:22:09] Yes, and thanks for the entire team, the amazing sessions.
[0:22:12] Everyone that's been watching at home and as always, happy coding.
[0:22:17] Happy coding.
