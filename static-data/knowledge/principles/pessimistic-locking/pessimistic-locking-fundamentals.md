---
title: "Pessimistic Locking: Lock Before You Touch"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define pessimistic locking"
  - "Use SELECT ... FOR UPDATE style locks"
  - "Explain lock scope and duration"
  - "Compare with optimistic locking"
prerequisites:
  - "principles/optimistic-locking"
  - "principles/consistency-pattern"
knowledge_refs:
  - "principles/pessimistic-locking"
---

# Pessimistic Locking: Lock Before You Touch

## The Idea

Pessimistic locking acquires the lock before the read-modify-write, so no other writer can interfere — at the cost of waiting. It is right when conflicts are frequent, retries are expensive, or the operation cannot be re-run (charging a card, transferring funds).

The database form: SELECT ... FOR UPDATE locks the row until the transaction commits, serializing writers while readers continue on snapshots.

```sql
-- Pessimistic: lock the row, then act, then commit
BEGIN;
SELECT balance FROM accounts WHERE id = 42 FOR UPDATE;
-- ... compute and write with certainty no one else moved it ...
UPDATE accounts SET balance = 90 WHERE id = 42;
COMMIT;   -- lock released

-- The FOR UPDATE lock guarantees exclusive write access
-- for the duration of the transaction.
```

## Lock Discipline

Lock scope must cover exactly the read-modify-write, and nothing more: acquiring early or holding long multiplies contention and can deadlock. Lock ordering (always lock resources in the same order) prevents circular waits.

## Practice: Lock the Seat

A booking flow must guarantee a seat stays held through the payment attempt (up to 10 minutes).

**Task 1:** Design the lock: row, scope (seat), and duration (hold period with expiry).

**Task 2:** Trace two concurrent bookings for the same seat: who waits, who wins?

**Task 3:** Design the hold expiry so a crashed client releases the seat automatically.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why holding a lock across a network call (payment) is dangerous and how to shorten it.

**Prompt 2 — Compare & Contrast:**
> Compare pessimistic locking with optimistic locking for a bank transfer. Which fits, and why?

**Prompt 3 — Boundary Testing:**
> A locked row's owner crashes mid-transaction. What guarantees the lock is eventually released?

## Key Takeaways

- Pessimistic locking serializes writers at acquisition time
- Right for frequent conflicts and un-rerunnable operations
- Lock scope must cover exactly the read-modify-write
- Consistent lock ordering prevents deadlocks

## Further Reading

- [SELECT FOR UPDATE — PostgreSQL](https://www.postgresql.org/docs/current/sql-select.html)
- [Pessimistic vs Optimistic Locking — Hibernate](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#locking)
