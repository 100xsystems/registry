---
title: "Repository: Abstract the Data Layer"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the repository intent"
  - "Hide query details"
  - "Return domain objects"
  - "Test with fakes"
prerequisites:
  - "principles/dependency-inversion"
  - "patterns/factory"
knowledge_refs:
  - "patterns/repository"
---

# Repository: Abstract the Data Layer

## The Problem

Domain code that runs SQL directly couples business logic to the database and makes testing slow. The repository presents a collection-like interface — find(id), add(entity), remove(entity) — and hides the persistence technology behind it. The domain depends on the interface; the adapter depends on the database.

```typescript
// Repository: the domain sees a collection, not a database
interface OrderRepository {
    findById(id: string): Order | null;
    findByCustomer(customerId: string): Order[];
    add(order: Order): void;
    remove(order: Order): void;
}

// Production adapter: SQL under the interface
class PostgresOrderRepository implements OrderRepository {
    constructor(private db: Pool) {}
    async findById(id: string) {
        const row = await this.db.query(
            'SELECT * FROM orders WHERE id = $1', [id]);
        return row.rows[0] ? Order.fromRow(row.rows[0]) : null;
    }
    // add/remove translate to INSERT/DELETE here
}

// The domain uses the interface; tests use an in-memory fake.
```

## Repository vs DAO

A DAO (data access object) exposes table-shaped operations: findById, insert — close to SQL. A repository speaks the domain language: findOpenOrdersFor(customer) — it returns domain objects and encapsulates the query policy. Repositories sit above DAOs and are the domain-facing contract.

## Practice: Wrap the Database

An order service queries SQL in 30 places; tests hit a real database.

**Task 1:** Define the repository interface in domain terms.

**Task 2:** Implement the Postgres adapter and the in-memory fake.

**Task 3:** Migrate the 30 call sites and run the tests against the fake.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why the repository speaks the domain language rather than SQL. Start with the method names.

**Prompt 2 — Compare & Contrast:**
> Compare repository with DAO and with the unit-of-work pattern. What does each layer own?

**Prompt 3 — Boundary Testing:**
> A query needs a paginated, filtered shape. Design the repository method or the specification object that keeps the interface domain-friendly.

## Key Takeaways

- Repository hides persistence behind a collection interface
- It returns domain objects and speaks domain language
- The domain depends on the interface, never the DB
- Fakes make tests fast and deterministic

## Further Reading

- [Repository — Martin Fowler (P of EAA)](https://martinfowler.com/eaaCatalog/repository.html)
- [Repository pattern — Microsoft](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-design)
