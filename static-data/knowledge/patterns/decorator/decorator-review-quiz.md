---
title: "Decorator: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate decorator concepts"
  - "Compose behavior stacks"
  - "Choose stack order"
prerequisites:
  []
knowledge_refs:
  - "patterns/decorator"
---

# Decorator: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A decorator? (A: wraps and adds behavior / B: changes the interface / C: creates objects)
- Q2: Decorators beat inheritance for? (A: combinations / B: speed / C: memory)
- Q3: Stack order matters because it? (A: changes behavior / B: never matters / C: is cosmetic)
- Q4: True or false: decorators must preserve the interface.
- Q5: An adapter differs from a decorator by? (A: changing the interface / B: adding behavior / C: being faster)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> An HTTP client needs logging, retry, and timeout decorators. Stack them, justify the order, and show the undecorated test version.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why decorators keep cross-cutting code out of business classes.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Decorators compose behavior at runtime
- Order, identity, and observability are the care points
