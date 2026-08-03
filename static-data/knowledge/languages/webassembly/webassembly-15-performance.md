---
{
  "title": "Performance Patterns",
  "description": "Write fast WASM.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Avoid boundary crossings",
    "Batch memory ops",
    "Use typed arrays",
    "Benchmark"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-15-performance"
  ],
  "prerequisites": [
    "WebAssembly-14: WAT and AssemblyScript"
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

# WEBASSEMBLY-15-PERFORMANCE: Performance Patterns

## Introduction

Write fast WASM. By the end of this lesson you will be able to: Avoid boundary crossings; Batch memory ops; Use typed arrays; Benchmark.

## Key Concepts

### 1. Avoid boundary crossings

Target: Avoid boundary crossings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
// Prefer: pass a batch to WASM once, not many small calls
```
### 2. Batch memory ops

Target: Batch memory ops. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
const arr = new Uint32Array(memory.buffer, 0, 1024);
```
### 3. Use typed arrays

Target: Use typed arrays. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
// Process large arrays entirely in WASM
```
### 4. Benchmark

Target: Benchmark. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
performance.now() to measure
```

## Practice Questions

1. What is the key idea behind "Performance Patterns"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance Patterns with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance Patterns"
1. "Provide advanced patterns and performance considerations for Performance Patterns"

## Key Takeaways

- Master the core ideas of Performance Patterns through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
