---
title: "Single Responsibility in Production: Services and Modules"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design responsibility boundaries for services"
  - "Align module ownership with change actors"
  - "Prevent responsibility creep"
  - "Balance granularity with operational cost"
prerequisites:
  []
knowledge_refs:
  - "principles/single-responsibility"
---

# Single Responsibility in Production: Services and Modules

## Service Responsibility

A microservice is a single responsibility with an owner: the payments service owns payment state, the identity service owns identity. The boundary is drawn where the reason to change diverges — two teams changing one service for different reasons is the service-level SRP violation.

```text
Service responsibility test:
  - Who changes this service? (one team/actor = good)
  - Why do they change it? (one reason family = good)
  - Does another actor's change block this service's deploy?
If two actors must coordinate on every change, the service
has two responsibilities: split the boundary.
```

## Responsibility Creep

Services accumulate jobs over time ("it is easy to add here"). Responsibility creep shows up as a service that owns data it does not produce, sends emails it has no business sending, and blocks on concerns outside its domain. Regular ownership audits prune the creep.

## Practice: Audit the Services

A "user service" now handles auth, profiles, billing addresses, and marketing consent.

**Task 1:** List the responsibilities and their change actors.

**Task 2:** Propose the boundary split (identity vs billing vs marketing) and what moves.

**Task 3:** Decide whether to split now or extract modules first, with the triggers for each.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why service boundaries should follow change actors, not data ownership alone.

**Prompt 2 — Implementation Design:**
> Design the extraction of billing from a user service: data migration, event contract, and deploy order.

**Prompt 3 — Boundary Testing:**
> Two responsibilities genuinely share a transaction (profile + billing in one checkout). Design the boundary that respects the transaction.

## Key Takeaways

- Service boundaries follow change actors
- Two actors coordinating on every change = split
- Responsibility creep is a creeping tax
- Extract in steps, not big-bang splits

## Further Reading

- [Microservices Boundaries — Martin Fowler](https://martinfowler.com/articles/microservices.html)
- [DDD Bounded Contexts](https://martinfowler.com/bliki/BoundedContext.html)
