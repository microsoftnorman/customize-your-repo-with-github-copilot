---
video_id: 6K5UW594BUc
title: "Ralph loop vs Copilot CLI Autopilot + Fleet mode"
url: https://www.youtube.com/watch?v=6K5UW594BUc
channel: "@BurkeHolland"
published: 2026-03-06
speakers:
  - Burke Holland
topics:
  - copilot-cli
  - autopilot
  - fleet
  - agentic-workflows
relevance: primary
---

# Ralph loop vs Copilot CLI Autopilot + Fleet mode

Burke Holland compares a Ralph loop pattern against GitHub Copilot CLI's built-in Autopilot and Fleet modes for hands-off task execution.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | What is a Ralph Loop |
| 01:51 | How a Ralph Loop Works |
| 06:06 | Copilot CLI Autopilot + Fleet |
| 08:08 | Checking progress |
| 10:58 | Comparing the Results |
| 15:21 | The Verdict |

## Key Topics Covered

- **Copilot CLI**
- **Autopilot**
- **Fleet mode**
- **Agent loops**

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] to Ralph or not to Ralph.
[0:00:03] That is the question.
[0:00:05] And in this video,
[0:00:06] we're going to take a look at Ralph,
[0:00:08] specifically Ralph Loops,
[0:00:10] what they are, how they work,
[0:00:12] how you can use one with the GitHub Copilot CLI,
[0:00:17] and whether or not that's even a good idea.
[0:00:22] So if you're ready, let's do it.
[0:00:25] Okay, so in a standard agent interaction,
[0:00:28] like when you're just working with the agent in chat,
[0:00:31] it looks something like this.
[0:00:33] You have a chat session, which is this,
[0:00:35] this outside box here, and then there's a prompt,
[0:00:37] and then you get an agent response,
[0:00:39] and then what happens?
[0:00:41] You send another prompt,
[0:00:43] and then you get another agent response, right?
[0:00:47] And it just keeps going, and it goes,
[0:00:49] and it goes, and it hopefully, eventually,
[0:00:52] right out the other end here, you have an app,
[0:00:55] or whatever you're trying to create.
[0:00:57] In a Ralph loop, you're kind of taken out of the picture
[0:01:01] in the agent iterates on what's called a product requirements
[0:01:05] document, which we talked about in videos before,
[0:01:09] to do the entire implementation for you.
[0:01:12] And it looks pretty much like this.
[0:01:15] It's just a while loop with a prompt
[0:01:17] that gets passed to Copilot.
[0:01:20] Now, if you've only used Copilot in Visual Studio Code,
[0:01:24] you might think, well, how does that,
[0:01:26] how would that work?
[0:01:27] Because I can't just pass a prompt to Visual Studio Code
[0:01:29] in a loop like that,
[0:01:32] but you can with the Copilot CLI.
[0:01:34] So I'm gonna show you two different ways to do this.
[0:01:36] One of them is with the Ralph loop,
[0:01:38] we're gonna look at the standard Ralph loop,
[0:01:40] and then we're gonna look at autopilot and fleets,
[0:01:43] which is built into the CLI.
[0:01:45] See which one of these two is better,
[0:01:47] which one gives us better results.
[0:01:48] So let's first look at the actual Ralph loop.
[0:01:52] Okay, here's an example of a Ralph loop.
[0:01:54] This is it.
[0:01:54] It's just a bash script.
[0:01:56] Up here we have a counter.
[0:01:58] The counter is one to 1,000.
[0:01:59] It could be one to 100, it could be one to 10.
[0:02:01] So whatever you want,
[0:02:02] this is just how many times you want the loop to run.
[0:02:05] And then what it's going to do is,
[0:02:07] it's going to go through,
[0:02:08] and it's going to call Copilot here,
[0:02:12] passing dash dash yellow,
[0:02:14] which just means approve all tool calls and dash P.
[0:02:17] When you call Copilot with dash P,
[0:02:19] let me show you what happens here.
[0:02:20] If you didn't know that you can do this,
[0:02:22] you can call the Copilot CLI,
[0:02:23] so Copilot, you've dash P,
[0:02:26] and then whatever your prompt is, right?
[0:02:28] So if I say say hello to chat here,
[0:02:31] then this will get passed to the model.
[0:02:34] The model will generate a response,
[0:02:36] charge me three premium requests to say hello to you.
[0:02:40] And there it is.
[0:02:41] And then it just exits back to the terminal,
[0:02:42] right? It's a non-interactive session.
[0:02:45] And because you can do that,
[0:02:47] you can call this over and over and over again
[0:02:50] inside a while loop.
[0:02:51] And then we're passing in the contents of this prompt.md file.
[0:02:55] So let's take a look at that.
[0:02:57] So the prompt just tells the agent what to do.
[0:03:00] It tells it read the PRD to see which user stories
[0:03:04] and user stories are just describing
[0:03:07] how a feature should work are unchecked.
[0:03:09] And then it refers to the progress.txt.
[0:03:11] This is another important part of the Ralph loop,
[0:03:14] which we'll talk about here in a second,
[0:03:16] where we're going to store learnings
[0:03:17] and patterns from previous iterations.
[0:03:20] Pick the first unchecked, unfinished, undone user story
[0:03:24] and implement one in one only.
[0:03:27] Then test your implementation manually
[0:03:29] using the agent browser skill, which I added,
[0:03:32] commit your work, check the item off.
[0:03:35] And then right here,
[0:03:36] append any learnings about what you did
[0:03:40] to progress.txt.
[0:03:42] Now, this is a core principle of Ralph.
[0:03:44] And that is that every time that loop gets called,
[0:03:48] it starts with a fresh context window.
[0:03:50] So it has no idea what was previously done.
[0:03:53] And the idea here is that as the context window grows,
[0:03:57] the agent makes mistakes and that it will see those mistakes
[0:04:02] and it may be inclined to make the same mistakes again.
[0:04:04] And so by providing a fresh context window,
[0:04:07] but always giving it the learnings of the past run,
[0:04:11] that the agent theoretically is getting smarter as it goes.
[0:04:14] It gets to start over with fresh learnings each time.
[0:04:18] Now, the PRD here is a PRD to port
[0:04:23] and applications.
[0:04:24] The same application I show you in every video
[0:04:26] from Blazor static web apps over to JavaScript.
[0:04:31] And we'll take a look at that application
[0:04:33] at the end here and see how the two methods
[0:04:37] that we had did at actually porting that.
[0:04:40] I created this using plan mode in the copilot CLI.
[0:04:44] I basically just said,
[0:04:45] I want to port this application to JavaScript.
[0:04:48] I let it ask me questions.
[0:04:50] And then I said, save that plan as a PRD.
[0:04:52] And this is what we got.
[0:04:53] There's a lot of general guidelines up here at the top.
[0:04:57] But if we scroll down,
[0:04:58] then you'll start to see the actual things
[0:05:01] that need to be done.
[0:05:02] These were very specific.
[0:05:04] And this isn't really as much a PRD as it is a plan,
[0:05:07] but it's a checklist of things that actually need to be done.
[0:05:10] Usually when you see a Ralph loop,
[0:05:11] it'll be something like the user should be able
[0:05:14] to click on the button or there should be a green button
[0:05:17] in the right corner.
[0:05:18] And so in that case,
[0:05:19] the agent is actually implementing the feature
[0:05:21] and deciding what that is.
[0:05:23] We're using it for a port.
[0:05:24] So it's not quite the same,
[0:05:26] but there's no one right way to do a PRD files.
[0:05:30] It's just a way to track what needs to be done,
[0:05:32] what has been done and what remains to be done.
[0:05:35] That's essentially the Ralph loop in a nutshell.
[0:05:39] Now, how do you run a Ralph loop?
[0:05:41] You run it in the terminal.
[0:05:43] So let's do that.
[0:05:44] It's just the file and you run it.
[0:05:48] And that's it.
[0:05:49] And this is going to run,
[0:05:50] let's see how many iterations did we put in here.
[0:05:54] We've got 100 iterations.
[0:05:55] So it's gonna run 100 times
[0:05:57] or it's going to run until it sees that all stories
[0:06:02] are complete and it will respond with complete.
[0:06:06] Okay, we're gonna let this Ralph loop cook.
[0:06:10] You can see that it's cooking here.
[0:06:11] It's already going through and doing the thing.
[0:06:14] While it does the thing, let's jump over
[0:06:16] and let's look at autopilot in the copilot CLI.
[0:06:20] Autopilot is very similar to a Ralph loop
[0:06:23] in so much as its main goal is to get the agent to run
[0:06:27] until everything is finished.
[0:06:30] But it doesn't work the same way.
[0:06:33] So for instance, in autopilot mode,
[0:06:36] the prompt that we're gonna pass is really simple.
[0:06:38] Just implement the PRD, put the app in an app subfolder,
[0:06:42] which I had for the Ralph loop as well.
[0:06:44] Work and commits and then check all of your work
[0:06:46] with the agent browser skill.
[0:06:49] None of the orchestration here we have to worry about at all.
[0:06:53] Autopilot handles that behind the scenes
[0:06:56] and we could dig into how that works exactly
[0:06:59] the way that it sort of gets the agent to look
[0:07:01] for a higher order completion token of greater confidence.
[0:07:05] But it's just another way to get the agent
[0:07:08] to keep going, keep going, don't stop
[0:07:10] because you may run this on a massive code base
[0:07:13] that takes hours or days to complete.
[0:07:15] And you need that agent to keep running
[0:07:17] until everything is finished.
[0:07:20] So let's see how we actually run this with autopilot.
[0:07:22] I'm gonna shift tab into autopilot mode,
[0:07:26] you need to do it's green here.
[0:07:27] And then all I'm gonna do here is I'm gonna tell it
[0:07:29] to implement the prompt, but we're gonna use
[0:07:31] an additional feature of the CLI called fleet.
[0:07:36] And fleet allows it to deploy a fleet of sub agents
[0:07:41] that can work simultaneously.
[0:07:43] So the copilot CLI will figure out which jobs
[0:07:47] can be done at the same time
[0:07:48] without stepping on each other and it will parallelize
[0:07:51] that work with fleet.
[0:07:53] And then I'm just gonna pass in the prompt
[0:07:55] and I'm gonna mention it with the at syntax here.
[0:07:58] I rarely use the syntax, but in this case, this is perfect.
[0:08:01] And then we're just gonna send it.
[0:08:05] Now, while this cooks, let's go back and check on Ralph
[0:08:10] and see how Ralph is coming with that implementation.
[0:08:14] So it looks like Ralph has created the application here
[0:08:17] in the folder and it is going through
[0:08:20] and starting to complete this PRD.
[0:08:24] If we look at the progress here,
[0:08:25] it doesn't look like it's logged any progress yet.
[0:08:28] And if we look at the PRD, my guess is it has not checked
[0:08:31] anything off, which means that it is still on phase one.
[0:08:35] So it hasn't actually checked anything off yet.
[0:08:38] It's going through and actually setting up all of the scaffolding
[0:08:43] that's needed for this project.
[0:08:44] It's initializing a Git repo.
[0:08:46] It's adding things to the Git ignore,
[0:08:48] making sure node modules is excluded.
[0:08:51] Agents are crazy smart these days.
[0:08:53] It's so much fun to just watch them work
[0:08:55] and watch what they do.
[0:08:57] Okay, so now it's marked the story is complete.
[0:08:59] And if we go to progress, we'll actually see some of the learnings
[0:09:02] that it has.
[0:09:04] So it's said it's created a React 19 plus V'd app
[0:09:07] installed in front of dependencies, learnings.
[0:09:10] NPM create VLatus prompts for V8 beta pipe into skip,
[0:09:14] node 25 works fine for all dependencies.
[0:09:17] Is that super important for the next run to know?
[0:09:21] I don't really know.
[0:09:21] Doesn't seem like it, but this is what Ralph will do.
[0:09:25] It will just continue to loop and iterate
[0:09:27] until this entire thing is done.
[0:09:30] So let's jump back and check on autopilot with fleet
[0:09:33] and see what it's up to.
[0:09:34] What autopilot does is it creates these to-do's
[0:09:37] in the SQLite database that comes with the Co-pilot CLI.
[0:09:41] If you didn't know that, and there is a SQLite database there,
[0:09:44] it's created it to do.
[0:09:45] And then for each one of the items that needs to be done over in the PRD,
[0:09:49] and then it's kicked off these tasks.
[0:09:52] It's task, general purpose task, task.
[0:09:54] These things are all running simultaneously.
[0:09:57] And we can look at those if we do slash tasks.
[0:10:00] We can see everything that's currently running.
[0:10:02] So it's creating an index.
[0:10:03] It's porting the global CSS, scaffolding the project,
[0:10:06] and it looks like it's already downloaded the static assets.
[0:10:09] And I can hit enter again to sort of just drill in here
[0:10:12] and see exactly what happened in this agent.
[0:10:16] And then we're going to bounce back out.
[0:10:18] So we have multiple things happening at one time.
[0:10:21] A parallelized setup with the autopilot and fleet.
[0:10:26] And that's being powered by that slash fleet.
[0:10:30] I've let these things run to completion.
[0:10:32] I actually did this yesterday because it takes a while.
[0:10:35] For the Co-pilot CLI, it took about 45 minutes to finish this.
[0:10:38] And for the Ralph Loop, it took almost a full day.
[0:10:41] Really long time.
[0:10:42] I had it on a lot more loops though.
[0:10:44] I had it on 1,000, but it took a really long time.
[0:10:46] So what I want to do now is jump in and look
[0:10:49] at the different implementations
[0:10:51] that we got from those two methods.
[0:10:53] And let's compare and see which one of those
[0:10:55] gets us closer to the real thing.
[0:10:57] OK, this is the app that it's supposed to be porting
[0:11:00] from Blazer ASP.NET to JavaScript React VIT.
[0:11:06] You've probably seen this before.
[0:11:07] If you've seen any of my videos, it's always the same demo.
[0:11:10] You can add a new link here.
[0:11:11] Let's add GitHub.com.
[0:11:13] Let's add Microsoft.com.
[0:11:15] Let's add this great side.
[0:11:18] And then we get a bunch of links down here.
[0:11:20] We can drag and reorder these.
[0:11:22] We can have a vanity.
[0:11:25] Oop, looks like the advantage is taken.
[0:11:27] So we want to get a new one.
[0:11:28] And then we can publish this.
[0:11:30] And then if you go to this URL, you
[0:11:32] would see this live right now.
[0:11:34] I can go to my lists.
[0:11:35] I can manage these lists.
[0:11:36] Go back in, add remove links.
[0:11:38] That's the site.
[0:11:39] It's got a dark mode.
[0:11:41] So what we want to see is how well did these two things
[0:11:44] port the application?
[0:11:46] So the first one we're going to look at is Ralph.
[0:11:48] So let's take a look at Ralph.
[0:11:50] So this is Ralph.
[0:11:51] Now let's go back and compare because we
[0:11:53] wanted a pixel perfect match.
[0:11:55] And we don't have it.
[0:11:57] So here's the original.
[0:11:58] And then here's Ralph.
[0:12:00] And so the header's a bit off.
[0:12:02] That icon is too small.
[0:12:04] The highlight is overlapping.
[0:12:07] I did get the imagery right.
[0:12:08] It got this nice subtle arc down here, correct?
[0:12:12] All of this looks right.
[0:12:13] If I put in a URL, that OK.
[0:12:16] This page actually looks far worse.
[0:12:20] So let's go back here.
[0:12:21] If you remember, it should look like this.
[0:12:27] And instead, we got this.
[0:12:29] So still functional.
[0:12:32] But it doesn't look great.
[0:12:34] If I drag, OK, so that works.
[0:12:37] And then can we log in?
[0:12:40] Looks like we can.
[0:12:42] And can we publish?
[0:12:45] Doesn't look like that worked.
[0:12:47] And if we go to my lists, that does not look like the my lists
[0:12:50] page.
[0:12:52] OK.
[0:12:52] So we got some work to do on this.
[0:12:55] That's not a one for one port.
[0:12:57] This application, by the way, looks simple, but it isn't.
[0:12:59] I've been over this before.
[0:13:00] It's pretty complex.
[0:13:01] And so it's a hard thing for a model to one shot.
[0:13:04] Let's just see if the dark mode worked.
[0:13:09] Yeah, looks pretty good.
[0:13:10] OK.
[0:13:11] Now let's take a look at what autopilot plus fleet
[0:13:13] was able to pull off here.
[0:13:16] OK.
[0:13:17] So in this case, if we compare to the home page, this looks a little bit better.
[0:13:21] The logo is still a little small.
[0:13:23] The text here is too dark on the autopilot.
[0:13:28] We can see here and here and here.
[0:13:30] But it got the color right.
[0:13:31] It didn't make this mistake, the mistake that Ralph made of having this be
[0:13:36] a different color.
[0:13:37] Now does it actually work, paste to URL.
[0:13:40] OK, so that's not what we said at all.
[0:13:42] What we said was example.com.
[0:13:45] So not a pixel perfect match there.
[0:13:47] If we put in Google, oh, interesting.
[0:13:50] So Ralph picked up on the fact that it doesn't have to have a protocol.
[0:13:56] You shouldn't have to type the HTTPS.
[0:13:59] Ralph picked that up.
[0:14:00] Autopilot did not.
[0:14:02] But if we add it here, can we add a link?
[0:14:05] We did not get the open graph info.
[0:14:06] Let's try to add one more.
[0:14:10] Add it GitHub.
[0:14:11] OK, that's how we did get the open graph info.
[0:14:14] So that's big because that's done on the server side.
[0:14:17] That's a function that runs on the server.
[0:14:20] It looks like we would need to fix it coming from the home page,
[0:14:22] but we did get it here.
[0:14:25] We can move things around.
[0:14:26] Can we log in?
[0:14:28] Sign in with Google?
[0:14:31] We cannot log in.
[0:14:32] So it's difficult for us to test the My Links page.
[0:14:35] If we go there, I don't believe we can even go there.
[0:14:38] If we're not logged in, we cannot.
[0:14:40] So finally, I just want to test the 404.
[0:14:43] This is the 404 that the site has with this global green
[0:14:46] creature.
[0:14:47] Here's the 404 from Ralph.
[0:14:49] Looks pretty good.
[0:14:51] There's the 404 from Autopilot.
[0:14:53] And actually, for comparing Autopilot and almost nailed it.
[0:15:00] Ralph didn't quite get it right.
[0:15:01] It's a little too small there.
[0:15:03] So you can see that neither of them got it exactly right.
[0:15:07] But remember that both are dependent on the PRD
[0:15:09] that I gave them.
[0:15:10] So we could go back and look at the PRD
[0:15:13] and see if I actually gave them the information required
[0:15:16] to do this pixel-perfect port.
[0:15:18] My guess is I did not.
[0:15:21] Now, the question is, should you use Ralph or should you use Autopilot?
[0:15:24] Well, let's looking at the results here.
[0:15:27] I would say that Autopilot probably
[0:15:29] did a slightly better job than the Ralph loop did.
[0:15:33] But there's some other major differences here.
[0:15:35] First of all, the Autopilot finished way faster.
[0:15:38] I think it was something like 45 minutes.
[0:15:40] Second of all, Autopilot is one go.
[0:15:43] So that's three premium requests to implement this whole port.
[0:15:47] For the Ralph loop, it's three premium requests
[0:15:50] on every single loop.
[0:15:54] So that's for a hundred times.
[0:15:58] That's 300 for a thousand.
[0:15:59] That's 3,000 premium requests.
[0:16:02] It's still odd.
[0:16:03] It's not the most bang for your buck by a long shot.
[0:16:06] And it is not evident to me that having an empty context window
[0:16:09] makes a difference in quality here.
[0:16:12] So my vote is Autopilot and fleets because of cost,
[0:16:16] because of quality, and because it's built into the tool.
[0:16:18] So it's just simpler to use.
[0:16:21] There's no shell script to stand up.
[0:16:22] No loop to write, nothing like that.
[0:16:24] Just very simple.
[0:16:26] So to Ralph or not to Ralph, in my opinion, not to Ralph.
[0:16:32] But my demo is contrived.
[0:16:34] There are going to be places where Ralph is probably
[0:16:36] a better option.
[0:16:37] And you need to just know that you have that option.
[0:16:41] You can stick the Co-Pilot CLI in a loop
[0:16:43] and run it over and over again.
[0:16:45] And that's OK to do, by the way, by the terms and conditions.
[0:16:48] I checked with the PM on that product.
[0:16:50] And that's OK to do.
[0:16:51] Your premium requests use them how you want to.
[0:16:54] So as always, user works best for you,
[0:16:58] whether that's Ralph or Autopilot with fleet,
[0:17:01] what works for you is all the matters.
[0:17:04] Thanks for watching.
[0:17:05] And as always, happy cutting.
