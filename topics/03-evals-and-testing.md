---
slug: evals-and-testing
seed_terms:
  - "LLM agent eval harness"
  - "testing non-deterministic AI systems"
  - "regression testing agent behavior"
---

# Evals & testing

How to test systems whose output isn't deterministic: eval harness
design, regression prevention, and the difference between output
checking and process checking.

## Seed entries (status: candidate, not yet reviewed)

Pending first ingestion sweep.

## Entries

- [Promptfoo, "Evaluate Coding Agents"](../entries/promptfoo-evaluate-coding-agents.md) — why agent evals differ from plain LLM evals, start here
- [Confident AI, "LLM Agent Evaluation Metrics in 2026"](../entries/confident-ai-agent-eval-metrics.md) — end-to-end / trajectory / component-level taxonomy
- [arXiv:2606.11686, "Layer-Isolated Evaluation"](../entries/layer-isolated-evaluation-arxiv.md) — separating deterministic scaffold testing from LLM-based eval
- [Vinod Rane, "Chapter 8: Agent Evaluation for LLMs"](../entries/vinod-rane-cost-aware-agent-eval.md) — cost-tiered evaluation strategy
- [Vervali, "AI & LLM App Testing 2026"](../entries/vervali-llm-testing-2026.md) — LLM-as-judge reliability studies

## Open questions

- What's the minimum viable eval suite for a solo operator vs. a team?
- How do you eval the agent's judgment, not just its final output?
