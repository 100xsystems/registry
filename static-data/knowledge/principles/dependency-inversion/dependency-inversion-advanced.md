---
title: "Advanced Dependency Inversion: Modules and Compile-Time Arrows"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Structure modules so arrows point inward"
  - "Prevent dependency cycles with ownership rules"
  - "Enforce architecture with dependency tests"
  - "Apply DIP to cross-module interfaces"
prerequisites:
  []
knowledge_refs:
  - "principles/dependency-inversion"
---

# Advanced Dependency Inversion: Modules and Compile-Time Arrows

## Module-Level Arrows

The same inversion applies between modules: the domain module should not depend on the infrastructure module. Put interfaces in the module that owns the policy, and let the implementation module depend on it.

When module A needs data from module B, define the interface in A and implement it in B — so A stays independent and B imports A. This is how the dependency arrow flips at the module scale.

```text
Module arrows point inward:
  domain/   (no imports of infra)  <- owns ports
  infra/    (imports domain)       <- implements ports
  app/      (imports domain + infra) <- composition root

Architecture test (pseudo):
  assert_no_import(module='domain', forbidden={'infra', 'web', 'sql'})
```

## Enforcing with Architecture Tests

Conventions decay without enforcement. Architecture tests (e.g., ArchUnit for Java, dependency-cruiser for JS) assert the import rules in CI: the domain module may not import infrastructure packages, and dependency cycles fail the build.

These tests are cheap to write, run in seconds, and turn "keep the arrows right" from a review comment into a hard guarantee.

## Practice: Map and Enforce Module Dependencies

Your monorepo has 6 modules; the domain module already imports a logging library and a JSON library from the infra layer.

**Task 1:** Define the allowed dependency matrix for the 6 modules.

**Task 2:** Write the architecture test that forbids domain importing infra.

**Task 3:** Find the existing violations and refactor two of them using interfaces.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me how to decide which module owns an interface when two modules need each other. Ask me to reason through a cycle example.

**Prompt 2 — Implementation Design:**
> Design a plugin architecture where third-party plugins implement domain-defined ports. How do you load, validate, and isolate plugins?

**Prompt 3 — Boundary Testing:**
> A shared util module becomes a dumping ground everyone imports. Design the dependency rule and the migration.

## Key Takeaways

- Module arrows should point inward toward the domain
- Own the interface in the module that defines the policy
- Architecture tests enforce arrows in CI
- Plugin systems are DIP applied at the deployment level

## Further Reading

- [ArchUnit (Java architecture tests)](https://www.archunit.org/)
- [dependency-cruiser (JS)](https://github.com/sverweij/dependency-cruiser)
