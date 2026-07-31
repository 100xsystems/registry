---
title: "Advanced CQS: CQRS and Event Sourcing"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Design a CQRS system with separate read and write models"
  - "Explain when event sourcing complements CQRS"
  - "Manage read-model consistency (eventual vs synchronous)"
  - "Avoid CQRS complexity where it is not needed"
prerequisites:
  []
knowledge_refs:
  - "principles/cqs"
---

# Advanced CQS: CQRS and Event Sourcing

## CQRS: Separate Models

CQRS gives commands and queries different models, storage, and scaling. Writes go to the transactional write model; reads are served by optimized read models (denormalized projections) built from the write stream.

The cost: eventual consistency between write and read models, plus the machinery to project and rebuild them. Use it when read and write shapes diverge sharply or reads dominate.

```text
CQRS topology:
  Command side:  POST /orders -> write model (normalized, transactional)
  Event stream:  order.created, order.paid, order.shipped
  Projection:    builds read model (denormalized order summaries)
  Query side:    GET /orders?status=paid -> read model (fast, shaped)
Consistency: eventual between stream and projection.
```

## Event Sourcing

Event sourcing stores every state change as an event (append-only) and derives current state by replay. It gives perfect audit history and makes projections trivial — at the cost of complexity, eventual read models, and schema evolution of the event stream.

CQRS + event sourcing is powerful but is a heavy tool: most systems need only the service-level CQS split, not the full architecture.

## Practice: Design a Projection

An orders service: writes are normalized; the dashboard needs aggregated daily revenue by region.

**Task 1:** Define the events and the projection that builds the daily-revenue read model.

**Task 2:** Handle projection lag: what does the dashboard show during a replay?

**Task 3:** Design rebuild-from-scratch for the read model after a bug in the projection.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can articulate the difference between CQS (method-level) and CQRS (architecture-level) and when each applies.

**Prompt 2 — Implementation Design:**
> Design an event-sourced cart with projections for cart view, analytics, and recommendations. How do you version the events?

**Prompt 3 — Boundary Testing:**
> The read model lags and a user sees a stale order status. Design a per-user read-your-writes projection or a sync boundary.

## Key Takeaways

- CQRS separates read and write models end-to-end
- Event sourcing makes projections and audit trails natural
- Read models are eventually consistent with the write stream
- CQRS+ES is heavy — apply it only where shapes diverge

## Further Reading

- [CQRS — Martin Fowler](https://martinfowler.com/bliki/CQRS.html)
- [Event Sourcing — Microsoft Docs](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)
