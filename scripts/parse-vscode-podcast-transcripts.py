"""Parse local VS Code Insiders Podcast transcript markdown files into JSON.

Usage:
    python scripts/parse-vscode-podcast-transcripts.py
    python scripts/parse-vscode-podcast-transcripts.py <podcast_dir> <output_dir>

The script reads markdown files in references/transcripts/vscode-podcast/, extracts
frontmatter and the ## Full Transcript section, detects the transcript format, and
writes one JSON file per episode plus an index.json file.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


DEFAULT_PODCAST_DIR = Path("references/transcripts/vscode-podcast")
DEFAULT_OUTPUT_DIR = DEFAULT_PODCAST_DIR / "parsed"

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
FULL_TRANSCRIPT_RE = re.compile(r"\n## Full Transcript\r?\n(.*)\Z", re.DOTALL)
SPEAKER_TIME_RE = re.compile(r"^\d{2}:\d{2}\.\d{2}$")
SRT_INDEX_RE = re.compile(r"^\d+$")
SRT_TIME_RE = re.compile(
    r"^(?P<start>\d{2}:\d{2}:\d{2},\d{3})\s+-->\s+(?P<end>\d{2}:\d{2}:\d{2},\d{3})$"
)


def parse_frontmatter(text: str) -> dict[str, object]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("Missing frontmatter")

    metadata: dict[str, object] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"')

        if value.lower() == "true":
            metadata[key] = True
        elif value.lower() == "false":
            metadata[key] = False
        elif key == "episode":
            metadata[key] = int(value)
        else:
            metadata[key] = value

    return metadata


def extract_full_transcript(text: str) -> str:
    match = FULL_TRANSCRIPT_RE.search(text)
    if not match:
        raise ValueError("Missing ## Full Transcript section")
    return match.group(1).strip()


def normalize_whitespace(value: str) -> str:
    value = value.replace("\ufeff", "")
    value = value.replace("\r", "")
    return value.strip()


def parse_speaker_turns(lines: list[str]) -> list[dict[str, object]]:
    segments: list[dict[str, object]] = []
    index = 0

    while index < len(lines):
        if not SPEAKER_TIME_RE.match(lines[index].strip()):
            index += 1
            continue

        start = lines[index].strip()
        speaker = lines[index + 1].strip() if index + 1 < len(lines) else ""
        index += 2

        text_lines: list[str] = []
        while index < len(lines) and not SPEAKER_TIME_RE.match(lines[index].strip()):
            current = lines[index].strip()
            if current:
                text_lines.append(current)
            index += 1

        text = " ".join(text_lines).strip()
        if text:
            segments.append(
                {
                    "start": start,
                    "speaker": speaker or None,
                    "text": text,
                }
            )

    return segments


def parse_srt_blocks(text: str) -> list[dict[str, object]]:
    lines = [line.strip() for line in normalize_whitespace(text).splitlines()]
    segments: list[dict[str, object]] = []
    index = 0

    while index < len(lines):
        current = lines[index]
        if not current:
            index += 1
            continue

        if SRT_INDEX_RE.match(current):
            index += 1
            while index < len(lines) and not lines[index]:
                index += 1
            if index >= len(lines):
                break
            current = lines[index]

        time_match = SRT_TIME_RE.match(current)
        if not time_match:
            index += 1
            continue

        index += 1
        text_lines: list[str] = []
        while index < len(lines):
            candidate = lines[index]
            if SRT_INDEX_RE.match(candidate):
                lookahead = index + 1
                while lookahead < len(lines) and not lines[lookahead]:
                    lookahead += 1
                if lookahead < len(lines) and SRT_TIME_RE.match(lines[lookahead]):
                    break
            if SRT_TIME_RE.match(candidate):
                break
            if candidate:
                text_lines.append(candidate)
            index += 1

        text_value = " ".join(text_lines).strip()
        if text_value:
            segments.append(
                {
                    "start": time_match.group("start"),
                    "end": time_match.group("end"),
                    "speaker": None,
                    "text": text_value,
                }
            )

    return segments


def parse_paragraph_fallback(text: str) -> list[dict[str, object]]:
    cleaned = normalize_whitespace(text)
    if not cleaned:
        return []
    return [{"speaker": None, "text": re.sub(r"\s+", " ", cleaned)}]


def detect_and_parse_transcript(text: str) -> tuple[str, list[dict[str, object]]]:
    cleaned = normalize_whitespace(text)
    if not cleaned or cleaned.startswith("No official transcript was published"):
        return "unavailable", []

    lines = [normalize_whitespace(line) for line in cleaned.splitlines()]

    if any(SPEAKER_TIME_RE.match(line) for line in lines):
        segments = parse_speaker_turns(lines)
        if segments:
            return "speaker_turns", segments

    if any(SRT_TIME_RE.match(line) for line in lines):
        segments = parse_srt_blocks(cleaned)
        if segments:
            return "srt_blocks", segments

    return "paragraph_fallback", parse_paragraph_fallback(cleaned)


def parse_episode_file(file_path: Path) -> dict[str, object]:
    source_text = file_path.read_text(encoding="utf-8")
    metadata = parse_frontmatter(source_text)
    full_transcript = extract_full_transcript(source_text)
    transcript_format, segments = detect_and_parse_transcript(full_transcript)

    return {
        "source_file": file_path.name,
        "transcript_format": transcript_format,
        "segment_count": len(segments),
        "metadata": metadata,
        "segments": segments,
    }


def main() -> int:
    podcast_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PODCAST_DIR
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUTPUT_DIR

    if not podcast_dir.exists():
        print(f"Podcast directory not found: {podcast_dir}")
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)

    parsed_index: list[dict[str, object]] = []
    markdown_files = sorted(path for path in podcast_dir.glob("*.md") if path.name != "README.md")

    for markdown_file in markdown_files:
        parsed = parse_episode_file(markdown_file)
        output_file = output_dir / f"{markdown_file.stem}.json"
        output_file.write_text(json.dumps(parsed, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        metadata = parsed["metadata"]
        parsed_index.append(
            {
                "episode": metadata.get("episode"),
                "title": metadata.get("title"),
                "published": metadata.get("published"),
                "transcript_available": metadata.get("transcript_available"),
                "transcript_format": parsed["transcript_format"],
                "segment_count": parsed["segment_count"],
                "source_file": markdown_file.name,
                "parsed_file": output_file.name,
            }
        )

    index_file = output_dir / "index.json"
    index_file.write_text(json.dumps(parsed_index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Parsed {len(markdown_files)} episode files into {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())