---
title: "Advanced Repository: Specifications and Data Mappers"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Design specification objects"
  - "Build composable queries"
  - "Map between models cleanly"
  - "Handle transactions and units of work"
prerequisites:
  []
knowledge_refs:
  - "patterns/repository"
---

# Advanced Repository: Specifications and Data Mappers

## Specifications

When repository methods multiply (findActive, findActiveInCity, findActiveInCityAfter), a specification object captures the predicate as data: repository.find(spec). Specifications compose (AND, OR, NOT) and translate to SQL or to in-memory filters — the same object works for query and test.

```java
// Specification: predicates as data, composable
interface Spec<T> { boolean isSatisfiedBy(T t); }
class And<T> implements Spec<T> {
    private final Spec<T> a, b;
    And(Spec<T> a, Spec<T> b) { this.a = a; this.b = b; }
    public boolean isSatisfiedBy(T t) { return a.isSatisfiedBy(t) && b.isSatisfiedBy(t); }
}

class CustomerIsActive implements Spec<Customer> {
    public boolean isSatisfiedBy(Customer c) { return c.isActive(); }
}
class CustomerInCity implements Spec<Customer> {
    private final String city;
    CustomerInCity(String city) { this.city = city; }
    public boolean isSatisfiedBy(Customer c) { return c.city().equals(city); }
}
// repository.find(new And<>(new CustomerIsActive(), new CustomerInCity("NY")))
// The same Spec predicates drive the SQL translation (via a mapper)
// and the in-memory filter — one definition, two engines.
```

## Data Mappers

A data mapper transfers between the domain model and the database schema without either knowing the other — unlike active record, where the domain object carries its own persistence. Mappers enable rich domains at the cost of a translation layer that must stay explicit and tested.

## Practice: Compose the Query

A report screen needs 12 filter combinations over customers; the repository methods multiply.

**Task 1:** Define the specification objects and the compositions.

**Task 2:** Translate the specs to SQL and verify the generated queries.

**Task 3:** Use the same specs in memory for the test fake.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why specifications stop repository-method explosion.

**Prompt 2 — Implementation Design:**
> Design a filter UI backed by specifications: how do checkbox states become a composed query?

**Prompt 3 — Boundary Testing:**
> A spec translates to SQL that is 10x slower than a hand-written query. Design the plan inspection or the query-object escape hatch.

## Key Takeaways

- Specifications compose predicates as data
- One spec drives SQL and in-memory filters
- Data mappers decouple domain from schema
- Query complexity needs escape hatches

## Further Reading

- [Specification — Martin Fowler](https://martinfowler.com/apsupp/spec.pdf)
- [Data Mapper — P of EAA](https://martinfowler.com/eaaCatalog/dataMapper.html)
