---
title: "Advanced Convention: Domain Structure and Codegen"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Design domain-driven folder conventions"
  - "Generate boilerplate from conventions safely"
  - "Version conventions as code"
  - "Avoid convention traps: magic and indirection"
prerequisites:
  []
knowledge_refs:
  - "principles/convention-over-configuration"
---

# Advanced Convention: Domain Structure and Codegen

## Domain Structure

Organize by domain (billing/, orders/, identity/) rather than by technical layer (controllers/, services/, models/), so each feature is a self-contained unit. Within a domain, the layering convention applies uniformly.

```text
Domain-first convention (per domain folder):
  orders/
    api/        # routes/handlers
    domain/     # entities, value objects, rules
    app/        # use cases / services
    infra/      # persistence, queues, clients
    tests/
The same shape for every domain -> predictable navigation
```

## Codegen and Convention Versioning

Generators turn conventions into instant, consistent artifacts: a new domain scaffolded by a CLI is identical in shape to every other. The generator IS the documented convention.

Version the generator with the repo; when the convention evolves, the generator and its outputs migrate together, and CI fails on stale-shaped modules.

## Practice: Build the Scaffolder

Your team creates a new domain folder by hand every time, and they differ subtly.

**Task 1:** Specify the generator inputs (domain name, entities) and outputs (all folders + skeletons).

**Task 2:** Add a CI check that validates every domain folder matches the current template.

**Task 3:** Design the migration path when the convention changes: rename, regenerate, or dual-run?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can articulate when code generation helps versus when it creates a second source of truth.

**Prompt 2 — Implementation Design:**
> Design a convention system for a 200-module monorepo where 10 teams contribute. How do you make conventions cross-team and enforced?

**Prompt 3 — Boundary Testing:**
> A generator creates boilerplate that drifts from hand-written modules. Design a drift detector and a fix workflow.

## Key Takeaways

- Domain-first structure scales to hundreds of modules
- Generators turn conventions into enforced artifacts
- Version generators and migrate outputs together
- CI drift checks keep convention decay out

## Further Reading

- [Feature-Sliced Design](https://feature-sliced.design/)
- [Code Generation — AWS Amplify / Prisma Philosophy](https://www.prisma.io/docs)
