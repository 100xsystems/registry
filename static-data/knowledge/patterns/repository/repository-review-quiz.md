---
title: "Repository: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate repository concepts"
  - "Design interfaces"
  - "Compose queries"
prerequisites:
  []
knowledge_refs:
  - "patterns/repository"
---

# Repository: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A repository presents? (A: a collection-like interface / B: SQL directly / C: the cache)
- Q2: A DAO exposes? (A: table-shaped operations / B: domain language / C: the UI)
- Q3: Domain code should depend on? (A: the repository interface / B: the database driver / C: the ORM)
- Q4: True or false: specifications compose like predicates.
- Q5: A data mapper keeps? (A: domain and schema decoupled / B: one object / C: the DB busy)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> An order service with 30 ad-hoc queries needs a clean persistence boundary. Design the repository set and the test fakes.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why the database should be the last thing the domain knows about.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- The repository is the domain's door to storage
- Own your query shapes or they leak everywhere
