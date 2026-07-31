---
title: "Two-Phase Commit: Atomicity Across Systems"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the 2PC protocol"
  - "Describe the two phases"
  - "Understand the coordinator"
  - "Know the blocking problem"
prerequisites:
  - "principles/acid"
  - "patterns/saga"
knowledge_refs:
  - "patterns/two-phase-commit"
---

# Two-Phase Commit: Atomicity Across Systems

## The Protocol

A transaction spans two databases; each can commit or abort independently, but the business needs both or neither. 2PC adds a coordinator. Phase one (prepare): every participant prepares — writes its state so it can commit or roll back — and votes yes or no. Phase two (commit/abort): if all voted yes, the coordinator tells everyone to commit; if any voted no, everyone aborts. Atomicity through agreement.

```text
Two-phase commit:
  Phase 1 - Prepare:
    coordinator -> participant: "can you commit?"
    participant: writes prepare log, holds the locks
    participant -> coordinator: vote YES or NO
  Phase 2 - Decide:
    all YES  -> coordinator: "commit" (participants commit)
    any NO   -> coordinator: "abort"  (participants roll back)
  Participants:
    - never commit before the coordinator decides
    - once they vote YES, they MUST follow the decision
  The catch: while waiting for the decision, a participant
  holds its locks and stays available-but-blocked. If the
  coordinator dies mid-protocol, participants block until a
  new coordinator completes the decision — the blocking
  problem of 2PC.
```

## When It Works

2PC gives strong atomicity across participants — the reason it powers distributed databases and XA transactions. It works best when participants are few, reliable, and the coordinator is highly available. The cost: blocking on failures and coordination latency — which is why modern microservices prefer sagas and accept eventual consistency.

## Practice: Trace the Protocol

A transfer moves money from Bank A to Bank B — two databases, one transaction.

**Task 1:** Trace prepare, votes, and commit on the happy path.

**Task 2:** Trace an abort when Bank B votes no.

**Task 3:** Describe what happens if the coordinator dies after the first YES.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why participants must follow the decision after voting yes.

**Prompt 2 — Compare & Contrast:**
> Compare 2PC with saga: atomicity and blocking vs eventual consistency and availability.

**Prompt 3 — Boundary Testing:**
> A participant votes yes then crashes before committing. Design the recovery that completes the decision.

## Key Takeaways

- 2PC coordinates atomic commit across participants
- Prepare-then-decide with a coordinator
- Once yes, a participant must follow the decision
- Blocking on coordinator failure is the known cost

## Further Reading

- [Two-phase commit — Wikipedia](https://en.wikipedia.org/wiki/Two-phase_commit_protocol)
- [Distributed Transactions — Martin Kleppmann](https://martin.kleppmann.com/2016/02/08/is-there-any-hope-for-consensus.html)
