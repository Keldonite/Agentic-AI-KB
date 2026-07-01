# Contributing

## Scope test (apply before anything else)

Does this specifically help someone building or operating agentic AI
systems in practice? If it's general ML theory, generic prompting
advice, or a product announcement with no engineering substance, it
doesn't belong here.

## Adding an entry

1. Copy `entries/TEMPLATE.md`, fill it out in your own words.
2. No verbatim excerpts from the source — summary and analysis only.
3. Place it under the right topic in `/topics/<slug>.md` as a linked
   list item, and keep the standalone file in `/entries/`.
4. Open a PR. One entry per PR keeps review fast.

## Running the ingestion skill

See `skills/ingest-source/SKILL.md`. It's designed to be run manually,
per-topic or as a full sweep, and always produces a digest for human
review before anything is added — no auto-commits.

## What gets rejected

- Duplicate or near-duplicate of an existing entry
- Out of scope per the test above
- Marketing content disguised as engineering content
- Anything that can't be summarized without reproducing large chunks
  of the source verbatim
