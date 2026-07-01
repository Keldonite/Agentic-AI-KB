#!/usr/bin/env python3
"""
Fetch a YouTube video's transcript via its caption track (not the video
audio itself). Requires captions to exist on the video — auto-generated
or manual. Does not work if captions are disabled.

Usage:
    python fetch_transcript.py <video_id_or_url> [--lang en] [--out transcript.txt]

Install:
    pip install youtube-transcript-api --break-system-packages
"""
import argparse
import re
import sys

try:
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import (
        TranscriptsDisabled,
        NoTranscriptFound,
        VideoUnavailable,
    )
except ImportError:
    sys.exit(
        "Missing dependency. Install with:\n"
        "  pip install youtube-transcript-api --break-system-packages\n"
        "  (or without --break-system-packages if not on Debian/Ubuntu system Python)"
    )

# youtube-transcript-api v1.0+ replaced the old classmethod API
# (YouTubeTranscriptApi.get_transcript(...)) with an instance-based one
# (YouTubeTranscriptApi().fetch(...)). This script targets v1.x.


def extract_video_id(value: str) -> str:
    """Accept a raw video ID or a full YouTube URL and return the ID."""
    patterns = [
        r"(?:v=|/)([0-9A-Za-z_-]{11})(?:[?&]|$)",
        r"youtu\.be/([0-9A-Za-z_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, value)
        if match:
            return match.group(1)
    if re.fullmatch(r"[0-9A-Za-z_-]{11}", value):
        return value
    raise ValueError(f"Could not extract a video ID from: {value}")


def fetch_transcript(video_id: str, lang: str = "en"):
    api = YouTubeTranscriptApi()
    try:
        fetched = api.fetch(video_id, languages=[lang, "en"])
    except TranscriptsDisabled:
        sys.exit(f"Captions are disabled for video {video_id}. No transcript available.")
    except NoTranscriptFound:
        sys.exit(f"No transcript found for video {video_id} in language '{lang}'.")
    except VideoUnavailable:
        sys.exit(f"Video {video_id} is unavailable (private, deleted, or region-locked).")
    # FetchedTranscript is iterable; each item is a FetchedTranscriptSnippet
    # with .text, .start, .duration attributes (not dict keys, in v1.x).
    return list(fetched)


def format_transcript(segments, with_timestamps: bool = True) -> str:
    lines = []
    for seg in segments:
        text = seg.text.replace("\n", " ")
        if with_timestamps:
            minutes, seconds = divmod(int(seg.start), 60)
            lines.append(f"[{minutes:02d}:{seconds:02d}] {text}")
        else:
            lines.append(text)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", help="YouTube video ID or full URL")
    parser.add_argument("--lang", default="en", help="Preferred caption language (default: en)")
    parser.add_argument("--out", default=None, help="Output file (default: print to stdout)")
    parser.add_argument(
        "--no-timestamps", action="store_true", help="Omit timestamps, plain text only"
    )
    args = parser.parse_args()

    video_id = extract_video_id(args.video)
    segments = fetch_transcript(video_id, lang=args.lang)
    output = format_transcript(segments, with_timestamps=not args.no_timestamps)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Wrote {len(segments)} caption segments to {args.out}")
    else:
        print(output)


if __name__ == "__main__":
    main()
