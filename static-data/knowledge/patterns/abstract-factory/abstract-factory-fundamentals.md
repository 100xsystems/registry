---
title: "Abstract Factory: Families of Related Objects"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the abstract factory intent"
  - "Build a factory of factories"
  - "Keep related products consistent"
  - "Compare with the factory method"
prerequisites:
  - "patterns/factory"
  - "patterns/singleton"
knowledge_refs:
  - "patterns/abstract-factory"
---

# Abstract Factory: Families of Related Objects

## The Problem: Related Objects Drift

Some objects belong together: a Windows dialog uses Windows buttons and Windows menus; a dark theme uses dark widgets. If callers construct these individually, a bug can mix a Windows button into a Linux dialog — an inconsistent family.

The abstract factory provides one interface for creating an entire family of related objects. Each concrete factory (WindowsFactory, LinuxFactory) produces a consistent set.

```java
// Abstract factory: one interface per product family
interface GUIFactory {
    Button createButton();
    Dialog createDialog();
}

class WindowsFactory implements GUIFactory {
    public Button createButton() { return new WindowsButton(); }
    public Dialog createDialog() { return new WindowsDialog(); }
}

class LinuxFactory implements GUIFactory {
    public Button createButton() { return new LinuxButton(); }
    public Dialog createDialog() { return new LinuxDialog(); }
}

// The app is given a factory; it can never mix families.
void buildUI(GUIFactory f) {
    Button b = f.createButton();   // always matches the dialog
    Dialog d = f.createDialog();
}
```

## Consistency Is the Point

The pattern exists to guarantee consistency, not just to avoid new. The factory encodes the constraint "these objects belong together" in the type system — a compiler-enforced product family.

## Practice: Build a Cross-Platform Layer

A data layer must support Postgres and SQLite with matching Connection and Query objects.

**Task 1:** Define the abstract factory and the two product interfaces.

**Task 2:** Implement the two concrete factories with their products.

**Task 3:** Show why the app can never mix a Postgres connection with a SQLite query.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the difference between factory method and abstract factory. Start with the number of products.

**Prompt 2 — Compare & Contrast:**
> Compare abstract factory with the builder pattern. When is a family of products the right abstraction versus a single complex product?

**Prompt 3 — Boundary Testing:**
> A new product type joins the family and every factory must change. Is that a violation of open-closed? Design the fix.

## Key Takeaways

- Abstract factory creates families of related objects
- Consistency of the family is the core guarantee
- The type system enforces "no mixed products"
- Growing the product set touches every factory — extend with care

## Further Reading

- [Abstract Factory — Refactoring Guru](https://refactoring.guru/design-patterns/abstract-factory)
- [Abstract Factory — Wikipedia](https://en.wikipedia.org/wiki/Abstract_factory_pattern)
