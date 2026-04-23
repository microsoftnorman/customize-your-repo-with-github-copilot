---
video_id: R9KSJ0Vfy8I
title: "GitHub Copilot Cloud Coding Agent: A Beginner's Guide & Model Showdown"
url: https://www.youtube.com/watch?v=R9KSJ0Vfy8I
channel: "@JamesMontemagno"
published: 2025-12-31
speakers:
  - James Montemagno
topics:
  - cloud-agents
  - coding-agents
  - model-selection
  - productivity
relevance: primary
---

# GitHub Copilot Cloud Coding Agent: A Beginner's Guide & Model Showdown

James Montemagno introduces GitHub Copilot cloud coding agents, showing setup, background execution, and model comparisons for day-to-day workflows.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Introduction: The Power of Coding Agents |
| 00:22 | Embracing Cloud Agents for Productivity |
| 01:37 | Setting Up Cloud Agents |
| 02:18 | Exploring Cloud Agent Capabilities |
| 09:11 | Building a Pet-Friendly Locations Website |
| 12:20 | Comparing Different Models |

## Key Topics Covered

- **Cloud agents**
- **Background execution**
- **Model comparison**
- **Productivity workflows**

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] The last year has been a journey and a whirlwind with coding agents.
[0:00:04] Every single day I'm booting up a Visual Studio or VS Code and I'm getting more work done than ever in my entire life.
[0:00:11] Thanks to these amazing models and the coding agents that are built directly into the code editors and IDEs that I use every single day.
[0:00:17] I use GitHub co-pilot and VS Code non-stop. I'm getting so much done.
[0:00:22] But there's been a new way that I've actually been leveraging agents, which is Cloud agents, getting work done in the cloud in the background while I sleep.
[0:00:31] So I wake up and have beautiful PRs ready to go.
[0:00:34] Now, this has transformed how I work as a local and local background agents work locally and they're very eager.
[0:00:39] They want to get things done fast.
[0:00:41] But Cloud agents enable me to code anytime, sort of whenever I have an idea.
[0:00:46] So I could be at the airport, I could be driving to work, I could be getting a coffee, I boot up the GitHub mobile app,
[0:00:51] I create a task, I sign it to Cloud agent and boom, I'm good to go.
[0:00:55] I may be signing off for the day from work, might be inside a VS Code, might be halfway through a task that I'm working on and boom, delegate the rest of it to the Cloud agent.
[0:01:04] And at any time I go to any of my repos whenever I have ideas, spin up a new task or assign an issue directly to GitHub co-pilot and I am good to go.
[0:01:12] So Cloud agents have completely transformed how I work, which means that I can just work all the time and I can get this done while I sleep while I'm taking a shower.
[0:01:20] I want to make you my morning coffee.
[0:01:22] So when I get to the desk and I'm ready to go, I have a bunch of code that's ready for me to review.
[0:01:26] So I love it.
[0:01:27] I absolutely love it whenever I get a bug report, I get something in, sign it to the Cloud agent and I'm good to go.
[0:01:32] It allows me to focus on the task that I want to when I'm inside a VS or VS code.
[0:01:36] So if you're brand new to Cloud agents, I want to kind of walk through kind of like how you get them set up, but I really want to show off some of the power because now with GitHub co-pilot, you can actually use different models when assigning different tasks to the Cloud agent.
[0:01:45] So I wanted to break down and redo my simple sort of pet application and assign it to the different models and see how the different Cloud agents work.
[0:01:59] So I'm going to walk through some of the things that I've been doing with Cloud agents and then go and break down all three of these different PRs that have opened for me.
[0:02:06] So let's get into it.
[0:02:07] Okay, so let's first talk about the Cloud agents.
[0:02:20] So if you go to get up to a com slash co-pilot, you can ask kind of co-pilot about anything.
[0:02:25] Just kind of like a normal assistant.
[0:02:27] You can add repository, file spaces.
[0:02:29] This is a normal chat.
[0:02:30] You can click on this task to do slash task and then you can then select a repo.
[0:02:35] You can select branches and then also sub agents that are configured.
[0:02:39] So you might have different experts like a blazer expert or a front end expert or CSX expert that you're assigning these agent tasks to.
[0:02:47] And then you can go ahead and like give it. So there's some suggestions here.
[0:02:50] Now I actually like to come over to this tasks and then you can go ahead and pick the repo.
[0:02:55] You can go and do the same exact thing and use all your current agent sessions that are here.
[0:02:59] And then you can also if you're a pro pro plus I'm pretty sure that to check the features double check there.
[0:03:04] It's normally auto but you can select GPT 5 1 codecs max on a 4 5 or Opus 4 5 as well with different multipliers.
[0:03:11] So assign the different tasks off to you can also go to any GitHub repo like I am here.
[0:03:16] And you can actually see this little new agent session button or up here agents panel.
[0:03:20] You can basically see it from like all over the place.
[0:03:23] So you can go ahead and do that too.
[0:03:24] And you can just go and spin up the same UI for this repo.
[0:03:27] You can additionally come over to any issue.
[0:03:30] For example, if you had an issue, you could then tap on it and then you could assign it to co pilot as well, which is really cool.
[0:03:35] So you could do that.
[0:03:36] So as I example here, let's say John has this thing here.
[0:03:39] He's at this page analysis.
[0:03:40] Let's assign it to co pilot.
[0:03:42] And then here I could give it additional context.
[0:03:45] I could say auto whatever I wanted to do.
[0:03:47] That should be fine.
[0:03:48] I'm going to assign it off.
[0:03:49] So if I create a task here or if I assign an issue, what is going to happen next is one of two things.
[0:03:57] If it's an issue, it's going to create a pull request and link it to this issue.
[0:04:01] If I just create a task, it'll just create a pull request and get to work.
[0:04:04] So we can see here we have co pilot getting to work and it's coming up and it's showing me, hey, here's your original prompt.
[0:04:11] Here's what you're given, which was the actual issue.
[0:04:14] And then it's going to get to work for me.
[0:04:16] If we scroll down, the first thing it's going to do is come with an initial plan and assign this off.
[0:04:21] So this is going to kind of get to work.
[0:04:23] And at any time, I could steer it as well.
[0:04:25] So I could act co pilot to make changes to the pull request once it finishes.
[0:04:30] I can do anything else to it.
[0:04:32] And we can see here that now co pilot has started working.
[0:04:35] And we'll see this that it's in draft and a work in progress.
[0:04:38] And that'll get updated when it's done.
[0:04:40] So if you do this session, I go, then go into this other view basically, which is me reviewing and seeing this work happened in real time.
[0:04:48] And what's cool is that I can see this on GitHub.com, but I can also see it inside of VS code.
[0:04:52] And we'll take a look at this here.
[0:04:54] So here is this kind of steering.
[0:04:56] So if I am watching it and I'm understanding what's going on, I can then steer it in a certain direction.
[0:05:01] It's going to get to work.
[0:05:02] It's installing MCP servers and it's just going to go to town.
[0:05:05] It'll update this along the way with code files that have changed as well.
[0:05:09] So we can see the automotive selected clubs on M45.
[0:05:11] So I can watch that as well.
[0:05:13] So the automotive is picking the best one and most readily available model at the time there.
[0:05:19] So I can see this.
[0:05:20] And then at any time, I could go back to the pull request too.
[0:05:23] So let's actually talk about how I use this every single day.
[0:05:28] So that's one example.
[0:05:29] Right.
[0:05:30] If you actually go into pull request here for feedback flow, you can see that I am in real time, almost assigning different tasks to get up co pilot anytime.
[0:05:38] So you can see all of these here, right?
[0:05:40] So you can see it all happened here.
[0:05:42] You know, basically if there was an issue linked to it, or if it was just me assigning a task to it.
[0:05:47] So if I come in over here and say, okay, I want to add, you know, these different options, I can see that I merge this in.
[0:05:53] I could then scroll down, see the files change.
[0:05:56] It writes a beautiful summary of everything that's happening here even before and afters and benefits.
[0:06:01] And I can still dive into that session to understand exactly what was happening with that different tasks.
[0:06:07] So I can see all the different views and things that it was doing all the different tool calls along the way, which is really, really cool.
[0:06:13] So that was me building out feedback flow.
[0:06:15] And this is my feedback analysis application that I built this entire year, 100% with GitHub co pilot and visual studio and VS code and the cloud agent that takes in any URL and does product feedback analysis and a lot more.
[0:06:28] Another app that I built out that I want to kind of show to is trim tally.
[0:06:32] So this is a new mobile application that I built for iOS that allows you to do private secure weight tracking.
[0:06:38] I'm on a journey in 2026 to get down to an ideal weight.
[0:06:42] So you can kind of see this here.
[0:06:43] So this was 100% this website was built with it.
[0:06:47] And if you click on the app store, the mobile application was also built with it 100% as well, which is really cool.
[0:06:53] So you get it all there.
[0:06:54] If we go into that repo, you'll see the same thing.
[0:06:57] When I go into pull request and I look at closed, you're going to see that a vast majority of things that are happening here are either between the website or things that I'm assigning off to co pilot here to do.
[0:07:08] And you see that many of these are not linked if any to an issue.
[0:07:11] So this is just me spinning up tasks, going to town and doing that there, which is really, really cool.
[0:07:17] Okay.
[0:07:18] So from inside of VS code, you can pretty much do all the exact same things.
[0:07:22] Here I have my simple pet application open, which is a place or web assembly app that I use in a lot of my videos like I talked about.
[0:07:28] And here I have my standard agent view that's going on here.
[0:07:33] So if I wanted to, I could come in and I don't know, let me just like highlight this program.
[0:07:38] So I could say at workspace, explain.
[0:07:41] And then I could go ahead and ask it to explain.
[0:07:44] So here what I'm doing is I'm doing a local session here, right?
[0:07:47] So this is understanding what this is doing inside of here.
[0:07:50] If I came up over in created a new chat, I could use that same exact agent.
[0:07:56] I could delegate in a few different ways.
[0:07:58] I could say, let's do an SEO analysis of this website.
[0:08:03] So here I could fire it off.
[0:08:05] I could select of course different models.
[0:08:07] I could also come in and just hit enter and that'll just do the same exact thing that I just did.
[0:08:13] So I could just hit enter and then it's going to be a little delegate button.
[0:08:15] And that allows me to continue in the background, which is going to be running locally on my machine,
[0:08:19] either in the current workspace with the CLI or on a work tree, which is another branch base that's up and running,
[0:08:25] or a cloud agent that is for all intents and purposes,
[0:08:27] exact same things.
[0:08:28] So it's going to allow me to fire that off just like that.
[0:08:32] Now the other thing I can do is I can come into this new and I can do new chat,
[0:08:36] but I can also do new background agent, which is specific to the background agent task.
[0:08:41] So I can do different models and then do work tree or workspace.
[0:08:44] And then also I can come in and say new cloud agent.
[0:08:47] And now we can see the icon updates because I'm using an agent here to go and do the SEO analysis of the website.
[0:08:53] So I'm able to do that exactly the same as we saw before.
[0:08:57] Now you can also see all of the different sessions here.
[0:09:01] So let me go ahead and just filter these down and just turn off background and codecs and things like that.
[0:09:06] So we just see the ones that are going on here.
[0:09:09] So we can see that I have three different ones.
[0:09:11] So what I wanted to do is put the cloud agent to work to say,
[0:09:14] can I have it build this entire website and the PRD from scratch for me and test out the different models.
[0:09:20] So I had this idea and this is the idea.
[0:09:22] So a website that allows pet owners to find pet friendly locations, kind of like meet up at Yelp and go to town.
[0:09:27] So if I head over into my browser again, here is the prompt that I gave it.
[0:09:32] So this is one of these sessions here.
[0:09:34] So I said, I want you to create a PRD and I want you to put it in a PR.md file in the route implement mock data, build out the entire website, use blazer and see our best practices.
[0:09:47] I want light theme, dark theme, pink, cues, nice fonts, headers, footers.
[0:09:51] I want the pages to be responsive here.
[0:09:54] I want it to be, you know, all the key landing pages and features to be highlighted.
[0:10:00] And then I've given it some photos as well to work on here.
[0:10:03] So I ran this three times.
[0:10:05] So we can see here I have GPT 5-1 codecs here and I can see the summarization of everything that's doing.
[0:10:10] I can take a look at the files that have changed here, which is really cool.
[0:10:14] I've also did the same exact prompt just from the getup.com with Claude sonnet 4.5.
[0:10:20] And here we have one session, premium requests.
[0:10:23] And then I did another one here with Claude Opus 4.5.
[0:10:27] So I did it all three of the same exact prompts from the same boilerplate file new project.
[0:10:33] So if I come back over here and I just run this thing, I will show you that besides just some images that I put in.
[0:10:40] It just says hello world.
[0:10:41] So nothing fancy going on there.
[0:10:43] Right? So if I come back over, we can see that I have some images, so pets and cats and dogs and venues.
[0:10:48] So it should be smart about understanding like what is going on there.
[0:10:51] So what's really neat is that I could, let me go ahead and take some of this down.
[0:10:55] Because I could tap on any of these.
[0:10:57] So here, for example, this is going to be the Opus one.
[0:11:01] So I tap on that.
[0:11:02] It's going to load it up directly inside here for me.
[0:11:06] So I can see that I can see the same exact overview from the cloud agent, the prompt, everything like that, the PRD here too.
[0:11:14] And what I love about this is that I can actually scroll the files changed.
[0:11:18] And I can tap on them to see the PRD, the files changed in real time here.
[0:11:23] So I can just browse it without having to jump around different contexts.
[0:11:26] I can see everything that's going on here, the before and after.
[0:11:29] So if I want to look at that program, see how I can see everything that happened here and the diff that it added for the mock data service, for example.
[0:11:36] So I go in there.
[0:11:38] I can also type back.
[0:11:39] So if I didn't like something, I can delegate a task back to the cloud agent.
[0:11:43] I can do pound here to add different things.
[0:11:46] I can add files to it.
[0:11:48] And I can steer it back just like I did over on get up.
[0:11:52] I'm also able to hover over this and actually open the changes to see all the changes, apply the changes locally here to my current branch.
[0:12:00] And I can also check it out too.
[0:12:02] So I can do that for any of these, which is cool.
[0:12:04] Now you can see that I have this in progress one working here, which is kind of cool.
[0:12:08] So this is happening in real time.
[0:12:10] So the codecs one, for example, actually had an error when I tried to build it.
[0:12:14] So I actually told it to recheck it out, redo everything for you.
[0:12:17] So that's going to get to work on how that finished.
[0:12:19] So let's start off first and let's start with Opus 4.5.
[0:12:23] Why not? Let's do Opus 4.5.
[0:12:25] Let's do Claude Sonnet 4.5 and go to town there.
[0:12:28] So I'm just going to revalidate here.
[0:12:30] So if I come back up and I look here, this is going to be my PRD.
[0:12:35] So I can tap on this.
[0:12:37] And then sure enough, here's the pull request.
[0:12:39] I can see the pull request that's happening right here.
[0:12:41] So that's going to be 56.
[0:12:43] So let me just revalidate 56 is the right one.
[0:12:46] So 56, Claude of his 4.5.
[0:12:49] Perfect.
[0:12:50] Okay, cool.
[0:12:51] So I can open this here as well.
[0:12:52] So I can check it out there or I can just check it out right here.
[0:12:55] So we can see it funnily enough that I think that this one had the most files changed.
[0:13:02] If I come back over here, let's take a look.
[0:13:04] So 5,000, 4,000.
[0:13:06] I'm pretty sure this one had like a thousand lines changed as well.
[0:13:09] So it'll be interesting how that does.
[0:13:11] Okay, cool.
[0:13:12] So we have this here.
[0:13:13] I can see the diff.
[0:13:14] So I can see the full pull request over here.
[0:13:16] I can make comments and things.
[0:13:18] I can also tap on the GitHub button here.
[0:13:21] And we can see that I have, you know, co-pilot on my behalf here.
[0:13:25] So I can see all the things that are happening.
[0:13:27] So the PRD, the implement, the ones here as well.
[0:13:30] I can see I have this checked out too.
[0:13:32] So I have that there running, which is nice.
[0:13:34] Okay, let's go ahead and pull this up.
[0:13:37] And let me go ahead and just run it and see what happens.
[0:13:40] So let me go ahead and see if I can just run it and give it a whirl.
[0:13:46] So hopefully it'll, you know, pull it down.
[0:13:48] Do everything for us.
[0:13:49] And let's see what we have.
[0:13:50] Okay, cool.
[0:13:51] So here I have the zoomed in pretty far.
[0:13:54] But you can see this monitor here.
[0:13:55] So we have my pet venue, venues, ad venue, my pets, light theme,
[0:14:00] dark theme, does seem to be working on some of it, which is good.
[0:14:04] Not all of it.
[0:14:05] So we have ad venue explore venues here, birds, dogs, pets.
[0:14:09] Trusted reviews, we have featured venues, view details.
[0:14:13] And again, I'm kind of zoomed in here a little bit, but zoom out there too.
[0:14:18] Browse by category.
[0:14:20] I mean, this is a pretty great starter.
[0:14:21] We have the actual reviews that are coming in here.
[0:14:24] We have overview for the pets.
[0:14:26] So there's our pets going on here, which is great.
[0:14:29] And then yeah, we have the light theme, dark theme happening on some of it,
[0:14:33] but not all of it.
[0:14:34] So I'd probably have to go back and iterate a little bit more on it as well.
[0:14:38] Probably just some background there.
[0:14:40] Let's go to the venues.
[0:14:41] So we see here we have all the different venues.
[0:14:43] Can I search for one?
[0:14:45] Let's say Seattle.
[0:14:46] Here, zoom out a little bit.
[0:14:49] And we also do Seattle in real time.
[0:14:52] We do Portland.
[0:14:53] There's one in Portland.
[0:14:54] So it filters it down in real time, which is cool.
[0:14:56] I can view it.
[0:14:57] Then we get this information.
[0:14:59] So accepted pets, so right reviews, favorites, share venues here.
[0:15:03] That's pretty nice.
[0:15:04] And I get this nice header and footer as well.
[0:15:07] I do anything else.
[0:15:08] I have my pets.
[0:15:09] Okay, cool.
[0:15:10] My pet, that is my pet.
[0:15:11] That is milling, not max necessarily, but there's that.
[0:15:13] I can edit.
[0:15:14] I can't edit.
[0:15:15] Oh, I can edit.
[0:15:16] Oh, wow.
[0:15:17] Okay, cool.
[0:15:18] So I can actually edit.
[0:15:19] So I did milling.
[0:15:20] Does it save it?
[0:15:21] It'd be fascinating to see how different images.
[0:15:22] Oh, it does.
[0:15:23] Wow.
[0:15:24] So that's kind of cool.
[0:15:25] That actually does that.
[0:15:26] So I actually edit this again and do Australian cattle dog.
[0:15:30] That's cool.
[0:15:31] And she is nine.
[0:15:33] 94.
[0:15:34] There we go, died.
[0:15:35] Perfect.
[0:15:36] Cool.
[0:15:37] All right.
[0:15:38] I love that.
[0:15:39] So that is neat.
[0:15:40] I had venues.
[0:15:41] I can add a venue on to here.
[0:15:42] I love that.
[0:15:43] All the different amenities, selecting venue images.
[0:15:46] That's pretty cool.
[0:15:47] And again, browsing all this.
[0:15:49] And there's even a bow page.
[0:15:50] So that is fairly nice in general.
[0:15:53] I mean, just from a 20, 30 minute session to get something like that spun up that I could
[0:15:58] just see, is this even something I want to continue?
[0:16:00] Are there things that I like?
[0:16:01] I could go back and iterate on it as well.
[0:16:03] But from a landing page, featured venues, things like that, I'm relatively impressed.
[0:16:08] All right.
[0:16:09] Let's look at the code.
[0:16:10] Because I think the code is important here.
[0:16:12] So if I look over here, we have some models.
[0:16:14] We have like amenity.
[0:16:16] We have pet, pet type.
[0:16:18] So just standard classes that it did here.
[0:16:20] Nothing fancy.
[0:16:22] We do have some services.
[0:16:24] So we have a mock data service here.
[0:16:28] So initialize amenity services.
[0:16:30] It doesn't seem like it used any interfaces.
[0:16:33] So that would be one thing that would have been nice to have it kind of out of the box do for us.
[0:16:37] But it does look like it just created all the sample data for us.
[0:16:40] Then we have the pages.
[0:16:42] So it's just using razor here.
[0:16:44] And I assume all of the CSS and just one huge CSS file.
[0:16:49] So our razor CSS would have been nice.
[0:16:51] I didn't necessarily tell it to do that, but it is here.
[0:16:54] And then we can see that we're using like edit forms and data annotation validators.
[0:16:58] So that's really nice to see that off the rip, which is cool.
[0:17:02] All right, cool. That looks pretty good.
[0:17:04] All right, let's go ahead now.
[0:17:06] And come back over here and let's go and look at this one here.
[0:17:10] So this one is going to be Claude's sonnet 4.5.
[0:17:13] So I can go and tap on that.
[0:17:15] That's now going to load it up as well.
[0:17:17] So we can see that we have 28 files changed.
[0:17:19] And we got a lot of different razor files.
[0:17:21] So star rings, bendies, cars, footers, amenities, pets.
[0:17:24] So probably relatively similar.
[0:17:26] I mean, they're both Claude models.
[0:17:28] But I can now tap on this.
[0:17:30] So I can then see what's going on here.
[0:17:32] So exact same PRD.
[0:17:34] So this is the PRD created and then the PRD that it implemented here.
[0:17:38] This is actually pretty long.
[0:17:39] I mean, this is a pretty long one.
[0:17:41] So I'm interested to see how it did.
[0:17:43] That is for sure.
[0:17:44] So let's go ahead and check this out.
[0:17:47] And this is going to check out that branch.
[0:17:50] Let's go ahead and close these down.
[0:17:53] All right, cool.
[0:17:54] So I'm going to close this over here.
[0:17:55] And yeah, we can see that we have all these files changed.
[0:17:58] So let's go ahead and spin this up.
[0:18:00] I'm going to launch it here.
[0:18:02] I'll just see if it builds.
[0:18:03] So I'll play a builds.
[0:18:04] All right, there we go.
[0:18:05] And yeah, okay.
[0:18:07] Let me go ahead and control shift hard just in case.
[0:18:09] Here.
[0:18:10] So let's see.
[0:18:11] We've got light mode, dark mode.
[0:18:13] All right, light mode, dark mode.
[0:18:14] This pink should obviously go across the entire screen.
[0:18:17] What it is.
[0:18:19] You know, not too bad.
[0:18:20] I think it looks okay for like giving it no context
[0:18:23] really what to use going on here.
[0:18:25] It did default.
[0:18:26] It's a dark mode.
[0:18:27] That's kind of nice.
[0:18:28] Okay, so we have better new locations.
[0:18:29] I like that emojis are up and down.
[0:18:31] Here, trusted reviews, popular venues.
[0:18:34] That's interesting, fire emoji.
[0:18:36] And then we get kind of a nice view here.
[0:18:38] It's nice hover animations, beach, venues, recent reviews.
[0:18:41] So not too far off from Opus.
[0:18:43] I do see that there is a error that occurred here.
[0:18:46] So I'm not sure why what happened there.
[0:18:48] I have to look into the logs.
[0:18:49] Let's take a look at the venues.
[0:18:51] So sure enough, do we get see how we get
[0:18:52] real time?
[0:18:53] That's nice.
[0:18:54] Oh, nice little Portland.
[0:18:56] CCaddle.
[0:18:58] It looks like it's filtering out.
[0:19:00] So if I do pause, so the names here,
[0:19:02] so I can click on them here.
[0:19:03] We get types going on here.
[0:19:05] That's nice.
[0:19:06] All right, let me click on this.
[0:19:07] And we can see this is a clinic.
[0:19:09] We have about amenities.
[0:19:10] This is a nice pretty view here as well.
[0:19:12] So this is kind of nice.
[0:19:13] Home links add venue, things like that, which is cool.
[0:19:16] Let's do add venue.
[0:19:18] So relatively basic form.
[0:19:20] Over data here.
[0:19:21] It looks pretty nice.
[0:19:22] Add venue.
[0:19:23] Then we go into reviews.
[0:19:25] All right, so this is just community review.
[0:19:26] So you can just kind of see all the filtered reviews.
[0:19:29] Go directly to it and things like that.
[0:19:31] So it didn't decide to do profiles.
[0:19:32] It didn't decide to do my pets.
[0:19:33] I mean, like that.
[0:19:34] That's OK.
[0:19:35] I'm always just kind of interested to see what it gives us
[0:19:37] at the end of the day.
[0:19:39] I'll take a look at the code.
[0:19:41] I'm going to stop this here.
[0:19:42] I'll just pull this over.
[0:19:43] So the first thing that we're going to see is
[0:19:45] I actually get some components here.
[0:19:46] I kind of like that.
[0:19:47] We have an amenity option.
[0:19:48] So in here, I kind of like that.
[0:19:49] We have an amenity icon, review card, star rating, a venue card.
[0:19:54] I like that.
[0:19:55] I broke that down into smaller chunks for us.
[0:19:57] We have models.
[0:19:58] So a lot of models user review.
[0:20:01] So there's a user that's anonymous.
[0:20:03] And I'm interesting.
[0:20:04] I don't know if I necessarily saw anything for a user itself.
[0:20:12] Going to venues.
[0:20:13] Can I add a review?
[0:20:16] No, I don't think so.
[0:20:17] So I don't see anything about.
[0:20:19] I don't see an about page or anything about me, but there is a user
[0:20:22] specifically there, which is interesting.
[0:20:26] Then you add venue.
[0:20:28] We do a theme service.
[0:20:29] So here's this JavaScript interops.
[0:20:31] So it's kind of a nice component there.
[0:20:33] And then we have mock data service.
[0:20:35] So this again is a mock data service.
[0:20:37] And we're getting again very similar results here.
[0:20:41] So no interfaces.
[0:20:43] Just here it is.
[0:20:44] Go to town there.
[0:20:45] And the same thing.
[0:20:46] It seems to have just put all the CSS and one big CSS file, which is OK.
[0:20:50] I'm not mad at it.
[0:20:51] You know what I mean?
[0:20:52] But it did at least give us the two services that are getting registered here, which is kind of nice.
[0:20:56] OK.
[0:20:57] Let's look at the last one here, which is going to be our codecs.
[0:21:00] Five one.
[0:21:01] So GPT-51 codecs max.
[0:21:05] I'm a little concerned that only 800 lines of code changed.
[0:21:08] But that's OK.
[0:21:09] You know, who knows?
[0:21:10] You know, it's a PRD.
[0:21:12] So let's go ahead and see what it did here.
[0:21:15] So I tap on this.
[0:21:17] We have the PRD.
[0:21:19] OK, we have a relatively very small PRD.
[0:21:22] So, you know, if you write a PRD as a thousand lines and you get a thousand lines with this one,
[0:21:27] we wrote a very small PRD of just 50.
[0:21:29] So pretty small, to be honest with you.
[0:21:32] But that's OK too.
[0:21:34] You know, it has some stuff in scope here that it wants to do.
[0:21:38] So it did follow my in scope things that I wanted to do.
[0:21:40] Let's go and check out this branch and let's see what happens here.
[0:21:44] So I'm going to pull this over and let's open the files and go to my program.
[0:21:50] Let's go ahead and run it here.
[0:21:52] So I'm going to run this now.
[0:21:54] All right.
[0:21:55] Let's see what we get.
[0:21:56] All right.
[0:21:57] Actually, not bad.
[0:21:59] So this is kind of cool because it did create a very small PRD.
[0:22:03] Let's see if it did light mode in dark mode.
[0:22:05] That's kind of cool.
[0:22:07] It didn't do any of the kind of pop-ups.
[0:22:10] It looks like the images aren't loading here for the venues.
[0:22:13] But it did create a very relatively simple overview.
[0:22:16] I like the left to right view here.
[0:22:19] We can see highlights.
[0:22:20] There's smart filters curated highlights.
[0:22:22] Light theme dark theme ready.
[0:22:24] That's what it is.
[0:22:25] Cool.
[0:22:26] Sunset here.
[0:22:27] Let's go to venues.
[0:22:28] And then this has a venues page.
[0:22:30] And it can filter it.
[0:22:31] So I'm not sure exactly why.
[0:22:34] What's going on?
[0:22:35] There's Sunset Park.
[0:22:36] So it looks like it has some kind of funkiness going on with it.
[0:22:40] I can't tap on these.
[0:22:41] So it actually just did the smallest POC ever, basically.
[0:22:46] So this is like mock date only curated events home.
[0:22:51] So it did something for me here.
[0:22:53] I actually like this kind of view up here.
[0:22:55] It's not too crazy AI.
[0:22:56] I had some subtleness here.
[0:22:58] I could then work with it to actually build something out.
[0:23:01] And the light theme dark theme is relatively responsive.
[0:23:04] So it does look like maybe it got some funkiness with the images.
[0:23:06] Although I got most of the images working.
[0:23:08] So it's kind of fascinating as well.
[0:23:10] So again, I think that Son of four, five and Ope is kind of like,
[0:23:13] you know, a beast kind of with this UI views that they create.
[0:23:17] But I do kind of like what it's created here for us, you know,
[0:23:21] by scrap.
[0:23:22] I mean, off the rip.
[0:23:23] So I think that looks pretty good to be honest with you.
[0:23:26] Just above the fold below the fold.
[0:23:28] And it's okay.
[0:23:29] Now maybe with the obvious those images we're showing up.
[0:23:31] It'll be a little bit better.
[0:23:32] So I could work with the there.
[0:23:34] Let's look at the code that it generated though.
[0:23:36] So I'm going to go over here.
[0:23:38] So fascinating.
[0:23:40] This is the first one that did an iPad venue service.
[0:23:43] Okay.
[0:23:44] So it has get featured, get all.
[0:23:46] I like that it did an interface base first one.
[0:23:48] That's cool.
[0:23:49] And then here we have a mock pet venue service.
[0:23:52] There we go.
[0:23:53] So just normal stuff.
[0:23:54] We have a theme service.
[0:23:55] So very similar.
[0:23:56] And it was very, very simple.
[0:23:58] So it created this home.
[0:23:59] Nothing fancy, a venue's.
[0:24:01] And that's it.
[0:24:02] And then I sort of stopped and just has one model.
[0:24:04] So I didn't do anything else.
[0:24:05] Which isn't necessarily bad.
[0:24:07] It did create components for footer and nav bar venue card as well.
[0:24:11] So that's quite nice that it did there.
[0:24:14] So I'm relatively surprised of what it created just with the minimal parts there.
[0:24:18] And it did create a little bit of theme here as well.
[0:24:20] I do think that if I see here we have venues.
[0:24:25] Yeah.
[0:24:26] And that's it.
[0:24:27] So we're good.
[0:24:28] So everything that it gave us on the PRD as well that we went through.
[0:24:30] So it did.
[0:24:31] What it did.
[0:24:32] Right.
[0:24:33] So it basically just wrote a very similar, very chill user flow.
[0:24:36] And that's it.
[0:24:37] So they didn't necessarily go any deeper into the venue cards, the ratings.
[0:24:43] And actually tapping on details on it at all.
[0:24:45] Right.
[0:24:46] But now if I wanted to, I could come back here.
[0:24:48] I could update the PRD for more detail.
[0:24:50] Let it go to town.
[0:24:51] Let it do everything else that I wanted to do.
[0:24:53] And one of the nice things that we're seeing is that it's actually validating any tests that I have running
[0:24:58] everything that I have here.
[0:24:59] And then going to town.
[0:25:00] So pretty cool overall just seeing it all come together.
[0:25:03] And of course, I love being able to come back.
[0:25:05] I love being able to come in here and to see these different sessions.
[0:25:09] Tap on one, get more information there.
[0:25:12] There.
[0:25:13] So it's really fascinating to see the different models.
[0:25:15] But I love being able to come in, delegate those tasks off directly from getup.com.
[0:25:21] Review them here, pull them up into VS code and get everything together.
[0:25:25] All right.
[0:25:26] That's how I've been using Cloud Agents every single day.
[0:25:29] I think it's kind of fun to see how the different models perform.
[0:25:32] Obviously every model inside a VS or VS code where I'm using it in a co-pilot.
[0:25:34] Perform differently.
[0:25:35] I'm often going back and forth between GPT-5-2, a mini models, a high-coo,
[0:25:40] Son of 4-5 and sometimes Opus as well.
[0:25:42] Based on the tasks that I'm trying to complete.
[0:25:44] So I thought it'd be interesting.
[0:25:46] Like I said, to kind of break down that super high level, create the PRD, create the entire application, and see outcomes.
[0:25:50] Is that something that you're going to do every day?
[0:25:52] Maybe not.
[0:25:53] However, one thing that I have been doing is creating brand new marketing websites for a lot of the apps that I've been
[0:25:59] creating with Don M. Alley or with Swift for example.
[0:26:03] I need a beautiful landing page and I can easily have these Cloud Agents take my idea and put it into a full static website that I can
[0:26:10] deploy to get up pages in seconds.
[0:26:12] So it's really, really cool to get that set up.
[0:26:14] Are you using Cloud Agents?
[0:26:15] Are you only using Agents inside of VS or VS code?
[0:26:18] Or what else are you using these agents?
[0:26:20] Let me know in the comments below how your experience has been with these different models.
[0:26:24] All right.
[0:26:25] It's going to do it for this one.
[0:26:26] So until next time, thanks for watching and happy-goating.
[0:26:28] Happy-goating.
