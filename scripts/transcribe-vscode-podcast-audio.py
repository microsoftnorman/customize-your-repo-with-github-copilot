"""Download VS Code podcast audio and transcribe it locally.

This script is intended for episodes that do not publish an official transcript on
the podcast site. It keeps generated transcripts separate from the official
transcript cache.

Prerequisites:
    pip install faster-whisper
    ffmpeg must be installed and available on PATH

Usage:
    python scripts/transcribe-vscode-podcast-audio.py
    python scripts/transcribe-vscode-podcast-audio.py --all
    python scripts/transcribe-vscode-podcast-audio.py --episodes 1 2 3
    python scripts/transcribe-vscode-podcast-audio.py --model small

By default the script:
1. reads references/transcripts/vscode-podcast/*.md
2. selects episodes where transcript_available: false
3. downloads the episode MP3 into references/transcripts/vscode-podcast/audio/
4. writes local STT output into references/transcripts/vscode-podcast/local-stt/

The script writes three files per processed episode:
- <episode>.json        structured metadata + segments
- <episode>.txt         plain text transcript
- <episode>.segments.json   raw segment list with timestamps
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path


PODCAST_DIR = Path("references/transcripts/vscode-podcast")
AUDIO_DIR = PODCAST_DIR / "audio"
OUTPUT_DIR = PODCAST_DIR / "local-stt"
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
EPISODE_FILE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--podcast-dir",
        type=Path,
        default=PODCAST_DIR,
        help="Directory containing the podcast markdown files.",
    )
    parser.add_argument(
        "--audio-dir",
        type=Path,
        default=AUDIO_DIR,
        help="Directory where MP3 files are downloaded.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_DIR,
        help="Directory where local STT output is written.",
    )
    parser.add_argument(
        "--model",
        default="small",
        help="faster-whisper model size to use, for example tiny, base, small, medium, large-v3.",
    )
    parser.add_argument(
        "--language",
        default="en",
        help="Language hint passed to the transcription model.",
    )
    parser.add_argument(
        "--device",
        default="auto",
        help="Transcription device for faster-whisper, for example auto, cpu, cuda.",
    )
    parser.add_argument(
        "--compute-type",
        default="auto",
        help="faster-whisper compute type, for example auto, int8, float16.",
    )
    parser.add_argument(
        "--episodes",
        nargs="*",
        type=int,
        default=[],
        help="Optional episode numbers to process.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Process all episodes with audio URLs, including ones with official transcripts.",
    )
    parser.add_argument(
        "--skip-download",
        action="store_true",
        help="Do not download MP3s again; require local audio files to already exist.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing local STT output files.",
    )
    return parser.parse_args()


def parse_frontmatter(file_path: Path) -> dict[str, object]:
    text = file_path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"Missing frontmatter: {file_path}")

    metadata: dict[str, object] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"')

        if key == "episode":
            metadata[key] = int(value)
        elif value.lower() == "true":
            metadata[key] = True
        elif value.lower() == "false":
            metadata[key] = False
        else:
            metadata[key] = value

    metadata["source_file"] = file_path.name
    metadata["source_path"] = str(file_path)
    return metadata


def load_episodes(podcast_dir: Path) -> list[dict[str, object]]:
    episodes: list[dict[str, object]] = []
    for markdown_file in sorted(
        path for path in podcast_dir.glob("*.md") if EPISODE_FILE_RE.match(path.name)
    ):
        episodes.append(parse_frontmatter(markdown_file))
    return episodes


def filter_episodes(episodes: list[dict[str, object]], args: argparse.Namespace) -> list[dict[str, object]]:
    selected = []
    requested = set(args.episodes)

    for episode in episodes:
        number = int(episode.get("episode", 0))
        if requested and number not in requested:
            continue
        if not args.all and episode.get("transcript_available") is True:
            continue
        if not episode.get("audio_url"):
            continue
        selected.append(episode)

    return selected


def download_audio(audio_url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(audio_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request) as response:
        destination.write_bytes(response.read())


def format_seconds(seconds: float) -> str:
    total_ms = int(round(seconds * 1000))
    hours, rem = divmod(total_ms, 3_600_000)
    minutes, rem = divmod(rem, 60_000)
    secs, ms = divmod(rem, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{ms:03d}"


def collect_segments(model: object, audio_path: Path, language: str) -> tuple[list[dict[str, object]], object]:
    segments, info = model.transcribe(
        str(audio_path),
        language=language,
        vad_filter=True,
        beam_size=1,
        best_of=1,
        temperature=0,
    )

    normalized_segments: list[dict[str, object]] = []
    for segment in segments:
        normalized_segments.append(
            {
                "id": segment.id,
                "start": format_seconds(segment.start),
                "end": format_seconds(segment.end),
                "text": segment.text.strip(),
            }
        )

    return normalized_segments, info


def get_output_paths(output_dir: Path, episode: dict[str, object]) -> tuple[Path, Path, Path]:
    stem = Path(str(episode["source_file"])).stem
    json_path = output_dir / f"{stem}.json"
    txt_path = output_dir / f"{stem}.txt"
    segments_path = output_dir / f"{stem}.segments.json"
    return json_path, txt_path, segments_path


def transcribe_audio(audio_path: Path, model_name: str, language: str, device: str, compute_type: str) -> tuple[list[dict[str, object]], dict[str, object]]:
    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:
        raise RuntimeError(
            "faster-whisper is not installed. Run `pip install faster-whisper` first."
        ) from exc

    resolved_device = device
    resolved_compute_type = compute_type
    if resolved_device == "cpu" and resolved_compute_type == "auto":
        resolved_compute_type = "int8"

    try:
        model = WhisperModel(model_name, device=resolved_device, compute_type=resolved_compute_type)
        normalized_segments, info = collect_segments(model, audio_path, language)
    except RuntimeError as exc:
        if device != "auto" or "cublas" not in str(exc).lower():
            raise
        print("CUDA runtime not available; retrying transcription on CPU.")
        resolved_device = "cpu"
        if resolved_compute_type == "auto":
            resolved_compute_type = "int8"
        model = WhisperModel(model_name, device=resolved_device, compute_type=resolved_compute_type)
        normalized_segments, info = collect_segments(model, audio_path, language)

    transcription_info = {
        "language": getattr(info, "language", language),
        "language_probability": getattr(info, "language_probability", None),
        "duration": getattr(info, "duration", None),
        "duration_after_vad": getattr(info, "duration_after_vad", None),
        "model": model_name,
        "device": resolved_device,
        "compute_type": resolved_compute_type,
    }
    return normalized_segments, transcription_info


def write_outputs(output_dir: Path, episode: dict[str, object], segments: list[dict[str, object]], transcription_info: dict[str, object], overwrite: bool) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path, txt_path, segments_path = get_output_paths(output_dir, episode)

    if not overwrite and json_path.exists() and txt_path.exists() and segments_path.exists():
        return

    payload = {
        "episode": episode,
        "transcription": transcription_info,
        "segment_count": len(segments),
        "segments": segments,
    }
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    segments_path.write_text(json.dumps(segments, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    transcript_text = "\n\n".join(f"[{segment['start']}] {segment['text']}" for segment in segments)
    txt_path.write_text(transcript_text + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    episodes = load_episodes(args.podcast_dir)
    selected = filter_episodes(episodes, args)

    if not selected:
        print("No episodes matched the requested filter.")
        return 0

    print(f"Selected {len(selected)} episode(s) for local STT processing.")

    for episode in selected:
        number = int(episode["episode"])
        title = str(episode.get("title", f"Episode {number}"))
        stem = Path(str(episode["source_file"])).stem
        audio_path = args.audio_dir / f"{stem}.mp3"
        json_path, txt_path, segments_path = get_output_paths(args.output_dir, episode)

        if not args.overwrite and json_path.exists() and txt_path.exists() and segments_path.exists():
            print(f"Skipping episode {number}: local STT outputs already exist")
            continue

        if not audio_path.exists():
            if args.skip_download:
                print(f"Skipping episode {number}: audio file missing at {audio_path}")
                continue
            print(f"Downloading episode {number}: {title}")
            download_audio(str(episode["audio_url"]), audio_path)

        print(f"Transcribing episode {number}: {title}")
        segments, transcription_info = transcribe_audio(
            audio_path=audio_path,
            model_name=args.model,
            language=args.language,
            device=args.device,
            compute_type=args.compute_type,
        )
        write_outputs(args.output_dir, episode, segments, transcription_info, args.overwrite)
        print(f"Wrote local STT output for episode {number} with {len(segments)} segment(s)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())