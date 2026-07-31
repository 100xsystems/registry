---
title: "Composite: Trees of Part-Whole"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the composite intent"
  - "Build leaf and composite nodes"
  - "Treat leaves and branches uniformly"
  - "Recognize tree structures in code"
prerequisites:
  - "patterns/iterator"
  - "patterns/decorator"
knowledge_refs:
  - "patterns/composite"
---

# Composite: Trees of Part-Whole

## The Idea

Some structures are naturally trees: files and folders, employees and departments, UI widgets and panels. Composite lets code treat a single item and a group of items through the same interface — draw() on a file draws the file, draw() on a folder draws all its contents.

```java
// Composite: leaf and branch share the interface
interface Graphic {
    void draw();
    void add(Graphic g);      // no-op on leaves
}

class Circle implements Graphic {
    public void draw() { System.out.println("circle"); }
    public void add(Graphic g) { }            // leaf: cannot add
}

class Group implements Graphic {
    private final List<Graphic> children = new ArrayList<>();
    public void draw() { for (Graphic c : children) c.draw(); }
    public void add(Graphic g) { children.add(g); }
}

// Callers draw() a circle or a group of groups — same call.
Graphic scene = new Group();
scene.add(new Circle());
scene.add(new Group().add(new Circle()));
```

## Recursion Is the Point

The composite pattern is recursive: a group contains graphics which may themselves be groups. Operations (draw, render, size) recurse naturally, and callers never branch on "is this a leaf or a group?" — the interface hides it.

## Practice: Build the File Tree

A file explorer shows files and folders; folder size is the sum of contents.

**Task 1:** Define the FileSystemNode interface with size() and render().

**Task 2:** Implement File (leaf) and Folder (composite).

**Task 3:** Compute the total size of a deeply nested tree with one recursive call.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why leaves and composites sharing an interface removes caller branching. Start with the size() recursion.

**Prompt 2 — Compare & Contrast:**
> Compare composite with decorator (both wrap objects) and with the visitor pattern (both traverse trees).

**Prompt 3 — Boundary Testing:**
> A leaf's add() silently no-ops. Design the alternative: throw, or move add() to a Branch interface?

## Key Takeaways

- Leaves and branches share one interface
- Operations recurse naturally through the tree
- Callers never branch on leaf vs group
- Trees of files, UI, and orgs are composite territory

## Further Reading

- [Composite — Refactoring Guru](https://refactoring.guru/design-patterns/composite)
- [Composite Pattern — Wikipedia](https://en.wikipedia.org/wiki/Composite_pattern)
