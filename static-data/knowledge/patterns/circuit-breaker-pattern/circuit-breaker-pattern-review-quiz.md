---
title: "Circuit Breaker (Pattern): Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate breaker concepts"
  - "Tune for real failure modes"
  - "Design probing and fallbacks"
prerequisites:
  []
knowledge_refs:
  - "patterns/circuit-breaker-pattern"
---

# Circuit Breaker (Pattern): Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: In OPEN state, calls? (A: proceed / B: fail fast / C: queue)
- Q2: HALF_OPEN allows? (A: a probe call / B: all traffic / C: nothing)
- Q3: minimumNumberOfCalls prevents? (A: flapping / B: timeouts / C: caching)
- Q4: True or false: a breaker only reacts to HTTP status codes.
- Q5: The user-visible contract of a breaker is its? (A: fallback / B: threshold / C: timeout)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A provider fails for 2 minutes then recovers. Design the breaker timeline: open, probe at 30s, ramp, and what users see at each stage.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why timeouts alone cannot prevent cascading failures.

## Key Takeaways

- Q1: B; Q2: A; Q3: A; Q4: false; Q5: A
- Breakers convert slow cascades into fast, bounded failures
- Signals, probes, and fallbacks make them production-safe
