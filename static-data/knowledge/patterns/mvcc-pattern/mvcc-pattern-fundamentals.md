---
title: "MVCC: Multi-Version Concurrency Control"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the MVCC model"
  - "Describe version chains"
  - "Understand snapshot isolation"
  - "Know why reads do not block"
prerequisites:
  - "principles/optimistic-locking"
  - "principles/pessimistic-locking"
knowledge_refs:
  - "patterns/mvcc-pattern"
---

# MVCC: Multi-Version Concurrency Control

## The Model

MVCC keeps multiple versions of each row instead of overwriting. A writer creates a new version; readers see the version that existed when their transaction started. Because readers never touch the new version, they never block writers — the core win over row locks.

```sql
-- MVCC in Postgres: every row carries xmin/xmax version markers
-- Tx 1 (begins first): reads the row at its snapshot
BEGIN;
SELECT balance FROM accounts WHERE id = 1;   -- sees v0 (100)

-- Concurrent Tx 2 updates the row:
BEGIN;
UPDATE accounts SET balance = 90 WHERE id = 1;  -- creates v1
COMMIT;

-- Tx 1 reads again: still sees v0 (100) — its snapshot
SELECT balance FROM accounts WHERE id = 1;   -- 100, not 90
COMMIT;
-- No locks were held by Tx 2's write: readers never blocked.
```

## Snapshots

Each transaction takes a snapshot — the set of committed versions visible to it — at its start (or statement). Versions a transaction itself created are visible to it; versions from uncommitted or later transactions are not. Old versions stay until no snapshot references them, which is where vacuuming comes in.

## Practice: Trace the Versions

A bank balance is updated by three overlapping transactions.

**Task 1:** Trace the version chain as each transaction commits.

**Task 2:** Show what each concurrent snapshot sees.

**Task 3:** Identify the anomaly (write skew) that snapshot isolation still allows.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why keeping versions removes the reader-writer conflict. Start with a long read.

**Prompt 2 — Compare & Contrast:**
> Compare MVCC with pessimistic locking and with optimistic rechecking. When does each fit?

**Prompt 3 — Boundary Testing:**
> A long transaction keeps old versions alive and storage grows. Design the vacuum/sweep policy that reclaims them safely.

## Key Takeaways

- MVCC keeps versions so readers never block
- Each transaction reads a consistent snapshot
- Old versions live until no snapshot needs them
- Snapshot isolation still has write-skew anomalies

## Further Reading

- [PostgreSQL — MVCC](https://www.postgresql.org/docs/current/mvcc.html)
- [MVCC — Wikipedia](https://en.wikipedia.org/wiki/Multiversion_concurrency_control)
