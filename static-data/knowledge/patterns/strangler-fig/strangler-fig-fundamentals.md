---
title: "Strangler Fig: Replace a System Slowly"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the strangler pattern"
  - "Route incrementally"
  - "Avoid the big-bang rewrite"
  - "Retire legacy pieces"
prerequisites:
  - "patterns/facade"
  - "patterns/proxy"
knowledge_refs:
  - "patterns/strangler-fig"
---

# Strangler Fig: Replace a System Slowly

## The Model

Named after the fig that grows around a host tree and eventually replaces it, the pattern builds the new system next to the old one, routes traffic over incrementally, and retires legacy pieces once the new ones carry them. No big-bang rewrite: the system is replaced feature by feature, safely.

```text
Strangler fig flow:
  1. A facade/router sits in front of the legacy system.
  2. New capability is built in the new system behind the same
     interface.
  3. The router sends that feature's traffic to the new system.
  4. When the new system covers a legacy feature, the legacy
     implementation is retired.
  5. Eventually the router only points at the new system and
     the legacy host dies.
Rules that keep it safe:
  - the facade interface must not change during the migration
  - each feature ships with a rollback (route back to legacy)
  - legacy pieces are deleted, not abandoned (no zombie code)
```

## Why Not Rewrite

Big-bang rewrites fail: the legacy encodes years of hard-won behavior that a rewrite cannot reproduce at once. Strangling delivers value continuously — each feature ships, each risk is contained — and keeps the old system as the safety net until its last feature is replaced.

## Practice: Strangle the Monolith

A 10-year-old billing monolith: invoices move to the new service first, payments later.

**Task 1:** Design the facade and the routing rule per feature.

**Task 2:** Plan the feature order by risk and value.

**Task 3:** Design the rollback for the first migrated feature.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why incremental replacement beats the big-bang rewrite. Start with risk.

**Prompt 2 — Compare & Contrast:**
> Compare strangler with the branch-by-abstraction and the anti-corruption layer. When does each apply?

**Prompt 3 — Boundary Testing:**
> A migrated feature has a subtle legacy edge case. Design the shadow-traffic comparison that catches it before cutover.

## Key Takeaways

- Strangler replaces systems feature by feature
- A stable facade makes routing reversible
- Each migration ships with a rollback
- Retired pieces are deleted, not abandoned

## Further Reading

- [Strangler Fig — Martin Fowler](https://martinfowler.com/bliki/StranglerFigApplication.html)
- [Strangler pattern — Microsoft](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig)
