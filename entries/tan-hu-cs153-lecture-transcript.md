---
title: "The AI Native Company: How One Founder Becomes a 1000x Engineer (Stanford CS153 guest lecture)"
type: "talk"
author: "Garry Tan (YC) and Diana Hu (YC), Stanford CS153"
url: "https://www.youtube.com/watch?v=Lri2LNYtERM"
date_published: "2026"
date_added: "2026-07-01"
topic: "skill-design-harness-engineering"
status: "indexed"
---

## Why it's here

Primary source, not commentary. Every other entry in this topic is
someone else's write-up of Skillify/GBrain second-hand; this is Tan's
own account, transcribed directly from the talk. Distilled from the
full caption transcript, own words throughout, no reproduction of the
original text.

## Key claims and content

**Origin of Skillify, in Tan's own telling:** he describes it as
emerging almost by accident from repeated use of an agent harness late
at night, rather than a deliberately designed methodology from the
start. He posted about it on X, it went viral, and only afterward did
he formalize it into the ~10-step process (unit tests, LLM evals,
resolver triggers, dedup checks) covered by the secondary sources
already in this topic. Worth noting: this origin story is less tidy
than the polished "10-step methodology" framing in his own later
long-form write-up — a useful reminder to treat any single account of
a tool's origin with some skepticism.

**Skill files, explained plainly:** Tan frames a skill as essentially
a runbook — a sequence any human or agent could follow — with the key
difference from a plain checklist being that a skill can also invoke
code, not just instructions.

**"Deterministic vs. latent" as a design heuristic:** he says most of
his own agent failures came from misclassifying which kind of work a
task was — trying to do deterministic work (should be code) inside a
markdown skill, or trying to force latent/fuzzy reasoning work into
rigid code. Concrete example given: seating a small dinner party by
LLM works fine; seating thousands of people the same way breaks down
and needs deterministic logic instead.

**Resolvers as the fix for context bloat:** the common failure mode of
a CLAUDE.md/AGENTS.md file growing to tens of thousands of tokens gets
solved by moving instructions into separate files loaded only on
demand ("load change_log.md only when writing to the change log"),
rather than keeping everything in the always-loaded context.

**GBrain's architecture, per Tan:** explicitly built on top of
Andrej Karpathy's "knowledge wiki" concept, then extended because
plain grep-based search broke down — he added vector search, backlink
ranking, and describes plans for an "epistemology layer" to
distinguish tracked beliefs/hunches from established facts.

**Diana Hu's framing (control-theory metaphor):** she describes
pre-AI companies as open-loop systems — decisions made on lossy,
undocumented information (Slack DMs, unwritten meeting notes) — versus
a closed-loop system where an agent has read access to every artifact
a company produces and can act on that closed loop. She introduces a
three-role model: individual contributor, DRI (directly responsible
individual, an Apple-derived term), and a new "AI founder" role.

**On evaluation:** Hu argues generic public benchmarks (she names
MMLU) don't validate whether an actual product works — only
user-facing outcomes and human review of agent traces do. She frames
this as requiring ongoing human-in-the-loop labeling of failures,
which then feeds back into the skillify/resolver loop Tan described.

**Growth claims cited (unverified outside this talk):** Hu names three
YC portfolio companies — Salient (voice agents for lending), Happy
Robot (freight/logistics), and Reductum/Reduct (document processing)
— as examples reaching 8-figure revenue within roughly a year using
this agent-embedded approach.

## Who should read/watch this

Anyone drawing on the Skillify/GBrain entries elsewhere in this topic
— this is the primary account those are all reacting to, and it
surfaces the deterministic-vs-latent framing that none of the
secondary write-ups foreground as clearly.

## Confidence note

[FRAME]: growth and revenue figures cited by Hu are claims made in a
promotional lecture context (YC partner speaking to prospective
founders), not independently audited numbers. Treat as directional,
not verified.

## Related entries

- (link to Skillify/GBrain secondary-source entries once drafted)
