---
title: "MVCC in Production: Postgres and Isolation Levels"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Compare isolation levels"
  - "Explain visibility rules"
  - "Tune vacuum"
  - "Handle write skew"
prerequisites:
  []
knowledge_refs:
  - "patterns/mvcc-pattern"
---

# MVCC in Production: Postgres and Isolation Levels

## Isolation Levels

Read committed takes a fresh snapshot per statement; repeatable read (snapshot isolation in Postgres) takes one per transaction. Read committed is the default — each statement sees the latest committed data. Repeatable read guarantees the whole transaction sees one consistent snapshot, but both still allow write skew and (with certain engines) phantom anomalies.

```sql
-- Isolation levels in PostgreSQL
BEGIN ISOLATION LEVEL READ COMMITTED;    -- snapshot per statement
SELECT balance FROM accounts WHERE id = 1;  -- sees latest committed
-- another tx commits an update; THIS statement sees it
SELECT balance FROM accounts WHERE id = 1;  -- new snapshot, new value
COMMIT;

BEGIN ISOLATION LEVEL REPEATABLE READ;   -- one snapshot for the tx
SELECT balance FROM accounts WHERE id = 1;
-- concurrent update commits; this statement STILL sees the old value
SELECT balance FROM accounts WHERE id = 1;
COMMIT;
-- Write skew: two txs each read old values and both write — neither
-- sees the other until commit. MVCC prevents lost updates only if
-- the write rechecks (SELECT ... FOR UPDATE).
```

## Vacuum and Bloat

Old versions accumulate as dead tuples; vacuum removes them and reclaims space. Autovacuum tunes itself, but pathological workloads (massive updates, long transactions) need manual attention. Index bloat follows table bloat: a table that is 50% dead tuples makes every scan 2x cost.

## Practice: Tune the Vacuum

A table updated 1M rows/hour shows 60% bloat and slow scans.

**Task 1:** Measure bloat with pg_stat_user_tables and estimate dead tuples.

**Task 2:** Set autovacuum thresholds and a manual vacuum schedule for the peak.

**Task 3:** Verify scan cost recovery after the vacuum run.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me the difference between a per-statement snapshot and a per-transaction snapshot. Ask me to show the observable difference.

**Prompt 2 — Implementation Design:**
> Design a balance-transfer flow safe under repeatable read: where do you add FOR UPDATE and why?

**Prompt 3 — Boundary Testing:**
> A report transaction runs for an hour and blocks vacuum. Design the statement-level isolation or snapshot freeze that bounds the bloat.

## Key Takeaways

- Isolation level = snapshot scope
- Read committed vs repeatable read differ per statement
- Dead tuples need vacuum to reclaim space
- Write skew needs explicit locking, not MVCC

## Further Reading

- [PostgreSQL — Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
- [Routine Database Maintenance — vacuum](https://www.postgresql.org/docs/current/routine-vacuuming.html)
