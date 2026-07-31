---
title: "Bloom Filters: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate bloom filter concepts"
  - "Tune filters for workloads"
  - "Design scalable membership"
prerequisites:
  []
knowledge_refs:
  - "patterns/bloom-filter"
---

# Bloom Filters: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A bloom filter never produces? (A: false positives / B: false negatives / C: collisions)
- Q2: The optimal hash count is? (A: (m/n) ln 2 / B: m / C: k=1)
- Q3: The valuable answer a bloom filter gives is? (A: definitely present / B: definitely absent / C: exact count)
- Q4: True or false: counting filters support deletion.
- Q5: Plain bloom filters merge via? (A: bitwise OR / B: addition / C: XOR)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A URL crawler must not revisit 1B URLs with 200MB of memory. Design the filter and the false-positive policy.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "sometimes says yes" is a feature, not a bug.

## Key Takeaways

- Q1: B; Q2: A; Q3: B; Q4: true; Q5: A
- Probabilistic membership trades exactness for space
- No false negatives is the superpower
