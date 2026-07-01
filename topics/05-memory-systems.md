---
slug: memory-systems
seed_terms:
  - "agent memory system architecture"
  - "knowledge graph vs RAG agent"
  - "personal knowledge base AI second brain"
---

# Memory systems

Persistent memory architectures for agents: knowledge graphs vs. RAG,
markdown-as-source-of-truth systems, and second-brain designs for
individual operators.

## Seed entries (status: candidate, not yet reviewed)

Pending first ingestion sweep. Note: this topic overlaps with
VitaOrigin's own RAG vs. LLM Wiki architecture review — treat that as
prior internal context, not a citable public source.

## Entries

- [Latimer et al., "Hindsight is 20/20" (arXiv:2512.12818)](../entries/hindsight-agent-memory-benchmark.md) — head-to-head benchmark of memory architectures
- [Atlan, "AI Memory System vs RAG"](../entries/atlan-ai-memory-vs-rag.md) — decision framework + cited third-party benchmark
- [Skyhawkbytecode, "Choosing the Right RAG Architecture in 2026"](../entries/skyhawkbytecode-rag-architecture-choice.md) — diagnosing RAG failure modes
- ["Memory in the Age of AI Agents" (arXiv:2512.13564)](../entries/memory-in-age-of-ai-agents-survey.md) — broader graph-memory literature survey
- [MAGMA (arXiv:2601.03236)](../entries/magma-multi-graph-agent-memory.md) — four-graph decoupled memory architecture; outperforms vector RAG on long-horizon reasoning (ACL 2026)
- ["Scaling Teams or Scaling Time?" (arXiv:2604.03295)](../entries/llma-mem-team-scale-lifelong-memory.md) — empirical: better memory can substitute for larger team size in multi-agent systems
- ["From Recall to Forgetting" (arXiv:2604.20006)](../entries/memora-recall-to-forgetting-benchmark.md) — Memora benchmark + FAMA metric for evaluating memory invalidation, not just retrieval
- ["Don't Ask the LLM to Track Freshness" (arXiv:2606.01435)](../entries/deterministic-memory-conflict-resolution.md) — deterministic serial-number rule beats LLM conflict resolution by 24 points
- ["Multi-Agent Memory from a Computer Architecture Perspective" (arXiv:2603.10062)](../entries/multi-agent-memory-computer-architecture-lens.md) — maps multi-agent memory consistency onto cache coherence; vocabulary + framing for team-scale design

## Open questions

- RAG vs. knowledge graph vs. hybrid — what's the actual decision
  criterion, not just the marketing framing?
- How does memory architecture change between single-operator and
  team-scale use?
