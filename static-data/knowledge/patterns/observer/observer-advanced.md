---
title: "Advanced Observer: Event Sourcing as Observer"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Explain event sourcing"
  - "Build projections as observers"
  - "Replay events"
  - "Handle schema evolution"
prerequisites:
  - "patterns/event-sourcing"
  - "patterns/cqrs"
knowledge_refs:
  - "patterns/observer"
---

# Advanced Observer: Event Sourcing as Observer

## Events as Truth

Event sourcing stores facts — every state change as an event — instead of current state. Observers (projections) subscribe to the event stream and maintain read models: a report view, a search index, an email trigger. The same stream feeds every observer, and any projection can be rebuilt by replaying events.

```python
# Event sourcing: events are the source of truth
# Aggregate: apply(Event) -> state
class Account:
    def __init__(self):
        self.balance = 0
    def apply(self, event):
        if event.type == 'DEPOSITED': self.balance += event.amount
        if event.type == 'WITHDRAWN': self.balance -= event.amount

# Projection (observer): maintains a read model from the stream
class BalanceProjection:
    def __init__(self):
        self.accounts = {}
    def on(self, event):
        a = self.accounts.setdefault(event.account_id, Account())
        a.apply(event)
# Rebuild = replay the event log from the start.
# Every observer consumes the same immutable stream.
```

## Rebuilds and Evolution

A projection is rebuildable: drop and replay. That is the power — a buggy projection fixes itself by replaying. Schema evolution is the cost: old events must stay readable, so events are versioned and upgrades translate old shapes. Event stores are append-only; immutable history is the contract.

## Practice: Build the Projection

An order system publishes OrderPlaced, PaymentReceived, OrderShipped; three projections must stay in sync.

**Task 1:** Define the event stream and the aggregate applies.

**Task 2:** Build the three projections as observers.

**Task 3:** Simulate a projection bug, drop it, and rebuild from the log.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why replaying events can rebuild any projection.

**Prompt 2 — Implementation Design:**
> Design the event schema for a cart: add, remove, checkout. How does a projection compute the current cart, and how is a v2 event handled?

**Prompt 3 — Boundary Testing:**
> A projection lags behind the stream and events age out. Design the snapshot + replay strategy for large histories.

## Key Takeaways

- Event sourcing stores facts; projections observe them
- Rebuild any projection by replaying the log
- Events must stay readable across schema changes
- The event store is append-only truth

## Further Reading

- [Event Sourcing — Martin Fowler](https://martinfowler.com/eaaDev/EventSourcing.html)
- [Eventuate — event sourcing platform](https://eventuate.io/)
