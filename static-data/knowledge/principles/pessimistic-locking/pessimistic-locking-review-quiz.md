---
title: "Pessimistic Locking: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate locking concepts"
  - "Design safe distributed locks"
  - "Prevent deadlocks"
prerequisites:
  []
knowledge_refs:
  - "principles/pessimistic-locking"
---

# Pessimistic Locking: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Pessimistic locking acquires the lock? (A: after the write / B: before the read-modify-write / C: never)
- Q2: A distributed lock must have? (A: a lease / B: a queue / C: a cache)
- Q3: Deadlocks are prevented by? (A: canonical lock ordering / B: bigger locks / C: faster disks)
- Q4: True or false: holding a lock across a slow network call is safe with a long lease.
- Q5: On a deadlock error, the application should? (A: ignore / B: retry the transaction / C: crash)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A seat-hold system must guarantee exclusive holds without deadlocks. Design the lock scope, order, lease, and fencing.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "I added a lock" is only half the solution — leases and ordering are the other half.

## Key Takeaways

- Q1: B; Q2: A; Q3: A; Q4: false; Q5: B
- Pessimistic locking serializes when it must
- Leases, fencing, and ordering make it safe
