---
title: "Advanced Event Sourcing: Projections and Sagas"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Build projections from event streams"
  - "Orchestrate sagas with events"
  - "Handle event-driven consistency"
  - "Operate event sourcing safely"
prerequisites:
  []
knowledge_refs:
  - "patterns/event-sourcing"
---

# Advanced Event Sourcing: Projections and Sagas

## Projections as Views

Every read model is a projection over the stream: a balance, a dashboard, a search index. Projections are idempotent functions of the stream, rebuildable at any time — event sourcing makes the read side a pure derived concern.

```go
// Projection: pure function of the stream -> rebuildable views
func projectBalance(events []Event) Balance {
    var b Balance
    for _, e := range events {
        switch e.Type {
        case "deposit":  b.Amount += e.Amount
        case "withdraw": b.Amount -= e.Amount
        }
    }
    return b
}
// Same function builds the current balance or the balance at any past
// point — cut the stream at sequence N and replay.
```

## Sagas and the Danger Zone

A saga listens to events and issues commands: OrderCreated triggers the ChargeAccount command; PaymentSucceeded triggers ShipOrder. Failures produce compensating commands. The danger: saga logic distributed across many consumers becomes hard to reason about — centralize orchestration deliberately.

## Practice: Design the Saga + Projection

An order saga: create order, charge, reserve inventory, ship; the dashboard needs live totals.

**Task 1:** Design the events and the saga state machine (which event triggers which command).

**Task 2:** Design the compensation for each failure point.

**Task 3:** Build the dashboard projection and its rebuild-from-scratch path.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why sagas need idempotent commands and compensations.

**Prompt 2 — Implementation Design:**
> Design a saga as a state machine: events in, commands out, timeouts for stuck states. Where do timeouts live?

**Prompt 3 — Boundary Testing:**
> An event arrives out of order after a partition. Design the saga handling for gaps and duplicates.

## Key Takeaways

- Read models are projections — pure and rebuildable
- Sagas coordinate via events with compensations
- Orchestration centralization keeps sagas sane
- Out-of-order and duplicate events need explicit handling

## Further Reading

- [Saga — Microservices.io](https://microservices.io/patterns/data/saga.html)
- [Eventuate Tram (saga framework)](https://eventuate.io/)
