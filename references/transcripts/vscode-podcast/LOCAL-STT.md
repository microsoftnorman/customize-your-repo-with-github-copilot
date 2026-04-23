# Local STT Workflow

This workflow exists for podcast episodes that do not publish an official transcript file on the podcast site.

It keeps local speech-to-text output separate from the official transcript cache:

- Official podcast metadata and first-party transcripts remain in `references/transcripts/vscode-podcast/`
- Machine-generated local transcripts are written to `references/transcripts/vscode-podcast/local-stt/`
- Downloaded MP3 files are written to `references/transcripts/vscode-podcast/audio/`

## Prerequisites

Install a local transcription backend:

```powershell
pip install faster-whisper
```

`ffmpeg` must also be installed and available on `PATH`.

## Usage

Process only episodes without official transcripts:

```powershell
python scripts/transcribe-vscode-podcast-audio.py
```

Process specific episodes:

```powershell
python scripts/transcribe-vscode-podcast-audio.py --episodes 1 2 3
```

Process all episodes, including ones that already publish official transcripts:

```powershell
python scripts/transcribe-vscode-podcast-audio.py --all
```

Use a different local model:

```powershell
python scripts/transcribe-vscode-podcast-audio.py --model medium
```

Normalize the generated local STT output into the same parsed schema used by the
official transcript parser:

```powershell
python scripts/normalize-vscode-podcast-local-stt.py
```

## Output

For each processed episode the script writes:

- `<episode>.json` with metadata and normalized segments
- `<episode>.txt` as a plain text transcript
- `<episode>.segments.json` with timestamped segment records

These local STT outputs are machine-generated and should not be confused with the official `transcript.txt` files published by the podcast host for episodes 13-21.

## Parsed Compatibility

The normalization step writes parsed-compatible JSON files to:

- `references/transcripts/vscode-podcast/local-stt/parsed/`

That output uses the same top-level shape as the files in:

- `references/transcripts/vscode-podcast/parsed/`

This makes it easier to build one local search or indexing flow across official and locally transcribed podcast episodes.