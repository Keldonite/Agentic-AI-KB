---
title: "Learning Agent-Compatible Context Management for Long-Horizon Tasks (AdaCoM)"
type: "paper"
author: "arXiv:2605.30785"
url: "https://arxiv.org/pdf/2605.30785"
date_published: "2026"
date_added: "2026-07-01"
topic: "tool-use-context-management"
status: "indexed"
---

## Why it's here

Formal research treatment of an idea already logged as a practitioner
heuristic elsewhere in this repo (the resolver pattern in
skill-design-harness-engineering: load only what's needed, when
needed). Worth cross-referencing rather than treating as unrelated.

## Key claim or contribution

Proposes an external LLM that manages what context gets shown to a
second, frozen (untrained) agent before each step, using task feedback
to update only the manager rather than retraining the underlying
agent. The stated goal is discovering agent-compatible context
management strategies without needing to fine-tune the agent itself —
relevant for long-horizon tasks like multi-step research or extended
tool-use sequences where context degradation compounds over many
steps.

## Who should read/watch this

Anyone building long-running agent workflows (multi-step research,
extended tool chains) who's hit context degradation and is looking for
a more principled approach than manual context trimming.

## Related entries

- (cross-reference: resolver pattern in skill-design-harness-engineering topic)
