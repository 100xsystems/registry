---
title: "Advanced Optimistic Locking: Conflict-Free Alternatives"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Recognize when optimistic locking breaks down"
  - "Use atomic conditional writes where possible"
  - "Apply CRDTs for conflict-free convergence"
  - "Combine optimistic locking with idempotency keys"
prerequisites:
  []
knowledge_refs:
  - "principles/optimistic-locking"
---

# Advanced Optimistic Locking: Conflict-Free Alternatives

## Hot-Row Breakdown

When a single row is written by thousands of concurrent clients (a popular counter, a seat map), conflicts approach 100% and optimistic locking degenerates into retry churn. The answer is a different data shape: shard the counter, use atomic increments, or move the hot state to a fast store with a reconciliation step.

```sql
-- Atomic conditional: no version needed for simple guarded writes
UPDATE inventory
SET stock = stock - 1
WHERE sku = 'A1' AND stock > 0;    -- atomic guard: never oversells

-- For hot counters: shard into per-shard counters
-- UPDATE counters SET n = n + 1 WHERE shard = 1;  (then SUM over shards)
-- Atomic ops beat read-check-write on hot rows.
```

## Conflict-Free by Design

CRDTs eliminate conflicts for merge-friendly data (sets, counters, text): replicas diverge and merge deterministically. Pairing optimistic locking (for sequential edits) with CRDTs (for concurrent merges) covers most collaborative workloads.

Idempotency keys + optimistic locking combine to make retries safe against both duplicates and lost updates.

## Practice: Escalate the Locking Strategy

A ticket sale: 10,000 seats, 50k concurrent requests.

**Task 1:** Show why optimistic locking on a single seat-map row collapses.

**Task 2:** Redesign: per-seat rows with atomic conditional update (stock>0 guard).

**Task 3:** Add the idempotency key so retries do not double-book, and the reconciliation for partial failures.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why atomic conditional updates are optimistic locking with the check moved into the write itself.

**Prompt 2 — Implementation Design:**
> Design a collaborative document: which fields use CRDTs, which use optimistic locking with conflict UI? Justify each.

**Prompt 3 — Boundary Testing:**
> A distributed counter needs exact totals for billing (not approximation). Design the path from sharded counters to an exact reconciled total.

## Key Takeaways

- Hot rows break optimistic locking — change the data shape
- Atomic conditionals move the check into the write
- CRDTs remove conflicts for merge-friendly data
- Idempotency keys make retries safe on top of locking

## Further Reading

- [CRDTs for Collaborative Editing](https://hal.inria.fr/inria-00555588/document)
- [Atomic Ops in PostgreSQL](https://www.postgresql.org/docs/current/sql-update.html)
