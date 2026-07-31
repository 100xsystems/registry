---
title: "Singleton in Production: Pools and Registries"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Use singletons for shared resources"
  - "Inject instead of import"
  - "Scope to lifetimes"
  - "Test with fakes"
prerequisites:
  []
knowledge_refs:
  - "patterns/singleton"
---

# Singleton in Production: Pools and Registries

## Legitimate Singletons

Connection pools, caches, and config are legitimate singletons: one instance shared by the whole app, never duplicated. The problem was never the single instance — it is the global access point. Inject the singleton into its consumers, and the tests inject a fake instead.

```typescript
// Singleton scoped and injected — no global access point
export class Db {
    private static instance: Db;      // one instance, app-scoped
    static get(): Db { ... }          // used ONLY by the composition root
    query(sql: string): Result { ... }
}

// Consumers receive it:
export class OrderService {
    constructor(private db: Db) {}    // injected, testable with a fake
}
// Composition root wires it once:
const db = Db.get();
const orders = new OrderService(db);
// Only the composition root touches Db.get() — tests construct
// OrderService with an in-memory fake and never see the global.
```

## Scoping

Scope to the right lifetime: a connection pool is app-scoped; a request-scoped transaction context is per-request; a per-test cache is per-test. DI containers manage these lifetimes. The "singleton" pattern collapses every lifetime into global — which is exactly why it is usually a code smell in modern code.

## Practice: Inject the Pool

A connection pool is imported as a singleton by 50 classes; tests hit the real database.

**Task 1:** Inject the pool through constructors everywhere it is imported.

**Task 2:** Add the in-memory fake for tests.

**Task 3:** Verify only the composition root calls the singleton accessor.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me the difference between a singleton instance and a global access point, and why the second is the problem.

**Prompt 2 — Implementation Design:**
> Design a cache singleton that is injectable: interface, instance, and the test fake.

**Prompt 3 — Boundary Testing:**
> A test leaks singleton state between cases. Design the reset hook or the per-test scoping that isolates them.

## Key Takeaways

- Pools, caches, and config are legitimate singletons
- Inject the instance; drop the global access point
- Lifetimes vary: app, request, test
- Only the composition root touches the accessor

## Further Reading

- [Dependency injection — Martin Fowler](https://martinfowler.com/articles/injection.html)
- [Composition root — Mark Seemann](https://blog.ploeh.dk/2011/07/28/CompositionRoot/)
