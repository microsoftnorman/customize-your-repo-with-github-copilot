---
series: VS Code Insiders Podcast
episode: 13
title: "Beyond the Keynote: VS Code at GitHub Universe 2025"
url: https://www.vscodepodcast.com/13
transcript_url: https://media24.fireside.fm/file/fireside-images-2024/podcasts/transcripts/f/fc261209-0765-4b49-be13-c610671ae141/episodes/7/7e57fc08-eebc-4985-b31f-16473168d9a0/transcript.txt
audio_url: https://aphid.fireside.fm/d/1437767933/fc261209-0765-4b49-be13-c610671ae141/7e57fc08-eebc-4985-b31f-16473168d9a0.mp3
published: 2025-11-10
duration: 45:06
transcript_available: true
---

# Beyond the Keynote: VS Code at GitHub Universe 2025

This episode was sourced from the official VS Code Insiders Podcast site.

## Episode Summary

        What does it look like for VS Code to be an AI-native editor? How is it evolving with agents running locally in the editor, in a CLI, in the cloud, or even from other companies? Pierce breaks down every part of what was announced for VS Code at GitHub Universe and goes behind the scenes of his part of the keynote.

Follow VS Code:


X: https://x.com/code
Bluesky: https://bsky.app/profile/vscode.dev
YouTube: https://youtube.com/code
LinkedIn: https://www.linkedin.com/showcase/104107263
GitHub: https://github.com/microsoft/vscode

      

## Transcript Status
An official transcript was available on 2026-04-21.

## Full Transcript
00:00.56
James
Welcome back everyone to the VS Code Insiders podcast, the behind the scenes of your favorite code editor, Visual Studio Code. I'm your host today, James Montemagno and with me back.

00:11.28
James
It's been a while. Pure spoken.

00:12.42
Pierce
It has.

00:12.49
James
How's it going? like

00:12.79
Pierce
It's going good. I'm fighting the post-conference sickness that always inevitably happens to me whenever I attend a conference.

00:20.29
James
Yes. Besides the sickness, how was your GitHub universe?

00:23.39
Pierce
It was amazing. It was actually the first time I've ever been, which is a little surprising, but it's like, I'd always heard how this was like the most developer, developer conference of all time. um And I mean, keep it real, like I've been at Microsoft a while, I've been to the Microsoft events and sometimes they just can feel very like corporate-y and like they lose that developer feel. And the really cool thing, it's hard to explain about like what exactly makes this the case, but like everybody there as a developer is super passionate about developers and making it awesome, building cool stuff, like developer tools, all that stuff. And so I think the energy around the event was really, really cool.

01:00.76
Pierce
um The excitement around VS Code and GitHub Copilot and also all the improvements happening on GitHub.com as well. um So it was super cool. It's definitely like a a must do for me. And I think I'm definitely already marking my calendar for next year because I think they announced the dates. It's going to be the same week next year in 2026. I'll be there.

01:17.90
James
Yep. I will probably be there as well. Yes. It was my first universe as well, which was awesome. A huge, amazing, like a plethora of of folks and amazing backgrounds, just diversity of people, which was really cool to see.

01:28.57
Pierce
Yep.

01:29.26
James
And I was stuck in the awesome live coding booth, uh, the Microsoft VS code booth, but you for your first universe, wow. On stage keynote. What's up, man. oh wow

01:39.74
Pierce
I'm not really like I feel like all the other people in the keynote are like professional public speakers and I'm just like a guy who likes talking about VS Code. So that was a little bit of a different vibe for me. Like they were having to teach me like all the like keyboard Zoom things like that you probably are a pro at.

01:54.24
Pierce
um Like you should probably Zoom when you talk about that. I was like, oh, I always just kind of been like, this is what I do. And they're like, yeah, but you're you're public speaking, man. You can't do that. So um there was a lot of stuff like that that was kind of new for me because this this was really my first time ever doing anything like a keynote. But yeah,

02:10.14
Pierce
It's cool to kind of see how the sausage is made, like in terms of like the run up, like how it actually gets planned, how you do all the scripting and demos and all that stuff. And then like finally actually like seeing all the hard work of the team like displayed at the event um and trying to show that off in the best way possible. It's all super cool to see come to life.

02:28.86
James
Yeah, and it's super hard. It's it's like what people don't know is like you were there like a week and a half, like early, basically going through over and over again. You you have five minutes on stage to kind of show a bunch of stuff off.

02:39.64
James
And that's really hard, right? Like, because one, when you're prompting, and you're waiting for responses, like, you don't know how long it's going to take.

02:41.55
Pierce
It is.

02:46.08
James
Like, it's, you know, if GPT-5 mini or GPT-5 or some other model decides to go thinking, it's like, you I'm going to start thinking right now. You know, it's like, oh, God, I'll slow it down. You know what i mean Like, that is a while. So actually, like these...

02:58.43
James
keynotes, these demos, these sessions that we do become harder and harder, you know what I mean? And ah to see things live and do things live, but you did run some prompts and do some stuff.

03:03.62
Pierce
Yep.

03:05.86
James
But today what I want to do is you had five minutes on stage. We got time.

03:09.00
Pierce
Yep.

03:09.92
James
Well, not all the time, but we got time.

03:11.73
Pierce
Sometimes.

03:12.83
James
I want to unravel the keynote, like the behind the scenes, behind the keynote, because you talk through a lot of stuff.

03:17.78
Pierce
Check.

03:19.38
James
You know, we've had videos and stuff. We have a great blogs and stuff like that. I'll link to in the show notes, but like, actually want to go like deeper on stuff. And actually the first place that I want to start is Kyle was on stage and he said, vs Code is our AI native editor.

03:33.32
James
What does that actually mean

03:38.07
Pierce
So if you think about VS Code, it literally started as just the Monaco editor, right? And over time evolved to get kind of the extension host and extensions and more language support. And then we added remote support. And so like VS Code is kind of always just like the developer space constantly evolving to meet the needs of like what the community needs from us.

03:59.28
Pierce
um And I think it's very clear, like over the past couple of years that AI is the next evolution. Like we really deeply believe that it's going to, um, change how we work as developers and empower us to do even more and embrace this abundance mindset around building things in code.

04:13.66
Pierce
um And so like, I think when we talk about the AI editor, what we're really saying is like, no, like we're deeply thinking about for any new feature we're building, Like, how do we how does this actually fit in with all the AI stuff? So I'll give an example. Like, okay, now I'm using the agent much more, right?

04:31.55
Pierce
um So what are the consequences of that, right? So like, I'm going to have way more PRs, which means I'm going to have way more merge conflicts, okay? So like, what are we doing about that?

04:43.00
Pierce
um I'm also going to do way more code review. Okay, how do we make that better? And so you start to think about, and we'll talk about how some of that mindset also bleeds into the announcements at the keynote, but really like it's a mental state that you have to live in as the team and the product to really think about like, okay, what do we need to do if we are evolving into this AI editor?

05:00.82
Pierce
And then there's like the product truth behind that, right? Like over the last year, we've added agent mode, next edit suggestions, background agents, bring your own key, model choice, so many different features, and they're like really integrated deeply into the editor. like Not just the chat pane, but like if you go to Terminal, there's AI. If you go to the editor, there's AI. If you go to the source control view, there's AI to help you generate your commit message.

05:22.13
Pierce
um And then also kind of also true to our story, ah open source, right? um So making sure that um all of the AI functionality that we build inside the product is actually all available for the community to to kind of view and build on with us. so um That's always been a big part of our story.

05:39.55
Pierce
GitHub Copilot wasn't always open source in VS Code, and this year we've worked to make that true as well.

05:43.93
James
Yeah. And i think you just announced like a pretty, like I just saw on Twitter, Twitter acts thingy that but something else just happened in that space as well as it has to do the keynote, but what actually just happened in that space for the open source part.

05:49.62
Pierce
Yep.

05:56.31
Pierce
Yeah, so back in June, we open-sourced the GitHub Copilot chat extension, which powered pretty much all of the AI capabilities inside of VS Code outside of kind of where it all started with the ghost text completions where you hit tab and it completes your thought, which is crazy.

06:10.55
Pierce
That was like only a couple years ago because it feels like so long ago, but that's like the OG Copilot, right?

06:13.56
James
Yeah.

06:15.82
Pierce
um Where it all began. And so that was actually a separate extension. So if you install GitHub Copilot, you'll notice you have two extensions inside of VS Code, GitHub Copilot, GitHub Copilot chat. So now we're kind of taking all the functionality from the GitHub Copilot extension, bringing that into GitHub Copilot chat. So it's one extension and it's open source.

06:33.53
Pierce
But there's some other benefits, right? Like because there is two extensions, sometimes completions and next edit suggestions, which kind of also are AI powered suggestions in the editor, but they're kind of predicting your next thought. more so than finishing your current one, they would kind of fight.

06:46.92
Pierce
And you'd have situations where, okay, we're doing two requests, right? We're doing a completions request and an NES request. What wins, right? You have kind of all those things. And so it's also a step for us as we can move towards kind of one model, powering these things behind the scenes, one prompt.

07:01.06
Pierce
And hopefully that means faster and higher quality suggestions for you inside the editor.

07:05.28
James
Very cool. And I like how you kind of talked about how AI is kind of blending in, a but more naturally, right? Like you said, like, Hey, there's a box to enter the commit message, but also like you could just like have it auto complete or you're in the terminal, like you're doing natural stuff.

07:10.78
Pierce
Yep.

07:17.83
James
There's a bunch of completion. a bunch of auto stuff. There's a lot of things happening, but also. Maybe you don't have to run a command, just ask the command. like It's very natural, it's not directly, it's not taking over your editor. right it's like It's here naturally for you and ideally is evolving as the space evolves too.

07:34.24
James
like I think we'll talk about some of the things that is really nice, but where I'm coding nowadays isn't necessarily 100% in VS code. right like I literally, this podcast, I went onto GitHub, I saw there was an issue.

07:42.88
Pierce
Yeah.

07:47.58
James
I, uh, my MCP badge creator website, um, Frank, and I assigned it to copilot as some extra context. I watched in mission control and then I like open it in VS code. I'm doing testing and I'm iterating with it as well.

08:00.11
James
So it's like where I am working is, is now dave in more places than ever.

08:00.47
Pierce
yep

08:04.45
James
And i think you're kind of showing that in your demo. So i want to kind of set the stage. when you were thinking about what you wanted to show, right? Obviously, the there's a bajillion things that the team actually like shipped in Insiders.

08:16.33
James
and like ever like Even since the Universe, there's been a whole bunch of new stuff, too.

08:18.94
Pierce
Yeah. Yeah.

08:20.49
James
I open it up. i'm like I click a button. i'm like, that's new. Whoa. I tweeted, all you that's amazing. And Oren's always spoiling everything like on WordPress.

08:27.96
Pierce
Shout out to Oren.

08:27.99
James
Whoa. thats a X.com slash or in me, I think is like, ah is awesome. If you want, he I think he just like watches the commits in the open tier. To your point, everything that team is putting in is in there.

08:35.88
Pierce
Yeah.

08:38.36
James
So stuff that was in the keynote was already in the product.

08:39.16
Pierce
Exactly.

08:41.44
James
It's just some stuff you needed to figure out. So when you're thinking about what you wanted to show in the the story, how did you decide what story you wanted to tell? What was important about how like VS code has been evolving and and what just dropped?

08:54.17
James
Like, how did you come up with a story plan that fit into the bigger narration?

08:58.53
Pierce
Yeah, so I think like you you, know, unfortunately, unfortunately, I'm extremely online. The team is extremely online, right? Like we see all the the problems that come in, whether it's social media issues, you know, one-on-one conversations we have with developers or their teams. Like you start to see as as more and more people are adopting AI and in particularly agentic workflows, like the types of kind of things that start cropping up more as like, okay, now we have this. Now this is my new set of things to the point about evolution that I kind of have to struggle with as a developer.

09:31.16
Pierce
And so there was a couple of themes that really were coming up more and more. um So like there was this theme of like, how do I actually get good results from the agent? right like a lot of people will spend time iterating with the agent and you're just like so frustrated because you can't get what you want. And so that's like a common theme of like, well, how am I actually supposed to partner with this thing? How do I impart my special knowledge as a developer on the solution that the agent's building?

09:53.20
Pierce
So that's like a super common theme we hear a lot about. customization, like the built-in VS Code agent is amazing, but like it's certainly true that every team is different in how they work and their process and like what they like to see. And so we've always done a lot of customization work inside of VS Code, but in particular around agents, it's becoming more of a theme for us.

10:12.50
Pierce
um And then also kind of this theme of partnering with more agents um and in ah in different ways. To your point, like you're not always necessarily kicking off your coding task in VS Code, right?

10:24.36
Pierce
Maybe you're on GitHub.com, you notice something, you kick off a co-pilot task, then you're coming into VS Code and you're more in review mode, right? Review and run mode, like, I'm going to get feedback, to do the last mile work that this thing that I kicked off somewhere else is going. And so...

10:39.78
Pierce
kind of We kind of started with like what are the big problems that we think developers have, and then of course like match that to the story of how we think we're evolving VS Code to to meet those things. And it is really hard because there's, like you said, you have five minutes, right? Every word is really...

10:54.86
Pierce
heavily scrutinized. And you like I really want to show all the things that are happening with the team. To your point, but there's so much happening every single month in VS Code. It's hard to show it all, especially in five minutes.

11:06.30
Pierce
But like in terms of prioritizing the items we showed, those were the main areas we want to focus on. like What are the big problems that we're hearing from developers that they have right now? And then like how do we see like VS Code evolving to actually help developers with those problems?

11:18.50
James
And I think Kyle said it pretty good when he was talking about the AI native editor, how close the the GitHub and the co-pilot and the VS code team are working.

11:25.08
Pierce
Yep.

11:25.58
James
Because to your point, if I'm working with the agents be everywhere now, by the way, everything's an agent, right? If I'm working and I'm um working on GitHub.com and I'm assigning stuff and I'm pulling it down, like I need it to work the same, right?

11:31.74
Pierce
Mm-hmm.

11:40.05
James
If I have an agent, Like i have ah you know a C-sharp agent or a WinForms agent or a VEAT agent, right? That's like really specialized or a CSS agent. It's like, so I'm doing a super specialized css task.

11:51.58
James
I need to be able to go from online where background agents and things are running into my CLI or into my code editor. need it to work like a hundred percent of the same, right? And also and don't want to change context.

12:04.64
James
either. So I think to what you're saying is how are is developers working?

12:05.00
Pierce
yeah

12:08.54
James
Well, they're working in many places, but actually VS Code can also be the hub for those things as well. and that's what I want to kind of dig a little bit deeper into as we kind of go through your keynote. So you and the team and everyone, we're building this OctoCanvas thing.

12:20.64
James
You plug in your your username, you get a bunch of stats. I love stats. You get badges, you get trading cards, you get all these things. I love a big stats guy over here. I love stats.

12:29.44
Pierce
Classic engineer.

12:31.05
James
Love a good stat. um Love to fill the grid if you possibly can. ah So you started off and you said, I want to add some new features. So talk about three weeks ago, how you used to plan features and now how you plan features now.

12:39.92
Pierce
Yep.

12:45.21
James
And also like how this new feature of of this plan agent actually works, because it's the very first thing you talked about. We kind of had to go through it, right? Because planning takes time.

12:54.68
Pierce
Yeah. Yeah, so um i think this idea of planning is not necessarily new um We have a lot of um art already out in the community. Like our team has already been shipping something called SpecKit, which is like a really opinionated version of this workflow that has a lot more features.

13:15.46
Pierce
um But we we also have kind of been thinking about planning at different altitudes, right? Like SpecKit is really like, I'm planning my project and everything in it, all the features and like cascading all the way down to like, how do i actually build this thing?

13:28.71
Pierce
Then you have kind of what where plan mode sits, which is like, i already have like, So a somewhat like specified thing that I want to go do, I want to add this feature to VS Code or something like that.

13:39.50
Pierce
um I'm not like, I don't know what I want to build. Like i already have an idea, right? um But maybe I need help with the implementation details. And then we are, so it's not really, it's kind of planning. Like we have to-dos that we announced a couple um releases ago. And that's kind of within the actual conversation turn you have in chat of like, that is a plan plan.

13:57.68
Pierce
for based off what you prompted the agent to do in that turn. And so I think the thing we're missing was kind of what's the thing in between that super high level we're planning the whole you know product thing um and the like within the turn thing. And so...

14:11.69
Pierce
um This was where plan mode came in. um We actually, i think Harold and I did a build talk, which was like structured vibe coding. I don't remember the name of it or something like that, where we kind of like started talking about early explorations of this flow.

14:24.56
Pierce
um And so um ultimately like this kind of started as a custom mode ah that we had in the VS Code repo for planning, which our team uses to actually implement new features inside of Copilot. And then kind of by using that, you start to see other things you want, right?

14:39.81
Pierce
um One of which was like, planning is very ah tricky because there's a lot of context-heavy operations, right? Like, pretty much every planning session starts with research, right?

14:52.25
Pierce
How does, okay, the user wants to implement X feature. Well, obviously, i need to understand how the code works, right? And so you start by kind of gathering all of the the context. um That is very context-heavy.

15:03.14
Pierce
And the reason that matters is... Like typically, that would the way this would work um previously is i would if I wanted it to go find a bunch of files, it would find those files. And then that would just be attached. Like the whole file would be attached in your context.

15:15.99
Pierce
And then suddenly your context window just has, it's separate from the context window itself. It has a lot of things in there and not all of it is actually relevant for what the user said. right Only a subset is.

15:24.83
James
Yeah.

15:25.15
Pierce
And so we introduced this kind of idea of subagents, which is like, agent mode can basically go create another agent to do a super specialized thing that's very context heavy. And then that subagent returns back to the main thread, kind of the most important things.

15:38.59
Pierce
And so this enables us to keep all the context-heavy operations somewhere else, return only the most important information back to the main thread, which does two things. It keeps your response quality super high because you only have the most important context in there.

15:50.83
Pierce
And also it keeps you from filling your context window prematurely. So both of these things are good things. So that's also kind of part of plan mode and something as we explored planning more that we ran into. The other is like, the first version of the plan often is like, okay, but like, there's other things that you really need to to consider.

16:08.80
Pierce
um And so we really wanted to like explore this idea of, like okay, follow-up questions, basically. like Okay, the user tells me they want this, but have they thought about, after I looked at the code, these are these are the things you actually need to consider, right?

16:21.84
James
Yeah.

16:22.09
Pierce
um and then And then it's obvious, okay, i have my plan, now what? And so this was kind of this idea of handoffs of, like okay, maybe I want to pop this plan into the editor for further iteration, like as a Markdown file.

16:33.54
Pierce
We'll do some other things in the future where like you can... um like, basically interact with that more as an actual artifact inside of VS Code that's not just a Markdown file. So this is just kind of the first rev of this.

16:44.20
Pierce
um But the other benefit of that is you can check the plan into source control, right? um So that's kind of good if you really like your planning artifacts to be, like, under source control. um Or you can just pass to agents to start implementing. So, like, we also wanted, like, if we're going to have this notion of modes, like, the obvious thing that always happens is you're like well, now I have to change the mode.

17:01.91
Pierce
And that's kind of annoying. And so we we introduced this notion of handoffs inside of plan to kind of help me through that. So in the keynote, we planned ah this sharing feature so that those wallpapers you mentioned, we could actually basically share to social.

17:13.21
Pierce
And so it was kind of complex, actually, because there's really not actually a good way to share images, actually, to Twitter. And so kind of as part of the planning process with the agent, one thing that um came up is like, okay, well, we can actually use the Twitter intent kind of URL to open this up with some pre-canned text, but I actually can't attach an image.

17:34.62
Pierce
So then we had to kind of go through the plan and it was like, okay, now we need to actually convert the the image to base 64. We need to copy that to the user's clipboard. That needs to actually be posted. And so that was all things planned to mode that helped me to figure out in the keynote.

17:49.36
James
Yeah, we did a whole podcast with Bavia last week. So definitely go listen to that one as well to even deeper dive on the planning agent.

17:56.99
Pierce
Yep.

17:57.68
James
But I think what's really fascinating about it is like, like you said, I sort of was doing this a little bit previously, ah where I would go just like open up Copilot, like maybe like an ask mode, or I just go to like get up.com slash Copilot and like open my repo and say, Hey,

18:04.18
Pierce
Yep.

18:11.76
James
I want to do this thing. Like help me draft an issue. Like that's what, that that was my flow. Like help me draft an issue, an artifact, right? That was there. But now what I've noticed is that you said that it's grabbing this context and then being smart and asking me follow-up questions, which I really appreciate because It's like pretty smart.

18:30.58
Pierce
Yep.

18:31.03
James
Some of the models will keep asking you questions forever, basically. And so it's like, but it's also helpful because you don't have to answer all the questions or you can just like decide that this is good enough.

18:34.78
Pierce
Yep.

18:38.39
Pierce
Yep.

18:40.44
James
We'll figure it out later. But I want to talk about the sub but agents that you're talking about.

18:45.31
Pierce
ye yeah

18:47.03
James
Because what I've noticed is when I prompt it, all of a sudden I see this, I see like new indentation of things. It's like starting research. I see like instead of waiting, right?

18:56.18
Pierce
Yep.

18:56.25
James
Or thinking it's doing, so and then I see like a, what's happening there?

18:56.74
Pierce
Yep. Yep.

19:02.28
Pierce
So, uh, So what's happening, that's, a by the way, that's how you know that Flow is using a subagent right now in chat. If you see like, like a task, and then you see like a indentation, like a sub bullet, basically of things happening, like read this file or did this thing.

19:18.25
Pierce
um That's essentially using subagents. We might play with the UX a little bit to make it more obvious, but that's kind of how it works today. um But basically, what's happening is the main thread has been instructed to use a subagent for certain tasks.

19:29.19
Pierce
And so a subagent is just a tool, just like reading a file as a tool and other things. And so basically it will run the run subagent tool. It will say, your job is to, in the case of plan mode, to do this research, you need to do these things.

19:41.96
Pierce
So the the main agent will kind of draft ah dynamically a prompt for the subagent, send it off. Then basically everything that happens from then on out is in the subagent layer. So like in plan mode, that's mostly searching and reading files.

19:55.27
Pierce
um And so all that's happening in that sub-agent. And then when the sub-agent is satisfied, then it basically takes all that and it says, okay, this was actually the goal of like this whole thing, that the user originally started this with.

20:09.07
Pierce
Rather than just returning all the files that we came back with in this code-based search, like what's actually the important context, return that back to the main thread. So in some ways, it's like a function, right? like you You're like, function sub-agent, this is what the user's goal is, and then as a return thing, pass back all the important information, and that's essentially what's happening there.

20:19.54
James
Yeah.

20:25.80
Pierce
um You will get like a lot of reads coming in, and that's because ah we've recently done work to do parallel tool calling, which is pretty cool ah for the models that support it. So like, what We used to be like, read this file, read this file, read this file.

20:40.05
Pierce
Now it's like if the model found like five results simultaneously in its search, like whether that was a semantic search or regex search or a keyword-based search, it might say like, oh, these are the five files i need to look at.

20:51.29
Pierce
It will actually simultaneously in one tool call, go and read all those files. and then you'll just, boom, see them all stream into chat. So also, you know that makes searching faster. That's not really necessarily something restricted to subagents, but it is very helpful for the subagents flow as well.

21:06.93
James
That's cool. Yeah. And I noticed that, you know, when we talk about this, there's these, this newer concept, right? where We had agent mode now kind of these modes are transforming into like the agents themselves, right?

21:14.35
Pierce
Yeah.

21:18.42
James
Agents calling agents and like planning is kind of a mode, but it's also like an agent because it's, it's, it's, it it's thinking and operating in a different way.

21:23.32
Pierce
Yeah.

21:26.66
James
So kind of, we did a podcast with Burke a while ago about beast mode, but now it's really the beast agent.

21:27.58
Pierce
Yep.

21:31.73
Pierce
Yep.

21:32.50
James
so Everything's an agent, but these agents work across multiple places.

21:32.92
Pierce
Yep.

21:36.09
James
so You transition into like, hey, we've planned this thing out, but now I actually want to implement the thing.

21:40.51
Pierce
Yep.

21:43.02
James
and Then you actually use a different agent.

21:43.27
Pierce
Yep.

21:45.10
James
like You could have just, like you said, through handoff gone and said, let's start implementing this.

21:48.29
Pierce
Great.

21:48.34
James
Here's an artifact.

21:48.91
Pierce
Yeah.

21:49.42
James
But use a different agent. Let's talk about custom agents because that was the bigger thing. i don't know if people grokked it as much. It took me a little bit to actually going to Awesome Copilot, the GitHub repo, which I'll put in the show notes, and looking at the different agents that were available and understanding but they what they wanted.

21:56.23
Pierce
Yeah.

22:04.67
James
So can you explain this TDD agent, test-driven development agent? It's your madman over there doing tests.

22:10.28
Pierce
yeah

22:12.13
James
Um, although I literally just asked like for V tests to go create a bunch of tasks for my MCP thing. So I should have this agent I think is, is what I'm thinking, but how should developers think about this agent? How did you think about it in your flow and how's it changing how you develop and like, why, how is it different than this kind of custom modes that we used to have before?

22:30.83
Pierce
Yeah, so just at a high level, um like what is an agent, it right? um It's a good question.

22:37.65
James
Everything.

22:38.11
Pierce
like yeah and it Basically, like there's differing definitions out there, but I think everyone's largely aligned. like It is a prompt, it has a set of tools, and it has a model. And um like if you think about the difference between, what is the difference between the agent in VS Code and the agent in the Copilot CLI?

22:58.70
Pierce
Well, it has different prompts. um It has a different set of tools. Like VS Code is optimized to use the full tool set of VS Code and the full context of the editor obviously don't have that in the terminal. So it uses more terminal-based tools.

23:09.34
James
and

23:09.98
Pierce
So the tools are restricted, which is good and bad. um And they have different models that they use. um Now, in the case of Copilot, largely we try to make sure all the models are available everywhere, but you might have like different defaults and things like that depending on the modality you're working in.

23:25.03
Pierce
So then like if you extend that definition and you're like, okay, well, like, I want to do something like test-driven development. um Which, by the way, like I have always hated this. like i The test-driven development zealots out there, like I was just like, all right, I get it.

23:38.12
Pierce
like But and it is actually very important with AI because if you if you actually are doing a significant volume of AI-generated contributions... It's going to get very unwieldy for you to manually make sure that nothing is regressed in code review. And so it's kind of funny because some of the basic software engineering practices actually I feel like are more important and more noticeable with AI because they're they're like your checks and balances, right, if you're moving at a faster pace. And so tests are actually quite important.

24:03.89
Pierce
um And so i was like, okay, I want to do test-driven development. Now, I could have just prompted agent mode, I want you to do test-driven development. I want you to do these things. Well, in practice, the more you run through this flow, you'll realize, man, there's a lot of edge cases, right?

24:19.11
Pierce
I don't want you to... like Sometimes the agent would like ah try and implement the feature and then write the test, or it would write the test and then it would implement the feature, and then it would try to just fit the test to actually ah pass, even though it's not actually doing what I asked.

24:32.24
Pierce
and like

24:32.63
James
it's It's as if it's non-deterministic.

24:33.04
Pierce
so Yes, exactly. And so you realize actually this prompt, if I'm really like leaning on this as my workflow, I have to get super specific. So the prompt really becomes super unwieldy if you wanted to do this every single time, right?

24:47.14
Pierce
Then also the tools, right? um So in Test-Driven Development Agent, I have many built-in tools from VS Code. I have MCPs and extensions I've installed that give me more tools.

24:59.93
Pierce
Actually, you can get much better results with AI when you constrain the tool set that's available. um You can do this manually in HMO with the tool picker. But again, if I'm doing this repeatedly on my team, this is very difficult to go in and constantly ti toggle all the tools I want. And so in the case of TDD, it's like, okay, what do i need?

25:15.17
Pierce
I need to check for problems from the language service. I need to check the test runner. I need to be able to use the Playwright MCP. um I need to be able to read files. I need to be able to edit files. That's probably it. Like, I don't need the Jupyter tools. I don't need all these other things. And so the constraint is actually quite good for the agent's performance in terms of quality.

25:30.39
Pierce
um And so that's like another big component component. And then like, I played with a lot of different models and it's like, I think certain models are better at this test driven development flow. And so, Then it's for me, that was Sonnet 4.5. So I was like, all right, we'll use Sonnet 4.5.

25:43.74
Pierce
um And so that is kind of the definition of this test-driven development agent. But the cool thing is it's like a file, right? And so I can check it into my work ah check it into my repo, and it just lives alongside my code. So every developer on my team has access to the same agent.

25:57.67
Pierce
um this is another big reason you would create a custom agent. Sure, maybe Pierce can prompt this thing. Maybe I could change the tools. Maybe I could change the model every time. But like if I'm running a real engineering organization, that's not a scalable technique of like, please do all these things. like That's not how we do software engineering. We like repeatability, right? And so that's why we kind of really like this idea of defining your agent in a file.

26:19.19
Pierce
And that lives in your repository. And to your point earlier, we're trying to make sure that for a lot of these customers customization features that we build, they work everywhere. So if you build a custom agent in VS Code, that custom agent should work if you're using custom agents on GitHub.com. And so that was another big kind of part of this flow. It's like, no, we actually really believe in custom agents. And we think no matter where you are, we're GitHub and we're VS Code and Microsoft, like it should work no matter what service you're in, right?

26:43.00
Pierce
So that was another big motivation for us in this custom agents work workflow.

26:47.17
James
Yeah, that's super nice, especially when you're working with a custom agent, like in locally or then following up later, like sending off to a background cloud agent to be like, say, no, use the same exact agent, right? Like keep, keep it going there. I wrote a blog post. I'll put a link to it, but I have this.

27:04.80
James
app that I've coded, which is like a type back app. Cause I do a lot of demos and i write a lot of typos. Now I know the AI doesn't care, but it's not super professional when I typo every other word. Cause I'm trying to type fast.

27:15.67
James
So I wrote an app that basically just types back ah a thing that I give it. It could be a file. It could be just like tax site, use a control shift one and just like boom goes, but it's a wind forms app.

27:24.33
Pierce
That's

27:25.36
James
So do a lot of my demos on windows and, um, I, there's a custom wind forms agent, which is kind of bananas, but also like

27:33.37
Pierce
pretty cool.

27:34.39
James
It is huge. And like the actual engineering team, the Dun & Engineering team put it together to help build better WinForms apps.

27:40.20
Pierce
Yep.

27:42.06
James
Like it is aware of DPI. It's aware of light theme, dark theme. It's aware of all these best practices and layouts and the designer, which inherently like...

27:48.12
Pierce
Yep.

27:50.83
James
You know, it's making it aware of how designer files work behind the scenes. It's actually this huge custom agent. Like I get like way better results, but now I can go between all the things and work everywhere. Just go. And like you said, you can also use MCP servers as tools, right It's not just like the built-in tools, any, anything.

28:04.40
Pierce
Yep. yep Yeah, I mean, I think it's like one of those things. Like if you're listening to Insiders podcast, you're obviously like really into this space, right? And I think if you're not just a solo founder or developer working on your own thing, you're working with other people and it's likely that you all have differing levels of experience with AI.

28:22.46
Pierce
And so like, it I definitely don't want to undersell the point of like, it is very important that this is a way that you as a person on your team who's really into AI and understands how all this work can really make sure that your entire team is really doing really well with this thing. Because otherwise, like if you wanted to go and teach everyone how to prompt and do all TDD and all this the right way, that would be a lot of work.

28:45.08
Pierce
And you should still should probably do that. But like a good way to kind of enforce best practices on your team is stuff like this. It's like the new, like you know how, wait, I still do this. like You design CI pipelines and stuff to check for all the things you want. It's like another way that you can make sure that your engineering organization is doing the things you want.

29:02.21
Pierce
So I definitely encourage everyone who's listening to this like on your team to think about like how you work and like is it something that could be represented by a custom agent?

29:09.65
James
Yeah, that's a great way of thinking about it. And I think the other thing that I've been doing too, is as you're working, like, and things are doing good, you can always like have the AI, like help you build the custom agent for you or the prompt for you or the instructions for you. Like I do that a lot.

29:25.56
Pierce
Fun fact, that happened with the TDD agent.

29:25.63
James
Like, you know, no, nice.

29:28.14
Pierce
So the initial scaffolding for the TDD agent, had I actually prompted. I said, I want to build this TDD agent. Here's kind of how generally I want it to work. So it scaffolds out something. And it actually did really good.

29:38.39
Pierce
Like it it gave a prompt and it gave examples, which I wouldn't have done. It's like, here's an example of what the user wants.

29:41.93
James
I

29:43.19
Pierce
And here's example of what I want you to do if the user asks this. And that does really well when the AI starts to give examples like view shot prompting. And so like, yeah, using AI to to write the custom agent is actually a a really good protein Yep.

29:56.23
James
Yeah, that's awesome. Uh, and we talked a little bit about how these new custom agents are kind of working everywhere. We've talked a bit about how, you know, these, these new modes are really helping out and we have MCP everywhere as well, not only in the, in the editor, but also in the CLI and to get in a GitHub. And we've talked about all these things.

30:14.29
James
and And we had Josh and Bridget on oh quite a while ago, actually, when the kind of cloud agent, you or it was coding agent at the time, it's a cloud agent, which you know makes sense, it's in the cloud, it's happening, was starting to be integrated into VS Code.

30:17.88
Pierce
Yep.

30:28.28
James
But it feels like this moment that you talked about on stage of partnering closer with not just co-pilot, but with agents in general as a high-level term, right?

30:35.74
Pierce
Yep. Yep.

30:39.26
James
And I think this is important. verbiage and word selection is that the team thought about how could you make that experience better. so After you've sort of started to work and do things in the id IDE and and and in your code editors, you know there's a bunch of sessions happening everywhere.

30:59.08
Pierce
Yep.

30:59.99
James
So how is VS Code bringing it together into a unified space?

31:00.39
Pierce
yep

31:05.36
James
And how is it actually not just Copilot either? right Because like it's it's about agents, not necessarily about just Copilot.

31:13.86
Pierce
That's right. Yeah, I think like this goes back to like the thing we were talking about earlier about like when we think about features, like we think about like if this feature is successful, what are actually the consequences of that, right?

31:25.52
Pierce
and so like Admittedly, you don't always, especially not an AI, you can't perfectly predict things, but we listen to the community and like we try to reason about these things. And I think one thing that I didn't really fully anticipate is like, okay, when I was using, especially the local agent mode, right, um I'm mostly partnering synchronously with the agent, right? And so, yes, I want kind of, and we will add support for better multi-synchronous local chats. That's a thing we'll do. But generally, actually, when I'm in VS Code, I'm in agent mode and I'm partnering with it.

31:55.88
Pierce
I'm like, My job is watching watching that chat and making sure it's doing what I want. And so it it deserves my full attention. And so you know we didn't really notice this kind of pattern of like, oh, I have a lot of things I need to keep track of until you start thinking about background delegation, right?

32:10.32
James
Yeah.

32:10.54
Pierce
And that is where all this all started. we We built kind of this view to kind of, okay, we have these background tasks now. How do I actually see them all? And for me, actually, that's how I mostly work now. I start by kicking off a... but I might even do plan local.

32:24.33
Pierce
Then I kick off ah coding agent task on GitHub.com or from VS Code. um And then i actually like doing the last mile work. like If I've done the planning, then the cloud agent actually does a pretty good job.

32:36.98
Pierce
Then I go into review mode and I'm kind of making tweaks and things like that locally. So the way I partner with Copod has also changed inside of VS Code, at least for me. But the implication of that is now I suddenly have many more...

32:48.18
Pierce
threads. Because I think we're similar. We've talked both talked about it like a lot of how like I'll be on mobile and I'm like, I have this idea, like let me kick it off. Or you know like I'm in a meeting, let me quickly kick this off.

32:55.99
James
Yeah.

32:57.83
Pierce
And now we have Teams and Slack integration. Oh, I'm going to kick this off. But if you were to see like the amount of PRs I'm kicking off, it's a lot. right If I even have a half-decent idea, I'm kicking it off. right um And that can become very unwieldy at scale. right um And I think originally this was like overwhelming.

33:14.30
Pierce
It's like, okay, agents were supposed to make my life better. And did they just make it more complicated for more things for me to keep track of?

33:19.15
James
yeah

33:20.47
Pierce
Right. And so then it was like, Okay, what do we need for that? And I think it was very obvious we needed... It's been a long time since we added a new, like what I'll call, view primitive in VS Code of like, okay, you have the Explorer, you have source control.

33:33.87
Pierce
But it's like, okay, if we're an AI editor, if people are partnering more with agents, if you're going to have more of these things, it's kind of obvious that you need a place where you can kind of kick off, monitor, and review all of your chats no matter where they're from.

33:44.80
Pierce
So that was kind of the initial inspiration for Agent Sessions view, which is new inside of VS Code Insiders. so um And that's kind of like, it's got all your local chats. It's got ah all of your co-pilot coding agent, like cloud co-pilot tasks. It's got all your CLI tasks too. We now have CLI integration in there if you really like the CLI agent harness.

34:02.88
Pierce
um And so all those are integrated there. And then it was kind of obvious from talking to developers that like, VS Code has always also been about choice, right? Like, when you download VS Code, it's empty.

34:15.36
Pierce
but you You have to go and install themes, extensions, right, languages.

34:15.46
James
Yeah.

34:19.94
Pierce
um That's how VS Code works. um We recently did a bring your own key API. So extensions can contribute models to Copa. And it's like, okay, Like both from a VS Code and Copilot perspective, it's kind of obvious we really want to support like all of your agents, even if they're not from us in this view, right?

34:37.74
Pierce
um And so that was another big announcement is like we announced that Codex is available inside of this view as well. There is an API and we're kind of inviting more partners to build with us. It's not a super stable API, admittedly, because um we're still figuring out like the space is moving so quickly, exactly what we need.

34:53.19
Pierce
um But it is an API that's publicly available and Codex has built on that for for OpenAI. And so the idea is like no matter what agents you're partnering with, whether they're from Copilot or Microsoft or from, ah you know, third parties like OpenAI, like you should be able to see all those in one view.

35:08.46
Pierce
Just like you can when you install any other VS Code extension and it can you know supply views to different parts of the editor. um So that was like the first inspiration. The second was like, okay, like if we're already kind of saying, like I'm in VS Code, right?

35:22.76
Pierce
And I'm partnering with these agents. And especially like as more especially people more kind of power users have a lot of preferences of like, I like to use Codex for this thing, or I like to use Cloud Code for this thing, or I like to use Copilot for this thing. Like...

35:33.72
Pierce
Then you kind of get to this point, you like have a ridiculous amount of subscriptions. like I don't know if you're like, how many subscriptions you got, James? like My credit card people are like, are are you hacked? like Because I'm constantly signing up and canceling different subscriptions.

35:46.57
Pierce
um

35:47.96
James
You got to collect them all.

35:48.19
Pierce
Yes, you do have to collect them all. And so then kind of the obvious thing is like, hey, we provide inference via this thing called Copilot API that's already in GitHub Copilot. We already have kind of for business and enterprise, this like really nice observability layer with metrics and policies and things like that.

36:03.63
James
Thank you.

36:04.16
Pierce
if we're letting other agents play in this view, like wouldn't it also be cool if like that could all be centralized under my GitHub Colpod subscription too? And that's great for developers because then I get choice and it's great for like enterprises and people more kind of an IT role to have the observability of what's happening with all these agents no matter what you choose. And so the other really cool announcement is for ProPlus subscribers, you can actually use your GitHub Colpod subscription with OpenAI's codecs without having to sign up for like a separate chat GPT subscription. So that's really cool as well.

36:33.12
James
Yeah, it's pretty wild. Like ah some people were asking me like why, and I did a whole video about how why and how I use this different things. It kind of, like you said, it's about choice.

36:41.90
Pierce
yeah Love a button.

36:41.92
James
One of the things that's really fascinating is I actually, I do like to, I'm not a CLI person as many people know, listen this podcast or know me personally. love i love a button.

36:50.62
Pierce
Big button guy.

36:51.75
James
Give me a big button guy. love, give me buttons. I'm good to go toggles, dropdowns. I love a UI, big gooey guy, big gooey guy. And, but Scott Hanselman, my boss, is a big CLI fan.

37:03.70
James
And the one thing that's kind of bugged me about any CLI is if I want to start working, i have to like go and navigate to a folder. like That is just pure chaos. ah it's just like I know I can right-click open and turn but that's still too many too many buttons, like too many too many keystrokes wasted on navigating around.

37:22.50
James
So thing that's really fascinating in this agent session is the integrations of being able to open different things. And people may not know this, but one of the cool parts, Because even if you're just like, I love the CLI, I think VS Code is a better shell, if you will, for for the the the CLI because it gives you two options.

37:39.54
Pierce
yeah

37:40.81
James
It actually gives you a GUI option, and then it gives you ah a raw terminal option. However, it will open the terminal to where you're at. Like if you have a folder open, it opens there.

37:49.99
Pierce
ye

37:53.67
Pierce
Yeah, I think I totally forgot the point I was going to make. You were making it really? Oh, yes. um So ah like as you're talking, I'm also... like You're like, the VS Code is a natural place. We're talking about how how we work as changing with agents.

38:07.55
Pierce
like I think it's very interesting that... um Codex and Cloud Code both started as pure terminal experiences and then built VS Code extensions. And I think the reason for that is one, like people like the different viewports and how they partner with it.

38:20.29
Pierce
But I think also, just like with the Cloud Agent, still, like regardless of how your code is actually getting written, I like looking at my code in VS Code, seeing the diffs, I run my code in VS Code, I debug my code in VS Code, right?

38:34.19
Pierce
And so that's also kind of an obvious thing is like, even if my code is actually being written by the CLI, i still need to go to VS Code, right?

38:42.61
James
I need to see the code.

38:42.96
Pierce
And so, exactly. Yep. Like, we're not at the point where, as a developer, the code is, like, doesn't matter. Like, I don't think we're anywhere close to that, actually. um And so, like,

38:53.59
Pierce
Then if I'm spending a lot more time looking at code, running code, that sort of thing, then the obvious thing I have to do is go to the editor. And then it's quite awkward if those things aren't very tightly tied together. And so I think that is why like Codex and and Cloud Code built VS Code extensions ultimately. And that is why like also you kind of need something like agent sessions, right, for this exact task as well. So um yeah, it was kind of...

39:16.09
Pierce
I didn't really anticipate it when these terminals came out, these CLIs for different ah agents, but it's kind of obvious, right? Like, it's very rare that you would just be using a CLI and building an app and then like, oh, I'm never looking at the code, I'm never running this, and you know, like, that just seems unlikely to me, right? So it's kind of obvious that you would end up back in VS Code.

39:34.54
James
Yeah, it's super fun. And I do like both views. like And a good example of like what what I mean by GUI for the terminal is that you can just do a new one. It actually like gives you a chat box there and actually gives you ah a model dropdown.

39:44.76
Pierce
Yep.

39:46.29
James
So you can select things that you would normally run a command for. And I'll just run the commands for you. Or you can just say, give me the terminal. Here it is. Give me big terminal. Boom, I'm good to go. give me Give me that. I love that. I'm good to go. But they all show up on the left-hand side.

39:58.09
James
And like like you said, I've been i've been using this a lot.

39:58.20
Pierce
Yep. And you don't have to use them all, right? Like, use the ones that work for you.

40:01.39
James
Yeah. it's It's very true. It's like you're playing Pokemon. Listen, you're going to collect them all, but you're only going to put six in your in your and your starters, And you're actually only going to use like two of those. Let's just be honest.

40:11.61
Pierce
It's true.

40:12.53
James
We all just level up whatever's in the first slot in our Pokeballs. So anything else, know we've been talking for a long time, but I wanted to take this five minutes and extrapolate it out as much as I possibly could, just mostly because I like hanging out with you.

40:20.15
Pierce
yep

40:25.64
James
But anything else that people like really need to take away from not just this release, but from GitHub Universe and the direction that VS Code is going here?

40:37.20
Pierce
Yeah, I mean, I think ah in general, you can see like we're investing a lot in agents and kind of the implications of agents. There's more things we're working on in terms of code review and things like that that we're working on bringing into the editor.

40:48.69
Pierce
I did not talk a lot about um like ah the code AI code first workflow. We talked a lot about the prompt first workflow, but there's still like a lot of improvements happening there as well. Like I mentioned earlier, we open source the completions code for GitHub Copilot Chat.

41:03.60
Pierce
We've constantly been building, like, we don't really talk about it a lot. We should talk about it more, James. But, like, we're constantly building new custom models to power many of these features, right? um And so, like, also that experience continues to kind of level up as we're building new models that incorporate the latest capabilities, new data, etc., um that really are up-leveling the completions and next-edit suggestions experience, like,

41:27.20
Pierce
We're upgrading things like the code-based search like models that we have behind the scenes with Copilot embedding. So we have kind of a lot of things that, to your point earlier, like i got five minutes. What do i talk about? like But there's so many other things that I think are interesting about what's going on in VS Code. And I think the really cool thing is, like I said, like all this is actually driven by your feedback.

41:47.05
Pierce
um Like we listen. um If we don't, then you should let us know why we're not listening. But we we do listen. um i think I read every single tweet about VS Code every single day. Like the VS Code team is super responsive on GitHub issues.

42:00.20
Pierce
We read Reddit. Like...

42:01.87
James
Thank you.

42:01.94
Pierce
we're kind of all we're talking to developers one-on-one, so like if there's areas you'd like to see us invest more, like please hold us accountable. like That's the beauty of open source and kind of the way that the VS Code team works. and so um yeah We'll keep thinking about, kind of okay, what is the next implication of of of the work that we've done here and what do we need to go do? and um But yeah, i just wanted to kind of celebrate the community because it's also been like, I was reflecting because it's kind of the end of the year and at Microsoft it's like when we do our performance reviews and things like that. And It's kind of crazy, like just the last year of like what has happened with Copilot and even imagining, like someone tweeted like after Universe, like it's crazy to see like what happened in the last year with Copilot.

42:42.25
Pierce
And it's like, I even think about that for like the next week. like What will the next week look like?

42:45.84
James
Yeah.

42:47.65
Pierce
Because like a year ago, we barely had non-open AI models in the product. We didn't have agent mode. We didn't have next edit suggestions. like All the things that I actually use as my daily drivers in the product didn't exist.

42:59.15
Pierce
And this is kind of insane to say, right? But like then I also think about, well, this is like the velocity we've had over the last year. And now like where we have agents at our disposal, you know local and background, and were we're kind of really leaning into all this. like Where will we be in a month or two? like yeah It's crazy to think about, you know?

43:17.20
Pierce
um So I'm also like incredibly proud of like all the work the team has done over the last year to kind of go on this transition of like VS Code into an AI editor. um i think it's been really cool to see and it's been great to have the community like holding us accountable and giving us feedback along the way.

43:32.48
James
And not only just, uh, you know, giving feedback, but also like making pull requests, like it's open source.

43:36.30
Pierce
Yeah.

43:36.84
James
You're the PRs.

43:37.43
Pierce
Yep.

43:37.48
James
I, I, it's a spoiler alert. I like, I run a weekly query to find external contributors and send out sweet VS code swag. So like not saying it's a guarantee, but like, you know, I think it's super rad to see stuff come in and have the the conversation about it.

43:45.74
Pierce
There go.

43:51.22
James
So Pierce, thank you so much for coming on. and talking through the keynote in depth as well. um I really appreciate it because it's, you see it and you watch it for five minutes, but actually it's about a thousand other things and the mindset of of why that happens.

44:05.13
James
I'll put links to the keynote, put links to the release notes. I'll put links to everything that we talked about. I'm going to put chapters on this one since it is our longest podcast today. So you're saying, why not?

44:13.16
Pierce
Sorry, I like to talk.

44:14.10
James
No. All good. Well, thanks for coming on. i really appreciate it. And if you made it this far on the podcast, thank you so much for for listening and or watching. If you are watching this on YouTube, I want to remind everyone that you can only, of course, subscribe to the VS Code YouTube channel.

44:29.53
James
for awesome videos and live streams bunch of other stuff. But this is also an audio podcast. So if you're like, wow, this is cool. Like it's really great just to see James and Pierce's face and a few demos in between, but it would just be great to like, listen to my car ride.

44:41.50
James
You can take it on the go anytime. It's in every single podcast application, RSS feed, Spotify, Apple podcast, pocket cast, my favorite. anything that's out there, go to VS code podcast.com or just literally search VS code podcast, VS code insiders inside your podcast application today. Share it with your friends, like subscribe all stuff.

45:00.83
James
It's going to do it for this VS code insiders podcast until next time. Happy coding.


