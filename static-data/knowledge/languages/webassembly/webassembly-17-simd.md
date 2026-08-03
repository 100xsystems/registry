---
{
  "title": "SIMD",
  "description": "Vectorized computation.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use v128 instructions",
    "Load vectors",
    "Add vectors",
    "Speed up math"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-17-simd"
  ],
  "prerequisites": [
    "WebAssembly-16: Threads and Shared Memory"
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

# WEBASSEMBLY-17-SIMD: SIMD

## Introduction

Vectorized computation. By the end of this lesson you will be able to: Use v128 instructions; Load vectors; Add vectors; Speed up math.

## Key Concepts

### 1. Use v128 instructions

Target: Use v128 instructions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
(func (export "vadd") (param v128 v128) (result v128)
  local.get 0
  local.get 1
  i32x4.add)
```
### 2. Load vectors

Target: Load vectors. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
(func (export "load_v") (param i32) (result v128)
  local.get 0
  v128.load)
```
### 3. Add vectors

Target: Add vectors. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
i32x4.mul
```
### 4. Speed up math

Target: Speed up math. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
v128.store
```

## Practice Questions

1. What is the key idea behind "SIMD"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain SIMD with analogies and real-world examples"
1. "Show me common mistakes beginners make with SIMD"
1. "Provide advanced patterns and performance considerations for SIMD"

## Key Takeaways

- Master the core ideas of SIMD through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
