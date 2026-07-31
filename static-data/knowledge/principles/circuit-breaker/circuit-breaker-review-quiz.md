---
title: "Circuit Breakers: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate breaker concepts"
  - "Tune breakers for real failure modes"
  - "Design effective fallbacks"
prerequisites:
  []
knowledge_refs:
  - "principles/circuit-breaker"
---

# Circuit Breakers: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: In OPEN state, calls to the dependency? (A: proceed / B: fail fast / C: retry 3x)
- Q2: HALF_OPEN means? (A: probing recovery / B: permanently closed / C: degraded mode)
- Q3: minimumNumberOfCalls prevents? (A: flapping on a blip / B: slow starts / C: timeouts)
- Q4: True or false: a breaker opens based on status codes only.
- Q5: The user-visible contract of a breaker is its? (A: thresholds / B: fallback / C: timeout)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A dependency returns 500s for 2 minutes then recovers. Design a breaker that opens, probes once at 30s, and recovers without a stampede. What does the user see at each stage?

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why a 30s timeout alone is not enough to protect a system, using a thread-exhaustion cascade story.

## Key Takeaways

- Q1: B; Q2: A; Q3: A; Q4: false; Q5: B
- Breakers convert slow cascades into fast, bounded failures
- Health signals and fallbacks determine real resilience
