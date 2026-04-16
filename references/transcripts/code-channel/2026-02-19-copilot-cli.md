---
video_id: _l3UO1oUoec
title: "Copilot CLI in VS Code"
url: https://www.youtube.com/watch?v=_l3UO1oUoec
channel: "@code (Visual Studio Code)"
published: 2026-02-19
speakers:
  - Alex Weininger
topics:
  - copilot-cli
  - terminal
  - cli-integration
relevance: primary
---

# Copilot CLI in VS Code

Alex Weininger demonstrates the GitHub Copilot CLI — terminal-first agent workflows, slash commands, and integration with VS Code sessions.

## Key Topics Covered

- **Copilot CLI overview** — Terminal-first agent
- **Commands** — Slash commands and configuration
- **VS Code integration** — How the CLI integrates with editor sessions
- **Demos** — Real workflows in the terminal

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Uh hello everybody. I'm Alex. Um I'm a
[0:00:02] VS Code on the Azure tools for VS Code
[0:00:05] team. And today I'll be showing off a
[0:00:07] bunch of features
[0:00:10] that make it easier.
[0:00:13] Uh today I'll be showing off a bunch of
[0:00:15] features.
[0:00:20] Uh today I'll be showing off a bunch of
[0:00:21] features that make it easier to use the
[0:00:24] uh copilot CLI uh alongside VS Code. Um,
[0:00:28] so to summarize, the features I'll be
[0:00:30] going over today is the new slash ID
[0:00:33] command in the CLI, uh, the new diff
[0:00:36] feature, uh, showing CLI sessions in the
[0:00:40] VS Code sessions view, and, uh, sharing
[0:00:43] the active editor context, uh, from VS
[0:00:46] Code to the CLI.
[0:00:48] Now, if you're not familiar with the
[0:00:49] GitHubs copilot CLI, um, it's an agentic
[0:00:52] co-pilot experience that's all packaged
[0:00:55] into a command line tool. Um, if you're
[0:00:57] watching earlier, it's what uh Burke is
[0:00:59] using to vibe code his uh Rust web app.
[0:01:03] Um, and if you want to try out the
[0:01:05] Copilot CLI for yourself, uh, the
[0:01:07] installation instructions are located on
[0:01:09] the uh, GitHub repositories uh, readme.
[0:01:14] Now, as I get into my demo, I'm going to
[0:01:16] switch to my uh my terminal. And quick
[0:01:20] note, uh, everything I showed today, uh,
[0:01:22] for all the CLI features, um, they're
[0:01:25] available whether you're using an
[0:01:26] external terminal or if you prefer to
[0:01:29] use the VS codes integrated terminal.
[0:01:32] And actually later in the demo, I'll be
[0:01:33] switching over to the VS code uh,
[0:01:35] integrated terminal.
[0:01:40] And then so the first thing I'm do
[0:01:43] create a new u demo project folder. I'll
[0:01:46] be doing very complicated tic-tac-toe
[0:01:49] app.
[0:01:52] And the first thing I'll do is start up
[0:01:54] my VS Code window in this new folder.
[0:01:58] Um, and VS Code will ask me if I trust
[0:02:00] this folder. I'll say yes. I'm sure many
[0:02:03] of you have seen this prompt before. I'm
[0:02:05] going to head back into the terminal and
[0:02:07] I'm going to start the Copilot CLI. You
[0:02:09] do that by just typing Copilot.
[0:02:13] That'll start up the uh the copilot CLI.
[0:02:15] And since I already opened uh this
[0:02:18] folder NBS code, two things happen
[0:02:20] behind the scenes. First, the copilot
[0:02:24] CLI skipped the um typical trust prompt
[0:02:27] that you would see in the CLI. Um that
[0:02:30] is because I just marked it as trusted
[0:02:32] in VS Code and that trusted workspace
[0:02:35] information is shared from VS Code to
[0:02:37] the CLI.
[0:02:39] Um, and the second thing that happens is
[0:02:41] if you notice right here, it says
[0:02:43] connected to v Visual Studio Code
[0:02:45] Insiders.
[0:02:47] Um, it has automatically connected to
[0:02:50] the VS Code window that I just opened.
[0:02:52] Um, because it it recognized that that
[0:02:54] VS Code window has the same folder open,
[0:02:57] I should automatically connect to it.
[0:03:00] And the first uh little feature I want
[0:03:03] to show off is the new command / IDE. Uh
[0:03:06] this command allows you to manage that
[0:03:08] connection between the CLI and VS code.
[0:03:11] You run it by typing / ID. Hit enter.
[0:03:14] And now two things happening on this
[0:03:16] screen. Um at the top it gives a brief
[0:03:19] summary about all the features that are
[0:03:22] um you know brought to you because of
[0:03:24] this connection. As I just mentioned it
[0:03:27] says you know the CLI automatically
[0:03:29] connects to VS Code when your workspace
[0:03:31] matches the current folder. And then it
[0:03:34] goes over some of the other features
[0:03:35] that I'll be showing um next. And then
[0:03:38] at the bottom here, you can use the
[0:03:39] arrow keys to maybe change which VS Code
[0:03:43] window you want to uh connect the CLI
[0:03:45] to. You can also disconnect all
[0:03:48] together. Um but since this is already
[0:03:50] configured automatically, I don't have
[0:03:52] to do anything. I'll just press escape
[0:03:53] to cancel.
[0:03:56] Um now I'm ready to create my project.
[0:03:59] I'll say create tic-tac-toe
[0:04:02] in vanilla JavaScript.
[0:04:06] I'll tell it to keep the HTML, CSS, and
[0:04:09] JS files separate.
[0:04:14] So, um, it'll go work for me now. And as
[0:04:18] soon as it's done, um, that's when we'll
[0:04:20] get into the next feature. Um, so now
[0:04:23] that it's done thinking, it is asking me
[0:04:26] if for permission to edit this file and
[0:04:29] to create the files that I asked it to
[0:04:30] create. Now, typically you would review
[0:04:33] this in the CLI. Um, however, I prefer
[0:04:36] to review code in VS Code. So, the new
[0:04:39] feature that we've added, it actually
[0:04:41] utilizes VS Code's diff view features,
[0:04:44] so you can review the proposed changes
[0:04:46] from the CLI right inside of VS Code.
[0:04:48] Um, and I can accept or reject these
[0:04:51] changes using the top these buttons in
[0:04:53] the top right corner. So, I'll go ahead
[0:04:56] and accept all the uh, you know, this
[0:04:59] looks good to me. That looks good to me.
[0:05:02] And I go back to the CLI and I see, you
[0:05:05] know, it has created all three files.
[0:05:09] Now,
[0:05:11] now that it's created the project, I
[0:05:13] actually want to switch into VS Code
[0:05:15] because maybe you prefer using the
[0:05:16] integrated terminal. So, I'm going to
[0:05:18] exit this CLI session uh here. And then
[0:05:21] I'm going to switch to VS Code. And then
[0:05:24] if I go up into this uh this button
[0:05:26] here, it says one unread session. Um now
[0:05:29] our session that we just had on the
[0:05:31] terminal is listed here um in the
[0:05:33] sessions view. And I can rightclick this
[0:05:35] and select resume and integrated
[0:05:37] terminal. And that'll take me right back
[0:05:39] to where I was working outside of VS
[0:05:41] Code, but now I'm inside of VS Code.
[0:05:44] I'll go ahead and close the uh the
[0:05:46] sessions view and I'll going to open
[0:05:50] these folders up in a split view.
[0:05:55] Okay, so now let's begin to edit our
[0:05:57] project.
[0:05:59] And the first thing I want to point out
[0:06:01] is this indicator in the bottom right.
[0:06:04] Uh you can see that it actually is
[0:06:06] showing what the active file is in VS
[0:06:08] Code.
[0:06:10] This is an indicator of what context is
[0:06:12] being automatically added to the copilot
[0:06:15] CLI um prompt. And so essentially the
[0:06:20] CLI now is aware of what files you are
[0:06:22] working in in VS Code. And it also u is
[0:06:25] aware of what you're highlighting. I can
[0:06:28] demonstrate this uh by let's say we want
[0:06:31] to change the O players color to purple.
[0:06:34] I can just say change this to purple. It
[0:06:36] knows what I'm highlighting. You know,
[0:06:38] there are many colors in this file that
[0:06:40] it could have changed, but it knows that
[0:06:42] I'm talking about cell uh the player O's
[0:06:45] colors because I have it highlighted.
[0:06:47] And then once again, I can use the new
[0:06:49] diff view feature to accept these
[0:06:50] changes.
[0:06:53] Um, and there we go.
[0:06:56] Uh, the next feature I want to point out
[0:06:58] is in the CLI, you can appmentntion
[0:07:01] files. Um, this is a really great way to
[0:07:03] guide copilot or scope down your request
[0:07:06] to specific files if you know that it
[0:07:08] should be reading or editing specific
[0:07:10] files and you can mention multiple
[0:07:12] files.
[0:07:13] Um,
[0:07:15] and a shortcut that we built on top of
[0:07:17] this if you're working inside of VS Code
[0:07:20] is the new command add file to copilot
[0:07:23] CLI. So, what this does, which I just
[0:07:26] ran it, uh, it adds an app me an app
[0:07:29] file at mention reference for the
[0:07:31] current file into the prompt. So, I can
[0:07:33] go in any file and it'll just add that
[0:07:36] to the prompt really quick and easy. And
[0:07:38] it also works if you have highlighted
[0:07:40] text, it'll add that file and also
[0:07:43] include the selection information.
[0:07:45] So, that's the last little uh tip and
[0:07:48] trick that we've added. Um, I'll send it
[0:07:52] back to Burke and Pierce in the studio.
