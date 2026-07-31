---
title: "Event Sourcing: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate event sourcing concepts"
  - "Design streams and snapshots"
  - "Build projections"
prerequisites:
  []
knowledge_refs:
  - "patterns/event-sourcing"
---

# Event Sourcing: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: In event sourcing, the truth is? (A: the current state / B: the event log / C: the cache)
- Q2: State is derived by? (A: replay / B: guessing / C: caching)
- Q3: Snapshots bound? (A: replay cost / B: storage / C: nothing)
- Q4: True or false: appends are safe from conflicts.
- Q5: Read models are? (A: projections / B: the write truth / C: backups)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A compliance system must prove the full history of a loan. Design the event store, the snapshot strategy, and the audit query.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why the event log is more truthful than stored state.

## Key Takeaways

- Q1: B; Q2: A; Q3: A; Q4: true; Q5: A
- The log never lies — state is derived
- Snapshots, versioning, and projections make it scale
