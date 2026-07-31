---
title: "Composite: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate composite concepts"
  - "Design tree structures"
  - "Choose traversal strategies"
prerequisites:
  []
knowledge_refs:
  - "patterns/composite"
---

# Composite: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Composite treats leaves and groups? (A: uniformly / B: differently / C: never)
- Q2: Operations on composites? (A: recurse / B: loop / C: fail)
- Q3: A DOM is an example of? (A: composite / B: singleton / C: memento)
- Q4: True or false: a leaf's add() should be meaningful.
- Q5: The visitor pattern is useful for? (A: many ops on stable nodes / B: many nodes with stable ops / C: caching)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A permissions model: a role contains users and other roles. Design the composite and the hasPermission() recursion with cycle protection.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why caller branching on "is this a folder?" defeats the pattern.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: false; Q5: A
- Part-whole trees share one interface
- Visitors and iterators keep traversal clean
