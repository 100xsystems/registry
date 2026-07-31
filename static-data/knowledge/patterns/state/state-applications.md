---
title: "State in Production: Workflows and State Machines"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design state machines"
  - "Use state machine libraries"
  - "Persist state"
  - "Validate transitions"
prerequisites:
  []
knowledge_refs:
  - "patterns/state"
---

# State in Production: Workflows and State Machines

## State Machines

Production state machines centralize states, events, transitions, and guards in one declarative table — XState, Spring Statemachine, or a hand-rolled table. The table is data: auditable, testable, and documented. The state pattern classes are the OO view; the table is the operational view — same model.

```typescript
// XState: a declarative state machine
import { createMachine, interpret } from 'xstate';

const orderMachine = createMachine({
  id: 'order',
  initial: 'draft',
  states: {
    draft:     { on: { SUBMIT: 'submitted' } },
    submitted: { on: { PAY: 'paid', CANCEL: 'cancelled' } },
    paid:      { on: { SHIP: 'shipped' } },
    shipped:   { on: { DELIVER: 'delivered' } },
    cancelled: { type: 'final' },
    delivered: { type: 'final' },
  },
});
const service = interpret(orderMachine).start();
service.send({ type: 'SUBMIT' });   // draft -> submitted
service.send({ type: 'PAY' });
// Guards (e.g., only paid orders ship) attach to transitions.
// The machine is data: it can be persisted, restored, and tested
// by walking its transition table.
```

## Persistence

Long-lived workflows persist the current state — the state value in a database — so a crash resumes where it stopped. The machine is deterministic: same state + same event = same transition, so restoring the state restores the behavior. Auditing records every transition.

## Practice: Automate the Lifecycle

A support ticket moves new -> triaged -> in_progress -> resolved -> closed, with SLA guards.

**Task 1:** Define the machine: states, events, transitions, guards.

**Task 2:** Implement it with a state machine library.

**Task 3:** Persist the state and design the resume and audit trail.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why a declarative machine is easier to audit and test than scattered if-chains.

**Prompt 2 — Implementation Design:**
> Design a state machine for a refund flow: request, review, approve/reject, issued. What are the guards?

**Prompt 3 — Boundary Testing:**
> A persisted state becomes invalid after a deploy. Design the migration and the validation that rejects it.

## Key Takeaways

- State machines centralize states, events, and guards
- The table is auditable, testable, and documented
- Persistence makes workflows resumable
- Determinism makes the machine testable

## Further Reading

- [XState — state machines](https://stately.ai/docs)
- [Spring Statemachine](https://projects.spring.io/spring-statemachine/)
