---
title: "Sharding: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate sharding concepts"
  - "Choose keys and layouts"
  - "Plan resharding"
prerequisites:
  []
knowledge_refs:
  - "patterns/sharding"
---

# Sharding: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Sharding scales? (A: capacity / B: availability only / C: the frontend)
- Q2: The shard key decides? (A: distribution and routing / B: compression / C: indexing)
- Q3: Range sharding fits? (A: time-series / B: random access / C: graphs)
- Q4: True or false: resharding is a rehearsed migration.
- Q5: A hot shard is caused by? (A: a skewed key / B: too many shards / C: caching)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A 20B-row events table must scale and support tenant time-range queries. Design the key, the layout, and the growth plan.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why the shard key is the most important decision in the database.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Keys, layout, and rebalancing define sharding success
- Resharding is the migration you rehearse
