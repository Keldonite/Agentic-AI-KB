---
title: "MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents"
type: "paper"
author: "arXiv:2601.03236"
url: "https://arxiv.org/abs/2601.03236"
date_published: "2026-01"
date_added: "2026-07-01"
topic: "memory-systems"
status: "candidate"
---

## Why it's here

Fills the gap between "use a vector store" and "use a knowledge graph": MAGMA decouples memory into four orthogonal graphs (semantic, temporal, causal, entity) and formulates retrieval as policy-guided traversal rather than similarity search. ACL 2026 Main with empirical evaluation on LoCoMo and LongMemEval.

## Key claim or contribution

Monolithic vector stores entangle temporal, causal, and entity information — a single similarity score cannot distinguish why something is relevant. The multi-graph decoupling enables structured, interpretable retrieval paths and consistently outperforms state-of-the-art agentic memory systems on long-horizon reasoning benchmarks.

## Who should read/watch this

Engineers hitting the ceiling of vector-similarity retrieval in complex, long-horizon agents, particularly where multi-hop reasoning or causal tracing matters. Also relevant to anyone evaluating graph memory as a concrete alternative to RAG rather than a theoretical one.

## Related entries

- [skyhawkbytecode-rag-architecture-choice.md](skyhawkbytecode-rag-architecture-choice.md)
- [memory-in-age-of-ai-agents-survey.md](memory-in-age-of-ai-agents-survey.md)
- [atlan-ai-memory-vs-rag.md](atlan-ai-memory-vs-rag.md)
