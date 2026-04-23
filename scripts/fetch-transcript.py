"""Fetch a YouTube transcript and append it to an existing stub file.

Usage:
    python scripts/fetch-transcript.py <video_id> <path_to_stub_file>

The stub file must contain the marker:
    <!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

Everything after that marker is replaced with a fresh timestamped transcript.
Each line is formatted as `[H:MM:SS] text` where the timestamp is the start of the snippet.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import YouTubeTranscriptApiException


def fmt_ts(seconds: float) -> str:
    total = int(seconds)
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}"


def fetch_youtube_captions(video_id: str) -> list[str]:
    transcript = YouTubeTranscriptApi().fetch(video_id, languages=["en"])
    return [
        f"[{fmt_ts(snip.start)}] {snip.text.replace(chr(10), ' ').strip()}"
        for snip in transcript.snippets
    ]


def transcribe_audio_locally(video_id: str) -> list[str]:
    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:
        raise RuntimeError(
            "faster-whisper is not installed. Run `pip install faster-whisper` first."
        ) from exc

    if shutil.which("yt-dlp") is None:
        raise RuntimeError("yt-dlp is not installed or not on PATH.")
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("ffmpeg is not installed or not on PATH.")

    with tempfile.TemporaryDirectory(prefix="yt-local-stt-") as tmp_dir:
        temp_path = Path(tmp_dir)
        audio_template = temp_path / "audio.%(ext)s"
        command = [
            "yt-dlp",
            "-x",
            "--audio-format",
            "mp3",
            "-o",
            str(audio_template),
            f"https://www.youtube.com/watch?v={video_id}",
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            raise RuntimeError(
                "yt-dlp audio download failed: "
                + (result.stderr.strip() or result.stdout.strip() or f"exit code {result.returncode}")
            )

        audio_files = sorted(temp_path.glob("audio.*"))
        if not audio_files:
            raise RuntimeError("yt-dlp did not produce an audio file for local STT.")

        model = WhisperModel("tiny.en", device="cpu", compute_type="int8")
        segments, _info = model.transcribe(
            str(audio_files[0]),
            language="en",
            vad_filter=True,
            beam_size=1,
            best_of=1,
            temperature=0,
        )

        lines: list[str] = []
        for segment in segments:
            text = segment.text.replace("\n", " ").strip()
            if not text:
                continue
            lines.append(f"[{fmt_ts(segment.start)}] {text}")

        if not lines:
            raise RuntimeError("Local STT completed but produced no transcript lines.")

        return lines


def write_stub_transcript(stub_path: Path, lines: list[str]) -> None:
    text = stub_path.read_text(encoding="utf-8")
    marker = "<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->"
    idx = text.find(marker)
    if idx == -1:
        raise RuntimeError(f"Marker not found in {stub_path}")

    header = text[: idx + len(marker)]
    body = "\n\n" + "\n".join(lines) + "\n"
    stub_path.write_text(header + body, encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 1

    video_id, stub_path = sys.argv[1], Path(sys.argv[2])
    if not stub_path.exists():
        print(f"Stub file not found: {stub_path}")
        return 1

    try:
        lines = fetch_youtube_captions(video_id)
        source = "captions"
    except YouTubeTranscriptApiException as exc:
        print(f"YouTube captions unavailable for {video_id}: {exc.__class__.__name__}. Falling back to local STT.")
        lines = transcribe_audio_locally(video_id)
        source = "local STT"

    try:
        write_stub_transcript(stub_path, lines)
    except RuntimeError as exc:
        print(str(exc))
        return 1

    print(f"Wrote {len(lines)} snippets to {stub_path}")
    print(f"Transcript source: {source}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
