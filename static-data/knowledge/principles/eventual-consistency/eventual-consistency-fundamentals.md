---
title: "Eventual Consistency: Converging Without Coordination"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define eventual consistency precisely"
  - "Explain why it enables availability and low latency"
  - "List convergence mechanisms: propagation, retries, CRDTs"
  - "Describe user-visible staleness windows"
prerequisites:
  - "principles/base"
  - "principles/consistency-pattern"
knowledge_refs:
  - "principles/eventual-consistency"
---

# Eventual Consistency: Converging Without Coordination

## The Definition

Eventual consistency: if no new writes occur to a replicated item, all replicas will eventually converge to the same value. The window of divergence is unbounded in theory but bounded in practice by propagation time and retry behavior.

The guarantee is weak on purpose: it lets replicas serve reads and accept writes independently, which is what keeps the system available during partitions and fast in normal operation.

```text
Eventual consistency timeline:
  t0: client writes v2 to replica A
  t1: replica B still serves v1 (stale read)
  t2: propagation delivers v2 to B
  t3: B serves v2 (converged)
Convergence is guaranteed only after writes stop.
```

## Where It Is Safe

Eventual consistency fits data where transient divergence is invisible or acceptable: like counts, presence, feeds, recommendations, session caches. It is dangerous for balances, inventory, and uniqueness constraints.

## Practice: Map the Staleness Window

A social app replicates posts across 3 regions with async propagation (~200ms).

**Task 1:** Describe the worst-case staleness for a reader in region C when a post is written in region A.

**Task 2:** Identify which features break visibly (read-your-writes for the author) and design the session affinity fix.

**Task 3:** List three data types that must NOT be eventually consistent here.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why "eventual" has no time bound and how systems bound it in practice. Start with propagation.

**Prompt 2 — Compare & Contrast:**
> Compare eventual consistency with causal consistency and read-your-writes. Which user bugs does each one eliminate?

**Prompt 3 — Boundary Testing:**
> A like counter converges eventually, but a viral post gets 10k likes/min. Describe the convergence lag and whether users notice.

## Key Takeaways

- Eventual means converges when writes stop
- It buys availability and low write latency
- Staleness is bounded by propagation, not by promise
- Match data types to the guarantee they can tolerate

## Further Reading

- [Eventually Consistent — Werner Vogels](https://www.allthingsdistributed.com/2008/12/eventually_consistent.html)
- [Cassandra Consistency Levels](https://docs.datastax.com/en/cassandra-oss/3.x/cassandra/dml/dmlConfigConsistency.html)
