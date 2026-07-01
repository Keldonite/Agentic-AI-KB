---
title: "Prompt Injection Still Drives Most Agentic AI Security Failures in Production"
type: "industry report"
author: "Help Net Security, reporting on OWASP 2026"
url: "https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/"
date_published: "2026-06"
date_added: "2026-07-01"
topic: "security-and-safety"
status: "indexed"
---

## Why it's here

Aggregate framing for where attacks are actually landing. Ties
together several of the CVEs OWASP catalogs while adding the coding-
agent-as-primary-attack-surface observation.

## Key claim or contribution

Reports OWASP's 2026 State of AI Surveyor tracking 53 agentic
projects, with 28 of them being coding agents — meaning coding
agents are the dominant source of new attack data this year, not
consumer chatbot deployments.

Highlights two containment-inversion CVEs against coding tools:
CVE-2026-22708 against Cursor, where an attacker poisons the agent's
execution environment so allowlisted commands like `git branch`
deliver arbitrary payloads (the allowlist made the attack easier by
auto-approving the exact commands the attacker needed), and
CVE-2025-59532 against OpenAI's Codex CLI, where the agent's own
output could redefine the boundary of its sandbox.

Also mentions hackerbot-claw, described as an attack that worked its
way up the stack starting from GitHub Actions misconfigurations
across open source repositories in February 2026.

## Who should read/watch this

Anyone deploying coding agents (Claude Code, Cursor, Codex) — coding
agents are where the attack data is concentrating right now,
disproportionate to their share of overall agent deployments.

## Related entries

- owasp-agentic-skills-top-10.md
- cyberdesserts-ai-agent-security-2026.md
