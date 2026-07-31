---
title: "Advanced 2PC: Blocking, Recovery, and Alternatives"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Analyze the blocking problem"
  - "Design recovery protocols"
  - "Use presumed-commit/abort"
  - "Choose 2PC vs alternatives"
prerequisites:
  []
knowledge_refs:
  - "patterns/two-phase-commit"
---

# Advanced 2PC: Blocking, Recovery, and Alternatives

## Blocking and Recovery

The blocking problem: after a participant votes yes, it holds locks and waits for a decision that may never come (coordinator crash). Recovery protocols reconstruct the decision: participants contact the coordinator (or a replicated coordinator) whose durable log answers. Presumed-abort and presumed-commit are optimizations — abort unless told otherwise, or commit unless told otherwise — trading recovery complexity for fewer messages.

```text
Recovery and optimizations:
  Coordinator crash recovery:
    - coordinator persists each decision before sending it
    - participants in doubt ask the (new) coordinator
    - HA coordinator: the log replicates, a peer resumes
  Presumed abort:
    - if the decision log has no entry, presume ABORT
    - participants resolve doubt quickly; commit needs a log
  Presumed commit:
    - if the decision log has no entry, presume COMMIT
    - faster common case; dangerous if a no-vote was lost
  Participant crash recovery:
    - on restart, check its prepare log; if prepared, ask the
      coordinator for the decision; apply it (commit or rollback)
  Timeouts:
    - every phase has a deadline; timeout drives the recovery
      query, never a unilateral commit by the participant
```

## When Not to Use 2PC

2PC trades availability for atomicity. When participants are many, slow, or failure-prone — typical microservices — sagas and idempotent steps preserve availability with eventual consistency. Use 2PC across few, reliable, homogeneous participants (databases), not across dozens of services.

## Practice: Design the Recovery

A coordinator crashes between prepare and commit across three participants.

**Task 1:** Design the coordinator log and the participant doubt-resolution query.

**Task 2:** Compare presumed-abort vs presumed-commit for this workload.

**Task 3:** Design the timeout policy that bounds blocking.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain the blocking problem and how recovery resolves it.

**Prompt 2 — Implementation Design:**
> Design a presumed-abort 2PC coordinator with an HA log. What does a participant do when in doubt?

**Prompt 3 — Boundary Testing:**
> A no-vote is lost before reaching the coordinator. Design the safeguard that prevents a presumed-commit disaster.

## Key Takeaways

- Blocking is 2PC's core failure cost
- Durable coordinator logs enable recovery
- Presumed-abort/commit optimize recovery
- Choose sagas across many services; 2PC across few databases

## Further Reading

- [Consensus protocols — Kleppmann](https://martin.kleppmann.com/2016/02/08/is-there-any-hope-for-consensus.html)
- [2PC — Distributed Systems Reading Group](https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf)
