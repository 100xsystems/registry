---
title: "Idempotency in Production: Keys, Stores, and Lifecycles"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design an idempotency-key store"
  - "Handle concurrent requests with the same key"
  - "Set key retention and cleanup policies"
  - "Build idempotent event consumers"
prerequisites:
  []
knowledge_refs:
  - "principles/idempotency"
---

# Idempotency in Production: Keys, Stores, and Lifecycles

## The Key Store

The idempotency store maps key → response (or status). A request with a seen key returns the stored response; a new key records the in-flight operation. Concurrency: two simultaneous requests with the same key must resolve to one execution — the store's unique constraint on the key is the lock.

```sql
-- Idempotency store: key unique, status tracks lifecycle
CREATE TABLE idempotency (
    key        text PRIMARY KEY,
    status     text NOT NULL,              -- in_progress | done | failed
    request    jsonb,
    response   jsonb,
    created_at timestamptz DEFAULT now()
);
-- Concurrent same-key: INSERT ... ON CONFLICT (key) DO NOTHING
INSERT INTO idempotency (key, status, request)
VALUES ($1, 'in_progress', $2)
ON CONFLICT (key) DO NOTHING
RETURNING status;   -- empty = another request already owns this key
```

## Idempotent Consumers

Event consumers see at-least-once delivery: the same event can arrive twice. Dedupe by event ID (store seen IDs, skip repeats) or process idempotently (upserts, set semantics). Both make replay and retry safe — which every pipeline eventually needs.

## Practice: Design the Key Lifecycle

A payment endpoint must be idempotent, and keys can be reused after 24 hours.

**Task 1:** Design the store schema, the concurrency resolution, and the 24h retention cleanup.

**Task 2:** Define behavior: same key + same request → stored response; same key + different request → 409.

**Task 3:** Design the event consumer dedupe and the replay workflow.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why the idempotency check and the business action must be atomic (same transaction).

**Prompt 2 — Implementation Design:**
> Design an idempotent refund API: two refund requests for the same charge must produce one refund. What key, what store, what conflict behavior?

**Prompt 3 — Boundary Testing:**
> The idempotency store itself fails. Design the degraded path that still prevents double charges (or makes them detectable).

## Key Takeaways

- The key store's unique constraint resolves concurrency
- Key + request must be checked atomically with the action
- Retention policies bound the store
- Event dedupe makes replay safe

## Further Reading

- [Idempotent Consumers — Microservices.io](https://microservices.io/patterns/communication-style/idempotent-consumer.html)
- [Stripe Idempotent Requests](https://stripe.com/docs/api/idempotent_requests)
