---
{
  "title": "Linear Memory",
  "description": "The memory model.",
  "type": "lesson",
  "order": 5,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Declare memory",
    "Load from memory",
    "Store to memory",
    "Grow memory"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-05-memory"
  ],
  "prerequisites": [
    "WebAssembly-04: Arithmetic Instructions"
  ],
  "references": [
    {
      "title": "WebAssembly Specification",
      "url": "https://webassembly.github.io/spec/core/",
      "description": "The official spec"
    },
    {
      "title": "MDN WebAssembly Docs",
      "url": "https://developer.mozilla.org/en-US/docs/WebAssembly",
      "description": "Mozilla reference"
    },
    {
      "title": "WebAssembly.org",
      "url": "https://webassembly.org/",
      "description": "Official site"
    }
  ]
}
---

# WEBASSEMBLY-05-MEMORY: Linear Memory

## Introduction

The memory model. By the end of this lesson you will be able to: Declare memory; Load from memory; Store to memory; Grow memory.

## Key Concepts

### 1. Declare memory

Target: Declare memory. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
(module
  (memory (export "memory") 1)
  (func (export "store") (param i32 i32)
    local.get 0
    local.get 1
    i32.store))
```
### 2. Load from memory

Target: Load from memory. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
(func (export "load") (param i32) (result i32)
  local.get 0
  i32.load)
```
### 3. Store to memory

Target: Store to memory. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
(func (export "init")
  i32.const 0
  i32.const 42
  i32.store)
```
### 4. Grow memory

Target: Grow memory. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
(memory 1 4)   ; 1 page initial, 4 pages max
```

## Practice Questions

1. What is the key idea behind "Linear Memory"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Linear Memory with analogies and real-world examples"
1. "Show me common mistakes beginners make with Linear Memory"
1. "Provide advanced patterns and performance considerations for Linear Memory"

## Key Takeaways

- Master the core ideas of Linear Memory through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
