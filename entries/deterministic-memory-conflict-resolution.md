---
title: "Don't Ask the LLM to Track Freshness: A Deterministic Recipe for Memory Conflict Resolution"
type: "paper"
author: "arXiv:2606.01435"
url: "https://arxiv.org/abs/2606.01435"
date_published: "2026-06"
date_added: "2026-07-01"
topic: "memory-systems"
status: "candidate"
---

## Why it's here

Counter-intuitive engineering result with immediate design implications: replacing LLM-mediated conflict resolution with a deterministic max(serial_number) rule yields 78% accuracy on single-hop tasks vs. 54% for the best prior system. The bottleneck is post-retrieval aggregation, not storage or retrieval — a distinction most memory system designs ignore.

## Key claim or contribution

When two stored facts conflict (e.g., "user lives in Seattle" vs. the newer "user moved to Austin"), don't pass both to the LLM and ask it to decide — apply serial-number comparison deterministically and discard the older fact before context assembly. Extends to multi-hop via per-hop deterministic Self-Ask, reaching 30.2% on multi-hop tasks (+20 points over prior work with identical retrieval and storage components).

## Who should read/watch this

Engineers implementing mutable state in any agent memory system. The fix is a small amount of Python logic and requires no model changes.

## Related entries

- [hindsight-agent-memory-benchmark.md](hindsight-agent-memory-benchmark.md)
- [memora-recall-to-forgetting-benchmark.md](memora-recall-to-forgetting-benchmark.md)
