---
title: "Consistency Patterns: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate consistency concepts"
  - "Apply guarantees to workloads"
  - "Spot consistency anti-patterns"
prerequisites:
  []
knowledge_refs:
  - "principles/consistency-pattern"
---

# Consistency Patterns: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: The strongest consistency level is? (A: eventual / B: linearizable / C: causal)
- Q2: W+R>N guarantees? (A: serializability / B: read sees latest write / C: no conflicts)
- Q3: Vector clocks detect? (A: latency / B: causality / C: partitions)
- Q4: True or false: stronger consistency always costs availability during partitions.
- Q5: A chat reply appearing before its parent message is a violation of? (A: causality / B: durability / C: idempotency)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A distributed ledger needs strict ordering for transfers but tolerates lag for balance displays. Design the consistency split and justify with failure costs.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why eventual consistency is not "wrong" but a deliberate, bounded trade-off.

## Key Takeaways

- Q1: B; Q2: B; Q3: B; Q4: true; Q5: A
- Consistency guarantees are per-path contracts
- The cheapest guarantee that meets the failure cost is the right one
