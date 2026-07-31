---
title: "Advanced Facade: Bounded Facades and Fragile Foundations"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Design multiple facades per audience"
  - "Balance hiding with capability"
  - "Keep facades thin and honest"
  - "Evolve facades safely"
prerequisites:
  []
knowledge_refs:
  - "patterns/facade"
---

# Advanced Facade: Bounded Facades and Fragile Foundations

## Facades per Audience

Different callers need different simplifications of the same subsystem: an admin facade (reconfigure, inspect), an operator facade (metrics, drain), and a user facade (use). Each facade is a role-shaped door — the interface segregation principle applied to facades.

```text
Facades per audience over one engine:
  UserFacade:     start, pause, stop            (the product)
  OperatorFacade: status, drain, metrics        (the SRE)
  AdminFacade:    configure, migrate, snapshot  (the admin)
Each facade is thin: it delegates to the engine, never re-implements.
Thin facades stay honest; thick ones become new subsystems.
```

## The Fragile Foundation

A facade that hides error modes can become a fragile foundation: callers never see failures until they burst through. Facades should return explicit result types, surface retryable states, and never swallow errors silently — the door must be honest about what is behind it.

## Practice: Design the Facade Set

A video pipeline has user, operator, and admin audiences.

**Task 1:** Design the three facades and what each exposes.

**Task 2:** Verify each facade stays thin (delegates, never re-implements).

**Task 3:** Design the error surface: what each audience can observe and what is always logged.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can articulate when one facade is enough and when per-audience facades pay off.

**Prompt 2 — Implementation Design:**
> Design a facade that never hides failures: explicit result types and observable states. What does the caller's error handling look like?

**Prompt 3 — Boundary Testing:**
> A facade hides a subsystem swap behind it. Design the versioning that keeps the swap invisible to callers.

## Key Takeaways

- Per-audience facades shape the same engine
- Thin facades delegate; thick ones become subsystems
- Honest facades never swallow errors
- The facade can hide swaps, not failures

## Further Reading

- [Facade — Refactoring Guru](https://refactoring.guru/design-patterns/facade)
- [Interface Segregation + Facade](https://martinfowler.com/bliki/RoleInterface.html)
