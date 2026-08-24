# Media Ingestion Tooling

Status: Candidate  
Owner: Unparalleled Source  
Validated: 2026-08-24

## Decision

Use **yt-dlp** as the preferred current media-ingestion CLI. Keep **youtube-dl** as a reference/compatibility fallback only. Do not select youtube-dl for new workflows unless a specific compatibility requirement justifies it.

## Freshness evidence

- `yt-dlp/yt-dlp` showed active commits through 2026-08-20 during the audit.
- `ytdl-org/youtube-dl` remained available, but the newest commits returned during the audit were from 2025-11-26.
- yt-dlp is a feature-rich downloader in the youtube-dl lineage with support for many sites.

## Current state

- `yt-dlp`: **CANDIDATE / preferred**
- `youtube-dl`: **REFERENCE / compatibility only**

## Allowed uses

- metadata acquisition for public/authorized media;
- captions/subtitle retrieval where available and permitted;
- audio/video acquisition when the user has rights or permission;
- source preparation for transcription, summarization, NotebookLM ingestion, cinematography analysis, or archival workflows;
- extracting metadata before deciding whether the full file is required.

## Efficiency rule

Prefer the lightest acquisition that satisfies the task:

1. metadata only;
2. subtitles/transcript only;
3. selected audio stream;
4. selected video format;
5. full media only when needed.

Do not download large media when metadata, subtitles, thumbnails, or a source URL are sufficient.

## Promotion smoke test

Run in a network-enabled harness against a public test asset the user is authorized to access:

```bash
yt-dlp --version
yt-dlp --simulate --dump-json '<test-url>' > metadata.json
yt-dlp --write-subs --write-auto-subs --sub-langs 'en.*' --skip-download '<test-url>'
yt-dlp -f 'bestaudio/best' --max-filesize 25M '<test-url>'
```

Pass criteria include valid metadata JSON, clean subtitle absence handling, bounded media acquisition, sanitized/routed filenames, no credential persistence, and actionable diagnostics.

## Security / governance

Do not use media tooling to bypass DRM, paywalls, private-account access, authentication controls, or site restrictions. Treat cookies, auth tokens, browser profiles, and downloaded media as sensitive. Respect copyright, platform terms, and user authorization.

## BRAIN routing

For media tasks: native transcript/metadata source → yt-dlp metadata/subtitles → selected media acquisition → heavier browser/scraping workflow only when necessary.
