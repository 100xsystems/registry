---
title: "Visitor: Operations over Object Structures"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the visitor intent"
  - "Define the double dispatch"
  - "Add operations without editing classes"
  - "Know the structure constraint"
prerequisites:
  - "patterns/composite"
  - "patterns/iterator"
knowledge_refs:
  - "patterns/visitor"
---

# Visitor: Operations over Object Structures

## The Problem

An AST, a document tree, a config: classes are stable, but operations grow — pretty-print, validate, transform, compile. Adding each operation to every class is invasive and centralizes concern in the wrong place. The visitor moves the operation into one visitor class and dispatches on the element type — double dispatch: the element accepts the visitor, and the visitor's visit method matches the element's concrete type.

```python
# Visitor: operation lives in the visitor, not the elements
from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def accept(self, v): ...           # double dispatch entry

class Num(Node):
    def __init__(self, value): self.value = value
    def accept(self, v): return v.visit_num(self)

class Add(Node):
    def __init__(self, left, right): self.left, self.right = left, right
    def accept(self, v): return v.visit_add(self)

class Eval(ABC):                       # one operation = one visitor
    def visit_num(self, n): return n.value
    def visit_add(self, a):
        return a.left.accept(self) + a.right.accept(self)

class ToString(ABC):                   # another operation, no edits
    def visit_num(self, n): return str(n.value)
    def visit_add(self, a):
        return f'({a.left.accept(self)} + {a.right.accept(self)})'

tree = Add(Num(2), Add(Num(3), Num(4)))
print(tree.accept(Eval()))             # 9
print(tree.accept(ToString()))         # (2 + (3 + 4))
```

## The Cost

The visitor adds a method per element type to every visitor — adding a new element class means editing every visitor. The pattern pays when the structure is stable and operations grow; it punishes structures that grow. That direction of change is the decision: stable structure, growing operations → visitor.

## Practice: Visit the Document Tree

A document AST (text, bold, link, list) needs rendering and word-count operations.

**Task 1:** Define the elements with accept methods.

**Task 2:** Implement the render visitor and the count visitor.

**Task 3:** Add a third operation and confirm no element edits were needed.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why operations move out of the element classes.

**Prompt 2 — Compare & Contrast:**
> Compare visitor with the strategy and with plain iteration plus instanceof checks.

**Prompt 3 — Boundary Testing:**
> A new element type appears. Design the compilation error or fallback that catches unhandled visits.

## Key Takeaways

- Visitor moves operations out of stable element classes
- Double dispatch routes by concrete element type
- Stable structure + growing operations is its niche
- New element types break every visitor — plan for it

## Further Reading

- [Visitor — Refactoring Guru](https://refactoring.guru/design-patterns/visitor)
- [Visitor pattern — Wikipedia](https://en.wikipedia.org/wiki/Visitor_pattern)
