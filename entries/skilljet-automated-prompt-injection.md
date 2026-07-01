---
title: "SkillJect: Effectively Automating Skill-Based Prompt Injection for Skill-Enabled Agents"
type: "paper"
author: "arXiv:2602.14211"
url: "https://arxiv.org/abs/2602.14211"
date_published: "2026"
date_added: "2026-07-01"
topic: "security-and-safety"
status: "indexed"
---

## Why it's here

Names the exact defensive weakness this topic needs to address:
attacks camouflaged as legitimate workflow steps, not obvious
malicious instructions.

## Key claim or contribution

Observes that manual prompt-injection attacks against skill-enabled
agents are brittle — explicit malicious instructions tend to get
rejected or ignored when they don't align with the workflow the agent
is already executing. Proposes an automated framework for generating
poisoned skills that get around this by using two coordinated
channels: the artifact channel hides the payload inside an auxiliary
helper script bundled with the skill; the instruction channel rewrites
SKILL.md with a front-loaded inducement, placing the injected content
at the beginning of the skill file and framing the helper script as a
mandatory prerequisite or initialization step the agent is expected
to run before doing anything else.

The framework matters not because the specific tool is public, but
because it demonstrates that the "malicious content stands out"
assumption underlying most defensive audits is not durable — an
attacker with automated tooling can produce skills that pass casual
review while still delivering payloads.

## Who should read/watch this

Anyone whose skill-review process assumes malicious content will look
obviously out of place — this is evidence that assumption doesn't
hold against attackers with even modest automation.

## Related entries

- malicious-agent-skills-in-the-wild-arxiv.md
