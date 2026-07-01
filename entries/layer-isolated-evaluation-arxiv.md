---
title: "Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness"
type: "paper"
author: "arXiv:2606.11686"
url: "https://arxiv.org/pdf/2606.11686"
date_published: "2026"
date_added: "2026-07-01"
topic: "evals-and-testing"
status: "indexed"
---

## Why it's here

A concrete, formalized implementation of the "deterministic vs.
latent" distinction already logged in the skill-design-harness-
engineering topic (Tan/Hu lecture transcript). Worth cross-referencing
rather than treating as an unrelated paper.

## Key claim or contribution

Proposes separating a production agent's deterministic scaffold (the
non-LLM code paths — parsing, routing, tool invocation logic) from its
genuinely non-deterministic parts, and gating the deterministic
scaffold with an ordinary regression-locked test harness that involves
no LLM calls at all. The LLM-based, non-deterministic evaluation
machinery is then reserved only for the parts of the system that
actually need it. Cites a broad landscape of existing agent
benchmarks in its references (AgentBench, AgentBoard, SWE-bench, GAIA,
among others) as context for where layer-isolated testing fits
relative to full-system benchmarking.

## Who should read/watch this

Anyone testing their entire agent pipeline with LLM-as-judge evals,
including the parts that are actually deterministic code — this is
the case for splitting that testing strategy in two.

## Related entries

- confident-ai-agent-eval-metrics.md
- vinod-rane-cost-aware-agent-eval.md
