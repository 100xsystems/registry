---
title: "LSP in Production: Interfaces and APIs"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Apply LSP to interface implementations"
  - "Design contracts with pre/post conditions"
  - "Test substitution behavior"
  - "Avoid covariant traps"
prerequisites:
  []
knowledge_refs:
  - "principles/liskov-substitution"
---

# LSP in Production: Interfaces and APIs

## Interface Contracts

Every implementation of an interface promises the contract: the same behavior for the same inputs, honoring the same invariants. The repository interface promises find() never returns null on missing rows? Then every implementation — Postgres, in-memory, mock — must keep that promise.

```typescript
// Contract: find returns undefined for missing ids, never throws
interface UserStore {
    find(id: string): Promise<User | undefined>;
}

// Postgres impl: returns undefined on empty row   -> honors contract
// Redis impl:   throws on missing key            -> VIOLATES contract
// Fake in tests: returns User({ id, ... })         -> honors contract

// Contract tests run against every implementation:
test.each(implementations)('$name find honors contract', (impl) => {
    expect(await impl.find('missing')).toBeUndefined();
});
```

## Contract Tests

The strongest guard for LSP is contract testing: the same test suite runs against every implementation of an interface, verifying pre/post conditions and invariants uniformly. If the mock, the real store, and the cache all pass the same suite, substitution is safe.

## Practice: Write the Contract Suite

A cache interface has get, set, and delete, with a documented contract.

**Task 1:** Write the contract: what get returns for missing keys, TTL semantics, and delete idempotency.

**Task 2:** Implement the contract test suite and run it against an in-memory and a Redis implementation.

**Task 3:** Fix the implementation that violates the contract and document why.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why contract tests are the practical enforcement of LSP. Ask me to list the contract points of an interface you know.

**Prompt 2 — Implementation Design:**
> Design a plugin API where third-party plugins must honor the contract. What tests can you run against plugins at load time?

**Prompt 3 — Boundary Testing:**
> Two implementations legitimately differ in performance but not behavior. Where does that difference belong in the contract?

## Key Takeaways

- Every implementation honors the same contract
- Contract tests run uniformly against all implementations
- Behavioral substitutability is what callers rely on
- Performance differences are not contract violations

## Further Reading

- [Contract Testing — Pact](https://docs.pact.io/)
- [Design by Contract — Eiffel](https://www.eiffel.com/values/design-by-contract/introduction/)
