---
title: "Hash Indexes: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate hash index concepts"
  - "Design shards and keys"
  - "Mitigate hot partitions"
prerequisites:
  []
knowledge_refs:
  - "patterns/hash-index"
---

# Hash Indexes: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A hash index is O(1) for? (A: ranges / B: exact equality / C: ordering)
- Q2: Consistent hashing makes resharding touch? (A: everything / B: a fraction / C: nothing)
- Q3: A hot key concentrates traffic on? (A: one partition / B: all partitions / C: the coordinator)
- Q4: True or false: hash indexes support range scans.
- Q5: Hash-range keys order by? (A: hash value / B: sort key / C: arrival time)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A chat archive stores 10B messages sharded by conversation. Design the hash-range schema and the hot-conversation mitigation.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why an index choice must follow the query shape, not convention.

## Key Takeaways

- Q1: B; Q2: B; Q3: A; Q4: false; Q5: B
- Hash for equality, B-tree for order
- Shard design is where hash indexes win or lose
