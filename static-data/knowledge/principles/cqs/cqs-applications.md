---
title: "CQS in Production: APIs and Services"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Map HTTP methods to commands and queries"
  - "Design services with explicit command and query interfaces"
  - "Use read models for query-heavy paths"
  - "Avoid hidden mutations in getters"
prerequisites:
  []
knowledge_refs:
  - "principles/cqs"
---

# CQS in Production: APIs and Services

## REST as CQS

REST already models the split: GET is a query (safe, idempotent), POST/PUT/DELETE are commands (mutating). Violations appear when a GET has side effects or a POST returns a big payload that should be a follow-up GET.

```text
REST as CQS:
  GET    /orders/123        -> query, no side effects
  POST   /orders            -> command, returns 201 + location
  DELETE /orders/123        -> command, returns 204
Anti-pattern: GET /orders/123/refresh  (mutation via GET)
Anti-pattern: POST /orders  returning the full rendered page
```

## Service-Level Split

Split service methods into CommandService and QueryService. Query methods can be cached, replicated, and read-replicas can serve them; command methods take the transactional, validated path. This is CQRS in miniature, without the event-sourcing ceremony.

## Practice: Refactor a REST API

POST /api/login both authenticates (mutation) and returns the full user profile with 20 fields.

**Task 1:** Redesign as POST /api/sessions returning only a token, plus GET /api/me for the profile.

**Task 2:** List every hidden side effect in your current GET endpoints.

**Task 3:** Decide which GET endpoints should serve from a read model and why.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why "GET that increments a counter" is a CQS violation and a caching hazard.

**Prompt 2 — Implementation Design:**
> Design the command/query split for a billing service: create-invoice (command), list-invoices (query), reconcile (command). Where do read replicas fit?

**Prompt 3 — Boundary Testing:**
> A command must return the ID of the created entity. How do you keep CQS clean? (return 201 + Location header, or a result record)

## Key Takeaways

- GET is query; POST/PUT/DELETE are commands
- Explicit command/query service interfaces scale reads
- Read models decouple query shape from write model
- Return identifiers and locations, not payloads, from commands

## Further Reading

- [REST API Design Best Practices](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)
- [CQRS Journey Guide](https://learn.microsoft.com/en-us/previous-versions/msp-n-p/jj554200(v=pandp.10))
