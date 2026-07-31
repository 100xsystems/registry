---
title: "Advanced Separation of Concerns: Events and Domains"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Decouple concerns with events"
  - "Design domain-event boundaries"
  - "Isolate concerns across services"
  - "Avoid event-driven entanglement"
prerequisites:
  []
knowledge_refs:
  - "principles/separation-of-concerns"
---

# Advanced Separation of Concerns: Events and Domains

## Events as Decoupling

Events let one concern (orders) announce facts without knowing who cares (inventory, email, analytics). Each consumer handles its concern independently — new consumers attach without changing the producer. This is separation of concerns across service boundaries.

```text
Event-driven concern separation:
  orders service publishes: order.created, order.paid
  inventory service consumes: order.created  (stock concern)
  email service consumes:     order.paid     (notification concern)
  analytics consumes:         order.*        (metrics concern)

Producer knows nothing about consumers. Adding a concern =
adding a consumer, not editing the producer.
```

## The Trap: Event Entanglement

Events decouple producers from consumers but can couple consumers to each other if they share state or ordering expectations. The discipline: each consumer owns its concern and its read model; cross-consumer ordering assumptions are a hidden coupling.

## Practice: Design the Event Boundaries

A checkout publishes order.* events; three teams consume for inventory, email, and fraud.

**Task 1:** Define the events and their payloads (stable, additive).

**Task 2:** Verify no consumer depends on another consumer's processing order.

**Task 3:** Design the consumer error policy: one consumer failing must not block the others.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain how events separate concerns without coupling consumers to the producer.

**Prompt 2 — Implementation Design:**
> Design an outbox + event bus for a monolith splitting into services. Which concerns move to consumers first?

**Prompt 3 — Boundary Testing:**
> Two consumers both update the same denormalized table — a shared concern. Design the ownership rule that prevents conflicts.

## Key Takeaways

- Events let concerns attach without producer changes
- Each consumer owns its concern and its read model
- Cross-consumer ordering assumptions are hidden coupling
- Consumer failure isolation is part of the design

## Further Reading

- [Domain Events — Martin Fowler](https://martinfowler.com/eaaDev/DomainEvent.html)
- [Event-Driven Architecture — AWS](https://aws.amazon.com/event-driven-architecture/)
