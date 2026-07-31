---
title: "Factory Method: Let Subclasses Create"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the factory method intent"
  - "Defer creation to subclasses"
  - "Compare with abstract factory and simple factory"
  - "Apply the new keyword rule"
prerequisites:
  - "patterns/abstract-factory"
  - "patterns/singleton"
knowledge_refs:
  - "patterns/factory"
---

# Factory Method: Let Subclasses Create

## The Idea

The factory method lets a class delegate creation to subclasses: the base defines create() abstractly, each subclass returns its own product. Callers depend on the base class; the "which product" decision moves to the subclass.

```java
// Factory method: creation is a subclass decision
abstract class Dialog {
    abstract Button createButton();          // the factory method

    void render() {
        Button b = createButton();           // polymorphic creation
        b.onClick(() -> System.out.println("clicked"));
        b.render();
    }
}

class WebDialog extends Dialog {
    Button createButton() { return new HtmlButton(); }
}
class MobileDialog extends Dialog {
    Button createButton() { return new TouchButton(); }
}
// render() works for any subclass; creation stays in the subclass.
```

## The new-Keyword Rule

Direct new in business code couples the caller to a concrete class. Factory methods and injected factories localize creation so the caller depends on abstractions. The rule: put new behind a factory when the concrete choice should vary.

## Practice: Defer the Parser Choice

An importer parses JSON, CSV, or XML based on the file type.

**Task 1:** Define the Parser interface and the three implementations.

**Task 2:** Design the factory method on the importer (or a ParserFactory) that returns the right parser.

**Task 3:** Add a fourth format with zero changes to the import flow.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the difference between a factory method (overridable) and a simple factory (a function with a switch).

**Prompt 2 — Compare & Contrast:**
> Compare factory method with abstract factory and with dependency injection.

**Prompt 3 — Boundary Testing:**
> The factory returns a product that needs different setup per subtype. Design the factory that handles divergent construction.

## Key Takeaways

- Factory methods defer creation to subclasses
- Callers depend on abstractions, not concretes
- The new keyword hides behind factories
- Adding a product = adding a subclass

## Further Reading

- [Factory Method — Refactoring Guru](https://refactoring.guru/design-patterns/factory-method)
- [Factory Method — Wikipedia](https://en.wikipedia.org/wiki/Factory_method_pattern)
