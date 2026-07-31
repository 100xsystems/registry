---
title: "Decorator in Production: Middleware and Observability"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Wrap services with cross-cutting decorators"
  - "Compose observability stacks"
  - "Keep decorators interchangeable"
  - "Test decorated stacks"
prerequisites:
  []
knowledge_refs:
  - "patterns/decorator"
---

# Decorator in Production: Middleware and Observability

## Service Decorators

A repository interface decorated with a CacheDecorator, a MetricsDecorator, and a RetryDecorator gives every capability without touching the repository — or the callers. Cross-cutting concerns become composable layers.

```java
// Service decorators: stack cross-cutting concerns
interface UserRepo {
    Optional<User> find(String id);
}

class CacheDecorator implements UserRepo {
    private final UserRepo inner;
    CacheDecorator(UserRepo inner) { this.inner = inner; }
    public Optional<User> find(String id) {
        // cache-first; fall back to inner on miss
        return cached(id).or(() -> inner.find(id));
    }
}

UserRepo repo = new MetricsDecorator(
                    new CacheDecorator(
                    new RetryDecorator(
                        new DbUserRepo())));   // stack order = behavior
```

## Interchangeable Stacks

Because decorators implement the same interface, stacks are interchangeable: tests use an in-memory repo with no decorators, production stacks them all. The composition root decides the stack; the application never knows.

## Practice: Stack the Decorators

A payment client needs retries, circuit breaking, metrics, and logging.

**Task 1:** Implement the four decorators over the PaymentClient interface.

**Task 2:** Decide the stack order and justify (metrics outermost, retries inside circuit breaker?).

**Task 3:** Show the test stack (no decorators) and the prod stack (all four) share the same interface.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why decorator order changes behavior (retry inside vs outside a circuit breaker). Ask me to pick the right order.

**Prompt 2 — Implementation Design:**
> Design an observability decorator that measures latency, counts errors, and propagates trace IDs. What does it add to the interface?

**Prompt 3 — Boundary Testing:**
> A decorator swallows an exception to return a fallback. Design the flag that keeps the original error observable.

## Key Takeaways

- Cross-cutting concerns become composable layers
- Stack order is behavior — choose deliberately
- The composition root chooses the stack
- Test stacks and prod stacks share the interface

## Further Reading

- [Decorator Pattern — Refactoring Guru](https://refactoring.guru/design-patterns/decorator)
- [Fault Tolerance with Decorators (Resilience4j)](https://resilience4j.readme.io/)
