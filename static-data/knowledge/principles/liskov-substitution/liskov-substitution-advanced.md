---
title: "Advanced LSP: Variance and Behavioral Contracts"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Explain variance in typed systems"
  - "Apply behavioral subtyping rules precisely"
  - "Use immutable types to avoid substitution traps"
  - "Design hierarchies that survive evolution"
prerequisites:
  []
knowledge_refs:
  - "principles/liskov-substitution"
---

# Advanced LSP: Variance and Behavioral Contracts

## Variance

Variance governs where a subtype can appear: a List<Square> is not a List<Rectangle> (adding a Rectangle would break it). Covariance (producers) and contravariance (consumers) encode this: read-only containers can be covariant; mutable ones cannot.

```text
Variance rules:
  Covariant  (out / +T): value only leaves -> List<out Square> is List<Rectangle>
  Contravariant (in / -T): value only enters -> Consumer<in Rectangle> is Consumer<Square>
  Invariant: mutable containers (read AND write) -> no substitution

Behavioral subtyping: subtype must
  - not strengthen preconditions
  - not weaken postconditions
  - preserve invariants
  - not broaden thrown exceptions
```

## Immutable Design

Immutable types sidestep most variance and substitution hazards: a read-only Square where a Rectangle is expected is safe because nothing can mutate it into a contradiction. Immutability turns many LSP traps into non-issues.

## Practice: Design a Variance-Safe Model

A document system: read-only views, mutable documents, and a producer of documents.

**Task 1:** Design the type hierarchy so read views are covariant and writers are invariant.

**Task 2:** Prove that a List<SpecialDoc> is not assignable to List<Doc> and explain the runtime hazard it prevents.

**Task 3:** Refactor one mutable hierarchy to immutable value types and note what substitution guarantees you gain.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why "out" and "in" annotations encode behavioral substitution in the type system.

**Prompt 2 — Implementation Design:**
> Design a collection library API with correct variance annotations and prove each with a substitution example.

**Prompt 3 — Boundary Testing:**
> A subtype narrows a return type (covariant return) — is that always safe? Give the rule and a counterexample.

## Key Takeaways

- Variance encodes where substitution is type-safe
- Behavioral subtyping rules are the semantic contract
- Immutability eliminates many substitution hazards
- Covariant returns are safe; covariant mutable containers are not

## Further Reading

- [Variance — Kotlin Docs](https://kotlinlang.org/docs/generics.html#variance)
- [Behavioral Subtyping — Wikipedia](https://en.wikipedia.org/wiki/Behavioral_subtyping)
