---
title: "Forage V2: Knowledge Evolution and Transfer in Autonomous Agent Organizations (Section 7.4, citing Phillips et al. 2026)"
type: "paper"
author: "cited via Forage V2, arXiv:2604.19837"
url: "https://arxiv.org/pdf/2604.19837"
date_published: "2026"
date_added: "2026-07-01"
topic: "agent-architectures"
status: "indexed"
---

## Why it's here

The one academic-adjacent source in this batch. Sourced via the
Forage V2 paper's literature review section rather than chasing down
the original Phillips et al. paper directly, since this is the
document actually in hand.

## Key claim or contribution

Identifies five coordination patterns for multi-agent systems:
Generator-Verifier, Orchestrator-Subagent, Agent Teams, Message Bus,
and Shared State — and recommends Orchestrator-Subagent as the
default choice. Separately notes that centralized/pipeline
architectures (where a coordinator assigns subtasks to specialists in
sequence) face a characteristic complexity escalation: adding roles
requires adding coordination mechanisms, which creates dependencies,
which require conflict resolution, which demands more management
infrastructure — each layer patching the side effects of the layer
before it.

## Who should read/watch this

Anyone naming or classifying their own system's coordination pattern
for the first time — useful as shared vocabulary with the rest of the
field, and the complexity-escalation observation is a good early
warning sign to watch for in your own architecture.

## Related entries

- beam-ai-orchestration-patterns.md
