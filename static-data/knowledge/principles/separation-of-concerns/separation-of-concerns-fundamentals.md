---
title: "Separation of Concerns: One Job per Part"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define separation of concerns"
  - "Identify entangled concerns in code"
  - "Split mixed responsibilities"
  - "Explain the benefit for testing and reuse"
prerequisites:
  - "principles/single-responsibility"
  - "principles/information-hiding"
knowledge_refs:
  - "principles/separation-of-concerns"
---

# Separation of Concerns: One Job per Part

## The Principle

Separation of concerns (Dijkstra): a system is easier to understand, test, and change when each part addresses one concern. A request handler should not also contain SQL, validation, email logic, and retry policy — each concern deserves its own place.

The payoff: each piece can be tested in isolation, reused independently, and changed without touching the others. Entangled code changes ripple in every direction.

```python
# Entangled: handler, validation, persistence, email all in one function
def signup(request):
    # validate + persist + send email + log — four concerns, one place

# Separated:
def signup(request):
    data = validate(request.body)         # validation concern
    user = users.create(data)             # persistence concern
    email.send_welcome(user)              # notification concern
    logger.info('signup', user_id=user.id)  # observability concern
    return user
# Each concern is a function with its own tests.
```

## Concerns vs Layers

Concerns are the "what" (validation, persistence, presentation); layers are the "where" (API, domain, infrastructure). Separation applies at both: a domain object should not know how it is stored, and an HTTP handler should not know the business rules inside the domain.

## Practice: Untangle the Handler

A 200-line handler validates, queries, formats, emails, and retries — all inline.

**Task 1:** List the concerns tangled in the handler.

**Task 2:** Extract each into its own module/function with a test.

**Task 3:** Show how the extracted validation is now reusable by another endpoint.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the difference between separation of concerns and just "smaller functions". Start with what a concern is.

**Prompt 2 — Compare & Contrast:**
> Compare separation of concerns with single responsibility and layering. Where do they overlap?

**Prompt 3 — Boundary Testing:**
> Two concerns are tightly coupled by performance (validation must happen in the SQL for speed). Design the boundary that keeps them conceptually separate.

## Key Takeaways

- Each part should address one concern
- Entangled code changes ripple everywhere
- Separation enables isolation, reuse, and testing
- Boundaries are conceptual before they are physical

## Further Reading

- [Separation of Concerns — Wikipedia](https://en.wikipedia.org/wiki/Separation_of_concerns)
- [AOP and Cross-Cutting Concerns](https://en.wikipedia.org/wiki/Cross-cutting_concern)
