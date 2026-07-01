---
title: "Holos: A Web-Scale LLM-Based Multi-Agent System for the Agentic Web (Section 4.2.2)"
type: "paper"
author: "arXiv:2604.02334"
url: "https://arxiv.org/pdf/2604.02334"
date_published: "2026"
date_added: "2026-07-01"
topic: "deployment-and-observability"
status: "indexed"
---

## Why it's here

A concrete testing methodology for resilience, not just an
architecture description — directly applicable to validating recovery
claims made elsewhere in this topic rather than taking them on faith.

## Key claim or contribution

Runs a chaos-engineering-style resilience test on a web-scale
multi-agent system: 500 complex tasks sampled from the Humanity's Last
Exam dataset, with controlled failure-injection probabilities (ranging
from none to total) simulating agents going offline, crashing mid-task,
or becoming unresponsive. The orchestrator is tasked with real-time
failure detection and dynamic reconfiguration of the task graph —
finding and routing to alternative agents to preserve the integrity of
the overall task chain when a node fails.

## Who should read/watch this

Anyone claiming their multi-agent system "recovers from failures" who
hasn't actually run a controlled failure-injection test to verify it —
this is a concrete methodology for that test, not just the claim.

## Related entries

- graph-based-self-healing-tool-routing.md
