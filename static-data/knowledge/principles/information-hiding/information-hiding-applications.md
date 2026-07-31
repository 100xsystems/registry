---
title: "Information Hiding in Production: Modules and Packages"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design package/module visibility"
  - "Use exported surface areas deliberately"
  - "Manage cross-module dependencies"
  - "Version public APIs while hiding internals"
prerequisites:
  []
knowledge_refs:
  - "principles/information-hiding"
---

# Information Hiding in Production: Modules and Packages

## Module Boundaries

At module scale, information hiding is about the exported surface: which types and functions other modules may import. A module with everything public has no boundary; a module with a deliberate public API hides its evolution.

```text
Module surface design:
  public:   types the contract needs (Order, OrderService)
  internal: helpers, adapters, representation (never importable)
  Private-by-default languages: Rust (pub), Go (exported), Java (package-private)

Rule: if a caller imports your internals, your module has no boundary.
```

## API Stability

The public API is a stability contract: callers compile against it, so breaking changes cost migrations. Hiding internals means the public API can stay stable while the internals evolve freely. Semantic versioning signals when the public surface does change.

## Practice: Audit the Exports

A library module exports 30 symbols; only 6 are used by consumers.

**Task 1:** Identify the 6 that form the real API and move the rest to internal visibility.

**Task 2:** Check the exported types: do any leak internal representation (e.g., a backing collection)?

**Task 3:** Write the public API doc: what is promised, what is internal, what is experimental.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why "everything public" in a module is an anti-pattern and how visibility keywords encode the boundary.

**Prompt 2 — Implementation Design:**
> Design a module that hides its persistence (SQL) behind a repository interface. What escapes if the SQL leaks?

**Prompt 3 — Boundary Testing:**
> A consumer needs one internal helper. Design the path: promote it to the public API, duplicate it, or export a narrow "experimental" surface?

## Key Takeaways

- Deliberate exported surfaces create real boundaries
- Internals leaking into imports destroy module independence
- Public APIs are stability contracts
- Experimental surfaces accommodate rare needs

## Further Reading

- [The API Surface — Google Style Guides](https://google.github.io/styleguide/)
- [Semantic Versioning](https://semver.org/)
