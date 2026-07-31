---
title: "Graceful Degradation: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate degradation concepts"
  - "Design fallback chains"
  - "Communicate degraded states honestly"
prerequisites:
  []
knowledge_refs:
  - "principles/graceful-degradation"
---

# Graceful Degradation: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Graceful degradation turns a full outage into? (A: a silent error / B: a partial, honest state / C: a retry loop)
- Q2: The first tier in a fallback chain is? (A: static defaults / B: live data / C: stale cache)
- Q3: Fallbacks can become the new outage if? (A: uncapped / B: cached / C: tested)
- Q4: True or false: degraded states should be invisible to users.
- Q5: Adaptive quality means? (A: fixed fallback / B: quality adjusts to load / C: always full quality)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A payment provider outage hits at 2am. Design the degraded checkout, the queued-payment reconciliation, and the morning recovery runbook.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "hide the broken widget" is degradation but "return 200 with wrong data" is not.

## Key Takeaways

- Q1: B; Q2: B; Q3: A; Q4: false; Q5: B
- Degradation must be honest and capacity-planned
- Quality ladders extend degradation to the premium path
