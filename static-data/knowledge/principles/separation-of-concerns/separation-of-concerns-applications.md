---
title: "Separation of Concerns in Production: Layers and Modules"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design clean layer boundaries"
  - "Handle cross-cutting concerns without entanglement"
  - "Prevent layer violations"
  - "Keep modules independent"
prerequisites:
  []
knowledge_refs:
  - "principles/separation-of-concerns"
---

# Separation of Concerns in Production: Layers and Modules

## Cross-Cutting Concerns

Logging, auth, metrics, and error handling touch every layer. Entangling them into every function is duplication; the answer is middleware, decorators, or AOP that wrap the flow once. The concern stays separated — implemented once, applied everywhere.

```typescript
// Cross-cutting concern via middleware: auth applied once
app.use('/api', authenticate);          // auth concern, one place
app.use('/api', logRequest);            // observability, one place
app.use('/api', errorBoundary);         // error handling, one place

// Handlers stay focused on business logic only:
app.get('/orders/:id', (req, res) => {
    const order = orders.get(req.params.id);
    res.json(order.toDto());
});
```

## Enforcing Boundaries

Layers decay without enforcement: a controller that queries the database directly is a layering violation that grows. Enforce with architecture tests (import rules), package visibility, and code review — same discipline as dependency inversion.

## Practice: Audit the Layers

A service where controllers query the DB, domain objects know the ORM, and email is sent from the repository.

**Task 1:** Map every violation: where does each layer reach into another?

**Task 2:** Refactor to clean boundaries (controller -> service -> repository -> infra).

**Task 3:** Add the architecture test that fails on future violations.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why cross-cutting concerns should be applied once by middleware rather than repeated everywhere. Ask me to list the repeats in a typical handler.

**Prompt 2 — Implementation Design:**
> Design the middleware chain for a checkout API: auth, rate limit, validation, logging, error handling. What order, and why?

**Prompt 3 — Boundary Testing:**
> A legitimate query must read from a read replica — a layering exception. Design the boundary that allows it without opening the floodgates.

## Key Takeaways

- Layers separate the what from the where
- Cross-cutting concerns belong in middleware, once
- Boundaries need enforcement (tests, visibility)
- Exceptions must be deliberate and narrow

## Further Reading

- [Clean Architecture — Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Layered Architecture — Microsoft Docs](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures)
