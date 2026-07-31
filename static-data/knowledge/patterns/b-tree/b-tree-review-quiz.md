---
title: "B-Trees: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate B-tree concepts"
  - "Design composite indexes"
  - "Choose engines"
prerequisites:
  []
knowledge_refs:
  - "patterns/b-tree"
---

# B-Trees: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: B-trees beat binary trees on disk because of? (A: branching factor / B: smaller data / C: caching)
- Q2: Range scans are supported because B-trees? (A: keep keys sorted / B: hash keys / C: compress data)
- Q3: A composite index (a, b, c) is useless for a filter on? (A: a / B: b alone / C: a and b)
- Q4: True or false: an index-only scan avoids reading the table.
- Q5: LSM-trees optimize? (A: reads / B: writes / C: memory)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A chat app stores messages by conversation. Design the B-tree index for "latest 50 messages of conversation X" and explain the page reads.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "add an index" needs a query-shape analysis first.

## Key Takeaways

- Q1: A; Q2: A; Q3: B; Q4: true; Q5: B
- B-trees are the read-optimized default
- Index design follows query shapes
