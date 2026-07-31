---
title: "Factory in Production: DI and Parsers"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Use factories with DI containers"
  - "Select implementations by context"
  - "Test factory output"
  - "Avoid factory misuse"
prerequisites:
  []
knowledge_refs:
  - "patterns/factory"
---

# Factory in Production: DI and Parsers

## Factories and DI

DI containers provide singletons; factories provide context-dependent instances. A factory that receives the container and builds the right implementation per request (per tenant, per format) combines the two cleanly.

```java
// Factory injected by the container, produces per-context products
@Singleton
class PaymentFactory {
    private final Map<String, Provider> providers;   // injected set

    PaymentFactory(List<Provider> all) {
        this.providers = all.stream()
            .collect(toMap(Provider::name, p -> p));
    }

    Provider forCurrency(String currency) {
        return providers.getOrDefault(currency, providers.get("default"));
    }
}
```

## Misuse

Factories are misused when they replace a plain constructor for no varying reason, or when they grow into god-objects that construct everything. The smell: a factory with a parameter that switches on every product type — that is a simple factory that should be a registry or config.

## Practice: Build the Context Factory

A notification service chooses email, SMS, or push by the user's channel preference.

**Task 1:** Define the Channel interface and three implementations.

**Task 2:** Build the factory that selects by preference with a default fallback.

**Task 3:** Add a fourth channel (WhatsApp) with zero changes to the sender flow.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me when a factory is justified versus a direct constructor. Ask me to apply the "does the choice vary?" test.

**Prompt 2 — Implementation Design:**
> Design a DI-registered factory for per-tenant storage. Where does the tenant context come from?

**Prompt 3 — Boundary Testing:**
> The factory returns a product with an unsatisfied dependency. Design the startup validation that catches it.

## Key Takeaways

- Factories combine with DI for context-dependent instances
- Selection by key with a default is the common shape
- The "does the choice vary?" test gates factory use
- Factory registries beat god-factories

## Further Reading

- [Factory Method — Refactoring Guru](https://refactoring.guru/design-patterns/factory-method)
- [Dependency Injection — Martin Fowler](https://martinfowler.com/articles/injection.html)
