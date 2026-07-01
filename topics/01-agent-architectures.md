---
slug: agent-architectures
seed_terms:
  - "multi-agent orchestration architecture"
  - "planner executor agent pattern"
  - "agent system design production"
---

# Agent architectures

Orchestration patterns for agentic systems: single-agent vs. multi-agent,
planner/executor splits, sub-agent delegation, and the tradeoffs each
introduces (latency, cost, failure surface).

## Entries

- [Beam.ai, "6 Multi-Agent Orchestration Patterns for Production (2026)"](../entries/beam-ai-orchestration-patterns.md) — Princeton NLP counter-finding + pattern-selection heuristics
- [Microsoft ISE, "Orchestration Patterns for Multi-Agent Systems"](../entries/microsoft-ise-orchestration-tradeoffs.md) — real production case study, retail chatbot
- [Forage V2 (arXiv:2604.19837), citing Phillips et al. 2026](../entries/forage-v2-coordination-patterns.md) — five-pattern taxonomy, complexity-escalation warning
- [Kore.ai, "Choosing the Right Orchestration Pattern"](../entries/kore-ai-orchestration-pattern-choice.md) — simplified framing for non-technical stakeholders

## Open questions

- When does multi-agent orchestration earn its complexity vs. a single
  well-scoped agent with good tools?
- How do teams debug failures that span multiple agents?
