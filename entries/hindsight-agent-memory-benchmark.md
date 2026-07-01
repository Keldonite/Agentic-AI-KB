---
title: "Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects"
type: "paper"
author: "Latimer, Boschi, Neeser, Bartholomew, Srivastava, Wang, Ramakrishnan"
url: "arXiv:2512.12818"
date_published: "2025-12"
date_added: "2026-07-01"
topic: "memory-systems"
status: "indexed"
---

## Why it's here

The standout entry in this topic — real comparative benchmark data on
memory architectures, not another opinion piece. Directly relevant to
any RAG-vs-structured-memory architecture decision.

## Key claim or contribution

Head-to-head benchmark of memory architectures — MemGPT, Zep, Mem0,
Mem0-Graph, A-Mem, LangMem, Memobase — on the LoCoMo benchmark, with
per-system accuracy numbers rather than qualitative claims. The
authors' own system (Hindsight) makes an explicit architectural choice
most competitors don't: separating tracked facts from opinions/beliefs,
plus temporal reasoning about when something was true vs. when it was
recorded. Reports raising overall accuracy from roughly 76% (a strong
baseline system) to the mid-to-high 80s with their approach, depending
on backbone model size.

## Confidence note

[FRAME]: benchmark numbers for competing systems (e.g. Backboard) are
self-reported by those systems per the paper's own disclosure, not
independently reproduced by these authors — treat cross-system
comparisons as directionally informative, not exact.

## Who should read/watch this

Anyone choosing between RAG, a knowledge graph, or a structured memory
system for an agent that needs to track facts vs. hunches over time —
this is the closest thing in this topic to actual data on that
tradeoff.

## Related entries

- atlan-ai-memory-vs-rag.md
- memory-in-age-of-ai-agents-survey.md
