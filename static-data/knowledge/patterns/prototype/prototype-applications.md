---
title: "Prototype in Production: Serialization and Deep Copy"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Clone via serialization"
  - "Apply copy-on-write"
  - "Handle cycles and identity"
  - "Use registries safely"
prerequisites:
  []
knowledge_refs:
  - "patterns/prototype"
---

# Prototype in Production: Serialization and Deep Copy

## Serialization Cloning

Deep cloning through serialization — object -> bytes -> object — works for arbitrary graphs but is slow and has identity surprises: the clone is a new identity even for values that were shared. Copy-on-write defers the copy: clones share until one mutates, which is how persistent structures and COW filesystems amortize cloning.

```python
# Deep clone via serialization (pickle) — simple but slow
import copy

original = load_expensive_graph()
deep = copy.deepcopy(original)      # full graph copy

# Copy-on-write alternative: share until mutation
class CowNode:
    def __init__(self, shared_ref=None):
        self._ref = shared_ref      # shared until written
        self._owned = None
    def mutate(self, value):
        if self._owned is None:
            self._owned = deepcopy(self._ref)   # copy now, once
        self._owned.value = value
# Many readers share; the first writer pays the copy.
# This is how COW snapshots and persistent structures work.
```

## Cycles and Identity

Cyclic graphs break naive recursive copy — you need a visited map or a serialization format that handles references. Identity matters when the clone must preserve shared sub-objects (the graph stays a graph) vs duplicating them. Prototype registries must be careful: a mutated template clones wrong by default.

## Practice: Design the Clone Strategy

A configuration graph has shared nodes, cycles, and immutable leaves; it is cloned 1,000 times per deploy.

**Task 1:** Clone with a visited map to preserve the graph shape.

**Task 2:** Add copy-on-write for the hot path and measure the savings.

**Task 3:** Guard the registry: freeze templates after registration.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why cycles break naive deep copy and how a visited map fixes it.

**Prompt 2 — Implementation Design:**
> Design a COW document model: shared immutable history, copy on edit. How do versions stay cheap?

**Prompt 3 — Boundary Testing:**
> A registered template is mutated after cloning begins. Design the freeze-and-version that makes clones deterministic.

## Key Takeaways

- Serialization cloning is simple but slow
- Copy-on-write defers copy until mutation
- Cycles need visited maps; identity must be defined
- Registries must freeze or version templates

## Further Reading

- [Copy-on-write — Wikipedia](https://en.wikipedia.org/wiki/Copy-on-write)
- [Python — copy module docs](https://docs.python.org/3/library/copy.html)
