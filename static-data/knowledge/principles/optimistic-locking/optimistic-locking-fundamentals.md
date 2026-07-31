---
title: "Optimistic Locking: Check Before You Write"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define optimistic locking"
  - "Use version numbers to detect conflicts"
  - "Handle conflict on write"
  - "Compare with pessimistic locking"
prerequisites:
  - "principles/consistency-pattern"
  - "principles/idempotency"
knowledge_refs:
  - "principles/optimistic-locking"
---

# Optimistic Locking: Check Before You Write

## The Idea

Optimistic locking lets many readers and writers proceed concurrently, assuming conflicts are rare. Each row carries a version; a write succeeds only if the version it read still matches. If it does not, the write fails with a conflict the application resolves.

It trades retries (on conflict) for concurrency (always allowed). For read-heavy, low-contention data — profiles, documents, carts — it beats holding locks.

```sql
-- Optimistic: version-guarded update
UPDATE accounts
SET balance = 100, version = version + 1
WHERE id = 42 AND version = 7;      -- only if unchanged since read

-- If 0 rows affected: someone else wrote first -> conflict
-- The app re-reads, re-applies the change, and retries.
-- Version (or updated_at) is the conflict detector.
```

## Why Optimistic

Pessimistic locks serialize writers and force waiting — fine for hot rows, costly when contention is low. Optimistic locking has zero lock overhead in the happy path; the cost appears only when conflicts actually happen.

## Practice: Detect the Conflict

Two users edit the same document concurrently; both loaded version 3.

**Task 1:** Trace the two writes: which succeeds and what happens to the loser?

**Task 2:** Design the conflict UX: reload, merge, or overwrite — and when each is right.

**Task 3:** Compare with a version-less update (lost update bug). Show the difference.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why the lost-update bug disappears when a version guard is added. Start with the two-reader scenario.

**Prompt 2 — Compare & Contrast:**
> Compare optimistic locking with pessimistic locking and atomic conditional updates. When is each cheapest?

**Prompt 3 — Boundary Testing:**
> A long-running form holds a document open for an hour; by submit time, 20 versions have passed. Design the merge/retry path that does not frustrate the user.

## Key Takeaways

- Version guards detect conflicts at write time
- Optimistic = no lock overhead, retry on conflict
- Best for read-heavy, low-contention data
- Conflict UX is part of the design, not an afterthought

## Further Reading

- [Optimistic Concurrency — Wikipedia](https://en.wikipedia.org/wiki/Optimistic_concurrency_control)
- [PostgreSQL — Row-level Locks & MVCC](https://www.postgresql.org/docs/current/mvcc.html)
