---
title: "Decorator: Add Behavior Without Changing the Class"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the decorator intent"
  - "Wrap objects with added behavior"
  - "Compose multiple decorators"
  - "Compare with inheritance"
prerequisites:
  - "patterns/composite"
  - "patterns/adapter"
knowledge_refs:
  - "patterns/decorator"
---

# Decorator: Add Behavior Without Changing the Class

## The Idea

A decorator wraps an object and adds behavior, implementing the same interface. A coffee: an espresso wrapped by Milk decorator wrapped by Whip decorator. Each layer adds cost/behavior without touching the base class — decorators compose at runtime.

```java
// Decorator: wrap with behavior, same interface
interface Coffee { double cost(); String description(); }

class Espresso implements Coffee {
    public double cost() { return 1.50; }
    public String description() { return "espresso"; }
}

class WithMilk implements Coffee {
    private final Coffee base;
    WithMilk(Coffee base) { this.base = base; }
    public double cost() { return base.cost() + 0.30; }
    public String description() { return base.description() + " + milk"; }
}

Coffee c = new WithMilk(new Espresso());   // compose at runtime
// New toppings = new decorator classes; the base never changes.
```

## Why Not Inheritance

Inheritance for every combination explodes (EspressoMilkWhip, LatteCaramelNoWhip...). Decorators compose the pieces at runtime — the number of classes is the number of toppings, not the number of combinations.

## Practice: Decorate the Stream

A text stream needs encryption, compression, and buffering — in any combination.

**Task 1:** Define the Stream interface (read/write).

**Task 2:** Implement FileStream plus EncryptedStream, CompressedStream, BufferedStream decorators.

**Task 3:** Compose a compressed+encrypted stream and show the layer order matters.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why decorators beat inheritance for combinatorial behavior. Start with the class count.

**Prompt 2 — Compare & Contrast:**
> Compare decorator with adapter (interface change), proxy (access control), and composite (trees).

**Prompt 3 — Boundary Testing:**
> Two decorators conflict (encrypt after compress vs compress after encrypt). Design the ordering rule or the guard.

## Key Takeaways

- Decorators add behavior via wrapping
- Composition beats inheritance for combinations
- Layer order is part of the behavior
- The interface stays unchanged

## Further Reading

- [Decorator — Refactoring Guru](https://refactoring.guru/design-patterns/decorator)
- [Decorator Pattern — Wikipedia](https://en.wikipedia.org/wiki/Decorator_pattern)
