---
series: VS Code Insiders Podcast
episode: 17
title: "VS Code - 2025 Wrapped with Burke Holland and Pierce Boggan"
url: https://www.vscodepodcast.com/17
transcript_url: https://media24.fireside.fm/file/fireside-images-2024/podcasts/transcripts/f/fc261209-0765-4b49-be13-c610671ae141/episodes/d/d7220a2a-d598-404c-a40b-f8dd4f032da8/transcript.txt
audio_url: https://aphid.fireside.fm/d/1437767933/fc261209-0765-4b49-be13-c610671ae141/d7220a2a-d598-404c-a40b-f8dd4f032da8.mp3
published: 2025-12-23
duration: 43:58
transcript_available: true
---

# VS Code - 2025 Wrapped with Burke Holland and Pierce Boggan

This episode was sourced from the official VS Code Insiders Podcast site.

## Episode Summary

        Burke and Pierce sit down to review a full year of releases, surprises, partnerships, and AI goodies in VS Code from 2025!

Follow VS Code:


X: https://x.com/code
Bluesky: https://bsky.app/profile/vscode.dev
YouTube: https://youtube.com/code
LinkedIn: https://www.linkedin.com/showcase/104107263
GitHub: https://github.com/microsoft/vscode
Special Guest: Burke Holland.
      

## Transcript Status
An official transcript was available on 2026-04-21.

## Full Transcript
episode17
===

[00:00:00] Um, what, why you like disappointing My drinks all the way down there. I left it down there. It says we're supposed to introduce ourselves. Oh, we are? Yeah, apparently. Okay, well let's do that. It says introduce this to themselves. Well, I'm Pierce. I'm on the VS code team and I'm Burke and I'm also on the VS code team.

And we are in. Huntsville, Alabama. Yeah. And, uh, we're gonna chat a little bit about what we've done this past year. Yeah. With Visual Studio code and copilot and AI and all those things. 'cause it's been a heck of a year that it has. Let's jump in. Let's start with, uh, let's roll the clock back. I was, I was thinking the way up here, it's 19th, 18th, last year, December, we released copilot free, which in my mind is like the, the moment that everything really started to accelerate and amp up for us.

Yeah, right about this time last year, right around this time last year. Yeah. Like normally at [00:01:00] Microsoft, December is a pretty slow time, right? People are getting ready for the holidays. Nobody's around. Yeah. This time last year we were shipping copilot free. That's right. Which is kind of insane that, that was a year ago.

But, um, yeah, I mean, um, I, I agree. That was like the first big announcement we had Universe last October, where we announced like we support multiple model providers now and not just open AI models. So we had anthropic. Jim and I. That's right. I remember. That's right. We had, we had copilot edits. There was a couple big moments at Universe and then there was kind of like a little bit of a pause while we kind of like collected ourselves and actually got all that out the door.

There was like co-pilot free in December and then that kind of like set the tone for the rest of the year. Yes, it did. And so coming off of, so we, we did co-pilot free in December and then we came back in January and we shipped almost immediately. Yeah. So February, early February we shipped two sort of big things.

The first one was, uh, copilot edits, ga, which we had previewed I think at, in October. So literally three months later we GAed it. Which GA [00:02:00] means just, it's like a Microsoft terminology for It's ready. Yeah. That's all it means. And then the other thing was next edit suggestion. Yeah. So let's talk about edits a little bit.

Yeah. So edits basically was, for me, the moment when. It was kind of in some ways a evolution of how I already was using AI to build apps, right? Like I would go to something like chat GBT or chat inside of VS code. I would say like, how do I do this? I would get a code snip and I would paste it back into my code.

It's crazy. We're at this place a year ago. Yeah, yeah. Then we have little buttons in there was that insert into file. Insert into file, and that was, it was, but it, it was in many ways a very profound shift, even though it seemed subtle at the time, which was like, I used to always go to the editor as my first way of like.

I am imparting my thoughts onto how this solution should work. And that was like a change of like, no, now I'm literally prompting and this is how I'm build. I'm starting to build applications now. At that time, it was very simple things, right? Like copilot edits. You had to reference specific files. It wasn't looking across your whole project automatically.

Very contained. Very contained, very like. And even I [00:03:00] remember them, people were like, oh, this is, this might be a little radical or, yeah, the vibe, we've gone too far. But that, but that was like, at the time, like that was very cutting edge and was a sign of things to come, but it was kind of a big shift in how we build applications.

Um, so yeah, I, I remember I was on paternity lead at that time and started trying edits and I was. Oh man, this is, this is pretty magical. I used it over Christmas break last year, and I was impressed. I built like, um, a small website. I think I redesigned my blog. Okay. But it's pretty limited. It's definitely limited.

Yeah. Um, and so I, you know, I was thinking, and this is around the time that people were like, well, AI's gonna take everybody's jobs in six months. And I was like, I can't even do that. I was like, there's, there's no way. The only way you'd say that is if you've never used these tools. But another really important tool that came out, which was more along the lines of what made Copilot famous to begin with.

Yeah. What Copilot really pioneered was ghost text. Yep. And then the next evolution of that was next edit suggestions was also dropped in early fe. Yeah, that's right. So like, um. [00:04:00] If like the ghost text code completions and the editor is like finishing your current thought. Okay. I start typing a line of code and our comment and yeah, I guess is what the rest of what I'm trying to type is and completes that thought like any s is really thinking about.

Okay. Based off what you're doing now and the context of this file, what is the next thing after the thing you're doing now that you want to do? So, okay, I have an idea of what that is. Where in the file would I actually need to place that edit? And then what would the content of that entity and so right.

That was also a pretty big moment in like how I actually partner with AI within the editor itself, because at that point I was still living very much. Although I was using things like edits, I was still very, like the editor was my primary driver of my Oh, code first. Code first, right. Which I think at that time, I think it's changed now, but I think at that time you had two camps of people.

Some people are like, I'll never use ai. That's right. And then some people are like, I'm using it. And then most of those people are mostly using completions. I think today. We may still have some holdouts that people are like, I don't use AI at all, but you have two camps. You have people who use completions [00:05:00] and next set of suggestions.

That's right. Completions being about writing code, you haven't written yet. Yeah. The next set of suggestions about editing code that you already have written without you even asking for that edit based on some other change you've made and then well, we're moving like along the spectrum you have edits and then what comes after that.

And what came after that was the same month. Yeah. I dunno if you remember this. Yeah. It was a late crazy February we previewed. Uh, agent mode. That's right. Yeah. So we ga edits in early Feb. Yeah. Can that be right? That is right. Yeah. And we previewed agent mode at the end of the month. Yeah. Yeah. So agent mode like, uh, was kind of like, it's kinda like you follow the same thread of like, okay, if I'm using natural language's, looking at files, I specify.

Okay. How could the agent look at all of my files? How could it do other things that are not just editing? Right? That's kind of essentially what the agent is. It, I mean it, it is very fancy, but it at the same time, it's quite simple. It's okay. You have a prompt, [00:06:00] you tell and that prompt, this is what I want you to do.

This is what the user's asking, and here's a set of tools you have access to that you can do other things. The AI can say, I wanna use these tools to do certain things like search your code base. Mm-hmm. It returns that back to us. We have programmatic things we've written in client inside of VS. Code to go search for code base.

Right. Um, and then, okay, we get out edits from that and then we pass that back to the agent. It's just a loop. Right? Right. And it now it can choose the next action based off the context it has. And so like from that perspective, it's like quite simple. But it was another one of these kind of profound moments of like, I don't even think we necessarily realized how big it was at the time and how much it would change everything is when we introduced Hm.

OI mean. I was super skeptical about it. Yep. Just because that just seemed like a terrible idea right off the rip. Uh, because remember the models that we had back then too. I think we were, I think we had, what were the models? We had some four. One, maybe four. One four. Sonet, SONET, three, five, maybe question marks around that [00:07:00] time.

I don't remember, but I just do, I do remember just thinking like, these models can write code, but the code is not great and I don't know if this is a great idea. Yeah, just being honest. That was my thinking around age MO, but that was not the only thing we released. At the end of February, which was huge.

Yeah. Because now we have this autonomous thing that can actually do very complex SaaS. Yeah. Check its output, uh, auto heal. Yeah. Right. But then we also, we ga custom instructions, which that's another thing that feels like it's been around forever, but I guess it's not. Late February was custom instructions and, um.

Oh, and also terminal suggestions. We've done a lot of work on terminal. We should talk about that in a minute. But yeah, custom instructions. Yeah, I think, well, custom instructions were already in the product, but they really, in my opinion, became way more important with the agent, right? Because you want AI to work how you and your team work, and at least with the editor, you're still kind of, not that you're not in control with the hm, but you're literally dictating every single line of code that's happening, right?

Um, and so you have a lot more opportunity [00:08:00] for intervention and I think. As you kind of, you're the way you partner with AI shifts with the agent. It's very critical that it works in the same way you and your team do. And so instructions, again, a very simple concept. It's basically a prompt that you attach to every other prompt that's on like some additional context you want the AI to know, but.

We see in practice, like we have offline evals and things like that. Even very simplistic instructions of like, this is what type of project it is, here is the layout. It can improve the output of the code that you get from models, and it also can improve the latency of the overall time it takes to get back what you want.

Because if you're telling the AI hints basically. Has to, it may be able to figure it out just with grab. Right. Or if you're telling it to look here, like then it's gonna look much quicker. Right? Yeah. Even stuff as simple as this is how you start the project in dev mode. Yeah. It can figure that out. Yeah.

But that's less work. It has to do faster. Agent turns more accurate agents, and as you're using this over many, many, many hours, days, weeks, months. Right. And also I [00:09:00] think another critical thing with all the customization features is I think we all on every team, even extremely AI first teams like ours.

There's a spectrum of like how advanced people are in their partnership with ai, and I think the really cool thing about things like instructions is it's a way for you to basically skill like your entire team up on how to use this thing because you don't have to be a prompt master, right? You can help to bake some of those things over to the default per person who likes to do that.

Can do that. Right. And people who don't wanna write prompts or the person on your team who knows. Even if everyone knew great about ai, there's probably a couple of you on your team who are like I, I'm the one person on this team who understands how this whole system works. Yeah. Like documenting that in once and putting it in your instructions.

Like it's not even just your scaling yourself and the agent, you're scaling every single person that repository. 'cause that instruction lives in your repo about how. To partner with AI and you, you're just upleveling your entire team. Yeah. So it's very simple but also very profound. Okay, so that wraps up February and then early March.

Yep. [00:10:00] M-C-P-M-C-P, which was huge. And that lands in agent mode. Actually a ton of stuff happens in March. Let's start with MCP because that's like a huge moment just in the industry in general. Yeah, so, you know, I, I kind of introduced this concept of tools and those were all things that we had kind of built into VS code.

And at that point we had fewer tools, but we had like code-based search making, edits those sorts, checking the linter for errors, right. Those sorts of things all existed. Um, but it was kind of obvious at that point that there was things you wanted to do and it was like, really? Are we gonna have to bake every single one of these into VS code to the point about making the agent work like you and your team do?

And so while there had been kind of some attempts, like there had been plugins from chat GBT, um, there had been some other kind of initiatives like this. MCP was really the first one that leaned into kind of the H intake workflow. And really like, again, something that was big at the time, but even in retrospect is bigger now, which is basically like you can make the agent do whatever you want by bringing these additional tools, right.

Making it, [00:11:00] letting the agent basically decide to use those tools. So like I know every single project I'm working on, I'm using the GitHub, MCP, I'm using playwright, right? Chrome Dev Tools cp. That's a good one. There's a couple ones that I'm just using on pretty much every project I'm working on. I use context seven context, context seven, adding more context, right?

So yeah, like I think even if we were shipping a ridiculous amount of things that the agent could do as a built in thing, there would always be a long tail of tasks that weren't possible. So MCP really unlocks that by allowing you to bring your own tools to the agent. Yeah, that was huge. And then the other thing we released in March, that was huge, which a lot of people still don't know about today.

Yeah. Is BYOK or bring your own key? Yes. Essentially means you can use your own model local, maybe it's a Google model, maybe it's open router, maybe it's a, our friends at Cereus, right? Yep. Yeah. So like, um. You know, there was a couple people who were like, I just want, you know, Chad to talk directly to my imprints.

And so that was kind of a common customer quest around that time. But then there was still kind of like big [00:12:00] model players, but you were starting to see more models like this long tail of either open source or other models kind of come out on the market. And it was like we wanted people to be able to use those in copilot.

Obviously there's real engineering work to bring those things into copilot itself, right? It's make them good, right? Because test, it's not just like, oh, the model is an API. We call that in co-pilot. There's a lot of work that goes into shipping great models in the product. We can't do that. So though the way we support this long tail is bring your own key.

And so to this day, like, you know, sometimes when like one of these big new models drops the open source models, deep seeq, whatever it may be, you know, I mean, bring your own key. I'm trying to see how's this thing work with agent load and what's the results get? Also the benchmarks can be a little gamey, right?

So like you don't always know until you try and so. Ring your own key is, is a very popular feature and it's not even just for individuals. We're starting to see a lot more teams using it. Yeah, I hear it a lot. People are always like, I wanna use my own model With copilot. You can, you can, it's just go to go to your model picker and then what is it?

Manage models. Manage models and then there's a whole configuration experience. I mean, there's a lot of people who like [00:13:00] are in very specialized domains who are fine tuning their, their A model over their code base, like they have their own domain specifically or whatever. Right. Yeah. Great. Use that in copilot.

Bring your own key two more things in March. Yeah. This could take forever. This dude, this can be the hour and a half podcast. Sorry. Chat. Chat modes. Chat modes showed up, which are now called custom agents. Yes. But chat modes. Yes. Yeah. So, um, we noticed that there was like workflows that people would, would try to use the agent for.

And again, to the point about like you could just prompt this every single time, it's not very ergonomic to do that. And also scaling the best practices across how your team, you and your team work. Like we really needed a good way to kind of. Formalize that. And so we created this chat mode, which is unlike a prompt, we'll get to prompt files in a second, but like, it's more of a persistent kind of way of working.

It's not like a specific one time action, which is more of a prompt. And so, um, like that could be, I'm doing security work. That could be, I am, uh, doing code [00:14:00] review and people were basically creating chat modes for each of these things. And that was kind of another big custom, like we, we introduced agent mode, then we start adding, okay, now you can customize tools.

Okay, now you can add custom instructions. Okay. Now you can add modes. And so we're starting to layer on more functionality onto that base agent as we go through the year. Yeah. And people always ask, what is the difference between custom instructions and prom files and custom agents or custom modes? And the answer is, it's just different ways to build workflows.

Right? Yeah. They're all just different ways of adding, uh, additional instructions to the agent. That's right. They're all similar, essentially doing very similar things, but they have different used cases. Yeah. And so we're just trying to provide you with all the building blocks that you need to build.

Okay, so we had talk chat modes and then notebook editing, notebook editing. So like, um, you know, as a developer before joining VS. Code, like we all have our language stacks we live in. And for me at the time I was living much less kind of in the data science world, much more now, but like I didn't realize how many people are doing data science and vs code.

It is a ridiculous number. Yeah, it's, [00:15:00] yeah. And so Jupyter notebooks are obviously like the foundational element in this space. And so, um, we basically made it such that the agent can do agentic data science with Jupyter notebooks. So you can basically say like, I want you to do this, uh, explore this, add a graph for this.

And you know, it can modify the notebook and the cells and look at the output of the cells very similar to actual code in the outputs of code. To basically build out notebooks. And this is how, like how the VS code team works. We have a ton of Jupyter notebooks for different things. Like that's true Bug triage.

That is literally a Jupyter Notebook that has been written by AI over APIs. It's a GitHub, GitHub issues notebook. Right? It's a GitHub issues notebook. Yeah. I have, you know, I have, people don't know you can do that. They don't know you can do that. And there's, even if you're, if you're using something like, uh, you know, uh, Azure Monitor or things like that.

There's really cool things you can do with like telemetry. You can be like, oh, I really wish, like we could pivot this with this. And you're like, I don't know the syntax of custo. Like, please help me figure this out. Ai. So with like data analysis task, now literally you can just be like, I need to figure this out.

[00:16:00] Please help me. And if you give it the right context and can do that. Now this gets us through. We're only to March. We we're three months in. We made it one fourth of the 30 minutes reliving. Yeah. Alright. That was, so that was March. So let's talk about April. And April. We get sort of two big things. Prompt files or reusable prompts.

Yep. And, uh, multi window support for chat editors. So I'll start with prompt files. So I, I, this is what I have regrets about in a way that maybe you're not gonna anticipate, which is, I wish we had called them slash commands. 'cause that's actually how you use them in the product. Yeah. And like the amount of people who are like, why can't I do slash commands?

And you're like, you literally can't. You can't. Yeah. But. Essentially, I mean, it does describe what it is. It is literally a file that contains a prompt and you can invoke it with a slash command. There's also a little play icon and similar to the modes, you see people kind of doing these workflows again and again and it's annoying having to type that every time they get a prompt file.

Now I wrote one on your team can go and do that. Yeah. The other one that gets me is when people are [00:17:00] like, I wanna be able to attach like context, like I wanna, it's like you can just use the hash symbol and you can attach anything, but they're looking for the at symbol. A little inside baseball. Like we actually discussed this exact one in our UX call this last week.

'cause I was like, I feel like the every editor but us has kind of converts on the, on the ads on that. And we're like holding out with the hashtag. This is one of the, uh, maybe the downsides is doing these first. Is that. Exactly. People standardize on other things. Yeah. But let's talk about multi window support.

Yeah. For, because used to be chat was confined to the sidebars. That's right. And then we made it so you could use it in the, you had pop 'em out into the editors. Yeah. So we saw people starting to experiment more with, like, I am not always partnering 100% synchronously with the agent. I, I wanna fire off multiple tasks at once.

I wanna be looking into multiple things at once. So that was kind of like the first moment where that was really starting to become a thing. And so it's like, well, why would you ever need to pop something out? I'm always staring at the agent while it [00:18:00] works. It's like, well, no, like. Now I'm starting to kind of delegate a little bit more.

So you start to see the delegation workflow starting to come more into the product with this. Yeah, definitely. So that was, that brings us through April. Yep. And so then we hit May. Yep. And in May, uh, let's see here. There's so much, I mean, this is where we started really starts to just kind of blow out. We have the MP NCP auth was implemented, which prior to that I don't think there was built an auth.

It was basically just like, yeah, it was very Yo spin the thing up. Yeah. Yeah. There was a lot of yo lowing this year. Um, but that was good because then like you could reach into systems that required authentication and you could do so securely. So that opened up a whole new generation of tools that you could bring in, which was really nice.

Right, because before like the GitHub NCP server would run locally. Yep. And then it was, now it runs by a URL. Yeah. Uses and shout out to Tyler for all his work on Oz. Yeah. Great job Tools were grouped and managed. So we were, I approving the grouping of tools in the, um, in the [00:19:00] tool picker for MCP started adding more and more tools.

Right. Like it wasn't a problem before. 'cause we didn't have that many tools. And now you got MCP, you got, yeah. Uh, basically a tool for every surface inside of S code. Correct. It gets a little unmanageable. So we had to clean it up. Got unwieldy quickly. And then, um, the cloud agent shows up. Is that, is that right Nate?

That's right. Yeah. That was one of the big. Microsoft build announcements last year. Oh, that's right. Um, yeah, so that was a big one because it was like, okay, now like going back to the like, how do I partner with this thing? It was all synchronous, then it was like kind of synchronous and local, and then this was like the first time you really have like.

I'm gonna kick something off. It may not be perfect, right? But it's, it's getting an initial stab at what I want to do and that's happening in the background that I'm pulling that into vs code and doing more work on it. And that was like another big work workflow shift for me, um, where I was like starting to kick off way more cloud tasks, like way more cloud tasks.

Um, and to the point that that's now actually my primary workflow. Yeah. Oh really? You're a big fan of the cloud agent. [00:20:00] I am like overwhelmingly I'll, we'll get to planning in a second, but I'll plan stuff. I'll be like, I am happy with this 'cause I want to agree on the plan upfront. Then I kick, I kick to the agent and I'm just letting that thing cook.

And then it's not that I think it's like, okay, I'm gonna merge this right away. It's like, okay, well that thing's, literally doing stuff while I'm doing other things. I'm parallelizing myself and then I'm pulling it into VS code and sometimes that needs tweaks or last mile work. I'm doing that inside of VS code.

That's kind of like now how I'm partnering with agents inside of the product. And so this was like the first moment where that started to kind of become a thing. Yeah, I remember that. And one of the things about the cloud agent that, because I do remember doing this at Build with the demos that we built, was the, the how it's worked into the PR workflow.

So it just follows the natural GI workflow, which is already there, which I thought was great. And then I learned from you sort of the value of delegating things to the cloud agent and being like, I, you know, at the time I would be like, um, redesign this landing page. Yeah. [00:21:00] Give me 10 different designs.

Yeah, I want 10. And then I'll just pick the best, the one that I want, right? So I would open like, or you gimme 10, or I would just be firing off a bunch of prs and I would just close the ones I didn't want and keep the ones I did, which is called abundance it. And I started doing much a lot more of this.

Abu Abundance is really like, I mean, it's kind of like a buzzword, but like I, I really do think that AI enable. Abundance and you really, a lot of teams that I talk to are still very much, I call it AI 1.0 of like I used to do X thing. We can speed it up with AI and Y way. Actually like the, and that yes, you should do that, right?

But then the really cool thing is like to the variance idea of like, I don't have to like, be like, oh, I don't like this design and keep iterating, keep it. Just gimme 10 designs and like I'll pick the one that works best. Right? Yeah. That is a, that is a workflow that was never practical for you to do before.

It is now possible. It's, I think it just feels really wasteful to everyone. Right? Like even the other night I did a refactor and the thing like I, it, I think it did 4,000 something lines and [00:22:00] I wasn't happy with the refactor. I just threw the whole thing away. Yeah. The fact that you would, someone would write 4,000 lines of code that would just be thrown away.

Just feels morally wrong. Yeah, yeah, yeah. But that's not the world we live in anymore. It's not, yeah. I think it's actually the workflow you're talking about is very interesting because now with ai, I used to do this thing where like I would prompt, okay, maybe I don't have the best prompt, it's not the most specified and it doesn't quite gimme what I want.

And then you kind of do this thing where you just like keep kind of prodding it to get what you want. I don't even do that anymore. I am very much like, if I don't get what I want, use for the most part, right. Start over. Yeah. It, it is almost always actually cheaper. It doesn't feel this way, right? It feels very like, oh, I just wasted my time.

But it's actually cheaper from your time perspective to go back just reprompt with a stronger prompt. It's actually just do it again. Do it again. But now with the background agent, you can basically do that process, but in the background at scale, right now, what I, I don't do that, but what I will do is sometimes, like if I see it going and I'm like, oh no, no, no.

I forgot to tell something, I'll stop. [00:23:00] And I'll say, I'm gonna stop you right there. Yep. And then I'll provide you extra context and then just let it continue on. Yep. And it seems to do just fine with that. Now that was cloud agent may build tools are grouped and manage, but we made another huge announcement in May.

Yeah. That didn't actually drop until June, but it was a huge announcement. Ad build, co-pilot chat is Open source. Open source. We open source it, we open source GitHub copilot. Yeah. And I mean, I think we talked a little bit about this, but this is the insider's pod, so I'll let you inside like. I think it was always very, you know, everyone who works on VS Code believes deeply in open source and working in the open.

And I think it was always kind of a bit of a contradiction for us that like, it's like, okay, yeah, vs code is open source, but like our work around copilot isn't. And that was increasingly becoming more and more of what we're spending time on. 'cause that was the area where everything is changing is the developers.

So we obviously spend our time there and I think like. It was kind of eating us, right? Because we're all people who really believe in open source. And so I think separate from, you know, all the other benefits we highlight on in our blog post, it's [00:24:00] like, I think for our team, just as people and like the values we have, we want it to be working in the open.

And so it's like a huge moment for us that we brought it up, it, it felt right when we finally were able to be like, this is what we're working on, this is how we work. And I know also for me, like I always see. You and I both are like always getting looped into like internet conspiracies. I'll get a co-pilot, but it's cool for me because it's basically our full-time job.

It's our full-time job responding conspiracy theories. But like it is cool that like when someone's like, oh, I bet they're prompting it to do this crazy thing. It's like, well literally you can go in and you can see exactly how the product works. Yeah. And it's all out there and that's good or bad. Right?

But like. That's the value system that we wanna work in and that we believe made VS code successful. And that's what we think will make Copilot Chat successful, is working in the open with all of you and the community to make this thing a success. Right? Yeah, exactly that. So that was super exciting. Um, it was huge for the team.

It was a very energizing moment for, it was everyone because it felt like we were returning to what we do. Yeah. Right. It's a return to roots moment. Return to roots. Yeah, exactly. Now the other thing that we got in [00:25:00] June was, um, so Daniel who works on the terminal, his favorite thing. Auto approving terminal commands.

Just not Daniel's clear. Daniel doesn't like this at all. I don't think this auto, this idea that you can have the terminal, you just say auto approve and it will just execute things in the terminal, you know, without bothering you. Daniel wants you to be safe and has put a, an allow list that he would please like you to use.

Yeah, I think it's like one of those things of like. We've been talking about a lot about how we work shifts and like some of our assumptions and like what we're comfortable with and what we're not. It's depends a lot for me on like what I'm working on specifically. Like I, my comfort level doing things like YOLO mode on my personal project that's backed by GI and all this other stuff on my personal computer.

I'm just like, I am actually very comfortable with that idea. Um, but I, there's other projects where it's like, I, I think I should be more careful. And I think especially if you have tools that touch your infrastructure, that's where things can really go awry. Yeah, right. Then it's like, oh, well it delete, I, you know, [00:26:00] you see this Twitter thread, this didn't happen with GitHub profile.

It's like, delete it by database. It's like, well, yeah, I mean, when you, when you're moving into this, I just trust it to do its thing kind of environment. That's a risk you take, right? Um, so yeah, like it's also kind of starting to highlight the security of these workflows and how different people are thinking about different parts of how we secure the agent.

And I think for us it was always. Still to this day is we want to keep you in the loop as a default. Mm-hmm. And we want you to be in control of what happens on your machine. You're the developer you know best. And so that is reflected in our defaults. Auto approve is still not on by default, which a lot of people complain about and think we don't have.

As a result, it's still there. But I think actually the way we solve this, which we're working on now, is, is sandboxing. Right? Like sandboxing, the terminal commands. So they can't do steering, which by the way, you can do this today in code spaces. Yes. If you use GitHub code spaces. You are sandbox. In fact, I believe it's a relatively safe place for you to turn on auto approve [00:27:00] and do yolo.

I don't think many bad things can happen. Brooke and I are not security experts, but I feel pretty confident you're running in a container, right? We cannot give financial advice, but you are in a container. That's the ideal environment. The other thing that we got was, um, delegating to the, to the cloud agent from video code, which we have the ability to.

I don't think you could start a cloud agent session, but you could interact with it once you started it on GitHub, but then now you could just like take a chat session FROMS code and from VS code to delegated it to the cloud. That's right. I mean, and as a developer, I live in VS code and not that I have any problems going to github.com, but like it's just good to keep me in the flow and that was a nice improvement there.

That was huge. Now what, what, what month do you think we're at, by the way? Uh, are we to December yet? No, it's, it's July. It's July, and by the way, this is such a reflection. Like all this stuff is a reflection of how many hours the team, the engineering team Yeah. Our team has, has put into this and how just [00:28:00] incredible it was, the velocity of which they've been able to ship.

Because remember, they're still building core editor features. At the same time and it in across multiple platforms. Yes. And like there's other, you know, other products building on top of VS. Code and choosing us as a foundation. Like all of that is real engineering work has to happen from our team. So like one of the things that we shipped in July, that's a really good example of this that enables a lot in other editors that build on top of us is work tree support.

Yeah. So like we shipped work tree support in Visual Studio Code, which enables the background agents that we have today. Exactly. And that whole ecosystem, but also. Check chat checkpoints and rollbacks, which was, I use this all the time. That's insane. Huge. I, I shot, I think Justin worked on this. Yeah.

Justin from our engineering team worked on this, like, yeah, like we had kind of this like undo redo, but it, it was getting kind of messy because it would undo like literally the last thing they LM did. But like you're getting to the point now where the agent can work for more than like. 30 seconds at a time, right.

It can work [00:29:00] for minutes, even tens of minutes, and in some cases much longer. And so like, it's like, oh, well, just spanning the button was getting unwieldy. But this actually using, get behind the scenes, it's, it's creating like a, basically a ton of STEs of, of your code. It works so well. It works. I use, I use checkpoints all the time, or just going up and editing the message and it, and then when you edit it and send it, it's like, Hey, everything from this point on is gonna get blown away.

Are you cool with that? I'm like, yeah. That's totally fine. Huge quality of life improvement, Connor, with the virtual tool sets, which was also huge. Connor works on the N CCP tools. Yep. Virtual tools, because before you, like you said, you'd have all these N CCP tools and I think GitHub alone had a hundred and it was like 80 something tools and the limit.

For passing these tools is 120 eighth to these models. And so we would have to say, you'd try to send a chat. It would be like, you have more than 128 tools select to try again. And so they introduced virtual tool sets? Yep, yep. That's right. Yeah. There was some improvements to basically like, you know, [00:30:00] continuing this theme of, okay, I have more and more tools.

How do we manage this? And there's like a UX challenge there of like. Okay. It's kinda an unwieldy, like having to go and uncheck. I wanna, I'm okay with these getup things and I'm okay with these Azure things, but then like you start a new chat and it's not there anymore and like, so fixing that problem, but also like kind of starting to think more about how do we solve this like problem of 128 tool limit in a world where you're working with more and more tools and you don't want people to have to manually go in and check all the tools.

Very tedious. Every single time. Yeah. No, this time around I won playwright August. Auto mode agents, MD and migrating work trees. I think auto Mode and agents, MD are probably the two biggest things here. Thoughts? Yeah. So, uh, at this point we're starting to ship multiple models every single month from all the providers.

It's getting overwhelming and so we were hearing a lot of feedback like, can you just help us to pick a better model? And so, uh, we introduced auto mode, which is like. Still something that's very much a work in progress and we're trying to make better every single month. But [00:31:00] we basically looked at some of the top performing models in our product and we said, okay, like.

Can we look at that and also, which models tend to be fastest and have the lowest amount of problems infrastructure wise, put those in there with a, uh, you know, a defined model mix and essentially like route to route to the best set of models within the product. And so this was kind of the initial inspiration product mode.

You get a 10% discount if you use this thing, um, on your premium request, which is super cool. And kind of in the future, the way this is going is like. Imagine you say Update this markdown file to have this text, right? You don't need Opus for that as much as you Burke might wanna like inflate his like usage just by using Opus for this show, your boss, you're using more ai.

Um, it's not very efficient. It takes longer, right? You should be using a small model for that. So this is kind of the direction we're going is like we're also taking doing out task complexity, which is pretty cool. Agents, md like I think one really cool thing about VS code that's may be underappreciated is just the amount of which we've adopted these open standards this year.

Right? Right. And you know, we [00:32:00] talked about MCP agents, MD is kind of the, why do we have literally a markdown file in all of these products? That is basically the same thing of providing custom instructions, right? And so this was us adopting that inside of the product as well. Oh, and also shout out to, uh, to David Kramer from Century.

Yep. Who was the one on Twitter who was like, Hey, uh, the instructions file situation's, getting outta control. Yep. And I was like, cool, bro, could you open an issue? And he opened an issue. Yeah. And that actually, that issue kind of kicked that off. And so. Thanks, David. All right. Uh, September. This is ridiculous.

Do we, did we do all this unified notifications plan mode, open AI codex integration, subagents, MCP, gallery and handling merge conflicts with ai? Yeah, so I think, uh, plan mode with, sorry. Hold on. Plan. Well, one, go ahead. You're killing me, man. Uh, plan mode was like. Uh, I think something that was already representative of how a lot of us worked right on the team is like we would, [00:33:00] we would kind of like informally do some like lightweight planning and then pass to the agent, and we found that it was really like improving the quality of outputs we get when we're building GitHub, goput and VS code with ai.

And so it was one of those of like, it kind of just makes sense that it should be built into the product. And so that was kind of like our first real exploration into being super opinionated about like. We think this is a way that you should be partnering with AI and something that's working for us, because I think, again, even on teams where people are very advanced with ai, you know, you're only gonna, it's like garbage and garbage out.

If you're not prompting well, you're not gonna get good results. And so the, the planning process is really helping you to basically construct a really impressive prompt, right, to give something like Opus, which as you said, that's even getting powerful enough. It can go figure out stuff on its own to go and actually solve your problem.

So plan mode was huge. Um. Subagents were kind of another big one in the agent kind of space because essentially we were noticing like there's this problem of [00:34:00] context bloat. And as the agent does more and is capable of more, it uses more context. And one of the challenges with that is as you use more context, the code quality you actually get from the agent decreases, right?

Degrades. And there's a couple of really like kind of. Context, heavy tasks that happen basically at the beginning of every single agent session, like gathering context. And really, there's only a subset of that context is actually necessary for what you said, right? And so. Subagent is basically, could we take all that spin a, a subagent from the main agent, agent, basically do all that, return the most important stuff from that thread back to the main agent.

And then basically you have this really clean, low context, um, that you're maintaining in the main agent. And that's the goal is basically that this is gonna give you way higher quality results. Subagent is huge. It's something that I use all the time. I to the folks that like, uh, interact with us on Reddit.

We love you so much and we know that you're very concerned about the context windows. We see this all the time. Um, but it, it is true that larger context, windows [00:35:00] degrade model performance significantly, not just in accuracy but also in speed. And so subagent, you should use them liberally because. They, uh, redo, they have isolated context windows, and they stop that from happening, right?

They, instead of having these monolithic chat threads where you're, by the time it says summarizing chat, it's, it's too late. But, but, but when we do summarize chat, we also replace your chat history with that summary, so we are kind of resetting the content. The MCP gallery was huge. This is something that we did with philanthropic Yes, too, because we had all of these people that stood up, these great, um, MCP registries.

It was tons of 'em, and they were great. Uh, but there was no real one place to go get them. We wanted to be able you to be able to install them from VS Code or any editor. That's right. From like an extensions gallery view, which you can now do. The one we announced in October at AT Universe, which I was on at a little bit of fomo, was the open AI Codex integration.

Yeah. So I, you know, again, it's like kind of a return to roots moment. VS Code and [00:36:00] GitHub have always been a developer platform, right? Like VS code literally is just an editor and you have to add stuff to it to get it to be whatever you want, right? GitHub also has a very extensible platform, and so a kind of trend we were noticing is like people were really enjoying using multiple agent harnesses.

There are certain agents that are better at certain things, and so at that time, the Codex team, we were talking with a lot and we were like. Be really cool to have Codex inside of, inside of VS Code one, um, and natively integrated. Um, so that was kind of like, uh, the first talking point, but then also, um, a, a trend we were seeing is like people wanna experiment with multiple agents, but they still want kind of that.

Centralized observability metrics, all that you get from GitHub platform and GitHub copilot, and without having to have like 40 AI subscriptions, right? Like, so, um, that's kind of where this like concept of like h and hq, which we announced at GitHub Universe came in and also VS code, the Codex integration, which is kind of like the main integration that highlights this today, where you can sign into open AI Codex agent, [00:37:00] not GitHub copilot, but with your GitHub copilot subscription.

Use that inside of VS. Code, right. As a natively integrated thing. No new subscription required. No new subscription required. And so this is super cool. 'cause like now, like basically GitHub co-pilot becomes like your ai dev tool subscription and you can go and try out, of course, the built in AI experiences we have in the product, but also agents like Codex.

Yeah. You get to use the a, uh, the, uh, agent that you want and then in November. So coming right off of that, we had background agents. Yep. Which was built on the work tree work that was done before. So this new unified agent's view where you can see local agents, cloud agents, background agents, codex, what other, and, and you could even install other agents in the future.

You can be install other agents via extensions. You can easily delegate between agents. So you could plan locally and then hand that off to the cloud. Exactly right. You can just. Uh, sort of like mid operation there, delegate to others. And then another huge thing that [00:38:00] we just shipped, in fact, we just, I think we just announced it yesterday, was.

Agent skills or quad Quad skills now called agent skills available now in vision skills. That's right, yeah. And again, another example of us partnering with others in the industry and adopting standards. And so that's the really cool thing if you're using VS code and GitHub copilot and there's standards emerging elsewhere in the ecosystem, like you will have access to those things inside of our product.

So we're gonna follow those and. We can't forget a year of models. Claude Sonnet four and four. Five Opus four and four five. Can't forget the GPT five launch. The GPTs. Yeah, the GPTs. Uh, five one. Now we're at five two. Yes. Uh, GPT five mini GPT five Codex Rock fast one. I mean, you worked on these model launches.

I don't think people know. They don't understand what goes on behind the scenes. Yeah. For us to just tweet out and be like, available today. Yeah. There's a lot of work that happens from a ton of teams across VS Code and GitHub to get these [00:39:00] models out. Um, it's not just literally like, oh, like we call it, I mean, in some ways it is as simple as you call an api, but it's actually not.

Because really to, by making a model available in GitHub copilot, we want it to be a great experience. So this process starts happening weeks before we actually ship a model. We start working with our model partner friends. They say we have a model, um, here's what we're noticing about it. Here's some general guidance on how to integrate the model in terms of prompts and tools.

So we start doing that. We have a whole offline evaluation suite that we run. Yeah. So we're constantly trying different prompt tweaks and things like that. We're sending feedback back to the model partners. Then all of that kind of culminates in shipping the model on day one. But then there's also like a whole feedback loop that happens after where we're running experiments, we're talking again with the model partners on like how we can make these models even better.

So there's an optimization loop that happens once we have a lot more people like, yeah, like the people on Reddit, the people on X and, and GitHub issues were saying. I noticed this kind of like weird behavior with this model, like with GBD five two was like it's stopping early. Yeah. [00:40:00] It's we, and we love that like when requests are, when requests are failing and you're posting that to Reddit.

We love that. Yeah, we love that because it, we need to know that so we can go back and look at the services, see what's happening with the upstream providers. There's a lot going on behind the scenes with these. Yeah, that's right. Like, but behind all these launches, there's a team of scientists working on the evals.

There's people working on prompts and tools. There's infrastructure people, right? So there's, there's a ton of folks that really make that, to your point, like that very seemingly simple tweet of like, we now have this pro, this model inside of GitHub copilot. Actually a thing, but yeah, like if you ever notice weird behaviors, that's why it's so important for you to like let us know.

Because a lot of these things, like even if it's not immediately obvious how you fix, I mean they are still LLMs, right? They sometimes have do weird things. Yeah. We have. Our model partner friends that we partner with closely, not just OpenAI, but Anthropic, Google, XAI and all those folks are also super smart and we put our heads together and try to figure out how to make the models.

Awesome. I wonder people know that we're sort of on the phone with these folks prior to these model launches, working very [00:41:00] closely with them to, to make sure that things work well for you. But the time we tweet it out, say it's on the product, it's not like we just turn a flag on for in the Mac. And so that is essentially your wrap of the last 12 months.

Lemme just tell you. We're barely gonna make it. The sun is now fully, I'm leaning into your, we're down. One of our mics is broke. And what an incredible year though. I mean, intense for you. For me, right? Yeah. I mean, I think like you called it out, like I just really wanna highlight all of the work of everyone on the team.

Like when, I mean, it's like a cliche to say everyone gave 110%, but that really was how this past year was, and all of us like. All of us care so much, right? Like Burke and I often will like text and it's like sometimes it like physically like causes us problems when something is not quite right and we want something to be better and that is the level of like care we have about this thing.

And so we're all working our butts off to try and build the best product possible. I think it's reflected in the. Just the year [00:42:00] that VS. Code and GitHub copilot had like hundred percent. I mean, we barely could get through this pod in a reasonable amount of time and we cut out so many things. Right. We didn't even talk about a lot of work.

Oh yeah. There's so much stuff we have, we view that as like. A massive reason that we were able to do all this. Like you're constantly challenging us to think bigger, try new things, reporting issues, holding us accountable, giving us encouragement. You know, that's all super important to us and that's what made VS code great.

And that's what we think is making GitHub co-pilot great too. So I definitely wanna shout out to community. Yeah, we appreciate that. So keep those comments coming. You can find Pierce on X. Find me there. You can find us on Reddit. We're there? Yes. Um, but we just wanna say thank you to all those who. Sent us feedback even if it was critical feedback.

Yep. To those who used copilot and really enjoyed it. Those who were on this ride with us, there's so many to name, you know, some names come to mind, like I think of Oren, I think of. Eleanor, I think of, uh, Stan, I think of Par. There's so many folks. Um, so we just are [00:43:00] extremely grateful for y'all. Uh, that's the reason why I think that kept us going.

It did. Yeah. I mean, it's, I mean, not to get too personal, but like. I have enormous respect for anyone working in ai. This thing will challenge you like no other. The space is moving so fast and so yeah, like we really appreciate the community. Like you guys are a huge reason that like keeps us going every single day.

We, we, your tweets, your Reddit threads, all that, all bank sway into the VS code Slack. Oh yeah. Our, you see it all, our whole bridge though is like, we share it good and bad and so yeah, like we've loved being on this journey with you over the last year and like just reflecting on like. The product change that has happened in the last year, how much better the models are.

Uh, 2026 is gonna be a wild ride too. Absolutely. Alright, y'all, that is a wrap for you for 2020. Is it 2025 still? Is it? It is, yeah. What a year. We'll see you again next year if we've come this far in 12 months. Yep. Where will we be a year from now? Thanks y'all. Bye. Thank you.


