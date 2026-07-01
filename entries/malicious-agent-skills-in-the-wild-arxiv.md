---
title: "Malicious Agent Skills in the Wild: A Large-Scale Security Empirical Study"
type: "paper"
author: "Liu et al., USENIX Security 2026"
url: "https://arxiv.org/html/2602.06547v1"
date_published: "2026-02"
date_added: "2026-07-01"
topic: "security-and-safety"
status: "indexed"
---

## Why it's here

Peer-reviewed empirical study complementing the Snyk industry audit
— gives the taxonomy of what attackers actually try to do, not just
how many bad skills exist.

## Key claim or contribution

Names three attacker objectives observed in confirmed malicious skills:
data theft (credentials, source code, conversation context), agent
hijacking (unauthorized actions, safety bypass), and persistence
(supply chain compromise, hidden triggers).

Distinguishes two attack channels: code-level attacks through bundled
scripts (credential harvesting, network reconnaissance, data
transmission over the network) and instruction-level attacks through
malicious directives embedded in SKILL.md itself (prompt injection,
hidden instructions steering the agent toward attacker-chosen tools
or outputs).

Flags a structural gap in the ecosystem: as of January 2026, no major
AI agent vendor maintained an official centralized skill registry
with full visibility into all deployed skills — meaning provenance
tracking is an open problem, not a solved one, at the platform level.

## Who should read/watch this

Anyone building a threat model for an agent that loads third-party
skills — this gives the actual observed attacker objective set, not
a hypothetical one.

## Related entries

- snyk-toxicskills-audit.md
- skilljet-automated-prompt-injection.md
