---
video_id: FjvtWeG6EEo
title: "Let it cook: Agent Steering, Queueing, Hooks, CLI Integration, & more!"
url: https://www.youtube.com/watch?v=FjvtWeG6EEo
channel: "@code (Visual Studio Code)"
published: 2026-02-13
speakers:
  - James Montemagno
  - Pierce Boggan
topics:
  - agent-steering
  - queueing
  - hooks
  - cli-integration
  - tips-and-tricks
relevance: primary
---

# Let it Cook: Agent Steering, Queueing, Hooks, CLI Integration, & more!

James and Pierce share tips and strategies for working with agents including steering, queueing, and more.

## Key Topics Covered

- **Agent Steering**  Techniques for guiding agent behavior during sessions
- **Queueing**  Queuing multiple tasks for agents to process sequentially
- **Hooks**  Runtime enforcement layer for coding agent sessions
- **CLI Integration**  Using Copilot CLI alongside VS Code
- **Best Practices**  Real-world patterns from the VS Code team

## Links

- Pierce's thread: https://x.com/pierceboggan/status/2019575107681993014

---

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:17] Woohoo!
[0:00:23] Woo!
[0:00:27] Woo!
[0:00:34] Woo!
[0:00:56] Woohoo!
[0:01:17] Woo!
[0:01:43] Oh, sorry. I was I was cooking over
[0:01:45] there, Pierce. I'm sorry.
[0:01:48] I was like, "Where's James?" This the
[0:01:50] thing came up and I look over because
[0:01:52] the music stopped and there's no James.
[0:01:54] I was ready if I had to.
[0:01:56] >> As the as the countdown was ticking
[0:01:58] down, I was like, I need to fire off
[0:02:01] this cook right now and let it rip. Uh,
[0:02:04] welcome back everyone to another edition
[0:02:06] of Let It Cook. here uh on occasion
[0:02:09] maybe soon to be weekly uh behind the
[0:02:12] scenes with the team uh mostly with
[0:02:15] Pierce and sometimes with Burke and
[0:02:16] sometimes with me as well. Uh this is a
[0:02:18] show that we started oh gez like I don't
[0:02:20] know like what eight nine 10 months ago
[0:02:21] where basically we're going to show you
[0:02:23] all the crazy amazing features that the
[0:02:25] team has been up to. Uh, which is
[0:02:27] awesome because there's so much goodies
[0:02:29] happening like all the time and we want
[0:02:31] to keep you up to date. And now Pierce,
[0:02:34] uh, it seems like the team is shipping
[0:02:35] even more than ever. Can you tell us a
[0:02:38] little bit? I'm going to share my tab
[0:02:39] over here. What is happening? Because
[0:02:41] there's been almost a weekly release, I
[0:02:44] think. What is up?
[0:02:45] >> Yeah, I mean the team is moving super
[0:02:48] fast and we've been delivering as always
[0:02:50] a ton of features into insiders every
[0:02:52] single day. But then we got a lot of
[0:02:55] feedback of like, hey, I really love
[0:02:57] what's in insiders, but I can't use it
[0:02:58] at work. I'm not allowed to use stable
[0:03:00] versions or I just prefer to use VS Code
[0:03:02] stable. You know, why do I have to wait,
[0:03:05] you know, 30 days for this thing to make
[0:03:07] it to VS Code stable? And so, um, for
[0:03:10] the past while we've been kind of
[0:03:12] shipping a version of a weekly update.
[0:03:14] Normally, it doesn't have features in
[0:03:16] it. And so as of yesterday was kind of
[0:03:19] our first attempt at this of of shipping
[0:03:21] a stable kind of within the month of the
[0:03:23] typical VS Code stable releases. Um and
[0:03:26] we had some good stuff in there and it
[0:03:27] was stuff that people really wanted from
[0:03:28] insizers into stable. So we'll see how
[0:03:31] it goes. Um give us your feedback on
[0:03:32] what you think about the weekly
[0:03:34] releases. like not every week we'll have
[0:03:35] this jam-packed of stuff, but if we see
[0:03:37] things that we feel good about the
[0:03:39] engineering quality of in insiders and
[0:03:41] also people want in stable before the
[0:03:43] end of the month, we'll do our best to
[0:03:45] try and bring it to stable like midmon.
[0:03:47] >> That's awesome. Yeah. So, like there's
[0:03:49] obviously a whole bunch of things like
[0:03:50] just like kind of like people are
[0:03:51] probably used to these like here's 1091
[0:03:53] 1092.
[0:03:55] This is the January release which comes
[0:03:56] out in February as people may know.
[0:03:58] Well, this was this was today. No, no
[0:04:00] date stamp on it, Nick. But, um, you
[0:04:02] know, it's I guess a release date. Oh,
[0:04:04] no, no, just no release date on this.
[0:04:06] Just it came out. It's there, right? But
[0:04:08] there's also this insiders tab. Boop.
[0:04:10] Which is here, too. Uh, which will show
[0:04:12] you the thing. So, there's all there's
[0:04:14] tons of things. Not everything in
[0:04:15] insiders is like in that in that release
[0:04:18] like you said, there's like a quality
[0:04:19] like gate type of thing happening,
[0:04:21] right?
[0:04:21] >> Yeah. And I mean, from an engineering
[0:04:23] standpoint as well, right?
[0:04:25] you see if you use insiders the velocity
[0:04:27] of the features that go into that. It's
[0:04:30] hard to cherrypick things back to
[0:04:31] another branch with different, you know,
[0:04:34] a different base, right? So, this is
[0:04:36] being cherrypicked from our main back to
[0:04:38] a release branch. And so, there's some
[0:04:40] changes that are just too big and not
[0:04:42] isolated enough to be able to backport.
[0:04:44] And so, those will also have to wait.
[0:04:45] But, yeah, it's generally kind of a
[0:04:47] always a quality consideration and then
[0:04:49] also like a customer need consideration
[0:04:51] as well. Yeah, and this was a big one
[0:04:53] yesterday. Let me zoom in here. We got
[0:04:55] Well, look at that. Super zoom. Wow. Uh
[0:04:57] message we're going to talk about today.
[0:04:58] Steering and queuing, agent hooks, um
[0:05:01] some new cloud compatibility stuff, and
[0:05:03] skills as slash commands. I'm going to
[0:05:06] show off a bunch of those things as well
[0:05:07] because I have it here. Of course, I'm
[0:05:08] going to roll insiders because I always
[0:05:10] do it. And I recorded a video yesterday
[0:05:13] and then I updated today and then I was
[0:05:14] like, ah, the UI changed.
[0:05:17] Shipping it, shipping it, whatever. It's
[0:05:19] all happening. Now, I do want to tell
[0:05:21] tell people here as well, there's also a
[0:05:22] new uh Twitter account over here.
[0:05:25] >> It's called the uh VS Code change log uh
[0:05:29] at x.comvcode
[0:05:31] log. I'll put that in the chat as well.
[0:05:33] Oh, look, look, I'm cooking right now,
[0:05:34] too. Wow, that's great. Um, so uh just
[0:05:38] joined uh as well recently. Uh and it's
[0:05:42] all the updates. So, this is uh a big
[0:05:44] automation stream set up here. So you
[0:05:46] can see already if you want to get the
[0:05:48] updates PICE before they're even on the
[0:05:51] website like I want to point this out
[0:05:53] before the that they've even landed here
[0:05:57] I will be even faster because I worked
[0:05:59] we worked really close with Nick who
[0:06:01] does like all the documentation all this
[0:06:03] release all this stuff and this all
[0:06:05] pulls from the open source repo and then
[0:06:07] the open source repo gets built and then
[0:06:09] it gets deployed to the website. So like
[0:06:11] if there's a timing thing where like
[0:06:12] this will like basically go faster then
[0:06:15] >> love that. Yeah. I mean because
[0:06:17] literally we're moving so fast like for
[0:06:20] things like the release automation. I
[0:06:21] know the same is true for copilot CLI.
[0:06:23] You're we're having to build all this AI
[0:06:25] automation because it's like impractical
[0:06:28] for a human at the speed at which we're
[0:06:29] moving to be able to every single day
[0:06:32] look at all the merge PRs and manually
[0:06:34] hand author artisally craft some release
[0:06:37] notes. Um, and so if anything really
[0:06:40] crazy happens, there's a disclaimer that
[0:06:42] it is AI generated, but we do try to
[0:06:44] look at it to make sure there's nothing
[0:06:45] insane happening there. But it seems
[0:06:47] like it's working pretty well. Like I
[0:06:48] kind of like I wish that I got more. It
[0:06:50] says in five more. I wish I got a little
[0:06:51] bit more detail there. But I think
[0:06:53] >> yeah,
[0:06:54] >> this is looking pretty good overall.
[0:06:55] Like I'm I'm really happy with this as a
[0:06:57] first attempt.
[0:06:58] >> Oh, don't worry. I'm I'm working on it
[0:06:59] right here up.
[0:07:00] >> You're literally clicking at the moment.
[0:07:02] I see a active co-pilot session. Okay,
[0:07:03] >> there's a active enhance insiders tweet.
[0:07:06] It's probably with my prompts. Yeah,
[0:07:08] there we go. Critical. Your primary goal
[0:07:10] is to show more
[0:07:12] >> expert.
[0:07:13] >> Show aim. Yes, it it's like you really
[0:07:16] are. You are a VS Code release. Yeah,
[0:07:18] this is my huge prompt to uh There you
[0:07:20] go. Oh. Oh, yeah. Look at this. Look at
[0:07:23] Oh, that's great. Hopefully, it
[0:07:25] improves. I'm really excited. I need to
[0:07:26] show you my evals thing and we can like
[0:07:28] build some evals for your uh tweet RSS
[0:07:31] thing because I think that would be cool
[0:07:33] because then you could actually test
[0:07:34] different prompts and see if they're
[0:07:36] better or worse.
[0:07:37] >> Oh, that'd be cool. Yeah, I just I just
[0:07:38] yolo and release it and then it happens.
[0:07:41] >> I mean, and it's it's the release notes
[0:07:43] thing. Like the worst that can happen is
[0:07:44] like we have a bad tweet out there. Um
[0:07:47] so I don't think it's like that
[0:07:49] dangerous to yolo it. The one thing that
[0:07:51] I do which is fascinating is uh so this
[0:07:54] so here's the fascinating part is like
[0:07:57] every single time you run it it's
[0:07:58] actually going to be different. So I
[0:08:00] actually have a test endpoint where I
[0:08:01] can just test it and sure enough like it
[0:08:03] picks different things as much as
[0:08:05] humanly possible. So
[0:08:07] >> because I could run this again and maybe
[0:08:09] it would have two, maybe it would have
[0:08:10] three, maybe it have four, but it's
[0:08:11] trying to figure out what it's actually
[0:08:12] trying to do is highlight the most like
[0:08:16] important features. So what this is
[0:08:18] deemed is that there's only one one
[0:08:20] important feature.
[0:08:21] >> So So I should be insulted if I merge
[0:08:24] something in and I don't see it here
[0:08:25] because the AI has determined my feature
[0:08:27] wasn't important.
[0:08:28] >> That's the new team goal. That's the new
[0:08:29] team goal.
[0:08:30] >> Uh all right. I want to show something
[0:08:32] quick before you hop into these new
[0:08:34] features. I want to talk a little bit
[0:08:35] about the CLI and some of the new
[0:08:37] integrations into VS Code.
[0:08:42] >> Um so the first thing here is uh I have
[0:08:45] insiders. you're going to have to tell
[0:08:46] me what's in stable and what's not in
[0:08:48] stable. But I'm pretty sure like
[0:08:50] >> some of these integrations are in
[0:08:51] insiders
[0:08:52] >> and then like the CLI features are in
[0:08:54] the CLI itself. Um, but this is the
[0:08:58] Visual Studio wallpaper website. So it's
[0:09:00] a it's a website and I've been having
[0:09:02] fun. I've just been converting it to
[0:09:03] different like programming languages.
[0:09:04] Like I made a React version, a Blazer
[0:09:07] version. I'm going to do like a Java
[0:09:08] like I don't know just kind of have like
[0:09:09] every I was gonna have to reprogram it
[0:09:11] in every single programming language.
[0:09:12] But right now it's a Blazer Blazer app
[0:09:14] because I'm on the Blazer branch. But
[0:09:17] what I wanted to show off is a lot of
[0:09:18] people use, you know, obviously the chat
[0:09:21] session here, but a lot of people are
[0:09:22] also hanging out and and using the
[0:09:26] Copilot CLI. And often Pierce, they're
[0:09:29] like this, like this is what it looks
[0:09:30] like. You got a CLI here. And in fact,
[0:09:34] most of the time it just looks like
[0:09:35] it'll look like this, right? That's what
[0:09:38] they're that's what they're dealing
[0:09:39] with. Maybe their their terminal is
[0:09:41] better than mine. I'm not really a Mac
[0:09:43] person. I'm more of a Windows person.
[0:09:44] So, I'm not a Windows terminal, so I
[0:09:45] don't know what I'm doing.
[0:09:46] >> Wait, so what are you running here for
[0:09:47] terminal
[0:09:48] >> terminal?
[0:09:52] If it's in the box, that's what I use,
[0:09:55] man. If it's in the box, Apple deems
[0:09:56] that this is the terminal. So,
[0:09:59] >> it's the terminal. Windows terminal.
[0:10:00] It's in the box of default. That's what
[0:10:02] I use. That's the default terminal. Oh
[0:10:04] my. Oh my posh. Little Oh my POSH here.
[0:10:07] Look, I don't even know how to make it
[0:10:08] bigger. on my posh. So you can see I'm
[0:10:11] on these things. All right. So if I do
[0:10:12] copilot
[0:10:14] uh it's going to boot up copilot. Now
[0:10:16] actually I'm inside a terminal but
[0:10:17] inside of PowerShell inside of terminal.
[0:10:20] So that's my shell inside my terminal.
[0:10:21] Do you know those are two different
[0:10:22] things? A shell and terminal.
[0:10:25] >> I did know that.
[0:10:26] >> Yeah. Handsome had to describe that to
[0:10:27] me because I don't understand how
[0:10:29] terminals and shells work. He's like
[0:10:30] he's like it's in the name James Power
[0:10:32] Shell. And I was like oh I see I see
[0:10:35] what they did there.
[0:10:37] >> Exactly.
[0:10:37] >> Yeah. Okay. So, here's my co-pilot here.
[0:10:39] And if you want to get better, let's
[0:10:41] co-pilot d-banner. There we go.
[0:10:45] Beautiful. Okay. That's the more proper
[0:10:47] uh way of working with it there. Okay.
[0:10:49] Um, but I want to point this out. Look
[0:10:51] at this. You see this connected to
[0:10:54] Visual Studio Code Insiders.
[0:10:57] >> What does that even mean? Well, it's a
[0:10:58] great question.
[0:10:59] >> I'm going to say slash IDE. You're not
[0:11:00] going to have that by default. So, like
[0:11:02] I turned it on. So, slash IDE. When you
[0:11:05] do slash IDE in the terminal, I'm going
[0:11:07] to show you also how this kind of just
[0:11:08] works magically inside of VS Code, but
[0:11:10] it's going to say, "Hey,
[0:11:13] we'll automatically trust the folders.
[0:11:16] We will automatically have access to
[0:11:17] editor selection and diagnostics, and
[0:11:19] it'll also, most importantly, do a file
[0:11:22] change approvals
[0:11:24] uh with diff taps. This is my favorite
[0:11:25] feature. So, you can turn it on. Boom.
[0:11:28] It's good to go." Now, the one thing
[0:11:29] right away that you could do once it's
[0:11:30] connected, I could come over here and I
[0:11:34] could highlight like this for each loop
[0:11:36] or whatever on this wallpaper grid. I
[0:11:38] can rightclick. It's probably nearly
[0:11:39] impossible to see because it's like so
[0:11:41] small on the screen, but it says add
[0:11:42] file to copilot CLI. That would be uh
[0:11:46] shift
[0:11:47] command dot if I understand my Mac
[0:11:50] keyboard or add selection to the copilot
[0:11:52] CLI. Watch this. I did that and then
[0:11:55] boom, it's it's in it.
[0:11:58] It's like connected. It's like magic.
[0:12:00] >> So, that's pretty cool.
[0:12:02] >> Let's do something different. Um, let's
[0:12:04] do let's add Oop, it's all caps. That
[0:12:06] was me. Uh, I'm just going to yell at
[0:12:08] it. Let's add cool uh popup
[0:12:12] um cards for Scott Hanselman
[0:12:17] and James Monty Magno on the bottom of
[0:12:20] the screen. Okay, so my GP53 codeex is
[0:12:25] getting to work here. I'm really upset
[0:12:27] with it because I'm caps locked and it's
[0:12:29] going to get to work thinking, right?
[0:12:30] So, just normal kind of CLI mode. And
[0:12:31] like normally, you know, you would just
[0:12:33] be hanging out here waiting for it to to
[0:12:36] get to work. There we go. It's thinking.
[0:12:38] It's doing some stuff. And at the bottom
[0:12:39] of this page, basically, there's like a
[0:12:41] little footer that's like made by Scott
[0:12:43] and James and Copilot because the the
[0:12:44] page is like really nice. Um, so it's
[0:12:47] going to explore the layout and then
[0:12:48] it's going to get to work. So, now we're
[0:12:50] just cooking.
[0:12:52] Cooking. It's doing stuff. I'm on a
[0:12:55] medium over here. How do you feel about
[0:12:57] medium with codecs? How's your 53 codecs
[0:13:00] cooking going?
[0:13:01] >> Good. Uh I run medium or high most of
[0:13:03] the time. And that is configurable in
[0:13:05] both CLI and VS Code. Um actually Opus
[0:13:09] 46 in most of the C-pilot integrations
[0:13:11] runs high because we saw in our evals
[0:13:13] that we got better results. medium I
[0:13:16] think for codecs as a default makes more
[0:13:18] sense because there's different task
[0:13:19] difficulties and if you put high you're
[0:13:21] just your agent loop is going to take
[0:13:23] much longer and that may not always be
[0:13:25] necessary. Um there's people think that
[0:13:27] like oh if I just set it to high I
[0:13:29] always get better results and that may
[0:13:30] be true on extreme difficulty problems
[0:13:33] but most problems don't fall into that
[0:13:35] and so you're just making your agent
[0:13:37] wait longer for no reason on most of
[0:13:39] your inquiries. I got 99 problems and
[0:13:41] none of them are difficult.
[0:13:44] Uh, so here's here's what happens. This
[0:13:46] is the normal kind of CLI view. So if
[0:13:48] you've been living and breathing in the
[0:13:49] CLI, now maybe you're like me and I you
[0:13:51] just yolo and you're just like, I just
[0:13:52] do whatever, go to town. But if you like
[0:13:54] to look at code, which I like to do,
[0:13:56] this pops up and this is, you know, this
[0:13:59] is a thing. But if I just open up VS
[0:14:02] Code,
[0:14:03] what just happened? Look at this. So you
[0:14:07] can see it says uh copilot CLI. I'll
[0:14:09] make this really big. Look how big that
[0:14:11] is. So big you can't even see it. Let's
[0:14:13] just drop that down. Boom. It says
[0:14:15] co-pilot CLI main layout razor, right?
[0:14:18] So what it did is it's connected over
[0:14:20] here and it's showing me the diff
[0:14:23] right in line there. So that's really
[0:14:25] cool. So for example, if you just want
[0:14:27] to go and say, okay, let's cook. And now
[0:14:29] it went away, right? Because I approved
[0:14:30] that tool. Now you could approve all of
[0:14:31] them and it wouldn't obviously open up
[0:14:32] or do anything. But now it's going to
[0:14:34] implement the rest of the footer cards
[0:14:35] and it's going to get to work over here.
[0:14:36] So, um, and it will go through that for
[0:14:39] every single one. So, we can see here's
[0:14:41] the addition. That looks good. There
[0:14:42] might be additions. There might be
[0:14:43] subtractions. It would show you that
[0:14:45] real inline diff inside of it. Uh, I
[0:14:48] think Damian on the net team. So, it's
[0:14:50] already done. It's like, cool, let's
[0:14:51] build it. Um, the the footer is a pretty
[0:14:54] easy example. I probably didn't need 53
[0:14:56] codecs to do that, but yeah, it's a 1x,
[0:14:58] so why not? Yeah.
[0:15:00] >> Look at the job here. Unlimited premium
[0:15:02] request.
[0:15:03] >> Unlimited. And there we go. See, that
[0:15:04] was a nice little diff where it like
[0:15:05] showed it. So, especially if you have
[0:15:07] big diffs, right? Maybe multi files,
[0:15:09] things like that, like it's going to
[0:15:11] show you all those in tabs as it opens
[0:15:13] up, which is like so nice to see,
[0:15:15] especially if you have like an ultra
[0:15:16] wide like I do that's not in currently
[0:15:18] 1920 x 1080 mode. So, like it's just
[0:15:20] huge black bars. You could be running
[0:15:22] these side by side and seeing them
[0:15:24] there. Especially if you're just like,
[0:15:25] hey, I have like a bunch of different
[0:15:27] things.
[0:15:28] >> But, you know, inherently like I'm not a
[0:15:29] CLI person like Scott is, right? Like
[0:15:32] that's like what he loves and breathes
[0:15:34] it. So, some people might be saying
[0:15:35] like, "Well, James, like why wouldn't
[0:15:36] you just like type that like over here
[0:15:39] like into the sessions and and things
[0:15:41] like that, right?" And like you
[0:15:42] definitely could and then you would see
[0:15:44] everything happening in real time. But
[0:15:46] different tools, different resources and
[0:15:48] different sort of workflows that you may
[0:15:50] be done. Let's see if this worked. Um,
[0:15:52] let's net run this pup. Net run. Net
[0:15:57] run.
[0:15:59] Net watch run. I'm going to watch run.
[0:16:01] I'm I'm not even going to do that. So,
[0:16:03] I'm going to do this. And then, you know
[0:16:05] what? I really want feature request.
[0:16:07] >> What?
[0:16:07] >> Like when a when a URL shows up here,
[0:16:10] >> when I click it, don't open the browser,
[0:16:12] but open the integrated browser.
[0:16:14] >> Yeah, I actually had this same request
[0:16:16] the other day.
[0:16:17] >> That'd be cool.
[0:16:18] >> Shout out to the integrated browser.
[0:16:20] That was new in the last major stable
[0:16:21] release.
[0:16:22] >> Oh, look at this. I'm a wallpaper
[0:16:24] wizard.
[0:16:25] >> What's Handsomeman?
[0:16:27] >> Handsomeman is a community curator.
[0:16:30] So, I got little cards there and you
[0:16:32] know it's AI because it's it little
[0:16:33] hover effects. I love hover on anything.
[0:16:36] Okay. So, so that's pretty cool. You get
[0:16:38] to see that. But some people also work
[0:16:40] in the terminal directly here. So, let's
[0:16:42] say I stop this pup.
[0:16:43] >> Um, actually just keep it running. Open
[0:16:46] another terminal because why not? And
[0:16:47] let me just make this bigger. There
[0:16:49] probably better ways of doing this. But
[0:16:51] let's say I'm down here and let's just
[0:16:52] say I'm like, you know what? You know,
[0:16:54] I'm just going to co-pilot it here,
[0:16:56] right? like open a copilot inside of the
[0:16:59] terminal. Now, what's nice is that
[0:17:00] copilot CLI knows that I'm already
[0:17:03] inside the terminal inside of VS Code
[0:17:05] has detected it and it automatically
[0:17:07] connects it and it's automatically ready
[0:17:09] to roll. Right? So, let's say I was
[0:17:11] like, let's add a VS Code Insiders theme
[0:17:16] to the app. Boop. And then let it cook.
[0:17:19] So, now this is going to go to town.
[0:17:20] This probably going to ask me a bunch of
[0:17:21] questions for that normal workflow. So,
[0:17:22] now at this point, I could just open
[0:17:24] more terminals. I could come over here
[0:17:26] into the chat session. Maybe I want to
[0:17:28] do local. Maybe I want to do some
[0:17:30] planning, you know, a bunch of stuff
[0:17:31] here. Like just different workflows. I
[0:17:33] might have some like super long running
[0:17:35] task. It should be over here. Maybe it's
[0:17:36] on a work stream. Maybe it's doing
[0:17:37] something. I'm just like, "All right, go
[0:17:38] to town, right?" Um, and just do it. So,
[0:17:42] um, again, it's it's going to be here
[0:17:44] and just ask me some questions. But
[0:17:46] ideally,
[0:17:48] it was showing this to me yesterday. Is
[0:17:50] it not? Oh, local work tree. There it
[0:17:52] is. Oh, I forgot to to to to point. I
[0:17:55] had the filter on reset. Um, those
[0:17:58] sessions also show up right here. Right.
[0:18:00] So, here's the add bottom cards, right?
[0:18:03] Oh, didn't Oh, because I think I
[0:18:05] finished that section. Uh oh. We go.
[0:18:08] Insiders. We're rolling insiders,
[0:18:10] people.
[0:18:17] Where'd it go? Oh, there we go. Bring
[0:18:19] it.
[0:18:21] Bring it back. Oh, it's gone. My
[0:18:23] sessions are gone. Pierce, help me. Oh
[0:18:26] my gosh. Oh, it was there.
[0:18:30] >> Try uh
[0:18:33] try a window reload.
[0:18:36] >> I'm actively cooking. I'm actively
[0:18:38] cooking. It's okay. We're going to let
[0:18:40] it cook over here. Let's see here.
[0:18:42] >> So, let's see. It's exploring. It's
[0:18:44] doing stuff. It's planning. And then
[0:18:46] what I wanted to show basically is you
[0:18:48] get this like a few things. You get this
[0:18:49] nice little like, hey, it's updating
[0:18:50] here, right? See, it like updated the
[0:18:52] name automatically. That's cool. Then
[0:18:54] you get the same experience. So here,
[0:18:55] for example, boom. And then you get the
[0:18:57] the live diffing, all that stuff that
[0:18:59] you would expect. So, you know, you can
[0:19:01] obviously, you know, decide if you want
[0:19:03] one, two, three, whatever. But it's
[0:19:04] going to go and start to do this thing.
[0:19:06] Oh, it's hot reloading in real time.
[0:19:07] That's kind of cool.
[0:19:08] >> All right, let's see if it will cook
[0:19:11] over here.
[0:19:12] >> So, let me show you my flow if you don't
[0:19:14] mind. Yeah.
[0:19:15] >> Um, right click on the implementing
[0:19:17] theme changes like on the and then move
[0:19:19] it into the editor area.
[0:19:22] >> And so now it's a tab. But then hold on
[0:19:25] a Yeah. Make the terminals fall.
[0:19:28] >> Um, and now what you can actually do if
[0:19:30] you drag that like to the right, like
[0:19:32] click on the editor tab. Yeah. And drag
[0:19:34] it like kind of to the right like you're
[0:19:35] trying to Nope. Like in the editors
[0:19:37] lower, lower. There you go. Drop.
[0:19:41] >> And then you can open your browser on
[0:19:43] the left. Right.
[0:19:45] >> Ah,
[0:19:46] >> so you're reclaiming a lot of visual
[0:19:48] space here if you do this. Um, okay. And
[0:19:50] you could actually like say you wanted
[0:19:51] to cook five copilot CLI at once. When
[0:19:54] you move it into the editor, you can use
[0:19:55] the editor like grid layout system. And
[0:19:57] so you could like have a quad box of CLI
[0:20:00] going at once.
[0:20:02] >> That's cool. Wow.
[0:20:03] >> Yeah.
[0:20:05] >> So when I'm cooking on like four or five
[0:20:07] things at once, sometimes I like to do
[0:20:09] that. And I I like actually having it
[0:20:11] all encapsulated in one window because
[0:20:13] yeah, of course you could have four
[0:20:15] copilot CLI terminal processes going,
[0:20:17] but it's kind of a little messy visually
[0:20:19] to like tab between them and everything.
[0:20:21] So I kind of actually like having one
[0:20:23] window where they're all there and I can
[0:20:24] just click into that.
[0:20:25] >> That's cool. I like that. Yeah. So we
[0:20:27] had a question here from Shaw. Uh so
[0:20:31] when you open the CLI directly inside of
[0:20:33] VS Code, it'll just automatically
[0:20:35] connect. is also a command called slash
[0:20:37] IDE and that will allow you to connect
[0:20:40] directly to the workspace or disconnect
[0:20:41] from the workspace there too if you're
[0:20:43] just in standalone CLI. This is nice and
[0:20:45] you can see it actually did integrate
[0:20:46] our VS Code theme. I need to actually
[0:20:47] add an icon. Um but besides that it's
[0:20:51] ready to
[0:20:53] down there. That's kind of cool. I like
[0:20:54] that. Cool. So it did it. It did the
[0:20:56] whole thing. Now let's see if I have the
[0:20:59] Let me do a window reload. Reload.
[0:21:03] Let's see if that does it. Okay, there
[0:21:04] they are. Cool. So the other thing that
[0:21:05] I want to point out really quick is that
[0:21:07] these do show up inside your sessions,
[0:21:10] right? So you could, you know, if you
[0:21:12] like this view, you can see it happen in
[0:21:14] real time. And sometimes what's nice
[0:21:16] about that y
[0:21:17] >> is like if I make that bigger is the CLI
[0:21:19] is like flowing so fast.
[0:21:22] >> Sometimes I will actually just open up
[0:21:25] the chat and then I will like look, oh,
[0:21:27] what did it do? Oh, it read this. It
[0:21:29] searched it. It did some stuff, right?
[0:21:30] because the CLI really compacts it, but
[0:21:32] you can see everything that the CLI was
[0:21:34] doing here in the tool calls and the
[0:21:36] descriptions and the patching everything
[0:21:38] like that. So like that's really really
[0:21:40] nice to have that like deeply integrated
[0:21:42] uh into it. You can have these side by
[0:21:43] side. Now also if you want you can also
[0:21:46] come up here and you can also just say
[0:21:47] new CLI session
[0:21:48] >> and I'm just going to spin up a bunch of
[0:21:50] CLIs. Let's see if that's going to work.
[0:21:54] >> Did it work?
[0:21:55] >> It did. Yeah, you have two tabs.
[0:21:57] >> Oh, okay. I got the two tabs. I don't
[0:21:58] know if it actually didn't. Maybe my oh
[0:22:00] my posh probably broke it.
[0:22:02] >> Oh, I see what you mean. It didn't auto
[0:22:03] run copilot.
[0:22:04] >> Yeah, it should auto run copilot. It did
[0:22:06] on my other machine. So I blame my
[0:22:09] >> Let me try that.
[0:22:10] >> I blame my machine. Classic developer.
[0:22:13] >> Blame my mish that's loading PowerShell
[0:22:16] because I don't understand how terminals
[0:22:17] work. So um
[0:22:20] >> it works for me. So yeah, I'm blaming
[0:22:22] user error. But we should probably file
[0:22:24] a bug for that.
[0:22:25] >> Yeah, but it's probably me. But you
[0:22:28] know, and it's like this delay. So, we
[0:22:30] can show it on your machine as well. Um,
[0:22:31] there I didn't test that earlier, but
[0:22:33] you can have like as many of these as
[0:22:34] you want, right? And then the titles are
[0:22:35] update. So, if you want, you can come
[0:22:37] down here and just like create a bunch
[0:22:39] of, you know, terminals, launch it, do a
[0:22:40] thing, but it's all there for you as
[0:22:42] well. I guess you can do that and then
[0:22:44] open another one. That one see
[0:22:45] >> So, yours isn't working at all, which
[0:22:46] makes me think that, yeah, there's
[0:22:48] something we're not handling right about
[0:22:50] your config or your shell.
[0:22:52] >> It's a messy shell configs. I don't know
[0:22:54] how shell configs work. So, I will send
[0:22:56] my exact shell config to the team.
[0:22:59] >> We have problems like that with the
[0:23:00] terminal tool sometimes, too. It's kind
[0:23:02] of like the bane of my existence. Um,
[0:23:05] >> but you can just you could just yolo
[0:23:06] like this. This could be your new hub
[0:23:09] >> for look at everything happening
[0:23:11] everything happening here and uh just go
[0:23:13] to town.
[0:23:14] >> It's nice that you have like the the
[0:23:16] sessions you can always come back to
[0:23:18] visually over here. And like if you're
[0:23:20] like me and you're using like multiple
[0:23:22] things at once, like just having a
[0:23:24] single view where all that data is
[0:23:25] streaming in is quite nice in my
[0:23:27] opinion.
[0:23:28] >> Now, one thing I'll point out here too
[0:23:29] is like down here there is like local
[0:23:33] sometimes you'll see background, you
[0:23:35] might see uh you might see CLI, you
[0:23:38] might see whatever the flavor of the
[0:23:40] team has decided today and then you can
[0:23:42] see cloud. So work tree is interesting
[0:23:44] because this is going to use the GitHub
[0:23:46] copilot CLI, but it's actually going to
[0:23:47] create a work tree. So, if you actually
[0:23:48] wanted to run on like multiple tasks all
[0:23:50] in the same time, I'm sure the CLI has
[0:23:52] something built in as well. Um,
[0:23:55] >> but like this is nice because you don't
[0:23:56] have to think about it. It just kind of
[0:23:58] does it and then sends it off to the
[0:24:00] thing. Uh, here then you got agents and
[0:24:02] then if I have local, check out this. I
[0:24:04] got that. I got a bunch of stuff in
[0:24:05] here. Other other agents. So, you have a
[0:24:07] little bit, you know, the same control
[0:24:08] just different UI and then obviously
[0:24:10] other agent harnesses as well that you
[0:24:12] might spin up on as well. So, kind of
[0:24:14] point that out. You know, you have these
[0:24:16] options. I think one thing that I wanted
[0:24:18] to kind of show off here really is like
[0:24:20] it's about, you know, developer choice,
[0:24:22] right? Like how you want to code, how
[0:24:25] you're feeling that day, but how these
[0:24:27] tools also like work together, right, in
[0:24:30] general. So, um,
[0:24:32] >> and I want to call out here, yes,
[0:24:33] digital drummer boy Jay, what's going
[0:24:34] on, man? It's good to see you. Uh,
[0:24:36] points out, yes, I could probably just
[0:24:38] ask co-pilot to fix up my config.
[0:24:41] Yeah, I also I was talking to Yan uh of
[0:24:44] Oh My Posh and he was like, "Oh, you
[0:24:46] should build an MCP server that um that
[0:24:49] helps you build Oh my Posh
[0:24:50] configurations." And I was like, "Cool,
[0:24:51] I'll do that." So then I just asked
[0:24:52] Copilot to do it and it did it. So that
[0:24:54] was pretty fun.
[0:24:55] >> I was about to say, "Didn't you tweet
[0:24:56] that out?" I was like, "I have this I
[0:24:58] have vague recollection of seeing
[0:24:59] something on my feed about this."
[0:25:02] >> Yeah, I have it. I have the Oh my Posh
[0:25:04] Configurator 5000.
[0:25:06] >> That's what I think I was. I I see you
[0:25:07] went with the naming on it. Uh with the
[0:25:10] 5,000 at the end.
[0:25:12] >> Yeah, it's like, oh my gosh. Here we go.
[0:25:15] Let's see. I I'll bring up my screen
[0:25:17] again here.Oop.
[0:25:19] There we go. There we go. Cool. So, this
[0:25:22] is the Oh my Posh configurator. And
[0:25:25] then, see, I have I have it cooking
[0:25:27] right now over here in this tab, which
[0:25:28] is
[0:25:29] >> I'm mad you were too scared to put 5,000
[0:25:31] in the slug for the name.
[0:25:33] >> Uh, if you tap on it though, I I didn't
[0:25:35] even put in the name. It should be I
[0:25:36] just
[0:25:37] >> Come on. Branding.
[0:25:38] >> I know branding. All right. Well, let's
[0:25:40] see. Okay.
[0:25:40] >> This is pretty cool, though.
[0:25:42] >> Uh, update the name to be Oh, my POS
[0:25:48] configurator 5000.
[0:25:51] Uh, who do I need? Click on it. Sure.
[0:25:53] Okay. Uh, let's PR that. So, this is
[0:25:56] nice because if you're like not like me,
[0:25:58] this is like the configurator and you
[0:26:00] can see like a live preview of what it
[0:26:01] would look like in your terminal.
[0:26:02] >> That is really cool.
[0:26:04] >> And then you have all of the different
[0:26:05] segments. So, if you're like, oh, I want
[0:26:06] the battery here, that would show up
[0:26:08] there. And then you can tap on it and
[0:26:10] then you can uh change the colors and
[0:26:12] you have a whole color palette selection
[0:26:14] thing here.
[0:26:16] Different different dividers if you're
[0:26:18] like oh I want like a you know diamond
[0:26:20] or accordion or like however you want.
[0:26:22] So it does its best representation right
[0:26:24] to do it.
[0:26:25] >> Um and you can pick like the font that
[0:26:27] or the the nerd font different cache
[0:26:28] settings. It's really complex. We also
[0:26:30] have a theme library. Um so you can save
[0:26:33] your own but you can also just be like
[0:26:35] there's all segments. say here's every
[0:26:37] if you want every segment here's what it
[0:26:39] would kind of look like. No, not all of
[0:26:40] them show like all the time. But um you
[0:26:43] know a good example would be if you're
[0:26:45] just like hey I want you know Apple
[0:26:47] Music uh I think it's just YouTube music
[0:26:49] maybe Spotify. Then here's like you know
[0:26:51] Spotify would show up in there and then
[0:26:53] you could modify the color and the uh
[0:26:56] the different colors that you have.
[0:26:57] There's like different foreground
[0:26:58] background things that are in here that
[0:26:59] are specified. So I'm like, "Oh, you
[0:27:01] know what? I want that to be a hex value
[0:27:03] and make that I don't know, whatever."
[0:27:06] Right? So So it all works. It's all
[0:27:07] magic. But you can add your own. So like
[0:27:09] here's Kayla's theme, which I stole
[0:27:12] basically. So this is I just steal
[0:27:13] Kayla's theme because it's great. And
[0:27:15] there's even a co-pilot one, too. So
[0:27:16] there's like a CLI and there's a there's
[0:27:18] a GitHub copilot uh one in here as well.
[0:27:20] So you can just add that and then it
[0:27:22] will show you how many premium requests
[0:27:23] you have left, which is pretty cool.
[0:27:25] >> So soon there'll be an MCP server. So
[0:27:27] you can just like go ahead and like say
[0:27:29] oh
[0:27:29] >> update my oh my posh to blah blah blah
[0:27:32] blah blah and it'll like grab and
[0:27:33] understand everything that you want.
[0:27:34] Yeah. Like hey like I'm in this project
[0:27:36] like you know blah blah blah or add
[0:27:38] caching or do this thing you know. So I
[0:27:40] try to make it like you could do these
[0:27:41] different things. There's official
[0:27:42] themes too. So this is nice because on
[0:27:44] the oh my posh website there's like hand
[0:27:47] curated you know themes from actual
[0:27:50] people that know things.
[0:27:53] So you can like go and tap
[0:27:55] >> 5000.
[0:27:56] >> Yeah. Yeah, you can go and visualize it,
[0:27:57] right? And it's not perfect. It's not a
[0:27:58] one one because I'm not like running.
[0:28:00] This isn't like a terminal window. It's
[0:28:02] like a preview, right? So, it's it's
[0:28:04] trying its best to do the thing, but you
[0:28:06] can have like extra block. It's that was
[0:28:08] crazy. This is like a one day hack
[0:28:10] project that turned into a week and
[0:28:12] yeah, so cool. So, anyways, that's what
[0:28:14] I've been cooking. Uh, all right. What
[0:28:18] are you cooking, man?
[0:28:19] >> My screen. Um,
[0:28:21] >> yeah. I guess like just to close out on
[0:28:23] the on the CLI and VS Code topic, if you
[0:28:26] have like a wish list of things like
[0:28:28] please send it to James or me or Evan or
[0:28:30] Pong or anybody on the VS Code or CLI
[0:28:33] team. Uh, we made a lot of improvements
[0:28:35] as James showed off, but there's still
[0:28:37] more to do. Sharing my screen, which is
[0:28:40] why I'm I feel like that's a universal
[0:28:42] like trailing off like when you're like
[0:28:44] trying to find the share. Oh, James,
[0:28:46] you're gonna be really bad at me. Uh oh.
[0:28:48] Do you got to reboot?
[0:28:50] >> Nope. No. We're good. We're safe.
[0:28:52] >> We're safe. I was really worried I was
[0:28:54] gonna have to reboot, but we're saved.
[0:28:56] Um All right. Let me know. We're good.
[0:28:59] >> Okay. Bringing it up.
[0:29:01] >> Bringing it up.
[0:29:02] >> You're live. It's live. It's happening,
[0:29:03] people.
[0:29:04] >> Um Okay. So, uh what do I want to show
[0:29:09] off? I think I'm gonna show off hooks.
[0:29:11] So, we'll talk a little about steering
[0:29:12] and queuing as well. How about that?
[0:29:14] Some of the new things in the stable
[0:29:15] release.
[0:29:16] >> Yeah, let's do it.
[0:29:18] Okay. So, um, what are hooks? Um, so I
[0:29:22] think we've all kind of had something
[0:29:24] where we're trying to get the agent to
[0:29:26] do something at a specific point in the
[0:29:29] agent life cycle, whether at the
[0:29:30] beginning or end of the session or
[0:29:32] somewhere like after you do this, do
[0:29:34] this. And sure, you can try and prompt
[0:29:38] the agent to do this, but it's it's very
[0:29:40] difficult often to get 100% success rate
[0:29:42] with prompting of like, I always want
[0:29:45] you to do this at the end of your turn.
[0:29:47] Um, end of turn and start of turn is
[0:29:49] actually easier, but like say it's like
[0:29:51] after every edit, I want you to do this
[0:29:53] thing, right? Um, it's kind of hard to
[0:29:56] get the agent to do what you want. And
[0:29:58] so, uh, hooks kind of solve this
[0:29:59] problem. So basically they allow you
[0:30:01] aptly name to hook into different parts
[0:30:04] of the agent life cycle. Um and so
[0:30:05] there's a different config. I'll I'll
[0:30:07] kind of show that off in a minute. Um
[0:30:10] but essentially you can pick like what
[0:30:12] you want to hook into like what life
[0:30:13] cycle event and then you have something
[0:30:15] you can do when that life cycle event is
[0:30:17] hit, right? Um and so kind of like
[0:30:21] describing this by the way you can this
[0:30:24] uh MCP server for ex gal it draw is
[0:30:27] amazing. I recommend it. Oh, cool.
[0:30:30] >> Well, because people always ask like how
[0:30:32] does um how does X work in VS Code,
[0:30:35] right? And the cool thing about being
[0:30:37] open source uh both VS Code and VS Code
[0:30:39] Copilot chat is you can literally just
[0:30:41] open up the repo and be like, I don't
[0:30:43] understand how this works. Like please
[0:30:46] tell me. And of course, it would do that
[0:30:47] before this, but now with this MCP
[0:30:49] server, like you actually, this is an
[0:30:51] MCP app, so it can render like rich
[0:30:54] information in the Windows. So here this
[0:30:56] is actually using the new MCP apps
[0:30:58] integration. Anyways um so yeah what is
[0:31:02] actually happening? So like say I enter
[0:31:04] a prompt. Um then basically we have this
[0:31:08] run start hooks uh that's going to
[0:31:10] happen. So it's going to see like do you
[0:31:12] have any start hooks that you've said.
[0:31:13] So at the beginning of a turn I want you
[0:31:15] to do this sort of thing. Whether that's
[0:31:17] the overall agent so like I just said hi
[0:31:19] and it's you know the first thing is
[0:31:21] happening or you're using sub aents. So
[0:31:23] you can hook into either one. Um, so say
[0:31:25] in your sub agent you wanted to be
[0:31:27] explicit about loading some context or
[0:31:29] doing something like that, you could
[0:31:30] hook in in that way. Then it the hook
[0:31:32] executes which in many cases is just a
[0:31:35] shell script. Um, there's also the tool
[0:31:37] calling loop. So basically as the agent
[0:31:40] runs, all it's doing is passing back a
[0:31:43] prompt with some tools and saying based
[0:31:45] off of this prompt and tools, what do
[0:31:47] you do next? You can call a tool, you
[0:31:49] can return markdown. And so that's how
[0:31:51] the agent works. And so the hooks
[0:31:53] integration basically hooks into that
[0:31:55] and says, "Okay, um when do I need to
[0:31:59] actually run certain things?" So after
[0:32:00] certain edit tools or things like that
[0:32:02] or when the agent actually stops. Um
[0:32:05] okay, when it stops again, run the run
[0:32:08] the hooks that are relevant for that
[0:32:09] thing. Um so let's try and make this a
[0:32:11] little bit more concrete.
[0:32:13] So, I built a um I built a little VS
[0:32:17] Code extension um that will Did I just
[0:32:20] mess that up?
[0:32:23] We'll see. Um
[0:32:26] this is the problem with having 10
[0:32:27] editors open at once, James. It's likely
[0:32:29] I've entered some characters that I
[0:32:31] should not have entered. Um so, I built
[0:32:33] this little VS Code extension, peon
[0:32:35] ping. Um, so for those in the chat who
[0:32:38] have ever played like Warcraft or World
[0:32:40] of Warcraft, you know the little peeons
[0:32:41] that like have the little sayings and so
[0:32:44] I mean this is a fun example but like uh
[0:32:46] basically you run this um extension and
[0:32:49] it will add in these hooks. Um so here
[0:32:53] let me look so you can see here's some
[0:32:55] different hooks I've defined. They're in
[0:32:57] GitHub hooks. So like all of my
[0:32:59] customizations are in this GitHub
[0:33:00] directory. Um and you can see the hooks
[0:33:02] I define here. So on session start I
[0:33:05] want you to run this on user prompt
[0:33:08] submit run this on tool use run this. Um
[0:33:10] and so I can kind of define different
[0:33:12] you know life cycle events here that I
[0:33:14] actually want to happen. Um and then
[0:33:16] what I want to do when uh when that
[0:33:19] actually happens. So um right now this
[0:33:22] is mostly like you know running a
[0:33:24] process whether that's like a shell
[0:33:26] script or like in this case it's running
[0:33:28] some JavaScript. Um but in the future
[0:33:30] like something that we're exploring is
[0:33:33] imagine if this thing could also hook
[0:33:35] back into VS Code.
[0:33:37] >> Ah like say you're like I want to I want
[0:33:40] to create a plan for this new feature
[0:33:42] and then I want you to create four chats
[0:33:43] that actually solve this.
[0:33:45] >> You can imagine actually having a hook
[0:33:47] that then can use the new chat thing
[0:33:50] populate the input box kick off all the
[0:33:52] commands then when it's done take all
[0:33:54] the outputs throw it back into the main
[0:33:56] chat. So you can do some really really
[0:33:57] cool stuff once we start wiring it up to
[0:34:00] VS Code commands. But as of right now
[0:34:02] it's this. It's still really powerful.
[0:34:04] Um and so let me go ahead and just like
[0:34:07] test this. You can This is how you know
[0:34:10] that I've been doing some testing. By
[0:34:11] the way, look at this session history
[0:34:14] inquiry.
[0:34:15] >> You saw saw mine earlier. It was like
[0:34:16] add footer, add footer, add footer, add
[0:34:18] footer.
[0:34:18] >> Yeah. James,
[0:34:21] >> also tips. This is a new thing. Um
[0:34:23] >> tip of the week.
[0:34:24] >> Tip of the week. Um, okay. Let's see. I
[0:34:28] don't know if I shared my system audio,
[0:34:29] so we'll see if it Oh, I think I
[0:34:31] actually did mess it up. Let's see.
[0:34:33] >> I think you just have like an extra
[0:34:34] slash in there.
[0:34:35] >> Yeah, I think I did.
[0:34:37] >> Uh, you know what I'm actually just
[0:34:39] going to do is
[0:34:41] I'm just going to run my thing, which
[0:34:43] will reset the state anyways. Okay,
[0:34:45] trying again. Let's do new chat. How
[0:34:48] many tokens have been burned by me
[0:34:50] saying hello?
[0:34:51] >> Ready to work.
[0:34:52] >> There we go.
[0:34:53] >> Oh, nice. I'm good. I heard it. I heard
[0:34:56] it.
[0:34:57] >> Okay. So, this is just a silly one.
[0:35:00] What?
[0:35:00] >> I do want I want a Starcraft one. It's
[0:35:02] like fire it up.
[0:35:03] >> Get him.
[0:35:06] >> Um, yeah. I mean, this is a silly one,
[0:35:08] but it kind of shows a lot of the things
[0:35:10] you can do.
[0:35:12] I I I won't take credit for this.
[0:35:14] Someone else had already built a hook,
[0:35:15] and I just made a little VS Code
[0:35:16] extension to to bootstrap a repo with
[0:35:18] it. Um, but I'll show like a more
[0:35:20] serious example now. Um, so let's go
[0:35:22] over to my coloring book app. Always a
[0:35:24] classic, the coloring book app, James.
[0:35:26] >> It's a it's a great app. I mean, one,
[0:35:28] it's personal because uh PICE built this
[0:35:30] for him and his family.
[0:35:32] >> Yep.
[0:35:32] >> And uh look, look, it's you and and the
[0:35:35] kids. It's cute. And it's kind of, you
[0:35:36] know, and and it's personal because it's
[0:35:38] like a thing that you you know, I love
[0:35:39] apps that you someone was asking. I was
[0:35:41] getting my haircut yesterday and
[0:35:42] they're, "Oh, what do you what do you
[0:35:42] build?" And I was like, "Ah, I build
[0:35:43] stuff for me." Like, "Oh, like what?" I
[0:35:45] was like, "Well, here's a weight
[0:35:46] tracking app. Like, here's this app.
[0:35:47] Here's that." And they're like, "Oh,
[0:35:48] that's cool." I'm like, "Yeah, like I
[0:35:49] have a problem. I build it for me
[0:35:50] because I want it even if it exists. So
[0:35:52] I can kind of like own the flow. So it's
[0:35:54] cool. And this evolved a lot since we
[0:35:56] saw it on Let It Cook like a year ago.
[0:35:58] >> Yeah. I mean, I have an iPad app now for
[0:36:00] this uh for for like road trips and
[0:36:03] going on a vacation soon. We try not to
[0:36:05] put the iPad too much in front of the
[0:36:06] kids, but you know, sometimes you got to
[0:36:08] do what you got to do. And rather than
[0:36:10] watching, you know, Brain Rot TV, um
[0:36:13] it'd be fun if he could color like real
[0:36:16] photos of our family. So I took this is
[0:36:18] an X.JS JS app, but I ported it recently
[0:36:20] with GPD53 codeex to uh iOS in like 30
[0:36:25] minutes. Um, so that was fun. Um,
[0:36:27] >> as one as one does. As one does
[0:36:29] >> as you do these days. I think you're
[0:36:30] right though, like this is really like
[0:36:33] the golden age of personal software.
[0:36:34] Like it's always been kind of a meme
[0:36:36] that us as developers would like do
[0:36:38] automate things that like take five
[0:36:40] minutes and it would take us a week. But
[0:36:41] like now it's like you can actually just
[0:36:44] build things. I mean, it's like a meme,
[0:36:46] but you really can just do things and
[0:36:48] build things. Um, and I have so many of
[0:36:50] these personal things and like you're
[0:36:52] whipping up your oh my posh
[0:36:54] configurator. You have all the CLI
[0:36:56] automation you built, the VS Code
[0:36:57] automation you built. Like we are like
[0:37:00] really building a lot of stuff. It's
[0:37:02] very rare that I don't have at least one
[0:37:03] or two agents running at once. I had to
[0:37:05] kill some before the stream because I
[0:37:06] didn't want them to mess the stream up.
[0:37:08] I like almost always have like three or
[0:37:10] four running. I was telling someone the
[0:37:11] other day, it's like here for example,
[0:37:13] like where if I was like, "Oh, it'd be
[0:37:14] really cool if you changed this or
[0:37:15] change that." You could just do it in
[0:37:17] real time. In fact, I was I was doing a
[0:37:19] podcast with Frank recently and we were
[0:37:21] talking about this switch website that I
[0:37:23] built and he was like, "Oh, it'd be
[0:37:24] great if you did this to this." And like
[0:37:26] literally as he was telling me his
[0:37:28] feature request, I was implementing it
[0:37:29] in real time. And I was like, "Cool,
[0:37:31] it's live." And he's like, "What?" And I
[0:37:32] was like, "You just told me what you
[0:37:34] wanted to change and I just had to
[0:37:35] change it and just did it.
[0:37:36] >> Just push it to prod." So anyways, I
[0:37:38] digress. Um, okay. So, um, coloring book
[0:37:42] app. Um, so what was I going to show?
[0:37:45] Hooks. So, we we just saw a fun one, but
[0:37:47] let me show you like a real kind of one
[0:37:49] that I have for my project. So,
[0:37:50] >> make it bigger.
[0:37:52] >> Yep. As one does and as one says,
[0:37:56] commits are free, James. People forget
[0:37:58] it all the time. You don't have to pay
[0:37:59] for your commits. They're free.
[0:38:02] >> They're free.
[0:38:02] >> I will never for the life of me
[0:38:04] understand why people don't commit more.
[0:38:06] You can use branches. In this case, I'm
[0:38:08] in Maine. So I will take that note that
[0:38:10] I shouldn't be pushing straight to main
[0:38:11] and I should have branch configurations
[0:38:12] on so I can't do that. But like you
[0:38:15] really should just be committing all the
[0:38:16] time. There's no reason if anything goes
[0:38:19] wrong you can roll back. All of your
[0:38:20] state is saved. So um I used to have a
[0:38:24] custom instruction that I would always
[0:38:25] This is a little distracting. I'm going
[0:38:27] to close that out. Um I used to have a
[0:38:29] custom instruction that I would run that
[0:38:31] was basically like at the end of the
[0:38:33] turn I want you to basically auto commit
[0:38:36] right. Yeah. Um, and there is the like
[0:38:39] keep and undo and all that in the
[0:38:41] timeline view in VS Code down here which
[0:38:43] has saved me a million times. But like
[0:38:46] it's better in my opinion because
[0:38:47] commits are free to just always commit.
[0:38:49] Um, so I have this stop hook. So this
[0:38:51] runs when uh when the agent turn
[0:38:54] actually stops as as it's aptly named.
[0:38:57] Um, and then it runs this uh shell
[0:39:00] script which is just basically
[0:39:02] committing uh with a time stamp. The one
[0:39:04] thing that's not great about this
[0:39:06] implementation, I will say, is the nice
[0:39:09] thing about the copod instruction is
[0:39:10] because it's running actually within the
[0:39:12] agent loop itself, you can have the
[0:39:13] agent like generate the commit message.
[0:39:15] >> So, this one's a little less good. Um,
[0:39:18] we're going to throw the iPad over
[0:39:19] there. I wanted to show the iPad app.
[0:39:21] >> You could you could use the Copilot SDK
[0:39:26] >> probably to actually generate and say,
[0:39:28] look at the commit messages and put it
[0:39:29] in here and that would be wild. Or like
[0:39:32] I actually don't think you can do this
[0:39:34] now, but like it'd be cool if you could
[0:39:36] have the AI generate like parameters and
[0:39:39] pass them into the hooks, right?
[0:39:42] >> Like like input parameters for the
[0:39:43] hooks. I actually don't that might be
[0:39:46] possible. Um
[0:39:47] >> I'm not sure,
[0:39:48] >> but that would be cool because then you
[0:39:49] could basically say like you can imagine
[0:39:51] like parameter commit message and then
[0:39:53] like that agent would prefill it when it
[0:39:55] starts the hook, right?
[0:39:57] >> Um
[0:39:58] >> anyways, so pretty simple. I you know
[0:40:00] this was a totally vibecoded
[0:40:02] implementation for this shell script
[0:40:03] because like James I really don't want
[0:40:05] to be dealing with shell scripts
[0:40:06] generally. Um that's not the level of
[0:40:08] abstraction I want to be working in. Um
[0:40:10] but let's go ahead and test this out. So
[0:40:13] also new things in in VS Code you see
[0:40:15] like I have the more session information
[0:40:18] up here right next to the chat icon.
[0:40:20] This is not the default but there is a
[0:40:21] setting you can click in here and like
[0:40:23] say like do things and it can send
[0:40:26] messages. I can query past sessions.
[0:40:28] It's pretty neat. That's
[0:40:31] >> so where was I? Um over here. Okay, it
[0:40:35] was just telling me it started the iPad
[0:40:36] thing. Um let's go ahead and test this
[0:40:38] out. So I'm going to get my um output
[0:40:41] window up here. Um
[0:40:48] output. There we go. Um so if you're
[0:40:52] ever debugging these things when you're
[0:40:53] authoring them and you want to make sure
[0:40:55] they work, you can go to this GitHub
[0:40:56] copilot chat hooks option. Oh, nice.
[0:40:59] >> Um, I'm going to go ahead and clear it.
[0:41:01] And let's just do something simple like
[0:41:04] um
[0:41:05] make their read me
[0:41:09] say I love James wants a magnet.
[0:41:13] It's Valentine's.
[0:41:15] >> It's true. It's happening.
[0:41:17] >> Okay. So,
[0:41:18] >> great commit. Great commit.
[0:41:20] >> Great commit. Um, commits are free.
[0:41:23] Maybe not the tokens used to generate
[0:41:25] this demo, but the commit is free. Um,
[0:41:28] >> we can see the we can see the context of
[0:41:30] how how much this took. So, that'd be
[0:41:32] perfect.
[0:41:32] >> Yeah. So, let's actually I'm going to
[0:41:34] pop open the SCM view and also this and
[0:41:39] okay, so we have a change and the push
[0:41:42] failed. Why? Okay, it just succeeded.
[0:41:45] Let's sync changes. Um, now remove that.
[0:41:48] Uh, and I'm going to clear this again.
[0:41:54] >> I never know what's going on with my git
[0:41:55] config. I have three different Git
[0:41:57] identities on this machine. Um, I have
[0:42:00] my personal GitHub account, I have my
[0:42:03] work GitHub account, and I have my work
[0:42:05] EMU GitHub account. And so I always have
[0:42:07] all kinds of issues. Okay, so this one
[0:42:09] worked. Um,
[0:42:10] >> so it said, okay, I got a hook. Um, we
[0:42:14] have a stop hook and then this is
[0:42:16] actually just outputting from from the
[0:42:18] hook. So it's saying, okay, I ran auto
[0:42:20] commit, one file changed. We had two
[0:42:22] deletions. Sorry, James, for deleting
[0:42:24] you. Um, and changes were pushed
[0:42:26] successfully. So, pretty
[0:42:28] straightforward. And then, of course, I
[0:42:30] can come down here
[0:42:31] >> to the graph. You can see like the auto
[0:42:34] commit was kicking in right here. So,
[0:42:37] this is actually pretty simple, but I
[0:42:38] think these things are really powerful.
[0:42:40] Um, so there's already some really cool
[0:42:42] ideas that people have been throwing
[0:42:43] out. So, like examples would be um like
[0:42:46] Orin had a fun one for like open
[0:42:48] telemetry. So he's like, I want to like
[0:42:50] at where he works, he wants to be like,
[0:42:52] I want to know like what prompts people
[0:42:55] are sending and stuff like that. And you
[0:42:56] can imagine like wiring up open
[0:42:58] telemetry to the agent life cycle and
[0:43:00] things like that. So there's all kinds
[0:43:01] of cool examples people have done in the
[0:43:03] community already. But I'm really
[0:43:05] excited we have hooks integration now.
[0:43:06] Um, any other questions on hooks before
[0:43:08] I show off queuing and steering, James?
[0:43:10] >> I don't think so. Yeah, there's a great
[0:43:12] documentation. and I'll link to a bunch
[0:43:13] of examples like oh you could like run
[0:43:15] prettier you could like do a validation
[0:43:17] tool like you could run security checks
[0:43:19] right you could do all these different
[0:43:20] things inside of it. So definitely check
[0:43:22] out the the actual documentation on it.
[0:43:26] Super powerful. I'd love to see a hooks
[0:43:27] like uh hooks hooks marketplace
[0:43:30] basically. So it' be pretty pretty neat
[0:43:33] to see.
[0:43:34] >> Yeah.
[0:43:35] >> Um okay I'm going to jump back over to
[0:43:38] my coloring book app. I was trying to
[0:43:39] get a diagram created for you guys. Um,
[0:43:42] so, um, wanted to show off the iPad app.
[0:43:45] Let's see.
[0:43:46] >> Oh, I'm going to log in over here. All
[0:43:48] right.
[0:43:49] >> Yeah, you log in to color. Come on, man.
[0:43:52] Can I get one for free guest account?
[0:43:55] >> You can. Um, okay. Here we are. We're
[0:43:57] back. Um, yes, I do want to save the
[0:43:59] password. Um, okay. So, this is the iPad
[0:44:02] app. I made a little bit of a kid mode
[0:44:04] cuz my son does this thing like all the
[0:44:06] kids apps have this where they're like
[0:44:08] just like
[0:44:09] >> it's kind of a little scary how good
[0:44:11] they are at using the iPad. So you need
[0:44:12] to like lock them in
[0:44:14] >> so they can't go do anything else. So
[0:44:15] like here I can come in I can color.
[0:44:18] Super fun. Um I can swap between the
[0:44:20] pages.
[0:44:22] >> Um and then to exit you have to enter
[0:44:24] the code and you know I have the most
[0:44:26] complex code one two three four
[0:44:28] naturally
[0:44:28] >> naturally.
[0:44:30] >> Anyways that's the iOS app. Um, let's
[0:44:32] see if we got our Okay, the Excala draw
[0:44:35] drawing isn't exactly what I wanted
[0:44:36] here, so I'll just demo it live. We'll
[0:44:39] do it live. So, uh, queuing and
[0:44:41] steering.
[0:44:42] So, James, if you're like me, you try to
[0:44:45] craft a beautiful prompt, but often it
[0:44:48] just doesn't work, right? Um, you know,
[0:44:51] maybe maybe the model's not
[0:44:53] understanding exactly what you want.
[0:44:55] Maybe you just wrote a bad prompt. Not
[0:44:56] trying to blame anybody here. I'll blame
[0:44:58] myself. Um, but a lot of times like the
[0:45:00] agent starts working and you're like,
[0:45:01] "Oh man, I really wish I had also said
[0:45:03] this." Because you can tell it's like
[0:45:05] reading a certain files and you're like,
[0:45:06] "No, no, no, no, not that one. I want
[0:45:08] you to do this other one instead." Um,
[0:45:10] and so like I'm going to try to come up
[0:45:11] with like a scenario here. Um,
[0:45:15] let's compress the UI so I can actually
[0:45:19] see my images above the fold and go
[0:45:23] ahead and attach like what I see here
[0:45:25] because I can't see any images.
[0:45:28] Um, and I'm going to go ahead and hit
[0:45:30] enter. And now I'm realizing I also have
[0:45:33] an iOS app in this project, right?
[0:45:35] >> And so I want to say in the web app. And
[0:45:39] so I can hit enter. Um, or I can steer.
[0:45:43] Um, and so what steering basically does
[0:45:47] is, um, rather than waiting for the
[0:45:50] entire agent to finish what it's doing
[0:45:52] and then send a message, it actually,
[0:45:54] you notice it sent it at the next
[0:45:56] available point, which in this case was
[0:45:58] right here, right after, you know, the
[0:45:59] reasoning text came in. Um, and this is
[0:46:03] really powerful because basically we're
[0:46:04] injecting it at the next tool calling
[0:46:06] point. So going back to what I said
[0:46:08] earlier, the agent's just a loop, right?
[0:46:10] and it's calling tools and steering is
[0:46:12] basically saying whenever whatever is
[0:46:13] currently happening is is done whether
[0:46:16] that's writing text uh or calling a tool
[0:46:18] like reading a file or editing a file
[0:46:20] send this message right so it won't
[0:46:22] interrupt literally exactly what it's
[0:46:24] doing but the next moment that it gets
[0:46:26] it will interrupt so this thing could
[0:46:28] potentially have run for another five
[0:46:29] minutes and done the wrong thing right
[0:46:31] yeah
[0:46:31] >> but with the steering message I can go
[0:46:33] ahead and interject to make sure it's
[0:46:34] doing the right thing um chat debug view
[0:46:38] let's see if I can roll down here and
[0:46:40] see where that actually happened. Um, so
[0:46:43] here was my initial message where I
[0:46:44] said, okay, let's um let's actually
[0:46:49] implement this app. I all my
[0:46:51] instructions are attached right there,
[0:46:52] which is why it's a little messy. Okay,
[0:46:54] let's compress the UI. And then it
[0:46:56] started doing stuff. So you can see I'm
[0:46:57] starting to get some tool calls. It's
[0:46:59] reading some files. It I had some text
[0:47:01] back. And then if I come back down here,
[0:47:04] you can see that it's just basically
[0:47:06] appending my uh my request. I said in
[0:47:10] the web app and that's tagged user
[0:47:12] request um right after that read call.
[0:47:14] And so then it's just going and keeping
[0:47:16] doing what it was doing with this new
[0:47:18] context. And so that's all that's
[0:47:19] happening when steering is going on. Um
[0:47:22] and it's exactly what it sounds like.
[0:47:23] You're steering the agent while it's
[0:47:25] working. Um any questions, James, on
[0:47:27] steering? Well, so when you're in there,
[0:47:29] so it's still working like bring up the
[0:47:31] options again. So if you start typing
[0:47:32] something,
[0:47:34] so here you have just the main one, but
[0:47:37] bring up the little toggle again, the
[0:47:39] little chev.
[0:47:40] >> So there's stop and send, add to Q, and
[0:47:43] then steer with message. So
[0:47:45] >> like basically they're kind of what it
[0:47:48] says, but stop and send is like just
[0:47:50] immediately stop what you're doing,
[0:47:52] right? Like stop it, you've gone too
[0:47:54] far, like reset, right? And it's it's
[0:47:57] kind of manually as if you hit stop,
[0:47:59] enter a message, go. Then there's the
[0:48:01] steer with message, which is what you
[0:48:03] did. I think that's enter is the
[0:48:05] default, right? So
[0:48:06] >> I could have just hit enter, but I
[0:48:07] actually wanted to show off the chevron,
[0:48:08] so I I clicked it. Um, you can also
[0:48:11] change that default. So you could say
[0:48:13] actually I want enter to be queuing.
[0:48:15] >> I think I for me actually I think I will
[0:48:17] change that because I'm I'm queuing
[0:48:19] messages much more frequently than I'm
[0:48:21] steering. Yeah. Um, so I think that
[0:48:23] personally for me will probably be my
[0:48:25] default. Um, let us know what you would
[0:48:27] like to see as the default as you use
[0:48:28] this more. But that is a user
[0:48:30] configurable setting for like what
[0:48:31] behavior you want on enter.
[0:48:33] >> That's cool because the add to Q then so
[0:48:35] is basically a queue, right? So it's
[0:48:37] like as soon as it's done then do then
[0:48:40] do the next thing. So, finisher and I
[0:48:41] use queuing all the time and I remember
[0:48:44] I was recording a video like with my
[0:48:46] team of like here's how I here's how I
[0:48:49] here's how I code
[0:48:50] >> and like basically it was like oh um
[0:48:56] I am already written the next prompt
[0:48:59] while it's still cooking right I'm just
[0:49:01] waiting to hit send right so there's
[0:49:03] that here's a good one from
[0:49:06] does the steering cost any is there any
[0:49:08] additional premium requests how does
[0:49:09] that work
[0:49:10] >> it it is an additional premium request.
[0:49:13] So um it's anything in copilot that is a
[0:49:16] user initiated request. So, a prompt is
[0:49:19] uh is charged at a premium request. And
[0:49:22] obviously, like it would be better like
[0:49:24] as a user like it's great if you never
[0:49:26] had to pay for that, but I think uh it's
[0:49:29] basically what you would do anyways,
[0:49:31] right? Um you would have to correct the
[0:49:33] agent. Um and it's saving you time. And
[0:49:36] to be honest, like it is a pretty big
[0:49:37] abuse vector if we didn't do that. Like
[0:49:39] you could in theory just infinitely
[0:49:41] steer the agent to keep doing more and
[0:49:42] more tasks and never stop, right? Um, so
[0:49:46] there's like some abuse, you know,
[0:49:48] protection in there by charging a
[0:49:49] premium request for that.
[0:49:51] >> Yeah.
[0:49:51] >> Um, okay. Maybe I'll show the queuing
[0:49:54] because I also use it quite frequently.
[0:49:55] >> Okay.
[0:49:56] >> Um, so this is better. It's more
[0:49:58] condensed. I don't know why that green
[0:49:59] bubble is there. Um, so let's go ahead
[0:50:02] and uh better.
[0:50:06] Can we make it more condensed?
[0:50:09] And then I'm also noticing uh green
[0:50:12] bubble. get rid of it.
[0:50:15] Uh right here.
[0:50:18] And so this one, because my default
[0:50:19] isn't queuing, I'll click that. So I
[0:50:21] have a cued message here. And then let's
[0:50:23] find something else fun to do. Um James,
[0:50:26] give me another suggestion. Um
[0:50:32] Yeah. Then maybe do you have favorites?
[0:50:34] Can you add like favorites to
[0:50:36] >> Yeah, that's what this thing is.
[0:50:37] >> Oh, okay.
[0:50:38] >> Yeah.
[0:50:38] >> Maybe is there a filter button to only
[0:50:40] see favorites? um
[0:50:42] >> or show all maybe, you know,
[0:50:44] >> uh add filter to only show favorites as
[0:50:49] well. Um
[0:50:52] and uh so you can see they're all just
[0:50:55] kind of lined up here. You can drag and
[0:50:57] drop, right? So I'm actually going to
[0:50:59] say boom, put that there. Um and these
[0:51:02] are all my cued messages. And uh so now
[0:51:05] I can just like leave my keyboard and
[0:51:07] those next prompts are all going to run,
[0:51:09] right? Whenever this one actually
[0:51:11] totally finishes, the technical term is
[0:51:14] like the agent will literally send a
[0:51:15] stop message saying I'm done
[0:51:17] >> like this turn is over. When we get
[0:51:19] that, that is when the typically the uh
[0:51:22] you know the the turn of your
[0:51:24] conversation would end. It say I'm done.
[0:51:26] It do a summary like this, right? Um and
[0:51:28] then it would start the next request. Um
[0:51:30] so now we're starting on the made with
[0:51:31] love one, it looks like. Um and uh the
[0:51:35] difference again with steering and
[0:51:36] queuing is steering is just going to
[0:51:38] immediately next opportunity gets throw
[0:51:40] it in there, right? Um whereas queuing
[0:51:43] is waiting for it to finish its current
[0:51:44] task. So in theory, could I have queue
[0:51:47] could I have steered with all those
[0:51:48] messages and just had it done all that
[0:51:50] in one turn?
[0:51:51] >> Yes, maybe. from like a from a like
[0:51:55] agent quality and um output standpoint,
[0:51:59] the more things you ask the agent to do
[0:52:01] in a turn as a conversation, the more
[0:52:03] likely it is to not do what you want.
[0:52:06] >> So, it's actually better to send those
[0:52:07] as as separate messages actually. You're
[0:52:10] basically telling it in one turn to do
[0:52:12] one thing, which is ideal.
[0:52:13] >> Yeah, I've noticed that I've
[0:52:14] accidentally steered when I meant to
[0:52:16] queue and then it'll be like, "Oh, cool.
[0:52:17] I'll go do that and then I'll go back to
[0:52:19] finish the thing that I was starting."
[0:52:20] But actually I was like no it's like a
[0:52:21] dependency or like it'll try to like
[0:52:23] it'll try to you know it'll take a
[0:52:25] little bit longer than what I wanted as
[0:52:26] well. Um so someone says can you steer
[0:52:29] it when it's waiting for approval to run
[0:52:30] a terminal command? Maybe the command
[0:52:32] isn't quite right. I mean yeah I think
[0:52:34] you would just probably steer it or you
[0:52:36] probably wouldn't steer it if the
[0:52:37] command's not right. You would probably
[0:52:39] stop it and send it immediately.
[0:52:42] >> Yeah. Yeah. Oh there's my love. Um
[0:52:45] >> yeah so you could do that. Um you can
[0:52:47] also just basically tell um uh copilot
[0:52:51] in the terminal like or sorry in chat
[0:52:53] like I don't want to run this command.
[0:52:54] You can skip it and then uh that
[0:52:58] sometimes works because copilot just
[0:53:00] basically knows you skipped it and it
[0:53:01] doesn't know why you skipped it, right?
[0:53:02] And so that's where like if it
[0:53:03] >> if you think it might be confusing, you
[0:53:05] could send another message or you could
[0:53:06] just like
[0:53:07] >> skip it and see if co-pilot figures it
[0:53:09] out and not burn the premium request
[0:53:11] trying to steer it. That's up to you if
[0:53:12] you think your time is worth that or
[0:53:14] not. Um, I also noticed a visual bug.
[0:53:16] You see how the queueing text is like
[0:53:18] the gray text? And then I noticed when I
[0:53:20] sent this, look, this is all in gray as
[0:53:22] well. So, we need to fix that. Um, all
[0:53:25] right. Let's see. We got rid of. So,
[0:53:26] that was great. Like, in that one thing,
[0:53:28] I went and by the way, as a manager, I
[0:53:30] do this all the time. I I know it's
[0:53:31] probably the same for you, Jen. You're
[0:53:32] like,
[0:53:33] >> you have like two minutes in between
[0:53:35] calls and you're in a manager schedule
[0:53:36] and you're like, I just need to f I have
[0:53:38] like 10 things. I just need to fire them
[0:53:39] off and I will come back after I'm done
[0:53:42] and make sure it actually did what I
[0:53:44] wanted.
[0:53:44] >> Exactly. Yeah,
[0:53:46] >> this looks pretty good. I think I'm
[0:53:48] getting a little too I mean this is the
[0:53:49] amount of toggles and buttons I really
[0:53:51] need to revisit uh what I'm doing here.
[0:53:55] Of course, I favored all the images so
[0:53:56] the toggle doesn't work. But um this is
[0:53:59] looking much better in my opinion. And
[0:54:00] by the way, no changes. Why?
[0:54:03] >> Wow.
[0:54:05] >> Wow. Wow. Stop hook done.
[0:54:08] >> Yep.
[0:54:08] >> Magical. Magical. That's cool. These are
[0:54:11] just some of the features. There's a
[0:54:12] whole bunch of new things that like land
[0:54:14] every single day. So, um, definitely
[0:54:16] check out the logs. Uh, see what's
[0:54:18] happening on the updates. I'll take that
[0:54:19] on your screen. Boop. Now that we're
[0:54:21] basically at our hour point, this is
[0:54:23] awesome. I think it's so cool to see not
[0:54:25] just like all the great enhancements,
[0:54:26] everything that like ship now. That
[0:54:27] stuff's in stable, funnily enough. Like
[0:54:29] I showed some insider stuff, but like
[0:54:31] you showed everything that's like that
[0:54:32] stuff's available in stable today. So,
[0:54:34] when you update just your your blue your
[0:54:36] blue VS code, boom, you're good to go.
[0:54:38] If you're like us, rolling insiders
[0:54:40] every single day. It was great. I did
[0:54:42] wake up this morning. I was like, "Oh,
[0:54:43] there's an update." Oh, amazing.
[0:54:45] >> Always sometimes multiple times a day.
[0:54:47] >> You got to It's like But you know, so
[0:54:49] like I think like the velocity of the
[0:54:51] ship, right, is is like always moving.
[0:54:54] And I'll also point out you can't really
[0:54:55] see it. We we shouldn't had you
[0:54:58] we should have launched it fresh cuz
[0:55:01] there is the new like uh update download
[0:55:03] thing in the bottom as well. Is there a
[0:55:05] progress bar now? Did I see that in a
[0:55:07] release note?
[0:55:08] >> Um maybe question mark. I haven't I have
[0:55:11] updated to today but I skipped that. But
[0:55:13] yes, like if there's a pending update,
[0:55:14] we'll actually show that like in the
[0:55:16] bottom um and then in the status bar and
[0:55:19] then we're working on basically being
[0:55:21] able to tell you what's in that new
[0:55:22] version. Um, so like the same automation
[0:55:25] that you're using for website and notes,
[0:55:27] right? Imagine if it's like, oh, you
[0:55:29] should update because today's version
[0:55:30] actually has these three things. Um, so
[0:55:33] that's kind of where we're going with
[0:55:34] that. But yeah, lots of new stuff,
[0:55:36] plenty to try out both in insiders and
[0:55:38] in stable. There's a lot of things we
[0:55:39] didn't talk about that are in insiders
[0:55:41] that I'm excited about, but we're going
[0:55:43] to try to be better with this weekly.
[0:55:45] Um, like I'm actually off today and I
[0:55:47] came in because I care so much about
[0:55:48] cooking with James and all of our
[0:55:50] community. So, um, we're going to try to
[0:55:53] be more regular. It had been kind of a
[0:55:54] like regular thing and then you know how
[0:55:56] life is. Um, but we're going to try to
[0:55:58] keep it a regular thing.
[0:55:59] >> Well, I also want to point out really
[0:56:01] quick, uh, talking about regular things,
[0:56:03] we won't do one next week because
[0:56:05] people, there is going to be the VS Code
[0:56:09] live agent sessions day next Thursday.
[0:56:13] Let me go and bring that puppy up over
[0:56:14] here. Let me share my me pull my
[0:56:16] StreamYard over here. Boop. And then
[0:56:18] pull this up. Boop. I'll put a link to
[0:56:20] that. It's the agent sessions day. It's
[0:56:23] the yearly sort of like big
[0:56:26] >> VS Code comp basically. That's what I'm
[0:56:28] gonna call it. Uh here
[0:56:31] >> and you can see it here on YouTube.
[0:56:33] There's already a hundred people
[0:56:34] waiting. They're just sitting there
[0:56:35] waiting for a whole week next week.
[0:56:37] >> Ready to go.
[0:56:38] >> They're ready to go. Um be ready to go
[0:56:41] there. So check that out. I'll put a
[0:56:42] link uh or you just go to the release
[0:56:44] notes. You'll find it. Just agent
[0:56:45] sessions. You're on YouTube anyways.
[0:56:47] Just go and find it. There's gonna be
[0:56:48] tons of stuff happening. So with the
[0:56:50] team, with the engineers, with the PM.
[0:56:52] So definitely like check that out. Super
[0:56:53] excited uh for that. U be so many new
[0:56:57] goodies. That's only a week away. So we
[0:56:58] won't be cooking next week because I'll
[0:56:59] also be out of the country. So that will
[0:57:01] also be a little bit hard for me to
[0:57:02] stream, but you got Asia sessions day
[0:57:04] coming up and then we'll be back in a
[0:57:05] few weeks talking about all the new
[0:57:07] stuff that is shipped to insiders and uh
[0:57:09] stable as well. Pierce, thanks for
[0:57:11] taking time on your your day off. Have
[0:57:13] an amazing uh long weekend here in the
[0:57:15] States. Happy Valentine's Day. I love
[0:57:17] you.
[0:57:18] >> Byebye.
[0:57:19] Seating.
