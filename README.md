# Agentic AI Engineering KB

A living, versioned knowledge base for people building agentic AI systems — harnesses, tool-use, context management, evals, skill design, memory systems, deployment. Not a general "AI engineer roadmap." Scoped specifically to the practice of building things *with* agentic coding tools (Claude Code, Codex, etc.) and *for* agentic systems.

## Why this exists, and why it's different

Most "awesome-AI" lists are static — a link dump that rots within months. This repo is paired with an **ingestion skill** (`skills/ingest-source/SKILL.md`) that runs live searches, checks new candidates against what's already indexed, and drafts a digest of what's worth adding. The repo is the output of a pipeline, not a one-time curation pass.

Scope is deliberately narrow: agentic engineering, not ML research, not generic prompting tips, not "10 tools to try." If it wouldn't help someone shipping production agent systems, it doesn't belong here.

## Structure

```
/topics/       — six core topic areas, each with a curated, annotated source list
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

## Status

Skill-design-harness-engineering topic (04) is populated with 6 entries. The other five topics remain empty shells with only seed search terms. Next step is running ingestion sweeps on the remaining topics.
## License

CC-BY-4.0 for the curation and annotations. Individual linked sources retain their own licenses — this repo never reproduces source content, only links, summaries in our own words, and structured metadata.

