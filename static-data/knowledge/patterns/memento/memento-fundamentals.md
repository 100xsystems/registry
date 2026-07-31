---
title: "Memento: Snapshots Without Breaking Encapsulation"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the memento intent"
  - "Capture state without breaking encapsulation"
  - "Implement undo/redo"
  - "Know the memory cost"
prerequisites:
  - "patterns/command"
  - "patterns/state"
knowledge_refs:
  - "patterns/memento"
---

# Memento: Snapshots Without Breaking Encapsulation

## The Problem

Undo needs the previous state, but reading all fields to snapshot them either exposes internals or couples the undo logic to every field. The memento is an opaque snapshot created by the originator itself — only the originator can read and restore it, so encapsulation survives.

```java
// Memento: the editor snapshots itself; caretaker holds history
class Editor {
    private String text;
    Memento save() { return new Memento(text); }        // snapshot
    void restore(Memento m) { this.text = m.getText(); }
}

class Memento {                    // opaque to everyone but Editor
    private final String text;
    Memento(String t) { this.text = t; }
    String getText() { return text; }   // package-private access
}

// History: a stack of Mementos, all opaque
Stack<Memento> history = new Stack<>();
history.push(editor.save());
editor.type("hello");
editor.restore(history.pop());     // undo
```

## Undo/Redo

Undo = pop a memento and restore; redo = push back. Two stacks make both work. The memento pattern is the textbook undo — but snapshots are copies: a large document snapshot per keystroke is memory-heavy, which is why real editors use deltas or persistent data structures.

## Practice: Build Undo for the Editor

A text area needs undo/redo across 1000 edits without exposing its internal buffer.

**Task 1:** Implement the memento and the two-stack undo/redo.

**Task 2:** Bound the history: drop the oldest snapshots beyond a limit.

**Task 3:** Measure memory for full snapshots and propose the delta alternative.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why the memento keeps encapsulation while saving state.

**Prompt 2 — Compare & Contrast:**
> Compare memento with command (the other undo approach) and with event sourcing. Which restores what?

**Prompt 3 — Boundary Testing:**
> A snapshot is taken mid-edit and restored later, corrupting an invariant. Design the state validation on restore.

## Key Takeaways

- Mementos capture state without breaking encapsulation
- Undo/redo = two stacks of snapshots
- Snapshots cost memory — bound the history
- Deltas or persistent structures scale undo

## Further Reading

- [Memento — Refactoring Guru](https://refactoring.guru/design-patterns/memento)
- [Memento Pattern — Wikipedia](https://en.wikipedia.org/wiki/Memento_pattern)
