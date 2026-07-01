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

## Entries

- [Snyk, "ToxicSkills Study"](../entries/snyk-toxicskills-audit.md) — first comprehensive audit, ~3,984 skills scanned
- [Liu et al., "Malicious Agent Skills in the Wild" (arXiv:2602.06547, USENIX Security 2026)](../entries/malicious-agent-skills-in-the-wild-arxiv.md) — attacker objectives and attack channels
- [OWASP Agentic Skills Top 10](../entries/owasp-agentic-skills-top-10.md) — vetted CVE catalog for the year
- [arXiv:2602.14211, "SkillJect"](../entries/skilljet-automated-prompt-injection.md) — automated poisoned-skill generation, camouflage attacks
- [Cyberdesserts, "AI Agent Security Risks 2026"](../entries/cyberdesserts-ai-agent-security-2026.md) — aggregate year framing, MCP as connective tissue
- [Help Net Security / OWASP 2026 State of AI Surveyor](../entries/helpnetsecurity-owasp-2026-prompt-injection.md) — coding agents as dominant attack surface

## Open questions this topic should eventually answer

- What does a minimal security review checklist look like before
  installing a third-party skill from a marketplace?
- How do teams scope agent credentials so a compromised skill can't
  escalate to full account access?
- What's the actual attack surface difference between a skill with
  bundled scripts vs. one that's instructions-only?
