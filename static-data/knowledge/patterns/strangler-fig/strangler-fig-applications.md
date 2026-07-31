---
title: "Strangler Fig in Production: APIs and Databases"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Strangle APIs incrementally"
  - "Migrate databases safely"
  - "Use dual writes and backfill"
  - "Manage the coexistence window"
prerequisites:
  []
knowledge_refs:
  - "patterns/strangler-fig"
---

# Strangler Fig in Production: APIs and Databases

## API Strangling

A gateway fronts both systems; routes move endpoint by endpoint. The new service implements the same contract, the gateway flips one route, and observability compares behavior. Coexistence: both systems run, sharing the database or not — the dual-write and backfill pattern migrates data while both write.

```text
API strangling sequence:
  - gateway routes /v1/invoices -> legacy, /v1/orders -> new
  - each endpoint flips independently with a rollback
  - contract tests run against both sides during coexistence
Database migration (dual-write):
  - new schema added alongside the old
  - every write goes to both; a backfill copies history
  - reads move over when the new side is verified
  - the old column/table is dropped only after a grace window
  - change data capture (CDC) keeps both sides in sync
  The coexistence window is where incidents happen: plan the
  data sync, the rollback, and the cutover drill.
```

## Order of Operations

Read-only features migrate first (lowest risk), then read-write, then writes with data migration. The database is usually the last strangler target — it is the hardest to dual-run. The monolith shrinks as modules move out; the gateway grows as the routing map fills.

## Practice: Strangle the Checkout

A checkout API and its orders table must move out of the monolith to a new service.

**Task 1:** Design the gateway routes and the migration order (reads first).

**Task 2:** Design the dual-write, backfill, and cutover for orders.

**Task 3:** Design the rollback: what happens if cutover fails at 90% traffic?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why read-only features migrate first and the database migrates last.

**Prompt 2 — Implementation Design:**
> Design a dual-write migration for a users table: the new table, the sync, the verify, and the drop schedule.

**Prompt 3 — Boundary Testing:**
> Dual writes diverge and the new table is missing a row. Design the CDC catch-up and the verification that finds it.

## Key Takeaways

- Gateways route endpoint by endpoint
- Databases migrate with dual writes and backfill
- Reads move before writes
- The coexistence window needs a cutover drill

## Further Reading

- [Strangler Fig Application — Fowler](https://martinfowler.com/bliki/StranglerFigApplication.html)
- [Branch by abstraction](https://martinfowler.com/bliki/BranchByAbstraction.html)
