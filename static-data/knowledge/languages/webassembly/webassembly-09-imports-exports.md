---
{
  "title": "Imports and Exports",
  "description": "The module interface.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Export functions",
    "Import functions",
    "Import memory",
    "Use wasm-bindgen"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-09-imports-exports"
  ],
  "prerequisites": [
    "WebAssembly-08: Tables and call_indirect"
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

# WEBASSEMBLY-09-IMPORTS-EXPORTS: Imports and Exports

## Introduction

The module interface. By the end of this lesson you will be able to: Export functions; Import functions; Import memory; Use wasm-bindgen.

## Key Concepts

### 1. Export functions

Target: Export functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
(module
  (func (export "hello") (result i32)
    i32.const 42))
```
### 2. Import functions

Target: Import functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
(module
  (import "env" "log" (func $log (param i32)))
  (func (export "run")
    i32.const 42
    call $log))
```
### 3. Import memory

Target: Import memory. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
(import "env" "memory" (memory 1))
```
### 4. Use wasm-bindgen

Target: Use wasm-bindgen. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
(export "run" (func $run))
```

## Practice Questions

1. What is the key idea behind "Imports and Exports"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Imports and Exports with analogies and real-world examples"
1. "Show me common mistakes beginners make with Imports and Exports"
1. "Provide advanced patterns and performance considerations for Imports and Exports"

## Key Takeaways

- Master the core ideas of Imports and Exports through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
