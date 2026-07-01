---
slug: deployment-and-observability
seed_terms:
  - "deploying AI agents production"
  - "agent observability monitoring"
  - "agent failure recovery patterns"
---

# Deployment & observability

Running agents in production: monitoring, logging what actually
matters for debugging non-deterministic failures, and recovery
patterns when an agent goes off-track.

## Seed entries (status: candidate, not yet reviewed)

Pending first ingestion sweep.

## Entries

- [arXiv:2603.01548, "Graph-Based Self-Healing Tool Routing"](../entries/graph-based-self-healing-tool-routing.md) — Recovery Time / Task Integrity / Failure Observability metrics
- [arXiv:2605.06737, "A Self-Healing Framework for Reliable LLM-Based Autonomous Agents"](../entries/self-healing-framework-reliability-arxiv.md) — failure taxonomy + reliability model
- [Coralogix, "Agentic AI Observability: A Practical Guide for 2026"](../entries/coralogix-agentic-observability-guide.md) — practical metric baseline
- [DEV Community, "The Self-Healing Agent Pattern"](../entries/dev-community-self-healing-pattern.md) — practitioner pattern (anecdotal, flagged)
- [arXiv:2604.02334, "Holos" (Section 4.2.2)](../entries/holos-chaos-engineering-resilience-test.md) — chaos-engineering resilience test methodology

## Open questions

- What's actually worth logging for an agent, vs. log noise?
- What does graceful failure/recovery look like for a long-running agent?
