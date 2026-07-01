---
title: "Graph-Based Self-Healing Tool Routing for Cost-Efficient LLM Agents"
type: "paper"
author: "arXiv:2603.01548"
url: "https://arxiv.org/pdf/2603.01548"
date_published: "2026"
date_added: "2026-07-01"
topic: "deployment-and-observability"
status: "indexed"
---

## Why it's here

Proposes named, measurable production-readiness metrics for agent
recovery — a rare concrete alternative to vague "make it more robust"
guidance.

## Key claim or contribution

Argues agent architectures are typically evaluated only on correctness
and cost, while production deployments actually depend on three
additional properties most frameworks ignore: Recovery Time (explicitly
modeled on Recovery Time Objective from infrastructure engineering —
the elapsed time between a tool failure and the agent resuming correct
execution), Task Integrity (how much already-completed work survives
the recovery process rather than being discarded), and Failure
Observability (whether the system can actually detect that it has
failed, as opposed to continuing silently in a degraded state).
Benchmarks different agent architectures (including ReAct-style agents)
and finds fundamentally different recovery profiles between them — some
require full LLM inference for every recovery step, which has direct
cost and latency implications.

## Who should read/watch this

Anyone designing failure-recovery logic for a production agent —
gives concrete metrics to measure instead of just "does it eventually
recover."

## Related entries

- self-healing-framework-reliability-arxiv.md
