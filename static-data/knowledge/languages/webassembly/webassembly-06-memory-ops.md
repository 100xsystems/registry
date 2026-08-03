---
{
  "title": "Memory Operations",
  "description": "Loads and stores with offsets.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use load/store offsets",
    "Handle alignment",
    "Store byte arrays",
    "Read strings"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-06-memory-ops"
  ],
  "prerequisites": [
    "WebAssembly-05: Linear Memory"
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

# WEBASSEMBLY-06-MEMORY-OPS: Memory Operations

## Introduction

Loads and stores with offsets. By the end of this lesson you will be able to: Use load/store offsets; Handle alignment; Store byte arrays; Read strings.

## Key Concepts

### 1. Use load/store offsets

Target: Use load/store offsets. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
(func (export "store_at") (param i32 i32)
  local.get 0
  i32.const 0
  local.get 1
  i32.store offset=0)
```
### 2. Handle alignment

Target: Handle alignment. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
(func (export "load8") (param i32) (result i32)
  local.get 0
  i32.load8_u)
```
### 3. Store byte arrays

Target: Store byte arrays. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
(func (export "write_byte") (param $addr i32) (param $val i32)
  local.get $addr
  local.get $val
  i32.store8)
```
### 4. Read strings

Target: Read strings. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
(func (export "read") (param $addr i32) (result i32)
  local.get $addr
  i32.load align=4)
```

## Practice Questions

1. What is the key idea behind "Memory Operations"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Memory Operations with analogies and real-world examples"
1. "Show me common mistakes beginners make with Memory Operations"
1. "Provide advanced patterns and performance considerations for Memory Operations"

## Key Takeaways

- Master the core ideas of Memory Operations through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
