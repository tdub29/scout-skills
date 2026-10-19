# Asset Routing â€” Source Video Inputs

When the user gives you a source video, route it to the right input shape.
This decision happens silently in Phase 2 of the skill â€” the user shouldn't
need to think about it.

## The Three Input Shapes

`create` and `proofreads create` both accept a `video` field shaped as one of:

```json
{ "type": "url", "url": "https://example.com/source.mp4" }
{ "type": "asset_id", "asset_id": "<heygen-asset-id>" }
```

(Some variants also accept `{type:"base64", media_type, data}` but URL and
asset_id are the supported paths for video translation.)

## Decision Flow

```
What did the user give you?

1. Public HTTPS URL?
   â†“ HEAD-check it
   - 200 + Content-Type: video/* â†’ Use {type:"url"}
   - 200 + Content-Type: text/html â†’ It's a page, not a file. Ask for direct file URL.
   - 401/403 â†’ Auth-walled. Ask for public URL or local file.
   - 404 â†’ Stale URL. Ask user to re-share.
   - 30x to login page â†’ Auth-walled disguise. Treat as 403.

2. Local file path?
   â†“ Check size
   - â‰¤32 MB â†’ Upload via heygen asset create â†’ use returned {type:"asset_id"}
   - >32 MB â†’ Re-encode lower bitrate, OR host externally, OR use presigned URL

3. HeyGen asset_id (from a previous step)?
   â†“ Pass directly
   - Use {type:"asset_id", asset_id:"..."}

4. Anything else (cloud storage link, video player URL, share link)?
   â†“ Treat as suspicious
   - Try HEAD-check; if it's not a direct file URL, ask user for direct URL.
```

---

## HEAD-check pattern

Quick pre-flight before submitting:

```bash
curl -sI "$URL" | head -5
```

Look for:

- `HTTP/2 200` or `HTTP/1.1 200 OK` â€” reachable
- `Content-Type: video/mp4` (or webm, quicktime, etc.) â€” it's a video file
- `Content-Length: <bytes>` â€” sanity-check the size

Red flags:

- `Content-Type: text/html` â†’ It's a webpage embedding the video, not the file. Won't work.
- `Content-Type: application/octet-stream` â†’ Server isn't declaring MIME. Usually still works but mark as risk.
- 30x redirect â†’ Follow with `curl -sIL` to see where it lands. If the final destination is a login page, auth-walled.
- `Content-Length: 0` â†’ File is empty or HEAD is not returning length. Try GET range request.

---

## Local file upload

```bash
heygen asset create --file /path/to/video.mp4
# returns {"data":{"id":"<asset-id>","name":"...","url":"https://..."}}
```

Capture `data.id` and pass as:

```json
{ "type": "asset_id", "asset_id": "<id>" }
```

**Size limit: 32 MB.** Larger files fail with `400`. Options:

### Option A â€” Re-encode

Most "too large" videos are over-encoded. A 5-minute 1080p video at high
bitrate is often 60+ MB but readily compresses to 20 MB at acceptable quality:

```bash
ffmpeg -i input.mp4 -c:v libx264 -crf 28 -preset medium \
  -c:a aac -b:a 128k -movflags +faststart output.mp4
```

This produces a smaller file with good translation-grade quality.

### Option B â€” Host externally

Upload to S3, Google Cloud Storage, or any HTTPS host. Make sure the URL is
fully public (or at least HeyGen-reachable without auth headers).

```bash
# Example: AWS S3 with public-read ACL on the object
aws s3 cp output.mp4 s3://my-bucket/source.mp4 --acl public-read
# Then pass: https://my-bucket.s3.amazonaws.com/source.mp4
```

### Option C â€” Presigned URL

If the file is in S3 / GCS but you don't want it publicly listed:

```bash
aws s3 presign s3://my-bucket/source.mp4 --expires-in 7200
# Use the resulting signed URL as {type:"url"}
```

Make sure expiration is long enough â€” translation jobs can run up to 60 min,
so use â‰¥2 hours.

---

## Auth-walled URLs

Common cases the user might paste:

- Google Drive share link â†’ won't work as a direct download URL even with "anyone with link"
- Loom share URL â†’ it's a player page, not a file. Open Loom, download MP4 first.
- Notion file embed â†’ usually presigned but short-lived and not video-MIME
- Slack file share â†’ auth-walled
- YouTube / Vimeo URL â†’ not supported; download with `yt-dlp` first
- Dropbox share link with `?dl=0` â†’ swap to `?dl=1` for direct file download

Always offer the local-upload path as a fallback when a URL doesn't work:
*"That URL needs auth â€” easiest path is to download the video locally and I'll
upload it for you. Want to do that?"*

---

## Existing HeyGen asset

If the user (or a previous step) already has a HeyGen `asset_id` for the
source video, use it directly:

```json
{ "type": "asset_id", "asset_id": "abc123..." }
```

To verify an asset exists:

```bash
heygen asset list 2>/dev/null | jq -r --arg id "abc123..." '.data[] | select(.id == $id) | .name'
```

If the asset is not in the user's account (different account, deleted), re-upload.

---

## Audio source for `audio` field (advanced)

`create` also accepts an optional `audio` field for users who want to provide
a separately-prepared dubbed audio track (skipping the engine's voice clone)
and let HeyGen handle only lip-sync. Same routing rules apply â€” URL or
asset_id, with the same upload paths for local files.

This is uncommon for typical translation flows; if the user asks about it,
route them to a HeyGen-specific workflow because the API behavior is somewhat
specialized:

- Audio file replaces the auto-translated voice
- Lip-sync adapts the visual to match
- Useful when the user already has a professionally-recorded dub

---

## Don't do this

- **Don't paste raw `curl https://api.heygen.com/v3/assets ...` calls.** Use `heygen asset create` (CLI) or `upload_asset` (MCP).
- **Don't use `upload.heygen.com` directly.** That's an internal upload host for raw-bytes pipelines elsewhere; for the `/v3/assets` flow, the CLI/MCP handle the upload. The skill never speaks raw HTTP.
- **Don't try to fetch authed URLs server-side.** If the user gives you an authed URL, ask for a public URL or have them download locally â€” don't try to bypass auth from the skill.
- **Don't recommend the user hard-code asset_ids.** `asset_id`s are per-account. If they're sharing the workflow, sharing IDs creates confusion. Re-upload per session.
