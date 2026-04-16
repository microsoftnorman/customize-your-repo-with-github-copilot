"""Fetch a YouTube transcript and append it to an existing stub file.

Usage:
    python scripts/fetch-transcript.py <video_id> <path_to_stub_file>

The stub file must contain the marker:
    <!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->

Everything after that marker is replaced with a fresh timestamped transcript.
Each line is formatted as `[H:MM:SS] text` where the timestamp is the start of the snippet.
"""
from __future__ import annotations

import sys
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi


def fmt_ts(seconds: float) -> str:
    total = int(seconds)
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}"


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 1

    video_id, stub_path = sys.argv[1], Path(sys.argv[2])
    if not stub_path.exists():
        print(f"Stub file not found: {stub_path}")
        return 1

    transcript = YouTubeTranscriptApi().fetch(video_id, languages=["en"])
    lines = [
        f"[{fmt_ts(snip.start)}] {snip.text.replace(chr(10), ' ').strip()}"
        for snip in transcript.snippets
    ]

    text = stub_path.read_text(encoding="utf-8")
    marker = "<!-- PASTE FULL TRANSCRIPT BELOW THIS LINE -->"
    idx = text.find(marker)
    if idx == -1:
        print(f"Marker not found in {stub_path}")
        return 1

    header = text[: idx + len(marker)]
    body = "\n\n" + "\n".join(lines) + "\n"
    stub_path.write_text(header + body, encoding="utf-8")
    print(f"Wrote {len(lines)} snippets to {stub_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
