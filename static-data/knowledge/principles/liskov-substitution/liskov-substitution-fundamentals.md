---
title: "Liskov Substitution: Replaceable Without Surprises"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "State the Liskov substitution principle"
  - "Identify substitution violations"
  - "Recognize the is-a vs behaves-as distinction"
  - "Fix inheritance design that violates LSP"
prerequisites:
  - "principles/interface-segregation"
  - "principles/single-responsibility"
knowledge_refs:
  - "principles/liskov-substitution"
---

# Liskov Substitution: Replaceable Without Surprises

## The Principle

Liskov Substitution (LSP): if S is a subtype of T, then objects of type T may be replaced with objects of type S without altering the correctness of the program. Callers code against the base contract; every subclass must honor that contract.

The classic violation: a Square extending a Rectangle. A caller widens a rectangle and expects height to stay the same; a Square silently changes both. The caller's assumptions about the base class break.

```java
// Violation: Square overrides setters, breaking base-class assumptions
class Rectangle {
    void setWidth(int w)  { this.w = w; }
    void setHeight(int h) { this.h = h; }
}
class Square extends Rectangle {
    void setWidth(int w)  { super.setWidth(w); super.setHeight(w); }
    void setHeight(int h) { super.setWidth(h); super.setHeight(h); }
}
// Caller: rectangle.setWidth(5); rectangle.setHeight(10); assert h == 10
// With a Square in disguise, h becomes 5. Broken.

// Fix: separate shapes — Square and Rectangle are both shapes, not one
// a subtype of the other. Favor composition or a common Shape contract.
```

## Contracts, Not Class Hierarchies

LSP is about honoring contracts: preconditions not strengthened, postconditions not weakened, invariants preserved, exceptions not broadened. A subclass that throws a new checked exception, returns null where the base promised a value, or silently ignores parameters violates the contract even if it compiles.

## Practice: Find the Violations

Review: a Bird base class with fly() and a Penguin subclass throwing UnsupportedOperationException; a FileStorage subclass of Storage that writes to memory only.

**Task 1:** For each, state the contract violation and the caller surprise.

**Task 2:** Redesign Penguin: an interface hierarchy (FlyingBird, SwimmingBird) instead of Bird.fly().

**Task 3:** Redesign FileStorage: separate MemoryStorage implements the same Storage contract honestly.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the difference between is-a (taxonomy) and behaves-as (contract). Start with Penguin.

**Prompt 2 — Compare & Contrast:**
> Compare LSP violations with interface segregation: what each protects and how they interact.

**Prompt 3 — Boundary Testing:**
> A subclass strengthens a precondition (rejects empty strings the base accepts). Is that always a violation? Argue with a real API.

## Key Takeaways

- Subtypes must honor the base contract fully
- Preconditions strengthen or postconditions weaken = violation
- Contract-first design beats taxonomy-based inheritance
- Composition and interfaces prevent most LSP traps

## Further Reading

- [The Liskov Substitution Principle (Barbara Liskov)](https://en.wikipedia.org/wiki/Liskov_substitution_principle)
- [SOLID — Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html)
