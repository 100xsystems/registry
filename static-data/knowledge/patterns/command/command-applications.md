---
title: "Command in Production: Jobs and Transactions"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Model jobs as commands"
  - "Make commands idempotent and retryable"
  - "Build multi-step workflows from commands"
  - "Persist command history"
prerequisites:
  []
knowledge_refs:
  - "patterns/command"
---

# Command in Production: Jobs and Transactions

## Jobs as Commands

A job queue is a queue of command objects: serialize the command (type + params), enqueue it, and a worker deserializes and executes. Retries re-enqueue the same command — idempotency keys keep replays safe.

```text
Job queue as commands:
  enqueue(ResizeImage{ path, size })   -> JSON {type, params}
  worker: deserialize -> execute -> mark done
  failure: re-enqueue with backoff (same command, idempotent)

Transactional commands:
  a command executes and its effects commit atomically;
  a compensating command (undo) rolls back on failure.
```

## Workflows

A workflow is a sequence of commands with state: each step enqueues the next. Sagas are workflows of commands with compensating undos — the command pattern is the unit that makes orchestration and rollback possible.

## Practice: Design the Job Queue

A media pipeline: upload, transcode, thumbnail, publish — each a job with retries.

**Task 1:** Define the four commands and their serialization.

**Task 2:** Make each command idempotent (re-running is safe).

**Task 3:** Design the failure path: retries, dead-letter, and the compensating command for a partial publish.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why idempotency keys make re-enqueued commands safe. Ask me to trace a double-execution.

**Prompt 2 — Implementation Design:**
> Design a saga as a chain of commands with compensations. What happens at each failure point?

**Prompt 3 — Boundary Testing:**
> A worker crashes mid-command. Design the recovery: how does the queue know the command state?

## Key Takeaways

- Job queues are command queues
- Commands must be idempotent for safe replays
- Workflows and sagas compose commands
- Compensating commands implement undo at scale

## Further Reading

- [Saga Pattern — Microservices.io](https://microservices.io/patterns/data/saga.html)
- [Transactional Outbox](https://microservices.io/patterns/data/transactional-outbox.html)
