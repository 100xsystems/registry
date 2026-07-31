---
title: "Advanced Decorator: Dynamic and Transactional Wrapping"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Assemble decorator stacks dynamically"
  - "Wrap transactions and sessions"
  - "Manage decorator state and identity"
  - "Avoid decorator over-wrapping"
prerequisites:
  []
knowledge_refs:
  - "patterns/decorator"
---

# Advanced Decorator: Dynamic and Transactional Wrapping

## Dynamic Stacks

Feature flags and tenant configs can assemble different decorator stacks per request: tenant A gets caching + metrics, tenant B gets metrics only. A stack factory builds the chain per context at the composition root.

```python
# Dynamic stack assembly per tenant
def build_repo(tenant):
    repo = DbUserRepo()
    if tenant.cache_enabled:
        repo = CacheDecorator(repo)
    if tenant.trace_enabled:
        repo = TraceDecorator(repo)
    repo = MetricsDecorator(repo)     # metrics always
    return repo

# Flags change stacks live without touching callers.
```

## Transactional Decorators

A transactional decorator wraps a method so it joins or starts a transaction, commits on success, rolls back on failure — leaving the business method free of transaction code. Nested decorators must cooperate (join the outer transaction, not nest blindly).

## Practice: Design the Dynamic Stack

A multi-tenant repo with per-tenant caching and tracing flags.

**Task 1:** Build the stack factory keyed by tenant config.

**Task 2:** Add the transactional decorator with correct join semantics.

**Task 3:** Design the identity problem: a decorated object compared by identity breaks. Document the fix (compare by interface semantics).

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why transactional decorators must join, not nest.

**Prompt 2 — Implementation Design:**
> Design a session decorator that opens, commits, and closes around a unit of work. Where does it sit in the stack?

**Prompt 3 — Boundary Testing:**
> Ten decorators deep hides a buggy middle layer. Design the observability (stack trace per layer) that finds it.

## Key Takeaways

- Stack factories assemble decorators per context
- Transactional decorators must join, not nest
- Identity comparisons break under wrapping
- Observable layers keep deep stacks debuggable

## Further Reading

- [Spring @Transactional (the classic transactional decorator)](https://docs.spring.io/spring-framework/reference/data-access/transaction/)
- [Decorator — Refactoring Guru](https://refactoring.guru/design-patterns/decorator)
