---
title: "Prototype: Clone Instead of Construct"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the prototype intent"
  - "Clone complex objects cheaply"
  - "Avoid constructor coupling"
  - "Implement a clone interface"
prerequisites:
  - "patterns/factory"
  - "patterns/flyweight"
knowledge_refs:
  - "patterns/prototype"
---

# Prototype: Clone Instead of Construct

## The Problem

Some objects are expensive or complex to construct: deep configuration, loaded assets, recursive structures. The prototype pattern creates new instances by cloning a configured prototype — the clone is a starting point that already has the hard parts done.

```java
// Prototype: clone() gives a ready-configured copy
class Document implements Cloneable {
    private String title;
    private List<Section> sections;   // deep structure
    private Theme theme;              // expensive to load

    Document cloneDocument() {
        try {
            Document d = (Document) super.clone();   // shallow
            d.sections = new ArrayList<>(this.sections);  // deep copy
            d.theme = this.theme;     // share the immutable theme
            return d;
        } catch (CloneNotSupportedException e) { throw new RuntimeException(e); }
    }
}
// Prototype registry: ready-made templates
Document invoiceTemplate = buildInvoiceTemplate();
Document invoice = invoiceTemplate.cloneDocument();  // no rebuild
invoice.setTitle("Invoice #1042");
```

## Shallow vs Deep

Shallow clone shares references; deep clone copies the graph. Which is right depends on what the clone may mutate: sharing immutable parts is cheap and safe; sharing mutable parts corrupts the prototype. The clone method must document its depth.

## Practice: Clone the Scene

A game loads a heavy scene (meshes, textures, AI graphs) and needs many variants.

**Task 1:** Define clone() with the right depth for each field.

**Task 2:** Build the prototype registry of scene templates.

**Task 3:** Trace what happens when two clones mutate a shared field.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about when shallow sharing is safe and when it corrupts. Start with mutable fields.

**Prompt 2 — Compare & Contrast:**
> Compare prototype with factory and with copy constructors. When does cloning beat constructing?

**Prompt 3 — Boundary Testing:**
> A clone mutates the prototype's shared theme. Design the immutable-share or copy-on-write rule.

## Key Takeaways

- Prototype clones configured objects instead of rebuilding
- Deep vs shallow copy is a contract
- Sharing immutable parts is safe; mutable is not
- Registries make templates reusable

## Further Reading

- [Prototype — Refactoring Guru](https://refactoring.guru/design-patterns/prototype)
- [Prototype Pattern — Wikipedia](https://en.wikipedia.org/wiki/Prototype_pattern)
