---
{
  "title": "Threads and Shared Memory",
  "description": "WebAssembly threads.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create workers",
    "Share memory",
    "Use atomics",
    "Synchronize threads"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-16-threads"
  ],
  "prerequisites": [
    "WebAssembly-15: Performance Patterns"
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

# WEBASSEMBLY-16-THREADS: Threads and Shared Memory

## Introduction

WebAssembly threads. By the end of this lesson you will be able to: Create workers; Share memory; Use atomics; Synchronize threads.

## Key Concepts

### 1. Create workers

Target: Create workers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
new Worker("worker.js");
```
### 2. Share memory

Target: Share memory. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
const shared = new SharedArrayBuffer(1024);
```
### 3. Use atomics

Target: Use atomics. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
const memory = new WebAssembly.Memory({ initial: 1, maximum: 10, shared: true });
```
### 4. Synchronize threads

Target: Synchronize threads. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
Atomics.add(new Int32Array(shared), 0, 1);
```

## Practice Questions

1. What is the key idea behind "Threads and Shared Memory"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Threads and Shared Memory with analogies and real-world examples"
1. "Show me common mistakes beginners make with Threads and Shared Memory"
1. "Provide advanced patterns and performance considerations for Threads and Shared Memory"

## Key Takeaways

- Master the core ideas of Threads and Shared Memory through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
