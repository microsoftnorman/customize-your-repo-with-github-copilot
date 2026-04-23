---
video_id: ZPaF_6mSp8I
title: "Create and install an F1 inspired MCP Server in VS Code"
url: https://www.youtube.com/watch?v=ZPaF_6mSp8I
channel: "@code (Visual Studio Code)"
published: 2026-04-01
speakers:
  - Liam Conroy Hampton
topics:
  - mcp
  - mcp-server
  - fastmcp
  - python
relevance: primary
---

# Create and install an F1 inspired MCP Server in VS Code

In this video Liam will show you how to create and install a Formula 1 inspired MCP Server in Python using the FastMCP library. He explains and shows you the client/server model, the transport used with STDIO, tool discovery, tool invocation and the schema discipline. 🔗 Repo: https://github.com/liamchampton/f1-race-engineer-mcp 🤝 Connect with Liam: https://www.linkedin.com/in/liam-conroy-hampton/

## Key Topics Covered

- **Mcp**
- **Mcp Server**
- **Fastmcp**
- **Python**

## Links

- https://github.com/liamchampton/f1-race-engineer-mcp
- https://www.linkedin.com/in/liam-conroy-hampton/

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Hey folks, in this video today, I'm
[0:00:02] going to be showing you how to create an
[0:00:04] MCP server inside Visual Studio Code.
[0:00:07] I'm going to be writing this in Python.
[0:00:09] We're going to be looking at the client
[0:00:10] server model. We're going to be looking
[0:00:11] at the transport. We're going to be
[0:00:13] looking at tool discovery and tool
[0:00:15] invocation. And we're going to look at
[0:00:16] some of the schema discipline as well.
[0:00:19] It's going to be a Formula 1 inspired
[0:00:21] MCP server. We're going to be looking at
[0:00:23] a big data set and how we can use an MCP
[0:00:26] server to talk to that data set using
[0:00:29] GitHub Copilot Chat.
[0:00:33] So, I was scrolling Instagram and I saw
[0:00:35] a few people come across this fastf1
[0:00:38] Python package, which is actually why
[0:00:40] we're doing this in Python because well,
[0:00:42] this is where it exists. Now,
[0:00:45] this has got all the data that we need
[0:00:46] to be able to query and walk through and
[0:00:49] just use with this MCP server. It looks
[0:00:52] like a very simple install with a pip
[0:00:53] install. I'm actually going to be using
[0:00:55] a virtual environment for this project.
[0:00:57] I'm not a Python developer, so this just
[0:01:00] makes it all the more fun for for us
[0:01:02] here.
[0:01:02] But, you know, it looks pretty pretty
[0:01:05] good. Now, what we're going to be doing
[0:01:06] or what we're going to be able to do
[0:01:07] with this is we're going to be able to
[0:01:09] load up Formula 1 sessions. We're going
[0:01:11] to be able to compare two drivers, their
[0:01:13] fastest lap, sector times, maybe some of
[0:01:15] the throttle application, and how
[0:01:17] different drivers drive differently.
[0:01:21] Okay, so the first thing that we want to
[0:01:23] do is go ahead and set up the
[0:01:24] environment so that I can start
[0:01:25] importing the code and the libraries and
[0:01:27] dependencies and all these kind of
[0:01:28] things with it. So,
[0:01:30] what I'm going to do is I'm going to
[0:01:31] jump to my terminal and we are going to
[0:01:34] create a new directory. I'm just going
[0:01:35] to say mkdir
[0:01:38] and let's just call it f1 race engineer
[0:01:42] mcp.
[0:01:44] Pretty straightforward. And let's go
[0:01:46] into this one into this directory and
[0:01:48] then I'm going to open up in code
[0:01:50] insiders. I like using insiders just
[0:01:52] because I get a lot of the nightly
[0:01:54] features or the daily features.
[0:01:56] Um and this is just a great way to test
[0:01:58] out and do a bit of dog fooding
[0:02:00] uh for the team as well. So, let's go
[0:02:02] ahead and open up Visual Studio Code
[0:02:04] Insiders.
[0:02:09] Okay, so now we have VS Code set up and
[0:02:12] open. Let's go and sort out the project
[0:02:13] itself. So, let's go and set that up as
[0:02:15] a virtual environment. So, I'm just
[0:02:17] going to drop in uh a couple of commands
[0:02:19] and this will help set up the project
[0:02:21] directory and then we're not sort of
[0:02:23] installing dependencies onto my host
[0:02:25] machine per se. We're really installing
[0:02:27] it into this kind of containerized
[0:02:28] environment. So, I'm just going to type
[0:02:29] in Python 3
[0:02:31] uh -m venv.venv.
[0:02:34] And hopefully that should run. You can
[0:02:36] see there the folder has been created in
[0:02:38] my workspace. And then I'm going to go
[0:02:40] and activate it. So, essentially go and
[0:02:43] start it so I can work within this kind
[0:02:45] of sandboxed environment. I'm going to
[0:02:47] use uh the command source uh
[0:02:49] .venv/bin/activate.
[0:02:52] And you'll notice here in my terminal
[0:02:54] I've now got a .venv. So, I'm actually
[0:02:56] now working inside of a virtual
[0:02:58] environment. So, this kind of sandboxed
[0:03:00] uh containerized uh element here.
[0:03:04] And now we've got the virtual
[0:03:05] environment set up, we can go ahead and
[0:03:08] start installing some of the
[0:03:10] dependencies we need. So, first of all,
[0:03:12] I'm actually going to upgrade pip
[0:03:13] itself. So, I'm just going to pip
[0:03:14] install
[0:03:16] uh --upgrade pip.
[0:03:18] And we will just get rid of whatever
[0:03:20] errors pop up. Like I said, I'm not a
[0:03:22] Python developer, so I'm not expecting
[0:03:23] my VS Code to have a lot of Python
[0:03:26] uh elements inside it. I can see I've
[0:03:28] got like a one or two extensions, but
[0:03:30] that's about it.
[0:03:31] Wonderful. So, that has now uh upgraded
[0:03:33] pip. Now, what I can do is I can go and
[0:03:35] get some dependencies. So, like I
[0:03:39] mentioned, we're going to be using the
[0:03:40] fastf1
[0:03:43] dependency or the import, but we're also
[0:03:44] going to be using pandas. Now, pandas is
[0:03:46] a way for us to sort of manage all of
[0:03:48] this data in one. So, we're going to go
[0:03:50] ahead and install those as well.
[0:03:54] And here we go. So, we're just going to
[0:03:56] do pip install
[0:03:58] uh
[0:03:59] matplotlib and pytest. So, that's going
[0:04:02] to allow us to work with the data,
[0:04:05] display it, and also test
[0:04:08] the code as well. Cuz that's equally as
[0:04:11] important as writing the code. There we
[0:04:13] have it. Now, what we can do is we can
[0:04:15] actually go and validate this by just
[0:04:18] typing one command in there. I'm just
[0:04:20] going to do python -c and I'm going to
[0:04:22] and this is just essentially a little
[0:04:23] bit of code that we're just dropping
[0:04:25] straight into the terminal through a
[0:04:27] command and hopefully we should see some
[0:04:30] results pop out. So, the import
[0:04:32] successfully
[0:04:34] uh installed and a version which then
[0:04:36] prints to the terminal. So, hopefully
[0:04:37] once this is run, we will see that it
[0:04:39] pops up. Wonderful. Here we can see we
[0:04:41] have got a whole couple of things. So,
[0:04:43] these are our imports that we installed
[0:04:45] uh and it's just popping out exactly
[0:04:47] what I expected to.
[0:04:50] Wonderful.
[0:04:54] Now, I've gone ahead and I have actually
[0:04:56] created some of the files and the layout
[0:04:58] for this just to save a bit of time in
[0:05:00] this video. Uh but essentially I've got
[0:05:02] the initial pi file. I've got
[0:05:04] comparisons, the data loader, MCP
[0:05:05] server, strategy inside the app folder.
[0:05:08] And then of course, I have some test
[0:05:10] files as well. However, these are all
[0:05:12] actually empty. So, what we're going to
[0:05:14] go ahead and do now is actually get the
[0:05:17] data loading
[0:05:20] with a sample application first. So,
[0:05:22] we're not going to incorporate any MCP
[0:05:23] just yet. We're just going to go ahead
[0:05:24] and get that data running. All right.
[0:05:27] So, let's close the terminal and let's
[0:05:29] start writing some code. Now, I'm
[0:05:32] actually going to use GitHub Copilot
[0:05:33] inline. So, I'm not I'm going to try try
[0:05:35] to avoid using the chat as much as I can
[0:05:37] just to show you how I actually work
[0:05:39] through problems when I'm creating these
[0:05:41] sort of applications. So, I actually
[0:05:43] want to get a data loader. I want to
[0:05:45] load some of the data which is coming in
[0:05:47] from the fastf1
[0:05:49] package. So, what I'm going to do here
[0:05:51] is I'm going to open up the data
[0:05:52] loader.py
[0:05:54] I'm going to um Oh, I'm going to import
[0:05:58] the fastf1
[0:06:01] import. And you can see here I I've
[0:06:03] automatically got like a whole bunch of
[0:06:04] suggestions, but I'm going to write a
[0:06:06] few comments and what I really want to
[0:06:08] do is I want to enable cache. So, I want
[0:06:11] the data to load once. Previous data
[0:06:13] doesn't change from any of these seasons
[0:06:15] or anything from
[0:06:17] uh prior years. It's always going to be
[0:06:19] the same. Oh, we want to get a session.
[0:06:21] So, based on a uh session code, a Grand
[0:06:24] Prix name, or, you know,
[0:06:26] a location, etc. So, I want to get some
[0:06:28] session data and then I want to actually
[0:06:31] load it. So, return that to the user.
[0:06:34] So, before I jump straight into writing
[0:06:36] some code, I'm actually going to start
[0:06:38] writing uh some comments. And so, in
[0:06:41] Python we use a like a hash tag
[0:06:44] uh just to dictate a comment. And I'm
[0:06:47] going to say enable
[0:06:49] uh cache
[0:06:51] once.
[0:06:53] After that, so that's going to hopefully
[0:06:54] just bring in the data and just load it
[0:06:56] once. That's all I needed to do. I'm
[0:06:58] then going to have a get session um
[0:07:04] information.
[0:07:06] And then I want to do a session.load.
[0:07:11] So, these are kind of what I'm expecting
[0:07:13] Copilot to really help me with. So, if I
[0:07:16] want to enable the cache once, so let's
[0:07:18] just say all right, it's already picked
[0:07:19] up from the import some of the functions
[0:07:21] that are inside the import itself. So, I
[0:07:23] am just going to use tab complete cuz to
[0:07:25] me that does look about right. Um and
[0:07:28] then from getting the session, so as I
[0:07:31] want to get the session, I want to pull
[0:07:33] that in based on some inputs. So, I'm
[0:07:35] going to do session equals fastf1
[0:07:38] uh .get_session 2023 Monaco and Q. So,
[0:07:41] that's just the um session code. You've
[0:07:43] got practice one, practice two, practice
[0:07:45] three,
[0:07:46] uh qualifying, and then you've got the
[0:07:47] Grand Prix. Unless it is a sprint race
[0:07:49] weekend and then of course, there's a
[0:07:50] different setup. However, the data will
[0:07:53] also help dictate that as well. So, what
[0:07:55] we can do is I don't need to change any
[0:07:57] of this information and then finally,
[0:07:59] the next that it suggests is which I've
[0:08:00] actually got turned on. Uh I can just
[0:08:02] hover over that
[0:08:04] uh suggestion and click go to accept
[0:08:06] because that is exactly what I wanted to
[0:08:08] do.
[0:08:10] So, now what we can go ahead and do is
[0:08:12] actually
[0:08:14] run this file. It's not quite a function
[0:08:16] yet because we haven't added a function
[0:08:17] signature.
[0:08:18] Uh but we can certainly go and run this
[0:08:20] and get back the data from qualifying in
[0:08:22] Monaco in 2023.
[0:08:24] So, the way that we do that is just by
[0:08:27] running uh the Python command. So, we're
[0:08:29] running in our virtual environment. So,
[0:08:30] let's just run Python uh let's go app
[0:08:34] and then let's do data loader. Now, we
[0:08:37] may get an error. Yes, we get an error.
[0:08:39] Of course, we do. Uh so, the reason why
[0:08:41] we've got this error is because we don't
[0:08:42] have a cache folder inside our
[0:08:47] project directory. So, we can go ahead
[0:08:48] and clear that now. And let's go and run
[0:08:51] that session again. Hopefully that
[0:08:52] should now start pulling some of the
[0:08:54] information from this session. Now, what
[0:08:57] this is doing is it's going to be
[0:08:59] writing a SQL database, I would assume.
[0:09:02] Uh and it says here, yeah, finished
[0:09:03] loading the data for 20 drivers. Uh for
[0:09:06] all these car numbers, this is the
[0:09:07] numbers of each car. So, if we look
[0:09:09] inside the cache, here we go. So, now we
[0:09:11] can look at some of the data inside. So,
[0:09:13] we've got some of the driver info.
[0:09:15] Um okay, that's a funky
[0:09:17] um
[0:09:18] output. But like we've got a SQLite uh
[0:09:21] cache database here, which we can then
[0:09:22] start going to filter through and start
[0:09:24] getting some of the data out.
[0:09:28] Now, what we can go ahead and do is
[0:09:29] actually
[0:09:30] wrap this in a function so that we can
[0:09:32] then call it with some variables. So,
[0:09:36] what I want to do is I want to do a
[0:09:37] uh function signature. So,
[0:09:40] def load. Yeah, that looks absolutely
[0:09:42] correct. And I'm not going to accept
[0:09:44] that because I already have it there.
[0:09:46] And then what we can do is we probably
[0:09:48] want to return the session at the end.
[0:09:50] So, now what we can go ahead and do is
[0:09:52] hopefully write in a command and we can
[0:09:55] do the same thing,
[0:09:56] except I'm going to
[0:10:00] in the command of 2024,
[0:10:02] but I just want to pull in 2023 like we
[0:10:05] did previously.
[0:10:07] So, I'm just going to be running this
[0:10:08] from the command line, and this is
[0:10:09] calling that function signature. So,
[0:10:11] there we go. It's using the cache data.
[0:10:13] It recognizes that that is there, and
[0:10:15] this function is now working.
[0:10:19] So, we couldn't really click into the
[0:10:20] files to see the data structure. So,
[0:10:23] what I'm going to do is I'm going to go
[0:10:24] into the record. So, I'm going to type
[0:10:26] in
[0:10:26] Oh, not that. I'm going to type into the
[0:10:28] terminal Python.
[0:10:29] And then we're going to jump into the
[0:10:32] sort of the terminal, and then we can
[0:10:34] interactively talk with the code base
[0:10:36] and test out some of these features.
[0:10:38] This is a quick way for me to jump into
[0:10:39] this function and and test it out. So,
[0:10:43] I've actually written down and copied in
[0:10:45] the
[0:10:46] function. And what we can see here is if
[0:10:49] we pull this up a little bit, we can see
[0:10:51] some of the data. And it's pulled in the
[0:10:53] data from the cache because it's already
[0:10:56] there.
[0:10:57] And then it's going to say, you know,
[0:10:59] we've got the
[0:11:01] driver number, we've got the broadcast
[0:11:03] name, abbreviation, driver ID, team
[0:11:05] name, team color, all these kind of
[0:11:07] things. But then we've also got another
[0:11:09] column, which is around laps. We've got
[0:11:11] results, and we have got laps as well.
[0:11:14] So, this is just really specifying the
[0:11:16] time, the driver, the driver number, the
[0:11:18] lap time, sector one, sector two. So, if
[0:11:20] you're into Formula One, just different
[0:11:22] sectors of the Formula One Grand Prix
[0:11:23] track. And then we can kind of work with
[0:11:27] this data. Now we know how it's laid
[0:11:29] out. Before we build any features, we
[0:11:31] can now understand what's really going
[0:11:33] on with it.
[0:11:36] So, now we've got one function working.
[0:11:38] I'm going to go ahead and create the
[0:11:39] tire strategy function and the uh driver
[0:11:43] comparison function, so we can compare
[0:11:45] two drivers and the tire strategies
[0:11:47] against different cars and different
[0:11:49] teams.
[0:12:33] Okay, so we have now got three complete
[0:12:38] files. So, we've got a tire strategy,
[0:12:40] we've got comparisons of drivers, and we
[0:12:42] have got the data loader itself, which
[0:12:44] pulls in the session data. So, what we
[0:12:46] don't have is tests. We've got no tests
[0:12:49] for any of this, and typically you do
[0:12:51] TDD, so test-driven development.
[0:12:53] However, in this scenario, I actually
[0:12:55] want to use custom agents inside Visual
[0:12:57] Studio Code and get a Copilot to help
[0:12:59] write a test suite for me.
[0:13:02] So, what I'm going to do is I am going
[0:13:05] to head over to the right-hand side, and
[0:13:07] I am going to make this box a little bit
[0:13:09] wider first of all. I'm going to click
[0:13:10] on agents, and at the bottom we've got
[0:13:12] configure custom agents. Now, here I'm
[0:13:16] going to say I can create a new custom
[0:13:18] agent. I could generate one, but I'm
[0:13:19] going to I've already written one, so
[0:13:21] I'm just going to use that. I'm going to
[0:13:22] put it in the .github agents directory,
[0:13:26] and then I'm just going to give it a
[0:13:28] name. So, I'm going to say Python
[0:13:31] uh test agent.
[0:13:34] And that's going to create a file for
[0:13:35] me. Now, with this file, I can edit it
[0:13:38] with the name, description, the argument
[0:13:39] hint, and some tools. So, after that,
[0:13:43] you then put in what you actually want
[0:13:44] the agent to specialize in. So, this is
[0:13:46] kind of like some custom instructions to
[0:13:48] some degree, but very much working with
[0:13:50] a standalone agent. So, I already have
[0:13:52] one, which I'm just going to drop in
[0:13:54] here, and we will walk through it just
[0:13:56] so you understand what I have written.
[0:13:58] So, we have got the description. Oh,
[0:14:01] it's actually missing uh the name off
[0:14:03] the top there. So, let me go put that
[0:14:06] in. Python test agent. There we go.
[0:14:09] So, we've got the description. So, use
[0:14:11] when writing Python tests, generating
[0:14:13] Pytest test cases, debugging test
[0:14:15] failures, etc. And I've got some tools
[0:14:17] as well. So, I'm actually allowing this
[0:14:19] custom agent to go in and uh use some of
[0:14:22] the APIs inside Visual Studio Code. So,
[0:14:25] VS Code, we've got execute, read, use
[0:14:27] agent mode, we've got edit files,
[0:14:29] search, web, etc. But I'm also giving it
[0:14:31] access to another MTP server I actually
[0:14:33] have installed, the Microsoft docs MTP.
[0:14:36] Now, that is because I actually want it
[0:14:38] to go ahead and use the best practices
[0:14:40] for Python testing, which is already on
[0:14:42] the Microsoft Learn documentation. So,
[0:14:44] we can go off and go and request that,
[0:14:46] pull it in, and use it.
[0:14:48] I have given it some conventions.
[0:14:51] So, typically the
[0:14:53] uh the directory that I want it to go in
[0:14:55] and work within is obviously tests,
[0:14:57] plural. I specified plural, not
[0:14:59] singular. Uh at the root of the project,
[0:15:01] we've got some prefixing for the files,
[0:15:03] we've got some um test classes that do
[0:15:06] not inherit from unittest.testcase. So,
[0:15:08] we're very much specifying that I want
[0:15:10] these to stand alone tests, and I want
[0:15:12] them to use assert. So, the conventions
[0:15:15] that I'm pulling in are very much
[0:15:17] standard, uh and this is what I'd be
[0:15:19] using anyway. So, rather than me having
[0:15:20] to go and sort of walk through this line
[0:15:23] by line and write each line of code for
[0:15:25] the test cases, I'm actually going to go
[0:15:27] ahead and just rely on this custom agent
[0:15:29] to do it. I'm going to give it an
[0:15:31] approach which I'd expect it to do. So,
[0:15:33] the way that I would look at this is
[0:15:34] obviously reading the source code,
[0:15:36] identify test cases, use fixtures, uh
[0:15:39] make sure I'm mocking external
[0:15:41] dependencies that I'm not having tests
[0:15:43] dependent on runtime, all these kind of
[0:15:46] things as well. And then I've also got
[0:15:48] some constraints. So, I'm asking it to
[0:15:49] not modify production code unless it
[0:15:52] obviously needs to do so, and even
[0:15:53] before that, it needs to ask me. And
[0:15:57] then I'm asking it to uh not add any
[0:15:59] extra dependencies beyond Pytest and
[0:16:01] Pytest Mock, which is essentially just
[0:16:04] the basic test case imports for us. And
[0:16:07] then I'm obviously making sure there is
[0:16:09] some kind of test structure for it,
[0:16:11] whether it be table test, whether it be
[0:16:13] a certain approach that you would
[0:16:14] personally use, but this is one that I'm
[0:16:16] giving it so that it can always make
[0:16:18] sure that the test cases look the same,
[0:16:20] feel the same, and are very easy to read
[0:16:22] and maintain as well.
[0:16:27] So, once I save that file, I can then
[0:16:29] look on the bottom right-hand side, and
[0:16:31] when I click on agent, you should see
[0:16:33] Python test agent actually come up at
[0:16:35] the bottom as well. So, I'm going to
[0:16:36] select that. This is going to be the
[0:16:37] custom agent that is going to be work on
[0:16:39] working on this, and I'm going to say
[0:16:44] uh cases for this application.
[0:16:50] So, now this is using GitHub Copilot
[0:16:52] Chat, and I'm using Claude Opus 4.6. So,
[0:16:56] this is, you know, it's it's a pretty
[0:16:57] beefy model. Uh it should allow me to to
[0:17:00] create these tests, and hopefully they
[0:17:01] should run first time. What I didn't
[0:17:03] actually put into the custom agent
[0:17:05] instructions, which I just thought of
[0:17:07] now, is actually how I run this
[0:17:09] application. I don't know whether it's
[0:17:10] going to know whether it's already
[0:17:11] running, whether it's running in a
[0:17:12] virtual environment or not.
[0:17:15] So, when it comes to test these uh the
[0:17:17] tests that it's writing, and when it's
[0:17:18] coming to validate them itself, we will
[0:17:21] see exactly what it tries to do. So, we
[0:17:23] can just have these files open and see
[0:17:24] what it's doing. So, uh at the moment it
[0:17:26] is going through it, searching the code
[0:17:28] base, it's looking at
[0:17:31] a whole bunch of things that I have in
[0:17:32] here. Uh it's written a to-do list. On
[0:17:34] the to-do list, it's just going to show
[0:17:36] me exactly what it's doing, what it's
[0:17:37] working through.
[0:17:39] So, it's done creating the conftest.py
[0:17:42] with shared fixtures.
[0:17:44] Uh it's now going to start looking at
[0:17:45] writing the test data loader and the
[0:17:47] test comparisons and the test strategy.
[0:17:53] We can see that it is also following the
[0:17:56] standard which I asked it to. So, we've
[0:17:58] got arrange, we've got act, and assert.
[0:18:00] So, this is very much the
[0:18:03] layout of which I expected it to. And
[0:18:06] there we have it. It's actually trying
[0:18:08] to
[0:18:10] uh restart my virtual environment. So, I
[0:18:12] can actually say the virtual
[0:18:15] environment
[0:18:18] is already
[0:18:20] running.
[0:18:21] So, I can hopefully go ahead and steer
[0:18:23] this.
[0:18:31] There we go. So, now it knows the
[0:18:32] virtual environment is already running.
[0:18:33] It may try and do this inside uh its own
[0:18:38] window. So, we'll see and there we go.
[0:18:40] Okay, so it has actually tried to We'll
[0:18:42] just pop that into a new
[0:18:46] file. Actually, what I'm going to do is
[0:18:48] I'm actually going to go ahead and just
[0:18:49] copy that, and I'm just going to drop it
[0:18:51] into here just to see if it's running.
[0:18:56] Okay, so it's actually trying to figure
[0:18:58] out
[0:19:00] a whole bunch of things. It's failed.
[0:19:02] Maybe my comment didn't actually help.
[0:19:09] I'm going to ask it to validate the test
[0:19:11] one more time.
[0:19:34] Okay, so going by what Copilot is
[0:19:36] telling me, it actually looks like it's
[0:19:39] got some passing a passing test suite.
[0:19:42] So, what I'm actually going to do is I'm
[0:19:43] just going to run Pytest on the test
[0:19:47] files. So, hopefully we can just maybe
[0:19:49] run Pytest. I'm not sure whether I need
[0:19:50] to specify
[0:19:52] a specific
[0:19:56] And there we go. It actually ran all of
[0:19:58] the tests, and we can see here at the
[0:20:00] bottom,
[0:20:01] uh 21 passed, one warning. Now, I'm not
[0:20:03] going to worry too much about that
[0:20:04] warning,
[0:20:05] um because we're not really doing
[0:20:06] anything production-ready at the moment.
[0:20:08] What I can do now is I can go ahead and
[0:20:09] click on keep. So, I'm going to hit the
[0:20:12] keep button, and now we've got a full
[0:20:14] test suite. I'm just going to close
[0:20:15] Copilot and bring down
[0:20:17] this terminal. So, we've got a full test
[0:20:19] suite, which is working. Now, of course,
[0:20:21] as a developer, I would need to go
[0:20:22] through and validate that all of these
[0:20:24] tests is working,
[0:20:25] but rather than having to write this
[0:20:27] line by line, I now have a test suite
[0:20:29] which has been written for me, which I
[0:20:30] can just go and verify.
[0:20:34] So, now we've got the test suite
[0:20:35] installed. We need to go and do the one
[0:20:37] thing that we have been wanting to do
[0:20:39] throughout this entire project, and that
[0:20:41] is turn it into an MCP server. So, what
[0:20:44] we've essentially done is created a lot
[0:20:46] of or a couple of tools for an MCP that
[0:20:49] can be utilized within an MCP server,
[0:20:51] such as the strategy for tires, we have
[0:20:53] got the driver comparisons, we have also
[0:20:56] got the session data loader. So, what we
[0:20:59] can now do is just encapsulate this and
[0:21:01] put it into a box, and then just put a
[0:21:03] wrapper on it, and say this is an MCP
[0:21:05] server. We can now utilize that with the
[0:21:08] likes of GitHub Copilot or other AI
[0:21:10] tooling that you wish. So, what we're
[0:21:13] going to do is we're going to go over to
[0:21:14] the MCP server.py
[0:21:17] file, and we're just going to drop in a
[0:21:19] very lightweight um
[0:21:22] server. Now, this is using Fast MCP.
[0:21:25] This is a great library which enables us
[0:21:27] to essentially create our own MCP
[0:21:29] servers in Python very, very easily
[0:21:31] using the mcp.tool notation. So, we
[0:21:35] don't actually have this installed, so I
[0:21:36] need to go ahead and install it.
[0:21:40] So, what I'm going to do is open up the
[0:21:41] terminal, and in the terminal I'm going
[0:21:43] to do I just make sure I'm in my virtual
[0:21:45] environment still, and I'm going to do
[0:21:48] pip install fast MCP.
[0:21:51] And that should go ahead and install
[0:21:53] fast MCP for us. So, now we have it
[0:21:55] available to us, and we can use it.
[0:21:59] So, now we've got Fast MCP available to
[0:22:01] us, and we've got an MCP server wrapper.
[0:22:04] We can use these mcp.tool decorators to
[0:22:08] wrap a function that we've written into
[0:22:10] a tool. So, I've actually gone ahead and
[0:22:13] and written this out already, but we'll
[0:22:15] walk through the code. Let's just drop
[0:22:17] this down and out the way a second.
[0:22:20] I'll close Copilot.
[0:22:22] So, we had a health check originally,
[0:22:24] but now we've actually got the load
[0:22:25] session, we have got the get tire
[0:22:27] strategy, and the comparing drivers
[0:22:30] functions that are all been pulled into
[0:22:32] this one MCP server file under a tool.
[0:22:35] So, we've got the function, which is
[0:22:38] over here on the left-hand side in a
[0:22:39] different file. We then wrap it around
[0:22:42] with the mcp.tool decorator, and then we
[0:22:45] can just grab it and sort of encapsulate
[0:22:47] it into this smaller function,
[0:22:50] allowing us to call that from our
[0:22:52] client, i.e., GitHub Copilot chat. So,
[0:22:55] now we actually have a Fast MCP server
[0:22:58] installed. We've got the tools available
[0:23:00] on the Fast MCP server. So, now we just
[0:23:02] need to go ahead and add it to
[0:23:06] VS Code. But remember, we're actually
[0:23:08] running within a virtual environment
[0:23:10] here. So, we need to be very careful as
[0:23:12] to where we place this or where we kind
[0:23:13] of point the
[0:23:15] execution to. So, let's just go ahead
[0:23:17] and add an MCP server. So, I'm going to
[0:23:19] do command shift and P on my keyboard to
[0:23:22] open up command palette. I'm going to
[0:23:24] click add an MCP server, and because
[0:23:27] we're using STDIO, we're going to make
[0:23:29] sure we select that option.
[0:23:31] And this is where we need to be really
[0:23:33] careful as to where we actually point
[0:23:35] the MCP server to. So, we would
[0:23:38] typically to run this, we would just
[0:23:40] call the sort of the MCP server
[0:23:43] file.
[0:23:45] But we can't just do that. We actually
[0:23:46] need to point it somewhere else. We need
[0:23:49] to point it to the execution
[0:23:51] or or I guess the Python
[0:23:54] binary inside the virtual environment
[0:23:56] here. So, we need to make sure that
[0:23:57] we're running still within the virtual
[0:23:59] environment, and we are calling the MCP
[0:24:02] file from that. So, what I'm going to do
[0:24:04] is I'm just going to pop this command
[0:24:05] in. Now, this is going to be different
[0:24:07] if you're running outside of a virtual
[0:24:09] environment and on your local machine or
[0:24:11] in the cloud or whatever. It's wherever
[0:24:13] you have this running.
[0:24:15] And then I'm going to call it the F1
[0:24:17] engineer
[0:24:20] uh MCP.
[0:24:21] And we're going to put it in the
[0:24:22] workspace. So, we're not going to have
[0:24:24] it global. We're just going to pop it
[0:24:25] inside this workspace. And there we have
[0:24:28] it. We have added it. It is Maybe it's
[0:24:31] running. Who knows? Let's start it up.
[0:24:33] Let's see if it's
[0:24:35] Perfect. It's actually got full tools,
[0:24:36] so you can see that it's found the full
[0:24:38] tools.
[0:24:39] You can have some configuration there.
[0:24:41] Now, what we can do is we can go ahead
[0:24:43] to Copilot, and we can just ask it a
[0:24:46] simple question of Let's do a
[0:24:49] comparison. Let's find a comparison like
[0:24:51] a good comparison.
[0:24:53] Compare Leclerc and Verstappen in 2024
[0:24:56] Monaco qualifying. Now, let's see if it
[0:24:59] is able to pick out the tool. Hopefully,
[0:25:01] the tool is selected. I didn't check
[0:25:03] that.
[0:25:05] Yes, it is selected, so it should be
[0:25:07] able to pick it up.
[0:25:09] And if we watch Copilot work,
[0:25:11] it should recognize that. Wonderful.
[0:25:13] It's asking me as the user for
[0:25:16] permission to go ahead and run this MCP
[0:25:17] server. I'm going to allow it. So, it's
[0:25:19] run the tool load session. So, it's
[0:25:22] probably going to load the session and
[0:25:23] probably compare the drivers. So, I'm
[0:25:25] going to allow that one as well.
[0:25:28] It's working through its own logic just
[0:25:30] using the MCP that we have wrapped these
[0:25:32] functions in. And there we have it. We
[0:25:34] can see the side-by-side comparison of
[0:25:36] Charles Leclerc and Max Verstappen and
[0:25:39] their qualifying times, Monaco 2024, and
[0:25:42] we can see what the delta is, we can see
[0:25:44] each individual sector and lap time.
[0:25:48] That's pretty cool. We have now got an
[0:25:50] F1 MCP server within VS Code.
[0:25:53] I guess the next challenge for you is to
[0:25:55] create a chat application where you can
[0:25:58] then just host it and call this MCP
[0:26:01] server
[0:26:02] yourself.
[0:26:05] So, there we have it. I hope you have
[0:26:06] learned how to create an MCP server
[0:26:09] inside VS Code that you can use with
[0:26:11] some clients. We've looked at the
[0:26:12] client-server model, i.e., VS Code and
[0:26:16] GitHub Copilot. We've looked at the
[0:26:17] transport, which is the STDIO. Some use
[0:26:20] HTTP, others use other methods as well.
[0:26:23] We've also looked at tool invocation,
[0:26:25] where you can invoke this and wrap your
[0:26:27] functions within tool decorators using
[0:26:30] Fast MCP. And of course, we looked at
[0:26:32] the schema discipline itself. So, the
[0:26:34] inputs are plain scalars like year, the
[0:26:37] Grand Prix, the session code, all of
[0:26:39] that kind of goodness inside the data.
[0:26:42] We've looked at a whole bunch of things
[0:26:43] in this video.
[0:26:46] The repository link for this MCP server
[0:26:48] will be in the description below. Happy
[0:26:51] coding, everyone.
