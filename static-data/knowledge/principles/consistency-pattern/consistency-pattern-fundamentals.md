---
title: "Consistency Patterns: From Strong to Eventual"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Order consistency levels from strong to eventual"
  - "Define strong, causal, and eventual consistency"
  - "Map workloads to appropriate consistency levels"
  - "Explain the cost of stronger guarantees"
prerequisites:
  - "principles/cap-theorem"
  - "principles/eventual-consistency"
knowledge_refs:
  - "principles/consistency-pattern"
---

# Consistency Patterns: From Strong to Eventual

## The Consistency Spectrum

Consistency is not binary. From strongest to weakest: linearizable (strong), sequential, causal, read-your-writes / monotonic reads, and eventual. Each step down buys availability and latency; each step up buys predictability.

Strong consistency means every read sees the latest committed write, as if there were a single copy. It costs: writes must synchronize across replicas before returning.

```text
Consistency spectrum (strong -> weak):
  Linearizable   : reads see latest write, real-time ordered
  Sequential     : operations ordered, no real-time guarantee
  Causal         : causally related writes seen in order
  Read-your-writes: you always see your own writes
  Monotonic reads: reads never go backwards in time
  Eventual       : replicas converge given quiet time
```

## Choosing a Guarantee

The rule: match the guarantee to the failure cost. Money and inventory need strong or quorum consistency. Feeds, counters, and profiles tolerate eventual consistency with bounded staleness.

Most systems use a mix — strong for the critical path, eventual for the rest — rather than one global setting.

## Practice: Assign Guarantees

For each operation pick a consistency level: withdraw cash, show friend count, post a comment, decrement stock, show chat typing indicator.

**Task 1:** Justify each choice with the worst-case user-visible failure.

**Task 2:** For stock decrement, explain why two concurrent decrements must not oversell.

**Task 3:** Design read-your-writes for the comment system so the author sees their own post instantly.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the cost difference between strong and eventual consistency in a multi-region setup. Start with write latency.

**Prompt 2 — Compare & Contrast:**
> Compare linearizable, causal, and eventual consistency in a collaborative editing app. Which guarantee does each CRDT provide?

**Prompt 3 — Boundary Testing:**
> A system needs strong consistency only for a single key (balance). Design a hybrid that is strong for that key and eventual for everything else.

## Key Takeaways

- Consistency is a spectrum, not a binary
- Strong guarantees cost latency and availability
- Match the guarantee to the failure cost per data path
- Hybrid systems mix levels by key or operation

## Further Reading

- [Consistency Models — Jepsen](https://jepsen.io/consistency)
- [CAP Twelve Years Later](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)
