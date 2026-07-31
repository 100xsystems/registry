---
title: "Optimistic Locking: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate locking concepts"
  - "Design version guards and retries"
  - "Choose escalation strategies"
prerequisites:
  []
knowledge_refs:
  - "principles/optimistic-locking"
---

# Optimistic Locking: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Optimistic locking detects conflicts? (A: at write time / B: before reads / C: never)
- Q2: The conflict detector is usually? (A: a version / B: a lock / C: a queue)
- Q3: MVCC lets readers? (A: block writers / B: read a snapshot / C: lock rows)
- Q4: True or false: retries should re-read the fresh version.
- Q5: Hot rows under optimistic locking cause? (A: retry churn / B: less work / C: no effect)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> An e-commerce cart merges concurrent edits from two tabs. Design the version guard, the conflict UX, and the retry path.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "just update the row" silently loses data without a version guard.

## Key Takeaways

- Q1: A; Q2: A; Q3: B; Q4: true; Q5: A
- Optimistic locking scales reads, retries on conflict
- Escalate to atomic ops or CRDTs when conflicts dominate
