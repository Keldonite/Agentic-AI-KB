---
title: "Agent Skills Specification"
type: "spec / docs"
author: "Anthropic"
url: "https://agentskills.io/specification"
date_published: "2025-12"
date_added: "2026-07-01"
topic: "skill-design-harness-engineering"
status: "indexed"
---

## Why it's here

This is the primary spec everything else in this topic reacts to or
builds on. Defines the SKILL.md format, the progressive disclosure
pattern (metadata → instructions → resources), and directory
conventions (scripts/, references/, assets/).

## Key claim or contribution

Skills load in layers: name/description (~100 tokens, always loaded),
full instructions (loaded only when triggered), and resource files
(loaded only when the instructions call for them). This keeps context
usage low even with many skills installed.

## Who should read/watch this

Anyone writing a SKILL.md for the first time, or debugging why a skill
isn't triggering — start here before any secondary commentary.

## Related entries

- bibek-poudel-skillmd-pattern.md
- lavi-nigam-skill-design-patterns.md
