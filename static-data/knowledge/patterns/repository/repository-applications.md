---
title: "Repository in Production: ORMs and Data Mappers"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Combine repositories with ORMs"
  - "Design query objects"
  - "Separate write and read models"
  - "Avoid leaking the ORM"
prerequisites:
  []
knowledge_refs:
  - "patterns/repository"
---

# Repository in Production: ORMs and Data Mappers

## ORM Repositories

ORMs (Hibernate, TypeORM, Prisma) provide generic repositories, but generic CRUD leaks: filters and joins leak into the domain, and N+1 query patterns appear. The fix is a domain-specific repository per aggregate that owns its query shapes, plus explicit fetching policies inside the repository.

```typescript
// Domain repository over Prisma — the ORM stays inside
export class OrderRepository {
    constructor(private prisma: PrismaClient) {}

    async findOpenForCustomer(customerId: string): Promise<Order[]> {
        const rows = await this.prisma.order.findMany({
            where: { customerId, status: 'OPEN' },
            include: { items: true },      // fetch policy lives here
            orderBy: { createdAt: 'desc' },
        });
        return rows.map(Order.fromPrisma);
    }
    // No .findMany with raw filters escapes this class.
    // The domain never imports Prisma.
```

## Read Models

Writes go through repositories; heavy reports read through dedicated read models (views, projections, or a query service) that are shaped for the screen — no ORM graph walking. This is CQRS-lite: separate the write path from the read path so neither compromises the other.

## Practice: Harden the Repository

An order list screen triggers N+1 queries through the generic ORM repository.

**Task 1:** Replace the generic call with a domain repository that owns the include policy.

**Task 2:** Add the read model for the report screen.

**Task 3:** Measure the query count before and after.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why generic ORM repositories leak queries into the domain and how owning the shapes fixes it.

**Prompt 2 — Implementation Design:**
> Design a repository set for an e-commerce aggregate: order, customer, and the read model for dashboards.

**Prompt 3 — Boundary Testing:**
> A developer bypasses the repository with a direct ORM call. Design the architecture test that fails the build.

## Key Takeaways

- Domain-specific repositories own query shapes
- Fetch policies (includes) live inside the repository
- Read models serve reports without ORM walking
- Architecture tests stop repository bypasses

## Further Reading

- [CQRS — Martin Fowler](https://martinfowler.com/bliki/CQRS.html)
- [Prisma — data modeling](https://www.prisma.io/docs/concepts/components/prisma-schema/data-modeling)
