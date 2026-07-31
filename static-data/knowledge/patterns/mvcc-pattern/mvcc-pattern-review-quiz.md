---
title: "MVCC: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate MVCC concepts"
  - "Choose isolation levels"
  - "Design distributed snapshots"
prerequisites:
  []
knowledge_refs:
  - "patterns/mvcc-pattern"
---

# MVCC: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: MVCC readers see? (A: a consistent snapshot / B: the latest write / C: random rows)
- Q2: Readers and writers? (A: never block each other / B: always block / C: share locks)
- Q3: Read committed takes a snapshot? (A: per statement / B: per transaction / C: never)
- Q4: True or false: snapshot isolation prevents write skew.
- Q5: Old versions are reclaimed by? (A: vacuum / B: the optimizer / C: the cache)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> An analytics read runs an hour while writes stream in. Design the isolation and the vacuum policy that keeps both healthy.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why versioning beats locking for read-heavy workloads.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: false; Q5: A
- Versions make readers and writers coexist
- Isolation level and vacuum are the operational dials
