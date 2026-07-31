---
title: "Throttling: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate throttling concepts"
  - "Design throttle and backoff"
  - "Apply fair adaptive throttling"
prerequisites:
  []
knowledge_refs:
  - "principles/throttling"
---

# Throttling: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Throttling differs from rate limiting by? (A: slowing instead of capping / B: stopping traffic / C: no difference)
- Q2: Backoff jitter prevents? (A: retry storms / B: latency / C: caching)
- Q3: AIMD stands for? (A: additive increase, multiplicative decrease / B: always increase, mostly decrease / C: a new metric)
- Q4: True or false: a fixed throttle rate needs no tuning.
- Q5: Fair throttling protects? (A: the noisiest consumer / B: quiet consumers / C: the edge)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A data pipeline's consumer is throttling against a fluctuating API. Design the adaptive fair throttle and the escalation to shedding.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "just add a sleep" and "just retry harder" are both wrong throttling.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: false; Q5: B
- Throttling shapes flow; backoff coordinates it
- Adaptive and fair variants make it production-safe
