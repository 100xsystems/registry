---
title: "BASE: Eventually Consistent Distributed Systems"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Deconstruct the BASE acronym into its three properties"
  - "Contrast BASE with ACID across real workloads"
  - "Recognize where eventual consistency is safe"
  - "Trace a read-your-writes violation scenario"
prerequisites:
  - "principles/acid"
  - "principles/eventual-consistency"
knowledge_refs:
  - "principles/base"
---

# BASE: Eventually Consistent Distributed Systems

## What BASE Actually Means

BASE stands for Basically Available, Soft state, Eventual consistency. It is the pragmatic counterweight to ACID: instead of guaranteeing consistency at every instant, the system guarantees the data will converge — eventually — while staying available.

Basically Available means the system responds to every request, even if the answer is slightly stale. Soft state means replicas may be out of sync at any moment. Eventual consistency means that, given enough time without new writes, all replicas converge to the same value.

```text
# The BASE contract in one sentence per property
Basically Available : every request gets a response (maybe stale)
Soft state          : replicas may diverge between writes
Eventual consistency: given quiet time, replicas converge
```

## BASE vs ACID

ACID optimizes for correctness under failure; BASE optimizes for availability and latency under scale. A bank ledger must be ACID; a social feed can be BASE.

The choice is not either/or — most production systems are a blend: ACID for the money path, BASE for the recommendation path.

## Practice: Choose the Right Consistency Contract

For each service below, decide ACID or BASE and justify in one sentence: a shopping cart, a like counter, a banking balance, a search index, a chat presence indicator.

**Task 1:** For the like counter, design a system where the count may briefly show 1,004 instead of 1,003. What convergence mechanism fixes it?

**Task 2:** For the banking balance, explain what breaks if you store it in a BASE store.

**Task 3:** Draw the read-your-writes violation: user writes a post on replica A, reads on replica B, and does not see it. How long until it appears?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about when a distributed system can be BASE for reads but ACID for writes. Start with the write path.

**Prompt 2 — Compare & Contrast:**
> Compare the eventual-consistency guarantees of DynamoDB (multi-AZ, strong by default) versus Cassandra (tunable, eventual by default). When is each the right call?

**Prompt 3 — Boundary Testing:**
> A BASE system serves a decrement of an inventory count. The request succeeds but the write is lost. Design a compensation mechanism that does not reintroduce a hot single-writer bottleneck.

## Key Takeaways

- BASE trades strict consistency for availability and low latency
- Soft state means replicas are allowed to diverge
- Eventual consistency requires convergence, not just availability
- Real systems mix ACID and BASE per data path

## Further Reading

- [Dynamo: Amazon's Highly Available Key-value Store](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)
- [CAP Theorem Explained](https://www.ibm.com/topics/cap-theorem)
