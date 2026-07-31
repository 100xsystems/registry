---
title: "Consistent Hashing: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate ring concepts"
  - "Design shard maps"
  - "Handle load and churn"
prerequisites:
  []
knowledge_refs:
  - "patterns/consistent-hashing"
---

# Consistent Hashing: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Adding a node under consistent hashing moves? (A: all keys / B: neighbor keys only / C: nothing)
- Q2: Virtual nodes fix? (A: load skew / B: latency / C: memory)
- Q3: Naive hash(key) % N breaks when? (A: N changes / B: N is prime / C: keys are strings)
- Q4: True or false: consistent hashing is used for session affinity.
- Q5: Bounded-load hashing guarantees? (A: per-node load caps / B: zero movement / C: exact balance)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A cache cluster of 10 nodes must scale to 12 without a hit-ratio collapse. Design the ring, the warm-up, and the load cap.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why hash % N is dangerous in production and what replaces it.

## Key Takeaways

- Q1: B; Q2: A; Q3: A; Q4: true; Q5: A
- The ring makes membership changes cheap
- Bounded loads and DHTs extend it to hard cases
