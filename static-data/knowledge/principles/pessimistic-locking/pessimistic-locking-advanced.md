---
title: "Advanced Pessimistic Locking: Deadlock Avoidance and Escalation"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Design lock hierarchies that prevent deadlock"
  - "Handle deadlock detection and retry"
  - "Choose lock granularity deliberately"
  - "Escalate to serialized structures when needed"
prerequisites:
  []
knowledge_refs:
  - "principles/pessimistic-locking"
---

# Advanced Pessimistic Locking: Deadlock Avoidance and Escalation

## Deadlock Avoidance

Deadlocks happen when two transactions each hold a lock the other needs. Prevention: acquire locks in a canonical order (e.g., always account A then B, sorted by ID). Detection: databases detect wait cycles and abort one transaction, which the app must retry.

```text
Deadlock avoidance rules:
  - Lock in a canonical order (sort resource IDs first)
  - Keep transactions short and single-purpose
  - Use NOWAIT / lock_timeout to fail fast instead of waiting forever
  - On deadlock error (40P01 in Postgres), retry the transaction

Escalation ladder:
  row lock -> table partition lock -> advisory lock -> queue/serialization
  Move up only when row-level serialization cannot do the job.
```

## Granularity and Escalation

Fine-grained locks (rows) maximize concurrency; coarse locks (tables, partitions) simplify but serialize. Escalate deliberately: a global sequence or a single-writer queue replaces row locking when the hot resource is a counter or a total, not a row.

## Practice: Eliminate the Deadlock

Transfers lock (A then B) in one code path and (B then A) in another.

**Task 1:** Reproduce the deadlock with two concurrent transfers in opposite orders.

**Task 2:** Fix with canonical ordering (sort account IDs before locking).

**Task 3:** Add deadlock detection handling (retry on 40P01) and lock_timeout as a backstop.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why lock ordering prevents deadlock and why detection-with-retry is the pragmatic fallback.

**Prompt 2 — Implementation Design:**
> Design a single-writer queue for a hot shared counter, and describe when it beats row locks.

**Prompt 3 — Boundary Testing:**
> A transaction locks 100 rows and the lock manager starts escalating. Design the granularity policy that avoids escalation storms.

## Key Takeaways

- Canonical lock ordering prevents deadlocks
- Detection + retry is the pragmatic backstop
- Granularity is a deliberate concurrency decision
- Escalate to serialized structures for hot shared state

## Further Reading

- [PostgreSQL — Deadlock Handling](https://www.postgresql.org/docs/current/explicit-locking.html#LOCKING-DEADLOCKS)
- [Lock Hierarchy — Operating Systems Concepts](https://en.wikipedia.org/wiki/Lock_hierarchy)
