---
title: "Saga in Production: Orchestration and Choreography"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Orchestrate sagas centrally"
  - "Choreograph with events"
  - "Persist saga state"
  - "Handle partial failures"
prerequisites:
  []
knowledge_refs:
  - "patterns/saga"
---

# Saga in Production: Orchestration and Choreography

## Orchestration

An orchestrator (Temporal, Step Functions) runs the saga as a state machine: it calls each service, records the step, and runs compensations in reverse on failure. Central orchestration makes the flow visible and resumable — the orchestrator persists state, so a crash resumes the saga mid-flight.

```text
Orchestrated saga (state machine):
  [Reserve] -> [Charge] -> [Dispatch] -> Done
      |           |
      v           v
  [Release]    [Refund]        (compensations, run in reverse)

  The orchestrator stores each step's outcome; on a crash it
  resumes from the last recorded step. Compensations run
  exactly once (idempotent) in reverse order.

Choreographed saga (event chain):
  OrderCreated -> InventoryReserved -> PaymentCharged
    -> ShipmentDispatched
  Each service reacts to an event and emits the next; a failure
  emits a compensation event. No central state; the flow is
  implicit in the event log. Traceable, but harder to reason
  about and to resume after a crash.
```

## Choosing

Orchestrate when the flow is long, has many failure branches, or must be resumable. Choreograph when services must evolve independently and the happy path is linear. Hybrid: choreograph the happy path, orchestrate the compensations. The orchestration state store (a database or a workflow engine) is the saga's source of truth.

## Practice: Operationalize the Saga

A 4-step onboarding saga fails at step 3; the first two must be compensated and the flow resumed.

**Task 1:** Design the orchestrated state machine with persisted state.

**Task 2:** Design the compensation retry and the manual override.

**Task 3:** Add the dashboard: running, failed, and compensating sagas.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why orchestration makes sagas resumable and choreography makes them decoupled.

**Prompt 2 — Implementation Design:**
> Design a booking saga (hotel + flight + car) with Temporal. What are the steps, compensations, and timeouts?

**Prompt 3 — Boundary Testing:**
> The orchestrator dies mid-compensation. Design the resume that completes the unwind exactly once.

## Key Takeaways

- Orchestrators make sagas visible and resumable
- Choreography trades control for independence
- Persisted state is the saga source of truth
- Compensations must resume after crashes

## Further Reading

- [Temporal — durable workflows](https://docs.temporal.io/)
- [AWS Step Functions — saga](https://docs.aws.amazon.com/step-functions/latest/dg/sample-saga.html)
