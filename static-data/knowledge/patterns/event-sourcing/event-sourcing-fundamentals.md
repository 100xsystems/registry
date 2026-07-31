---
title: "Event Sourcing: The Log Is the Truth"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain event sourcing"
  - "Derive state by replaying events"
  - "List the audit and rebuild benefits"
  - "Understand the costs"
prerequisites:
  - "principles/cqs"
  - "patterns/cqrs"
knowledge_refs:
  - "patterns/event-sourcing"
---

# Event Sourcing: The Log Is the Truth

## The Idea

Instead of storing the current state, store every event that changed it: OrderCreated, OrderPaid, OrderShipped. Current state is derived by replaying events. The event log is the only source of truth — it cannot be lost and it records exactly what happened.

```python
# Event sourcing: state = fold over events
def apply(state, event):
    if event.type == 'created':   return {**state, 'id': event.id, 'status': 'created'}
    if event.type == 'paid':      return {**state, 'status': 'paid', 'paid_at': event.at}
    if event.type == 'shipped':   return {**state, 'status': 'shipped'}
    return state

def rebuild(events):
    state = {}
    for e in sorted(events, key=lambda x: x.sequence):
        state = apply(state, e)
    return state

# Audit: every change is in the log. Rebuild: replay from scratch.
```

## Benefits and Costs

Benefits: perfect audit trail, full history, rebuildable state, projections for any view, and no lost updates (concurrent writes append). Costs: replay infrastructure, event versioning, eventual projections, and a learning curve.

## Practice: Model the Ledger

A bank account: deposit, withdraw, and freeze events.

**Task 1:** Define the events and the apply() fold.

**Task 2:** Rebuild the balance from a 1,000-event log and verify.

**Task 3:** Show the audit answer: "what happened to this account, in order?"

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why the event log beats stored state for audit. Start with what "what happened" requires.

**Prompt 2 — Compare & Contrast:**
> Compare event sourcing with a plain update-in-place store and with command sourcing.

**Prompt 3 — Boundary Testing:**
> A buggy old event is replayed after a rule change. Design the versioning that keeps replays faithful.

## Key Takeaways

- The event log is the source of truth
- State is derived by replay
- Audit and rebuild come free
- Versioning and snapshots manage the costs

## Further Reading

- [Event Sourcing — Martin Fowler](https://martinfowler.com/eaaDev/EventSourcing.html)
- [Event Sourcing — Microsoft Docs](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)
