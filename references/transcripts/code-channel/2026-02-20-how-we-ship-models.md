---
video_id: nD1U_wggrQM
title: "How we ship models"
url: https://www.youtube.com/watch?v=nD1U_wggrQM
channel: "@code (Visual Studio Code)"
published: 2026-02-20
speakers:
  - Visual Studio Code team
topics:
  - model-selection
  - evals
  - copilot
  - reliability
relevance: primary
---

# How we ship models

Shipping the right AI model for each task requires a lot of testing and evaluation. Get an inside look at how the VS Code and Copilot teams assess model quality, decide when to roll out updates, and balance capability with reliability.

## Key Topics Covered

- **Model Selection**
- **Evals**
- **Copilot**
- **Reliability**

## Links

- https://aka.ms/vscode/109
- https://aka.ms/vscode/insiders
- https://aka.ms/vscode/live
- https://aka.ms/vscode/109blog
- https://aka.ms/awesome-copilot

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Hi everyone, my name is Julia and in my
[0:00:02] session we're going to talk about how we
[0:00:04] ship models in VS code. Um so in
[0:00:06] Sundep's session you've already seen um
[0:00:08] how you can actually manage and you can
[0:00:10] configure these. Um and in my session
[0:00:12] I'm going to talk about a little bit how
[0:00:14] they actually like what it works or how
[0:00:16] it works how we're getting these models
[0:00:18] into VS Code. So for this I'm actually
[0:00:21] going to take you on a little bit of an
[0:00:22] journey. So I recently started as a PM
[0:00:26] in um Visual Studio Code. Before that, I
[0:00:29] was using VS Code daily, but I never
[0:00:32] really thought about, well, what happens
[0:00:34] or how does it work that a new model
[0:00:37] will just show up here? Um, and as an
[0:00:40] example, we released Sonnet 4.6 on
[0:00:43] Tuesday. We had Opus released um last
[0:00:46] week. We actually right now releasing
[0:00:49] Gemini 3.1 Pro. So, you can see there's
[0:00:53] a lot of traffic and a lot of movement
[0:00:55] for these model releases going on. So I
[0:00:58] never really thought about well how does
[0:01:00] it work and how do new models come in
[0:01:02] and most importantly how do we make sure
[0:01:04] the quality of these models actually
[0:01:07] work in VS code itself um as well. So
[0:01:11] while I was joining the team and for me
[0:01:13] to dig a little bit deeper into this um
[0:01:15] topic or this conversation. So how do we
[0:01:18] know whether a new model perform
[0:01:20] performs well inside VS code? How do we
[0:01:24] um know if the new model is actually
[0:01:26] using the VS code tools correctly and
[0:01:29] also how do we make sure that every time
[0:01:31] we are releasing a new model the
[0:01:33] experience stays fast stable and it
[0:01:36] doesn't really um disrupt the developer
[0:01:39] workflow and it just works right so
[0:01:41] these are all of these questions that I
[0:01:43] ask myself well how do we make sure that
[0:01:45] all of this works whenever a new model
[0:01:47] is being released
[0:01:49] this actually led us to a challenge
[0:01:51] which is called the nondeterminism
[0:01:54] problem. What is this all about? So AI
[0:01:57] systems are nondeterministic.
[0:02:01] This essentially means the same prompt
[0:02:04] can produce different outputs outputs
[0:02:07] across runs. And maybe you have
[0:02:09] experienced this yourself as well.
[0:02:11] Whenever you ask a model, hey, do this,
[0:02:15] it actually will produce every time you
[0:02:17] ask this model a certain prompt, it will
[0:02:20] reproduce an output differently every
[0:02:23] time. So for this and to showcase you
[0:02:26] this problem a little bit more in
[0:02:28] detail, um I prepared a few things. So
[0:02:31] I'm a big soccer fan. So I ask uh one of
[0:02:34] the models to generate me a c CSV file
[0:02:38] with just random um uh data in there
[0:02:41] about the upcoming world soccer cup. So
[0:02:44] I'm I'm yeah just asking about like
[0:02:46] category team size like um uh teams as
[0:02:50] well. So I'm like I just ask it to
[0:02:52] generate this as well. I also ask um one
[0:02:55] of the models to um create me a Jupiter
[0:02:58] notebook because I wanted to do some
[0:03:00] data analysis. So this was the notebook
[0:03:03] I started out with um where it imported
[0:03:06] me required libraries. It loaded the CSV
[0:03:09] file and then it also checked h checked
[0:03:11] for missing values. So what I did next
[0:03:14] and kind of to show you what the
[0:03:16] non-deterministic problem really is. I
[0:03:19] went into agent mode and I asked the
[0:03:22] exact same question three times and a
[0:03:26] different model. So for my first run I
[0:03:29] asked sonnet 4.6 six um I ask um opus
[0:03:33] and I also ask Gemini and you can see
[0:03:36] here on the left the different outputs
[0:03:38] for all of these different models. So
[0:03:41] this was my text prompt basically asking
[0:03:43] hey I want you to analyze my data. I
[0:03:46] also want you to kind of come up and
[0:03:47] visualize some of the key trends. So
[0:03:51] let's take a look and what of the
[0:03:52] different models um actually produced.
[0:03:55] So if we jump into the Gemini Pro
[0:03:58] Jupiter notebook, we can see that it
[0:04:01] used my um original Jupiter notebook as
[0:04:05] a um copy kind of like as a template,
[0:04:07] but then it started to add something. So
[0:04:09] this is the part where Gemini 3 Pro took
[0:04:12] over and it did the analysis. It um did
[0:04:16] like a little bit of tableing here and
[0:04:18] then also at the end it started to
[0:04:20] visualize it. It gave me um like top 10
[0:04:23] teams um and really nice one kind of
[0:04:26] visualization. Great. If we compare this
[0:04:29] again, keep in mind I asked the same
[0:04:31] model um different uh the the same text
[0:04:35] prompt. So for this one and this one I
[0:04:37] think is GPD GPD5.3
[0:04:40] codeex again it used my original Jupyter
[0:04:43] notebook as a template and then it went
[0:04:46] in and did an analysis. And if we scroll
[0:04:48] all the way down, we can immediately
[0:04:50] tell even though it was the sec same
[0:04:53] text prompt, it created a different
[0:04:55] output, right? The visualization looks
[0:04:57] very different. And last but not least,
[0:05:00] um I also did the same with our opus
[0:05:02] model. Um here it rather than just
[0:05:06] creating one um file, it actually um
[0:05:09] created different um columns, different
[0:05:12] visualizations.
[0:05:14] So, um, yeah, if I scroll down, it it
[0:05:17] does a nice job in separating some of
[0:05:19] these things, but it doesn't give me
[0:05:21] this one kind of visualization that the
[0:05:24] other models did. And not saying that
[0:05:26] any of these aren't true or aren't
[0:05:28] right. Just kind of to demonstrate you
[0:05:31] some of the challenges and we go through
[0:05:33] and also what it means to have this
[0:05:35] non-deterministic problem, especially if
[0:05:38] you're new releasing new models. like
[0:05:40] how do we know the quality of these
[0:05:42] models is actually accurate? Um so uh
[0:05:46] yeah.
[0:05:48] All right. So now that we identified the
[0:05:50] nondeterministic problem um how can we
[0:05:53] solve this problem especially if we are
[0:05:56] not yet releasing a model we know that
[0:05:59] there will be a model release um soon.
[0:06:01] So even though a system is
[0:06:03] non-deterministic,
[0:06:05] we needed a deterministic measurement, a
[0:06:08] way to repeatedly have tests that score
[0:06:12] the model's quality, the model's
[0:06:14] behavior the same way every time we do
[0:06:17] this. And this is where evaluations or
[0:06:20] evals come in. and evaluations is a big
[0:06:23] and core um core part of our development
[0:06:27] or our integration pipeline whenever we
[0:06:30] are releasing new models. So what are
[0:06:33] evals? Let's take a look at the
[0:06:34] definition here. An evaluation eval is a
[0:06:37] test for an AI system. You give the
[0:06:40] model an input, your text prompt
[0:06:42] basically. And then we use grading logic
[0:06:45] to score its output and determine
[0:06:48] whether it was successful, whether maybe
[0:06:51] it wasn't as successful. And for this um
[0:06:54] we using offline evolves which are a big
[0:06:57] part of our um shipment pipeline to have
[0:07:00] these repeatable automated tests before
[0:07:02] a model is rel released to the public.
[0:07:05] while we are integrating this into our
[0:07:08] development um into our development
[0:07:10] pipeline and we are trying to score how
[0:07:13] this AI system with a new model is
[0:07:15] performing on these predefined tasks.
[0:07:19] So what are the test cases or how do we
[0:07:21] come up with these test cases? So there
[0:07:23] are a bunch of open-source um benchmarks
[0:07:26] out there as a very prominent or popular
[0:07:29] um benchmark um it's called Swebench
[0:07:32] and using this like using SWEBench as
[0:07:36] part of our um release um pipeline. We
[0:07:39] are still doing this and it it is nice
[0:07:41] to kind of see what the standards are
[0:07:43] out there um using this open source um
[0:07:45] benchmark as well. But we are or we were
[0:07:48] detecting a few issues and a few
[0:07:51] challenges with this open source
[0:07:52] benchmark. One of them are potential
[0:07:55] leakage or familiarity challenge which
[0:07:58] essentially means this is an open source
[0:08:00] benchmark right so we don't know how the
[0:08:03] model are being trained if they're
[0:08:04] excluding this and yet they're training
[0:08:06] um data sets. So because it is public
[0:08:09] models might have seen similar fixes
[0:08:12] before. So um yeah just knowing that
[0:08:15] this might be one of the challenges that
[0:08:17] we are running into whenever we are
[0:08:19] using or whenever you are using an open
[0:08:21] source benchmark. Another one that we
[0:08:23] detected is Sweepbench um is very Python
[0:08:26] heavy and it uses a lot of their test
[0:08:28] cases uses Python reposs.
[0:08:32] So it has a very strong score or
[0:08:34] tendency towards this kind of language.
[0:08:37] Um so especially for VS code we know we
[0:08:40] have developers out there who is not
[0:08:41] just using Python we have so many
[0:08:43] different languages that they are using.
[0:08:45] So we wanted to make sure we are not
[0:08:46] just testing on one language in
[0:08:48] particular. We actually wanted to
[0:08:50] diversify the test cases that we are
[0:08:53] using.
[0:08:54] So what did we come up with? We came up
[0:08:57] with what we call VSC bench. VCbench is
[0:09:01] our own internal VS code benchmark that
[0:09:04] is made up of 50 plus developer test
[0:09:08] cases. This benchmark is still very new.
[0:09:10] We um started this effort whenever I
[0:09:13] joined last year in August. But we knew
[0:09:15] how important evaluations are as part of
[0:09:18] our release pipeline. So for every new
[0:09:22] model release in addition to running
[0:09:24] bench against it, we are also running
[0:09:26] VSCbench. Um we are run we are running
[0:09:29] all of these test cases as our um
[0:09:32] official offline evaluations and we are
[0:09:34] comparing the results um from one model
[0:09:37] family to the next one just to better
[0:09:39] quantify before we are releasing this to
[0:09:42] a live audience what the performance
[0:09:44] what the quality of this new model will
[0:09:46] look like and if it does work in our
[0:09:48] environment with our VS code built-in
[0:09:50] tools with all the developer task or
[0:09:53] developer flows we see very commonly in
[0:09:56] VS code itself as
[0:09:58] um as well and also to potentially catch
[0:10:00] any regression that we might we are or
[0:10:03] we could see with any of the model
[0:10:05] releases. So because this is an internal
[0:10:08] benchmark I'm not um able to show share
[0:10:11] too much detail into all of these
[0:10:13] different test cases that we have but as
[0:10:16] an example today I brought um one way
[0:10:20] how we are using this and what are a
[0:10:22] core concept of these um evaluation test
[0:10:26] cases is so this is a very simple one
[0:10:29] one of our example test cases um and
[0:10:32] this is the structure of it so every
[0:10:35] test case and we are CBench has an
[0:10:37] agent.yamel file and while we are
[0:10:39] running our offline evaluation it will
[0:10:42] go these steps and it will do the
[0:10:44] following. So it will use the text
[0:10:46] prompt which think of it a user going in
[0:10:49] here and typing this text prompt in VS
[0:10:52] code into the GitHub copilot chat
[0:10:54] experience. And then a very important
[0:10:57] part of offline evaluations are our
[0:11:00] assertions. we know how or what would be
[0:11:04] the minimum core requirements for this
[0:11:06] model to work with um this text prompt
[0:11:09] because especially again every time we
[0:11:12] run this the output could be very
[0:11:15] different but because we have these
[0:11:16] assertions in there which think of them
[0:11:19] the as the core requirements that are
[0:11:21] needed for this model to be successful.
[0:11:24] Um so we are um yeah we are like writing
[0:11:28] down the assertions for example hey for
[0:11:31] us it is very important that the agent
[0:11:33] should have a virtual environment. We
[0:11:35] want to make sure that the run in
[0:11:36] terminal tool is being called here and
[0:11:38] it doesn't um use any other built-in
[0:11:41] tools in VS code. So think of this as
[0:11:44] one test case. As I mentioned, VSCbench
[0:11:46] currently has 50 plus other um test
[0:11:49] cases as well across different languages
[0:11:52] across different developer workflows
[0:11:54] that we are seeing. And we are doing
[0:11:55] this repeatedly before a model launch to
[0:11:58] see how the model performs if we see any
[0:12:02] regression in the quality. So once this
[0:12:05] is being done um as part of our uh
[0:12:08] release we are autogenerating what we
[0:12:11] call a model report card uh and I
[0:12:14] brought an example model report card
[0:12:16] here um to showcase um one of the latest
[0:12:20] releases that we had GBD 5.3 codeex and
[0:12:24] usually as part of this we do start
[0:12:26] comparing it across the um different
[0:12:29] model families that we've had um so here
[0:12:32] you can see we are comparing ing one
[0:12:34] with the other. We typically start with
[0:12:36] some performance metrics where we want
[0:12:38] to make sure especially the resolution
[0:12:40] rate for these new models is going up.
[0:12:42] It is able to solve more of our test
[0:12:44] cases that we have in there because we
[0:12:46] really care about our quality and we
[0:12:49] also then checking on how many steps
[0:12:50] does it take for this model to come to
[0:12:53] this um conclusion and not always saying
[0:12:56] that less step is better. We of course
[0:12:58] care about the quality, but it's just
[0:13:00] interesting to see the overall
[0:13:03] performance across some of the different
[0:13:04] metrics that we have. Um, one very
[0:13:08] interesting metric that we care very
[0:13:09] deeply deeply about is called success at
[0:13:13] case steps. We really like it because it
[0:13:16] is a good indication indicator not just
[0:13:18] on the resolution rate but also
[0:13:21] efficiency. So it checks quality and
[0:13:23] efficiency at the same time because on
[0:13:26] one end it checks on how successful a
[0:13:29] run was and also at the same time takes
[0:13:31] into comparison on how many text steps
[0:13:35] were being used here. So with this model
[0:13:38] you were able to see very nicely and we
[0:13:41] only ran our VSC bench um against this
[0:13:44] once. Typically we try to do this
[0:13:46] multiple times because again every time
[0:13:48] we do this the outcome can be different.
[0:13:50] So we want to make sure that we actually
[0:13:52] have more data based on these different
[0:13:54] runs. But for this um example report
[0:13:57] card, you can see GBD 5.3 was able to
[0:14:02] very similar like GBD 5.2 go quickly up
[0:14:05] there, which is one of the things we
[0:14:07] care about. We want to see the model
[0:14:09] going up very quickly, but then overall
[0:14:11] the resolution rate is higher. So it
[0:14:13] seems to be more successful um with more
[0:14:17] or amount of steps. Um and three metrics
[0:14:22] overall that we are looking at here is
[0:14:24] the average lift across all of these
[0:14:27] case. We also check on the early step
[0:14:29] lift because we want to make sure even
[0:14:32] though a model is successful overall we
[0:14:35] still want it to be um improving on
[0:14:37] efficiency as well. So that's also one
[0:14:39] of the indication we look at and then
[0:14:41] overall the area under the curve should
[0:14:45] be positive for the new model. So we
[0:14:47] just know overall one of the like the
[0:14:49] the higher resolution rate is one thing
[0:14:51] that we also care about. All right. So
[0:14:55] once we've done this um and once we have
[0:14:58] our model card um what does the process
[0:15:01] overall then look like um and this is a
[0:15:04] very high level process on typically the
[0:15:07] cycle we go through um every time a new
[0:15:09] model appears. So we are working very
[0:15:12] closely with um the model um providers
[0:15:15] uh because they care about our feedback
[0:15:18] um but also we need to make sure that
[0:15:20] the model really works um before a new
[0:15:23] announcement as well. Um so once we hear
[0:15:26] about a new announcement from our model
[0:15:28] provider friends um we are typically
[0:15:30] getting access not too much um in
[0:15:32] advance um but we are getting access um
[0:15:36] to it and this is important because on
[0:15:38] VS code side we are making some prompt
[0:15:41] updates to truly make sure the model
[0:15:43] that um the model providers are giving
[0:15:45] us access to does work on client side on
[0:15:48] VS code side and then as part of offline
[0:15:52] evals that we just talked about We are
[0:15:54] kickstarting SW bench. We are
[0:15:56] kickstarting via Cbench and we also in
[0:15:59] parallel of course doing some manual
[0:16:01] testing. So think of these two things
[0:16:03] going on in parallel offline evaluations
[0:16:05] but also dog fooding manual testing
[0:16:08] within MVS code. We are using this as
[0:16:11] valuable feedback that we are sharing um
[0:16:13] with the model providers and see this as
[0:16:16] a very closed loop and we are getting
[0:16:19] based on the feedback we are getting
[0:16:21] recommendations from from them. we are
[0:16:23] taking some of the results we are seeing
[0:16:26] to make updates on the prompt um updates
[0:16:29] that we have to do and then ideally um
[0:16:32] depending on how much time we have
[0:16:34] before a model release we are trying to
[0:16:36] go through this cycle um more often so
[0:16:38] we truly make sure that it works until
[0:16:42] the big day um is coming your way um is
[0:16:45] the model launch day and this is how
[0:16:48] you're able to open up GitHub Copilot
[0:16:51] and VS Code to open up your model picker
[0:16:54] and that's how you're able then to see
[0:16:57] new models popping in and from an end
[0:16:59] user perspective it just kind of show up
[0:17:01] there shows up there's a lot of work
[0:17:03] going on before these model releases we
[0:17:05] are very thankful for all of the
[0:17:06] partnerships we have with the model
[0:17:08] providers and overall wanting to make
[0:17:10] sure we are providing um our developers
[0:17:12] the best um use case scenario the best
[0:17:14] developer experience in VS Code um so
[0:17:18] yeah overall if you're interested um in
[0:17:21] anything via Cbench related. I mentioned
[0:17:24] that this is currently an internal
[0:17:26] benchmark, but if these kind of topic
[0:17:28] areas are something that you're
[0:17:29] interested in, um yeah, just um tag us,
[0:17:33] reach out to us. We're always interested
[0:17:35] to kind of hear where this lands with
[0:17:36] our community, if this is an area of
[0:17:39] interest for more people out there. Um
[0:17:41] so yeah, h thank you all so much for
[0:17:43] listening and have a good rest of your
[0:17:46] day.
