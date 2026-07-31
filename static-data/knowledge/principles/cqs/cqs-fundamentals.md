---
title: "Command Query Separation: Mutations and Reads Never Mix"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define commands and queries precisely"
  - "Explain why mixing them is dangerous"
  - "Refactor a mixed method into command + query"
  - "Identify CQS violations in real code"
prerequisites:
  - "principles/single-responsibility"
  - "principles/separation-of-concerns"
knowledge_refs:
  - "principles/cqs"
---

# Command Query Separation: Mutations and Reads Never Mix

## The Rule

CQS (Bertrand Meyer): a method is either a command that changes state and returns nothing, or a query that returns a value and changes nothing. Never both.

A mixed method — "pop() returns the last element and removes it" — is a state-changing expression: callers may ignore the return (mutating) or call twice (reading), and each misuse hides a bug.

```java
// Violation: pop() mutates AND returns — caller must know both
Item item = stack.pop();          // is item the last one? was it removed?

// CQS: command + query separated
Item peek() { return stack.get(size() - 1); }  // query: no change
void  pop() { stack.remove(size() - 1); }      // command: no return
// Usage is now explicit:
if (!stack.isEmpty()) {
    Item top = stack.peek();
    stack.pop();
}
```

## Why It Matters

Queries are safe to call anywhere, any number of times, in any order — they enable caching, memoization, and parallelism. Commands are the opposite: order matters, repetition matters. Mixing the two destroys the ability to reason about either.

CQS is the object-level twin of the database pattern: reads and writes take different paths (CQRS) and can be scaled independently.

## Practice: Find and Fix Violations

Review these signatures and refactor the mixed ones: setBalance(x) returns boolean, getAndIncrement() returns int, deleteUser(id) returns User, findById(id) returns Optional.

**Task 1:** Classify each as command, query, or mixed.

**Task 2:** Refactor getAndIncrement() into get() + increment().

**Task 3:** For setBalance(x) returning success, explain why throwing or returning a result object is the CQS-clean alternative.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why "returns the old value" variants are worse than plain mixed methods. Start with thread safety.

**Prompt 2 — Compare & Contrast:**
> Compare CQS with CQRS (event-sourced read models). When does the object-level rule scale into the architecture-level pattern?

**Prompt 3 — Boundary Testing:**
> A cache get() populates the cache on miss — it mutates internal state but returns a value. Is this a CQS violation? Argue both sides.

## Key Takeaways

- Commands change state and return nothing
- Queries return values and change nothing
- Mixed methods destroy reasoning about both behaviors
- CQS scales into CQRS at the architecture level

## Further Reading

- [Command Query Separation — Martin Fowler](https://martinfowler.com/bliki/CommandQuerySeparation.html)
- [CQRS — Martin Fowler](https://martinfowler.com/bliki/CQRS.html)
