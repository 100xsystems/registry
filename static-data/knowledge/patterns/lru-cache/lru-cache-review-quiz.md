---
title: "LRU Cache: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate LRU concepts"
  - "Tune eviction policies"
  - "Design scan resistance"
prerequisites:
  []
knowledge_refs:
  - "patterns/lru-cache"
---

# LRU Cache: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: LRU evicts? (A: the least-recently-used / B: the oldest inserted / C: the smallest)
- Q2: O(1) LRU needs? (A: hash + list / B: array only / C: a database)
- Q3: A full scan workload causes LRU to? (A: thrash / B: shine / C: compress)
- Q4: True or false: LFU can keep a once-hot key forever.
- Q5: Two-tier LRU resists? (A: scan poisoning / B: disk full / C: network loss)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A recommendation feed cache serves 99% of traffic but a crawler sweeps it hourly. Design the policy that keeps the hot set.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why eviction policy is a product decision, not just plumbing.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- LRU assumes locality; adapt when the workload does not
- Eviction policy shapes user-visible latency
