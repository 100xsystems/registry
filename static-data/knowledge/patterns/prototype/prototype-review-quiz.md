---
title: "Prototype: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate prototype concepts"
  - "Choose copy depth"
  - "Design versioned clones"
prerequisites:
  []
knowledge_refs:
  - "patterns/prototype"
---

# Prototype: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Prototype creates objects by? (A: cloning / B: constructing / C: injecting)
- Q2: Shallow copy? (A: shares references / B: copies everything / C: deletes)
- Q3: Cyclic graphs break naive copy without? (A: a visited map / B: a cache / C: a compiler)
- Q4: True or false: structural sharing makes clone O(log n).
- Q5: Copy-on-write defers the copy until? (A: mutation / B: read / C: garbage collection)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A config system clones a heavy graph 1000x per deploy. Design the clone strategy and the version chain.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why copying the whole object is not the only way to get a new one.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Clone with intent: depth, identity, and sharing
- Structural sharing turns cloning into versioning
