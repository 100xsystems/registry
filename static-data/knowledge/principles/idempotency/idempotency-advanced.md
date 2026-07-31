---
title: "Advanced Idempotency: Distributed and CRDT Approaches"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Propagate idempotency keys across service boundaries"
  - "Use idempotent operations (upserts, CRDTs) by design"
  - "Handle exactly-once claims honestly"
  - "Design reconciliation for missed dedupes"
prerequisites:
  []
knowledge_refs:
  - "principles/idempotency"
---

# Advanced Idempotency: Distributed and CRDT Approaches

## Cross-Service Idempotency

An order flows through gateway → orders → payments → ledger. The original idempotency key must flow with the logical operation so each hop can dedupe against its own store — a duplicate at the gateway must not become a second payment further down.

```text
Propagate the key end-to-end:
  POST /orders  (Idempotency-Key: K)
    -> orders service stores K, emits event {key: K, ...}
    -> payments service stores K for the charge
    -> ledger service stores K for the entry
Retry at any hop reuses K; each hop dedupes independently.
Exactly-once is really: at-least-once delivery + idempotent processing.
```

## Idempotent by Construction

Some operations are naturally idempotent: upserts (same data written twice = one row), set adds, max/overwrite semantics, CRDT merges. Design data models around these operations and much of the retry problem disappears.

## Practice: Propagate the Key

A checkout spans orders, payments, and inventory services. Payment retries are double-charging.

**Task 1:** Trace the key from the client request through all three services and their events.

**Task 2:** Design each hop's dedupe store and the conflict rule (same key, different payload → 409).

**Task 3:** Design a nightly reconciliation that finds and fixes any double charge missed by dedupe.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why "exactly-once" is usually marketing for at-least-once plus idempotency. Ask me to prove it with a crash scenario.

**Prompt 2 — Implementation Design:**
> Design a distributed file sync where uploads are idempotent by content hash. How do concurrent identical uploads converge?

**Prompt 3 — Boundary Testing:**
> A key expires from the store but the client still retries. Design the backstop that prevents a duplicate payment after expiry.

## Key Takeaways

- Keys must propagate end-to-end with the operation
- At-least-once + idempotency approximates exactly-once
- Upserts and CRDTs are idempotent by construction
- Reconciliation catches what dedupe misses

## Further Reading

- [Exactly-Once Semantics — Kafka](https://kafka.apache.org/documentation/#semantics)
- [Transactional Outbox + Idempotency](https://microservices.io/patterns/data/transactional-outbox.html)
