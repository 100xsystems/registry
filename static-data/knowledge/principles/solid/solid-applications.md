---
title: "SOLID in Production: Design Reviews and Evolution"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Use SOLID vocabulary in design reviews"
  - "Prioritize violations by risk"
  - "Refactor toward SOLID incrementally"
  - "Keep the legacy migration safe"
prerequisites:
  []
knowledge_refs:
  - "principles/solid"
---

# SOLID in Production: Design Reviews and Evolution

## Reviews in SOLID Terms

SOLID gives review comments precision: instead of "this class is too big", say "this class has two reasons to change (SRP)" or "this switch must be edited for every new shape (OCP)". The shared vocabulary makes design discussions concrete and teachable.

```text
Review prompts in SOLID terms:
  S: "Who else changes this class, and for what reason?"
  O: "What breaks when we add the third variant?"
  L: "Does every subclass honor the base contract?"
  I: "Does this client depend on methods it never uses?"
  D: "What concrete detail is this coupled to?"
```

## Migration Order

Refactoring a legacy codebase toward SOLID is a risk-ranked sequence: fix the violations causing real pain first (the god class blocking features, the fat interface forcing changes), keep behavior identical with characterization tests, and refactor in small, reviewable slices.

## Practice: Prioritize the Violations

A legacy billing module fails every SOLID test. New features land weekly and keep breaking.

**Task 1:** Rank the violations by how much they block feature work.

**Task 2:** Write characterization tests that lock current behavior before refactoring.

**Task 3:** Plan the slice order: which class gets extracted first, and how is each step verified?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why characterization tests are the safe foundation for SOLID refactoring. Ask me how to write one.

**Prompt 2 — Implementation Design:**
> Design a weekly "design fitness" review that scores the riskiest module against SOLID and tracks the trend.

**Prompt 3 — Boundary Testing:**
> A refactor toward SOLID is blocked by a shared transaction. Design the outbox-based path that unblocks it safely.

## Key Takeaways

- SOLID is a precise review vocabulary
- Fix the violations that hurt most first
- Characterization tests make refactoring safe
- Migrate in small, verified slices

## Further Reading

- [Working Effectively with Legacy Code](https://www.oreilly.com/library/view/working-effectively-with/0131177052/)
- [Characterization Testing — Michael Feathers](https://michaelfeathers.silvrback.com/characterization-testing)
