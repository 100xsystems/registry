---
title: "Single Responsibility: One Reason to Change"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define single responsibility precisely"
  - "Identify multiple responsibilities in a class"
  - "Explain the \"reasons to change\" test"
  - "Refactor a multi-job class"
prerequisites:
  - "principles/separation-of-concerns"
  - "principles/information-hiding"
knowledge_refs:
  - "principles/single-responsibility"
---

# Single Responsibility: One Reason to Change

## The Principle

Single responsibility (SRP): a class should have one, and only one, reason to change. A class that parses, validates, persists, and emails has four reasons to change — a schema change, a validation rule change, an email template change each touch the same class, and they fight for it.

The test: name the actor who asks for a change. If you can name two different actors who would change this class for different reasons, split it.

```java
// Multiple responsibilities: parsing, validation, persistence, email
class OrderService {
    Order parse(String raw) { ... }
    void validate(Order o) { ... }
    void save(Order o) { ... }
    void sendConfirmation(Order o) { ... }
}

// One responsibility each:
class OrderParser      { Order parse(String raw) { ... } }
class OrderValidator   { void validate(Order o) { ... } }
class OrderRepository  { void save(Order o) { ... } }
class OrderMailer      { void sendConfirmation(Order o) { ... } }
```

## Responsibility vs Single Method

SRP is not "one method per class" — a class can have many methods serving one responsibility (a repository with find/create/delete serves persistence). The unit is the reason to change, not the line count.

## Practice: Split the God Class

A UserManager with 200 lines handling auth, profile, notifications, and audit.

**Task 1:** List the reasons to change and their actors (security team, product, compliance).

**Task 2:** Split into role-focused classes with clear ownership.

**Task 3:** Show how a security change now touches only the auth class.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the "reasons to change" test. Start with a class you know with many jobs.

**Prompt 2 — Compare & Contrast:**
> Compare SRP with separation of concerns. How are they the same idea at different scales?

**Prompt 3 — Boundary Testing:**
> Two responsibilities are so small that splitting creates five tiny classes. Design the judgment call: when is a class "one responsibility" despite doing several small things?

## Key Takeaways

- One reason to change per class
- Different actors mean different responsibilities
- SRP is about the unit of change, not line count
- Splitting isolates change and testing

## Further Reading

- [Single Responsibility Principle — Wikipedia](https://en.wikipedia.org/wiki/Single-responsibility_principle)
- [SOLID — Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html)
