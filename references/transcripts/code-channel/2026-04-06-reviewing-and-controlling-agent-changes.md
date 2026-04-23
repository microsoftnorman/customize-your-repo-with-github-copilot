---
video_id: oFSJs6RnFt4
title: "Reviewing and controlling agent changes"
url: https://www.youtube.com/watch?v=oFSJs6RnFt4
channel: "@code (Visual Studio Code)"
published: 2026-04-06
speakers:
  - Gwyneth Peña-Siguenza
topics:
  - agent-sessions
  - steering
  - review
  - checkpoints
  - todos
relevance: primary
---

# Reviewing and controlling agent changes

In this video we'll cover reviewing, controlling agent changes and forking our session.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | In this session |
| 00:23 | Editing messages |
| 01:15 | Steering messages |
| 02:25 | Reviewing the code |
| 04:03 | Forking the session |
| 06:00 | Todos |
| 06:50 | Restore checkpoints |
| 07:19 | In summary |
| 07:42 | What's Next - Agent Sessions and Where Agents Run |

## Key Topics Covered

- **Agent Sessions**
- **Steering**
- **Review**
- **Checkpoints**
- **Todos**

## Links

- https://youtu.be/0CsKOO7d35I
- https://aka.ms/vsc-learn
- https://x.com/madebygps
- https://x.com/code
- https://aka.ms/VSCode/LinkedIn
- https://bsky.app/profile/vscode.dev
- https://github.com/microsoft/vscode

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] In the last video, we understood the
[0:00:02] different approval levels that we have
[0:00:04] so our agents can run commands. And in
[0:00:06] this video, we're going to cover a
[0:00:08] couple of concepts that will allow us to
[0:00:11] steer and change the work that is
[0:00:13] happening in the moment. And
[0:00:15] additionally, we'll view the different
[0:00:17] options we have to actually review the
[0:00:19] changes that our agent has made. Let's
[0:00:22] dive right in. All right, so like I had
[0:00:24] mentioned in the previous video, I
[0:00:26] already know there's a change I wanted
[0:00:27] to do. So instead of doing a follow-up
[0:00:30] message, I personally like to just edit
[0:00:33] messages. That way, there's a cleaner
[0:00:36] sort of chain of actions versus a bunch
[0:00:38] of follow-ups to correct functionality.
[0:00:41] So instead, we can click on a message
[0:00:43] and then here I'll say the input should
[0:00:47] be provided by a CLI argument. Great.
[0:00:51] And then I'll go ahead and send that off
[0:00:53] and then this will say, "This will
[0:00:54] remove your last request and undo the
[0:00:56] edits made to main.py." I can go ahead
[0:00:58] and click yes there. And then we're back
[0:01:01] to a very simple main.py and it'll go
[0:01:04] ahead and implement the functionality
[0:01:06] that I have now asked for, right? So
[0:01:08] here we say, "Let me look at the current
[0:01:10] state of the workspace and understand
[0:01:12] what's already there before making
[0:01:14] changes, right?" And as this is working,
[0:01:17] you can also steer it. And I can say,
[0:01:19] "Also add tests, please."
[0:01:22] And then here if I right click, I can
[0:01:24] hit steer with message. Not right click,
[0:01:27] I meant the drop down here to the right.
[0:01:29] And what this will do is actually yield
[0:01:32] upon the next action. So the agent will
[0:01:35] consider this message that we provided
[0:01:39] for steering,
[0:01:40] right? And I'll just type in a letter
[0:01:42] here so I can show you the other options
[0:01:43] we have. Stop and send, which will stop
[0:01:46] the action completely or stop the agent
[0:01:48] completely and send the message, add to
[0:01:50] queue, which will queue this message to
[0:01:52] send after the current request
[0:01:53] completes, or steer, which will send the
[0:01:56] message at the next opportunity
[0:01:58] signaling the current request to yield,
[0:02:00] right? Which is what we did here, right?
[0:02:01] So not only did I edit that first
[0:02:04] message, I also provided a message and
[0:02:07] sent it to steer the action or steer the
[0:02:10] agent's actions there as well, right? So
[0:02:13] it is now writing our tests. So we can
[0:02:16] kind of smooth this down here so we're
[0:02:18] able to view all of the code that gets
[0:02:22] generated. And the next thing I want us
[0:02:25] to review is sort of how we can review
[0:02:28] the actual code, right? It looks like it
[0:02:30] finished here. It has now created the
[0:02:33] tests here for us and it should have
[0:02:35] also provided
[0:02:36] CLI argument here. Yes. And we can go
[0:02:40] ahead and ask it to give us some
[0:02:43] examples. So give me some examples to
[0:02:47] run my CLI
[0:02:49] encoder decoder
[0:02:52] CLI, right? And whenever the agent
[0:02:55] finishes editing files, you can see the
[0:02:58] status or summary right above the chat
[0:03:02] box. We have changes to two files, total
[0:03:05] 78 code lines added and two removed, and
[0:03:08] then we can either keep all the changes
[0:03:10] here or we can keep all of them per
[0:03:13] profile here as well. Or we can go file
[0:03:16] by file. We can open each file here,
[0:03:18] right? Main. And we can keep individual
[0:03:21] changes. The additions are in green and
[0:03:24] whatever was removed is going to be in
[0:03:26] red. And then everything else is going
[0:03:28] to not have any color. Or you can keep
[0:03:31] all the changes profiled down here as
[0:03:33] well. Or we can just click keep here to
[0:03:35] keep the rest of the changes there. Just
[0:03:37] to verify that it's working, we'll go
[0:03:39] ahead and run this example here. It says
[0:03:41] it's supposed to work, so let's see if
[0:03:43] it actually works. Well, that one was
[0:03:45] pretty simple, right?
[0:03:46] But let's give it a another one. Let's
[0:03:49] say 62.
[0:03:51] And there we go. We can do one more.
[0:03:53] Let's do 1 2 3 2 3 4 5 6 there. And
[0:03:58] there we go. Looks like that is working
[0:04:00] perfect for us. Okay. We have already
[0:04:03] done some reviewing files. We did some
[0:04:06] edits. We did some steering. But from
[0:04:08] here, let's say we wanted to sort of
[0:04:12] fork this into a different session. Like
[0:04:15] we want to kind of explore a different
[0:04:17] direction for this functionality. Well,
[0:04:19] I can say /fork, right? Or I can go
[0:04:24] above here where an
[0:04:27] agent action is
[0:04:28] completed. So like a an amount of work
[0:04:31] here. And I can click on this fork icon.
[0:04:33] I can also restore and we'll talk about
[0:04:35] that in a second, right? So restore
[0:04:38] checkpoint will essentially restore the
[0:04:40] work up until this point. And then
[0:04:42] forking will go ahead and send this over
[0:04:44] to another session. I can also just use
[0:04:46] fork in the chat. I'll just do fork. And
[0:04:50] then we are immediately taken to the new
[0:04:53] forked session, right? We have our
[0:04:55] original session here and then we have
[0:04:56] our forked one here. And you can see
[0:04:58] that that brings over all of our history
[0:05:02] of our session. And this is ideal if we
[0:05:04] want to sort of start exploring
[0:05:06] different functionality. Like if I
[0:05:07] wanted to say, "We'll add main as the
[0:05:09] context here and refactor to to an API
[0:05:14] to a to a fast API." We can have that
[0:05:17] running in this session. And then that
[0:05:20] leaves our original session for us to if
[0:05:23] we want to, I don't know, have
[0:05:24] clarifying more examples or if we want
[0:05:28] to continue building more tests or
[0:05:32] flushing out any other details here. And
[0:05:34] we can explore other things in a forked
[0:05:37] session if we'd like, right? Now, there
[0:05:39] is also another functionality here which
[0:05:43] is restore checkpoint. So let's say I
[0:05:47] just hit allow all commands in the
[0:05:49] session, right? We'll move this over
[0:05:50] here. We've got a We've got a lot open
[0:05:52] here. I'm just going to do that here.
[0:05:54] I'll have our chat and then we'll move
[0:05:55] this over here. Perfect. So it is
[0:05:57] outlining here a to-do list for itself
[0:05:59] and it's going to go ahead and refactor
[0:06:01] this from a CLI to a fast API. We can
[0:06:05] see the work done here. And let's say I
[0:06:08] actually don't want this work done. I'm
[0:06:11] going to actually let it complete there
[0:06:13] so I can show you how the restore
[0:06:14] checkpoint functionality works. But it's
[0:06:16] working through is the last thing it's
[0:06:18] doing is updating the tests for HTTP
[0:06:21] endpoints, which makes sense of course
[0:06:23] because the tests were originally made
[0:06:25] for the CLI, right? And these tests are
[0:06:28] going to are going to look a little
[0:06:29] different, right? And I'm going to click
[0:06:31] on the terminal icon and we'll just
[0:06:33] click on the hidden terminal because
[0:06:35] this is where this agent is working
[0:06:37] right now. And there are 36 tests now,
[0:06:39] which are a lot more than what we had
[0:06:41] previously. And it looks like it is
[0:06:43] about to wrap up work because it's
[0:06:45] checked off all of its to-dos.
[0:06:47] Fantastic. So I'm going to minimize this
[0:06:49] here. Now, let's say I don't want any of
[0:06:51] this. I can actually click restore
[0:06:54] checkpoint and we'll restore to here.
[0:06:56] And this will remove your last request
[0:06:58] and undo edits made to two files in your
[0:07:00] working set. Do you want to proceed?
[0:07:02] I'll click yes. And this allows us to go
[0:07:04] back to where our files in our code base
[0:07:07] was in up until this point, which is
[0:07:10] ideal in case you're experimenting, in
[0:07:12] case there was a big change that you
[0:07:14] don't want to do or whatever it is.
[0:07:17] Check out checkpoints for that. And that
[0:07:19] is it for this video and we covered a
[0:07:21] lot, so please feel free to review at
[0:07:23] your own pace. We understand how to edit
[0:07:27] a prompt. We understand how to steer our
[0:07:30] agent. We understand how to accept all
[0:07:34] the changes, undo changes, accept
[0:07:36] individual changes as well. And we
[0:07:39] finally saw how we can fork a session.
[0:07:42] Now, we now have a couple of sessions.
[0:07:45] So in the next video, what we're going
[0:07:47] to do is review the session view, see
[0:07:49] how we can keep tabs on all the work
[0:07:51] that is going on. So I'll see you in the
[0:07:53] next video.
