---
title: "KISS in Production: Architecture Simplicity"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Question new architectural machinery"
  - "Design simple, evolvable service boundaries"
  - "Resist complexity pressure from tools and fashion"
  - "Measure complexity cost in operations"
prerequisites:
  []
knowledge_refs:
  - "principles/kiss"
---

# KISS in Production: Architecture Simplicity

## Machinery Has a Cost

Every system you add — event bus, orchestration framework, feature-flag service, observability platform — adds operational surface: deployments, upgrades, incidents, and knowledge requirements. Add machinery only when the problem outgrows the simple approach, with a concrete trigger.

```text
Complexity pressure checklist before adding machinery:
  1. What breaks today without it? (concrete failure)
  2. What is the simplest thing that fixes that?
  3. What new failures does the machinery introduce?
  4. What is the un-add trigger (when to remove it)?
If the simple answer handles it, ship the simple answer.
```

## Fewer Services, Better Boundaries

A microservice is a complexity purchase: you buy isolation and scaling, and pay in distributed-debugging, consistency, and operations. Most teams are better served by a modular monolith with clean internal boundaries until a scaling or autonomy trigger justifies splitting.

## Practice: Challenge the Architecture

A team proposes splitting a 10k-line service into 8 microservices with an event bus.

**Task 1:** Apply the checklist: what concrete failure does the split fix?

**Task 2:** Propose the simpler alternative (modular monolith) and compare operational costs.

**Task 3:** Define the trigger conditions that would justify the split later.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can articulate when microservices pay for their complexity and when they do not.

**Prompt 2 — Implementation Design:**
> Design a modular monolith with clean domain boundaries that could later split into services. What must be true of the boundaries now?

**Prompt 3 — Boundary Testing:**
> The team already runs 30 services and the tooling handles it. Does KISS still argue for fewer? What complexity remains?

## Key Takeaways

- Machinery adds operational surface every time
- Simple architecture defers complexity until a concrete trigger
- Modular monoliths beat premature microservices
- Complexity costs appear in operations, not code review

## Further Reading

- [Modular Monolith — Martin Fowler](https://martinfowler.com/bliki/ModularMonolith.html)
- [Microservices — Martin Fowler](https://martinfowler.com/articles/microservices.html)
