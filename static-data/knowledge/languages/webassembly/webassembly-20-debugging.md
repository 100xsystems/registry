---
{
  "title": "Debugging WASM",
  "description": "Source maps and tools.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Generate source maps",
    "Use DevTools",
    "Inspect modules",
    "Use wat2wasm round-trip"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-20-debugging"
  ],
  "prerequisites": [
    "WebAssembly-19: Edge Computing and Serverless"
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

# WEBASSEMBLY-20-DEBUGGING: Debugging WASM

## Introduction

Source maps and tools. By the end of this lesson you will be able to: Generate source maps; Use DevTools; Inspect modules; Use wat2wasm round-trip.

## Key Concepts

### 1. Generate source maps

Target: Generate source maps. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
wasm-pack build --dev
```
### 2. Use DevTools

Target: Use DevTools. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
// DevTools Sources panel shows .wat
```
### 3. Inspect modules

Target: Inspect modules. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
wasm2wat math.wasm -o math.wat
```
### 4. Use wat2wasm round-trip

Target: Use wat2wasm round-trip. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
wasm-objdump -d math.wasm
```

## Practice Questions

1. What is the key idea behind "Debugging WASM"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Debugging WASM with analogies and real-world examples"
1. "Show me common mistakes beginners make with Debugging WASM"
1. "Provide advanced patterns and performance considerations for Debugging WASM"

## Key Takeaways

- Master the core ideas of Debugging WASM through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
