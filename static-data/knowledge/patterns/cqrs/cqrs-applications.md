---
title: "CQRS in Production: Projections and Read Models"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design event-driven projections"
  - "Rebuild read models from scratch"
  - "Handle projection failures"
  - "Scale reads with read replicas"
prerequisites:
  []
knowledge_refs:
  - "patterns/cqrs"
---

# CQRS in Production: Projections and Read Models

## Projections

A projector consumes the write stream and builds read models. The projection is idempotent: replaying the stream reconstructs the model exactly, so a failed projector restarts from its last checkpoint and rebuilds only the gap.

```go
// Idempotent projector: replay-safe read model builder
func project(ctx context.Context, events <-chan Event) error {
    for ev := range events {
        switch e := ev.(type) {
        case OrderCreated:
            // upsert: same event replayed = same row (idempotent)
            upsertOrderSummary(ctx, e.OrderID, e.Region, e.Amount)
        case OrderPaid:
            markPaid(ctx, e.OrderID, e.PaidAt)
        }
        checkpoint(ev.Sequence)   // resume from here after a crash
    }
    return nil
}
```

## Rebuild and Lag

Read models can be rebuilt from the entire stream when the projection schema changes. Lag is monitored: a stale read model silently serves old data, so lag alerts are the CQRS equivalent of a health check.

## Practice: Design the Projection Pipeline

A reporting read model aggregates orders by region and hour.

**Task 1:** Design the projector, its checkpointing, and idempotent upserts.

**Task 2:** Design the full rebuild when the aggregation schema changes.

**Task 3:** Set the lag alert and the degraded-read response during a rebuild.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why projections must be idempotent and checkpointed. Ask me to trace a crash mid-project.

**Prompt 2 — Implementation Design:**
> Design a read model for search: orders indexed by status, region, and SKU. What is the projection and its lag budget?

**Prompt 3 — Boundary Testing:**
> The event stream has a gap from an upstream outage. Design the reconciliation that fills the gap.

## Key Takeaways

- Projections are idempotent and checkpointed
- Full rebuilds are a first-class operation
- Lag is monitored like any health metric
- Read models scale independently of writes

## Further Reading

- [Event Sourcing + CQRS — Martin Fowler](https://martinfowler.com/eaaDev/EventSourcing.html)
- [Change Data Capture (Debezium)](https://debezium.io/)
