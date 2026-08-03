---
{
  "title": "Tables and call_indirect",
  "description": "Function pointers.",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Declare tables",
    "Use call_indirect",
    "Store function refs",
    "Implement dispatch"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-08-tables"
  ],
  "prerequisites": [
    "WebAssembly-07: Control Flow"
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

# WEBASSEMBLY-08-TABLES: Tables and call_indirect

## Introduction

Function pointers. By the end of this lesson you will be able to: Declare tables; Use call_indirect; Store function refs; Implement dispatch.

## Key Concepts

### 1. Declare tables

Target: Declare tables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
(module
  (type $binop (func (param i32 i32) (result i32)))
  (table 2 funcref)
  (elem (i32.const 0) $add $mul)
  (func $add (type $binop) (param i32 i32) (result i32)
    local.get 0
    local.get 1
    i32.add)
  (func $mul (type $binop) (param i32 i32) (result i32)
    local.get 0
    local.get 1
    i32.mul)
  (func (export "apply") (param i32 i32 i32) (result i32)
    local.get 0
    local.get 1
    local.get 2
    call_indirect (type $binop)))
```
### 2. Use call_indirect

Target: Use call_indirect. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
(type $void (func))
```
### 3. Store function refs

Target: Store function refs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
(table (export "table") 10 funcref)
```
### 4. Implement dispatch

Target: Implement dispatch. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
call_indirect (param i32) (result i32)
```

## Practice Questions

1. What is the key idea behind "Tables and call_indirect"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Tables and call_indirect with analogies and real-world examples"
1. "Show me common mistakes beginners make with Tables and call_indirect"
1. "Provide advanced patterns and performance considerations for Tables and call_indirect"

## Key Takeaways

- Master the core ideas of Tables and call_indirect through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
