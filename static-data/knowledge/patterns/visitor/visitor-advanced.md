---
title: "Advanced Visitor: Extensible and Generic Visitors"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Write type-safe visitors"
  - "Use generic visitors"
  - "Handle the expression problem"
  - "Choose visitor vs pattern matching"
prerequisites:
  []
knowledge_refs:
  - "patterns/visitor"
---

# Advanced Visitor: Extensible and Generic Visitors

## The Expression Problem

The expression problem: extend a system by adding new data variants (classes) or new operations (visitors) — classic OOP adds data variants easily (new classes) but struggles with new operations; visitors flip it: new operations are easy, new variants are painful. Modern languages solve it with pattern matching (exhaustive, compiler-checked) — the visitor without the boilerplate.

```typescript
// Exhaustive pattern matching vs visitor boilerplate
type Expr =
  | { kind: 'num'; value: number }
  | { kind: 'add'; left: Expr; right: Expr }
  | { kind: 'mul'; left: Expr; right: Expr };

function evalExpr(e: Expr): number {
  switch (e.kind) {
    case 'num': return e.value;
    case 'add': return evalExpr(e.left) + evalExpr(e.right);
    case 'mul': return evalExpr(e.left) * evalExpr(e.right);
  }
}
// Adding an operation = adding a function (like a visitor).
// Adding a variant = the switch exhaustiveness check flags every
// operation that must handle it — the compiler does the bookkeeping
// the visitor pattern does by hand. Same expressiveness, no
// accept methods, no visitXXX boilerplate.
```

## Choosing

Use the visitor pattern where pattern matching is unavailable or where the structure is an external library you cannot change. Use pattern matching (Rust match, Kotlin sealed classes, TS discriminated unions, Python match) where available — it is the same idea with compiler enforcement. The visitor survives in ecosystems where the structure must stay open.

## Practice: Compare the Approaches

An expression language with num, add, and mul needs eval, print, and a new mul variant.

**Task 1:** Implement eval and print as visitors.

**Task 2:** Implement the same with sealed/discriminated union pattern matching.

**Task 3:** Add a new variant in each and compare the change surface.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain the expression problem and why visitors are one side of it.

**Prompt 2 — Implementation Design:**
> Design a type-safe visitor in a language with generics. How does the visitor carry a generic result type?

**Prompt 3 — Boundary Testing:**
> A variant is added and half the visitors forget it. Design the exhaustive check that catches it at compile time.

## Key Takeaways

- The expression problem pits variants against operations
- Visitors make operations easy, variants hard
- Pattern matching gives the same power with exhaustiveness
- Visitors persist where structures must stay open

## Further Reading

- [The Expression Problem — Wikipedia](https://en.wikipedia.org/wiki/Expression_problem)
- [TypeScript discriminated unions](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#discriminated-unions)
