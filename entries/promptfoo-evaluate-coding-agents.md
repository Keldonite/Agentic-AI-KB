---
title: "Evaluate Coding Agents"
type: "docs"
author: "Promptfoo"
url: "https://www.promptfoo.dev/docs/guides/evaluate-coding-agents/"
date_published: "2026"
date_added: "2026-07-01"
topic: "evals-and-testing"
status: "indexed"
---

## Why it's here

Clean conceptual framing worth reading before any of the more tactical
entries in this topic — explains why agent evals are a different
problem from plain LLM evals, not just a bigger version of the same
problem.

## Key claim or contribution

Standard LLM evals test a function: given input X, does output Y meet
criteria Z. Agent evals test a system with emergent behavior, and
non-determinism compounds across the whole run rather than affecting
one generation — a plain chat model's temperature affects a single
output, but an agent's temperature affects every tool call, every
decision to read another file, every choice to retry, and small
variations cascade across the sequence.

Makes a sharp point about hidden cost: two agents can produce
identical final outputs while one read 3 files and the other read 30
— cost, latency, and failure modes differ dramatically even when the
end result looks the same, so evaluating only the final output misses
this entirely. Also argues capability is gated by the harness, not
just the model — a model can't be prompted into reading files if the
harness never gave it that tool — meaning you're evaluating the
system as a whole, not the model in isolation.

## Who should read/watch this

Anyone new to agent evaluation who's been applying plain LLM-eval
thinking (input/output pairs) to a multi-step agent system — read this
first, before the more tactical entries in this topic.

## Related entries

- confident-ai-agent-eval-metrics.md
