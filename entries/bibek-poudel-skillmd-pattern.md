---
title: "The SKILL.md Pattern: How to Write AI Agent Skills That Actually Work"
type: "blog"
author: "Bibek Poudel"
url: "https://bibek-poudel.medium.com/the-skill-md-pattern-how-to-write-ai-agent-skills-that-actually-work-72a3169dd7ee"
date_published: "2026-02"
date_added: "2026-07-01"
topic: "skill-design-harness-engineering"
status: "indexed"
---

## Why it's here

Practical, debugging-oriented take rather than pure spec explanation.
Directly useful for iterating on skills that already exist.

## Key claim or contribution

Central claim: when a skill fails to trigger, the cause is almost
always a weak or vague `description` field, not the instructions body.
Description is what the agent matches against a request, so it needs
concrete trigger phrases, not just a category label.

## Who should read/watch this

Anyone with an existing skill that isn't firing reliably — check the
description field before rewriting instructions.

## Related entries

- anthropic-agent-skills-spec.md
