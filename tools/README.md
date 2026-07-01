# Tools

Utility scripts that support maintaining this KB — not curated reference
content, and not subject to the topic scope test in CONTRIBUTING.md.
These exist because building and maintaining an agentic-engineering
knowledge base is itself an exercise in the practice this repo covers.

## fetch_transcript.py

Fetches a YouTube video's transcript via its caption track, using the
`youtube-transcript-api` package. Written to pull primary-source
material (talks, lectures) for entries in `/topics/`, rather than
relying only on secondary blog coverage of a talk.

Usage:
```
pip install youtube-transcript-api
python3 fetch_transcript.py "https://youtu.be/VIDEO_ID" --out transcript.txt
```

Requires captions to exist on the target video (auto-generated or
manual). Targets `youtube-transcript-api` v1.x's instance-based API
(`YouTubeTranscriptApi().fetch(...)`) — if a future major version
changes the interface again, this will need a corresponding update.

Only fetches the caption track. Does not download video/audio, and
does not work around videos with captions disabled.
