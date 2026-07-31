---
title: "Two-Phase Commit in Production: XA, Databases, and Coordinators"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Describe XA transactions"
  - "Run database 2PC"
  - "Make the coordinator reliable"
  - "Handle participant failure"
prerequisites:
  []
knowledge_refs:
  - "patterns/two-phase-commit"
---

# Two-Phase Commit in Production: XA, Databases, and Coordinators

## XA and Real Coordinators

XA is the classic 2PC standard: a transaction manager coordinates participating resource managers (databases, queues). PostgreSQL, MySQL, and Oracle implement the prepare/commit interface. Production 2PC is only as reliable as the coordinator: it must persist its decision log before sending commit, so a crashed coordinator can resume and complete the decision.

```sql
-- XA two-phase commit, PostgreSQL style
-- Phase 1: each participant prepares
xa start 'gtr1';
INSERT INTO accounts(id, balance) VALUES (1, 100);
xa end 'gtr1';
xa prepare 'gtr1';          -- vote YES (or NO on error)

xa start 'gtr1';
UPDATE accounts SET balance = balance - 50 WHERE id = 1;
xa end 'gtr1';
xa prepare 'gtr1';

-- Phase 2: coordinator decides
xa commit 'gtr1';           -- all prepared -> commit
-- or: xa rollback 'gtr1';  -- any no -> abort
-- The coordinator writes its decision to a durable log
-- BEFORE sending it, so a crash resumes the decision.
```

## The Coordinator

The coordinator is a single point of failure and the protocol's crux. Production coordinators: HA replicas, durable decision logs, and timeouts that drive recovery. Every participant must be able to ask the coordinator for the decision after a crash — the log is the source of truth.

## Practice: Operationalize 2PC

A checkout spans an orders DB and an inventory DB via XA; the coordinator must survive crashes.

**Task 1:** Design the coordinator with a durable decision log.

**Task 2:** Design participant recovery: asking the coordinator for the decision.

**Task 3:** Design the timeout policy and the stuck-transaction dashboard.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why the coordinator must log its decision before sending it.

**Prompt 2 — Implementation Design:**
> Design a 2PC coordinator service: prepare, decide, log, and recovery endpoints.

**Prompt 3 — Boundary Testing:**
> A participant is unreachable at commit time. Design the retry, the timeout, and the manual resolution.

## Key Takeaways

- XA standardizes 2PC across databases and queues
- The coordinator must log decisions durably
- Participants recover by asking the coordinator
- Timeouts and HA make the coordinator reliable

## Further Reading

- [PostgreSQL — two-phase commit](https://www.postgresql.org/docs/current/sql-prepare-transaction.html)
- [XA transactions — Wikipedia](https://en.wikipedia.org/wiki/X/Open_XA)
