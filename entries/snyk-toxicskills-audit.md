---
title: "Snyk Finds Prompt Injection in 36%, 1467 Malicious Payloads in a ToxicSkills Study of Agent Skills Supply Chain Compromise"
type: "industry report"
author: "Snyk Labs (Beurer-Kellner et al.)"
url: "https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/"
date_published: "2026-02"
date_added: "2026-07-01"
topic: "security-and-safety"
status: "indexed"
---

## Why it's here

The strongest single data point in this topic — first comprehensive
security audit of the agent skills ecosystem at real scale.

## Confidence note

[FRAME]: numbers come from a vendor security team publishing their own
audit, not a peer-reviewed independent baseline. Directional evidence
of scale, not a settled benchmark.

## Key claim or contribution

Scanned roughly 3,984 skills across ClawHub and skills.sh in February
2026: 13.4% (534 skills) contained at least one critical-level issue
(malware distribution, prompt injection, or exposed secrets); 36.82%
(1,467 skills) had at least one security flaw at any severity level,
from hardcoded API keys to dangerous third-party content exposure.

Flags three structural problems with the current skill ecosystem:
skills install with the full permissions of the agent that loads them
— there is no sandbox by default; publishing a new skill requires only
a SKILL.md file and a one-week-old GitHub account, with no code
signing or security review gate; and roughly 2.9% of ClawHub skills
(and 21% of confirmed malicious samples) dynamically fetch and execute
content from remote sources at runtime, meaning even a skill that
passes a static audit at install time can behave maliciously later.

## Who should read/watch this

Anyone about to install a third-party skill from a marketplace —
before doing so, at minimum read the SKILL.md, check the publisher's
account age, and note whether the skill fetches content from remote
URLs at runtime.

## Related entries

- malicious-agent-skills-in-the-wild-arxiv.md
- owasp-agentic-skills-top-10.md
