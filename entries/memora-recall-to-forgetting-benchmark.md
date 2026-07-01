---
title: "From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents"
type: "paper"
author: "arXiv:2604.20006"
url: "https://arxiv.org/abs/2604.20006"
date_published: "2026-04"
date_added: "2026-07-01"
topic: "memory-systems"
status: "candidate"
---

## Why it's here

The Hindsight paper benchmarks retrieval accuracy; this one adds the orthogonal dimension — does the agent correctly stop using facts that have become invalid? Introduces Memora (weeks-to-months conversation benchmark) and FAMA (Forgetting-Aware Memory Accuracy), a metric that penalizes recall of obsolete information.

## Key claim or contribution

Most memory agents fail the forgetting dimension, not just recall: systems frequently surface invalidated memories even when newer facts contradict them, and even purpose-built memory agents show only marginal gains over base LLMs on this axis. Evaluated across four LLMs and six memory agents with human evaluation and automated checks.

## Who should read/watch this

Anyone building personalized or long-running agents where user context evolves over time — subscription changes, location moves, preference shifts — rather than accumulates monotonically.

## Related entries

- [hindsight-agent-memory-benchmark.md](hindsight-agent-memory-benchmark.md)
