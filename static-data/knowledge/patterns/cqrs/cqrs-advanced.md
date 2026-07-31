---
title: "Advanced CQRS: Event Sourcing and Sagas"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Combine CQRS with event sourcing"
  - "Orchestrate sagas across command sides"
  - "Manage schema evolution of events"
  - "Choose CQRS complexity deliberately"
prerequisites:
  []
knowledge_refs:
  - "patterns/cqrs"
---

# Advanced CQRS: Event Sourcing and Sagas

## Event-Sourced Write Model

The command side can be event-sourced: every command produces an event appended to the log, and aggregate state is derived by replay. The events ARE the write model — perfect audit, easy projections, no lost updates.

```text
Event-sourced command side:
  Command: PlaceOrder{id, items, region}
  -> validates against derived state
  -> appends OrderCreated{id, items, region}   (the only truth)
  -> state = fold(replay(events))
  Query side: projections consume the same events.

Sagas: each step is a command on its own aggregate;
failures emit compensating commands.
```

## The Cost-Benefit

CQRS + event sourcing is powerful and heavy: event versioning, replay infrastructure, projection management, and eventual consistency everywhere. The discipline: start with a plain repository; adopt CQRS when read/write divergence or scaling demands it; adopt event sourcing when the audit/rebuild story is worth the machinery.

## Practice: Design the Saga + Projection

An order saga spans orders, payments, and inventory; the dashboard needs aggregates.

**Task 1:** Design the saga: commands per aggregate and compensating commands on failure.

**Task 2:** Design the projection that builds dashboard aggregates from saga events.

**Task 3:** Version the events so a schema change replays cleanly.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can articulate when event sourcing earns its cost and when it is ceremony.

**Prompt 2 — Implementation Design:**
> Design a saga with compensating commands for a payment flow. What happens at each failure point?

**Prompt 3 — Boundary Testing:**
> A projection and a saga consume the same event and both fail. Design the isolation so one does not block the other.

## Key Takeaways

- Events are the write model; state is derived
- Sagas coordinate commands with compensations
- Event versioning keeps replays faithful
- Adopt the machinery on demonstrated need

## Further Reading

- [Event Sourcing — Microsoft Docs](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)
- [Saga — Microservices.io](https://microservices.io/patterns/data/saga.html)
