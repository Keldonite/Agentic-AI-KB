---
title: "OWASP Agentic Skills Top 10"
type: "spec / catalog"
author: "OWASP Foundation"
url: "https://owasp.org/www-project-agentic-skills-top-10/"
date_published: "2026-03"
date_added: "2026-07-01"
topic: "security-and-safety"
status: "indexed"
---

## Why it's here

OWASP-vetted vulnerability catalog for the agent-skills attack
surface. The industry-standard reference for this topic — anyone
justifying security decisions to a stakeholder benefits from citing
this alongside the empirical studies.

## Key claim or contribution

Catalogs specific 2026 CVEs against major agent tooling:

- CVE-2026-28363 (ClawJacked, CVSS 9.9): malicious websites can
  brute-force localhost WebSocket connections with no rate limiting,
  silently hijacking local OpenClaw instances, registering new devices
  without user prompts, and exfiltrating data through existing agent
  integrations.
- CVE-2025-59536 and CVE-2026-21852 (Claude Code): repository-controlled
  configuration files can silently execute arbitrary shell commands
  and exfiltrate API keys at project-open time, before any trust
  dialog is shown.
- CVE-2026-22708 (Cursor): an attacker can poison the agent's
  execution environment so allowlisted commands (such as `git branch`)
  deliver arbitrary payloads. Notable case: the allowlist made the
  attack easier by auto-approving the exact commands the attacker
  needed.

Also notes a log-poisoning vulnerability patched in OpenClaw 2026.2.13
where an agent reading its own log files could be steered by
attacker-injected text — a form of indirect prompt injection through
the agent's own operational data.

## Who should read/watch this

Anyone building or deploying an agent using Claude Code, OpenClaw,
Cursor, or similar tooling — check whether your version is affected
by any of the CVEs above and confirm patches are applied.

## Related entries

- snyk-toxicskills-audit.md
- helpnetsecurity-owasp-2026-prompt-injection.md
