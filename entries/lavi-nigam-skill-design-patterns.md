---
title: "5 Agent Skill Design Patterns Every ADK Developer Should Know"
type: "blog"
author: "Lavi Nigam"
url: "https://lavinigam.com/posts/adk-skill-design-patterns/"
date_published: "2026-03"
date_added: "2026-07-01"
topic: "skill-design-harness-engineering"
status: "indexed"
---

## Why it's here

Fills a gap other entries in this topic don't cover: content
architecture inside a SKILL.md, as opposed to the container format
itself (which the spec and other guides already cover well).

## Key claim or contribution

Names five reusable structural patterns for what a skill's body
actually does: Tool Wrapper (thin instructions over an external
tool/API), Generator (fills a template using a style guide), Reviewer
(evaluates work against a checklist), Pipeline (strict multi-step
sequence with gates), and Inversion (interviews the user to gather
inputs before producing output). Notes these patterns compose — a
Pipeline can embed a Reviewer step, for example.

## Who should read/watch this

Anyone past the "I know the file format" stage and stuck on how to
structure what's actually inside a new skill.

## Related entries

- anthropic-agent-skills-spec.md
- termdock-agent-skills-guide.md
