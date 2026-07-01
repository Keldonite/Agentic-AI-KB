---
slug: skill-design-harness-engineering
seed_terms:
  - "SKILL.md agent skills"
  - "agent harness engineering"
  - "meta-skill self-improving agent"
  - "Claude Code skill patterns"
  - "agentic coding workflow reuse"
---

# Skill design & harness engineering

How practitioners turn repeated agent workflows into reusable, testable
components — skill files, meta-skills that generate skills, resolver/
routing systems, and the testing discipline needed to keep skills from
rotting.

## Entries

- [Anthropic Agent Skills Specification](../entries/anthropic-agent-skills-spec.md) — the source spec
- [Ling et al., "Agent Skills: A Data-Driven Analysis" (arXiv:2602.08004)](../entries/ling-et-al-agent-skills-analysis.md) — empirical study, 40k+ skills
- [Bibek Poudel, "The SKILL.md Pattern"](../entries/bibek-poudel-skillmd-pattern.md) — why skills fail to trigger
- [Termdock, "Agent Skills Guide 2026"](../entries/termdock-agent-skills-guide.md) — composition at scale, Superpowers
- [Lavi Nigam, "5 Agent Skill Design Patterns"](../entries/lavi-nigam-skill-design-patterns.md) — content architecture inside SKILL.md

## Open questions this topic should eventually answer

- When does a workflow "earn" being turned into a skill vs. staying ad hoc?
- How do teams (not just solo operators) version and code-review skills?
- What does a minimal eval/test discipline for a skill look like?
