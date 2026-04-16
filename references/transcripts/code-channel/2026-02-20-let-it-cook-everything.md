---
video_id: uquSQY10AGM
title: "Let it Cook - This changes EVERYTHING"
url: https://www.youtube.com/watch?v=uquSQY10AGM
channel: "@code (Visual Studio Code)"
published: 2026-02-20
speakers:
  - James Montemagno
  - Pierce Boggan
topics:
  - copilot-updates
  - agent-workflows
  - tips-and-tricks
relevance: secondary
---

# Let it Cook - This changes EVERYTHING

James and Pierce cover the latest in VS Code and GitHub Copilot.

## Key Topics Covered

- Latest VS Code and GitHub Copilot updates
- Agent workflow demonstrations

## Links

- VS Code Insiders: https://aka.ms/vscode/insiders

---

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:03] [music]
[0:00:09] [music]
[0:00:17] Woohoo! [music]
[0:00:24] [music]
[0:00:26] Heat!
[0:00:27] Heat. Heat. N.
[0:00:32] [music]
[0:00:37] Heat. Heat. N.
[0:00:40] [music]
[0:00:47] Woo! [music]
[0:00:57] [music]
[0:01:04] [music] Woo!
[0:01:10] [music]
[0:01:18] >> [music]
[0:01:27] [music]
[0:01:33] [music]
[0:01:34] >> Hey,
[0:01:43] Well, welcome back everyone. What is
[0:01:46] happening? There was a little tiny delay
[0:01:48] there. Do you like that, Burke?
[0:01:50] >> Can you hear James?
[0:01:51] >> Yeah, [laughter]
[0:01:53] >> you can hear me.
[0:01:56] >> Yes, we can hear James.
[0:01:58] >> Okay, perfect. [laughter]
[0:02:00] >> I can't hear him at all. What's
[0:02:02] >> refresh? I can hear you. Oh, refresh.
[0:02:04] Refresh. Refresh. Ver. Oh my goodness.
[0:02:09] [laughter]
[0:02:09] >> We're live, man.
[0:02:11] >> We're live. You bring Burke back for a
[0:02:13] day. Well, welcome everyone back. There
[0:02:14] goes Burke. He's here and then he's
[0:02:16] gone. As long as you can hear me,
[0:02:17] Pierce, that's all that matters. Welcome
[0:02:19] back everyone to Let It Let It Cook.
[0:02:21] We're here. We're cooking live. I'm
[0:02:23] fresh off of a plane from Korea, which
[0:02:25] means I've not done any cooking.
[0:02:27] Actually, I have. Like, if you actually
[0:02:28] go to my GitHub page, Pierce, and you
[0:02:30] look, there are plenty of green dots.
[0:02:33] >> I'm sure there are.
[0:02:34] >> I've been [laughter] I every time
[0:02:36] >> that plain Wi-Fi cook going for you? Oh,
[0:02:39] well, we took the Hawaiian Airlines
[0:02:41] Dreamliner, which has zero internet on
[0:02:43] it at all. So, I nailed it. Uh, so I did
[0:02:46] what I would do is I was like, because I
[0:02:48] knew this ahead of time, I I read I
[0:02:49] watched read some reviews and, uh,
[0:02:52] basically, let me bring back Pierce, see
[0:02:54] Burke, see if he could hear me. Can you
[0:02:55] hear me now, Burke? There you go.
[0:02:57] Perfect. Good. He's good to go. Um,
[0:02:58] [laughter]
[0:03:01] it's not my fault.
[0:03:02] >> No, I can't hear you. What? No, I hear
[0:03:04] you.
[0:03:05] >> [laughter]
[0:03:07] >> But uh so I knew I knew that there was
[0:03:09] going to be no internet on the plane.
[0:03:11] Then going there was like 12 hours.
[0:03:12] Coming back was nine and a half. So I
[0:03:14] fired off just tons on the GitHub mobile
[0:03:16] app. Just like tons of things to cook
[0:03:18] and I came back and my tiny my tiny
[0:03:20] clips app has tons of updates. It's good
[0:03:22] to go. But whenever we be on a train,
[0:03:23] I'm just like always like, "Okay, what
[0:03:24] else can I do? What else can I do? What
[0:03:25] else can I do?" Uh so I've been cooking
[0:03:27] non-stop, which has been good. However,
[0:03:29] I haven't updated I haven't even opened
[0:03:31] up VS Code at all. So I'm pretty sure
[0:03:32] nothing has changed. pretty sure in like
[0:03:34] a week.
[0:03:35] >> I responded to your tweet. I was like,
[0:03:38] "We only have an hour and I actually
[0:03:39] have a hard stop today and I'm actually
[0:03:42] worried about being able to go through
[0:03:43] all this stuff in one hour."
[0:03:45] >> So,
[0:03:45] >> we should get to it then because
[0:03:46] actually I don't know either, Pierce.
[0:03:48] Like, you keep posting about stuff and
[0:03:49] I'm like, I'm trying to follow you and
[0:03:51] I'm trying to follow what the CLI is
[0:03:52] doing and I I don't know what's going
[0:03:55] on.
[0:03:56] >> You want to know what's funny? What I'm
[0:03:58] doing right now? I'm literally opening
[0:03:59] up my own Twitter feed to be like, "What
[0:04:01] did we do? [laughter]
[0:04:04] Sounds about right. Sounds like
[0:04:05] >> this is the problem, man. Like I'm
[0:04:06] serious for just for devs in general.
[0:04:09] Like if we're struggling with this,
[0:04:10] what's everybody else doing, man?
[0:04:12] >> Yeah. I mean, we're definitely I I think
[0:04:15] like if you watch agent sessions day,
[0:04:17] Pong and I had this session which was
[0:04:18] like
[0:04:20] how do you even like operate in a world
[0:04:23] separate from like the writing of the
[0:04:24] code part where things are moving so
[0:04:26] fast? And so like I know for us the only
[0:04:29] way we could do it is we had to build
[0:04:30] even more automation. Like James built a
[0:04:32] ton for release notes. Like I have a ton
[0:04:35] for staying on top of what's changing
[0:04:37] every day in the codebase, what I need
[0:04:38] to be reviewing because
[0:04:40] >> if you don't have that, I think you know
[0:04:42] a couple days ago we had like 200 PRs
[0:04:43] merged in VS Code separate from VS Code
[0:04:46] Cophat, right?
[0:04:47] >> Yeah.
[0:04:48] >> I mean that is like not reasonable for
[0:04:50] any human like mentally to be able to
[0:04:52] take in. So
[0:04:54] >> yeah, it's pretty wild. like we're
[0:04:55] getting to the like the limits of human
[0:04:57] ability really quickly and [laughter]
[0:04:59] having to figure out how to use AI.
[0:05:03] >> Um well, let me share my screen. I can
[0:05:05] start showing some of the cool stuff. Um
[0:05:09] always scary sharing my screen on this
[0:05:10] on this.
[0:05:11] >> Well, I won't bring it up. I won't bring
[0:05:12] it up here since you're actually
[0:05:13] >> Oh, no. No. I have to restart.
[0:05:16] >> Oh gosh.
[0:05:18] Well, I was uh that's a the nice part
[0:05:20] like you're saying, Burke, is like what
[0:05:22] I've been trying to do in like the CLI
[0:05:23] and the VS Code change log release notes
[0:05:25] is use AI to like bubble up the top
[0:05:27] features that are like here's the most
[0:05:29] important two, three, four things you
[0:05:30] really need to know about and then go a
[0:05:32] little bit deeper. Like the CLI change
[0:05:34] log is like, hey, here's everything. So,
[0:05:36] it's like here's 85 different updates,
[0:05:38] you know what I mean, in it. And then
[0:05:40] Nick and the team for VS Code is like
[0:05:42] pretty trimmed down. It's like it's
[0:05:43] pretty much like here are the important
[0:05:44] things in there as it goes, but I'm
[0:05:46] still bubbling it up because sometimes
[0:05:47] there's some big updates in there, but I
[0:05:49] really want to turn that thing into an
[0:05:50] RSS feed because then anyone could like
[0:05:52] bump it into the thing uh in general. I
[0:05:54] think that'd be nice. But I am I am the
[0:05:56] number one feedback that I've addressed
[0:05:58] uh again via right before I got on the
[0:06:01] plane.
[0:06:01] >> I'm sure that was really profound. My
[0:06:03] audio cut out again. So, [laughter]
[0:06:05] >> oh no,
[0:06:08] >> I can hear Pierce. I can't hear James.
[0:06:10] [laughter]
[0:06:11] Your machine has decided to selectively
[0:06:13] mute. All right, I want to share my
[0:06:14] screen. I don't know what you guys about
[0:06:16] while I was gone. Let's see if this
[0:06:17] actually works.
[0:06:18] >> Nothing at all. I blame I blame
[0:06:20] >> I mean it is Friday to be fair. So,
[0:06:23] sure. I'll share some system audio. Why
[0:06:25] not?
[0:06:26] >> All right.
[0:06:27] >> What browser are you using, Burke? Are
[0:06:29] you using
[0:06:30] >> I was ching for I'm using Safari.
[0:06:33] >> Oh, well, there's your problem.
[0:06:34] >> Yeah, you can't use Safari.
[0:06:36] >> You can't use Safari. I always use
[0:06:37] Safari as my default generally on Mac OS
[0:06:39] just because I like all that syncing
[0:06:40] between my devices.
[0:06:42] >> Um but like you can't use it. It doesn't
[0:06:44] work with Streamyard.
[0:06:45] >> Yeah, it doesn't work.
[0:06:45] >> Okay, let me download a better browser.
[0:06:47] Let me get Edge.
[0:06:47] >> Yeah, just get Edge.
[0:06:49] >> There you go.
[0:06:49] >> I have a new This is a new machine.
[0:06:51] >> Oh, that's why excuse. All right, let me
[0:06:55] bring up your Are you ready? Are you
[0:06:56] ready, Pierce?
[0:06:57] >> I am ready. Yeah, of course.
[0:06:59] >> There it is. Look at all these updates.
[0:07:00] Where What is this? Oh, it's in It's
[0:07:02] inside.
[0:07:02] >> Yeah, so you can open the release notes.
[0:07:04] I forget the exact command. Yeah, code
[0:07:06] show release notes.
[0:07:08] >> Bam.
[0:07:08] >> And as of like last month, we had uh
[0:07:12] release notes for insiders. Um so to the
[0:07:16] point we were just talking about around
[0:07:18] automation, Burke does have issues. Um
[0:07:21] [laughter]
[0:07:22] um
[0:07:23] >> to the point around automation, right?
[0:07:25] Like we had to go build this because
[0:07:27] it's literally impossible to keep up
[0:07:28] otherwise. But this is cool. This is a
[0:07:30] way and I mean in the community we have
[0:07:32] so many accounts now. Like we have
[0:07:34] what's the what's the handle again James
[0:07:36] for our change log uh VS Code log
[0:07:39] >> VS Code change log. Yep.
[0:07:41] >> Brilliant. And then of course if you
[0:07:43] follow like Orin, right? Orin's going to
[0:07:44] be tweeting about it. So
[0:07:46] >> Orin the official change log.
[0:07:48] >> Orin has tweeted about it before I even
[0:07:49] know we've added something to VS Code.
[0:07:51] Um so follow Orin everybody.
[0:07:54] >> The other one can y'all hear me? The
[0:07:56] other one is Tech Sage.
[0:07:58] >> Yes. Yes. I saw he started some nice
[0:08:00] daily updates.
[0:08:01] >> Yeah. I find out about our stuff from
[0:08:03] people that [laughter] don't work here.
[0:08:06] >> H that that's living in a in an age
[0:08:09] where you're moving faster because of
[0:08:10] AI, right? Um okay. So, um just if
[0:08:13] you're ever like I have no idea what's
[0:08:14] going on, this is like a good place to
[0:08:16] start. But I think it's like one of
[0:08:17] those things of
[0:08:19] you don't like yes, like there is this
[0:08:21] pressure to like stay up to date with
[0:08:23] all the latest stuff, but to be honest
[0:08:24] like the team is moving slash already
[0:08:28] been doing weekly releases, right? And
[0:08:30] so, you know, you don't have to
[0:08:32] necessarily be following the daily
[0:08:33] insider stream. You don't even
[0:08:35] necessarily have to be following the
[0:08:36] weekly stream. The reality is like if
[0:08:38] one of these things is really useful,
[0:08:40] it's going to start bubbling up in our
[0:08:41] our broader content we do for VS Code,
[0:08:44] right? Yeah.
[0:08:44] >> Um,
[0:08:45] >> so yeah, like don't be like, "Oh, I
[0:08:47] didn't know about this very obscure
[0:08:49] setting that landed in Insiders Today."
[0:08:51] I you don't have to stress yourself out
[0:08:53] so much about that sort of thing, right?
[0:08:55] Um, I'm trying to think. Okay. So, first
[0:08:57] thing I want to show is um something
[0:09:00] we've been working on a lot. And so, I
[0:09:03] have my coloring book app here. This is
[0:09:04] a Nex.js app. I've shown this on the
[0:09:07] stream before. Uh the inspiration was
[0:09:10] that uh my kids love to color and I
[0:09:13] wanted to give them like realistic
[0:09:16] coloring book pages, right? Uh based off
[0:09:18] our family. And so, that started off as
[0:09:20] like a like I just want to generate like
[0:09:22] things I can print off and I can color
[0:09:24] and that's still part of it. But, uh,
[0:09:27] lately it's been more of like, oh, I
[0:09:29] want the digital like coloring canvas,
[0:09:31] right? So, like I have an iOS app now. I
[0:09:33] have an Android app even I said to you
[0:09:34] guys last night. Um, and like the iOS
[0:09:37] app, we're about to go on vacation. Like
[0:09:39] that thing's got to get installed on the
[0:09:40] on the iPad, right? That's going to be
[0:09:42] at least three hours of entertainment on
[0:09:44] this flight. So, um, so this is a app
[0:09:46] that's very personal to me. And if
[0:09:49] you've been building web apps in VS
[0:09:51] Code, like of course, you know, you run
[0:09:52] the app, you have your browser. If
[0:09:54] you're running dual monitor setup, you
[0:09:55] have both side by side. That still of
[0:09:57] course works. Um, we always had this
[0:09:59] thing in VS Code called simple browser,
[0:10:01] but of course it was quite literally as
[0:10:04] the name implies simple browser very
[0:10:06] simple. Um, so what we've done is we
[0:10:10] said okay like we're seeing a lot more
[0:10:12] front-end apps like we all have like 15
[0:10:14] front-end apps reviving right now,
[0:10:15] right? Um, thanks to AI. uh how can we
[0:10:19] make simple browser better in the
[0:10:20] context of like everything that I would
[0:10:22] want today if we were to do simple
[0:10:24] browser all over again. Uh and so now we
[0:10:26] have this uh new browser open integrated
[0:10:29] browser command. Um and I'll just go
[0:10:32] ahead and let's make sure I think it's
[0:10:34] running on localhost 3000. Yep. Um so
[0:10:37] there's a lot of cool cool things you
[0:10:38] can see here. Okay, so what right off
[0:10:40] the bat, right, like you used to just be
[0:10:42] like the Earl and [clears throat] that's
[0:10:43] what you got. Um but there's some other
[0:10:46] stuff in here. So like let's explore
[0:10:47] what we see when we when we do this. So
[0:10:50] I have a share with agent button here.
[0:10:53] So um like say I want the agent to see
[0:10:56] what I see in the browser.
[0:10:58] >> That's now possible, right? I can click
[0:11:00] this and it's kind of similar to how you
[0:11:01] can, you know, drag a file or reference
[0:11:03] a file with a hashtag um in chat, right?
[0:11:06] Like you're just basically saying, "Hey,
[0:11:07] agent, look at this thing." Um so the
[0:11:09] agent can see what I see if I click this
[0:11:11] button. Um we also let you go in and
[0:11:14] select uh specific elements. So, I can
[0:11:16] come in here and I can say like, uh,
[0:11:20] just trying to think of something. Uh, I
[0:11:23] don't like how this bubble and top right
[0:11:26] is rendered off the dialogue. Um, and so
[0:11:31] like it takes a screenshot of the
[0:11:33] element that you've attached. Um, so you
[0:11:35] can see it can hover over it and it also
[0:11:36] includes like the relevant like HTML.
[0:11:38] Um, so you can see if you hover over
[0:11:40] that you get like a nice little tool tip
[0:11:42] on what exactly was changed. You know,
[0:11:44] sometimes that's nice. I I think a lot
[0:11:46] of times you can just take a screenshot,
[0:11:48] right, and be like, "Fix this." But it's
[0:11:49] cool to be able to dig into the specific
[0:11:51] element if you have a lot of things that
[0:11:52] visually look very similar. Um,
[0:11:56] add console.
[0:11:56] >> Wait, hold on. What What is happening in
[0:11:58] the bottom right? What is cooking? What
[0:12:00] is happening in the bottom right?
[0:12:03] >> No, it says, "Let's cook, fam." What's
[0:12:05] the
[0:12:06] >> Oh, okay. I'm gonna get to this in a
[0:12:07] second. I'm gonna get to this in a
[0:12:08] second.
[0:12:09] >> I was like, who did we unleash on the on
[0:12:11] the translation team?
[0:12:13] the team merged my PR that has done
[0:12:15] something to what's happening.
[0:12:16] [laughter] He scared me. I was like, "Oh
[0:12:18] no, like is my messages showing
[0:12:20] >> fine tuning on Gen Z and here we are."
[0:12:22] >> I have a really funny story about those
[0:12:24] things at one second that I will tell.
[0:12:26] Um,
[0:12:27] >> okay. So, yeah, you can you can kind of
[0:12:29] attach elements. Uh, you can come in
[0:12:31] here and you can uh attach logs. So, it
[0:12:34] has the runtime context, right? Um,
[0:12:37] actually that happens automatically when
[0:12:38] you share with the agent. I'll show that
[0:12:40] in a second. Um, and then I can even
[0:12:42] like literally open DevTools right here
[0:12:44] in the browser or sorry, right inside of
[0:12:46] VS Code, which I guess is also a
[0:12:47] browser. [laughter] It's electron. Um,
[0:12:50] so yeah, this is pretty cool. I think
[0:12:52] like I personally like uh enjoy this
[0:12:55] flow when I'm like synchronously
[0:12:56] partnering with agents, like if I'm
[0:12:58] kicking off like 10 things at once,
[0:13:00] right? Um, then obviously like it's less
[0:13:03] useful, right? But when I'm
[0:13:04] synchronously partnering with the agent,
[0:13:05] maybe reviewing something that I kicked
[0:13:07] off on GitHub mobile, this is a pretty
[0:13:09] fun flow. So, I want to show something
[0:13:10] else. So,
[0:13:11] >> can it can it like click around? Can
[0:13:13] like it it navigate?
[0:13:14] >> So, we're going to try this out. We're
[0:13:15] going to try this out. Let's see if it
[0:13:17] works. So, I did add Look at all these
[0:13:20] fun pages.
[0:13:21] >> A look at that. You can see which ones I
[0:13:23] definitely weren't clip art that I threw
[0:13:25] in here as example images. Um Oh, look
[0:13:28] at this one. Little little uh Easter egg
[0:13:31] from from last week at agent sessions
[0:13:32] day. There's me and Burke. Burke. I feel
[0:13:35] like I kind of did you a little dirty on
[0:13:36] that.
[0:13:36] >> It looked like Yeah. Look at look at the
[0:13:38] look like a
[0:13:40] >> what I Yeah. Come on, man.
[0:13:42] >> Well, I guess I do look like
[0:13:45] that coffee should be spilled if if this
[0:13:46] is a photo realalistic.
[0:13:47] >> You look like my kid.
[0:13:49] >> Well, I am I am a kid. But
[0:13:51] unfortunately, I'm getting way older
[0:13:53] than I remember being. Um,
[0:13:56] >> you look 12 and I look 65. [laughter]
[0:13:59] >> Okay, maybe the prompt needs some
[0:14:01] dialing, admittedly, but you know, it's
[0:14:04] a coloring book app. Um, okay. So, um,
[0:14:08] there's a bug. Look at this. That's not
[0:14:10] great. [laughter]
[0:14:12] >> Look at all the confetti on the table.
[0:14:14] >> There was a lot of confetti. That's Go
[0:14:16] back and watch the end of Agent Sessions
[0:14:18] day. That scared me and Burke so much
[0:14:20] >> when that confetti went off. The
[0:14:22] producers came in and they were like
[0:14:23] right there and like we knew they were
[0:14:25] going to do it, but then they like
[0:14:26] didn't do it right away. And so I kind
[0:14:28] of like just the way my brain is, I just
[0:14:29] forgot. I was just talking to Berg and
[0:14:31] then like it just set off and I was
[0:14:34] You're in like this room like in a
[0:14:35] studio, right? So the sound is all kept
[0:14:37] like it's like soundproof and so like
[0:14:39] the confetti going off was even louder
[0:14:41] than one of those poppers is normally it
[0:14:44] was like very
[0:14:44] >> disorienting. So loud. Yeah. And you
[0:14:46] like rock your brain.
[0:14:48] >> Okay. I want to get the agent to fix
[0:14:49] this. So see I click this button. Okay.
[0:14:51] We want to make sure we're we're good
[0:14:53] with sharing. We are. It's just sharing
[0:14:55] with agent.
[0:14:56] >> And I'm going to say um I'll just like
[0:14:59] I'll even just navigate back to like the
[0:15:02] the homepage to show them the app. When
[0:15:04] I click on one of the coloring pages,
[0:15:09] digital canvas, it's way too zoomed in
[0:15:13] and I literally can't see it or color it
[0:15:18] at all. Um, what do I want to cook with?
[0:15:22] Um, so you can see I got some bring your
[0:15:23] own key going on here. Little GLM GBD
[0:15:25] OSS. Uh, let's cook with Sonet 46.
[0:15:31] >> New model picker.
[0:15:33] I'm a little nervous to to to expand my
[0:15:35] other models section.
[0:15:37] >> Don't do it.
[0:15:38] >> But uh basically what we noticed is like
[0:15:41] uh I put out a tweet like a couple weeks
[0:15:44] ago of like, hey, we want to redo model
[0:15:46] picker um because we got so much
[0:15:48] feedback and I think one of them was
[0:15:49] like when we built this thing, there was
[0:15:51] like a model ship happening like every
[0:15:54] >> day.
[0:15:55] >> I don't know. No, it was like every
[0:15:57] every month or two, right?
[0:15:59] originally I lo into my messages like
[0:16:01] hey we're shipping a model tomorrow hey
[0:16:02] we're shipping a model next week it's
[0:16:03] like three week right and so then the
[0:16:06] list just is ridiculous and the model
[0:16:07] picker wasn't made for that and so we
[0:16:09] had to go in we added search we have
[0:16:10] like this opinionated set of models that
[0:16:12] we think works really well for people to
[0:16:14] show at the top which there's a kind of
[0:16:16] a list that we create based off what we
[0:16:20] see working in evals and also like our
[0:16:21] own experience and then uh you can
[0:16:24] always still get to all the other models
[0:16:25] and if you use a model that isn't one of
[0:16:27] the like chosen defaults or whatever
[0:16:28] that we have in this section, then it
[0:16:30] will show up there. So you don't have to
[0:16:31] keep going back to other models, which
[0:16:33] would be annoying.
[0:16:34] >> But there's some other nice things
[0:16:35] coming in. So
[0:16:36] >> in the list, Pierce, they want to know.
[0:16:38] >> I know. Um, so there's some other nice
[0:16:42] things. So like you can hover, you can
[0:16:43] see context size. So you can see codeex
[0:16:44] is 400k, which is amazing. Um, we're
[0:16:47] trying to work on getting expanded
[0:16:49] context to all models. That's a top
[0:16:50] priority for us. Um, but soon you'll be
[0:16:53] able to do things like set reasoning
[0:16:54] effort and things like that for model
[0:16:55] pickers. So that's also something that's
[0:16:56] new this month. Um, so this didn't do
[0:16:59] what I wanted at all. Um, as as it as
[0:17:02] one does. Okay. So, I'm going to say I'm
[0:17:05] just going to give it a really strong
[0:17:06] hint browser. Um, better, but still not
[0:17:10] great. Uh, and then I can give it like
[0:17:13] even more forceful instructions like
[0:17:16] validate that it really works.
[0:17:19] Um, so yeah, this thing can drive the
[0:17:21] nav. It can take screenshots. It's
[0:17:23] basically got integrated playright is
[0:17:25] the way I would describe it. So,
[0:17:27] anything that Playright can do, this
[0:17:28] thing can do. Um, so I actually have a
[0:17:31] PR up. Oh, nice. It's going to navigate.
[0:17:33] Um, I actually have a PR up which will
[0:17:36] basically um it's called artifacts. And
[0:17:39] so like if you're taking like
[0:17:40] screenshots like and you're working with
[0:17:42] multiple agents, you kind of want at the
[0:17:44] end to not like read the whole chat log.
[0:17:46] At least I don't generally um not for
[0:17:48] this sort of project. And so like there
[0:17:50] will be a tab and it's just like what
[0:17:51] are all the artifacts? And then I can
[0:17:52] just go in and click in and view all the
[0:17:54] screenshots and stuff that it took and
[0:17:55] be like this is what I want or this
[0:17:56] isn't what I want. Right? Because that's
[0:17:58] what I'm going to do with an agent,
[0:17:59] right? That's what you're doing with
[0:18:00] your branch on your app you're building.
[0:18:02] Okay, pull down the branch npm rundev,
[0:18:04] you know, test it. Okay, it does what I
[0:18:06] want or it doesn't. But like if it could
[0:18:07] just do that itself, that's saving you a
[0:18:09] ton of time on every single agent,
[0:18:10] right?
[0:18:12] So you can see it's it can run playright
[0:18:14] code. So it's like I don't even know how
[0:18:15] to find the coloring button probably
[0:18:16] because I don't have good ARA labels on
[0:18:18] this thing. Um, so now it's like gonna
[0:18:21] search around. It's going to try to run
[0:18:23] playright code. Um, if I actually had
[0:18:26] like good instructions, I think it would
[0:18:28] be even better. And I think if you have
[0:18:29] accessibility labels and things like
[0:18:30] that that show up in the visual tree,
[0:18:32] it's going to be way better at driving
[0:18:34] the app. Right now, it doesn't even know
[0:18:35] what button to click because I'm pretty
[0:18:37] sure I don't have label a label
[0:18:38] [clears throat] in this coloring thing
[0:18:39] right here. Um, any questions about the
[0:18:43] browser while this thing cooks?
[0:18:47] >> Let me see. Let me take a look here in
[0:18:48] the chat in general. See if anything
[0:18:50] popped up for us here.
[0:18:53] Let's see.
[0:18:55] >> And then I need to talk about why it
[0:18:56] says let's cook, fam. [laughter]
[0:19:00] >> Uh,
[0:19:01] >> somebody was asking about People want to
[0:19:03] know about models. They're picking up
[0:19:05] what you're laying down, Pierce. They're
[0:19:06] asking about some they heard about a one
[0:19:08] million context window model on Reddit.
[0:19:12] >> Uh, yeah. I mean, I think what I would
[0:19:14] say is we're always exploring. This is
[0:19:16] kind of a corporate answer, but I mean,
[0:19:18] of course, we're always looking at
[0:19:20] different models. We're trying them
[0:19:21] internally to see, do they work? Do they
[0:19:24] not work? Are there any tweaks we need
[0:19:26] to make? And then based off the
[0:19:27] performance of those things, um, some of
[0:19:30] those things end up getting shipped to
[0:19:31] all of you. Um, so yeah, uh, we're
[0:19:34] always exploring different things.
[0:19:36] There's always new models we're trying
[0:19:38] even beyond the models that you see from
[0:19:40] the model families inside of model
[0:19:42] picker today. So that's a continuous
[0:19:44] thing because like people are always
[0:19:45] asking like oh what about this what
[0:19:46] about that and like I can assure you
[0:19:48] we're trying all those things um and
[0:19:50] seeing what works and then what whatever
[0:19:52] works you get right um
[0:19:54] >> so someone was asking about like they
[0:19:57] can't use MCP at their or basically so
[0:20:00] this is just like using playright
[0:20:01] internally so they seem to like it.
[0:20:03] >> Yep. Yeah. Uh so if you can't use the
[0:20:05] Playright MCP that's a good that's a
[0:20:07] good option. Uh another possibility is
[0:20:09] that um you use the new Playright CLI.
[0:20:12] Yeah.
[0:20:12] >> So, a lot of places will let you install
[0:20:14] the Playright CLI even if you can't get
[0:20:15] the MCP. Similar thing with with GitHub,
[0:20:17] right? Uh, if you can't install the
[0:20:19] GitHub MCP, which would be a little
[0:20:21] weird if you can use GitHub, but that's
[0:20:23] a different conversation. Um, but let's
[0:20:25] say you can, okay, there's a CLI. And
[0:20:27] often, like I mean, I'm I'm waiting into
[0:20:29] dangerous territory here with the MCP
[0:20:31] folks, but like I think sometimes like
[0:20:34] we like way over complicate our setup
[0:20:36] and like we can just use CLIs and
[0:20:37] they'll be fine, right? Not saying MCP
[0:20:40] is bad. I love MCP, but like hey,
[0:20:42] whatever gets the job done. I'm a
[0:20:43] pragmatist. It doesn't really matter to
[0:20:45] me. And often it can result in less
[0:20:46] context bloat in your context window as
[0:20:48] well.
[0:20:49] >> Okay,
[0:20:50] >> somebody clip that. We'll cut out the
[0:20:51] not saying. So it's just [laughter]
[0:20:54] >> disclaimer.
[0:20:55] >> Listen, I I've said this before on X and
[0:20:57] I'll say it here on the stream. I'm not
[0:20:58] afraid. I think that a CLI most of the
[0:21:01] time is all you need. Like agents are
[0:21:04] really good at discovering CLIs. Every
[0:21:06] CLI exposes a d-help.
[0:21:08] >> Yep. the Playright CLI. Um
[0:21:12] the the I use the Firebase CL CLI a lot.
[0:21:15] I'm probably not supposed to say that.
[0:21:16] James, cut that. Cut that from the V.
[0:21:17] [laughter]
[0:21:19] >> VSO channel. I
[0:21:20] >> if you can if you can just use a CLI and
[0:21:22] like with a markdown file and a skill a
[0:21:24] lot of times that's all you need.
[0:21:26] >> Yep.
[0:21:27] >> I think it's different context. I think
[0:21:28] the nice thing obviously about a CLI,
[0:21:31] right, is that like we're saying it's
[0:21:33] easy to run these different things. And
[0:21:35] actually the playright channel is a good
[0:21:36] like playright CLI and MCP comparison
[0:21:39] and the context window and like the
[0:21:40] different bloat the things cause or when
[0:21:42] to use what when basically but also like
[0:21:45] in some instances for a CLI you have to
[0:21:47] install the CLI right and then you'd
[0:21:49] have to have it on all the machines and
[0:21:51] like if you're using it on the coding
[0:21:52] agent right or like that but also think
[0:21:54] of MCP as also the availility now we
[0:21:57] have apps right so I added into my uh I
[0:22:01] have a oh my posh MCP and oh my posh MCP
[0:22:04] now is a visualizer. So I can say hey
[0:22:06] look at my MC look at my oh my posh
[0:22:08] config and like show me examples of like
[0:22:10] what it would look like and it'll like
[0:22:12] visualize all of it for you directly in
[0:22:13] the chat which is really cool. So kind
[0:22:15] of evolving that story but then also
[0:22:17] like obviously out the whole idea of MCP
[0:22:19] is also outside of the code editor too
[0:22:21] in broader context too. So all the
[0:22:24] different use cases that are out there
[0:22:25] for it. But I think there's not like a
[0:22:28] there's no wrong decision, right? So
[0:22:31] like if you like using like and having
[0:22:34] very a subset of tool control. I think
[0:22:36] that's one nice thing with MCP is you
[0:22:38] can control the tools that are visible
[0:22:40] right as well.
[0:22:42] >> Um compared to the CLI which like
[0:22:43] everything in the CLI will be available.
[0:22:45] So there's kind of like a mixed stream
[0:22:46] there. I use them interchangeably like
[0:22:48] it just depends on what I'm doing every
[0:22:49] single day. So,
[0:22:51] >> well, so I was trying to pull up I'm
[0:22:53] trying to remember the exact command. I
[0:22:55] need to I was it was kind of a joke
[0:22:56] about going and looking at my tweet, but
[0:22:58] also kind of not on what I wanted to
[0:23:01] what I wanted to see. There's the new
[0:23:03] chat debug log. What is the command for
[0:23:06] this thing? Um,
[0:23:08] so
[0:23:10] someone
[0:23:10] >> is this herald's visualizer? Did we add
[0:23:12] that in?
[0:23:13] >> Yeah. Uh, kind of. It's basically the
[0:23:15] same thing. Uh, hold on, hold on, hold
[0:23:19] on.
[0:23:21] because you used to be able to get to it
[0:23:22] from here and now you can't. Um, okay.
[0:23:25] While I while I try to find what I'm
[0:23:27] looking for there, I think like another
[0:23:29] We're just talking about customization.
[0:23:30] Something new that I wanted to show. Oh,
[0:23:33] there we go. Okay, we're we've solved
[0:23:35] one problem. Now, we can see the color
[0:23:37] canvas, but but not what I wanted. Um,
[0:23:40] >> so if you come into the extensions view,
[0:23:42] you know, you could already do the whole
[0:23:43] like I want to look at MCP servers
[0:23:45] thing, right? This is using the GitHub
[0:23:47] MCP registry, which is super cool. Um,
[0:23:49] but you can also now come in here
[0:23:51] >> and you can go agent plugins.
[0:23:54] And so if there's plugins you think are
[0:23:56] cool, these are coming from the Copilot
[0:23:59] plugins registry as well as the awesome
[0:24:01] co-pilot plugins registry.
[0:24:03] >> Um, and I think we have
[0:24:05] >> What is a plugin, Pierce?
[0:24:08] >> A collection of things. Um,
[0:24:10] >> okay.
[0:24:11] >> So, uh,
[0:24:12] >> some of us, some of us have dis some of
[0:24:14] us have disappeared for a week and we
[0:24:15] don't even know what a plugin is.
[0:24:17] >> Um, yeah, hold on. Uh, marketplace. I'm
[0:24:21] trying to remember the setting. Um, yes.
[0:24:23] Okay. So, you can come in here, chat,
[0:24:24] plugins, marketplaces. So, there is like
[0:24:26] a third party marketplace you wanted to
[0:24:28] add. Uh, that is a GitHub repo. You can
[0:24:30] just add it right here. Um, so say you
[0:24:32] have like
[0:24:33] >> Go ahead.
[0:24:34] >> Two questions here, Pierce. Can you
[0:24:35] install plugins like you can with the
[0:24:37] CLI where it's like copilot install and
[0:24:39] you just point it at a GitHub repo or
[0:24:41] does it have to be configured like this?
[0:24:44] >> Uh
[0:24:47] I mean you can install
[0:24:49] that's a good question. I'm not sure. Um
[0:24:52] so you're saying like in CLI you just
[0:24:54] basically like um do like what what's
[0:24:57] the command signature? It's like it's
[0:24:59] like copilot agent install and then it
[0:25:01] would be just the name of the repo the
[0:25:03] name of the user slashthereo. So like
[0:25:06] for the anvil plugin it's burllinanvil
[0:25:09] and then it just installs you know the
[0:25:12] agent the skill the mcp server
[0:25:14] everything. Um which having the registry
[0:25:18] is nice for orgs but it's nice if like I
[0:25:20] want to share it with someone I can just
[0:25:22] oneoff like you can just pull this in.
[0:25:24] Don't worry.
[0:25:25] >> Yeah, I don't think we have like a super
[0:25:26] easy way to like just like throw it into
[0:25:28] my customizations over here like you're
[0:25:30] saying. Um, let me try something else
[0:25:32] though. So, we have that, but we also
[0:25:34] have this new chat open customizations
[0:25:37] dialogue. So, I'll run this. So, um, I
[0:25:42] don't see something for plugins yet. Um,
[0:25:45] but this is basically uh a surface for
[0:25:48] managing all of your customizations that
[0:25:51] you have in both your user DUR and also
[0:25:54] your workspace ones, right? Cool.
[0:25:55] >> Um, I think we've all been in the place
[0:25:57] of like I don't even know what I've what
[0:25:59] I've added where this customization's
[0:26:01] coming from, right? So, if you open this
[0:26:03] up like you can come in here, you can
[0:26:04] see all my custom agents. You can see I
[0:26:07] really like this. You can see what's
[0:26:08] extension contributed. So, if you're
[0:26:10] like why is this custom agent showing
[0:26:12] up? Like sometimes extensions can
[0:26:14] contribute custom agents. Um I kind of
[0:26:16] want the ability to honestly go in and
[0:26:18] be able to say like I don't want any
[0:26:20] extension contributed custom agents.
[0:26:22] Sometimes that's right depending on the
[0:26:24] extension. I can come in here. These are
[0:26:25] all the skills I have. Again you can see
[0:26:27] the extension contributed skills. Um
[0:26:30] instructions.
[0:26:31] Uh prompts. These are my prompt files.
[0:26:34] Hooks. Uh so if I click in here
[0:26:37] >> I like that you can create you can
[0:26:38] create and you can generate and you can
[0:26:40] add. So oh there add server. There's ad
[0:26:42] servers. I bet you'll get a plugin one,
[0:26:44] Burke, to what I'm saying here.
[0:26:45] >> I I think we'd have like a plug-in thing
[0:26:47] here and then you could you could
[0:26:49] browse. It'd be cool to be able to for
[0:26:50] the skills thing to be able to do like
[0:26:52] the versel thing. I like the skills sh
[0:26:54] thing.
[0:26:54] >> Well, that's the other thing is like in
[0:26:56] my in so in Anvil, I actually tell
[0:26:57] people to install the front-end design
[0:26:59] skill from skills.sh because I don't
[0:27:01] want to rebundle their skill. Yeah.
[0:27:05] >> Um [clears throat] Okay. So the command
[0:27:08] that I was looking for is uh open agent
[0:27:13] debug panel.
[0:27:15] >> Okay, so um we have this like we've long
[0:27:18] had and the reason this is all tying
[0:27:20] together. I promise I'm going to tie
[0:27:21] this all up. Um I'm not just showing a
[0:27:23] ton of random stuff. So we started with
[0:27:24] the coloring book app, right? The
[0:27:26] browser's doing things. Um then we
[0:27:29] started talking about customization. So
[0:27:31] I showed you like how you can manage all
[0:27:32] of them with this dialogue, the new
[0:27:34] agent plugins thing. But I think like I
[0:27:36] would say one question I get, I don't
[0:27:38] know if you guys get this a lot, like
[0:27:40] every single developer I meet with,
[0:27:42] every single customer I talk to is like
[0:27:45] this is a lot, right? There's prompts,
[0:27:47] there's custom agents, there's skills,
[0:27:50] there's MCP servers, and it is
[0:27:52] overwhelming. And you're like, how does
[0:27:54] all of this even work? How how do I know
[0:27:57] like what's going on here? And the
[0:27:59] reality is like most of these
[0:28:00] customizations are very simple in their
[0:28:03] mechanism, right? they're appending the
[0:28:06] API request that is sent to the server
[0:28:09] which is an LLM uh with additional like
[0:28:12] text often markdown and they're doing
[0:28:15] that at different points in the life
[0:28:16] cycle and that is what's happening for
[0:28:17] many of these um and then in the case of
[0:28:20] other customization techniques they're
[0:28:22] appending the tools that are available
[0:28:24] to the agent with other tools so like
[0:28:25] MCP for example right so I love going
[0:28:29] and actually showing like how this thing
[0:28:31] works and it is actually helpful as a
[0:28:33] developer to understand how the agent
[0:28:35] loop works because then once you
[0:28:36] understand this a lot of these concepts
[0:28:38] just get way less scary, right? Um, so
[0:28:41] we always had this like chat debug log
[0:28:43] thing over here and you could come in
[0:28:45] here and one of the really cool things I
[0:28:47] like is okay, GitHub copilot and VS Code
[0:28:49] is open source, right? So it can always
[0:28:51] go in and see exactly what's happening,
[0:28:52] what prompts are sent, things like that.
[0:28:54] So this has always been here. It will
[0:28:57] continue to be here, I think. Um, but we
[0:28:59] have this new view because this is very
[0:29:00] visually overwhelming and this honestly
[0:29:02] is just us exposing the tools that we
[0:29:04] were using internally at the time to
[0:29:06] refine the prompts and such inside of
[0:29:07] Copilot. Um, but this new panel is much
[0:29:10] better. So I can click in here. Um, so
[0:29:13] right off the bat I get kind of a a
[0:29:15] session detail. Like I often hear people
[0:29:18] like I still think Copilot's like the
[0:29:19] best deal in all of AI. I really believe
[0:29:22] this. Like you can see that was four
[0:29:24] million tokens I just burned right on
[0:29:26] Sonic. Um,
[0:29:28] So, and that was what this is one
[0:29:30] premium request. It's still cooking. Um,
[0:29:33] so yeah, like it's pretty cool to see
[0:29:34] some of the internals. You can see
[0:29:36] there's a couple errors that had to
[0:29:37] recover from. 82 tool cost, 78 model
[0:29:40] turns. Uh, so there's a lot that's
[0:29:41] happening here. Uh, so I can come in
[0:29:43] here and I can I can view logs. And so I
[0:29:45] can come in here and I can see all the
[0:29:46] stuff that's happening throughout the
[0:29:47] life cycle. So
[0:29:49] >> um, so you can see right off the bat,
[0:29:50] okay, we load instructions, we load
[0:29:51] skills, we load agents, we load hooks,
[0:29:53] and you can see the per performance
[0:29:55] delta you pay, right? Like so in my
[0:29:57] case, loading the instructions did did
[0:29:58] have a little bit of perf hit on this
[0:30:00] turn, right? Um now maybe that saves me
[0:30:02] time later because the agent doesn't
[0:30:04] have to do other things because it
[0:30:05] understands more context, right? But
[0:30:08] that's a trade-off. Um so then you can
[0:30:09] see I start making like uh some tool
[0:30:11] calls. Almost always it starts with like
[0:30:14] some reads. So you can see I can click
[0:30:15] into this. I can see this is what the
[0:30:17] the arguments that uh we sent to the
[0:30:20] read file tool. So we had a path start
[0:30:22] line end line we want to read. You can
[0:30:24] see the output here. Um, and so let's go
[0:30:26] in. We can see like some cooler stuff.
[0:30:28] So in this case, it's a base 64 thing.
[0:30:31] I'm going to file a bug for that. Let me
[0:30:32] find one that's not screenshot page. Uh,
[0:30:35] let's find like a yeah, replace string.
[0:30:38] So replace string is like just taking
[0:30:40] the code from from the model and putting
[0:30:43] it back into your code, right? Um, so
[0:30:45] you have a file path, you have the old
[0:30:46] string, you have the new string, and
[0:30:47] then you have what happened here. So you
[0:30:49] can literally go in and see exactly
[0:30:50] what's happening like with your agent.
[0:30:52] Um, which is pretty cool. And then the
[0:30:54] other thing I like is you can see this
[0:30:56] flowchart right here.
[0:30:57] >> Cool.
[0:30:58] >> So you can actually come in and see like
[0:30:59] this is the flow of what's going on with
[0:31:01] the agent. Um which I personally find
[0:31:04] very helpful. Um I think like we need to
[0:31:06] figure out how to make it not like this
[0:31:08] massive thing I have to scroll. That's
[0:31:10] fair feedback. But um like we tried to
[0:31:13] do some nesting so you can see like okay
[0:31:14] at the start we load stuff. Okay what do
[0:31:16] we load? Um and then you can click into
[0:31:18] these things. You get that same detail
[0:31:20] view and stuff like that. So this is a
[0:31:21] cool way to be like I just added a
[0:31:23] plugin. I just added a skill. I just
[0:31:25] added an instruction. Okay. What what is
[0:31:27] actually happening here, right? Um
[0:31:31] so I want to show another thing that is
[0:31:34] related to this that is not technically
[0:31:36] inside of VS Code but is something that
[0:31:38] I built a month ago
[0:31:41] and Harold has been moving forward
[0:31:44] which was called primer. Now it's called
[0:31:47] agent RC. Wow.
[0:31:48] >> And so basically what this thing is is
[0:31:51] like taking it a step further like okay
[0:31:52] now I have these customizations. The
[0:31:55] thing I then hear as the next thing is
[0:31:56] like okay I understand how they work.
[0:31:58] How do you even know they work? Like how
[0:31:59] do I know instruction A is better than
[0:32:01] instruction B? Right? We're all just
[0:32:04] kind of vibing and saying oh it feels
[0:32:05] better if I have this instruction or I
[0:32:07] have this skill. But how do you really
[0:32:08] know? And so this thing's really cool
[0:32:10] because you can actually go in and you
[0:32:12] can inspect your repo. You can see like
[0:32:13] is it AI ready? That stuff is cool.
[0:32:15] generate instructions, configs, etc.
[0:32:18] Where's my eval one that I want to show
[0:32:20] um
[0:32:23] agent RC eval. So, this is really cool.
[0:32:26] So, I use copilot SDK here and on your
[0:32:30] repo, I will generate basically a set of
[0:32:32] test cases of like I'll do deep research
[0:32:35] over your thing and I don't care how
[0:32:36] many turns it takes to generate the
[0:32:38] answers, but we'll like generate a
[0:32:40] certain amount of emails and if there's
[0:32:41] ones you want to manually author, you
[0:32:42] can do that, too. And then you can
[0:32:44] basically run this CLI and it'll tell
[0:32:46] you before and after this is the
[0:32:48] difference in your instructions and the
[0:32:50] outcomes you got. And the cool thing
[0:32:52] about this is you can like actually more
[0:32:55] objectively say like this instruction is
[0:32:57] better or worse. Um so like it may not
[0:33:00] necessarily be like resolved rate or
[0:33:02] like I think it actually did a better
[0:33:04] job at answering my question. Maybe that
[0:33:05] for the repo you're working in it's
[0:33:07] actually pretty simple and it doesn't
[0:33:08] like it's going to resolve the same
[0:33:10] rate. But maybe you save yourself, you
[0:33:13] know, five tool calls and 25 seconds on
[0:33:15] every turn. That could be an outcome
[0:33:17] that you're trying to drive. We also log
[0:33:18] back. So this is like a first attempt at
[0:33:21] like how do you even measure the impact
[0:33:23] of these customizations, right? Um so if
[0:33:26] you have feedback on it, like definitely
[0:33:27] give it a try and let us know. But it's
[0:33:28] solving like a real pain point that we
[0:33:30] saw in a lot of our conversations with
[0:33:31] developers.
[0:33:33] >> That's cool. That's so cool. I mean it's
[0:33:34] cool to see that go from I was talking
[0:33:36] about primer internally and to kind of
[0:33:38] see it become a real thing. It's like I
[0:33:40] leave for a week and then it's a whole
[0:33:41] it's grown up. It's grown up so fast.
[0:33:43] >> Harold credit for that. I I I was a
[0:33:46] terrible open source maintainer and
[0:33:48] threw it up and then uh life got busy.
[0:33:51] So um Harold has really been the one
[0:33:53] who's made this thing into like a real
[0:33:55] production ready thing and we have a ton
[0:33:56] of internal teams and external teams
[0:33:57] using it.
[0:33:59] >> Okay, so that was all theory and
[0:34:00] customization stuff
[0:34:01] >> questions. Hold on. Okay, so okay, so we
[0:34:03] had a few things here which is good. Uh,
[0:34:06] so is there any way to like bring up
[0:34:08] some of that information without going
[0:34:09] directly into the debug views? Like is
[0:34:11] there a quick action or is it just like
[0:34:12] pinning that basically debug thing off
[0:34:15] to the side?
[0:34:17] >> Like what's the what's this what's your
[0:34:19] like golden
[0:34:20] >> the agent debug thing to see tokens and
[0:34:23] see stuff in general is like an easy way
[0:34:25] to get there.
[0:34:27] >> Uh, no, not without running that command
[0:34:28] right now. Um, like where would you want
[0:34:30] it? Like somewhere over here.
[0:34:32] >> Like I'm trying to trying to brainstorm
[0:34:33] with you. Some of that information would
[0:34:35] show up here like context window and
[0:34:36] such but like um
[0:34:38] >> I guess you can click on that and go
[0:34:40] into it right like ideally like maybe
[0:34:41] you hover over the cont from here as an
[0:34:44] actual
[0:34:44] >> Yeah. Yeah. You know what I do is I I
[0:34:46] just pin so if like you go in I just
[0:34:48] like pin that thing off to the side you
[0:34:50] know pin it to the left
[0:34:53] >> so like that's a good point. So that's
[0:34:55] not what I wanted. I can never remember
[0:34:57] the name of like all the commands. We
[0:34:59] need semantic search over the commands.
[0:35:00] Um,
[0:35:01] >> yeah.
[0:35:01] >> Let's see. So, we pin that. Hey,
[0:35:06] the amount of tokens that Microsoft has
[0:35:08] had to pay for with tests like this on
[0:35:12] models like open I feel so terrible for
[0:35:14] >> we were looking at the leaderboards this
[0:35:16] morning. Martin had sent me a message
[0:35:17] looking at the leaderboards and he did a
[0:35:19] little math for like the top person. It
[0:35:20] [laughter] is crazy what the cost.
[0:35:23] >> I mean, I have I have real data. I'm
[0:35:25] spending about $3,000 a month right now
[0:35:27] on imprints for just myself.
[0:35:29] >> Wow. I think we can get those numbers
[0:35:30] up, right? Like I want to see everybody
[0:35:32] burning like a hundred grand.
[0:35:33] >> Yeah. I I I think like at least
[0:35:35] internally like I encourage
[0:35:37] I mean I encourage people it like you
[0:35:40] don't want to tell people like I want
[0:35:41] you to have a higher spend necessarily
[0:35:43] but it's like I think directionally it
[0:35:45] is correct like if you have a higher
[0:35:46] spend then you're using more
[0:35:51] performative I think but like I think
[0:35:53] it's directionally the correct thing to
[0:35:54] measure.
[0:35:55] >> There will be coming a day though when
[0:35:57] that is not the case. Yeah.
[0:35:59] >> And like tokens matter, but we are not
[0:36:01] there yet. And I would tell people the
[0:36:03] same thing like while while the getting
[0:36:04] is good, get it. You know what I'm
[0:36:06] saying?
[0:36:07] >> All right.
[0:36:07] >> There's a Yeah, this one. I'm ready for
[0:36:09] this this uh so
[0:36:13] we are adding the other nice thing about
[0:36:15] AI is we can add things that we just
[0:36:17] think are fun. [laughter]
[0:36:19] It doesn't necessarily have to be oh
[0:36:21] like you know this is a P 0, this is a
[0:36:22] P1. You know, occasionally you want to
[0:36:24] have some fun, right? There's there's no
[0:36:25] reason to add something and you just
[0:36:27] want to add it. Um, that's something
[0:36:29] we're trying to have more fun. Like
[0:36:30] sometimes I think we're like too serious
[0:36:32] with [clears throat] the product and
[0:36:34] it's like is it really that big a deal
[0:36:35] to change the thinking phrase? So yeah,
[0:36:37] you can see mine here. So you can
[0:36:39] there's different modes. So you have
[0:36:40] this chat agent thinking phrases. Uh
[0:36:42] there's modes. So there's two different
[0:36:44] options. So replace is going to
[0:36:45] basically not use any of our thinking
[0:36:47] phrases we have. So if you're like I
[0:36:50] don't want to I don't care about what
[0:36:51] you have then uh use replace. Um, append
[0:36:56] is just going to add these to the
[0:36:57] existing list. And so you can see this
[0:36:59] is my list. Happy coding, of course, VS
[0:37:01] Code, Let's Cook, Brad the Hamster. That
[0:37:03] one's from Justin. Justin really likes
[0:37:05] that phrase. So, uh, I have that in
[0:37:07] there. Um, I met with the Outlook team
[0:37:09] the other day and they have a whole
[0:37:11] bunch of Outlook specific phrases that
[0:37:13] they have that they have as their
[0:37:15] thinking phrases in their product. But I
[0:37:16] do kind of like the idea like someone
[0:37:18] was like, you can really troll people
[0:37:19] with this because VS Code settings can
[0:37:22] be in your workspace, right? You can
[0:37:23] have likevscode
[0:37:25] settings JSON, right?
[0:37:27] >> And that will aend the user level
[0:37:28] settings with these workspace settings
[0:37:30] so that everyone on your team has the
[0:37:31] same settings. We have this on the VS
[0:37:32] code team so we all run the same
[0:37:34] settings, right? For the important
[0:37:35] things. Um,
[0:37:37] >> so the funny thing about that is like
[0:37:39] people don't know like you are surprised
[0:37:41] when you see this. You could put some
[0:37:42] insane things in your workspace.
[0:37:44] [laughter] Push it to your team.
[0:37:46] Someone's going to be using code and
[0:37:47] they're going to be like what is going
[0:37:48] on? I look forward to getting all kinds
[0:37:50] of chaotic bug reports based off the
[0:37:52] thinking phrases you use.
[0:37:53] >> This is great. Yeah. So, like for your
[0:37:55] whole org, you could just uh like you
[0:37:57] just do propaganda, right? Like work
[0:37:59] harder. You enjoy this.
[0:38:01] >> This is your favorite thing. You will be
[0:38:03] staying late tonight. [laughter]
[0:38:05] >> New new motivation technique just
[0:38:07] dropped. People parties out, thinking
[0:38:10] phrases in. Um
[0:38:11] >> yeah, it's like it's 5 PM. You can go
[0:38:12] home if you want to. You don't have to
[0:38:14] stay. [laughter]
[0:38:16] >> It's not mandatory. not mandatory.
[0:38:19] >> You don't have to. I'm just saying I'm
[0:38:21] not going anywhere, but if you want to,
[0:38:23] it's okay.
[0:38:24] >> That's a good one.
[0:38:25] >> Someone someone had one the other day
[0:38:27] that was like, I'm getting tired of like
[0:38:28] the agent like having like inner
[0:38:30] monologue of like, why do you keep
[0:38:31] sending me stupid prompts and stuff like
[0:38:33] that?
[0:38:34] >> This [snorts] again. I got to do this
[0:38:35] again. Great.
[0:38:36] >> Does it just does it just pick these uh
[0:38:38] randomly? Adobe was asking like does it
[0:38:41] just like this big Okay, gotcha. Yeah,
[0:38:43] this one is so like we have like this
[0:38:45] new like collapse thinking thing inside
[0:38:47] of VS Code. Um, so basically like um I
[0:38:50] think it shows well with codeex. Um
[0:38:54] >> these these these don't have anything to
[0:38:55] do with the context, right?
[0:38:58] >> So it's basically you know how you used
[0:38:59] to get like the working you still do at
[0:39:01] the beginning. It's kind of similar to
[0:39:02] that. Um
[0:39:03] >> gotcha.
[0:39:04] >> So like once we actually get going here
[0:39:07] >> TTFT on uh on codecs can sometimes be a
[0:39:11] little slow. Okay. So, it's working. And
[0:39:13] so, you can see like within the thinking
[0:39:15] blurb, we're getting one of my phrases
[0:39:16] right here.
[0:39:17] >> Um, so rather than just getting working
[0:39:19] again, right?
[0:39:20] >> Can I replace working with cooking?
[0:39:22] >> So, I want to do this. I really want to
[0:39:24] do this. This is good feedback. Um, I
[0:39:27] already sent it to Justin. So, it's it's
[0:39:29] on the road map. We're solving the real
[0:39:31] problems here in tech, right? This is
[0:39:32] actually the problems that we should be
[0:39:34] solving on the VS Code team, not all the
[0:39:35] other stuff. I
[0:39:36] >> Yeah, people would think orchestration
[0:39:38] and handoffs and planning over here and
[0:39:40] that tool. No, I just really I just want
[0:39:41] to have fun inside.
[0:39:42] >> Well, this stuff is important because
[0:39:44] it's like this is the human element that
[0:39:46] is still important. Yes.
[0:39:48] >> When everything is about AI, the human
[0:39:50] stuff becomes really super important.
[0:39:52] So, I'm actually glad to see this in the
[0:39:54] product. Very glad.
[0:39:56] >> Yeah. I'm have different ones for every
[0:39:57] repo. I'm just going to make sure like
[0:39:59] like you said like I think I don't think
[0:40:01] people know that you can just have that
[0:40:02] often like that. VS Code folder inside
[0:40:04] of your repo and then it'll just like
[0:40:05] put pick it up automatically. So, it's
[0:40:07] super nice, especially if you want
[0:40:09] people to automatically have certain
[0:40:11] extensions or servers or things like
[0:40:12] that, you know, you can just have all
[0:40:14] that stuff in there, which is super
[0:40:15] nice. So,
[0:40:15] >> well, and I think that people don't
[0:40:18] Yeah, like on every team there is like
[0:40:22] differing levels of maturity with the
[0:40:24] tools. That's certainly true on any
[0:40:26] team, with any tool. And um I think that
[0:40:31] that's like a really cool hack for being
[0:40:32] like like if there's settings and you're
[0:40:34] like everyone on the my team should be
[0:40:35] running these settings. Like the person
[0:40:37] who is actually opinionated about those
[0:40:39] things, there's going to be one person
[0:40:41] usually or two and then the rest of
[0:40:42] people probably care way less. Like if
[0:40:44] you just want to make sure your team is
[0:40:46] running the what you think are the right
[0:40:47] settings, that's a good way to do it. If
[0:40:49] you have like, you know, a repo you're
[0:40:50] mostly working out of, um
[0:40:53] >> I want to show one more thing.
[0:40:55] >> That's that's hilarious.
[0:40:57] Someone said they should have Instagram
[0:40:59] reels in there when it starts cooking.
[0:41:00] >> Well, so I I have a kind of funny idea,
[0:41:03] but also serious. Um, so the new
[0:41:06] integrated browser, I'm not
[0:41:07] >> subway server.
[0:41:10] >> I you could you could pull up Tik Tok,
[0:41:12] watch Tik Tok while the agent works.
[0:41:14] >> I showed this in our internal office
[0:41:15] hours. Tik Tok or Instagram reals and
[0:41:18] you're you're cooking on what? if you
[0:41:20] got Instagram [laughter] real or or Tik
[0:41:22] Tok depend
[0:41:24] >> like ticker like a news ticker down at
[0:41:25] the bottom with all the rage headlines
[0:41:27] going as well. What else can we throw in
[0:41:29] here to just
[0:41:30] >> I think we should chip an extension for
[0:41:31] this.
[0:41:32] >> I really do. It would be kind of
[0:41:34] hilarious. That's like this is the
[0:41:35] config for like having fun and letting
[0:41:37] the agent cook. Um that would be amazing
[0:41:40] actually.
[0:41:42] >> Yeah. Your Yeah. Your boss comes over
[0:41:43] like what are you doing? I'm I'm just
[0:41:45] coding. I'm just I'm just coding. No.
[0:41:47] Hands off. [laughter] I mean, if in the
[0:41:49] integrated browser, like what it could
[0:41:50] do is at with every turn it swipes to
[0:41:53] the next reel, you know what I mean?
[0:41:56] Like that would be like ridiculous and
[0:41:58] kind of amazing. So, oh, that's us.
[0:42:01] >> We're gonna watch ourselves cooking
[0:42:03] inception style.
[0:42:05] >> Oh no. [laughter]
[0:42:07] >> Oh gosh.
[0:42:08] >> Let's see. Does this work or Nope. An
[0:42:10] error occurred.
[0:42:13] >> Good. Good.
[0:42:15] >> On behalf of humanity. Wait, let's try a
[0:42:17] non-live video then. Um, let me go to
[0:42:20] our channel. Is it just that it's live?
[0:42:22] It doesn't like
[0:42:24] uh Oh, all of our agent sessions things
[0:42:26] are nice. Um, okay, Julia, how we ship
[0:42:29] models?
[0:42:29] >> Yes,
[0:42:31] please.
[0:42:32] >> Maybe it may be blocking some cookies.
[0:42:34] >> That's true. Actually, that is probably
[0:42:35] what's happening. Um,
[0:42:38] >> I am going to try this Tik Tok thing
[0:42:40] though after the call. I'm not going to
[0:42:41] lie. You could do this to where
[0:42:45] you like you're watching and then
[0:42:46] whenever one of your agents finishes it
[0:42:48] stops, right? And it's like go talk to
[0:42:51] your agent. No more reels for you until
[0:42:53] you get into
[0:42:55] >> So, you know how like uh in CLI you have
[0:42:57] like I think it's last usage and things
[0:42:59] like that. I like I love the idea of
[0:43:02] like agent watch hours or something like
[0:43:03] that. It's like the time you spend
[0:43:05] watching Tik Tok while the agent is
[0:43:07] working. We should have this as a metric
[0:43:09] we show. I wonder if it's possible to
[0:43:13] like take the agent output and like do
[0:43:16] something with it in a way that teaches
[0:43:19] you because a lot of times I'm watching
[0:43:21] the agent it's like okay we should be
[0:43:22] using a Unix socket here and I'm like
[0:43:24] what the heck is a Unix socket? How does
[0:43:26] that even work? And then I watch it do
[0:43:28] it and I'm learning
[0:43:29] >> but it's raw text. I wonder if you could
[0:43:31] take that and like I don't know in real
[0:43:33] time like make a tutorial. You know what
[0:43:36] I'm saying? Like run it through um
[0:43:39] What? I don't know. There's tools that
[0:43:41] do this.
[0:43:42] >> No, I think it'd be super cool. You
[0:43:44] could definitely do that. Um, like it
[0:43:46] would be I'm trying to think of how it
[0:43:48] would work. I mean, this is like just
[0:43:50] proof of concept. It would add a ton of
[0:43:52] latency to your request, but you could
[0:43:54] build a tool that's basically like
[0:43:56] analyze the conversation up to this
[0:43:58] point and then basically based off of
[0:44:00] that, search YouTube and find an
[0:44:03] appropriate link and then run a VS Code
[0:44:05] command to open the integrated browser
[0:44:07] to set link. I mean that is a very
[0:44:09] doable prototype.
[0:44:11] >> Yeah, you could you could create a
[0:44:13] >> you could create an MCP app, right, that
[0:44:15] takes the same thing like summarize it
[0:44:16] all and then the MCP app like goes off
[0:44:19] does a bunch of stuff, right? It could
[0:44:20] go look for YouTube. It could build a
[0:44:22] tutorial. It could do like Q&A like it
[0:44:24] could do like a a survey or something
[0:44:26] and then it could like prompt that back
[0:44:28] into the UI uh and then give that to
[0:44:30] you. That'd be kind of cool, right?
[0:44:32] Imagine it would be like a little trivia
[0:44:34] quiz basically and you could go do that.
[0:44:37] vibe that out
[0:44:38] >> because one of the things that I
[0:44:39] realized is that I thought that using
[0:44:41] agents was gonna make us all dumber for
[0:44:44] lack of a better word, right? Like I
[0:44:45] thought but it it isn't. What's
[0:44:47] happening is I'm learning
[0:44:49] >> all kinds of stuff that I never would
[0:44:50] have learned before because I'm too busy
[0:44:52] trying to figure out if I need an if
[0:44:53] statement or not. But I don't care about
[0:44:54] that anymore. So now I'm learning like
[0:44:56] all these terminal commands. I'm
[0:44:58] learning all types of things about Linux
[0:44:59] and Unix. So, if you don't if you're not
[0:45:02] watching the agent, you're actually
[0:45:05] losing a lot of the experience. You know
[0:45:07] what I mean?
[0:45:07] >> I I love reading it. My favorite part is
[0:45:09] reading it and understanding what it's
[0:45:11] thinking, how I'm thinking, how I'm
[0:45:12] thinking, how it's thinking, and like
[0:45:14] and steering it and navigating it back
[0:45:16] differently. What's that plus button on
[0:45:18] the bottom left?
[0:45:20] [clears throat]
[0:45:21] >> So, it's a little confusing. We're
[0:45:23] discussing it a lot on the team. So, I
[0:45:25] think it's very fair feedback that we
[0:45:27] have a very crowded input box, right?
[0:45:29] There's a lot going on here. This is the
[0:45:31] full screen width, right? Like but in
[0:45:33] the compressed view, this is like very
[0:45:36] >> I mean this is a lot, right?
[0:45:37] >> Yeah.
[0:45:38] >> Um so and we're there's other things we
[0:45:41] want to add which is the crazy thing. Um
[0:45:43] so we used to have add context up here,
[0:45:46] right?
[0:45:47] >> So basically we that took out some
[0:45:49] visual space, right? We wanted it to be
[0:45:51] like less boxy. So we took that out. Now
[0:45:54] it's a plus. But then it is the thing
[0:45:56] we've been discussing on the team is
[0:45:57] like it's kind of confusing now because
[0:45:59] we have two different meanings for these
[0:46:01] plus buttons within the same view.
[0:46:03] >> So that's kind of bad UX. So we're still
[0:46:06] talking about what we want to do there.
[0:46:07] The other problem is like okay now we
[0:46:09] have okay we have different agent types
[0:46:11] right we have our custom agents. Now
[0:46:14] I've run out of room because of my zoom
[0:46:17] width right for the model picker and
[0:46:19] tools. Then we have the context widget.
[0:46:21] I have speech enabled. I have the stop
[0:46:23] button. I have steering and queuing
[0:46:25] controls. So, David Dosset on our team
[0:46:29] is is going and actually doing a whole
[0:46:31] cleanup on this. And so, like if you
[0:46:33] have very specific feedback on like
[0:46:35] things that you would like to see, let
[0:46:36] us know because I agree like this is
[0:46:38] very visually overwhelming. So, that was
[0:46:40] one of the tweaks we've been trying. I
[0:46:42] don't know if we'll keep it, but um
[0:46:43] there was some feedback we got about it
[0:46:45] because it it did kind of break people's
[0:46:47] mental like that's the problem with
[0:46:49] these UX cleanups is like they're good I
[0:46:51] think in the whole but they also like
[0:46:53] move your cheese and you're like where
[0:46:54] did it go and it's very confusing people
[0:46:57] totally the CLI does this all the time
[0:46:58] where it's like it was control E and now
[0:47:01] it's control S and now it's this or that
[0:47:02] or the other and now we're automatically
[0:47:04] going to put a slash there for you or it
[0:47:06] wasn't there before and it's really it
[0:47:08] really is like a speed bump. I'm curious
[0:47:10] if you expand this window, Pierce,
[0:47:13] >> does this.
[0:47:14] >> So, okay, so this gets a lot better. You
[0:47:16] don't have to dig into menus now to get
[0:47:17] to the model picker, etc. So, right. So,
[0:47:19] like at this width,
[0:47:21] >> there's actually a lot of room for
[0:47:22] activities, right? You could you could
[0:47:24] slam a lot more stuff in here.
[0:47:26] >> Yeah.
[0:47:27] >> Yeah.
[0:47:28] >> I think to be fair, like I find myself
[0:47:31] running the full screen width a lot more
[0:47:33] because my primary partnership within
[0:47:36] the editor is now with the agent, right?
[0:47:38] So like I care I will dive into the
[0:47:41] actual files but like that's not a
[0:47:42] primary gesture for me. The primary
[0:47:44] gesture is staying here. So I'm actually
[0:47:46] much more okay running this full screen.
[0:47:48] But there's like some obvious cleanups,
[0:47:49] right? Like okay I'm not steering or
[0:47:50] queuing at all right now. So why is this
[0:47:52] button showing right? That should only
[0:47:54] show when I actually like have a message
[0:47:56] typed in this box.
[0:47:58] >> Yeah.
[0:47:58] >> So that's one one tweak. And then you're
[0:48:00] like um okay like uh the context widget.
[0:48:05] Some of these things I think we could
[0:48:06] still have, but maybe you put them below
[0:48:08] the the actual input box, right? Um, as
[0:48:11] additional information like one thing we
[0:48:13] were discussing is like should we have
[0:48:15] like uh an easy entry point for enabling
[0:48:18] like approve all tools from input box,
[0:48:22] right? A lot of AI assistants have this
[0:48:24] now, but like it would be very crowded
[0:48:26] to put that here. And it's also not
[0:48:27] exactly correct because it kind of
[0:48:28] implies that you're only doing that for
[0:48:32] the prompt you're about to send. But
[0:48:33] like the way we were imagining is like
[0:48:35] it would be this whole chat session you
[0:48:37] have going, right? Um and so it's not
[0:48:39] it's like kind of not correct to put it
[0:48:41] in the input box and kind of similar for
[0:48:43] the context widget like maybe that thing
[0:48:45] should just live outside the box.
[0:48:46] Anyways,
[0:48:47] >> yeah. Oh, one thing too. Can can you fix
[0:48:49] this? I'm on ultra wide often and I'll
[0:48:52] put VS Code huge and there's huge bars
[0:48:54] on the left and right. See how look at
[0:48:56] all that blank space on the left and
[0:48:57] right
[0:48:58] >> there? You could really
[0:48:59] >> There's a lot of wasted visual space. I
[0:49:01] agree. Um, and then also like
[0:49:04] >> change that padding. Change that
[0:49:05] padding.
[0:49:06] >> I generally like I'm presenting to all
[0:49:08] of you and it's confusing I think
[0:49:09] sometimes when I run different like
[0:49:10] activity bar configs, but like honestly
[0:49:13] like I run this like uh you can change
[0:49:16] like the configuration of this. So I can
[0:49:18] do like top. Okay. So I'm reclaiming
[0:49:21] some more space, right? The other thing
[0:49:23] that we're going to clean up is if you
[0:49:25] go over here,
[0:49:27] this is a lot, right? All these buttons
[0:49:29] all in this kind of area. So, we need to
[0:49:31] go clean that up. So, that's another
[0:49:33] thing we're thinking about. Um, the
[0:49:35] thing I wanted to show though on what
[0:49:36] just happened
[0:49:38] is that's also new is if I scroll up, I
[0:49:40] said, "Okay, what are five ideas?" Which
[0:49:42] sometimes is like I mean a throwaway
[0:49:43] prompt, but sometimes you get decent
[0:49:45] ideas. Um, we have this new explorer sub
[0:49:48] agent that is like it was it was already
[0:49:52] true in plan mode. We would spin a sub
[0:49:53] agent for searching. This is optimized
[0:49:56] and uses like a faster model and
[0:49:58] experience. So, this is like a new thing
[0:49:59] we have. You can see that I was in agent
[0:50:02] and it auto switched me into plan mode.
[0:50:04] That's this new switch agent tool. So
[0:50:07] basically if you have like an
[0:50:08] underspecified prompt like in this case
[0:50:10] I was like you should add color by
[0:50:12] number mode. It's like okay well that's
[0:50:14] not very good prompt. So let's that's
[0:50:16] underspecified. Let's jump into plan
[0:50:17] mode. Kick off some explore sub aents.
[0:50:19] You can see it kicked off too. Okay we
[0:50:21] have something. So there's a feature
[0:50:24] that I often want which is like okay
[0:50:27] dang I kind of wish like I had captured
[0:50:29] this date up here and done something
[0:50:32] with it right like maybe okay now I want
[0:50:34] to go do print on demand integration or
[0:50:36] whatever right so like then what do you
[0:50:38] do you like copy all this because I
[0:50:40] don't want all this context right in
[0:50:42] this new conversation I'm doing
[0:50:44] >> so a couple weeks ago I sent a PR for
[0:50:46] forking so you basically just come over
[0:50:48] here and you can click this button and
[0:50:50] it will fork if you if you click it at
[0:50:52] that point in the conversation,
[0:50:55] it will it will basically take
[0:50:57] everything above that. Kind of similar
[0:50:59] to restore checkpoint. Like if I stick
[0:51:00] if I click restore checkpoint here, this
[0:51:02] current chat goes everything above it
[0:51:04] stays, right? Fork is going to take
[0:51:06] everything above this point and create a
[0:51:08] new conversation. So you can see we have
[0:51:10] five ideas for product improvement and
[0:51:12] then we have this forked one which is
[0:51:13] the same thing. Um you can also come
[0:51:15] down here. So say like I'm at the end
[0:51:17] and I'm like I'm not I am proactive. I'm
[0:51:19] already thinking like I want to actually
[0:51:20] like go ahead and fork this. Actually,
[0:51:22] let me go to my forked forked
[0:51:23] >> and let's see if this this works. I want
[0:51:25] actually wonder what the chat title is
[0:51:26] going to be. So, I come over here and I
[0:51:28] go slashfork again. Let's see. Do I just
[0:51:32] get forked again? Yeah, I just got
[0:51:34] forked again. Um, but you can also come
[0:51:36] down here if you want like all of the
[0:51:38] conversation history to go into the
[0:51:39] fork, you can do that as well. And then
[0:51:41] of course like the I didn't this was
[0:51:43] kind of the initial stab at the titles,
[0:51:45] but you can always come in here and
[0:51:46] rename, right?
[0:51:47] >> Nice. Um, so that's like a nice little
[0:51:49] quality of life improvement. The other
[0:51:50] one that I think is really cool. Oh,
[0:51:52] this is what I really wanted to show.
[0:51:53] Look at this. There's a lot of buttons.
[0:51:55] >> I like how like this is what I really
[0:51:57] want to show. That's what I really want
[0:51:58] to show. That's what I really want to
[0:52:00] show.
[0:52:00] >> There's so many things. Um, so the other
[0:52:02] cool thing is if you come in, where is
[0:52:04] what I want?
[0:52:07] I'm trying to think about how I get to
[0:52:09] what I want. So I come in here and I
[0:52:10] click this. Of course, it's not showing
[0:52:12] now. Um, we have been working on kind of
[0:52:15] a contextual quickpic. I think we
[0:52:17] actually disabled it because we were
[0:52:18] branching for a stable. Um,
[0:52:21] I forget the setting name, but we're
[0:52:23] basically making it so that have you
[0:52:25] ever found it annoying like you'll do
[0:52:26] something and then the command pallet
[0:52:28] opens.
[0:52:28] >> It's called quickpink, but like that
[0:52:31] it'll open over here and you like click
[0:52:32] dialogue over here.
[0:52:33] >> So, we're fixing that. So, like we'll
[0:52:35] have basically contextual dialogues to
[0:52:37] where you clicked so your eyes aren't
[0:52:39] just like constantly going all over the
[0:52:40] screen. So that's like a nice little
[0:52:42] other like quality of life UX tweak and
[0:52:45] that's actually in VS Code core so like
[0:52:46] extension authors will be able to use
[0:52:48] that and things like that. So um I'm
[0:52:50] pretty excited about that one too.
[0:52:52] >> Well this has been a whirlwind. I've
[0:52:54] shown you a lot of things. Um
[0:52:56] >> the uh allow all for this session which
[0:52:59] it's kind of like YOLO but for the
[0:53:01] session. Um
[0:53:04] we get this question a lot. So
[0:53:08] you can come in here
[0:53:10] uh and we're going to add uh a command
[0:53:13] basically uh where is it?
[0:53:16] Is it in [clears throat] this build that
[0:53:17] I have? No, there's going to be a way to
[0:53:19] allow an insiders if not today uh on
[0:53:22] Monday. Uh basically for just this
[0:53:24] session um so you won't have to you
[0:53:27] won't have to like do global auto
[0:53:29] approve you can do it just be like I
[0:53:31] trust it for this particular session. So
[0:53:33] similar to CLI, you can just basically
[0:53:35] say like the equivalent of copilot yolo
[0:53:38] like you can do that inside of in chat
[0:53:40] as well.
[0:53:41] >> Nice.
[0:53:41] >> Nice.
[0:53:42] >> Yeah.
[0:53:44] >> I am kind of curious on the top you know
[0:53:45] you have like settings and new and dot
[0:53:47] dot dot like do we see like that those
[0:53:49] worlds combining at some point because
[0:53:50] like yeah like where is is the settings
[0:53:53] for the chat session? Is it for the chat
[0:53:54] in general? Like you know what I mean?
[0:53:56] Like I'm wondering if that's like where
[0:53:57] like we put some context like oh put
[0:53:59] this into yolo mode type of thing. You
[0:54:01] know what I mean? Yeah. Yeah. I don't
[0:54:04] know. We're still discussing this a lot.
[0:54:06] Um I didn't even talk about all the new
[0:54:08] CLI stuff we have. Um we're still
[0:54:11] discussing this a lot because like Yeah,
[0:54:13] there's just a lot here.
[0:54:16] The challenge is like
[0:54:19] you kind of like there's two purposes of
[0:54:21] this dialogue, right? There's the actual
[0:54:23] like I'm prompting and using the agent
[0:54:25] and then there's also the session
[0:54:27] management experience
[0:54:28] >> and both are in the same and that's
[0:54:29] what's contributing to this like double
[0:54:32] >> thing here right this is new because of
[0:54:35] sessions view
[0:54:36] >> um so that's like a lot of UX
[0:54:39] conversations we're having but some of
[0:54:41] again some of these I'm like could we
[0:54:42] get rid of these like do we need a
[0:54:43] refresh button for the sessions like
[0:54:45] probably not um filter and find I do
[0:54:48] need although I will say like I
[0:54:49] sometimes get tripped up on the filters
[0:54:52] right like I'm like I don't see my
[0:54:53] session and it's like oh I just need to
[0:54:54] reset my reset my filters right so
[0:54:57] >> yeah like I'll click on like the the top
[0:54:59] the little control mission thingy or
[0:55:01] whatever and like it filters for you
[0:55:03] automatically like no uh no not that one
[0:55:06] like click like the the two like you
[0:55:08] click on the two
[0:55:09] >> oh yeah
[0:55:09] >> like that it'll like prefilter it and
[0:55:11] I'm like okay go back and like oh like
[0:55:13] I'm actually filtered you know that type
[0:55:15] of thing for filtered too
[0:55:18] >> so I'm like oh where did all my sessions
[0:55:19] go I'm like ah every all the sessions
[0:55:21] are gone And then no, actually I just
[0:55:22] need to reset my filter basically to
[0:55:24] have them there. So
[0:55:25] >> yeah, this was added in the last
[0:55:26] release, but like these are super
[0:55:27] there's some super nice like quality of
[0:55:29] life things when you're working with
[0:55:30] agents. Like you have this, which is
[0:55:31] like your unreads. You can come over
[0:55:33] here. You can hover over a session and
[0:55:35] you get information. You can come here
[0:55:36] into the title bar, click in here. I can
[0:55:39] send prompts and stuff. Um I can
[0:55:42] navigate to past sessions. Um I can run
[0:55:45] commands obviously and see files. But
[0:55:47] like that's another cool entry point for
[0:55:49] everything is you can just click into
[0:55:50] the title bar here for quick access.
[0:55:53] >> That's cool. I remember talking to I
[0:55:55] think it was Justin I want to say or a
[0:55:57] while ago and we're like oh could that
[0:55:58] thing could that information bar be like
[0:56:00] more than what it is today? And it's
[0:56:02] cool to see like the team expand upon
[0:56:04] that as well. So yeah, good question
[0:56:06] here. Can we not delete them just
[0:56:07] archive them? Is is archiving deleting
[0:56:10] of the sessions?
[0:56:11] >> No, there's there's separate cont
[0:56:13] concepts. So like I'll archive that one.
[0:56:15] >> But I think you can delete right. I
[0:56:17] think you can right click delete.
[0:56:19] >> Uh yeah, you can delete.
[0:56:21] >> Yeah, delete.
[0:56:22] >> Um yeah, so you can archive and delete.
[0:56:25] I think like
[0:56:27] >> I just always always archive everything.
[0:56:29] I don't know if you taught me that for
[0:56:30] email, James. Just always always
[0:56:32] >> always archive. Yeah, commits are free.
[0:56:34] Archiving is free. Just always
[0:56:35] >> archiving is free until your until your
[0:56:37] storage fills up and then it's not free.
[0:56:39] But
[0:56:39] >> you know, everybody's like Gmail is
[0:56:41] mostly it's like 99% spam archived
[0:56:44] emails and actual. Yeah, like most of
[0:56:48] the servers and hard drives in the world
[0:56:50] are just full of junk.
[0:56:52] >> It really is.
[0:56:54] >> Yes, totally.
[0:56:54] >> It's I go into my spam folder on
[0:56:56] occasion just to kind of like see if I
[0:56:58] miss something and it's like every one
[0:57:00] second it's just like something new. I
[0:57:02] just like feel just it's ridiculous. Oh,
[0:57:04] good question.
[0:57:05] >> The same way. Every phone call I get is
[0:57:07] a
[0:57:07] >> it's all spam. It's all spam. Qu
[0:57:10] question that I have uh for this someone
[0:57:14] was asking on Twitter was can I sync my
[0:57:17] chat chats between my machines?
[0:57:22] >> Not currently because it's stored
[0:57:25] locally. But that's something we're
[0:57:27] we're thinking about because it's really
[0:57:29] just like like okay so VS Code has a
[0:57:31] concept of
[0:57:32] >> sync
[0:57:32] >> has a concept of like syncing right we
[0:57:34] sync settings we we actually sync your
[0:57:36] prompt files and things like that right
[0:57:38] if you have global MCP config you've set
[0:57:40] up that would be synced across sessions
[0:57:42] or sorry across devices so there's
[0:57:44] there's no technical reason we couldn't
[0:57:47] also do this um we also have the new
[0:57:53] uh like there's also like so then
[0:57:55] there's another kind of thing which is
[0:57:56] like you have sessions that are scoped
[0:57:58] to like just your you know what you're
[0:58:01] working on and what workspace you have
[0:58:02] open but like we're also working on like
[0:58:04] a more global experience for looking
[0:58:06] across all your workspaces you can kind
[0:58:08] of see a little bit of this in the
[0:58:09] welcome view obviously I don't expect
[0:58:10] people to be using the welcome view for
[0:58:12] these sorts of things but like um this
[0:58:14] is kind of taking sessions from multiple
[0:58:16] places and showing them here so um so
[0:58:19] that's like the the direction we want to
[0:58:21] go is these sessions go with you
[0:58:22] everywhere regardless of what device
[0:58:24] you're on you can get to them anywhere
[0:58:25] regardless of what device you're on. And
[0:58:27] if you just log into VS Code, you get
[0:58:29] what you need.
[0:58:30] >> Yeah, I like that. That's that's I like
[0:58:32] that. Someone says P's IDE is looking
[0:58:34] like Vzero Bolt.
[0:58:37] >> I mean I mean it's funny because I think
[0:58:40] everyone uses, you know, VS Code or the
[0:58:42] CLI differently, right? Like your
[0:58:44] experience and how I like like I'm often
[0:58:47] browsing files. I'm looking at diffs.
[0:58:48] I'm doing like I'm I'm actively as the
[0:58:51] the chat is outputting diffs. I'm I'm
[0:58:54] actively like looking and changing and
[0:58:56] like and like I want to see what the
[0:58:58] code changes are and then I don't know
[0:59:00] if Burke looks at code anymore. I think
[0:59:02] that it just flies by. I'm pretty sure
[0:59:04] from reading your I think code doesn't
[0:59:06] exist and I think Pierce is maybe
[0:59:08] somewhere in the middle. Like I think
[0:59:10] everyone and everyone is in different
[0:59:11] places and like that's okay, right? And
[0:59:14] VS Code is trying to figure out how to
[0:59:16] do that. And like I like to use the CLI
[0:59:19] often inside of VS Code as well to kind
[0:59:21] of like see the diffs happen in real
[0:59:24] time as they're flying by because I like
[0:59:26] to I like to see the changes. I like to
[0:59:27] see my visual get changes as well. But
[0:59:30] some people are just go like Hanselman
[0:59:32] is just a CLI exclusive person, right?
[0:59:35] And just that's how your brain brain
[0:59:38] works, right? And that's why I think
[0:59:39] like the bigger GitHub copilot story is
[0:59:41] so important, right? Using it and seeing
[0:59:43] it absolutely everywhere is so cool uh
[0:59:46] as well. I think the challenge to your
[0:59:47] point is like everyone partners with
[0:59:49] agents differently and also how I
[0:59:50] partner with agents changes every day
[0:59:53] and then it's like well then how do you
[0:59:55] build you know as a product builder how
[0:59:57] do you build an experience that people
[1:00:00] will be happy with when there are people
[1:00:02] who are like I literally want to babysit
[1:00:04] this thing and watch every single thing
[1:00:06] that this agent is doing live
[1:00:07] synchronously and then at the other
[1:00:09] extreme you have people who are like I
[1:00:11] never want to look at code I have 15 of
[1:00:13] these things running at once right and
[1:00:15] also like our confidence in the models,
[1:00:17] especially since like the Opus moment in
[1:00:18] December, like we have way more
[1:00:20] confidence in the models, too. And so,
[1:00:21] like there's just like such a vast
[1:00:23] spectrum. And then even like maybe I'm
[1:00:25] okay with just not looking at the code
[1:00:26] in my coloring book app, but in when I'm
[1:00:29] doing VS Code contributions, I care a
[1:00:30] lot about that, right? So, I think it
[1:00:33] also changes depending on what I'm
[1:00:35] working on as well. So, all of these
[1:00:36] things make building this UX extremely
[1:00:38] tricky. Um, so keep sending us your
[1:00:41] feedback on what you want.
[1:00:44] >> I love that. Yeah. Yeah, and I think
[1:00:45] it's the same. Uh, Pierce, I know you
[1:00:47] got to run. I know uh I have to run here
[1:00:49] and pick up my dog from our sitter here,
[1:00:51] but um I I don't know, Burke, if you're
[1:00:54] able to share your screen, give a sneak
[1:00:55] peek of next week's Let It Cook, which
[1:00:58] will be a full Burke stream on
[1:01:01] Ultralight and all the stuff that you're
[1:01:03] doing. I'm sorry.
[1:01:05] >> Yeah, we were gonna do it on this
[1:01:07] stream, but I think so.
[1:01:08] >> I know y'all Wait, are y'all leaving?
[1:01:10] It's just me.
[1:01:10] >> No, no, no, no, no, no.
[1:01:12] >> Just preview what's new for next week.
[1:01:14] We're gonna preview and then we're gonna
[1:01:15] leave.
[1:01:16] >> Yeah.
[1:01:16] >> All right.
[1:01:16] >> Yeah. You're live. You're live for the
[1:01:18] next five hours, B. Just so you know, we
[1:01:20] didn't tell you.
[1:01:21] >> I can do it. I'm not afraid. Wait, how
[1:01:23] do I
[1:01:24] >> We can't marry you.
[1:01:25] >> Oh, no. I have the new
[1:01:27] >> No, I'm just kidding.
[1:01:28] >> I know you can. Hold on. I have the new
[1:01:30] freaking
[1:01:31] >> He's gonna have to refresh.
[1:01:33] >> Add system settings.
[1:01:35] [laughter]
[1:01:35] >> This is my I So, I've been building tiny
[1:01:38] I've been building tiny clips.
[1:01:40] >> I've been building tiny clips. And let
[1:01:42] me tell you, so if you don't know Tiny
[1:01:44] Clips, it's a little Mac app.
[1:01:45] >> All right, y'all. I really gotta run.
[1:01:46] You'll close it out. I gotta get out of
[1:01:48] here. I'm coming right back.
[1:01:50] >> I'll talk through this while you go. So,
[1:01:52] I've been building out Tiny Clips over
[1:01:53] here. And I'm going to B Pierce just to
[1:01:56] say this. So, Tiny Clips has been quite
[1:01:57] fun to build exclusively as like a Mac
[1:02:00] desktop app. Uh, and learning the
[1:02:02] permissions of the Mac OS have been a
[1:02:05] joy to use, which is why you see people
[1:02:07] get new machines or do things like this.
[1:02:10] uh it's a it's a joy to see in general
[1:02:12] like going these permissions opening
[1:02:13] closing refreshing doing stuff as well
[1:02:16] which is why Burke had to had to drop
[1:02:18] and then we'll come right back uh with
[1:02:20] these permissions in the system and
[1:02:21] actually building these applications are
[1:02:23] like ridiculously hard to do as well uh
[1:02:26] there but okay we got the Burke back
[1:02:28] there he is he's given permissions to
[1:02:31] the machine yes tiny clips
[1:02:33] >> tiny clips permissions as well yeah what
[1:02:35] so let's sneak peek what we're going to
[1:02:37] talk about next week a little bit I like
[1:02:39] how your name changes every time as
[1:02:41] well. So
[1:02:43] >> what it's the same I'm going to share.
[1:02:45] So I'm I have a new machine and and
[1:02:48] things are kind of messed up. Um so I'm
[1:02:50] sorry and interception here for a
[1:02:52] minute. Let's I want to show something.
[1:03:02] >> Hold on. You roboted on me. You're
[1:03:04] roboting on me.
[1:03:05] >> No, I'm not.
[1:03:06] >> Okay. You're back.
[1:03:06] >> Am I back?
[1:03:07] >> You're back. Okay. So, what is what
[1:03:11] what is it like if you really use the
[1:03:14] agent to orchestrate everything? And
[1:03:16] what I mean by that
[1:03:16] >> should I bring up your screen? Should I
[1:03:18] bring up your screen?
[1:03:19] >> Yeah, go ahead.
[1:03:19] >> Okay. I was I was worried. Okay, I'm
[1:03:21] ready. Okay. What I mean by that is like
[1:03:23] you have the agent that you work with
[1:03:25] locally but then you also have the cloud
[1:03:26] agent and in order to properly orch like
[1:03:29] if you wanted a team James of like 10
[1:03:31] agents working on something at one time
[1:03:34] in order to do that locally you have to
[1:03:36] do you have to check out work trees
[1:03:38] which may not be feasible for your
[1:03:40] project if it's massive right so what if
[1:03:43] instead you have one agent that's
[1:03:44] running locally on your machine and it's
[1:03:47] spinning up agents in the cloud the
[1:03:49] cloud coding agent who then submit PRs
[1:03:52] and the orchestrator then pulls that PR
[1:03:55] down,
[1:03:57] checks it, makes sure that it merges and
[1:03:59] builds and then goes ahead and merges it
[1:04:02] back to main.
[1:04:03] >> Yeah.
[1:04:03] >> And then you like as the you're
[1:04:06] essentially now the project lead and
[1:04:07] you're just reviewing what it's doing
[1:04:10] >> every time it runs out of issues.
[1:04:12] >> Oh, cool.
[1:04:12] >> And then you're basically talking back
[1:04:13] to the orchestrator and saying, "Okay,
[1:04:15] here's what I'm seeing. I want you to
[1:04:16] change this." and it opens a bunch of
[1:04:18] issues for you and then comes back and
[1:04:20] tells you when that's all done.
[1:04:22] >> Yeah.
[1:04:22] >> Right. So now you're like you have your
[1:04:24] own dev shop. So let me just show you.
[1:04:26] Let me just show you. I built
[1:04:30] um a native Mac app to wrap the Copilot
[1:04:35] CLI. Now is it good? No, it's not good.
[1:04:38] But when I say I built it, so here it
[1:04:40] is. But so you can see like it's all
[1:04:42] kinds of messed up. But when this thing
[1:04:45] got built, I didn't actually build any
[1:04:47] of this. I basically dictated what I
[1:04:49] want and then the agent like the
[1:04:51] orchestrator then spun up all of these
[1:04:54] issues.
[1:04:56] Oh, that's not We'll take a look at that
[1:04:58] in a second because that's like the fun
[1:04:59] way to do this. Um,
[1:05:02] hold on. I can't I can't spell too much
[1:05:04] coffee, man. I'm super shaky. Um, Anvil.
[1:05:07] Yeah, Anvil tool.
[1:05:10] One second here. github.com/berkholland
[1:05:14] slash.
[1:05:16] So if you look at this, see all these?
[1:05:18] So there's 19 issues out here. So it's
[1:05:20] not running at the moment, but you can
[1:05:22] see there's 19 issues here. And pull
[1:05:24] request, there's 156. It's just been
[1:05:27] running in a loop for days adding its
[1:05:29] own features and trying to figure out
[1:05:31] what it should do. And so now I've got
[1:05:32] to the point where I'm I'm prompting it.
[1:05:34] So what I'll do, you know, is sit down
[1:05:36] and say, you know, I like this, I don't
[1:05:38] like that. Let's change this. This
[1:05:40] sidebar looks terrible. And then it goes
[1:05:42] back like it's flashing over here. I
[1:05:43] don't know what's going on. And so
[1:05:45] that's the idea that we're going to be
[1:05:47] exploring. Now, in the meantime, and I
[1:05:49] can't I shouldn't even do this.
[1:05:52] This is a terrible idea,
[1:05:56] but
[1:05:56] >> I'm ready.
[1:05:57] >> If you go to burrholland.github.io
[1:06:00] town,
[1:06:02] [sighs and gasps]
[1:06:05] you can claim a building in this town.
[1:06:08] And what you do is you just go up and
[1:06:10] you say add building
[1:06:12] and then you can open a GitHub issue
[1:06:16] and it will add a building to this town
[1:06:18] with your name on it here.
[1:06:21] Chat, do not make me regret this.
[1:06:24] [laughter] Okay, but it's using the same
[1:06:27] concept, right? There's an orchestrator.
[1:06:29] I can you can stop pull me off now.
[1:06:32] There's an orchestrator that is
[1:06:35] >> that is looking and seeing you submit an
[1:06:37] issue. It pulls it down, uses copilot to
[1:06:39] check it and make sure you're not trying
[1:06:40] to do shenanigans and then will build it
[1:06:43] in 3JS, you know, it's using the cloud
[1:06:45] coding agent to do that and the
[1:06:47] orchestrator running locally is doing
[1:06:48] all of that. And so I won't touch
[1:06:51] anything. It will reply to you as the
[1:06:52] town mayor and tell you yes or no, your
[1:06:54] building hasn't been approved. So that's
[1:06:56] what we'll do next week is just look at
[1:06:58] like how can we set up these complex
[1:07:00] workflows. Yeah,
[1:07:01] >> that further remove you from the loop
[1:07:04] and put more agents in charge. And how
[1:07:06] feasible actually is that? Because we
[1:07:08] don't we don't really know.
[1:07:10] >> Yeah, I'm interested. A lot of people
[1:07:11] have been talking about this sort of
[1:07:12] this orchestration part which we we've
[1:07:14] seen a little bit when it comes to
[1:07:16] planning and and implementation and
[1:07:18] going back and forth. But I'm really
[1:07:20] interested in exactly what you've been
[1:07:22] talking about, which is I'm often coming
[1:07:24] up with the ideas for my application and
[1:07:27] then submitting to to different agents
[1:07:29] and doing stuff. But I ideally wanted it
[1:07:30] to kind of think through things and and
[1:07:32] and to kind of just fan it out for me
[1:07:35] automatically. And I'm interested how
[1:07:37] you've been thinking about it as it goes
[1:07:39] like in general and and as you're
[1:07:42] building out these applications or
[1:07:43] you're building out these workflows like
[1:07:44] how are you actually thinking about it?
[1:07:46] Are you submitting the issues anymore?
[1:07:47] Are you planning it out or like how are
[1:07:50] you actually thinking about coding now
[1:07:52] in kind of Feb going into March of 2026?
[1:07:55] Yeah. I think every month we how are you
[1:07:58] thinking of coding and
[1:07:59] next week, none of this will be relevant
[1:08:01] anymore. So, we'll just change the whole
[1:08:02] show. But yeah, we should do that next
[1:08:04] week. Just talk about what are the
[1:08:05] options right now. And what I always
[1:08:07] tell people is just remember chat,
[1:08:10] >> just remember nobody knows what they're
[1:08:11] doing. All we know right now is that we
[1:08:14] can build features and we can try new
[1:08:16] ideas and we can see what works and what
[1:08:17] doesn't work. So don't don't feel like
[1:08:20] just because somebody's like, Ralph,
[1:08:22] like you have to stop what you're doing
[1:08:23] and go do all of that. You don't.
[1:08:25] >> Yeah.
[1:08:26] >> Right. Just explore things and have fun.
[1:08:28] Yeah, I like it. All right, next week
[1:08:30] more orchestration, AI towning, ultra
[1:08:33] lighting, anviling, all the things. I
[1:08:35] also like that you're coming up with
[1:08:36] unique names as well. I've been enjoying
[1:08:38] watching your Twitter feed.
[1:08:39] >> AI is coming up with all What do you
[1:08:40] think it's me? I'm not doing any of
[1:08:42] this.
[1:08:43] >> Hey, somebody's got to prompt it. I'm
[1:08:44] just saying.
[1:08:45] >> It's true.
[1:08:46] >> Somebody's got to prompt it. I'll take
[1:08:48] >> uh Well, I'm glad to have you back on
[1:08:50] the stream. Uh next week, join us for a
[1:08:53] lot of deep live coding as well. So,
[1:08:55] we'll be showing off the latest features
[1:08:57] as always on the Let It Cook, but we're
[1:08:58] do more actual cooking cooking.
[1:09:01] >> Maybe maybe we can get uh maybe Jay will
[1:09:03] come on. [laughter] How cool would that
[1:09:05] be?
[1:09:05] >> We have been talking to Jay Periq, our
[1:09:08] uh CVP. EVP.
[1:09:10] >> He's the EVP
[1:09:11] AI. Let's see if we can get him on here.
[1:09:13] >> We really want to. So, go uh tell tell
[1:09:17] uh Jay that we want to see him on the
[1:09:18] stream because he's been actively
[1:09:20] submitting PRs into like the CLI and
[1:09:22] other things as well. So, we want to
[1:09:24] cook live with with Jay. So, so that's
[1:09:26] another sneak peek that we'll do a
[1:09:28] special uh Let It Cook with our
[1:09:31] >> We'll do Jay and then we'll have Satia
[1:09:33] on. That's the goal.
[1:09:35] >> That's the goal of this show. It'll be
[1:09:36] like uh just growing growing and fanning
[1:09:39] up from from your favorite from your
[1:09:41] favorite folks into into us as well. All
[1:09:43] right. All right. I think that's going
[1:09:45] to do it for this Let It Cook. Thank
[1:09:48] y'all for watching. Come back next week
[1:09:50] for live coding with Burke Holland on
[1:09:53] Let It Cook. All right, thanks everyone.
[1:09:55] Like, subscribe, do all the things.
[1:09:57] Peace. [music]
