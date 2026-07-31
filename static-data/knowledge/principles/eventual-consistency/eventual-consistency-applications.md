---
title: "Eventual Consistency in Production: Replication and Read Models"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design async replication pipelines"
  - "Use outbox patterns for reliable propagation"
  - "Build read models and search indexes from events"
  - "Monitor replication lag as a first-class metric"
prerequisites:
  []
knowledge_refs:
  - "principles/eventual-consistency"
---

# Eventual Consistency in Production: Replication and Read Models

## The Outbox Pattern

Reliable propagation is the hard part: if you publish the event before committing the write, you may publish events for writes that roll back; if after, you may lose events on crash. The transactional outbox stores the event in the same transaction as the write, and a relay publishes it — exactly once.

```sql
-- Transactional outbox: event written with the business data
BEGIN;
INSERT INTO orders (...) VALUES (...);
INSERT INTO outbox (id, aggregate, payload, published)
VALUES (gen_random_uuid(), 'order.created', '{"orderId": 123}', false);
COMMIT;
-- Relay (idempotent):
UPDATE outbox SET published = true
WHERE id = $1 AND published = false;   -- exactly-once guard
```

## Read Models and Search Indexes

Search indexes and analytics warehouses are naturally eventual: they consume events and project them into optimized shapes. The key discipline is that reads served from them are understood to be slightly behind the source of truth, and the product communicates or tolerates that.

Monitor replication lag and index lag with dashboards and alerts — eventual consistency without visibility is how stale data becomes a silent production bug.

## Practice: Build a Reliable Sync Pipeline

Orders must appear in a search index within ~5 seconds. The current pipeline publishes events after commit and loses them on crash.

**Task 1:** Adopt the outbox pattern and describe the crash scenarios it fixes.

**Task 2:** Design the indexer: consume, dedupe, retry, and handle out-of-order events.

**Task 3:** Define the lag alert (e.g., >30s index lag pages) and the replay workflow.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why the outbox must be in the same transaction as the business write. Ask me to trace the two failure orders.

**Prompt 2 — Implementation Design:**
> Design a search index that must never show deleted orders. How do tombstones propagate through the pipeline?

**Prompt 3 — Boundary Testing:**
> The relay publishes a duplicate event after a retry. Design idempotent consumption (dedupe key) end-to-end.

## Key Takeaways

- Outbox pattern gives reliable, at-least-once propagation
- Consumers must be idempotent to survive retries
- Search/analytics are naturally eventual read models
- Lag is a first-class metric with alerts and replays

## Further Reading

- [Transactional Outbox — Microservices.io](https://microservices.io/patterns/data/transactional-outbox.html)
- [Change Data Capture (Debezium)](https://debezium.io/)
