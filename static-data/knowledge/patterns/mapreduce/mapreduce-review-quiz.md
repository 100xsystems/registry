---
title: "MapReduce: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate map-reduce concepts"
  - "Tune jobs"
  - "Design incremental pipelines"
prerequisites:
  []
knowledge_refs:
  - "patterns/mapreduce"
---

# MapReduce: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Map and reduce must be? (A: pure / B: stateful / C: interactive)
- Q2: The shuffle phase? (A: groups by key / B: sorts by size / C: drops data)
- Q3: A combiner runs? (A: on the map side / B: on the client / C: in the DB)
- Q4: True or false: one dominant key overloads a single reducer.
- Q5: Iterative algorithms stay fast with? (A: caching / B: re-reading / C: compression)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A daily user-activity rollup of 50B events has celebrity users. Design the job: combiner, salting, and the merge pass.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why pure functions are what make a 10,000-machine job recoverable.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Map-reduce is divide-and-conquer batch done right
- Purity, skew, and iteration define the hard parts
