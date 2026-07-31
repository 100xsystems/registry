---
title: "Advanced SOLID: DDD and System Design"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Apply SOLID thinking to domain models"
  - "Map SOLID to bounded contexts"
  - "Design system boundaries with SOLID analogies"
  - "Keep architecture honest with tests"
prerequisites:
  []
knowledge_refs:
  - "principles/solid"
---

# Advanced SOLID: DDD and System Design

## SOLID at the System Scale

Every SOLID principle has a system-level twin: SRP becomes "one bounded context per service", OCP becomes "add consumers, do not edit producers", LSP becomes "implementations honor the interface contract", ISP becomes "consumer-specific read models", DIP becomes "the domain does not import infrastructure".

```text
SOLID mapped to architecture:
  S -> bounded contexts / service ownership
  O -> event consumers attach, producers unchanged
  L -> contract-tested implementations
  I -> consumer-specific DTOs and read models
  D -> domain imports ports, not frameworks

A system designed this way changes by adding, not rewriting.
```

## Enforcing the Architecture

Architecture-level SOLID decays without enforcement: dependency tests, contract tests, and consumer-contract tests keep the boundaries honest. The same "test the invariants" discipline that guards a class guards a service.

## Practice: Map SOLID to Your System

Your platform has 12 services; one service owns payments, identity, and email.

**Task 1:** Map each principle to a concrete violation or strength in the platform.

**Task 2:** Design the boundary split for the multi-owner service.

**Task 3:** Add the architecture tests that would have caught the violation.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can articulate how SOLID principles scale from a class to a bounded context.

**Prompt 2 — Implementation Design:**
> Design a platform where adding a new notification channel is purely additive (OCP at the system level). What moves, what never changes?

**Prompt 3 — Boundary Testing:**
> A consumer contract changes and three services break. Design the contract test + consumer-version matrix that predicts the blast radius.

## Key Takeaways

- SOLID scales from classes to bounded contexts
- Additive change is the system-level payoff
- Architecture tests keep boundaries honest
- Contract tests predict cross-service blast radius

## Further Reading

- [Clean Architecture — Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Pact — Consumer-Driven Contracts](https://docs.pact.io/)
