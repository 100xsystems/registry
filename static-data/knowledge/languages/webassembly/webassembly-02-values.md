---
{
  "title": "Value Types",
  "description": "i32, i64, f32, f64.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use integer types",
    "Use float types",
    "Understand v128",
    "Use type annotations"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-02-values"
  ],
  "prerequisites": [
    "WebAssembly-01: Getting Started with WebAssembly"
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

# WEBASSEMBLY-02-VALUES: Value Types

## Introduction

i32, i64, f32, f64. By the end of this lesson you will be able to: Use integer types; Use float types; Understand v128; Use type annotations.

## Key Concepts

### 1. Use integer types

Target: Use integer types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
(module
  (func (export "int_const") (result i32)
    i32.const 42))
```
### 2. Use float types

Target: Use float types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
(func (export "float_const") (result f64)
    f64.const 3.14)
```
### 3. Understand v128

Target: Understand v128. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
(func (export "big") (result i64)
    i64.const 9223372036854775807)
```
### 4. Use type annotations

Target: Use type annotations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
(module (global $g (mut i32) (i32.const 0)))
```

## Practice Questions

1. What is the key idea behind "Value Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Value Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Value Types"
1. "Provide advanced patterns and performance considerations for Value Types"

## Key Takeaways

- Master the core ideas of Value Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
