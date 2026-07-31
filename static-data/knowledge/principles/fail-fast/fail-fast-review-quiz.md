---
title: "Fail Fast: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate fail-fast concepts"
  - "Design pipeline and runtime gates"
  - "Propagate deadlines correctly"
prerequisites:
  []
knowledge_refs:
  - "principles/fail-fast"
---

# Fail Fast: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Fail fast means failures are? (A: hidden / B: surfaced early and loudly / C: retried forever)
- Q2: The best place to catch a config bug is? (A: production at 2am / B: startup validation / C: user reports)
- Q3: A propagated deadline ensures? (A: total latency stays bounded / B: no failures / C: infinite retries)
- Q4: True or false: silent sanitization of invalid input is a form of fail-fast.
- Q5: When saturated, new work should? (A: queue forever / B: fail fast with a clear status / C: drop silently)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A misconfigured service deploys and breaks 3% of checkouts. Design the canary, alert, and rollback that catch it in minutes.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why the debugging distance between a bug and its symptom is the real cost of failing late.

## Key Takeaways

- Q1: B; Q2: B; Q3: A; Q4: false; Q5: B
- Fail at the earliest, loudest, cheapest point
- Deadlines and cancellation bound the blast radius
