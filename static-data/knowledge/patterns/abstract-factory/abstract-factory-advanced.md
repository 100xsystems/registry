---
title: "Advanced Abstract Factory: Registries and Conventions"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Build a factory registry"
  - "Select factories by convention or config"
  - "Keep the family open-closed"
  - "Handle cross-cutting product concerns"
prerequisites:
  []
knowledge_refs:
  - "patterns/abstract-factory"
---

# Advanced Abstract Factory: Registries and Conventions

## Factory Registries

When the number of families grows (ten databases, eight clouds), a registry maps a key to its factory: register(Key, Factory) at startup, then factory = registry.get(key). New families join by registration — the core stays closed.

```python
# Registry: new families join by registration, core never changes
class FactoryRegistry:
    def __init__(self):
        self._factories = {}

    def register(self, name, factory):
        self._factories[name] = factory

    def get(self, name):
        if name not in self._factories:
            raise KeyError(f'unknown family: {name}')
        return self._factories[name]

registry = FactoryRegistry()
registry.register('postgres', PostgresFactory())
registry.register('sqlite', SqliteFactory())
registry.register('memory', MemoryFactory())

factory = registry.get(os.environ.get('DB', 'memory'))
```

## Cross-Cutting Concerns

Every product may need logging, metrics, or retries. A decorator factory wraps every product the base factory creates — one place to add cross-cutting behavior across the whole family, keeping each concrete factory simple.

## Practice: Design the Registry

A data layer supports 6 databases; each needs a matching Connection and Query product with metrics.

**Task 1:** Build the registry and register the six factories.

**Task 2:** Add a decorator factory that wraps products with metrics — no concrete factory changes.

**Task 3:** Design the error when an unknown family is requested, and the startup validation that lists registered families.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain how a registry keeps the abstract factory open-closed.

**Prompt 2 — Implementation Design:**
> Design a theme system where themes register as factories and the UI core stays untouched. How do themes discover and hot-swap?

**Prompt 3 — Boundary Testing:**
> Two factories produce the same product type with different behaviors. Design the contract test that keeps them substitutable.

## Key Takeaways

- Registries make families extensible by registration
- Decorator factories apply cross-cutting concerns once
- Startup validation catches misconfiguration early
- Contract tests keep families substitutable

## Further Reading

- [Registry Pattern — Martin Fowler](https://martinfowler.com/eaaCatalog/registry.html)
- [Decorator Pattern — Refactoring Guru](https://refactoring.guru/design-patterns/decorator)
