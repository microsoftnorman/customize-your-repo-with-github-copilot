"""Normalize local STT podcast output into the parsed transcript schema.

Usage:
    python scripts/normalize-vscode-podcast-local-stt.py
    python scripts/normalize-vscode-podcast-local-stt.py <local_stt_dir> <output_dir>

This script reads JSON files produced by scripts/transcribe-vscode-podcast-audio.py
and writes one normalized JSON file per episode plus an index.json file.

The output schema matches the shape used by scripts/parse-vscode-podcast-transcripts.py:
    {
      "source_file": "...",
      "transcript_format": "local_stt_segments",
      "segment_count": 123,
      "metadata": {...},
      "segments": [...]
    }
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


DEFAULT_LOCAL_STT_DIR = Path("references/transcripts/vscode-podcast/local-stt")
DEFAULT_OUTPUT_DIR = DEFAULT_LOCAL_STT_DIR / "parsed"


def normalize_segment(segment: dict[str, object]) -> dict[str, object]:
    normalized: dict[str, object] = {
        "speaker": None,
        "text": str(segment.get("text", "")).strip(),
    }

    start = segment.get("start")
    end = segment.get("end")
    if start is not None:
        normalized["start"] = str(start)
    if end is not None:
        normalized["end"] = str(end)

    segment_id = segment.get("id")
    if segment_id is not None:
        normalized["id"] = segment_id

    return normalized


def normalize_episode_payload(file_path: Path) -> dict[str, object]:
    payload = json.loads(file_path.read_text(encoding="utf-8"))
    episode = dict(payload.get("episode", {}))
    transcription = dict(payload.get("transcription", {}))
    raw_segments = payload.get("segments", [])

    normalized_segments = [normalize_segment(segment) for segment in raw_segments]
    metadata = {
        **episode,
        "local_stt": True,
        "local_stt_model": transcription.get("model"),
        "local_stt_language": transcription.get("language"),
        "local_stt_device": transcription.get("device"),
        "local_stt_compute_type": transcription.get("compute_type"),
    }

    return {
        "source_file": str(episode.get("source_file", file_path.name)),
        "transcript_format": "local_stt_segments",
        "segment_count": len(normalized_segments),
        "metadata": metadata,
        "segments": normalized_segments,
    }


def main() -> int:
    local_stt_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_LOCAL_STT_DIR
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUTPUT_DIR

    if not local_stt_dir.exists():
        print(f"Local STT directory not found yet: {local_stt_dir}")
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)

    json_files = sorted(
        path
        for path in local_stt_dir.glob("*.json")
        if not path.name.endswith(".segments.json")
    )

    if not json_files:
        print(f"No local STT JSON files found in {local_stt_dir}")
        return 0

    index_entries: list[dict[str, object]] = []
    for json_file in json_files:
        normalized = normalize_episode_payload(json_file)
        output_file = output_dir / json_file.name
        output_file.write_text(json.dumps(normalized, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        metadata = normalized["metadata"]
        index_entries.append(
            {
                "episode": metadata.get("episode"),
                "title": metadata.get("title"),
                "published": metadata.get("published"),
                "transcript_available": metadata.get("transcript_available"),
                "transcript_format": normalized["transcript_format"],
                "segment_count": normalized["segment_count"],
                "source_file": normalized["source_file"],
                "parsed_file": output_file.name,
            }
        )

    index_file = output_dir / "index.json"
    index_file.write_text(json.dumps(index_entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Normalized {len(json_files)} local STT file(s) into {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())