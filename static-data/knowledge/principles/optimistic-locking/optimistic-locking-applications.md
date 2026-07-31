---
title: "Optimistic Locking in Production: MVCC and Retries"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Explain MVCC as the database-level optimistic mechanism"
  - "Design retry loops with bounded attempts"
  - "Use updated_at vs version counters"
  - "Handle partial failures in retries"
prerequisites:
  []
knowledge_refs:
  - "principles/optimistic-locking"
---

# Optimistic Locking in Production: MVCC and Retries

## MVCC

Databases use Multi-Version Concurrency Control: readers see a snapshot, writers create new versions, and conflicts are detected when a transaction commits against a stale snapshot. This is optimistic concurrency at the engine level — reads never block, and write conflicts surface at commit.

```text
MVCC in one picture:
  t0: T1 reads balance=100 (snapshot)
  t1: T2 reads balance=100 (snapshot)
  t2: T2 writes balance=90  -> new version, commits
  t3: T1 writes balance=90  -> CONFLICT (stale snapshot)
T1 must retry with the fresh version. Read-mostly workloads
never wait — that is why MVCC dominates modern databases.
```

## Retry Design

On conflict, the application re-reads, re-applies, and retries — with a bounded attempt count and backoff. Infinite retry on a hot row makes things worse; exponential backoff with a small max keeps the retry storm contained.

## Practice: Build the Retry Loop

A seat-booking flow increments booked count on a popular event.

**Task 1:** Implement the version-guarded update with a retry loop (max 3 attempts, backoff).

**Task 2:** Handle the terminal state: after 3 conflicts, return a friendly "seats changed" error.

**Task 3:** Verify idempotency: a retry must not double-count a seat.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why the retry must re-read the fresh version rather than blindly retrying the stale one.

**Prompt 2 — Implementation Design:**
> Design optimistic locking for a leaderboard with millions of score writes. When does optimistic locking break down, and what replaces it?

**Prompt 3 — Boundary Testing:**
> A conflict occurs after a side effect (email sent) but before the write. Design the ordering that makes the retry safe.

## Key Takeaways

- MVCC gives databases optimistic concurrency for free
- Retries must re-read and re-apply, with bounds
- Version counters beat timestamps for concurrent writes
- Side effects before writes break retry safety

## Further Reading

- [MVCC — PostgreSQL Docs](https://www.postgresql.org/docs/current/mvcc.html)
- [Optimistic Concurrency — Microsoft Docs](https://learn.microsoft.com/en-us/ef/core/saving/concurrency)
