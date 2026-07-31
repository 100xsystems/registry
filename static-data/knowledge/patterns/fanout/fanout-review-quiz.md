---
title: "Fanout: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate fanout concepts"
  - "Design feed fanout"
  - "Handle scale and failure"
prerequisites:
  []
knowledge_refs:
  - "patterns/fanout"
---

# Fanout: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Push fanout makes reads? (A: instant / B: slow / C: impossible)
- Q2: Pull fanout makes writes? (A: light / B: heavy / C: nil)
- Q3: In Kafka, each consumer group reads? (A: all messages / B: one message / C: nothing)
- Q4: True or false: one slow fanout destination should block the broadcast.
- Q5: Hybrid fanout pushes to? (A: active readers / B: everyone / C: nobody)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A messaging platform must deliver a viral post to 5M followers under 5s. Design the fanout: push/pull split, batching, regional, and the failure budgets.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why a million-inbox write needs fanout design, not a for loop.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: false; Q5: A
- Fanout is write-amplification vs read-latency
- Hybrid and partitioned fanout handle the scale
