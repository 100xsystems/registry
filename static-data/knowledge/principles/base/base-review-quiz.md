---
title: "BASE: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate the BASE mental model"
  - "Apply convergence reasoning to new systems"
  - "Spot anti-patterns in eventually consistent designs"
prerequisites:
  []
knowledge_refs:
  - "principles/base"
---

# BASE: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A BASE system must guarantee what about requests? (A: strong consistency / B: a response / C: serializability)
- Q2: Which of these is NOT a BASE property? (A: basically available / B: soft state / C: two-phase commit)
- Q3: A G-Counter merge uses which operation per slot? (A: sum / B: max / C: min)
- Q4: True or false: a TTL cache is a form of eventual consistency.
- Q5: An OR-Set prevents which failure mode? (A: lost updates / B: resurrection / C: deadlock)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A gaming leaderboard shows top-100 with slight lag. Users complain their rank is wrong. Redesign to make ranks converge within 5 seconds without a global lock.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "just use ACID everywhere" is not an option at global scale, using concrete latency and availability numbers.

## Key Takeaways

- Q1: B; Q2: C; Q3: B; Q4: true; Q5: B
- BASE is a contract about availability and eventual convergence
- Convergence mechanisms must be deterministic and idempotent
