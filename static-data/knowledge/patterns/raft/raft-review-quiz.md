---
title: "Raft: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate Raft concepts"
  - "Operate clusters"
  - "Design membership"
prerequisites:
  []
knowledge_refs:
  - "patterns/raft"
---

# Raft: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Raft has the roles? (A: leader, follower, candidate / B: master, slave, proxy / C: writer, reader, cache)
- Q2: A log entry commits when? (A: a majority stores it / B: the leader stores it / C: everyone votes)
- Q3: A higher term? (A: fences the old leader / B: speeds writes / C: shrinks the log)
- Q4: True or false: Raft needs an odd number of nodes.
- Q5: Membership changes use? (A: joint consensus / B: a coin flip / C: DNS)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A config cluster must grow from 3 to 5 nodes live. Design the joint-consensus steps and the snapshot plan.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why Raft is Paxos restructured, not a new idea.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Explicit roles and terms make consensus implementable
- Safety is a matter of quorums and fencing
