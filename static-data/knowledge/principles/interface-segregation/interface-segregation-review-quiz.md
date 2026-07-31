---
title: "Interface Segregation: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate ISP concepts"
  - "Split interfaces by consumer"
  - "Apply segregation to data exposure"
prerequisites:
  []
knowledge_refs:
  - "principles/interface-segregation"
---

# Interface Segregation: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A fat interface forces implementers to? (A: implement everything / B: hide everything / C: ignore methods)
- Q2: Role interfaces group methods by? (A: implementation / B: consumer role / C: database table)
- Q3: Consumer-specific DTOs prevent? (A: duplication / B: leaking unused fields / C: caching)
- Q4: True or false: implicit interfaces (Go) make segregation easier.
- Q5: The main cost of a fat interface is? (A: coupling / B: performance / C: memory)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A shared library interface has 18 methods used by 5 apps, each using 4-6. Plan the role split and the migration that breaks nothing.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "one interface for everything" feels convenient now and costs you every change later.

## Key Takeaways

- Q1: A; Q2: B; Q3: B; Q4: true; Q5: A
- Segregation is coupling control at the interface level
- Narrow interfaces change rarely and safely
