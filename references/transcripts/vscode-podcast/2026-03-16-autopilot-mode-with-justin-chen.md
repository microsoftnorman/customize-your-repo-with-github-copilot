---
series: VS Code Insiders Podcast
episode: 20
title: "Autopilot Mode with Justin Chen"
url: https://www.vscodepodcast.com/20
transcript_url: https://media24.fireside.fm/file/fireside-images-2024/podcasts/transcripts/f/fc261209-0765-4b49-be13-c610671ae141/episodes/4/4ad3d932-a795-4fba-8c48-b0c3e1a1dec0/transcript.txt
audio_url: https://aphid.fireside.fm/d/1437767933/fc261209-0765-4b49-be13-c610671ae141/4ad3d932-a795-4fba-8c48-b0c3e1a1dec0.mp3
published: 2026-03-16
duration: 26:30
transcript_available: true
---

# Autopilot Mode with Justin Chen

This episode was sourced from the official VS Code Insiders Podcast site.

## Episode Summary

        Justin and James deep-dive into Autopilot and the evolving VS Code chat UX—why shimmers and collapsed containers declutter conversations, and why the input bar split and new permissions picker matter. Learn how Autopilot (Insiders preview) can auto-approve tools, answer prompts, iterate until a task_complete signal or max retries, and when to use default vs bypass approvals; practical tips for safe, hands-off workflows and feedback.

Follow VS Code:


X: https://x.com/code
Bluesky: https://bsky.app/profile/vscode.dev
YouTube: https://youtube.com/code
LinkedIn: https://www.linkedin.com/showcase/104107263
GitHub: https://github.com/microsoft/vscode
Special Guest: Justin Chen.
      

## Transcript Status
An official transcript was available on 2026-04-21.

## Full Transcript
00:00.38
James
Welcome back everyone to the VS Code Insiders podcast, the behind the scenes look at your favorite code editor, VS Code. I'm James Montemagno, your host and with me, the one, the only software engineer on the VS Code team. Well, there's more than one. Justin Chen is here. How's it going, Justin?

00:15.54
Justin
Good, how's it going? i think I'm pretty excited to talk about Autopilot today.

00:21.43
James
Yeah, I'm super stoked. You and i were so planning on starting to record this podcast about 20 minutes ago, but then we just geeked out on Pokemon and and the Nintendo Museum and Pogtopia and everything like that. So that fun.

00:37.21
James
And people may notice that you're a little bit of a Pokemon fan, just a little bit.

00:37.27
Justin
wow

00:40.76
Justin
Just a little, just a little. I don't know if you can tell. And also the giant VS code sign in the background as well. i sold that from Walmart.

00:47.74
James
The two of them together. It's beautiful. I love it. um i myself also a huge Pokemon fan, so I'm excited to to geek out and and play some Poketopia together. So um today is going be a little bit special because there's been honestly like a crazy amount of amazing new features inside of VS Code. And we try to like talk about some of the deeper things inside of here. And I think what's been really fascinating, Justin, is kind of how the chat has evolved quite a bit and how developers

01:18.30
James
are focusing on interacting, working with tools. And now there's so many tools, skills, agents, MCPs, like actual, and you know tool, normal tool calling, things like that. Like what's your day to day in this space and what's your main area that you're focused on on the VS Code team?

01:34.84
Justin
yeah Yeah, the main thing I've been working on recently is just the general chat UI and UX and just general chat experience because i think there's a lot that goes into like what you see when the chat is like rendering or a lot of like tools that you can utilize to to properly, I guess.

01:56.22
Justin
I guess to use the agent to the better the best to the best extent as possible. um Yeah, I work mostly on UI rendering, a couple of the UX features with the input box, editing previous requests, checkpoints, just a little bit of everything to kind of make your experience in chatft the in the chat panel a little bit better.

02:17.02
James
I really feel like for me, as I use the chat, as a team has been evolving these features, everything you just mentioned, like I use, I use like steering, I go back, i edit previous requests. Like I'm looking at the output, like the streaming input that's coming in. I've noticed a few things before we get to autopilot is like,

02:32.82
James
It feels as though, and maybe you can distill this down since you're in this area. It feels like the chat is less chatty recently. You know what I mean? Like, like it's a lot more like a lot more like ah shimmers.

02:43.75
James
You know what I mean? Like what is happening? What is evolving in that space?

02:46.65
Justin
yeah Yeah, I think ah it's partially maybe some of the quirks of the models, but I think one thing that we've been working on is just kind of making... making the chat not so annoying, I guess, and making it a little bit more consistent as you go through it and look at it. So for example, the shimmers, right? A lot of the reasoning text, a lot of the tool calls, a lot of these things are getting collapsed into containers now, and they'll just collapse away once you're done. So as you kind of scroll through your chat, you you might notice that there are a lot of these like dropdowns that contain a lot of information inside, but maybe it's something that as a user, you don't actually need to care about.

03:22.97
James
That's cool. Yeah. I've been, I'm a big, and Pierce knows this. I'm a big like reader of the chat. I love to understand like what the agents are doing. I almost need a slow mode. You know, like on YouTube, you can do like slow mode. If there's like, can I get a slow, I don't one would use it besides me. So don't add it for me. Maybe I'll add an extension, but I have noticed that. Like, how is like the reception of that been? Have you seen like good feedback as far as like minimizing the chat or even as you're using it every single day?

03:47.19
Justin
I think it's been pretty good. i think it feels pretty good for it to be consistent. I think something that we had a couple months ago was that we had check marks all over the place. I think some of our tool calls would show up on the surface when like maybe it's a little bit annoying to see 10 read tool calls back to back to back to back.

04:03.64
Justin
And I think just collapsing some of this stuff away, making it a little bit more minimal, making it more consistent, removing the check marks, adding stuff like um the collapsed thinking mode where it just shows one tool call or the current tool call happening at the time.

04:16.57
Justin
um I think the reception has been pretty good and it makes the chat feel kind of alive still with showing working progress, but also a little bit more minimal.

04:25.67
James
That's cool. And I also noticed, Pierce showed off, that you can customize the text of the shimmers of like what it's doing to...

04:31.86
Justin
Yes, yes um I've been a pretty big fan of that. I wanted to see the text bribing the hamster and in chats. Like my Internet's not going fast enough, so I got to feed the hamster more.

04:44.95
James
There you go. And now you can. So I love it. Um, I've also noticed like that clarity has been helpful because sometimes when there's so much happening and scrolling in the chat, you, you know, I can read like those, those things, the thinking and the reasoning, but like, sometimes I'm like, Oh, did it actually like execute my skill? And like, now it's actually pretty clear because those things are auto collapse. I'm like, I can, I can actually see like the action it's taking and not necessarily having to read every single thing. So it feels like those actions are much more important.

05:12.41
Justin
Yeah, yeah, it'll it'll always clap down and summarize. It's an LLM-generated title regardless. So sometimes it's not 100% accurate of what it actually did or like maybe it's trying to summarize a lot of stuff at the same time.

05:23.80
Justin
But normally, let's say you had like four reads and it like read a skill. try to say something like, reviewed and like updated this and this. So hopefully that will help out with just kind of skimming through the chat and seeing what it tried to do.

05:32.40
James
That's cool.

05:37.27
James
Now, it seems like that chat bottom window is ever evolving. Like it is always changing, especially if you're on Insiders, you're rocking Insiders. Every day it's different. I'm pretty sure that between local background CLI cloud, that background co-pilot CLI, CLI work tree has changed the verbiage like a hundred times, which I love, by the way. But there's a bunch of new things. Can you walk through, at least when we're recording this in the year of of March 12th, 2026, Like what has changed in the bottom input windows, like for developers to kind of know about, um in both stable and obviously an insiders and like, why is that evolving? And, uh, what should they know but before we go to the brand, brand new hotness?

06:21.91
Justin
Yeah, yeah. I think the main thing is that we've split the toolbar that used to be in the input box into two different toolbars now. And the reason we wanted to do this is because there are some things that are more applicable towards the session and then some things that are more applicable towards the request.

06:38.58
Justin
So that's the main like differentiation between the two toolbars. um I think the permissions toolbar, the permissions picker is the main thing that's new and adding this additional thing just would have made that input bar too large anyway. So from a UX perspective, it made sense to split it out, but also kind of gives you a good mental image of what's actually happening in the session because the things at the bottom include the um like the the agent harness. So it'll be either like local, copilot, CLI, cloud, or Claude.

07:09.46
Justin
And then the other one in there is the permissions picker, which I just talked about. So that's the main new thing we have now.

07:16.06
James
No, it makes a lot of sense. I like actually that didn't make sense to me why I moved until you just said it, which is like for the reason, because actual, the context of those different, um, those different fields are important, right? Cause you're, when you're inside of a local session, you are adding context, you are picking the agent, you are picking the model, you are calling the tools, but it's always a local session once you pick that, right, in general for that whole state. Well, let's talk about that permission picker because it's gonna be brand new because everything else has been there kind of, and it's evolved and changed around a little bit, but it's brand new. um And if people have used like the Copilot CLI, some of these things may be new to them, but also some of these features have been in the product, but now exposed in the UI a little bit more. So when people go into VS Code, on the bottom of the chat window, they're going to see that local background, you know, CLI slash cloud, you know, agent where it's running. But they're going to see the permissions.

08:11.74
James
What is this permissions? What's in it? And what should people care about it right now today?

08:19.19
Justin
Yeah, so want to talk briefly about like the main reason we wanted to expose it. I think people just didn't really know that we had global auto-approved, right? it's It's something that if you go into your settings right now and you search YOLO mode or YOLO, it does show up.

08:32.98
Justin
How many people are actually clicking this? I'm not entirely sure, but I would constantly get questions like, oh, do you guys actually have YOLO mode? Yes, we do. And there's just a way to surface it. um And just to try to solve that friction between approvals, like having to constantly say, allow, allow, allow.

08:46.97
Justin
And the the three things that we currently have in the permissions picker are the one that you might see on startup. It's called default approvals. We have something called bypass approvals. And the last one is enabled currently by default only in state and insiders and will be slowly rolled out and stable as we continue to run evaluations on it as well as do some...

09:08.24
Justin
evaluation on like how cost is going to work and that the run is autopilot. So I can briefly talk about what those three different things mean.

09:19.03
Justin
I guess this one with default approvals, it's basically as if nothing changed, right?

09:19.34
James
Yeah.

09:24.67
Justin
It's going to use your default settings. It's going to use your configured settings. I believe the the description there says like Copilot will use your configured settings. And what that really means behind the scenes is if you haven't changed anything in the in the user settings, if you haven't changed anything in like the workspace settings or enterprise hasn't said anything,

09:41.75
Justin
it will prompt you to allow certain tools to happen as you're going through the chat. um But it will also take a look at what settings you have set, including any of the edit auto-approved settings, which are, i think they're like pattern-based rules for file edits. So certain files will get edited, certain files won't. I'll take a look at terminal auto-approved settings. Like I believe with terminal auto-approved, we have like safe commands like CD or like cats or grep. I think these are some some terminal tools that are automatically approved, but some of them are not like RM or curl or eval, et cetera, et cetera.

10:19.06
Justin
these terminal tools will get prompted to allow them in the session based on that setting. And then the last one is with yeah URLs, um with like fetches, like itll it'll double check, do you want to fetch from this yeah URL specifically? So these settings are just all settings that you can find in the and the settings UI. You just search auto-approved, I believe.

10:39.32
Justin
um But yeah, any setting related to auto-approved will be followed in this default approvals mode. And and It's already, once again, already mentioned, it's already pretty good. You can configure it to be very specific in this mode, but then that brings us to the question of what if I really just don't want to deal with approvals at all, right? And that's where bypass approvals come in. I think the description in bypass approval says allow all tools are auto-approved, something like that. And basically what it means is that

11:14.94
Justin
we are automatically approving most tools. The only tools that actually won't be approved are stuff like ask questions or anything that requires explicit user input. So for example, ask questions tool, as well as any terminal commands that might require you to type like yes or no or terminal commands that require user input. So those are the two things that um will will stop and not be auto-approved. But pretty much everything else will automatically ah be approved. And this is just an enhancement on the existing global auto-approved setting

11:47.61
Justin
um it's We're kind of in a weird state right now where we have this permission picker and still the setting. But the idea is that when you have it set in the permissions picker, it applies to that request in that session and it ignores any existing settings you might have set.

12:03.13
Justin
So anything that you set with all those auto-approved settings that I just mentioned will get completely ignored if you have bypass approvals on. It will just automatically continue on on tool calls, it'll auto-retry on errors. that's That was like a big one as well.

12:17.88
Justin
And then it will um still prompt you for certain things that require user input. and i

12:24.09
James
Yeah, and that's super. yeah and that's super nice too, especially if you're working like inside of a sandbox or like a code space. Like I was working on, i did a pull request for, i did a pull request, Justin, i don't know if you want to approve it.

12:36.03
James
if I did a pull request to the VS code, uh, repo and you know, in the chat, there's a gear and right now it's a huge dropdown list of a bunch of stuff.

12:42.49
Justin
Right, right.

12:45.97
James
What I really wanted to do is bring up the new, um, customization ui So I did a pull request and I was like, I don't know anything about the VS code code base. Don't really care about it. Uh, as far as like learning where every single thing is, but I wrote a big plan and I was like, Hey, let's plan this out. And I was like, cool, do a bunch of stuff. And then just like, keep going, right. Just keep going, keep doing stuff, figuring it all out, write the test, validate the stuff. And that was nice because it wasn't necessarily like doing a lot of what you're saying of like having to run tons of terminal commands or running a bunch of web stuff. but it was like running tests. It was checking the output where I would have to be validating every single time, but I was in a code space.

13:26.35
James
So I was like in a, in a, just cloud environment where I was in a safe environment. And that was super nice. Um, just in general or, you know, or for example, know, I guess with bypass tools, you can still limit the tools that it has. Right. So if you're just working with MCPs and you're like, I only want able to do these things that can only follow those tools, which is kind of nice too.

13:44.60
Justin
Exactly, yeah. Yeah. um And I guess to kind of roll on to the third picker that we have now, and that's the cool, shiny new thing that we've been working on. So this was actually inspired by Copilot CLI. So Autopilot is actually a mode that Copilot CLI already has existing. And it was something I wanted to bring over to VS Code because I think the application, it's pretty much the same, whether you're on local chat or using the Copilot CLI in VS Code. um I think generally, if you're if you trust the agent, if you're in a safe environment, I think it's a great tool to just create a great plan and then let it run let it run its course. And you can kind of like shift tasks and do a couple different things. But thought yeah, the idea behind it, it's currently still in preview.

14:31.67
Justin
As I mentioned at the beginning, insiders only at this point in time. You can enable it with the chat.autopilot setting in Sable, but it won't be defaulted to true there.

14:42.97
Justin
um And the premise of autopilot is that it has everything that bypass approvals has and a little bit more. The idea is that it will try to iterate autonomously until it's until it thinks that it's done with a task.

14:55.45
Justin
And the inspiration, as I mentioned, CLI, I think Cloud Code also has something similar called like a ralph loop. But it will actually do a couple of additional things like auto-replying to questions. So if the ask questions tool gets run, it'll auto-reply to those questions.

15:12.44
Justin
um If it's a user input required anything, whether it's a terminal or with the ask question tool that requires user like to type an answer in a freeform box or something like that, it'll respond by saying that the user isn't there to act on its flexibility.

15:27.99
Justin
And then lastly, it will retry and like kind of try and continue depending on the states of where it thinks it currently is. So we have this thing called the task complete tool, which is just saying, hey, don't call this tool unless the task is actually complete. And obviously it's a, I've dumbed it down a little bit, but the idea is that we check to see if that task complete tool was ever called.

15:51.45
Justin
Otherwise, we just continue to let it iterate, let it iterate, let it iterate. We do have a max continuations. I believe right now we say like max reiterate like five times. The idea is to make this configurable down the line. But at the moment, we're just hard coding it at that point.

16:07.42
Justin
um Yeah, I mean, it's just a cool thing to set off on its own. I don't want you, I don't want the agent to ask me anything. I don't want the agent to, to have to require any user input. I'll just let it run its course, finish the job. And yeah, I think it's just pretty cool to, to not have to look at the agent turn by turn and be like, oh, I have to approve all this. And and now i'll just let it run its course.

16:30.58
James
So you said it is different. So is the thinking then different between bypass, like bypass and default basically runs the same system prompt, but you're saying autopilot has some extra juice to it basically.

16:44.06
James
And if I'm understanding it correct, like is that extra juice in the way that it's thinking, in the way that it's looking at the task list? Like, is it validating its work? Is it is it implementing something and then revalidating it? And then like, like is it like code reviewing it? Like, is is that the type of loop that it's doing until it's done?

17:04.92
Justin
Yeah, so unfortunately at the moment, it's not that smart. I think we're we're doing some evals. We're trying to see where we can improve it, like stuff of like code review or stuff of like forcing iterations. But right now, realistically, we just have a slightly modified system prompt letting it know that it's an autopilot, letting it know that the user is not going to be there to answer any questions or to to so like basically answer any questions or answer any like user required inputs that we might show. But the main thing is just with this task complete tool. The idea is that the task complete tool will just be the the source of like ground truth where, yes, you called it.

17:41.43
Justin
We know we're done. We haven't called it. Let's try to continue until we actually are finished. um And I see a lot of times in like my own testing that sometimes it'll it'll work its way down and then it'll finish, but then you'll notice that the task isn't complete and it'll be like, oh, let me try again. And then maybe in that try again, it'll actually try to run some tests or it'll try to do some more reads or do some more tool calls.

18:05.69
Justin
There are a couple cases where it doesn't need to do anything else and they'll just return like, oh, hey, I'm actually done. And then it'll actually finish.

18:13.59
James
Got it. I see. And then there's some models that what I've noticed too, maybe this is where this autopilot comes in. Some models like to do like one or two things and then stop and be like, Hey, you want to check out this work?

18:24.66
James
And then just say like, continue or like, do do you want me to validate it? Right? Like, and the answer is like, probably like, yeah, run the build. So in this case, you're saying it'll just continuously go through that list. It's not going to stop basically. It's just going to keep going.

18:38.84
Justin
Exactly. yeah um We have um some, like, I mean, we're all open open source, so you can actually go and look at what part task complete tool says. I think it says something along, like I mean, I haven't pulled up here, but says something along the lines of like, yeah, signal when the task is completely done.

18:53.43
Justin
um Like, don't like provide a summary when you're finished. Like you must call this tool only when task is complete, verify that your changes work, like double check that there aren't any like remaining to-dos. And then on the case of continuation, we mentioned, oh, like,

19:09.24
Justin
um because you haven't called this tool yet, make sure that you verify that the tool is complete or that the the task has been complete using this tool. And then I'll continue iterate and then I'll actually mark it that's done.

19:18.98
James
That's

19:21.62
Justin
So yeah, I mean, so yeah, still playing around with it and and and like, again, trying to do some evals on it.

19:22.30
James
cool.

19:27.90
Justin
doing some a lot of self-hosting on it. um But generally, I think it's it's a great tool regardless because it still does all the bypass approval stuff and you can be a lot more hands-off instead of just like disabling the Ask Questions tool or something.

19:43.19
James
That makes sense. I've also noticed that Uh, there's integration with plan mode as well with autopilot. Like I've noticed, i don't know if it happens every time or not, but on occasion I see like run with autopilot, like how is that integration working?

19:57.91
Justin
Yeah, yeah. so if So there are two ways that... There are two kind of entry points. So the first one is if you start plan mode in autopilot, it will...

20:09.91
Justin
Well, plan mode normally doesn't really like ask for approvals except for like with the Ask Questions tool. But if you start the plan mode with autopilot, it'll go through. It'll know that it's in autopilot.

20:20.11
Justin
It'll answer the questions automatically.

20:21.92
James
Wow.

20:22.33
Justin
And then once it's done planning, it will automatically hand off to the agent. So it'll go plan in autopilot and then immediately start implementation. The alternative is if you start it in regular like approvals, it will still end at the end of the when ah when it's done planning, but then there will be that handoff option to start in autopilot in which you click on it and then it'll turn that session into autopilot.

20:48.25
James
So you said you've been dogfooding and doing some internal stuff. How are you using autopilot and how are you seeing it? Like when are you making the distinction of the different modes personally?

20:58.71
Justin
Yeah. Yeah. Um, honestly, it's been like 99% autopilot. I guess part of it is the dog fooding. And then part of it is like, in terms of like what I'm trying to get done, it's just more convenient if I just never have to take a look at it Maybe I'm just taking a look at what happened at the end, reviewing the code at the end.

21:17.37
Justin
Um, there there are very There are certain applications where it's like maybe it's better to use bypass approvals instead of autopilot. But yeah, personally for me, like if I'm just setting off like three or four different like sessions to take a look at like a bug here or a bug there, um just having it run in autopilot where it'll automatically verify either either like I attach a link to a GitHub PR or a link to a GitHub issue, and I'm like, oh, it'll automatically fetch it, it'll automatically do any like, it'll automatically do any like terminal tool calls for me, it'll automatically create work trees for me, stuff like that. It's just way, way easier for me to just go through and then go through the different work trees and they're all on autopilot. So I just look at the final results.

21:59.51
James
Wow, that's really cool. I didn't know that it spawn off work trees for you as well. That's really neat.

22:03.48
Justin
I mean, I'm prompting it, I'm prompting it to do so. And especially with our sessions app, that's something that you can do now as well, but it's not, that's not like an autopilot exclusive thing.

22:12.86
James
Yeah, sometimes people forget, like if you just tell it to do the thing, it'll go and do the thing.

22:17.27
Justin
Yeah.

22:17.46
James
Like if you just tell it to go create a, ja out cool I'll create work trees for you. Go. Do you, are you using it for like a single issue? Are you kind of rough looping it where you're like, Hey, i have this you know project. Go look at the repo, go through all the issues and do the thing fully and create work trees and do the, and just do it. Are you just kind of working on one thing at a time?

22:36.96
Justin
i'm I'm kind of doing one thing at a time and just doing multiple sessions of it and just being very hands-off. I think I could let it just take a look at the GitHub or our our VS Code our vco repo and just be like, I have all these issues assigned to me.

22:51.58
Justin
like Let's try to solve all of them. I think personally, i don't want shift bad code, so I do want to look to see what it's actually doing um at the end of the day and not just like accept just like randomly. so Unfortunately, it's not something I'd want to do yet, but it is definitely something you could try.

23:13.46
Justin
you could try um um um i might try it later on today and just say, like oh, this range of issues, I have a range of issues from the last week, let's just like take a look at all of these, see what is easy to fix, see what's not, and just like bump it onto one PR.

23:25.64
James
That's cool. Yeah, I've been ah i've been experimenting ah around with it a lot because we we track a lot of work in GitHub and we have a lot of different like project settings and we have a bunch of like... um like different requirements and like I need to like go grab like YouTube stats I need all this stuff and I find like I've created some skills to like go and say okay here's what I need you to do like for my backlog work tracking and I just say like let it rip and then it's gonna call and it's gonna run a bunch of like PowerShell scripts gonna run a bunch of this but it's kind of in this frame where it knows that it needs to just like only do these things And I found that super nifty because the auto-approved tools, maybe this a Daniel feedback, seems to be like really good where I can be like, oh yeah, run all the GH commands, like just go for go to town, right? Or just like go web request, ah go to town, right? For specific yeah URLs, like, oh yeah, it's fine to go look at getup.com or like, you know, Microsoft Learn documentation. But then there's other ones like for like, uh, PowerShell scripts. It's like, it's like every little, little indication without like running all. So I'm just like, okay, go for it. Right. And sometimes you, I think the other nice thing is sometimes at least for me, how I feel is like, I don't want to get in this pattern with the default of just always saying, yeah oh yeah, just approve that. Approve all, approve all just for the workspace and the workspace and the workspace. Cause then it feels like it's almost,

24:45.18
James
diminishing the point of the approvals because then you got to go manage going back. So I'm like, okay, I often do for this session. So that's kind of nice too that these are session based in general.

24:55.80
James
um This is really cool. I didn't know exactly how it worked. So it's kind of good because people are going to see this like, okay, how's this used on it? oh I guess if people want to give feedback, what's the best way for people give feedback on autopilot mode?

25:07.54
Justin
Yeah, yeah. I mean, Pierce and I have been posting on Twitter. We always get a bunch of feedback there. But the easiest way usually is just creating an issue on issue in the VS Code repo. um We'll definitely see it. I think a probably get auto assigned to me.

25:19.80
Justin
on But anything feedback related, whether you it's not looping the way it's supposed to or you don't really understand how it works. I mean, feel free. I'll chime in on the issue. But that's probably the best way to find us.

25:32.15
James
Very cool. Any final thing here, any hidden VS Code feature that people should know about that you use every day.

25:39.96
Justin
I mean, i would say i would say it's autopilot, but i will I'll talk about one other thing, and it's the sessions app that we've been working on um on the side. i don't i don't know how much of this is like super public and out there, but we've been iterating a lot on it, and it's just been really great to kind of dog food.

25:57.02
Justin
um ill it's basically just using CLI in the background and it's kind of cool to to use it and like not, it's more of like a no editor type tool and it's just been and a pretty cool thing to to try out and use on the side.

26:11.38
James
Very cool. Well, Justin, thank you for coming on and talking through this autopilot mode. If you haven't tried it out, go check it out. I've been using it like every single day. I really love it. so And we'll keep getting more updates, whatever is next in this in this world. I love it. And yeah, we have some some really cool stuff coming out from the team. You guys are crushing it. With these weekly releases too. So get up there. By the time this out, maybe it'll already be unstable. We'll see. Justin, thank you so much for coming on. I really appreciate it.

26:35.19
Justin
Yeah, thank you.

26:36.82
James
cool. Thanks everyone for tuning in to this VS Code Insiders podcast. Don't forget you can subscribe, like, of course, on the YouTube. We're on our own to 1 million YouTube subscribers. So check that out. There's a sweet 1M on the top of code.visualstudio.com. That's pretty sweet sub page. Go check that out. And also, of course, you could listen to us as well. You don't have to like watch me interview people all the time. You can just subscribe to the VS Code Insiders podcast on your favorite podcast application, Spotify, Apple Podcasts. Pocket Cast. That's my favorite. That's me though. That's going to do it for this vs Code Insiders podcast. So until next time, happy coding.


