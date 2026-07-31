---
title: "Open-Closed in Production: Plugins and Policies"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design plugin extension points"
  - "Extend business policies without editing core flows"
  - "Version extension points"
  - "Manage the tension between openness and simplicity"
prerequisites:
  []
knowledge_refs:
  - "principles/open-closed"
---

# Open-Closed in Production: Plugins and Policies

## Plugin Architectures

A plugin architecture makes the core open-closed by construction: the core defines extension points (interfaces, hooks, registries) and third parties register implementations. IDEs, browsers, and CI systems all work this way — the core stays stable while the plugin ecosystem grows.

```text
Plugin architecture shape:
  core/          defines ExtensionPoint interfaces (never changes)
  registry/      discovers and loads implementations
  plugins/       third-party implementations of the points

Rules:
  - The core never imports a specific plugin
  - The plugin manifest declares which point it implements
  - Version the extension point (major bump = breaking)
```

## Policy Extension

Business rules (discounts, taxes, shipping) are the most volatile part of a system. Modeling them as strategies or rule objects — rather than if-chains in the order flow — keeps the checkout core closed while policies grow.

## Practice: Design the Extension Points

A checkout flow needs new payment and discount types every quarter.

**Task 1:** Define the PaymentMethod and DiscountRule extension points.

**Task 2:** Move the current variants into implementations; verify the core flow is untouched.

**Task 3:** Define the versioning policy for the extension points and the migration path.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why versioning extension points matters and what happens when one evolves without a contract. Ask me about breaking changes.

**Prompt 2 — Implementation Design:**
> Design a plugin registry with discovery, validation, and isolation. How do you prevent a bad plugin from taking down the core?

**Prompt 3 — Boundary Testing:**
> A plugin needs to change core behavior, not just extend it. Design the escape hatch that does not break the closed core.

## Key Takeaways

- Plugins make the core open-closed by construction
- Business policies belong in strategies, not if-chains
- Extension points need versioning
- Openness and simplicity are balanced by contract discipline

## Further Reading

- [Plugin Architecture — Martin Fowler](https://martinfowler.com/articles/osgi.html)
- [Strategy Pattern — Refactoring Guru](https://refactoring.guru/design-patterns/strategy)
