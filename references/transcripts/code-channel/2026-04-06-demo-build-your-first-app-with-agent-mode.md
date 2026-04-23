---
video_id: hmfldW7dmgw
title: "DEMO - Build your first app with agent mode"
url: https://www.youtube.com/watch?v=hmfldW7dmgw
channel: "@code (Visual Studio Code)"
published: 2026-04-06
speakers:
  - Gwyneth Peña-Siguenza
topics:
  - agent-mode
  - plan-mode
  - demos
  - app-generation
relevance: primary
---

# DEMO - Build your first app with agent mode

This final VS Code Learn episode demonstrates building a URL shortener from scratch with agent mode and plan mode, turning the earlier conceptual videos into an end-to-end workflow example.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | In this session |
| 00:17 | Demo - Creating a URL Shortener App using Plan Mode |
| 07:18 | In Summary |
| 07:59 | Wrap |

## Key Topics Covered

- **Agent Mode**
- **Plan Mode**
- **End-to-End Demo**

## Links

- https://aka.ms/vsc-learn

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] In the last video, we took a look under the hood into the Agent Debug Logs in the chat
[0:00:06] Debug View. And this video, our goal is to put everything that we've seen in these series of
[0:00:12] videos and build something using Plan Mode. So let's dive right in.
[0:00:17] Alrighty, let's put everything we learned together. I have a brand new project. You can see here,
[0:00:23] if I open my Agent Debug Logs, there's nothing here. If I open my Show Chat Debug View,
[0:00:30] we only have the list of the models and then Content Exclusion, nothing else, fantastic. So I'm going
[0:00:36] to open up GitHub Co-Pilot Chat and I'm moving to Select Plan Mode. As you saw previously, we were
[0:00:44] building a URL shortener. We did some CLI stuff, but then we're like, no, we want to refactor to an
[0:00:50] API and then we wanted to build a frontend. And there's a lot of sort of scattered work. Ideally,
[0:00:56] we would just outline it in a plan, go have a back and forth, right? So I'm going to go ahead
[0:01:01] and dictate here what I want. Let's create a URL shortener using Python 3.14,
[0:01:09] SQL Light 3 built-in Python module and use UV for dependency management. Also create a very
[0:01:19] simple frontend with HTML and static files. The frontend should have a field where we can type in
[0:01:26] the URL we want shortened. And then at the bottom of that, just an element that will display
[0:01:35] the short-end URL that we can click on and that will be opened in another tab. Let's keep the UI
[0:01:42] great. And I think for a plan that is fine, I'm going to scooch this over a little bit here. And
[0:01:49] this model is fine, the thinking effort is fine as well. I'm going to go ahead and send this here.
[0:01:54] And another thing I forgot, but I do want to add here is can we also have a UI element that
[0:02:04] allows us to provide the short URL and it tells us what the original URL is. And then I am going to
[0:02:14] send this off, but actually here we have a functionality of plan mode, which is to ask us questions
[0:02:20] to better understand what we're trying to implement, right? And it's asking the web framework. I do
[0:02:26] want to use fast API. That's correct. And how should the short URL be generated? And random
[0:02:32] short string or hash URL actually here, we're going to say use base 62 for encode slash decode.
[0:02:45] And can we also have a UI element here and we're going to go ahead and send this up follow up.
[0:02:51] This will allow the plan to now consider the messages that I sent as clarification, right? So the
[0:02:58] goal is for you to outline your work. This is kind of one of the more popular methods where it's
[0:03:04] your focus on planning your work, fully understanding what the employment before actually
[0:03:09] switching over to the implementation of the work here. So I'm going to take a look here,
[0:03:14] a minimal URL shortener that looks good, UV corn, that looks good, back in, that looks good,
[0:03:21] encode, that looks fine, all right. And vanilla perfect, that looks good. Okay, great. That
[0:03:28] actually looks fine. Now we can, for the implementation, we can click on start implementation. This
[0:03:35] will also allow us to continue in the cloud or in co-pilot CLI. We can also go ahead and click start
[0:03:40] with autopilot, which will essentially set this to autopilot. And I'm just going to click start
[0:03:46] with autopilot. So this switch over to agent mode is switches it into autopilot mode. And this
[0:03:51] means all the commands that it needs to run are going to be auto approved, right? And I'm going to
[0:03:57] switch into chat debug mode. We see things are being added here. And then in our agent debug logs,
[0:04:03] we can see that tool calls and all that good stuff is being added here as well as the agent is
[0:04:09] working. Now we can see it has a task list here. It's got two of seven. And then I can also steer
[0:04:15] here if I wanted to. I can say something like make sure the UI has a dark theme. There we go. And
[0:04:25] again, we have the option to stop and send add to queue or steer with message. I'm going to go ahead
[0:04:30] and steer with message. And then we may or may not see this to do sort of change, right? So right
[0:04:37] now it's outlined the first init UV create base 62 create database create main dot pi. So it's
[0:04:44] continuing there, right? The user wants a dark theme for the UI. Let me continue with the
[0:04:48] implementation to make sure the CSS has a dark theme. And it's going to create main dot pi, the
[0:04:54] style that CSS and the static index HTML. So it's continuing the work here. And we see it's updated.
[0:04:59] It's to do for the create static dial that CSS to dark theme. Right. So you can also make these
[0:05:05] changes as it continues to work. So I'm going to actually create this or close this, I should say,
[0:05:11] and close this here just so it's a little less distracting. But as you know, if you ever want to
[0:05:17] dive into what is going on, all the cool calls to the LM, all the tool calls and such, you can do so
[0:05:24] by reviewing those debug views here. So we're going to let this run. I'm going to go ahead and expand
[0:05:29] our session here. And I'm going to create a new one. We can run this on local. And we can say
[0:05:34] something simple like right, a read me on our project, right? And then we can send this off
[0:05:41] and then this is running. And now we see both sessions are running. So we can focus on either one
[0:05:48] really. Now this one looks like it's verifying startup, which means it should be close to be
[0:05:54] in done. And then we can see that the read me is working through reading all the files that it needs
[0:06:00] to create this proper read me or the read me session, I should say. All right. So I'm going to move
[0:06:06] this over here. And I'm going to expand the terminal area. And then I'm going to click on the
[0:06:11] hidden terminal because that is where the agent is running. It's commands at the moment. And it
[0:06:16] looks like it executed the command in the terminal and ran everything. And it should be just
[0:06:22] about ready to wrap up its work. Now we're going to be running this command in a second. So I'm
[0:06:29] just going to cut. Oh, it looks like it ran it once more. And it is running a proper get redirect
[0:06:35] test fantastic. Well, let's give that a moment to finish. All right, it looks like it has tried to
[0:06:41] shorten the github.com slash feature slash co-poly URL fantastic. So it looks like it is running
[0:06:49] up in this one out. Yeah, it looks like it's still running. I told this here. The Dev Server is running
[0:06:53] out here. So I'm going to go ahead and open this up in the browser. All right. Now this is clean looking.
[0:06:59] I'm going to go ahead and provide a URL shortened fantastic. So if I click on to this year,
[0:07:06] open new tab, it is correctly routing fantastic. And let's say I want to look up one look up
[0:07:13] and fantastic works exactly as expected. And that is it for this video. We understand how plan mode
[0:07:20] works. We understand that we can have a back and forth conversation with the agent before actually
[0:07:26] implementing any work. We can provide clarifications. We also were able to steer the direction there.
[0:07:32] And then finally, we are able to kind of see the end results of everything put together. Now
[0:07:39] that is it for this introductory section of videos. We're going to dive deeper into the github
[0:07:45] co-pops CLI into customizations of your agents into using MCP servers in a bunch, bunch more.
[0:07:53] So you have the foundation here. And now you feel free to explore all the other topics that we
[0:07:58] have.
