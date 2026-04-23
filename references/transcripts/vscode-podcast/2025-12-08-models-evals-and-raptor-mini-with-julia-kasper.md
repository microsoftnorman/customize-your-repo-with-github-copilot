---
series: VS Code Insiders Podcast
episode: 16
title: "Models, Evals, and Raptor Mini with Julia Kasper"
url: https://www.vscodepodcast.com/16
transcript_url: https://media24.fireside.fm/file/fireside-images-2024/podcasts/transcripts/f/fc261209-0765-4b49-be13-c610671ae141/episodes/a/a70c9acd-9575-41f3-9ec5-ef6d30e7b9a5/transcript.txt
audio_url: https://aphid.fireside.fm/d/1437767933/fc261209-0765-4b49-be13-c610671ae141/a70c9acd-9575-41f3-9ec5-ef6d30e7b9a5.mp3
published: 2025-12-08
duration: 24:20
transcript_available: true
---

# Models, Evals, and Raptor Mini with Julia Kasper

This episode was sourced from the official VS Code Insiders Podcast site.

## Episode Summary

        In this episode of the VS Code Insiders podcast, James sits down with Julia to explore the fast-changing world of AI models inside VS Code. They dive into how developers can evaluate models, the role of fine-tuning, and why speed versus complexity matters. From Raptor Mini to Sonnet, this conversation reveals the behind-the-scenes work shaping your coding experience today.

Follow VS Code:


X: https://x.com/code
Bluesky: https://bsky.app/profile/vscode.dev
YouTube: https://youtube.com/code
LinkedIn: https://www.linkedin.com/showcase/104107263
GitHub: https://github.com/microsoft/vscode
Special Guest: Julia Kasper.
      

## Transcript Status
An official transcript was available on 2026-04-21.

## Full Transcript
1
00:00:00,000 --> 00:00:09,000
Welcome back everyone to the VS Code Insiders podcast.
Your one stop shop for your favorite code editor with the team behind it.
Today with me, the one and only Julia Castro. How's it going?

2
00:00:09,000 --> 00:00:21,000
I'm good. How are you, James?
I am absolutely delightful and yes I am your host today, James Montemagno.
We have worked together for, like, ever, basically.

3
00:00:21,000 --> 00:00:36,000
I'm excited to be here. Our paths have crossed multiple times.
Now I'm back working in the IDE space, so yeah.

4
00:00:36,000 --> 00:00:51,000
When you joined the VS Code team, I was really excited.
You've worked on many things in VS Code, but one of the more advanced topics is models and evaluations.
I want to dive into that.

5
00:01:19,000 --> 00:02:03,000
The most exciting thing is how AI has changed how developers work.
It speeds up development in amazing ways and feels like a mix of low-code and traditional coding.

6
00:02:14,000 --> 00:02:45,000
Developers often ask why I pick certain models like GPT-5 mini.
Sometimes it's just a vibe — smaller models are fast and free.
But how should developers think about choosing models?

7
00:03:18,000 --> 00:04:19,000
At first I stuck with one model, but now I switch depending on the task.
We continuously evaluate models, and sometimes older ones improve, so it's worth revisiting them.

8
00:04:47,000 --> 00:05:29,000
Why does a model feel different week to week?
We change custom prompts based on feedback and evaluations.
That’s why behavior can shift even after launch.

9
00:05:55,000 --> 00:07:17,000
Was Sonnet 4.5’s behavior change due to us or the provider?
Both. Providers update checkpoints, and we adjust prompts on the client side.

10
00:07:17,000 --> 00:09:10,000
Fine-tuning means taking a base model and training it with developer workflows.
Microsoft’s team fine-tunes models like Raptor Mini to optimize for speed and repetitive tasks.

11
00:09:49,000 --> 00:12:21,000
What’s the story behind Raptor Mini?
It’s a code name in the bird group. It’s optimized for speed and smaller tasks.
It’s free and great for repetitive scenarios like data analysis.

12
00:12:21,000 --> 00:16:19,000
Developers should pick models based on task complexity.
Mini models are fast and good for clear, repetitive tasks.
Larger models like Sonnet are better for creative or complex workflows.

13
00:16:47,000 --> 00:19:35,000
Evaluations (evals) help us measure model performance.
We run online evals with live data and offline evals with test cases.
Metrics include time to first token and resolution success.

14
00:19:35,000 --> 00:21:15,000
Benchmarks like SWE Bench are useful but language-biased.
That’s why we built VS Code’s own eval suite (VS Bench) to test coding scenarios.

15
00:21:15,000 --> 00:23:34,000
Developers can give feedback via Reddit or thumbs up/down in VS Code.
We track that data to improve models continuously.

16
00:23:34,000 --> 00:24:08,000
Thanks for joining us.
Remember to subscribe on YouTube or your favorite podcast app.
Until next time, happy coding!
