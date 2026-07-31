---
title: "Advanced Defensive Programming: Fuzzers and Contracts"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Apply design-by-contract with preconditions and invariants"
  - "Use property-based testing and fuzzing"
  - "Turn defensive checks into permanent regression tests"
  - "Balance defense with performance in hot paths"
prerequisites:
  []
knowledge_refs:
  - "principles/defensive-programming"
---

# Advanced Defensive Programming: Fuzzers and Contracts

## Design by Contract

Define preconditions (what callers must provide), postconditions (what the method guarantees), and invariants (what never changes). Enforced in debug builds, they catch contract violations at the first wrong step.

```python
# Contract enforcement with assertions (debug-only in hot paths)
def debit(account, amount):
    assert amount > 0, 'precondition: positive amount'
    assert account.is_open, 'precondition: open account'
    balance = account.balance - amount
    assert balance >= account.overdraft_limit, 'postcondition: within limit'
    account.balance = balance
    assert account.balance == expected, 'invariant: balance consistency'
    return balance
```

## Fuzzing and Property Testing

Fuzzing feeds random, malformed inputs to parsers and finds crashes and hangs the tests never imagined. Property-based testing asserts invariants over thousands of generated inputs — the same spirit as defensive checks, but automated and exhaustive.

This is defensive programming made productive: the checks you write by hand become test oracles that keep running forever.

## Practice: Write a Property Test

A parseUser() function parses JSON user objects.

**Task 1:** List three invariants (e.g., id is string, age >= 0 when present, name non-empty).

**Task 2:** Write a property test that generates 1,000 random user JSONs and asserts the invariants hold or the parse raises a clean error.

**Task 3:** Run a quick fuzz pass over the parser and fix any crashes.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why property-based testing is stronger than example-based tests for defensive code.

**Prompt 2 — Implementation Design:**
> Design a contract layer for a library: preconditions enforced in debug, elided in production. Where does each check go, and how is it logged?

**Prompt 3 — Boundary Testing:**
> An invariant check in a hot loop costs 2% throughput. Decide when to keep, move, or drop it, and how to measure.

## Key Takeaways

- Contracts make violations visible at the first wrong step
- Fuzzing finds what tests never imagine
- Property tests turn defensive checks into permanent oracles
- Hot paths trade defense against measured cost

## Further Reading

- [Design by Contract — Eiffel (Bertrand Meyer)](https://www.eiffel.com/values/design-by-contract/introduction/)
- [Hypothesis (property-based testing)](https://hypothesis.readthedocs.io/)
