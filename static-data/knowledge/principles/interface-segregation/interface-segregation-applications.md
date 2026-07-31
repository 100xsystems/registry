---
title: "Interface Segregation in Production: APIs and Services"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Segregate service interfaces by consumer"
  - "Design consumer-specific DTOs"
  - "Use capability views for role-based access"
  - "Manage API evolution with segregation"
prerequisites:
  []
knowledge_refs:
  - "principles/interface-segregation"
---

# Interface Segregation in Production: APIs and Services

## Consumer-Specific DTOs

A single fat response DTO forces every consumer to receive (and depend on) fields they do not use — and leaks data they should not see. Consumer-specific DTOs (or field projections) give each caller exactly the shape it needs.

```typescript
// Fat DTO: every consumer gets everything
interface UserResponse { id, email, passwordHash, ssn, admin, creditCard, ... }

// Segregated DTOs per consumer
interface ProfileResponse { id, name, avatar }        // public profile
interface AdminUserView  { id, email, admin, status } // admin panel
interface BillingView    { id, creditCardLast4 }      // billing

// The endpoint projects the source entity into the consumer's shape.
```

## Role-Based Views

Segregation doubles as a security tool: the admin-only fields simply do not exist in the public interface. This is "principle of least privilege" applied to data shapes — the code cannot leak a field it does not expose.

## Practice: Project the Shapes

A single /users/:id returns 25 fields to everyone, including internal flags.

**Task 1:** List the consumer groups and the exact fields each needs.

**Task 2:** Define the DTOs and the projection logic from the source entity.

**Task 3:** Remove the internal flags from the public path and add a test that they never serialize.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why fat response DTOs are a security and coupling problem, not just a style issue.

**Prompt 2 — Implementation Design:**
> Design the read-model split for a user service: profile, admin, billing, analytics views over one source of truth.

**Prompt 3 — Boundary Testing:**
> A new consumer needs 3 more fields. Design the evolution path that does not fatten the shared DTO.

## Key Takeaways

- DTOs should be shaped per consumer
- Segregation enforces least-privilege data exposure
- Projections keep one source of truth with many views
- New consumers get new views, not fatter ones

## Further Reading

- [DTO vs View Models — Martin Fowler](https://martinfowler.com/eaaCatalog/dataTransferObject.html)
- [GraphQL: ask for exactly what you need](https://graphql.org/learn/queries/)
