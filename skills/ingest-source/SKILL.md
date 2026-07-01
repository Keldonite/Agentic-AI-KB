---
name: ingest-source
description: >
  Finds and evaluates new sources (papers, blog posts, talks, podcasts,
  repos) for the Agentic AI Engineering KB. Trigger with "ingest sweep",
  "find sources for [topic]", or "update the KB". Always runs live
  searches — never answers from memory. Deduplicates against existing
  /entries before proposing anything new. Scoped strictly to the six
  topics in README.md; anything outside scope gets rejected with a
  one-line reason, not silently dropped.
---

# Ingest Source

## Trigger
- "ingest sweep" — run all six topics
- "find sources for <topic>" — run one topic
- "update the KB" — same as ingest sweep

## Process

1. **Search live.** For the given topic, run 3-5 targeted web searches
   using the topic's seed terms (see topics/*.md frontmatter). Never
   rely on training-data recall for what's new.
2. **Dedupe.** Check candidate URLs/titles against every entry already
   in /entries. Skip exact and near-duplicates (same source, different
   URL/mirror).
3. **Score for scope fit.** Reject anything that isn't specifically
   about agentic engineering practice (see README scope note). A
   general "prompting tips" post is out of scope even if popular.
4. **Draft entries.** For each surviving candidate, fill out
   entries/TEMPLATE.md in your own words — no verbatim excerpts from
   the source, ever. Summaries only.
5. **Digest.** Produce a short digest: N candidates found, M passed
   dedupe, K passed scope, list of drafted entries with one-line
   rationale each. Do not auto-commit — present the digest for human
   review before entries are added to /topics.

## Anti-patterns to avoid
- Do not pad the KB with volume. A sweep that finds nothing worth
  adding should report that honestly, not force in marginal entries.
- Do not quote source text at length. Entries are original summaries.
- Do not re-index something because it's popular; index it because it
  passes the scope test in README.md.
