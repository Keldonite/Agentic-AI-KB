---
slug: security-and-safety
seed_terms:
  - "prompt injection agent security"
  - "SKILL.md supply chain risk"
  - "agent credential secrets management"
  - "AI agent security vulnerabilities 2026"
---

# Security & safety

Cross-cutting concern, not a single layer — a skill can carry a
security bug, an orchestration pattern can leak data across agents, a
memory system can expose sensitive information. This topic covers
attack surfaces specific to agentic systems: prompt injection,
skill/plugin supply-chain risk (malicious or compromised SKILL.md
files, especially those with bundled scripts or external network
calls), credential and secrets handling inside agent workflows, and
audit/compliance patterns for agents with broad read/write access to
company or personal data.

## Seed entries (status: candidate, not yet reviewed)

Pending first ingestion sweep.

## Open questions this topic should eventually answer

- What does a minimal security review checklist look like before
  installing a third-party skill from a marketplace?
- How do teams scope agent credentials so a compromised skill can't
  escalate to full account access?
- What's the actual attack surface difference between a skill with
  bundled scripts vs. one that's instructions-only?
