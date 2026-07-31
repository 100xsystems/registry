---
title: "Iterator: Walk a Collection Without Its Layout"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the iterator intent"
  - "Separate traversal from the collection"
  - "Use lazy iteration"
  - "Implement a custom iterator"
prerequisites:
  - "patterns/composite"
  - "patterns/visitor"
knowledge_refs:
  - "patterns/iterator"
---

# Iterator: Walk a Collection Without Its Layout

## The Problem

A tree, a linked list, and a filtered view are traversed differently. If callers must know the layout to walk it, every change to the collection breaks every caller. The iterator exposes one protocol — next() / has_next() — so traversal logic lives with the collection and callers stay layout-agnostic.

```python
# Iterator: lazy traversal with a generator
class Node:
    def __init__(self, v, left=None, right=None):
        self.v, self.left, self.right = v, left, right

def inorder(root):                      # the traversal, owned here
    if root is None:
        return
    yield from inorder(root.left)
    yield root.v
    yield from inorder(root.right)

tree = Node(2, Node(1), Node(3))
print(list(inorder(tree)))              # [1, 2, 3] — caller knows nothing
```

## Lazy and Compositional

Iterators are lazy: each element is produced on demand, so infinite sequences and streaming pipelines are possible. Because iterators compose (map, filter, chain), whole data pipelines become declarative — the essence of generators in Python, iterators in Rust, and streams in Java.

## Practice: Hide the Traversal

A document model is a tree of paragraphs and sections; the word-count tool must walk it in order.

**Task 1:** Implement an iterator over the document tree without exposing nodes.

**Task 2:** Add a filtered iterator (only paragraphs) by composition.

**Task 3:** Rewrite the word-count tool to use only the iterator API.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why lazy iteration enables infinite sequences. Start with where the state lives.

**Prompt 2 — Compare & Contrast:**
> Compare iterator with visitor: one walks, the other performs operations per element. When does each fit?

**Prompt 3 — Boundary Testing:**
> A caller mutates the collection mid-iteration. Design the fail-fast or snapshot policy that prevents silent corruption.

## Key Takeaways

- Iterators decouple traversal from collection layout
- Lazy generation enables streaming and infinite sequences
- Iterators compose into declarative pipelines
- Mutation during iteration needs a defined policy

## Further Reading

- [Iterator — Refactoring Guru](https://refactoring.guru/design-patterns/iterator)
- [Iterators in Python — official docs](https://docs.python.org/3/library/stdtypes.html#iterator-types)
