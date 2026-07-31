---
title: "Advanced Fanout: Hybrid and Adaptive Fanout"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Design hybrid fanout with pull fallback"
  - "Adapt fanout to reader activity"
  - "Fan out across regions"
  - "Avoid fanout storms"
prerequisites:
  []
knowledge_refs:
  - "patterns/fanout"
---

# Advanced Fanout: Hybrid and Adaptive Fanout

## Hybrid Fanout

The production shape: push to active readers (small inboxes), pull for inactive and long-tail users, with a merge on read. Activity-based classification decides who gets pushed — usually a recency threshold (active in N days).

```text
Hybrid fanout algorithm:
  author posts post P
  for each follower F:
    if active(F): push P into F.inbox     # small set, fast
    else:         append P to F.pending    # lazy, merged on read
  read(F): merge(F.inbox, F.pending, author timelines)

  Adaptive: an inactive user who reads becomes active -> start pushing.
  A user inactive for 90 days stops receiving pushes.
```

## Regional and Storm Control

Cross-region fanout replicates the write, not a million messages: the post travels once; each region fans out locally. Storm control: fanout jobs are bounded (batches, queues), backpressure on the writer, and shedding of the lowest-priority destinations under load.

## Practice: Design the Hybrid Fanout

A video platform: 10M followers total, 5% active daily.

**Task 1:** Design the active/inactive split and the threshold.

**Task 2:** Design the merge-on-read for pull users.

**Task 3:** Design the regional replication and the fanout job's backpressure and shedding.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why hybrid fanout is the standard production answer.

**Prompt 2 — Implementation Design:**
> Design the fanout job with batch processing and backpressure: how does it survive a 10M-follower post?

**Prompt 3 — Boundary Testing:**
> A follower list changes mid-fanout. Design the snapshot semantics (fan out to the follower set at publish time).

## Key Takeaways

- Hybrid = push active + pull long tail
- Activity thresholds drive the split
- Regional fanout replicates once, fans out locally
- Bounded jobs and backpressure prevent storms

## Further Reading

- [Timeline Architecture (System Design)](https://github.com/donnemartin/system-design-primer#design-a-social-media-feed)
- [Batching at Scale — Google SRE](https://sre.google/sre-book/)
