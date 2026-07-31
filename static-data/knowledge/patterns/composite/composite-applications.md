---
title: "Composite in Production: UI Trees and Documents"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design widget/document trees"
  - "Traverse composites with iterators and visitors"
  - "Keep tree operations efficient"
  - "Avoid deep-tree recursion pitfalls"
prerequisites:
  []
knowledge_refs:
  - "patterns/composite"
---

# Composite in Production: UI Trees and Documents

## UI and Document Trees

A DOM or widget tree is a composite: a Panel contains buttons and nested panels; render() on the root renders everything. React/Vue component trees and document object models are composites by construction.

```text
Composite in the wild:
  DOM: <div> contains <p> and <section> containing <p>  -> render(root)
  Document: Paragraph contains Runs; Section contains Paragraphs
  Query AST: And(Equals(a,b), Or(Less(c,d), Exists(e)))
Operations recurse: render, serialize, validate, compute-size.
```

## Traversal and Depth

Iterators and visitors traverse composites without exposing internals. Deep trees risk stack overflow on recursive operations — iterative traversal or explicit work queues handle pathological depth, and lazy subtrees (virtualized lists) keep big trees responsive.

## Practice: Design the Query Tree

A search builder combines filters with AND/OR into a tree.

**Task 1:** Define FilterNode (leaf) and BooleanNode (AND/OR composite).

**Task 2:** Implement evaluate(record) recursively and toSQL() recursively.

**Task 3:** Add a visitor that pretty-prints the tree without modifying nodes.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why visitors keep traversal logic out of the tree nodes. Ask me when to prefer visitor over methods on nodes.

**Prompt 2 — Implementation Design:**
> Design a virtualized UI tree: a list with 100k rows renders only visible ones. Where does the composite pattern bend?

**Prompt 3 — Boundary Testing:**
> A circular reference in a tree (folder containing its ancestor) loops forever. Design the cycle guard.

## Key Takeaways

- DOM, document, and query trees are composites
- Visitors and iterators traverse without exposing internals
- Deep trees need iterative or lazy traversal
- Cycle guards prevent infinite recursion

## Further Reading

- [Visitor — Refactoring Guru](https://refactoring.guru/design-patterns/visitor)
- [Virtualized List — React Window](https://react-window.vercel.app/)
