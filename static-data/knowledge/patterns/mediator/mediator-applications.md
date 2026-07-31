---
title: "Mediator in Production: Event Buses and Orchestrators"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design an event bus mediator"
  - "Orchestrate workflows centrally"
  - "Coordinate transactions"
  - "Avoid mediator bloat"
prerequisites:
  []
knowledge_refs:
  - "patterns/mediator"
---

# Mediator in Production: Event Buses and Orchestrators

## The Event Bus

An in-process event bus (or a message broker) is a mediator: producers publish, the bus routes to subscribers, and no producer knows its consumers. The bus centralizes routing, ordering, and fan-out policy. The risk is the mediator becoming a god object — every rule flowing through one hub.

```go
// Event bus as mediator: publishers and subscribers never meet
type Bus struct {
    subs map[string][]func(Event)
}
func (b *Bus) Publish(topic string, e Event) {
    for _, h := range b.subs[topic] { h(e) }   // hub routes to handlers
}
func (b *Bus) Subscribe(topic string, h func(Event)) {
    b.subs[topic] = append(b.subs[topic], h)
}
// Order service publishes OrderPlaced; inventory and billing
// subscribe. Neither service imports the other — the bus mediates.
```

## Orchestration

A workflow orchestrator (Temporal, Step Functions) is a mediator for services: it decides the sequence, retries, and compensations. A transaction coordinator mediates distributed commits. The pattern scales up from dialogs to distributed systems — one hub, clear rules, decoupled participants.

## Practice: Orchestrate the Order Flow

Order placement touches inventory, payment, and shipping; failures need compensating actions.

**Task 1:** Design the orchestrator state machine and its events.

**Task 2:** Wire the services to the bus without any service importing another.

**Task 3:** Add the compensation flow for a payment failure mid-order.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why an orchestrator is a mediator and how it stays decoupled from the services it coordinates.

**Prompt 2 — Implementation Design:**
> Design a saga orchestrator: the hub, the per-step handlers, and the compensation table. Where does retry live?

**Prompt 3 — Boundary Testing:**
> The bus itself fails. Design the durable queue or the retry contract that keeps the workflow alive.

## Key Takeaways

- Event buses mediate between producers and consumers
- Orchestrators mediate across services
- The hub must not become a god object
- Durability of the hub is a first-class concern

## Further Reading

- [Temporal — durable workflows](https://docs.temporal.io/)
- [Mediator — Refactoring Guru](https://refactoring.guru/design-patterns/mediator)
