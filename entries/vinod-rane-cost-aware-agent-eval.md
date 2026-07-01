---
title: "Chapter 8: Agent Evaluation for LLMs: How to Test Tools, Trajectories, and LLM-as-Judge"
type: "blog"
author: "Vinod Rane"
url: "https://medium.com/@vinodkrane/chapter-8-agent-evaluation-for-llms-how-to-test-tools-trajectories-and-llm-as-judge-788f6f3e0d52"
date_published: "2026-05"
date_added: "2026-07-01"
topic: "evals-and-testing"
status: "indexed"
---

## Why it's here

The practical cost-aware complement to the more architectural
Layer-Isolated Evaluation entry — gives a tiered spending strategy
rather than just the principle of separating deterministic from
non-deterministic checks.

## Key claim or contribution

Frames cost-aware evaluation as spending compute where it creates the
most signal, not running every check on every output. Proposes a
three-tier structure: deterministic checks (schema validation, tool
call format checks, output length bounds, JSON parsing, safety filter
passes) run on 100% of outputs at near-zero cost, since they catch
common failures without needing any LLM judge at all; a lightweight
fine-tuned judge model (example given: a ~440M-parameter model)
running in milliseconds at a fraction of a frontier-model-judge cost,
used for hallucination detection, factuality checks, and grounding
verification at scale; and, implicitly, frontier-model judges reserved
for the highest-stakes remaining cases. Cites Galileo's "Luna" model
as a 2026 example of the lightweight-judge tier, running at sub-200ms
latency.

## Who should read/watch this

Anyone running every single agent output through an expensive frontier
LLM judge — most of that spend is likely going toward catching things
a near-zero-cost deterministic check would have caught anyway.

## Related entries

- layer-isolated-evaluation-arxiv.md
- vervali-llm-testing-2026.md
