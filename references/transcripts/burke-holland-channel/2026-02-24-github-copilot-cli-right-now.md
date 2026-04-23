---
video_id: CqcqWLv-sDM
title: "You need to try the GitHub Copilot CLI right now"
url: https://www.youtube.com/watch?v=CqcqWLv-sDM
channel: "@BurkeHolland"
published: 2026-02-24
speakers:
  - Burke Holland
topics:
  - copilot-cli
  - terminal-agent
  - plan-mode
  - autopilot
relevance: primary
---

# You need to try the GitHub Copilot CLI right now

Burke Holland introduces GitHub Copilot CLI, covering setup, terminal workflow tips, plan mode, and Autopilot.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Intro |
| 00:54 | Setup |
| 08:15 | Essential Shortcuts |
| 14:30 | VS Code Tweaks |
| 17:35 | Plan Mode |
| 25:50 | Autopilot |

## Key Topics Covered

- **Copilot CLI**
- **Plan mode**
- **Autopilot**
- **Terminal workflow**

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] the GitHub Copilot CLI. Yes, we have another tool and I've been talking a lot about it on X or
[0:00:08] Twitter, whatever you want to call it. And that's because I actually like it a lot. And one of the
[0:00:13] things I want to do on this channel is just always be really honest with you about what I think
[0:00:19] works and what I think is just shenanigans. And the Copilot CLI just really works really well.
[0:00:26] It's become my daily driver. And so in this video, I want to kind of walk you through
[0:00:30] how to get started with it. So it's a bit of a beginner video. But at the same time,
[0:00:34] I'm going to show you some of the things that I do with it, some tweaks where I actually use it,
[0:00:39] some of my workflows. And we'll actually build something in this video as well because that's
[0:00:43] the only way that you can really watch or learn to see how the Copilot CLI is actually used in real life.
[0:00:50] And so if you're ready, let's do it. All right. So to get started, obviously, the first thing
[0:00:56] thing you're going to want to do is install the CLI. So you can just Google that. You'll know
[0:01:00] how to do that. And then just click the install now button right now that takes you to a GitHub page.
[0:01:08] I think this is going to be improving shortly, but just find your installation and then install
[0:01:12] here was on a Mac. So I did a brew install. Now, the next thing you're going to want to know is where
[0:01:17] should I run this thing? Should I run it in the system terminal or how should I do this? So I'm going
[0:01:21] going to show you how I do it, which is that I always run it inside a Visual Studio code with the
[0:01:26] project that I'm working on open. And so let me show you what I mean and why I do this. So for this
[0:01:33] video, I've created a folder called the CLI video. So let's just move into that here in the
[0:01:39] terminal. And you'll notice I have the terminal on the right and the editor on the left here. And
[0:01:44] that's intentional. You'll see why here in just a second. Okay. So with our terminal open here,
[0:01:51] we actually want to open Visual Studio code on this folder. We don't have to do that to run
[0:01:56] the CLI, but Visual Studio code has this concept of being open on a folder. And so we want to keep
[0:02:04] with that concept here just to make it easier on our brains. So I'm going to run here code insiders
[0:02:12] the dot in a dash R. And it just says open the current folder in the existing window.
[0:02:17] So now we've done that. You can't really tell other than we have the title up here. It's open
[0:02:22] that sidebar again. And if you're wondering how I actually got the terminal here in the sidebar,
[0:02:26] what you have to do is from the bottom panel here from the bottom panel, you just drag these
[0:02:32] things and drop them there. So if you didn't know you can do that, you can. That's how I got
[0:02:36] the terminal over here. Now, I don't even though we're in the terminal, I don't run the CLI
[0:02:43] in the terminal per se. I run it over here in the editor space. And to do that, what you can do
[0:02:50] is just say a terminal. And if you look for terminal in editor, you can create a new terminal in the
[0:02:55] editor space like this right here. I do this a lot. And so what I do is create a keyboard shortcut.
[0:03:02] And then what we're going to do here is just look for terminal in editor. Then here, it says
[0:03:09] create new terminal in editor. And you can see I have that set to control option t because I do
[0:03:16] this a lot. And so control option t and we get new editor instance here or a new terminal instance
[0:03:21] rather in the editor space. Now, let's go ahead and fire up the CLI. So we're just going to type
[0:03:27] copilot. And here's the CLI. Now, the first time you do this, you'll get a nice animation and you'll
[0:03:32] have to type slash log in to actually log in, but I've already done that. So you're not going to
[0:03:37] see that here. All right. So with the copilot sale, I up, let's just do a quick tour of the interface
[0:03:43] here. You can see it's telling us that we can type at to mention files slash for commands
[0:03:48] your question mark for shortcuts. Now, I mostly use slash commands. We'll talk about some of the shortcuts.
[0:03:56] I hardly ever mentioned files. In fact, we don't even have one in here. But if we were to say, create
[0:04:01] a simple read me here, it will create a simple read name for this project. And then what we could do
[0:04:07] is just mention the file here. So we might want to say, you know, spruce up this read me. And
[0:04:14] you'll notice that saying, do you want to create this read me? And I do, but I don't want to have
[0:04:18] to tell the CLI every single time that it's okay to do something. And so what could do is say,
[0:04:23] yes, and don't ask for file operations. Again, it's going to ask me this every time it tries to
[0:04:27] do a tool call. So I'm going to say, yes, but I'm going to come back to the CLI here. And I'm
[0:04:34] going to say allow all like this. And when we do this, we're turning on what's essentially
[0:04:40] also referred to as yellow mode. So it's never going to ask me again for permission. And I want
[0:04:45] the full agenda experience. That's what we're going to do. Now, I like to alias this as well from
[0:04:50] the command line. So I'm going to press control C twice to jump out here. And from the command
[0:04:57] line, you can launch it in this boat by doing co pilot dash dash yellow, which gives you the exact
[0:05:02] same thing. It's just auto approve on my default. So I don't like to take that. So what I do is
[0:05:08] I just alias it so that I can just type yellow and I get the exact same thing, co pilot in
[0:05:14] allow mode. And if you're like, I don't know how to create an alias. Well, that's why we use the
[0:05:19] VS co terminal because co pilot is built in there as well. Right. So if you don't know, then you
[0:05:24] could just ask, command or control eye on windows, right? Say alias co pilot alias co pilot dash
[0:05:32] yellow to yellow, right? And it will create that alias for you. Whether or not your in power shell or
[0:05:39] bash doesn't matter. So this is why we like the VS co terminal because it has AI built in and that's
[0:05:44] command or control eye. Because we still need to be in the terminal. We're still going to have to do
[0:05:48] things. We want to have co pilot there with us as well, not just in the CLI. So let's go back into
[0:05:54] our session. And the session that we had, there's two ways to get back to it. So if we say co pilot
[0:06:00] dash dash resume, this will bring up a list of our recent sessions here. So you'll get to see
[0:06:05] I've been working on a lot of stuff. So simple remi right here. It's the top one here right there.
[0:06:11] You can see over is working on some project ideas as well. So we could resume that way. The other
[0:06:17] way that we can resume here is we could just do, we could do this. We could say co pilot
[0:06:24] dash dash continue. And this will just resume the last session we were in, which is the session
[0:06:29] that we just left. And speaking of aliasing, something that we could do here that's kind of fun is
[0:06:34] we can say alias co pilot dash dash continue to CPR. Right. And so essentially,
[0:06:43] so it's going to add this to my ZSH file. I'm going to go ahead and let it do that. And then we have to
[0:06:48] reboot our shell here. And then once we've done that, if we just had CPR, that will just resume
[0:06:54] the last session that we were in. So here we are. So if we kill it, get back to the terminal,
[0:06:59] that's fine. CPR bring it back to life. Get it? All right. Okay. Now, the next thing that we want
[0:07:05] to do here is look at some of the slash commands that we're going to use a lot. So obviously,
[0:07:10] model or models is a big one. This is select the AI model that you want to use. I'm seeing
[0:07:16] Opus 4 6 is the default. I don't know if that's actually the case for everybody. And I know
[0:07:21] if that's the case for you as well in your company, but you can see all of the models we have
[0:07:24] access to here. And again, if you don't see these, your company, if you have a company sub,
[0:07:29] maybe controlling what you can and can't see. Okay. And so that's why they may not be present in this
[0:07:34] list. Additionally, you'll see some models here. Let's say hidden for me. And that's because
[0:07:39] these are not public models. These are either internal models or they're not their preview models.
[0:07:44] And so I have these hidden here just so they don't confuse you as to why aren't those in my
[0:07:49] model list. Well, because they're not available to everyone just yet. So we're going to be on
[0:07:54] cloud Opus 4 6. I'm a huge fan of Opus. 5 3 is great. And we're actually going to use 5 3.
[0:08:01] But not not directly. And I'll explain why here in just a second. So this is how we could change
[0:08:06] our model if we wanted to in our reasoning levels. If you want to change the reasoning level, pick
[0:08:12] the model and then you can change the reasoning level. Now let's look at some shortcuts that
[0:08:17] you're going to use a lot. So one that I keep using that you've seen me use a bunch here is just
[0:08:21] control L. And that just clears the screen. Doesn't start a new session. Just clears the screen.
[0:08:26] And so what we can do here is look at some of the other commands that are super important. So
[0:08:32] what other commands do I need to know? One of them is control A, which is going to take you back to
[0:08:41] the start of the line. And the other one is control E, which is going to take you to the end of the line.
[0:08:46] And there's not that things you can do like control K, which I think deletes all of the
[0:08:50] all of the text after the cursor it does. And if you want to see what these are, you can just do
[0:08:56] a question mark here. And you'll see here they are control T, control O, control E.
[0:09:02] Editing is what you're looking for right there. So you can look at that at any time to see what
[0:09:06] those are. But those are the ones that I use the most. It looks like control U to delete to the
[0:09:11] beginning of the line. So if we had a longer prompt control U, delete to the beginning of the line,
[0:09:16] good to know those shortcuts. Okay. Now I talked about how I had a custom agent. You can set up
[0:09:23] your own custom agents here by just doing slash agent. And then you can see I've got a couple of
[0:09:28] them here. And then agent, let's like if we were going to create a new agent here, we could put it
[0:09:33] in either the user config, which is available to every project or just this project.
[0:09:39] An agent is just a prompt file, which gives the agents some instructions, but they're very,
[0:09:45] very powerful. In fact, I believe there's not a lot you can't do with custom agents. You can
[0:09:52] solve pretty much any workflow problem with them. But if we were going to create one, let's just
[0:09:58] call this a test agent here. It's just a test. And again, these are just, we're just showing how to
[0:10:05] to create a custom agent here. It's not going to do anything. And then in here, we would say
[0:10:08] something like, you know, you are a coding agent, always follow this workflow. And then the agent's
[0:10:15] been created. And it's created here. You can see it right there. And if we click this, we'll actually
[0:10:20] open it in Visual Studio code. This is another reason why we like to be in VS Code when we're
[0:10:25] using the terminal, because if we command click on links when given them from the terminal to files,
[0:10:32] they open right here. This is super powerful. I can't undersell this enough that the terminal on its
[0:10:38] own is great. But when you need the file editing capabilities, they want to see the file. You just can't
[0:10:44] beat this experience. You definitely want to be in Visual Studio code. Okay. Now I talked about a custom
[0:10:51] agent I have here called anvil. And that's the one that we'll be using today. And you can get this.
[0:11:02] If you go to burkalland.kdub.io slash anvil. And then it's just a plug in. And so these plugins
[0:11:09] are supported by the copilot CLI. This one is on GitHub. If you just look for the anvil repository,
[0:11:15] you can see how I created a plug in. And this plugin has a custom agent and the context seven MCP
[0:11:21] server. And again, and then there's a front end design skill here that I'm recommending that I
[0:11:26] don't give that to you because there's another place that I want you to install that from.
[0:11:30] So when you run this, you'll get the context seven MCP server and the agent. And you can know
[0:11:35] that that's the case. Good MCP here. You can see context seven is there and context seven just
[0:11:41] allows the agent to read docs as markdown files. That's it. The anvil custom agent does quite a
[0:11:49] bit more. So the agent really tries to force the model to use context seven a lot to use fetch a lot.
[0:11:57] And then it forces it to do what we call adversarial reviews or essentially to check its work with
[0:12:03] GPT53 codecs and Gemini, which is one of the hidden models that I'm using here. And the reason why
[0:12:09] I'm doing this is because I really like opists very agentic. It likes to please. It wants to do
[0:12:16] the work, but it doesn't always do the best job. GPT53 on the other hand is very rigid. It's not
[0:12:21] very much fun to work with, but it only does exactly what it's asked to do. So if we put these two
[0:12:26] things together, we get better results out the other side. Now, the last thing I want to show you
[0:12:31] before we get started here is this front end design skill, which I've recommended. So skills,
[0:12:36] if you haven't watched my video on my video on skills, should check that out, but they're just
[0:12:43] mark down files. There's a great one called front end design. And I recommend that you have it.
[0:12:50] It does front end design to install it. You're just going to copy and then come down. And then you
[0:12:55] want to run this in your terminal. Now, this is a really good opportunity for us to see a
[0:13:01] couple different ways to do that. So one of the ways is we could just open our terminal here to
[0:13:05] the side and execute it there. That's probably the easiest way. If you actually wanted to cancel
[0:13:12] out of the CLI, which you could do is press Ctrl C twice. And that just ends your session.
[0:13:18] And then we could run the command. However, there's a different way to do this. That's kind of unique.
[0:13:24] So let's bring our session back here with CPR. One of the things that's built into Linux,
[0:13:30] this is a Linux only thing they're about to show you is if you press Ctrl Z,
[0:13:34] it will suspend the process. And in this case, that's the CLI. And then we can run this other
[0:13:40] command to install the front end design skill, which I'm not going to do because I've already
[0:13:44] installed it here. And then if we want to bring this back, if we just hit F G, which is short for
[0:13:51] foreground, then it will bring the process back. And it's back. So there's a couple different ways
[0:13:57] that you can either drop out of the CLI or get back into the CLI. It's probably easier though
[0:14:03] to just have your terminal instance open and do these things over here and leave these things open.
[0:14:08] Now, another thing that we've got here is that up here at the top, if we have multiple terminal
[0:14:14] instances, it's not really easy for us to tell what's what. And the reason for that is because it
[0:14:20] just says node up top. So if we open another terminal instance here, and we have co pilot running
[0:14:25] over here as well. So let's yellow into this one. Now we don't really know like what's happening
[0:14:31] over here and what's happening over here. They both just say node. So there's a fix for this. If
[0:14:36] you go to settings, UI. And then what we're looking for is terminal title. And then you can see
[0:14:44] terminal tabs title here might be a little small. And what you want to do is you want to set this to
[0:14:50] sequence, right? This, this one right here. So let's just copy this, come down. We're just going to set
[0:14:55] it to sequence like this and then hop out. And then when we do that, you can see here what we've got
[0:15:00] at the top is a little bit more of a descriptive definition of what's actually happening. So in this
[0:15:06] one, as you as we go along, you'll see that what it does is it actually updates these titles with
[0:15:11] the title of the chat session, which is super nice. So you can see what's actually happening.
[0:15:16] One more tip I want to give you and it's a lot of logistics before you'd start it is that
[0:15:21] when you're running the terminal in a tab like this, it swallows a lot of the shortcuts that
[0:15:26] you're used to. So the command B works for me, but it won't work for you. And I can zoom in and I can
[0:15:31] zoom out, but it won't work for you. And to fix this, what you need to do is go to user settings
[0:15:36] and then you want to look for terminal integrated, I think it's just commands to skip shell.
[0:15:46] That's what we're looking for here. So you can see here, these are the different commands.
[0:15:50] Basically what we're saying is don't pass these commands to the shell, let VS Code handle them.
[0:15:55] And really the three that I add are zoom in, zoom out and toggle sidebar visibility. That's it.
[0:16:01] And then once you add those, then your keyboard shortcuts will start to work as you would expect
[0:16:07] them to. So that's a quick fix there for that. Now, got a lot of setup here. We've done a bunch.
[0:16:14] Let's go over and let's start to build something. And the question is always, well,
[0:16:19] what are we going to build? And I always build the same thing. So let's look at that.
[0:16:23] If you've watched some of my other videos, I always build this site. And the reason why I build
[0:16:27] this site is because it looks trivial, but it's actually not. So it's a site for sharing links.
[0:16:34] If we add a link here, we can add another link. Oh, it's ad microsoft.com. Let's add GitHub
[0:16:40] dot com slash copilot. Right. And then up here, we can add dope links. Oops, it's already taken.
[0:16:50] And so there's a lot that's going on here. We can publish, but we have to log in to publish.
[0:16:55] And so then we could see all of our links and then here's the links that we can we can reorder
[0:17:00] these. And then we can give somebody a single URL and they can share it with the world like this.
[0:17:05] All right. So I've logged in. If I hit publish, now we get this URL. And if you were actually to go to
[0:17:10] this URL right now, you will see this list of links, which I've created here. And I there was some
[0:17:15] others already in there. Say it to local storage. That's why you see some duplicates. So we want to
[0:17:19] recreate this site. That's the task that we're going to be doing with the agent. So let's jump back
[0:17:25] into the CLI and learn some more as we do this. So we want to build this thing. How are we going
[0:17:30] to do that? So first, I'm going to switch to my agent. I'm going to go to anvil. Now, the next thing
[0:17:35] we want to do is we want to do a plan because we're starting from, you know, absolute zero.
[0:17:41] There is nothing here. And this is a very special scenario to be in. It's one you may not be in. If
[0:17:47] you're not building green field projects, right? If you're working with existing projects,
[0:17:51] you may be in different scenarios here. But because we don't have anything,
[0:17:54] you really need to plan first. Whenever I'm doing this, and I have to give this thing
[0:18:00] quite a large prompt because I'm about to try to describe what I want. I don't want to type this.
[0:18:04] I want to speak this. And so to do that, I'm going to use the built-in voice-to-text support in the
[0:18:10] operating system for a Mac, you'll need to go to settings. And then in settings, you want to just
[0:18:22] look for a keyboard. So find keyboard here. And then under keyboard, you're going to look for
[0:18:27] dictation. Turn that on. And then set the shortcut to press Ctrl key twice. If you're on windows,
[0:18:33] I'm pretty sure it's already on. It's just windows key H. Okay. So I'm going to, I'm about to dictate
[0:18:40] a prompt in and we're going to create a plan. But we want to be in a special mode to do that,
[0:18:45] which is plan mode. So I'm going to hit shift tab, which is going to take me to plan mode.
[0:18:50] And then I'm going to start planning. So let's do it. I'd like to create a site called the
[0:18:59] URL list. The whole point of the site is to allow users to create lists of links and then share
[0:19:08] them with one URL. So the site is essentially a home page that describes what the site does with
[0:19:15] a big prominent input that says create your first list. And then after the user puts a link in,
[0:19:22] it takes them to a compose page where they can continue to put more links in. And as links are put
[0:19:28] in, the open graph data for those links is fetched from the internet so that each link has a nice
[0:19:34] icon title and description. The user can edit those titles and descriptions or they can take them
[0:19:40] as is. They can also reorder the items in the list using drag and drop. Additionally, they get
[0:19:47] to create a vanity URL. But these vanities have to be unique and the list can also have a description.
[0:19:53] Now once they have all this, they can publish the link, the list and make it public. In addition,
[0:20:01] they also have a my links page where they can see all of their links and they can edit those
[0:20:06] lists of links at any time from that my links page. To do this, I want you to use Firebase as a
[0:20:14] backend. I've installed the Firebase CLI and I've logged in. So feel free to create whatever
[0:20:19] resources you need. If you need something from me, just ask. The addition has always used the front
[0:20:26] end design still. You're building so that we have a nice beautiful site. I'm going to give you
[0:20:33] some design inspiration for that site. That was kind of a long prompt here. I'm going to press
[0:20:40] shift, enter to go down. You can see at the bottom, I said I was going to give it some design
[0:20:44] inspiration. We're going to do that. Let's jump over to the browser and we're going to go to
[0:20:49] color.adobe.com. We're going to look for just a nice palette here. Let's look for explore
[0:20:57] and then spring. I like light pastel colors. Let's look what we've got here. This is really pretty.
[0:21:04] You can imagine that might make a really pretty site. This one here's nice. I like this. I'm going to
[0:21:09] click on it here. I'm going to do is say copy as CSS. Let's go back. I'm just going to paste
[0:21:16] all of this in. There's a lot of lines so you won't see them. If we were because we are in
[0:21:21] Visual Studio Code, let's create a new tab here. We can just paste in and look. You can see
[0:21:26] what's really interesting about this is not only is it describing the color to use, but
[0:21:32] it's also describing white bush roses on a background of blue sky in the sunlight.
[0:21:38] The AI is going to look at that and it's going to translate that into design. We're literally
[0:21:42] giving it inspiration in the form or shape of CSS classes, totally fascinating. Let's not save this
[0:21:52] and we're going to go ahead and send this. This is a massive prompt. I basically just said
[0:21:59] whatever was on the top of my head and now the agent, Opus 4.6 is going to go to work here and
[0:22:05] it's going to try to create the plan for this. Now you can see here, it looks like we're not in
[0:22:11] yellow mode. Let's do yes and let's go back and do allow all. If you remember, that's how we
[0:22:16] get into yellow mode. Permissions are now enabled. Good. So it won't ask me anymore.
[0:22:23] And I may speed this up a little bit so that you don't have to watch the AI think,
[0:22:28] but it looks, I see you already have a project called Linklist. So I've done this demo before.
[0:22:32] Should I use that existing project? Let's create a new one just over starting from scratch here.
[0:22:38] How she users authenticate. Let's start with just Google sign and we'll just start with that.
[0:22:44] What front and framework to use? Interesting. I didn't specify any part of that.
[0:22:48] React plus Vite recommended. Next. Okay. All right. React plus Vite sounds good. Let's stick with that.
[0:22:55] Where should it be hosted? We want it hosted on Firebase. Everything is going to be on Firebase.
[0:23:00] Should creating a list requires signing in first. Now this is a good catch. So yes, sign in
[0:23:08] required. No, anyone can create, but only signing users can manage. So I think what we want here
[0:23:14] is anyone can create a list, but only sign in users can publish them. If the user is not logged in,
[0:23:26] they can create the list, which should be saved to local storage.
[0:23:32] Right. So there we're not getting an option we like. So we're providing some steering and
[0:23:38] some specification to the planning. And we're not writing any code right now. The agent isn't
[0:23:42] writing any code. All it's doing is helping us gather all of the requirements that we actually need
[0:23:48] to build this because otherwise it's going to have to do a lot of guessing and it's going to
[0:23:51] guess incorrectly because it's an AI. It's not a mind reader. Now it's gone off to create the plan.
[0:23:56] I should point out that in a normal workflow for myself, at this point, I will move on to something
[0:24:02] else. So I'm not going to sit here and just watch it. What I'm going to do is I'm going to create
[0:24:06] a new instance of Visual Studio code and I'm going to start to build something else or I'm going
[0:24:11] to go back and work on something else. So for instance, I've been working on a mobile app
[0:24:17] for iOS that is a chat app that works the way that I want it to work. So I'm going to go back here
[0:24:24] and I'm going to start working on this chat app. Normally, this is what I would do. I would let
[0:24:30] this other thing cook in the background. And then periodically, I'm going to go back and check
[0:24:35] and it looks like the plan mode is done. I'm just in time. Now you can see we're getting a couple
[0:24:39] different options here except plan and build on autopilot except plan and build on default. So I'm
[0:24:43] actually going to take any of that. I'm just going to hit escape to just completely cancel out of
[0:24:47] that. I'll explain why here in a minute. So you can see it's created the plan here. And if we
[0:24:52] remember, if we command click this, then you can see the plan right here. So here's the plan.
[0:24:57] And you can see it's actually quite long. It's laying out the data structure. It's laying out all
[0:25:05] of the pages, the routes, the cloud functions that are needed, the security rules. There's a lot.
[0:25:10] And ordinarily, if we weren't making just a demo video, we would go through this, review it.
[0:25:16] It doesn't, you don't have to review it in intense detail. You just discretize every detail.
[0:25:21] But you do need to go through and think about the different things that are happening and
[0:25:24] just see if anything pops out to you as being a red flag. That's generally what I do.
[0:25:28] But since we are making a video, we want to implement the plan. And so what we're going to do
[0:25:33] instead here is we're going to switch into, I'm going to do shift tab, and we're going to go into
[0:25:37] autopilot mode and autopilot. You can think of it as like the copilot CLI version of a
[0:25:43] Ralph loop. Okay? If you don't know what a Ralph loop is, it's essentially just putting the agent
[0:25:48] in a while loop and the agent just runs and runs and runs and it keeps being fed back its own
[0:25:54] result until it gets to this point where it's looked at its own output so much that it feels
[0:26:00] really confident that it's implemented things correctly. That's built into the CLI. I love this
[0:26:05] feature. It's called autopilot. We're going to leave it on anvil. Right? And we're just going to say
[0:26:10] implement. Now, we could mention the plan file here if we wanted to with the app, but we don't need
[0:26:15] to. We're just going to say implement the plan and then let it cook. Now, this is going to take a
[0:26:22] second. So I'm going to go off and work on some of the things and we'll come back and see exactly
[0:26:27] what's happened here and what we got. See you in a minute. All right. So I'm coming back to you here
[0:26:31] before this is actually finished. So we can take a look at a few things that are happening while
[0:26:36] this thing is running. So one of the things that we can do while it's running is we can look at
[0:26:41] the different background tasks. So you can see that it's doing an adversarial review with
[0:26:44] 5, 3. The hidden model is Gemini with Opus 4, 6. So if we hit slash tasks, we can see each one
[0:26:51] of these and we could dig in and see which what happened here. Right? So we can see that it looks like
[0:26:57] Gemini found some SSRF and open graph cloud cloud function critical severity. Right. And so it's going
[0:27:03] to take this open Opus. They're going to figure out between the two of them. So you can check in on
[0:27:08] background tasks that way, including background terminal processes. Someone escape and escape
[0:27:15] again to go back. Now the other thing that I want to show you here, which is quite fascinating,
[0:27:20] is that the other benefit of doing this inside of Visual Studio code is that we actually get
[0:27:25] integration with the built in chat in VS code. So I'm going to open that chat sidebar. And what
[0:27:31] you'll see here is the different sessions that we've had with Deco Pilot CLI. They just show up
[0:27:37] right here. And I'm going to expand this just a little bit. If I was to click into this,
[0:27:43] this will actually pull up and we're actually looking at the CLI session in the chat sidebar.
[0:27:50] Right. So if you scroll back up here and I'm quite zoomed in for videos. So it's really hard
[0:27:56] to see, but we can see exactly what's going on. And if we come back up here, let's see.
[0:28:03] Here's a good one. So this happened. Here's a sub agent that was used to check the Firestore
[0:28:08] status. Not something that's easy to look at in the CLI, but if we click here, it will take us
[0:28:14] into it. So we can see exactly what happened. Right. So it used the get diagnostics. So it's using
[0:28:20] follow me here. The CLI is using the editor's diagnostics tool, specifically the LSP or language
[0:28:29] server. So if I do, I'm going to pull up the bottom panel here. If you ever get a problem and you see
[0:28:34] problems, that is the language server doing that. That's called LSP or language server protocol.
[0:28:41] The CLI integrated with the editor is great because otherwise it doesn't know that there's errors.
[0:28:47] It can't use the editor features like linting and error checking to check its own code. It actually
[0:28:54] literally has to build and that's not the most efficient way. We want the agent to have this
[0:28:58] tool that we would have. And then we can see that it ran this command here and we could dig in
[0:29:03] and see exactly what that command was and what actually happened. So the integration with Visual Studio
[0:29:09] Code, super powerful, can be understated. A lot of times you don't care what's happening in the CLI,
[0:29:15] but when you do, you really need to be able to dig in and see it and the integration inside of
[0:29:21] VS Code provides that. And that's for free. That just works. There's nothing you have to do to
[0:29:26] configure that. So what's interesting here is you can see that it's going over the reviews from
[0:29:33] 5, 3 and from Gemini. And then it's doing a build and making sure that everything passes. And it's
[0:29:40] actually deploying the hosting and the rules. So again, we're in a Ralph loop here. So it's really
[0:29:47] going to try to get to the end. And remember, I told it, hey, you have the Firebase CLI. So just
[0:29:52] continue on until you're done. Do whatever you need to do. And you can see as it goes, you'll see
[0:29:57] these SQL calls. And that's because the CLI uses this SQL light database in the backend. And
[0:30:05] what Envil does is it uses that SQL light database to track progress so that when it gets to the end,
[0:30:11] it doesn't hallucinate whether or not it actually did something. It has to check the database to
[0:30:17] see if it actually did that thing. So it's done. And I zoomed out here so that we can see what's
[0:30:21] actually happening with Envil because all of this stuff at the end is this custom agent. So you can
[0:30:27] see, let's just sort of walk through what it actually did. It presents an evidence-based bundle. And
[0:30:32] this is really for its benefits so that it knows that it here's the evidence that it completed
[0:30:38] and did what it said it was going to do. So the initial state was clean after initial commit,
[0:30:43] empty project with a readme only. So it snaps out of the initial state. And then after the
[0:30:49] verification after it gets done. So it ran V it build, it looked at IDE diagnostics. It looks at
[0:30:54] the Firebase rules. It looked at the hosting, did the hosting function. So it looks like
[0:30:59] Blaze Plan required fall back in place. So it needs me to upgrade to the Blaze Plan. And then
[0:31:04] there's no regressions detected. And then here's the adversarial review where it looked at 5,
[0:31:09] 3 codecs, Gemini 3 Pro and Opus 4, 6. They all found sort of kind of the same things
[0:31:14] went through and fixed all those things. And then it came back and basically said, I'm done. And
[0:31:19] if you don't like this, you can just run this command right here to revert all of it.
[0:31:25] And that is the idea of Anvil is that it checks its work and makes it easy for you to roll back
[0:31:31] out of the changes that it made. Now, it wants me to upgrade to the Blaze Plan. So I'm going to do
[0:31:37] that real quick. It actually wants to run this in the cloud. It's deployed it. But I want to run
[0:31:43] it locally. So I will literally just ask, how do I run this locally? And hopefully it won't
[0:31:50] try to run it itself. If it does, we can stop it at any time. By the way, you can't stop any time
[0:31:56] with just hitting escape to once twice twice, once twice will stop. And just you can just stop
[0:32:05] the model from responding or doing whatever it's doing. So do you want to run this command?
[0:32:11] No. So we're going to run it ourselves. What do we want to run? We want to run, looks like we want
[0:32:17] to run NPX V it. All right. So it's running. And then let's go ahead and click and open our site.
[0:32:24] All right. So here's what it created. And remember, we provided the CSS. And you can see it's looks
[0:32:31] like we're already signed in. I don't know how. Here's my links. Let's try Google.com. It looks like
[0:32:37] it wants to fully qualify. So let's put that in. Great. Or let's there it is. Okay. And we've got
[0:32:43] two links. We can drag these. We can drop them around. Can we put a new one in? Microsoft Microsoft.com.
[0:32:52] That looks good. And we're getting the look at the like rounded added a little rounded
[0:32:57] on the open graph, which is lovely. I love that. Can I edit the different things? I can.
[0:33:02] That's just that's really nice. Let's do GitHub. And GitHub. Interesting. Okay. What about one more?
[0:33:08] What about this site? It's a good one. My own blog here. Shameless plug. There it is. Okay. And then
[0:33:16] here's our custom URL. And then can we publish? Looks like we can. Very nice. And so we could
[0:33:25] we should have added a title here. If we sign out, then we can sign in with Google. Here's here's my
[0:33:30] links. Let's create a new list. Give it a name, a description. So, you know, there's some things
[0:33:36] that I would change here. Like there's too many emoji. The flows a little bit goofy. I'd go back and
[0:33:41] start steering and making some changes. But essentially, that's kind of like you're burned down on
[0:33:48] the CLI. What you need to know today to use it and kind of like how I use it for workflows.
[0:33:53] And you can really build anything. I can't stress this enough. One of the things that I had been
[0:33:58] working on was a vibe coding competition that I had with Pierce from the product team last week in
[0:34:05] Redmond. And if you tuned in for that live. So here's the other Visual Studio Code instance. I
[0:34:10] actually have three of them. And I'm using the peacock extension so that I can tell which one I'm in.
[0:34:15] So this one's green, this one's blue. And then this is the one that we were in. So it's just an
[0:34:20] easy way for me to visually move and see, okay, this is my mobile app. This is the demo app that
[0:34:25] we're working on now. And here's the other one. So this one I just kind of want to show you because
[0:34:30] I'm kind of proud of it. But the whole point of this was to create a thank you wall for contributors
[0:34:37] because a lot of the contributions that are made are the code and Visual Studio Code comes from you.
[0:34:42] Comes from your pull request. And so we wanted to honor that. And so I created a site here
[0:34:46] called the thank you wall. This was part of the challenge. And you can load up a release here.
[0:34:51] And you can see all of the different contributors and then just sort of give them
[0:34:55] kudos here, which is which is nice. But I am showing you this because I also added the very bottom.
[0:35:00] I was like, it'd be so cool. If you could just like fly around and explore all of these different
[0:35:06] contributors. And so I did this. So you can just fly around through this guy and explore.
[0:35:12] I mean, and then give people kudos. This just blows my mind. A year ago, this would have just
[0:35:20] been impossible. And this is just me sort of telling the AI what I want. And it building. Look at
[0:35:25] these mountains and these trees and these clouds. You can do this. There's nothing that you can't do
[0:35:33] anyway, sidebar. Got a little distracted. But that's the GitHub co pilot CLI. I like it a lot.
[0:35:41] It's really powerful. I find that it's extremely good at handling background terminal activity.
[0:35:47] The autopilot or route fluke in there is great. We didn't even get to things like fleets,
[0:35:53] which allow you to deploy an entire fleet of sub agents to go out and tackle big projects like
[0:35:59] refactors. I hope this was helpful. I hope it helps with your workflows. And remember that
[0:36:06] whatever works for you, that's the right workflow. I'll leave the links to all of this stuff that
[0:36:11] you need or we used in the video like and vote below in the description. And as always, thanks
[0:36:17] for watching and happy coding.
