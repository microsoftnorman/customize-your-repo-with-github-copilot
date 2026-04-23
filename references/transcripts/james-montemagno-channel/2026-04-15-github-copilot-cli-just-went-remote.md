---
video_id: slmqmAe-fQg
title: "GitHub Copilot CLI Just Went Remote - This Changes Everything"
url: https://www.youtube.com/watch?v=slmqmAe-fQg
channel: "@JamesMontemagno"
published: 2026-04-15
speakers:
  - James Montemagno
topics:
  - copilot-cli
  - remote-control
  - mobile
  - approvals
relevance: primary
---

# GitHub Copilot CLI Just Went Remote - This Changes Everything

James Montemagno walks through remote control for GitHub Copilot CLI sessions, including remote monitoring, approvals, and follow-up commands from the web or mobile.

## Key Topics Covered

- **Copilot CLI**
- **Remote control**
- **Approvals**
- **Session steering**

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:02] Oh, sorry about that.
[0:00:03] I was off actually doing some coding with the brand new feature remote that's now available
[0:00:08] inside the GitHub co-pause CLI.
[0:00:10] It's an awesome feature that actually enables you to start a session on one machine.
[0:00:13] I was just doing control that session from another machine when you're on the go.
[0:00:19] Or for me, for example, why this feature is so important is that I am doing a lot of Windows
[0:00:24] development and Mac development and I'm rotating between the machines.
[0:00:28] This feature enables me to start a session directly on my Mac, for example, with
[0:00:32] my application tiny clips, which is a minibar Mac application that needs Mac build tools
[0:00:37] to actually verify the build itself.
[0:00:40] I can start that session on the GitHub co-pause CLI and pick it up directly on my Windows
[0:00:45] machine when I'm at work or when I'm on the go.
[0:00:48] You can access it directly from the browser and send the exact same controls and even
[0:00:52] interact with plan mode, auto-poly mode, and a lot more.
[0:00:55] As a killer feature that I'm super excited as coming out and I can't wait for the future
[0:01:00] of it as well as it comes out of public preview and hopefully into GA into the future.
[0:01:03] What I want to do is break it down, show you what it looks like to use and do some coding.
[0:01:09] I think you're going to dig it as well.
[0:01:11] Let's get into it.
[0:01:21] Here I am inside my Mac terminal.
[0:01:24] We're going to go ahead and co-pilot banner this.
[0:01:26] I get the nice beautiful co-pilot banner.
[0:01:29] Boom, we're going to go.
[0:01:30] In this tiny clips application, this is my Mac application.
[0:01:36] I do need my Mac build tools and Xcode actually build and compile this.
[0:01:39] That's really important as it's generating code to do normal builds.
[0:01:42] The first thing I'm going to do here is I'm going to search around and look at some
[0:01:46] of the features that I have.
[0:01:48] There is this feature that I want to implement.
[0:01:50] You have selection navigate single frames in the video editor.
[0:01:53] I'm going to go ahead and tap on that and say, let's come up with a plan.
[0:01:58] We go into plan mode here.
[0:02:00] This is my normal work stream.
[0:02:02] I've opened my terminal.
[0:02:03] I'm getting to work.
[0:02:04] Now I could be 10 minutes in, 30 minutes in, an hour in, 50 minutes in, whatever it is.
[0:02:10] I'm coming with my plans.
[0:02:11] I'm even doing implementation.
[0:02:14] Then something happens.
[0:02:17] I need to go ahead and hand off to finish the work.
[0:02:20] Have a few ways of doing that.
[0:02:21] We're going to explore those here and use the new remote feature.
[0:02:25] Let's go ahead and figure out this plan and see what we're going to implement here.
[0:02:32] We're going to go ahead and answer a few questions and get our plan in place.
[0:02:37] Our plan is here.
[0:02:40] This is looking pretty good.
[0:02:43] I'm able to then exit the plan mode, accept the plan, or suggest change.
[0:02:46] I'm going to exit plan mode.
[0:02:47] I'm going to prompt it myself because one of two things probably will have just happened
[0:02:52] at this point here.
[0:02:53] In this case, I have my plan or working on work and I need to go do something.
[0:02:58] I didn't need to leave this machine.
[0:02:59] I got to go back to work.
[0:03:00] I got to go off to do an appointment.
[0:03:03] What am I going to do?
[0:03:04] There's a few things I could do.
[0:03:06] First, I could go in and I could say,
[0:03:06] I should delegate.
[0:03:07] Now, this is going to send the session to GitHub and the GitHub Co-opout coding agent and
[0:03:13] create a pull request basically to implement this feature in functionality.
[0:03:17] This is a great feature.
[0:03:18] Use it all the time, especially from my mobile phone, to create new agent sessions.
[0:03:22] The problem here is that these are going to be kind of a Linux instances and it's going
[0:03:26] to be one office.
[0:03:27] Actually, an interactive experience or a kind of, as you can steer it as it goes.
[0:03:31] It's a handoff, right?
[0:03:34] I'm handing it off if I want to delegate.
[0:03:36] I love this feature.
[0:03:37] That's one option.
[0:03:39] Of course, it could just like could resume this session later, but let's go ahead and
[0:03:42] use the new remote feature here.
[0:03:45] It's going to enable steering our session from the GitHub web and mobile.
[0:03:49] Here, we get not only a link to remote steer.
[0:03:55] I can also do control E and get a whole QR code.
[0:03:58] I could pick that up on my phone, for example, which is huge.
[0:04:00] It obviously minimizes down.
[0:04:02] But I'm also going to do something here is inside of our slash commands.
[0:04:06] There are a bunch of features here as we can see.
[0:04:09] The one specifically that we're going to look for is keep alive.
[0:04:12] This is pretty nice if you're having a long-running session.
[0:04:14] This was just released.
[0:04:16] That's going to enable you to prevent your system from going to sleep.
[0:04:19] I'm going to say on, and turn that on to.
[0:04:22] I was not necessarily required, but it's a nice one here.
[0:04:24] I'm going to go ahead and click on this.
[0:04:26] We're going to be brought directly into that agent session here.
[0:04:30] We can see that we have, for all intents and purposes, our full session,
[0:04:38] a bunch of other sessions that I've been running as well, right here.
[0:04:41] We can see the full plan that's been implemented, everything like this.
[0:04:44] We also see that I'm in interactive mode.
[0:04:46] I can do plan mode, or I can do autopilot mode.
[0:04:49] Let's say, hey, let's just build the app to make sure it is in a working state.
[0:04:57] Again, I'm here on my Mac, and I'm here directly interacting with this remote session.
[0:05:04] I'm going to see that it's thinking.
[0:05:07] If I pull up my terminal, we can see that it's thinking here too.
[0:05:10] What we're seeing in real time is our terminal coming over, interacting with this remote
[0:05:17] session here and building the application.
[0:05:21] Now, this is pretty neat, but again, I'm on my same local machine.
[0:05:26] Of course, if I'm managing the different sessions in my browser, that's nifty.
[0:05:30] The real power is when you go to a different machine, where this is continuously being run over here.
[0:05:36] Let's head over to my Windows machine now and check that out.
[0:05:40] Here I am on my tiny clips repo.
[0:05:42] I went over to the agents tab, and as we scroll down, we can see that, yeah,
[0:05:47] I have a current terminal session planned for issue 58 that was created.
[0:05:52] Now, here, as we scroll down, we can see that the plan was approved.
[0:05:55] When you see the build is green, I'm going to say, hey, let's go ahead and implement that plan.
[0:06:02] So now, on my Windows machine, directly back here in the browser,
[0:06:07] I'm able to do interactive sessions, and then again, I could go ahead and move into autopilot or
[0:06:12] plan mode to carry on that existing session.
[0:06:17] Now, what's going to take this plan and is going to do a full implementation, and then at the end,
[0:06:25] it is going to continue off and then build that project again.
[0:06:31] Because the CLI in that session is running directly on my terminal, it is able to then go ahead
[0:06:41] and build that application on my Mac, which is crazy powerful.
[0:06:48] All right, well, that is off implementing features.
[0:06:50] You can see here that it says, only you can view remote sessions.
[0:06:54] So you can tap and get more information here and understand access control, right?
[0:06:58] So these sessions, they're here in public preview today, and then you can also try this
[0:07:02] out on mobile for test flight and Google Play, and that's going to land in the mobile application,
[0:07:06] which is going to be one of my favorite ways of using this to have access to my full Mac
[0:07:10] machine from my mobile device.
[0:07:12] Now, I was going to do it from the browser today as well.
[0:07:14] So you can see this all here as this is implementing and streaming in.
[0:07:17] And what happening is the CLI is going to go give updates back and forth.
[0:07:21] If you also head over into the change log, you can read more about this.
[0:07:25] Not only how I showed you how to use it today, but you can also do co-pilot dash, dash,
[0:07:29] remote, and just interactively start up that session.
[0:07:31] And then you can go ahead on that repo and spin up multiple of these sessions,
[0:07:34] you're working on multiple features.
[0:07:36] You can dive through this and more on how to update and how to go ahead and spin up new
[0:07:41] sessions and leverage existing sessions.
[0:07:44] So again, if I wanted to, I could just say co-pilot slash remote and then get another remote
[0:07:48] session as well.
[0:07:50] So let's head back over to our Mac and see what's happening here.
[0:07:52] Now that we can see that the implementation is starting directly here on my Windows machine,
[0:07:57] but happening over on my Mac.
[0:08:00] Okay, I'm back over here on my Mac, and I'm just kind of switching around machines,
[0:08:04] because I actually have a single machine here on my Mac mini setup, which is a mon now,
[0:08:07] and I have my Windows laptop that I'm over recording on, switching back and forth and capturing.
[0:08:11] So here, if we scroll down, we can see that we're seeing file edits take place where we can
[0:08:15] see all that in line, whether I'm here on my Mac machine or on my Windows machine,
[0:08:19] and then we can also see the implementation is continuing.
[0:08:22] Now, it's only given a certain update, right?
[0:08:23] If I was actually to bring over and see this here, because there's a lot more things happening
[0:08:28] inside the terminal, and it's giving us the main thing here.
[0:08:32] But the important part here is that it's getting edits, it's building, it's compiling,
[0:08:37] and seeing all that happen together.
[0:08:39] And again, now if I wanted to come over, I'm just going to go ahead and say CD,
[0:08:44] go here, say copilot dash, dash, remote, just like that.
[0:08:49] And now we're going to get another remote session spun up as well.
[0:08:53] So here, I kind of as many of these remote sessions as I want, ready to jump between them,
[0:08:58] which is super, super cool, right?
[0:09:00] Implementing these features and jumping between Windows, Mac, Linux, mobile, and so much more.
[0:09:07] All right, there you go.
[0:09:08] That is the new slash remote feature part of the GitHub copilot CLI.
[0:09:12] I'll link to the change log as well.
[0:09:14] And of course, follow the GitHub change log on Twitter or on the main feed for all the updates
[0:09:21] coming out, not only in GitHub copilot CLI, but the entire world of GitHub and GitHub
[0:09:25] copilot as well.
[0:09:26] Now, this is a killer feature that I'm going to be using every single day,
[0:09:29] because I'm coding all the time on the go.
[0:09:31] And being able to have a session linked on my direct machine, give me all the tools and
[0:09:36] capabilities that are super powerful.
[0:09:38] Let me know if you're going to give this feature a try in the comments below or if you've already
[0:09:42] given a try.
[0:09:43] And what's your thing?
[0:09:44] All right, this is going to do it for this video.
[0:09:45] So as always, if you liked it, thumbs up,
[0:09:47] jam the subscribe button and thanks for watching.
