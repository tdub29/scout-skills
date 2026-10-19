# Video Caption Generator

Automatically transcribe short-form videos from Google Drive, deduplicate by content, and generate social media captions + YouTube/Facebook titles using AI.

## What It Does

1. **Scans** a Google Drive folder for new video files (MP4, MOV, etc.)
2. **Transcribes** each video locally using OpenAI Whisper
3. **Deduplicates** â€” detects A/B variants (same audio, different on-screen titles) and processes them all with proper tagging
4. **Generates** a social media caption and a YouTube/Facebook title for each clip using Claude API
5. **Tracks** processed video IDs so re-runs skip already-seen files

## Example Output

```
*my-video-clip.mp4*
ðŸ“ Transcript: The biggest mistake people make with paid ads is not testing creative fast enough...
ðŸŽ¬ Caption: Most people blow their ad budget because they test one creative at a time. Run 5-10 variants in the first week â€” kill losers fast, scale winners hard. Speed beats perfection every time.
ðŸ“º YT/FB Title: Why 90% of Ad Budgets Get Wasted
```

For A/B variants (same transcript, different filename):

```
*my-clip(1).mp4* (A/B variant of my-clip.mp4)
ðŸ“ Transcript: The biggest mistake people make with paid ads...
ðŸŽ¬ Caption: ...
ðŸ“º YT/FB Title: The Ad Mistake That Burns Your Budget
```

## Prerequisites

- **Python 3.10+**
- **OpenAI Whisper** installed locally (`pip install openai-whisper` or via Homebrew)
- **Google Drive API access** via a CLI tool that can list and download files (the script uses `gws-gateway.sh` by default â€” adapt the `gws()` function to your Drive CLI or SDK)
- **Anthropic API key** for caption/title generation

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Install Whisper (if not already):

```bash
pip install openai-whisper
# or on macOS:
brew install whisper
```

3. Set your Anthropic API key:

```bash
export ANTHROPIC_API_KEY="your-key-here"
```

4. Configure your Google Drive CLI path in `scripts/process_videos.py` (see the `GWS_GATEWAY` variable).

## Usage

```bash
python3 scripts/process_videos.py --folder-id YOUR_FOLDER_ID
```

### Options

| Flag | Default | Description |
|------|---------|-------------|
| `--folder-id` | *(required)* | Google Drive folder ID to scan for videos |
| `--processed-log` | `processed_ids.json` | Path to JSON file tracking already-processed video IDs |

### Multiple Folders

Run against different folders â€” they share the same `processed_ids.json` since Drive file IDs are globally unique:

```bash
python3 scripts/process_videos.py --folder-id YOUR_MAIN_FOLDER_ID
python3 scripts/process_videos.py --folder-id YOUR_AB_FOLDER_ID
```

## Caption & Title Style Guide

- **Caption:** First person, conversational, no hashtags, 2-4 sentences. Hook first, insight second.
- **Title:** Curiosity-driven, under 60 chars, no clickbait. Lead with tension or a number.

## Customization

- Edit the prompt in `generate_caption_and_title()` to match your brand voice
- Swap `claude-sonnet-4-6` for another model in the API call
- Replace the `gws()` function with your own Google Drive SDK integration
- Add a `log_to_sheet()` implementation to track results in a Google Sheet

## How It Works

```
Google Drive Folder
        â”‚
        â–¼
  List new videos (skip already-processed IDs)
        â”‚
        â–¼
  Download each â†’ temp directory
        â”‚
        â–¼
  Whisper transcription (local, model: turbo)
        â”‚
        â–¼
  Content hash for dedup (detect A/B variants)
        â”‚
        â–¼
  Claude API â†’ caption + title per clip
        â”‚
        â–¼
  Output formatted results + save processed IDs
```

## License

MIT


---

<div align="center">

**ðŸ§  [Want these built and managed for you? â†’](https://singlebrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills)**

*This is how we build agents at [Single Brain](https://singlebrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills) for our clients.*

[Single Grain](https://www.singlegrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills) Â· our marketing agency

ðŸ“¬ **[Level up your marketing with 14,000+ marketers and founders â†’](https://levelingup.beehiiv.com/subscribe)** *(free)*

</div>
