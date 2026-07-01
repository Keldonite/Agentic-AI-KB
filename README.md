# Agentic AI Engineering KB

A living, versioned knowledge base for people building agentic AI systems — harnesses, tool-use, context management, evals, skill design, memory systems, deployment. Not a general "AI engineer roadmap." Scoped specifically to the practice of building things *with* agentic coding tools (Claude Code, Codex, etc.) and *for* agentic systems.

## Why this exists, and why it's different

Most "awesome-AI" lists are static — a link dump that rots within months. This repo is paired with an **ingestion skill** (`skills/ingest-source/SKILL.md`) that runs live searches, checks new candidates against what's already indexed, and drafts a digest of what's worth adding. The repo is the output of a pipeline, not a one-time curation pass.

Scope is deliberately narrow: agentic engineering, not ML research, not generic prompting tips, not "10 tools to try." If it wouldn't help someone shipping production agent systems, it doesn't belong here.

## Structure

```
/topics/       — seven core topic areas, each with a curated, annotated source list
/entries/      — individual source entries in a consistent template (see entries/TEMPLATE.md)
/skills/       — the ingestion skill that keeps this repo alive
/tools/        — utility scripts that support maintaining the KB (not subject to the topic scope test)
CONTRIBUTING.md
```

## Topics

1. **Agent architectures** — orchestration patterns, single-agent vs. multi-agent, planner/executor splits
2. **Tool use & context management** — context windows, tool-call design, retrieval strategies
3. **Evals & testing** — how to test non-deterministic systems, eval harnesses, regression prevention
4. **Skill design & harness engineering** — SKILL.md patterns, meta-skills, resolver/routing systems
5. **Memory systems** — persistent agent memory, knowledge graphs vs. RAG, second-brain architectures
6. **Deployment & observability** — running agents in production, monitoring, failure recovery
7. **Security & safety** — prompt injection, skill supply-chain risk, credential handling, audit/compliance for agents with broad data access

## Status

All 7 topics are populated with a first pass of curated, annotated entries — 33 entries total. Entry breakdown: skill-design-harness-engineering (6), agent-architectures (4), memory-systems (4), tool-use-context-management (4), evals-and-testing (5), deployment-and-observability (5), security-and-safety (6). Next step is repeat ingestion passes as new sources appear, plus running the ingestion skill programmatically rather than driving it manually.

## License

CC-BY-4.0 for the curation and annotations. Individual linked sources retain their own licenses — this repo never reproduces source content, only links, summaries in our own words, and structured metadata.
