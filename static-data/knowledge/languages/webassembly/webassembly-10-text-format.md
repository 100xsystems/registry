---
{
  "title": "Text Format Deep Dive",
  "description": "WAT syntax details.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read folded expressions",
    "Use s-expressions",
    "Annotate modules",
    "Convert to binary"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-10-text-format"
  ],
  "prerequisites": [
    "WebAssembly-09: Imports and Exports"
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

# WEBASSEMBLY-10-TEXT-FORMAT: Text Format Deep Dive

## Introduction

WAT syntax details. By the end of this lesson you will be able to: Read folded expressions; Use s-expressions; Annotate modules; Convert to binary.

## Key Concepts

### 1. Read folded expressions

Target: Read folded expressions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
(module
  (func $add (param i32 i32) (result i32)
    (i32.add (local.get 0) (local.get 1))))
```
### 2. Use s-expressions

Target: Use s-expressions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
(func (export "main") (result i32)
  (i32.const 2)
  (i32.const 3)
  (i32.mul))
```
### 3. Annotate modules

Target: Annotate modules. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
(module $m
  (func $f))
```
### 4. Convert to binary

Target: Convert to binary. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
(;; comment ;;)
```

## Practice Questions

1. What is the key idea behind "Text Format Deep Dive"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Text Format Deep Dive with analogies and real-world examples"
1. "Show me common mistakes beginners make with Text Format Deep Dive"
1. "Provide advanced patterns and performance considerations for Text Format Deep Dive"

## Key Takeaways

- Master the core ideas of Text Format Deep Dive through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
