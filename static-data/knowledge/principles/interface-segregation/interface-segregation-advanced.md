---
title: "Advanced Interface Segregation: Role Interfaces and Adapters"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Apply role interface patterns at module scale"
  - "Segregate adapters from core ports"
  - "Design stable interfaces under growth"
  - "Detect fat interfaces with tooling"
prerequisites:
  []
knowledge_refs:
  - "principles/interface-segregation"
---

# Advanced Interface Segregation: Role Interfaces and Adapters

## Role Interfaces at Scale

A module that plays many roles (a user is a reader, a writer, an admin) should expose role interfaces, not one god interface. Callers depend on the role, and a type can implement several roles without any caller seeing methods it does not use.

```go
// Go: interfaces are implicitly implemented — segregation is natural
type Reader interface { Get(id string) (*User, error) }
type Writer interface { Create(u *User) error; Update(u *User) error }
type Admin   interface { Delete(id string) error }

// The service implements all three; callers take only what they need
func handlePublic(r Reader) { /* only Get */ }
func handleAdmin(a Admin)   { /* only Delete */ }

// Fat-interface detection: an interface with many methods that
// callers use sparsely is a segregation violation waiting to happen.
```

## Adapter Segregation

Adapters (HTTP, SQL, queue) should implement narrow ports rather than one adapter that does everything. A Postgres adapter that implements read, write, delete, audit, and export is a fat adapter — split it so each port has a focused implementation, testable in isolation.

## Practice: Detect and Split

A repository interface has 15 methods used by 6 different services.

**Task 1:** Measure per-method usage across services to find the fat core.

**Task 2:** Split into role ports (reader, writer, deleter, auditor) and adapters.

**Task 3:** Add a lint/architecture check that flags interfaces used by disjoint consumers.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why implicit interfaces (Go) make segregation free while explicit ones (Java) require discipline.

**Prompt 2 — Implementation Design:**
> Design the port split for an event bus used by producers, consumers, and administrators. What roles exist, and what does each port promise?

**Prompt 3 — Boundary Testing:**
> Two role interfaces share a method that now changes semantics. Where does the change land, and who is affected?

## Key Takeaways

- Role interfaces let types play many roles cleanly
- Adapters should be narrow and focused
- Implicit interfaces reduce segregation friction
- Tooling can detect fat interfaces before they hurt

## Further Reading

- [Role Interface — Martin Fowler](https://martinfowler.com/bliki/RoleInterface.html)
- [Go: Interfaces and Composition](https://go.dev/doc/effective_go#interfaces)
