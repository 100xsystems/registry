---
title: "Advanced Command: Macro and Event-Sourced Commands"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Compose macro commands"
  - "Apply command sourcing (commands as events)"
  - "Replay and audit with commands"
  - "Keep commands backward compatible"
prerequisites:
  []
knowledge_refs:
  - "patterns/command"
---

# Advanced Command: Macro and Event-Sourced Commands

## Macro Commands

A macro command is a list of commands executed in order, with undo running them in reverse. Editors and CI pipelines are macro commands — composite objects made of commands.

```java
// Macro command: many commands, one undo
class MacroCommand implements Command {
    private final List<Command> commands = new ArrayList<>();
    void add(Command c) { commands.add(c); }

    public void execute() { for (Command c : commands) c.execute(); }
    public void undo() {
        List<Command> rev = new ArrayList<>(commands);
        Collections.reverse(rev);
        for (Command c : rev) c.undo();     // undo in reverse order
    }
}
```

## Command Sourcing

Command sourcing stores every command (not state) as the durable record. State is derived by replaying commands; audit and debugging are free because the history is complete. Combined with event sourcing, commands become the intent and events the outcomes — the fullest audit trail.

## Practice: Design the Audit Trail

A banking app must prove "who did what when" for every transfer.

**Task 1:** Model transfers as commands persisted with actor and timestamp.

**Task 2:** Design replay: rebuild account state by re-executing commands.

**Task 3:** Handle versioned commands: an old command must still replay after schema changes.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain the difference between command sourcing (intent) and event sourcing (outcome).

**Prompt 2 — Implementation Design:**
> Design a command-sourced inventory system with replay and a snapshot strategy.

**Prompt 3 — Boundary Testing:**
> A replayed command hits a changed business rule and diverges from history. Design the versioning rule for commands.

## Key Takeaways

- Macro commands compose and undo in reverse
- Command sourcing stores intent as the durable record
- Replay derives state; history is complete
- Versioned commands keep replays faithful

## Further Reading

- [Event Sourcing — Microsoft Docs](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)
- [CQRS + Command Sourcing](https://martinfowler.com/bliki/CQRS.html)
