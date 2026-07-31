---
title: "Chain of Responsibility in Production: Middleware"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design middleware chains"
  - "Short-circuit with early responses"
  - "Order middleware deliberately"
  - "Test chains in isolation and end-to-end"
prerequisites:
  []
knowledge_refs:
  - "patterns/chain-of-responsibility"
---

# Chain of Responsibility in Production: Middleware

## HTTP Middleware

Express/Koa/Rails middleware are chains: each middleware can handle (respond), pass to the next, or modify the request as it flows. Auth middleware short-circuits with 401 before the handler runs; logging middleware always passes.

```typescript
// Middleware chain: each piece passes or short-circuits
app.use('/api', auth);          // 401 if no token, else pass
app.use('/api', rateLimit);     // 429 if over limit, else pass
app.use('/api', validateBody);  // 400 if invalid, else pass
app.use('/api', cacheHit);      // serve cached if present, else pass
app.get('/api/orders/:id', handler);  // last in the chain

// Order matters: auth before rate limit, validation before handler.
```

## Chain Testing

Each middleware is tested in isolation (pass, handle, short-circuit), and the full chain is tested for order effects: a middleware that must run before another is verified with an ordering test.

## Practice: Design the API Chain

An API needs auth, tenant-scoping, rate limiting, caching, and audit — in the right order.

**Task 1:** Decide the order and justify each adjacency (why auth before tenant?).

**Task 2:** Implement short-circuit paths (401, 403, 429, cache hit).

**Task 3:** Write an ordering test that fails if auth runs after tenant-scoping.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why middleware order is a security decision, not just style. Ask me to order a chain with a reason for each pair.

**Prompt 2 — Implementation Design:**
> Design an event-preprocessing chain: validate, enrich, dedupe, route. What passes, what short-circuits?

**Prompt 3 — Boundary Testing:**
> Two middlewares both want to respond (cache hit and audit). Design the priority rule.

## Key Takeaways

- Middleware chains pass or short-circuit
- Order is a security and correctness decision
- Isolation tests plus ordering tests cover chains
- Terminal handlers respond when nothing else does

## Further Reading

- [Express Middleware](https://expressjs.com/en/guide/using-middleware.html)
- [Rack Middleware (Ruby)](https://github.com/rack/rack)
