---
title: "Interface Segregation: Fat Interfaces Hurt Callers"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "State the interface segregation principle"
  - "Recognize fat interfaces and their costs"
  - "Split interfaces by client need"
  - "Apply ISP to classes and modules"
prerequisites:
  - "principles/single-responsibility"
  - "principles/information-hiding"
knowledge_refs:
  - "principles/interface-segregation"
---

# Interface Segregation: Fat Interfaces Hurt Callers

## The Principle

Interface Segregation (ISP): no client should be forced to depend on methods it does not use. A fat interface — read, write, delete, audit, export, render — forces every implementer to provide everything, and every change to any method ripples through all implementers and callers.

The fix is small, role-specific interfaces: a Reader, a Writer, a Deleter. Each client depends only on the interface it actually uses.

```java
// Fat interface: every implementer must do everything
interface OrderService {
    Order get(long id);
    void create(Order o);
    void update(Order o);
    void delete(long id);
    byte[] exportCsv(List<Long> ids);
}

// Segregated by role:
interface OrderReader  { Order get(long id); }
interface OrderWriter  { void create(Order o); void update(Order o); }
interface OrderDeleter { void delete(long id); }
interface OrderExporter { byte[] exportCsv(List<Long> ids); }

// A read-only view implements only OrderReader.
```

## Costs of Fat Interfaces

Implementers stub unused methods (UnsupportedOperationException), callers compile against methods they never use (and depend on their stability), and the interface becomes a coupling hub that changes constantly. Small interfaces change rarely because they encode one role.

## Practice: Split the Monolith Interface

A UserService interface has 12 methods: auth, profile, admin, reporting, and billing concerns.

**Task 1:** Group the methods into role interfaces by consumer (auth client, admin panel, billing).

**Task 2:** Refactor the admin panel to depend only on its role interface.

**Task 3:** Show how adding a method to one role interface no longer affects other consumers.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the difference between a fat interface and a cohesive one. Start with how clients group methods.

**Prompt 2 — Compare & Contrast:**
> Compare ISP with single responsibility and role interfaces (Role Interface pattern). How do they reinforce each other?

**Prompt 3 — Boundary Testing:**
> Two clients genuinely share 80% of an interface's methods. Design the split that does not multiply interfaces pointlessly.

## Key Takeaways

- Clients should depend only on interfaces they use
- Fat interfaces couple implementers and callers together
- Role interfaces change rarely and independently
- Group by consumer, not by shared implementation

## Further Reading

- [Interface Segregation Principle — Wikipedia](https://en.wikipedia.org/wiki/Interface_segregation_principle)
- [Role Interface — Martin Fowler](https://martinfowler.com/bliki/RoleInterface.html)
