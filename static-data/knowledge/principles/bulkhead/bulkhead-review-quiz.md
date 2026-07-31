---
title: "Bulkheads: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate isolation concepts"
  - "Apply bulkhead reasoning to new systems"
  - "Spot shared-resource coupling quickly"
prerequisites:
  []
knowledge_refs:
  - "principles/bulkhead"
---

# Bulkheads: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A slow database exhausts the shared pool. What is the first symptom? (A: DB timeouts / B: HTTP timeouts across the service / C: cache miss)
- Q2: What does a semaphore do that a bounded queue does not? (A: fail fast / B: buffer / C: retry)
- Q3: Little's Law states concurrency = ? (A: rate × latency / B: rate / latency / C: latency / rate)
- Q4: True or false: a separate deployment is a valid, strong bulkhead.
- Q5: The strongest protection against a noisy tenant is? (A: bigger shared pool / B: per-tenant budget / C: retries)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A recommendation service OOMs during a spike and takes down the home page. Redesign with bulkheads so the home page serves without recommendations.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "we can just add more threads to the shared pool" is a trap, using a concrete failure story.

## Key Takeaways

- Q1: B; Q2: A; Q3: A; Q4: true; Q5: B
- Isolation is about containing, not preventing, failure
- Every compartment needs its own budget and fallback
