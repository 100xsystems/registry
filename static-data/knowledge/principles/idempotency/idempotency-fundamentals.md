---
title: "Idempotency: Safe to Repeat"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define idempotent and non-idempotent operations"
  - "Explain why retries need idempotency"
  - "Recognize idempotent HTTP methods"
  - "Make a non-idempotent operation idempotent"
prerequisites:
  - "principles/fail-fast"
  - "principles/eventual-consistency"
knowledge_refs:
  - "principles/idempotency"
---

# Idempotency: Safe to Repeat

## The Definition

An operation is idempotent if applying it multiple times has the same effect as applying it once. DELETE /orders/123 is idempotent (the order is gone either way); POST /orders is not (each POST creates another order).

Idempotency is what makes retries safe. Without it, "retry after timeout" can mean "charge the customer twice".

```http
Idempotent HTTP methods:
  GET, HEAD, PUT, DELETE, OPTIONS  -> safe to repeat
  POST, PATCH                      -> NOT idempotent by default

Fix: add an Idempotency-Key header on POSTs
  POST /orders
  Idempotency-Key: c9d3-4410-9a1f
Retrying with the same key returns the same order, never a duplicate.
```

## Why It Matters

Networks fail, clients time out, servers crash mid-request, retries happen. Every one of those is a chance for a duplicated side effect. Idempotency converts "I do not know if it happened" into "it does not matter — the result is the same".

## Practice: Classify the Operations

Classify each as idempotent or not: set the user's name, increment a counter, add an item to a cart, refund a charge, send an email.

**Task 1:** Justify each classification with the "run twice" test.

**Task 2:** For the non-idempotent ones, design the fix (idempotency key, natural key, upsert).

**Task 3:** Explain why "add to cart" repeated twice must be a cart with two items — and how the client prevents accidental doubles.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why idempotency keys must be unique per logical operation and stable across retries.

**Prompt 2 — Compare & Contrast:**
> Compare idempotency keys, unique constraints, and upserts. When is each the right mechanism for "no duplicates"?

**Prompt 3 — Boundary Testing:**
> A client retries with a new key by mistake. Design the server behavior that still prevents duplicates (natural-key uniqueness as backstop).

## Key Takeaways

- Idempotent = repeated application, same result
- Retries without idempotency duplicate side effects
- Idempotency keys on POSTs make them repeatable
- Unique constraints backstop accidental key drift

## Further Reading

- [Idempotency — Stripe API Guide](https://stripe.com/docs/api/idempotent_requests)
- [Idempotency Key Spec — IETF Draft](https://datatracker.ietf.org/doc/html/draft-ietf-httpapi-idempotency-key-header)
