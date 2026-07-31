---
title: "Advanced Chain: Dynamic and Concurrent Chains"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Reconfigure chains at runtime"
  - "Handle async and parallel chains"
  - "Design branching (fork/join) chains"
  - "Keep chains observable"
prerequisites:
  []
knowledge_refs:
  - "patterns/chain-of-responsibility"
---

# Advanced Chain: Dynamic and Concurrent Chains

## Dynamic Chains

When handler sets change at runtime (feature flags, tenant configs), build the chain from a registry at request time instead of wiring it statically. The registry maps conditions to handler lists.

```go
// Dynamic chain: assembled per request from a registry
func chainFor(r *Request) []Handler {
    var chain []Handler
    for _, h := range registry.all() {
        if h.appliesTo(r) {      // tenant/flag/route aware
            chain = append(chain, h)
        }
    }
    return chain
}

// Each request walks its own chain; flags flip chains live,
// no redeploy needed for handler selection changes.
```

## Async and Fork/Join

Handlers may be async (each awaits the next) and chains may fork: a request fans out to parallel chains and joins at a barrier. The pattern still holds — each stage passes or handles — but concurrency and ordering guarantees become explicit design decisions.

## Practice: Design the Dynamic Chain

Tenants configure their own processing pipeline: some add GDPR scrub, some add audit.

**Task 1:** Design the registry and the per-tenant chain assembly.

**Task 2:** Add async handlers and the join semantics for parallel branches.

**Task 3:** Design the tracing: a chain ID on every log line so handlers are attributable.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain the difference between a static chain and a per-request assembled one.

**Prompt 2 — Implementation Design:**
> Design a per-tenant data pipeline chain with fork/join and failure isolation. What happens when one branch fails?

**Prompt 3 — Boundary Testing:**
> A flag flips mid-request and the chain changes. Design the snapshot semantics (use the chain you started with).

## Key Takeaways

- Registries enable per-request chain assembly
- Async handlers make chains concurrent
- Fork/join needs explicit join semantics
- Chain IDs make async chains traceable

## Further Reading

- [Middleware as a Chain — Go net/http](https://pkg.go.dev/net/http)
- [Pipeline Pattern — Go Concurrency](https://go.dev/blog/pipelines)
