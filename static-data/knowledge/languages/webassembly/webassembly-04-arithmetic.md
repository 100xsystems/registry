---
{
  "title": "Arithmetic Instructions",
  "description": "Integer and float math.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Add and subtract",
    "Multiply and divide",
    "Handle overflow",
    "Use float math"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-04-arithmetic"
  ],
  "prerequisites": [
    "WebAssembly-03: Locals and Globals"
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

# WEBASSEMBLY-04-ARITHMETIC: Arithmetic Instructions

## Introduction

Integer and float math. By the end of this lesson you will be able to: Add and subtract; Multiply and divide; Handle overflow; Use float math.

## Key Concepts

### 1. Add and subtract

Target: Add and subtract. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
(func (export "add") (param i32 i32) (result i32)
  local.get 0
  local.get 1
  i32.add)
```
### 2. Multiply and divide

Target: Multiply and divide. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
(func (export "mul") (param i32 i32) (result i32)
  local.get 0
  local.get 1
  i32.mul)
```
### 3. Handle overflow

Target: Handle overflow. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
(func (export "div") (param i32 i32) (result i32)
  local.get 0
  local.get 1
  i32.div_s)
```
### 4. Use float math

Target: Use float math. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
(func (export "fadd") (param f64 f64) (result f64)
  local.get 0
  local.get 1
  f64.add)
```

## Practice Questions

1. What is the key idea behind "Arithmetic Instructions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arithmetic Instructions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arithmetic Instructions"
1. "Provide advanced patterns and performance considerations for Arithmetic Instructions"

## Key Takeaways

- Master the core ideas of Arithmetic Instructions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
