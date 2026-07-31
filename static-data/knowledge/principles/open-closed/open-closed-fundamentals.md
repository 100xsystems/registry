---
title: "Open-Closed: Extend Without Modifying"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "State the open-closed principle"
  - "Explain the risk of modifying tested code"
  - "Extend behavior through interfaces and composition"
  - "Recognize the modify-based anti-pattern"
prerequisites:
  - "principles/dependency-inversion"
  - "principles/interface-segregation"
knowledge_refs:
  - "principles/open-closed"
---

# Open-Closed: Extend Without Modifying

## The Principle

Open-Closed (OCP): a module should be open for extension (you can add new behavior) but closed for modification (you do not change its existing, tested code). Adding a new payment method should add a new class, not edit the switch statement.

Every modification of tested code re-risks it: new bugs, new test runs, review cycles, and merge conflicts. Extension without modification keeps the stable core untouched while the system grows.

```java
// Modify-based: every new shape edits the switch
double area(Object s) {
    if (s instanceof Circle) return pi * r * r;
    if (s instanceof Square) return side * side;
    if (s instanceof Triangle) return ...;   // edit here every time!
}

// Open-closed: new shapes implement the contract, no edits
interface Shape { double area(); }
class Circle implements Shape { public double area() { return pi*r*r; } }
// Adding a Triangle = adding a class. The area() loop never changes.
```

## Abstraction Is the Mechanism

Openness comes from an abstraction (interface/base) that new variants implement. The consuming code depends on the abstraction, so it stays closed while the set of variants is open. This is OCP realized through dependency inversion.

The trap: abstracting too early. OCP earns its keep when variants are genuinely expected — apply it on the second concrete case, not the first.

## Practice: Open Up the Report Export

A report module exports CSV; you must add JSON, XML, and PDF without touching the report core.

**Task 1:** Define the ExportFormat abstraction the core depends on.

**Task 2:** Add the four exporters as implementations — zero edits to the core.

**Task 3:** Wire the format selection at startup and explain why the core is now closed.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about when abstraction for openness is worth it and when it is premature. Start with one vs two variants.

**Prompt 2 — Compare & Contrast:**
> Compare OCP with the strategy pattern and with dependency inversion. How do they relate?

**Prompt 3 — Boundary Testing:**
> A new variant needs a behavior the abstraction cannot express. Design the evolution path that keeps the core closed.

## Key Takeaways

- Open for extension, closed for modification
- Abstraction is the mechanism of openness
- Modifying tested code re-risks it every time
- Generalize on the second concrete case

## Further Reading

- [Open-Closed Principle — Wikipedia](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle)
- [SOLID — Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html)
