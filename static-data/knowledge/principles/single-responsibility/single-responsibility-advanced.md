---
title: "Advanced Single Responsibility: Transactions and Bounded Contexts"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Handle cross-responsibility transactions"
  - "Design bounded contexts with clean translations"
  - "Use outboxes to keep boundaries without breaking transactions"
  - "Detect boundary rot with dependency analysis"
prerequisites:
  []
knowledge_refs:
  - "principles/single-responsibility"
---

# Advanced Single Responsibility: Transactions and Bounded Contexts

## The Transaction Trap

The strongest argument against splitting: "they share a transaction." But a single database transaction spanning two responsibilities is a coupling — the fix is the transactional outbox: each responsibility owns its writes, and the event that needs the other side is published atomically with its own write.

```text
Keeping boundaries with a transaction:
  checkout creates order + publishes order.created
  -> one transaction, outbox table, relay publishes
  billing consumes order.created -> owns its ledger (separate tx)
  inventory consumes order.created -> owns its stock (separate tx)
No distributed transaction; each responsibility keeps its boundary.
Saga/compensation handles multi-step failures.
```

## Bounded Contexts

DDD bounded contexts give each responsibility its own model and language: "customer" in sales differs from "customer" in support. The boundary includes a translation layer (anti-corruption layer) so neither model leaks into the other.

## Practice: Redesign the Shared Transaction

Order creation writes orders + decrements inventory + charges payment in one transaction.

**Task 1:** Identify the responsibilities entangled by the transaction.

**Task 2:** Redesign with outbox + consumers, keeping atomicity per responsibility.

**Task 3:** Design the compensation (saga) for the failure order: charge ok, stock failed.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why a shared transaction is a boundary violation even when it works.

**Prompt 2 — Implementation Design:**
> Design the anti-corruption layer between sales "customer" and support "customer" models.

**Prompt 3 — Boundary Testing:**
> A saga step is not idempotent. Design the idempotency guard that keeps the saga safe.

## Key Takeaways

- Shared transactions are the boundary-violation trap
- Outbox + consumers keep atomicity per responsibility
- Bounded contexts need translation layers
- Sagas need idempotent steps

## Further Reading

- [Bounded Context — Martin Fowler](https://martinfowler.com/bliki/BoundedContext.html)
- [Saga Pattern — Microservices.io](https://microservices.io/patterns/data/saga.html)
