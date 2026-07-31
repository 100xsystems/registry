---
title: "Gossip: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate gossip concepts"
  - "Choose dissemination strategies"
  - "Design reconciliation"
prerequisites:
  []
knowledge_refs:
  - "patterns/gossip"
---

# Gossip: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Gossip spreads state? (A: via a coordinator / B: via random peer exchange / C: via a tree)
- Q2: The fastest-converging exchange style is? (A: push / B: pull / C: push-pull)
- Q3: SWIM marks a node dead only after? (A: one ping / B: suspicion + confirmation / C: admin action)
- Q4: True or false: hinted handoff keeps writes available during a partition.
- Q5: Anti-entropy uses? (A: Merkle trees / B: full copies / C: FTP)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A 500-node fleet loses 5 nodes during an upgrade. Design the gossip membership and reconciliation that keeps the fleet healthy.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why a coordinator-free epidemic protocol is more robust but eventually consistent.

## Key Takeaways

- Q1: B; Q2: C; Q3: B; Q4: true; Q5: A
- Gossip is self-healing and coordinator-free
- Suspicion, hints, and anti-entropy keep it convergent
