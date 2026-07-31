---
title: "LSM Trees: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate LSM concepts"
  - "Tune engines"
  - "Choose compaction"
prerequisites:
  []
knowledge_refs:
  - "patterns/lsm-tree"
---

# LSM Trees: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: LSM turns random writes into? (A: sequential appends / B: in-place updates / C: deletes)
- Q2: The in-memory write buffer is the? (A: memtable / B: SSTable / C: WAL)
- Q3: Bloom filters make point reads? (A: skip files / B: slower / C: impossible)
- Q4: True or false: leveled compaction has predictable reads.
- Q5: After a crash, the memtable is recovered from? (A: the WAL / B: compaction / C: the network)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A chat history store writes 50k msgs/s, reads conversations. Design the LSM layout, compaction, and bloom settings.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why LSM trades read cost for write speed and how bloom filters pay it back.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Write-optimized by design; reads tuned with filters
- Compaction strategy is the main dial
