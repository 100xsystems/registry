---
title: "Advanced DRY: Abstraction Boundaries"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Recognize the \"god module\" failure mode"
  - "Version shared abstractions safely"
  - "Use dependency injection to vary behavior without forks"
  - "Measure coupling to guide extraction"
prerequisites:
  []
knowledge_refs:
  - "principles/dry"
---

# Advanced DRY: Abstraction Boundaries

## The God Module

When too much shared code accumulates in one utils module, every change ripples through dozens of consumers. The abstraction became a coupling point: DRY bought maintenance at the price of independence.

The fix is not abandoning DRY but right-sizing the boundary: group shared code by domain (shared/billing/, shared/identity/) so changes are scoped to consumers that share the domain.

```text
Anti-pattern: src/shared/utils.ts with 40 exports used everywhere.
Better: domain-scoped sharing
  shared/billing/  (used only by billing consumers)
  shared/identity/ (used only by identity consumers)
  shared/http/     (the few things truly global)
Coupling metric to watch: fan-in per shared module.
```

## Versioning and Variation

Shared abstractions that must evolve use semantic versioning: consumers pin major versions, and a new major can change the abstraction without breaking everyone at once. Alternatively, strategy injection lets consumers vary behavior through an interface instead of forking the shared code.

## Practice: Right-Size a Shared Module

shared/utils.ts has 40 exports, 200 importers, and every change takes a week to roll out.

**Task 1:** Measure fan-in per export; group exports by the domains that use them.

**Task 2:** Split the module into domain-scoped packages with versioned releases.

**Task 3:** Identify two exports that should be strategies (injected) instead of shared implementations.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can articulate when DRY and modularity conflict, and how domain-scoped sharing resolves it.

**Prompt 2 — Implementation Design:**
> Design a shared currency-conversion library used by billing, payroll, and reporting. How do you version rate-source changes without breaking all three?

**Prompt 3 — Boundary Testing:**
> Two consumers need subtly different semantics from a shared function. Design the option surface that covers both without a fork.

## Key Takeaways

- Over-abstraction becomes a coupling point
- Share by domain, not by dump
- Version shared abstractions; pin majors
- Strategy injection beats forking shared code

## Further Reading

- [The Wrong Abstraction — Sandi Metz](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction)
- [Rule of Three — Wikipedia](https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming))
