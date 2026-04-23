---
video_id: r3UkKVE3gtk
title: "Let's learn about MCP Apps"
url: https://www.youtube.com/watch?v=r3UkKVE3gtk
channel: "@BurkeHolland"
published: 2026-02-02
speakers:
  - Burke Holland
topics:
  - mcp
  - mcp-apps
  - ui
  - server
relevance: primary
---

# Let's learn about MCP Apps

Burke Holland demonstrates MCP Apps and how to build an interactive UI that works directly inside the AI chat surface.

## Agenda/Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Intro |
| 00:32 | Enabling MCP Apps |
| 00:45 | Demo: MCP Apps in action |
| 03:32 | A basic Hello World MCP Server |
| 08:08 | Adding the MCP Apps UI |
| 13:05 | Forcing AI to wait with Promises |

## Key Topics Covered

- **MCP Apps**
- **MCP server**
- **Interactive UI**
- **Tool waiting patterns**

## Full Transcript

<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

[0:00:00] Well, we got another new thing to learn today.
[0:00:02] And this time it's MCP apps.
[0:00:06] Now this one is kind of cool.
[0:00:08] For me at least I like UI and that's what MCP apps is.
[0:00:11] Is it basically a UI that MCP apps can return in the chat.
[0:00:15] So it's cool if you're a user and it's cool
[0:00:17] if you're building MCP servers in this video.
[0:00:20] We're going to look at how it works
[0:00:22] and how you can add it to your MCP server today.
[0:00:26] And then we'll look at what the practical use cases
[0:00:28] of MCP apps even are.
[0:00:30] You ready?
[0:00:31] Let's do it.
[0:00:32] Hey folks, just one other thing.
[0:00:34] I forgot to put in the video,
[0:00:35] but at the time of this recording you need to go to settings
[0:00:38] and look for MCP apps and settings
[0:00:40] and turn on this experimental feature.
[0:00:43] All right, so the easiest way to understand MCP apps
[0:00:45] is just to see them in action.
[0:00:46] So let's start with that and do that
[0:00:48] before we jump into how do you actually create one.
[0:00:52] And what we're going to do is we're going to use
[0:00:56] an MCP server to change the color of this light bulb
[0:00:58] over here and I'm going to turn you
[0:01:00] so you can watch the light bulb as it changes.
[0:01:02] So you don't need to see me, okay, bear with me.
[0:01:05] There we go.
[0:01:06] So there's an MCP server that I built
[0:01:09] that just controls the light.
[0:01:12] So we could say change the color of the lamp
[0:01:18] to blue.
[0:01:19] And this uses, and you'll see I misspell a lot,
[0:01:22] but it's fine, AI don't care.
[0:01:24] So this uses the LIFX, which is just a type of light bulb,
[0:01:29] API, and I have a key that passes
[0:01:31] and it's going to pass off and change the link color to blue
[0:01:35] and it just did, right?
[0:01:36] So that's just the simple MCP server that I built
[0:01:39] and it's this right here.
[0:01:41] Now, MCP apps, because prior MCPs could only return text
[0:01:47] in the chat.
[0:01:48] And so if the MCP server needed to get clarification from you
[0:01:52] or wanted to show you rich content, it couldn't do that.
[0:01:55] So now we have the ability to show you eyes.
[0:01:57] So what I can do here is just say,
[0:01:59] show me the lamp control panel.
[0:02:02] And this is a UI that will be returned
[0:02:06] by that same LIFX MCP server, but right in the chat.
[0:02:11] And here it is.
[0:02:14] So here it is.
[0:02:15] I built this and by myself, I mean, of course,
[0:02:18] Opus 4.5, but I can see all the lights I have.
[0:02:20] This is the one I want.
[0:02:22] I can change the color.
[0:02:23] And if you watch the lamp, it will change as I move around here.
[0:02:28] I'm sorry, I'm just moving ahead to make sure
[0:02:29] the video is updating.
[0:02:30] Yeah, it is good.
[0:02:32] Right, and then we can do effects and other things like that.
[0:02:34] And all of this is done in the chat here.
[0:02:39] Now, why would we do this?
[0:02:41] Well, because it's possible that I might come in
[0:02:45] and say something like change the color of the light.
[0:02:49] Now I have multiple LIFX bulbs.
[0:02:52] So I haven't told it what color to change it to
[0:02:54] or which bulbs I want to change.
[0:02:56] And so saw that it should be smart enough
[0:02:58] to look at this and be like, well, they didn't say,
[0:03:00] it may guess or it may just show me.
[0:03:05] Yeah, it does.
[0:03:05] So it basically says, if you see here it says,
[0:03:08] you didn't specify which light or what colors.
[0:03:11] Let me show you an interactive controller.
[0:03:12] And this is MCP apps in action here.
[0:03:15] And we're running out of space a little bit
[0:03:17] because of the zoom, let me zoom out a little bit.
[0:03:19] I apologize.
[0:03:21] So these are, this is MCP apps.
[0:03:23] This is what we're going to build.
[0:03:24] This UI can look like anything.
[0:03:26] You can build anything you want.
[0:03:28] And so let's get into how we do that.
[0:03:31] All right, now we're going to start
[0:03:33] from what I like to call absolute zero,
[0:03:35] which means we have no files whatsoever.
[0:03:37] We're starting with nothing.
[0:03:38] Now, we need a simple Hello World MCP server.
[0:03:42] And there's a couple of different ways we can do this.
[0:03:44] One from this, we could use skills.
[0:03:46] You watched my video on skills, video and skills.
[0:03:51] Since that video, there is a new site that's popped up
[0:03:54] that I wanted to show you called skills.sh.
[0:03:57] And there's all kinds of great skills in here.
[0:03:59] This site's so cool.
[0:04:01] This is from Versailles.
[0:04:02] I love the folks at Versailles.
[0:04:03] They do so many nice things for developers.
[0:04:06] Look at this.
[0:04:07] If we search for MCP, there's an MCP builder skill
[0:04:10] right from Anthrophic.
[0:04:12] And later on, there's MCP apps.
[0:04:15] If we're going to do MCP apps, which we are,
[0:04:17] there's an MCP apps skill here as well.
[0:04:21] So if you wanted to install one of these,
[0:04:23] you could just grab it, copy it, come to your terminal
[0:04:26] and Visual Studio code and run that
[0:04:29] and it will copy everything into your project, your skill.
[0:04:32] So nice, but we're not going to do that.
[0:04:34] And the reason for that is because when you're making a video,
[0:04:36] AI is really stochastic, which means I never know
[0:04:39] what it's going to do.
[0:04:40] And I feel like it's just going to confuse you
[0:04:42] if we vibe things and it doesn't come out the way I want.
[0:04:44] So what I'm going to do is create this very simple
[0:04:47] Hello World program and outcome right back to you
[0:04:50] and we'll pick it up from there.
[0:04:52] All right, let's remove the pie from the oven.
[0:04:54] You can see here I've got a package JSON here
[0:04:57] and we've got a couple different dependencies,
[0:05:01] Model context protocol SDK for TypeScript, Figlet,
[0:05:05] which creates the ASCII art that we're going to use
[0:05:07] to say hello world in our simple Hello World MCP server
[0:05:11] and Zod, which is just a schema library for TypeScript.
[0:05:16] Now I'm going to go back here.
[0:05:18] We need to take a look at the actual server file itself.
[0:05:21] It's really not that complex,
[0:05:23] but let's just take a look at what's going on.
[0:05:25] So here's our standard imports and then here at the top,
[0:05:28] this is where we're going to use Figlet
[0:05:30] to make the ASCII art.
[0:05:32] And then here's our tool, just a hello tool.
[0:05:35] Generally, generates a personalized ASCII art greeting
[0:05:39] and you can see there's a name argument
[0:05:41] with such optional defaults to world if not provided.
[0:05:44] And so here's some examples here for the model
[0:05:47] and then we're just returning that make greeting,
[0:05:52] which gives us the ASCII art back.
[0:05:55] A lot of work to just make some ASCII art.
[0:05:57] And then that's really all there's to it.
[0:06:00] So we can now add this MCP server too, Visual Studio Code.
[0:06:03] So there's a build step I already ran it
[0:06:06] and it just outputs our built file there.
[0:06:09] So let's go to MCP, add MCP server here, MCP, add server.
[0:06:14] And then the type is standard I.O.
[0:06:16] It's just running locally as a node program here.
[0:06:19] So let's just say node as the command we run and we'll call
[0:06:22] it hello world.
[0:06:24] And then we're going to put it in our workspace
[0:06:26] just so we can see all of the configuration here.
[0:06:30] Now you can see it's not actually running here.
[0:06:32] Although it was before, which is why it's picking that up,
[0:06:35] let's go ahead and for our arguments here,
[0:06:37] we just need to tell it where that JavaScript file is
[0:06:41] and it's right there.
[0:06:42] And you'll notice those the new completions kicking in
[0:06:46] is a really improved in Copilot in the last few months.
[0:06:49] So you check that out.
[0:06:50] All right, so let's go ahead and start this.
[0:06:53] So you can see it started and there's now just one tool,
[0:06:55] which is what we had.
[0:06:57] And now we can go to chat and we can actually test this.
[0:06:59] So let's go over to our chat and let's pick
[0:07:01] a small cheat model here.
[0:07:03] How about VS Code Prime.
[0:07:05] It's free and then we can just call our hello tool here.
[0:07:09] And I'll just say my name is Burke.
[0:07:13] And if we've done everything correctly,
[0:07:16] it should call our MCP server because I've mentioned it
[0:07:19] to directly and return the ASCII art greeting.
[0:07:23] And there we go, very nice.
[0:07:25] Now notice that I did call hello specifically.
[0:07:28] You'll see me keep doing that because hello
[0:07:30] is just way too broad of a thing to send a large language model.
[0:07:33] It knows how to answer hello.
[0:07:34] We'll happily do that.
[0:07:36] So now what we want to do is what happens
[0:07:38] if we just say hello.
[0:07:40] And then if you remember from the code,
[0:07:41] but do you remember what happens if we just say hello
[0:07:44] or what should happen based on the code?
[0:07:47] It just returns world.
[0:07:49] That's right.
[0:07:50] So what would be nice is if the user does not provide a name,
[0:07:53] then instead of just showing a default,
[0:07:55] we actually show a form where they can put their name in
[0:07:59] and click submit.
[0:08:00] So let's modify our applications to do that
[0:08:03] by adding MCP apps to this project.
[0:08:08] So first we need to update our package JSON file,
[0:08:10] which I did here.
[0:08:11] We need ex t apps.
[0:08:13] And then down here we need cross the NV,
[0:08:16] which we're using up here in the build command.
[0:08:17] We'll talk about that in just a second.
[0:08:19] And then we're using VIT and VIT plugin single file.
[0:08:22] And we're going to talk about why that is.
[0:08:25] So in order to understand what we're doing here,
[0:08:28] we need to understand that for MCP apps,
[0:08:30] what we're going to have is an HTML file and a TypeScript file
[0:08:32] that contains all the logic for the HTML file.
[0:08:35] And then we're going to use VIT to bundle those two things
[0:08:38] together into a single file.
[0:08:41] So to do that, we're going to need a VIT config.
[0:08:45] And our VIT config is going to look like this.
[0:08:48] Now you're thinking how am I supposed to remember
[0:08:49] all this code?
[0:08:50] You're not.
[0:08:51] We talked about their skills for doing this.
[0:08:53] The AI can do this.
[0:08:54] There's documentation for doing this.
[0:08:56] We're just doing it by hand so that we can learn
[0:08:57] without the AI getting in the way.
[0:09:00] So here's our config here.
[0:09:02] And then when we run a build, it will call this VIT.
[0:09:05] And it will bundle our two files together.
[0:09:07] Then it only exists yet.
[0:09:08] But let's create them now.
[0:09:10] So we're going to put the HTML file at the root of our project
[0:09:13] here.
[0:09:14] And let's just call it ncpapp.html.
[0:09:17] So here's our HTML file.
[0:09:19] And you can see here that it's pretty simple.
[0:09:21] We've got a very simple CSS framework
[0:09:23] we're using called PICO.
[0:09:25] And then it's a very simple form that just
[0:09:27] says, enter your name with a submit button.
[0:09:29] Very, very simple here.
[0:09:31] We could even preview this, although it won't look great.
[0:09:34] But that's essentially what it will look like in the chat.
[0:09:37] OK.
[0:09:38] Now the logic for this is coming from this SRCMCP app.ts,
[0:09:42] which does not exist.
[0:09:43] So let's create that.
[0:09:45] So I'm going to go to the source folder here
[0:09:46] and create a new file called mcpapp.ts.
[0:09:50] So let me grab the code for that.
[0:09:51] All right.
[0:09:51] So this is all of the logic that's
[0:09:53] going to end up in this HTML file to control that HTML file.
[0:09:58] And this is going to, if you've written JavaScript before,
[0:09:59] it's exactly what this is.
[0:10:01] There's like, document.getElementByID, things like that.
[0:10:05] So as we go down here, you can see that on the submit,
[0:10:08] what we're going to do is we're going to call the server tool.
[0:10:12] So what's the server tool?
[0:10:13] It's hello.
[0:10:14] It's this hello tool right here.
[0:10:17] So that's the cool thing about mcpapps
[0:10:19] is that they're bi-directional.
[0:10:21] So the form can call the server and the server
[0:10:22] can call back.
[0:10:23] And we're going to get the result here.
[0:10:25] And then we're going to pass in the name,
[0:10:28] which we're pulling from the form, pass that to the tool,
[0:10:31] and then get back the ASCII art.
[0:10:33] And then here, this is kind of the weird way
[0:10:35] you have to pull the text out of the response here.
[0:10:39] And then we're going to set the greeting element
[0:10:41] in our HTML to be that an escape HTML
[0:10:45] to make sure everything's safe.
[0:10:46] So in our index file here, we're going
[0:10:48] to add in a couple of packages here at the top.
[0:10:51] We're going to pull in from the ext apps packages,
[0:10:54] as well as using some file system and path modules
[0:10:58] for node.
[0:10:59] And then we just need to tell our mcp server
[0:11:03] about this UI resource.
[0:11:05] And we do that with this UI scheme here.
[0:11:08] And this UI scheme tells the host, as the comment says,
[0:11:12] that this is an mcp app resource here.
[0:11:14] And now we need to add another tool
[0:11:17] that the mcp server can call to show that UI.
[0:11:20] So let's come down to the bottom of our file here.
[0:11:23] We're going to add a new register app tool here.
[0:11:28] called show get name.
[0:11:29] So that's the name of this tool.
[0:11:31] And it shows a UI.
[0:11:32] And here, this is super important.
[0:11:35] So that resource UI we specified, that specified here.
[0:11:38] And this is how the mcp server knows this meta tag
[0:11:42] that this is an mcp app here.
[0:11:44] And then we're just returning nothing out of the content
[0:11:46] here because we don't care about that.
[0:11:48] We only care about the UI.
[0:11:50] Finally, we need to actually register this UI resource.
[0:11:53] So you can see here, we're reading in,
[0:11:55] reusing that path to get the HTML file from here,
[0:11:59] read it in, and then return this as the UI.
[0:12:03] So several steps here, but this is how you configure mcp apps
[0:12:08] if you're going to do it manually.
[0:12:11] Now that we have this, so let's go ahead and run a build.
[0:12:20] OK, and now let's go restart our mcp server.
[0:12:24] OK, and now we have two tools instead of just one.
[0:12:26] So let's go back here.
[0:12:28] And let's call the, I think it was called show get name.
[0:12:31] So we'll just call show get name directly here.
[0:12:34] And see if we can get it and force it to show us this input form.
[0:12:40] And there we go.
[0:12:42] Let's see here, we can collect that works perfect.
[0:12:44] And now if we say put our name in and say,
[0:12:47] Burke, what happens?
[0:12:48] Let's say hello.
[0:12:50] And it calls the mcp server, which returns the ASCII art
[0:12:54] and shows it right there.
[0:12:55] Perfect, exactly what we wanted.
[0:12:57] Now, one thing to notice here is that the chat actually
[0:12:59] finishes even after opening the form,
[0:13:03] because we didn't return anything.
[0:13:06] We returned it nothing from this, actually.
[0:13:08] You can see our input was that, but we didn't
[0:13:10] we didn't get anything back.
[0:13:11] And so the chat doesn't wait.
[0:13:13] It just shows the form and then finishes.
[0:13:15] So what would happen if we actually wanted to show a form
[0:13:19] and then have the chat wait for our input?
[0:13:22] Because that could be one use case for mcp apps
[0:13:25] is that we want a solicit feedback from the user.
[0:13:27] We want to use mcp apps to do it.
[0:13:29] We want the chat to wait.
[0:13:30] So to do that, we're going to need to use a promise
[0:13:34] and return that promise unresolved
[0:13:36] and then have the chat wait until that promise resolves.
[0:13:39] And I'm going to show you how to do that.
[0:13:41] All right, so let's go over to our index file here, which
[0:13:44] is our mcp server.
[0:13:47] And the first thing that we're going to want to do
[0:13:48] is declare at the very top here, our promise, which
[0:13:52] we're going to return.
[0:13:53] And that's pretty simple.
[0:13:54] It looks like this.
[0:13:55] We're just at this point, we're just declaring it.
[0:13:57] We're not actually doing anything with it.
[0:14:00] And now in our mcp app.ts file here,
[0:14:05] instead of calling this tool hello, what we want to do
[0:14:09] is create a new tool called Submit Name.
[0:14:13] So we need to add this new submit to the mcp server.
[0:14:18] So let's do that.
[0:14:19] So here's our first tool.
[0:14:20] Hello, so we can collapse this.
[0:14:22] And here's our second one, which is ShowGetName.
[0:14:25] And then we're going to create a third one here called Submit Name.
[0:14:28] And it's going to be subtly different.
[0:14:31] Now, the way that it's going to be most different
[0:14:34] is that its visibility is only to the mcp app.
[0:14:38] So the chat can't actually see this tool.
[0:14:40] It can't call it.
[0:14:42] Only the app can call this tool.
[0:14:43] So that's another benefit of mcp apps.
[0:14:46] Is that some things you can specify that are tools
[0:14:48] for the mcp server that only your app can call?
[0:14:52] And now we're going to go to our ShowGetName,
[0:14:54] which shows the form.
[0:14:55] And instead of returning nothing,
[0:14:58] we're actually going to return that promise.
[0:15:00] So we're saying await the value of this, right?
[0:15:04] This and this is what we're going to actually return up
[0:15:08] to the chat.
[0:15:09] Because what we want the chat to do
[0:15:10] is display the ASCII art equivalent of what we put in.
[0:15:13] So we need to have it wait here until it gets this back.
[0:15:17] And then it can display it in the content.
[0:15:20] So if you follow, it's going to show the UI.
[0:15:23] It's going to get this, it's going to wait on this resolve.
[0:15:26] It's not going to get anything back.
[0:15:27] It's just going to sit here and spin in the background
[0:15:29] and wait.
[0:15:30] And then when this resolves, then this line gets called
[0:15:32] and actually returned to the chat.
[0:15:35] The last thing we need to do is make sure
[0:15:36] that our mcp app is up to date.
[0:15:39] So we're going to remove all of this greeting text here.
[0:15:43] And we're just going to call that tool.
[0:15:46] So it was a server tool, call server tool.
[0:15:48] And I believe it was a name.
[0:15:51] And the name was submit name.
[0:15:54] There we go.
[0:15:55] And the arguments are name.
[0:15:57] And we don't need to handle the callback here
[0:15:58] because we're sending everything back to the chat.
[0:16:01] And so we're just going to send it and forget about it.
[0:16:04] We don't need to know anything about it.
[0:16:06] All right.
[0:16:06] Let's go ahead now and run a build.
[0:16:09] And then we just need to go over to our mcp.
[0:16:12] Jason here.
[0:16:13] And we need to go ahead and restart that server.
[0:16:16] So I've restarted it.
[0:16:17] You can see there's now three tools.
[0:16:19] Now I thought we said it wouldn't be visible one of those tools.
[0:16:23] Well, it's not.
[0:16:23] If we come here and we look for what did we call it?
[0:16:27] It was called the submit.
[0:16:28] You can see it's not there.
[0:16:30] Can't actually be seen.
[0:16:31] Now it can be seen from the app.
[0:16:33] It just can't be seen from the chat.
[0:16:35] But we can still call our show get name.
[0:16:38] And we'll do that with this free included model here.
[0:16:40] And this should allow us to enter our name in the form.
[0:16:45] And the chat should wait for us to do that.
[0:16:48] So you see a waiting here?
[0:16:49] It's waiting.
[0:16:51] It's still running.
[0:16:51] It's just waiting.
[0:16:52] And it will just sit here and wait.
[0:16:54] Enter our name.
[0:16:55] Click say hello.
[0:16:59] And then it actually gets resolved.
[0:17:02] And the chat continues on.
[0:17:03] And you can see the value that we passed in the form
[0:17:06] actually gets sent back to the chat and displayed right here.
[0:17:10] And that is your crash course on mcp apps.
[0:17:16] And if you made it through all of this,
[0:17:17] then you understand a lot about mcp apps now.
[0:17:21] Again, you can check out these skills here skills.sh.
[0:17:27] You can look for mcp builder.
[0:17:29] And you can also look for mcp apps.
[0:17:31] If you just search for mcp apps,
[0:17:33] you'll find an mcp apps creator skill here as well.
[0:17:37] And if I wasn't making a video, this
[0:17:39] is what I would use to build my apps
[0:17:42] instead of writing everything by hand.
[0:17:44] It just works better that way when you want to actually
[0:17:46] understand what's going on.
[0:17:49] That's it.
[0:17:50] And now you understand mcp apps pretty well.
[0:17:54] And you can go ahead and either build your own,
[0:17:56] add them to mcp servers.
[0:17:58] Or you can now expect to start seeing them in places
[0:18:02] where you use AI.
[0:18:04] These rich interfaces for things like charts,
[0:18:06] if you ask about data, or possibly in org chart,
[0:18:10] if you ask about an organization.
[0:18:12] Because AI shows up in more places than just Visual Studio
[0:18:15] code.
[0:18:15] And so you'll start to see these rich interfaces appearing
[0:18:18] in places.
[0:18:18] And those are mcp apps.
[0:18:21] Thank you for watching.
[0:18:22] And as always, happy cutting.
