---
title: "Command: Turn Actions into Objects"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the command intent"
  - "Build command objects"
  - "Queue, log, and undo commands"
  - "Compare with plain method calls"
prerequisites:
  - "patterns/strategy"
  - "patterns/memento"
knowledge_refs:
  - "patterns/command"
---

# Command: Turn Actions into Objects

## The Idea

A command wraps an action and its parameters in an object with execute() (and optionally undo()). The caller invokes the command without knowing its implementation — enabling queues, history, logging, and macro composition.

```java
// Command: an action as an object
interface Command {
    void execute();
    void undo();
}

class TransferCommand implements Command {
    private final Account from, to;
    private final Money amount;
    private boolean executed = false;

    TransferCommand(Account from, Account to, Money amt) { ... }

    public void execute() { from.debit(amount); to.credit(amount); executed = true; }
    public void undo() { if (executed) { to.debit(amount); from.credit(amount); executed = false; } }
}

// A queue of commands, an undo stack, a log — all just objects
Deque<Command> undoStack = new ArrayDeque<>();
undoStack.push(new TransferCommand(a, b, 100));
undoStack.pop().undo();
```

## Why Objectify Actions

Methods run immediately; command objects can be stored, ordered, retried, batched, and undone. They turn "do this" into a first-class value — which is exactly what editors, queues, and transactional systems need.

## Practice: Build the Undo Stack

A text editor needs undo for insert, delete, and format operations.

**Task 1:** Define the Command interface and three concrete commands.

**Task 2:** Wire the undo stack and the redo stack.

**Task 3:** Handle undo-after-undo and the empty-stack edge case.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about what command objects enable that method calls cannot. Start with undo.

**Prompt 2 — Compare & Contrast:**
> Compare command with strategy and with the observer pattern. Where do they overlap?

**Prompt 3 — Boundary Testing:**
> A command fails halfway through execute(). Design the state handling so undo still works.

## Key Takeaways

- Commands encapsulate actions as objects
- They enable queueing, logging, retry, and undo
- execute/undo pairs need careful state handling
- The caller never knows the command implementation

## Further Reading

- [Command — Refactoring Guru](https://refactoring.guru/design-patterns/command)
- [Command Pattern — Wikipedia](https://en.wikipedia.org/wiki/Command_pattern)
