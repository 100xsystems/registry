---
title: "Chain of Responsibility: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate chain concepts"
  - "Order handlers deliberately"
  - "Build dynamic chains"
prerequisites:
  []
knowledge_refs:
  - "patterns/chain-of-responsibility"
---

# Chain of Responsibility: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A handler that cannot process a request should? (A: pass it on / B: drop it / C: log and retry)
- Q2: Middleware that responds 401 is? (A: short-circuiting / B: passing / C: forking)
- Q3: The sender in a chain? (A: knows the handler / B: stays decoupled / C: must be a handler)
- Q4: True or false: middleware order is a security decision.
- Q5: Dynamic chains are assembled? (A: per request / B: once at boot / C: never)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> An approval chain for code deploys: lint, tests, security scan, human approval. Design the chain and the terminal handler.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why a chain with no terminal handler silently swallows work.

## Key Takeaways

- Q1: A; Q2: A; Q3: B; Q4: true; Q5: A
- Chains decouple requests from their processors
- Ordering and terminal handling are the safety rails
