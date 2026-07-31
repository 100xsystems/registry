---
title: "Idempotency: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate idempotency concepts"
  - "Design key stores and lifecycles"
  - "Build idempotent pipelines"
prerequisites:
  []
knowledge_refs:
  - "principles/idempotency"
---

# Idempotency: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Which HTTP method is NOT idempotent by default? (A: PUT / B: POST / C: DELETE)
- Q2: The idempotency store prevents duplicates via? (A: TTL / B: unique key / C: retries)
- Q3: Exactly-once delivery really means? (A: at-least-once + idempotent processing / B: no retries / C: no failures)
- Q4: True or false: an upsert is naturally idempotent.
- Q5: Same key + different request should return? (A: 200 / B: 409 / C: retry)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A mobile app submits an order and the connection drops; the retry must not double-charge. Design the client key generation, server store, and retention.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why idempotency is a contract between the retrier and the retried.

## Key Takeaways

- Q1: B; Q2: B; Q3: A; Q4: true; Q5: B
- Idempotency is the foundation of safe retries
- Design data models to be idempotent by construction
