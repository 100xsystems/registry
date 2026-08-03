---
{
  "title": "Getting Started with WebAssembly",
  "description": "What WASM is and your first module.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Understand what WASM is",
    "Write a WAT module",
    "Compile with wat2wasm",
    "Run in a browser"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# WEBASSEMBLY-01-GETTING-STARTED: Getting Started with WebAssembly

## Introduction

What WASM is and your first module. By the end of this lesson you will be able to: Understand what WASM is; Write a WAT module; Compile with wat2wasm; Run in a browser.

## Key Concepts

### 1. Understand what WASM is

Target: Understand what WASM is. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
(module
  (func (export "add") (param i32 i32) (result i32)
    local.get 0
    local.get 1
    i32.add))
```
### 2. Write a WAT module

Target: Write a WAT module. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
wat2wasm math.wat -o math.wasm
```
### 3. Compile with wat2wasm

Target: Compile with wat2wasm. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
WebAssembly.instantiateStreaming(fetch("math.wasm"))
  .then(({ instance }) => {
    console.log(instance.exports.add(2, 3));
  });
```
### 4. Run in a browser

Target: Run in a browser. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
(module (func $main (export "main")))
```

## Practice Questions

1. What is the key idea behind "Getting Started with WebAssembly"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with WebAssembly with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with WebAssembly"
1. "Provide advanced patterns and performance considerations for Getting Started with WebAssembly"

## Key Takeaways

- Master the core ideas of Getting Started with WebAssembly through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
