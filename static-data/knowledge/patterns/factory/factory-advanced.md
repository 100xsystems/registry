---
title: "Advanced Factory: Abstract Factories and Registries"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Compose factories hierarchically"
  - "Build registries for open-closed creation"
  - "Handle factory lifecycle"
  - "Test factory hierarchies"
prerequisites:
  []
knowledge_refs:
  - "patterns/factory"
---

# Advanced Factory: Abstract Factories and Registries

## Hierarchies and Registries

A registry of factories keeps creation open-closed: register(Key, Factory) at startup; new creators join by registration. A factory of factories (abstract factory) produces related products; the registry selects which family.

```python
# Registry of factories: open-closed creation
class CreatorRegistry:
    def __init__(self):
        self.creators = {}

    def register(self, key, creator):
        self.creators[key] = creator

    def create(self, key, *args):
        if key not in self.creators:
            raise UnknownCreator(key)
        return self.creators[key](*args)

# Startup: register all known creators
registry.register('json', JsonParser.create)
registry.register('csv', CsvParser.create)
# New parser -> one registration line, core untouched.
```

## Lifecycle and Testing

Factories that hold resources (connection pools, clients) need lifecycle management: create, validate, and dispose hooks. Testing factory hierarchies uses a fake factory registered under the same key — the registry makes the swap trivial.

## Practice: Design the Creator Registry

A platform parses 6 formats and must add more without touching the core.

**Task 1:** Build the registry and register six creators at startup.

**Task 2:** Add a validation pass (each creator produces a working product).

**Task 3:** Add lifecycle hooks (dispose) and the fake-factory test strategy.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain how a registry implements open-closed for creation.

**Prompt 2 — Implementation Design:**
> Design a plugin loader where plugins register their creators on load. How do you validate and isolate a bad plugin?

**Prompt 3 — Boundary Testing:**
> Two creators register the same key. Design the conflict policy (reject, last-wins, or namespace).

## Key Takeaways

- Registries keep creation open-closed
- Startup validation catches bad creators early
- Lifecycle hooks manage factory resources
- Fake factories under the same key make testing trivial

## Further Reading

- [Registry — Martin Fowler](https://martinfowler.com/eaaCatalog/registry.html)
- [Plugin Architecture](https://martinfowler.com/articles/osgi.html)
