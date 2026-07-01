---
title: "Scaling Teams or Scaling Time? Memory-Enabled Lifelong Learning in LLM Multi-Agent Systems"
type: "paper"
author: "arXiv:2604.03295"
url: "https://arxiv.org/abs/2604.03295"
date_published: "2026-04"
date_added: "2026-07-01"
topic: "memory-systems"
status: "candidate"
---

## Why it's here

Directly addresses the open question in this topic: how does memory architecture change at team scale vs. single-operator? The central finding — that memory quality can compensate for smaller team size — reframes the design tradeoff away from "add more agents" toward "improve memory."

## Key claim or contribution

Non-monotonic scaling: larger multi-agent teams don't reliably outperform smaller ones when the smaller team has better memory. Introduces LLMA-Mem, a lifelong memory framework evaluated empirically on MultiAgentBench across coding, research, and database tasks under different team-size/memory configurations. Tracks both performance and inference cost, making the team-vs-memory substitution curve concrete.

## Who should read/watch this

Engineers making team-size vs. memory-quality tradeoffs in multi-agent production deployments, especially where inference cost is a hard constraint.

## Related entries

- [memory-in-age-of-ai-agents-survey.md](memory-in-age-of-ai-agents-survey.md)
- [hindsight-agent-memory-benchmark.md](hindsight-agent-memory-benchmark.md)
