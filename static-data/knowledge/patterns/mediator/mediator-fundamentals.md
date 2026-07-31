---
title: "Mediator: One Hub for Many Collaborators"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the mediator intent"
  - "Replace many-to-many with hub-and-spoke"
  - "Build a UI mediator"
  - "Compare with observer"
prerequisites:
  - "patterns/observer"
  - "patterns/facade"
knowledge_refs:
  - "patterns/mediator"
---

# Mediator: One Hub for Many Collaborators

## The Problem

A form has 20 widgets; every widget reacts to changes in others. Direct wiring creates a many-to-many tangle. The mediator becomes the hub: widgets notify the mediator, and the mediator decides what to update. Widgets stay reusable and know nothing about each other.

```typescript
// Mediator: the dialog coordinates its widgets
class DialogMediator {
    constructor(private input: Input, private button: Button) {
        input.onChange = (v) => this.inputChanged(v);
        button.onClick = () => this.submit();
    }
    private inputChanged(v: string) {
        this.button.setEnabled(v.length > 2);   // hub decides
    }
    private submit() {
        if (this.button.enabled) save(this.input.value);
    }
}
// Input and Button have no reference to each other.
// A new widget joins by wiring it in the mediator only.
```

## Mediator vs Observer

Observer is a one-to-many notification: subjects announce, observers listen. Mediator is many-to-many coordination through one hub: it is the observer plus control flow. They combine well — widgets fire events, the mediator subscribes to all of them and orchestrates.

## Practice: Untangle the Form

A settings dialog: theme, font size, and preview update each other across 6 widgets.

**Task 1:** Draw the current many-to-many wiring and count the links.

**Task 2:** Build the mediator and move every link through it.

**Task 3:** Add a new widget and count the changes under both designs.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why the mediator centralizes control flow, not just notifications.

**Prompt 2 — Compare & Contrast:**
> Compare mediator with observer and with facade. Where does each belong in a UI or service layer?

**Prompt 3 — Boundary Testing:**
> Two widgets update each other in a loop through the mediator. Design the cycle guard.

## Key Takeaways

- Mediator turns many-to-many into hub-and-spoke
- Widgets stay decoupled and reusable
- Mediator owns the coordination logic
- Guard against update cycles

## Further Reading

- [Mediator — Refactoring Guru](https://refactoring.guru/design-patterns/mediator)
- [Mediator Pattern — Wikipedia](https://en.wikipedia.org/wiki/Mediator_pattern)
