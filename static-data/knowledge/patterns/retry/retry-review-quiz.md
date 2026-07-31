---
title: "Retry: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate retry concepts"
  - "Design budgets and queues"
  - "Layer resilience"
prerequisites:
  []
knowledge_refs:
  - "patterns/retry"
---

# Retry: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Retry only? (A: transient failures / B: all failures / C: successes)
- Q2: Jitter prevents? (A: thundering herds / B: retries / C: caches)
- Q3: A retry budget caps? (A: the retry rate / B: the database / C: memory)
- Q4: True or false: poison messages belong in a dead-letter queue.
- Q5: A circuit breaker opens when? (A: failures exceed a threshold / B: it is bored / C: memory is full)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A partner API is flaky and expensive. Design the timeout, retry, breaker, budget, and DLQ story.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why retrying without a policy is how outages become multi-hour.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Retries recover transients; policy bounds the damage
- Breakers, budgets, and chaos complete the stack
