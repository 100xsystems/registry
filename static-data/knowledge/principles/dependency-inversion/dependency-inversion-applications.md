---
title: "Dependency Inversion in Production: Ports and Adapters"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Structure a service with ports and adapters"
  - "Keep the domain free of framework imports"
  - "Use inversion for test doubles without mocks"
  - "Manage the wiring layer (composition root)"
prerequisites:
  []
knowledge_refs:
  - "principles/dependency-inversion"
---

# Dependency Inversion in Production: Ports and Adapters

## Ports and Adapters (Hexagonal)

Hexagonal architecture draws the application core as a hexagon: inbound ports (driven by UI/API) and outbound ports (driving database/queue/email). Adapters implement the ports at the edges. The domain core knows nothing about HTTP, SQL, or Kafka.

```text
Hexagonal (ports & adapters):
  [HTTP adapter] -> [inbound port] -> [DOMAIN CORE] -> [outbound port] -> [Postgres adapter]
                                   -> [outbound port] -> [Kafka adapter]
The domain core imports only ports + domain types.
Test: swap adapters for in-memory fakes with zero domain changes.
```

## Composition Root

The composition root is the single place where concrete adapters are chosen and wired. It lives at the application edge (main, startup config), never inside the domain. This concentrates the "what implementation today" decision in one file.

Inversion makes the domain testable with lightweight fakes: a fake repository implements the same port the real one does, so tests exercise the domain with no mocks, no databases, and no network.

## Practice: Hexagonalize a Service

A checkout service calls an HTTP payments API and writes to Postgres directly from the order logic.

**Task 1:** Define the outbound ports: PaymentProvider, OrderStore.

**Task 2:** Move HTTP and SQL calls into adapters; keep the order logic framework-free.

**Task 3:** Write a domain test using in-memory fakes for both ports. Note what it proves that a mock-based test cannot.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why the composition root must be outside the domain and what breaks if it is not.

**Prompt 2 — Implementation Design:**
> Design the ports for a notification system with email, push, and SMS providers, including retry and dead-letter semantics. Where does retry live — port or adapter?

**Prompt 3 — Boundary Testing:**
> A new persistence requirement (e.g., sharding) changes the data model. How does hexagonal structure contain the blast radius?

## Key Takeaways

- Ports and adapters keep infrastructure at the edges
- The domain core imports only ports and types
- The composition root concentrates wiring decisions
- Fakes beat mocks for testing the domain

## Further Reading

- [Hexagonal Architecture — Alistair Cockburn](https://alistair.cockburn.us/hexagonal-architecture/)
- [Ports & Adapters — Martin Fowler](https://martinfowler.com/articles/hexagonal-architecture-demo.html)
