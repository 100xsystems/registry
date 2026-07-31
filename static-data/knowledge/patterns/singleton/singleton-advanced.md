---
title: "Advanced Singleton: Multiton and Lifecycle Managers"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Explain the multiton"
  - "Manage instance lifecycles"
  - "Design registries"
  - "Test stateful singletons"
prerequisites:
  []
knowledge_refs:
  - "patterns/singleton"
---

# Advanced Singleton: Multiton and Lifecycle Managers

## Multiton and Registries

A multiton keys instances: one instance per key (one DB pool per tenant). A registry maps keys to instances with registration. Both are singletons generalized — and both belong behind a container or composition root, with explicit lifetimes, not globals.

```java
// Multiton: one instance per key
class PoolRegistry {
    private static final Map<String, ConnectionPool> pools = new ConcurrentHashMap<>();

    static ConnectionPool poolFor(String tenant) {
        return pools.computeIfAbsent(tenant, ConnectionPool::new);
    }
}
// One pool per tenant, created on demand, shared thereafter.
// Scoped where it is needed; never a global for the app.
// The registry is the natural home: registries, factories, and
// DI containers all manage "one per X" instances — the singleton
// pattern is the degenerate case of X = app.
```

## Lifecycle Management

Managed instances need lifecycle: creation, warming, shutdown, and recreation on failure. A container or a registry owns the lifecycle; the pattern's static instance does not. Stateful singletons (caches, pools) also need reset hooks for tests — which the global access point cannot provide cleanly.

## Practice: Manage the Pools

A multi-tenant app needs one pool per tenant, warm on first use, drain on shutdown.

**Task 1:** Build the registry with per-key creation.

**Task 2:** Add lifecycle: warm, drain, and recreate on failure.

**Task 3:** Add the test reset and verify pool state does not leak between tests.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why the multiton is a scoped singleton and who owns its lifecycle.

**Prompt 2 — Implementation Design:**
> Design a connection-pool manager for 100 tenants: creation, sizing, idle eviction, and shutdown ordering.

**Prompt 3 — Boundary Testing:**
> A tenant's pool fails open connections. Design the recreation path that warms a fresh pool without breaking in-flight requests.

## Key Takeaways

- Multiton keys instances per entity
- Lifecycle belongs to a manager, not a static field
- Registries and containers own the "one per X"
- Test resets need explicit hooks

## Further Reading

- [Multiton — Wikipedia](https://en.wikipedia.org/wiki/Multiton_pattern)
- [Registry — Martin Fowler](https://martinfowler.com/eaaCatalog/registry.html)
