---
title: "Advanced Mediator: Choreography vs Orchestration"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Contrast orchestration and choreography"
  - "Design event choreography"
  - "Handle compensation without a hub"
  - "Choose the coordination model"
prerequisites:
  []
knowledge_refs:
  - "patterns/mediator"
---

# Advanced Mediator: Choreography vs Orchestration

## The Trade-Off

Choreography drops the hub: each service reacts to events and emits its own, passing control along. It removes the single point of failure and keeps services fully independent, but the flow is implicit — harder to trace, test, and reason about. Orchestration is explicit and recoverable but concentrates coordination.

```text
Orchestration vs choreography:
  Orchestration (central hub):
    + explicit flow, easy to trace, retry, and compensate
    - hub is a dependency and a bottleneck
    Example: Temporal workflow coordinates order -> payment -> ship
  Choreography (event chain):
    + services fully independent, no hub to fail
    - flow is implicit; tracing needs an event store
    Example: OrderPlaced -> InventoryReserved -> PaymentCharged
      -> ShipmentDispatched, each step reacts and emits
  Hybrid: choreograph the happy path, orchestrate the failures.
```

## Choosing the Model

Pick orchestration when the flow is long, has complex error handling, or must be resumable. Pick choreography when services must evolve independently and the happy path is linear. Compensation in choreography spreads across services — each emits a compensating event — and tracing requires an event log.

## Practice: Choose the Coordination

A signup flow: validate, create account, send email, provision workspace — with retries on each step.

**Task 1:** Design the orchestrated version with a state machine.

**Task 2:** Design the choreographed version as an event chain.

**Task 3:** Compare failure handling and choose one, justifying the retry story.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why choreography makes flows implicit and tracing harder.

**Prompt 2 — Implementation Design:**
> Design a hybrid: choreographed happy path, orchestrated compensations. Where does the compensation hub live?

**Prompt 3 — Boundary Testing:**
> An event is lost in choreography. Design the outbox pattern or the reconciliation that makes the chain reliable.

## Key Takeaways

- Orchestration is explicit and recoverable
- Choreography is decoupled but implicit
- Flows with complex errors favor the hub
- Hybrids choreograph happy paths, orchestrate failures

## Further Reading

- [Saga pattern — microservices.io](https://microservices.io/patterns/data/saga.html)
- [Temporal — durable workflows](https://docs.temporal.io/)
