---
title: "Eventual Consistency: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate eventual consistency concepts"
  - "Design reliable propagation"
  - "Choose conflict strategies"
prerequisites:
  []
knowledge_refs:
  - "principles/eventual-consistency"
---

# Eventual Consistency: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Eventual consistency guarantees convergence? (A: immediately / B: after writes stop / C: never)
- Q2: The transactional outbox pattern guarantees? (A: exactly-once delivery / B: at-least-once with idempotent consumers / C: zero latency)
- Q3: A delete racing an edit needs? (A: tombstone / B: a bigger TTL / C: a lock)
- Q4: True or false: replication lag should be monitored like any other metric.
- Q5: LWW at value granularity can lose? (A: nothing / B: concurrent field edits / C: the whole database)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A multi-region cart must never lose items but tolerates slight lag. Design the read-your-writes route, the outbox, and the conflict policy.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "eventually consistent" needs bounds, alerts, and replay — not faith.

## Key Takeaways

- Q1: B; Q2: B; Q3: A; Q4: true; Q5: B
- Convergence needs mechanisms, not promises
- Idempotency and tombstones make propagation safe
