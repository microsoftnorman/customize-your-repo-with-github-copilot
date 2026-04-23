---
series: VS Code Insiders Podcast
episode: 14
title: "Designing for Everyone: Accessibility in VS Code with Megan Rogge"
url: https://www.vscodepodcast.com/14
transcript_url: https://media24.fireside.fm/file/fireside-images-2024/podcasts/transcripts/f/fc261209-0765-4b49-be13-c610671ae141/episodes/b/b23957b4-3148-4d98-a189-2fe162c040dc/transcript.txt
audio_url: https://aphid.fireside.fm/d/1437767933/fc261209-0765-4b49-be13-c610671ae141/b23957b4-3148-4d98-a189-2fe162c040dc.mp3
published: 2025-11-17
duration: 28:41
transcript_available: true
---

# Designing for Everyone: Accessibility in VS Code with Megan Rogge

This episode was sourced from the official VS Code Insiders Podcast site.

## Episode Summary

        Megan Rogge, Software Engineer on VS Code, joins James to explore how accessibility is woven into the culture and engineering practices of Visual Studio Code. From screen reader support to sound signals and contrast themes, this episode reveals the thoughtful design behind features that empower every developer.

Follow VS Code:


X: https://x.com/code
Bluesky: https://bsky.app/profile/vscode.dev
YouTube: https://youtube.com/code
LinkedIn: https://www.linkedin.com/showcase/104107263
GitHub: https://github.com/microsoft/vscode
Special Guest: Megan Rogge.
      

## Transcript Status
An official transcript was available on 2026-04-21.

## Full Transcript
00:00.00
James
Welcome back everyone to the Visual Studio Code Insiders podcast. Your behind the scenes look at your favorite code editor, Visual Studio Code. I'm your host, James Montemagno. And with me today, software engineer on the VS Code team, Megan Rogge. How's it going, Megan?

00:13.41
Megan
It's going great. I'm so happy to be here. i love ah talking about my work, especially accessibility. So it'll be fun. to hear what you have ah to ask me.

00:22.91
James
Yeah, I'm really excited because we have tons of accessibility features. It's a huge segment on every single release. um Before we dive into some of the accessibility stuff and maybe some of the new stuff that the team has been working on, um maybe can tell everyone a little bit about yourself and like what you do on the VS Code team?

00:38.12
Megan
Absolutely. Yeah. So I joined Microsoft and the VS Code team right after graduating about five years ago. And I've been on the team ever since. And I work on the integrated terminal I own tasks and I own accessibility for the team.

00:54.15
James
Oh, wow.

00:54.29
Megan
And out your work also working on the chat integration with all of those aspects.

00:54.72
James
Super, do you have a favorite?

01:02.01
Megan
um Did you say, do I have a favorite?

01:04.04
James
Yeah.

01:05.12
Megan
Yes, accessibility is for sure my favorite.

01:08.34
James
Why is so accessibility so important to you and why is it important to the product?

01:13.02
Megan
Yeah, so i would say that it's so important to me and has been for a really long time because I myself have dealt with some chronic medical conditions that I think opened my eyes to the challenges that people face out there and um how creative solutions can be so empowering to those people and also help others as well. You know, like an accessibility challenge really can benefit everyone. And it just allows you to think outside of the box um and enable more people to do cool stuff.

01:47.47
Megan
So. I think it matters to me for that reason. And then it matters to VS Code and has for a really long time. So the cultural feeling on the team is accessibility is important.

02:00.50
Megan
We want all of our users to succeed in the product. And I think over the past few years, that's even ramped up more as I've been more vocal about my work with screen reader users and other users that have challenges.

02:13.92
James
Very cool. That's awesome. It sounds like, yeah, like the culture, like you're saying is accessibility, accessibility features aren't just like an add on their core essential part of the product.

02:22.71
Megan
Yeah.

02:23.82
James
So when the team thinks about accessibility, like how does that work inside of VS code and how does it show up? Maybe for folks that like, aren't even aware of accessibility features, like what does that look like and how does that show up in the product?

02:37.32
Megan
Yeah, absolutely. So I would say the easiest way I can explain this is to describe a section of our users. So that would be screen reader users. So if you are blind, you most likely, when interacting with our product,

02:51.66
Megan
would use a screen reader. And what that is, is it's an application like NVDA on Windows or mac ah VoiceOver on Mac. And that reads the elements on the screen out loud so that you can ah navigate using the keyboard and then basically operate the product ah through this audio interface.

03:13.24
Megan
um And screen reader users face a number of challenges and require unique um features and and things that I helped to implement.

03:24.75
Megan
And um so an example of that would be vs Code is amazing because of the abundance of settings and commands that we have to offer. And we have so many different features. So we have the terminal, we have the editor, we have chat, all of these things have so many different commands and so many different key bindings.

03:44.33
Megan
It's very intimidating ah to try to keep track out of all of that as a screen reader user that's new to the product. And so a feature that I co-developed or brainstormed with screen reader users to build is called the accessibility help dialogue.

04:03.52
Megan
And so this is something that screen reader new users can pull up using a keyboard shortcut for any given feature that their focus is on. And it gives an overview of the feature, all of the relevant commands and key bindings they might want to use, and essentially walks them through this so that it's not a guessing game. It doesn't take years to learn.

04:25.82
Megan
And they have all the important info up front so they can most... Efficiently navigate and succeed.

04:35.66
James
When the team is working, when you're working on these features, Megan, like how do you engage the community? right Because it's one thing to be like, okay, there are these features that you know are sort of essential when it comes to accessibility, let's say like vision impairment. right But how do we actually go about like testing it and getting feedback from our developers that are out there? because You and I can test it, but it's very different ah you know you know to simulate versus actually using the product every single day with like vision impairment, for example.

05:05.93
Megan
yeah So similar to how we're so reliant on our open source community for feedback on what they're looking for, we also rely on users to report accessibility issues and then we listen to those.

05:21.01
Megan
But because these groups are the minority of the voices in the open source community, we can't strictly rely on that. So I meet weekly with a small group of screen reader users to learn about what they are facing in terms of challenges in using our product.

05:41.60
Megan
They try out new features and I write down things they encounter that are difficult. We brainstorm solutions. So carving out that intentional time to meet with the users and learn about their experience, not once a month or once a year, but weekly so that the most recently introduced features are getting this accessibility perspective um is how we've, I think, been successful in not having accessibility be an afterthought.

06:12.98
Megan
And then we also have a team-wide practice of the iteration after ah feature is introduced. we then test it using screen reader users using a screen reader ourselves.

06:26.98
Megan
So the team has this testing practice at the end of every month called end game, where we ah try it out ourselves and document any issues. And we do this similar approach, but give one month to breathe and let that area owner get the accessibility under control before we then test it out ourselves.

06:46.86
Megan
And then the last piece of this is we have dedicated testing team that goes through using screen reader users to make sure we're compliant with the latest web accessibility standards.

06:58.14
Megan
So it's really three or four different approaches. And then the last one I would say is just having me on the team and in calls, I think people are always bracing for, well, how will this work with only the keyboard or that kind of thing? And so i think yeah having someone that is dedicated to this and always thinking from that perspective is also very helpful.

07:21.21
James
That's really cool. I was recently, we're in Redmond with a few folks and and and some of the team and went to the inclusivity lab where we talk about sort of like Windows and Surface devices and different technologies because you can make the devices obviously like more inclusive and open and accessible.

07:41.16
James
But then actually if our software isn't, then it it is ah is a big challenge. What is like some of the feedback that you hear in in these sessions and engagements with with developers using these different features?

07:54.89
Megan
I had a recent experience with this myself, actually, because I'm working right now on the showing of the terminal output inside the chat.

08:06.09
James
Yes. Yes.

08:07.21
Megan
and This is very cool feature, but when I'm working with these screen reader users every week and they're like, oh, so excited for accessibility updates, what are they, Megan? And I'm like, well, I don't have any because I've been very busy working on this feature.

08:22.70
Megan
And so this past week, um and so they tried it out and it was moderately accessible, but there were a bunch of issues with it, which I already was aware of.

08:33.74
Megan
um So I actually just addressed those because right after the feature is in it's my desire to make sure it's it's mostly accessible. um And I think having the accountability of meeting with them every week really drives that forward for me, at least.

08:53.81
James
It makes a lot of sense. i think like I specifically for the terminal output, uh, cause it's, time it's timely cause it just, it'll be out by the time this podcast is out. I've been using it and I am a very much like ah a button click person.

09:06.04
James
Like I'm not a keyboard person, not a terminal person myself, but I am a button clicker. or i i love clicking mice clickers as fast as I can in the UI, ah which often like finds a bunch of weird issues and just like things that are popping up over each other, which is is there.

09:11.63
Megan
Yeah.

09:23.21
James
But I did notice in this feature um If people don't know about it, you know in the chat window, normally when a um command would get kicked off to the terminal, you'd see the terminal window pop up, you'd see output XYZ.

09:34.87
James
now there's the feature to have it like inline or even kind of hidden you didn't even see the output it's just doing it's it's happening right um i and i noticed that to actually be able to go see it there's kind of these ai terminals there's quite a few button clicks around like when you went to design that feature and you went to go test accessibility features like what are the things that you're thinking about right because because as a developer me i'm like implementing a feature just how i normally would but what's like the mindset that you're putting yourself in when you're actually developing these features and then testing these features as well

09:47.69
Megan
Yeah. Yeah.

09:51.17
Megan
yeah

09:54.08
Megan
yeah

09:58.64
Megan
yeah

10:04.60
Megan
Yeah, it's a really great question because i too can get in the mindset of, oh, let me click that, let me click this. ah But you have to think about how will the user even become aware that there is a new ah change here.

10:18.64
Megan
And so that is again where the accessibility help dialogue can come in, where we can say terminals for the chat are hidden by default. And we'll only insert that if this setting is set to X.

10:30.59
Megan
and we would have a different text inserted if the setting is why um But the second piece is when you put your focus on such an element, it has should have a description that's very helpful.

10:45.43
Megan
And so for example, with this output, um the ARIA label that's included, so when they tab to this, is output for command ls-a, for example, right?

10:58.39
Megan
And then we have an accessible view hint, which, so the accessible view is a component added around the same time as this accessibility help dialogue and it,

11:12.09
Megan
essentially renders any element as just text because for screen readers, um that is the most easy thing to navigate in. And you can imagine pressing arrow keys will read one character at a time.

11:27.13
Megan
And there are different keyboard shortcuts that will read the full sentence, et cetera. So for this terminal output feature that is um rendered HTML,

11:38.43
Megan
that can be tricky to navigate using a screen reader. So the thought was add this accessible view for this feature so they can just run this keyboard shortcut. It will open in this essentially text area where they know exactly how to navigate and it's very easy for them.

11:52.09
James
Yeah.

11:53.92
Megan
And you might be wondering, okay, that's great, but how do they discover that there is this accessible view, let alone the command to open that accessible view?

12:02.98
James
yeah

12:03.94
Megan
And that is where the um ARIA label hint comes in. So for each of these features around the workbench, we have a hint that says use Alt F2 to open the accessible view.

12:18.42
Megan
And while that's phenomenal for making things discoverable, imagine you're a screen reader user and you hear this 100 times a day. You'd want to rip your ears off, or at least I would.

12:31.34
Megan
So we have this behind a setting, so you can disable this, um what we call accessible ah view verbosity hint or something off.

12:36.50
James
Thank you.

12:41.65
Megan
So you are new to the product, you want these on, they're on by default, and then you disable the setting because you've learned about this feature, you don't need to hear it anymore.

12:53.50
Megan
And so this was what we developed, co-developed um the idea for in one of these weekly meetings. And um Ju Young, who is one of these power users screen reader users, is actually a professor. And we co-authored a paper about this whole project collaboration because it was so powerful. Him explaining the challenges and then us brainstorming, how can we actually fix this when VS code is really powerful, it could be so accessible, but it's hard to teach a beginner screen reader user what's happening.

13:32.77
Megan
And so when I think about accessibility for any new feature, I think, how can it be discovered and explained to any user, and then how can one use just the keyboard, not their mouse, to successfully use this?

13:52.21
James
Are there things that we're doing like from a, uh, you know, the engineers are implementing features or the communities implementing features or the things that we're doing to actually make that part of the process. I remember like Tyler, for example, recently came on the podcast. He was talking about some of the playwright automation stuff that he was doing.

14:11.05
James
Are there things that we're like building into our process, like catch these things earlier when we're implementing features?

14:17.17
Megan
Yeah, it's a good question. I was just looking at this NPM package that is using Playwright to test for accessibility of these features.

14:28.93
Megan
um And I think stuff like that can be powerful and and helpful. ah But the actual user experience, I think, is still the most meaningful one.

14:43.46
Megan
And so doing both, like, how can we insert checks such that accessible code is required, you know, versus i can merge this PR and then I'll get to accessibility when I can.

14:59.20
Megan
um And I, I think it is a balance because also you try to then shove accessibility down the throat of a developer that is working on an experimental feature even. Maybe this feature won't actually persist, right?

15:16.30
Megan
Or maybe it'll change shape dramatically. um So they might feel this is... premature, it's not solid enough to warrant us investing this time or energy before we know this is the direction we're going to stick with. So I think our waiting a month approach helps to walk the line there of not being so um preemptive here, but also mandating that there is some reasonable time

15:50.95
Megan
in which this must be fixed.

15:53.74
James
It makes a lot of sense because like if it's if if you don't even know you're going to ship the feature, then you would spend more cycles and then lets you not even maybe even finish the feature on time, which makes a lot of sense. Can we talk about i two other really interesting topics I want to talk about? Because we talked a lot about screen readers and accessibility features there, but I'm really interested in...

16:12.23
James
uh colors specifically my father was colorblind so whenever i think about software was thinking about the perspective like through his eyes so like when we think about the colors the contrast the things that we're shipping in the box right because i know with visual studio code it's like everyone loves every single feature right everyone loves every single customization and the colors that you can do like is that an important aspect of like

16:21.45
Megan
For sure.

16:37.84
James
of how we decide what we're shipping in the box, how we're shipping in the box, like how we decide colors, contrast in these features as well. Is that an important accessibility feature? I'm imagining it is, but I'm actually asking cause i don't know 100% like how that stuff works.

16:52.31
Megan
Yeah, we have minimum contrast ratios and consider color blindness in a variety of ways. But one example is um any thing that we're trying to highlight or something, it won't just be indicated with color. There will be some other...

17:10.22
Megan
demarcation who knows if it's italic or there's an underline or something, just to ensure that is not a blocker for people. And then we have our special high contrast themes that are really helpful for especially low vision um developers, but others that have um any visual impairment.

17:31.46
Megan
And these meet even more strict standards, but all of our built in themes um do meet the web accessibility guidelines standards, because you should out of the box be able to use the product and, and feel good about what you're seeing on the screen.

17:50.51
James
makes a lot of sense. Like, is there a way, like, let's say I'm a theme developer, like, is there a way that I can run my theme through some accessibility check before I actually ship it?

18:00.55
Megan
I, I wonder if that exists already. Maybe there's an extension for it. That sounds like exactly what a VS Code extension would be great for.

18:10.23
James
Yeah.

18:11.00
Megan
um But it is true that it it can be tricky looking. i I know that at least I have in the past published a theme that had some accessibility issues.

18:24.83
Megan
So our core set, we try to make sure are really solid for people.

18:30.70
James
Makes a lot of sense. Yeah. And I think I've been using like a lot of like, there's ones from like the, I think the, the edge team and like the windows team, like the accessibility checker that you can like put screenshots or like do stuff on the web.

18:37.65
Megan
Yes. Yes.

18:42.36
James
i've been running that as like a pass, like we run that on the VS code website, I believe as well, talking. but for every single, like that's one of the checks. I've also noticed not just in the product, but the product is also the website, right? Where people go and make sure the website's accessible too.

18:55.15
James
We're doing the VS Code Dev Days. And I remember, I think it was a Nick. He was like, oh yeah, nothing, nothing meets accessibility. I was like, what do I do? And he was teaching me like how to use the tools and run the things. And because I had AI generate a bunch of stuff, it just the color contrasts weren't correct.

19:09.71
James
So I was like, please, you know conform and do the thing.

19:10.16
Megan
Yes.

19:12.27
James
And then I was like, write a copilot instruction to make sure like you know things are there. So I think as a developer, like learning about the accessibility features of what's important also helps me craft like better code right that I'm writing in my applications to think about.

19:22.56
Megan
yeah

19:24.95
James
So like make sure I have ARIA tags, make sure I have these things that are accessible.

19:28.25
Megan
which actually reminds me of a point I brought up, you know, when these models are doing most of the code writing or a lot of the code writing for developers, how do we ensure that that code is accessible?

19:28.52
James
um

19:36.43
James
Yeah.

19:40.59
James
yeah

19:41.01
Megan
And so it's a lot about what data that they're being trained on. And so I was asking our data scientists to really consider that and use some metric like how within Microsoft,

19:56.35
Megan
each product has a grade based on how accessible they are? And could we use that or factor that in in determining what we're feeding to these models so that we can ensure proper code gets generated since this generated code, I'm sure will be eventually fed back into the model. And this could become a big problem if we don't ensure it's factored in you know, like in some reasonable time standard, because there's a lot of inaccessible code out there.

20:27.09
James
Yeah, I'll tell you a little story really quick ah that I think will resonate with exactly what you just said. So we were getting ready to celebrate the Visual Studio, one of the releases and of that and of VS Code.

20:42.10
James
And there was all these wallpapers that the design team was creating. And we wanted to create a website for it. And Scott Hanselman, my boss, had like all these community old like Visual Studio and VS Code like wallpapers, a community it created.

20:54.47
James
I was like, I'll just vibe code this website out. I'll put on GitHub pages. Like, no big deal. I sat down. And, you know, when you're in a code flow, even when you're code flowing with vibe codes, it was just going.

21:05.09
James
And, like, from I went from, like, nothing to like, it was resizing images, doing this and this and this and this. And, like, i me and Scott published it within, like, two hours. And we're like, Boom, here it is. We registered domain name. We got it up.

21:16.14
James
And Myra on our team, who owns a bunch of our websites, like developer.microsoft.com and the.NET website, she looked at it and she was like, this is like the most...

21:29.46
James
inaccessible website, because that's like shit that's part of her process, right? Is the accessibility like when you put it first. And I was like, Oh, my gosh, like, I was like, so embarrassed. And I was like, I was like, Okay, I'm gonna sit down. So I sat down with copilot. And I kind of what you're saying is I was like, I'm gonna understand all the failure points, put all this in there, and then like, how to do all this stuff. And I was like, if it can pass Myra, right, who's been building like,

21:51.09
James
accessible websites forever, then it was good. So like I had to craft it and do all this stuff. And then a few hours later, it was like in super great shapes, visual studio wallpapers.com. You can be the judge if it's even more accessible or not accessible there, but, and there's cool wallpapers back and forth, but I agree.

22:01.85
Megan
Yeah.

22:05.82
James
It's like thinking about it first is, is how do we do some of the, the wins, right? um I come from the Donette world and I worked really close with Rachel Kang, um, on the Donette Maui team, uh, now on the visual studio team.

22:19.27
James
And ah her and Shane were big sexibility accessibility champions for ah just putting things in the template, right? File new project should be accessible by by default.

22:30.24
James
And they got that up and running. it was really cool because then as a developer I see, oh, there's already some best practices here, which I which just thought was amazing. um One thing I'm really interested that maybe you give some insight Megan into is like sound.

22:44.01
James
Like um me as a demoer and advocate, I'm often using just voice because it's like the voice extension is there and I do it as well.

22:44.73
Megan
oh yeah

22:54.15
James
But I've also noticed that there seems to be a lot of other like banners, notifications, bings, bops, and like inputs as well.

22:59.18
Megan
you

23:00.55
James
Like how important are additional inputs? And you talked a lot about the keyboard input. What about other inputs and outputs too that like are actually built into VS code that people may not know about?

23:09.35
Megan
here Yeah, we have a really rich array of accessibility signals they're called. And that means either an announcement, which is just, you can picture the screen reader reading something like focused terminal one or um a sound that indicates that. And there is a yeah spectrum of preference here. Some screen reader users or low vision users want to hear both. Some only want one or the other.

23:42.25
Megan
um And some are Braille users, so only the announcements would be you know felt by them. And so those are really important in our and our product because we have a lot of visual indicators that happen and stuff that arises and we need a similar thing but in an auditory manner and so um the accessibility signals have been our answer for that and those you can look at i mean whether or not you're visually impaired I think they're very useful so you know like the chat response received sound is really nice or um user confirmation required so let's say you're multitasking and you're

24:22.40
Megan
in a different window, you hear this sound that tells you the agent is finished and needs your confirmation. So that's really cool. And then like a task completed sound or a task failed sound are also really nice if you've got long running build tasks.

24:38.11
Megan
And again, your focus is elsewhere. You hear it's finished, so you're ready to launch the process. um So I think sound is huge for us and If you haven't looked into these, you might find at least one of them used useful because I have several enabled myself.

24:58.43
James
If I'm open on VS Code right now, like where should I look? like Where should I? Is there like a big accessibility so section?

25:04.40
Megan
Great question.

25:06.03
James
like I don't know.

25:07.54
Megan
So there is. um It's because we have so many settings. It became clear that we needed ah way for people to review these more efficiently.

25:18.37
Megan
And so there's a command called accessibility list signal sounds.

25:25.85
James
I'm opening it right now as we

25:29.22
Megan
And you can go down the list and hear all of them.

25:33.64
James
Oh.

25:33.82
Megan
You might have just heard my computer doing that.

25:39.06
James
Yes, I did. that was very cool.

25:40.87
Megan
And ah they're associated with the respective label there. So you can try those out, set them, and then know that you can come back to this command and quick pick to manage all of them right there.

25:56.88
James
That's very cool. Yeah. And just going in and just typing accessibility, I see there's like six, I mean, just filtering for accessibility. There's like 66 plus, you know, 70 plus different features that are in there.

26:07.48
Megan
Yeah.

26:10.16
James
Um, that was astonishing. I mean, it's it's so cool like learn more. And then also like, I like that there seems to be like a lot of deep dives as well. I'm seeing there's like links to documentation and other things like in terminal and different settings that are linking as well. Um,

26:25.19
James
If people are super interested in learning more, is there a good way to connect with you and the team? Is it just through GitHub or ah if people are interested in going deeper and connecting with the team on these things? Like what's the next steps for them maybe to do?

26:37.76
Megan
I mean, we're an open source project, so GitHub is our home base. And good luck if you email me. But um i am responsive on GitHub. And I'd love to hear what people think or if they have ideas for accessibility.

26:53.20
James
Perfect. That's awesome. Anything else that, you know, kind of looking forward that you'd want to kind of instill on anyone listening?

27:02.46
Megan
I think It's important to say that we all have priorities and it doesn't always feel like accessibility deserves to be that based on you know like what might be on the roadmap for your company or your project.

27:19.47
Megan
But it's extremely meaningful and it feels that way. So I would encourage people to test it out and and see what it's like to use a screen reader because prior to this work, I had never tried.

27:32.31
Megan
And i you turn on a screen reader and instantly you realize how brilliant others must be to to operate the product and and succeed. And it humbles you, or at at least it humbled me.

27:44.91
Megan
And it made me want to do better in terms of our product to enable people to be able to succeed.

27:53.20
James
That's awesome. Well, I will put links to everything that we talked about today and to like actually how to use screen readers. And I'll put a link to a few other videos, um, that I found helpful when I was going through and planning for this, uh, podcast, some different accessibility features, not only from like what's in the products, but also like how to build different products as well. So i'll put those in there in the show notes, Megan, thank you so much for coming on the podcast. I really enjoyed it.

28:17.26
Megan
Yeah, me too. Thank you so much for having me.

28:19.53
James
Awesome. And don't forget that you can always subscribe in your favorite podcast application. If you're still listening to this at the end, share it with a friend, share it with a colleague and go through the entire back catalog. Go to VS code podcast.com. You can subscribe on your favorite podcast app, or you can see our faces on the VS code YouTube as well. That's going to do it for this VS code insiders podcast. So until next time, happy coding.


