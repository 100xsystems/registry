---
title: "CQRS: Separate Commands from Queries"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the CQRS intent"
  - "Separate command and query models"
  - "Understand when the split pays off"
  - "Compare with CQS at the method level"
prerequisites:
  - "principles/cqs"
  - "patterns/repository"
knowledge_refs:
  - "patterns/cqrs"
---

# CQRS: Separate Commands from Queries

## The Idea

CQRS splits the data path: commands (writes) go to a transactional write model; queries (reads) are served by optimized read models. They may even be different databases — the write model normalized, the read model denormalized for the exact query shapes.

The cost is eventual consistency between the models, so CQRS pays off when reads and writes have sharply different shapes, volumes, or scaling needs.

```text
CQRS topology:
  POST /orders   -> CommandService -> write model (normalized, transactional)
  OrderCreated   -> event -> projector -> read model (denormalized)
  GET /orders    -> QueryService  -> read model (fast, query-shaped)

  Consistency: eventual between write model and read model.
  Payoff: scale reads independently; shape reads for the UI.
```

## CQS vs CQRS

CQS is method-level: commands return nothing, queries mutate nothing. CQRS is architecture-level: commands and queries have separate models, stores, and often separate services. CQRS is CQS taken to the data-model scale.

## Practice: Split the Models

An orders service: writes are complex; the dashboard queries aggregate by region and status.

**Task 1:** Design the command model (normalized, transactional).

**Task 2:** Design the read model (denormalized dashboard rows).

**Task 3:** Decide the synchronization: synchronous projection or event-driven, and the lag each accepts.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why CQRS trades consistency for read/write independence. Start with the projection lag.

**Prompt 2 — Compare & Contrast:**
> Compare CQRS with a plain repository over one database. What concrete problem does the split solve?

**Prompt 3 — Boundary Testing:**
> A user reads a just-created order and the read model lags. Design the read-your-writes path.

## Key Takeaways

- Commands and queries get separate models
- Read models are shaped for query patterns
- Consistency between models is eventual
- CQRS pays off when read/write shapes diverge

## Further Reading

- [CQRS — Martin Fowler](https://martinfowler.com/bliki/CQRS.html)
- [CQRS Journey — Microsoft](https://learn.microsoft.com/en-us/previous-versions/msp-n-p/jj554200(v=pandp.10))
