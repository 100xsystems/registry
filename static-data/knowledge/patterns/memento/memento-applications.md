---
title: "Memento in Production: Checkpoints and Serialization"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design checkpoint-based recovery"
  - "Serialize snapshots durably"
  - "Restore workflow state"
  - "Manage snapshot size"
prerequisites:
  []
knowledge_refs:
  - "patterns/memento"
---

# Memento in Production: Checkpoints and Serialization

## Checkpoints

Systems checkpoint periodically: serialize a consistent state to durable storage so recovery starts from the checkpoint plus the log since it. Streaming engines checkpoint offsets and state to Kafka; databases checkpoint the WAL. The memento is the design: the originator (the engine) knows its own state layout.

```python
# Checkpoint + log replay: recovery from the snapshot
class Processor:
    def __init__(self):
        self.state = {}
        self.log = []                     # operations since checkpoint
        self.checkpoint = None            # last durable snapshot

    def apply(self, op):
        self.state[op.key] = op.value
        self.log.append(op)

    def checkpoint_now(self):
        self.checkpoint = dump(self.state)   # serialized memento
        self.log = []                        # log restarts from here

    def recover(self):
        if self.checkpoint is not None:
            self.state = load(self.checkpoint)   # restore
        for op in self.log:                      # replay the tail
            self.apply(op)
```

## Workflow State

Long-running workflows serialize their state between steps so a crash resumes exactly where it stopped. Temporal stores the workflow state and events; each step is a checkpoint. Snapshot size is the dial: full snapshots are simple but heavy, incremental snapshots (diff against the last) are lighter but need the base.

## Practice: Design the Checkpointing

A stream processor must resume exactly-once after crashes, checkpointing every 10 seconds.

**Task 1:** Design the snapshot format and the checkpoint trigger.

**Task 2:** Design recovery: snapshot + log replay, exactly-once.

**Task 3:** Compare full vs incremental snapshots for a 10GB state.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why checkpoint plus replay beats replay-from-the-beginning.

**Prompt 2 — Implementation Design:**
> Design a workflow engine checkpoint: what is stored, when, and how a mid-step crash resumes.

**Prompt 3 — Boundary Testing:**
> A checkpoint is corrupted on disk. Design the validation (checksums) and the fallback to the previous checkpoint.

## Key Takeaways

- Checkpoints make recovery replay only the tail
- The originator owns the snapshot format
- Workflow steps are natural checkpoints
- Snapshot size drives full vs incremental choice

## Further Reading

- [Flink — checkpointing](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/)
- [Temporal — durable execution](https://docs.temporal.io/)
