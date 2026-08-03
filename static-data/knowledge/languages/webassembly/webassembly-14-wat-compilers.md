---
{
  "title": "WAT and AssemblyScript",
  "description": "Compile TypeScript-like code.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use AssemblyScript",
    "Compile ASC",
    "Use asc CLI",
    "Interop with JS"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-14-wat-compilers"
  ],
  "prerequisites": [
    "WebAssembly-13: Rust and wasm-bindgen"
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

# WEBASSEMBLY-14-WAT-COMPILERS: WAT and AssemblyScript

## Introduction

Compile TypeScript-like code. By the end of this lesson you will be able to: Use AssemblyScript; Compile ASC; Use asc CLI; Interop with JS.

## Key Concepts

### 1. Use AssemblyScript

Target: Use AssemblyScript. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
npm install -D assemblyscript
npx asc assembly/index.ts -o build/index.wasm
```
### 2. Compile ASC

Target: Compile ASC. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
export function add(a: i32, b: i32): i32 {
  return a + b;
}
```
### 3. Use asc CLI

Target: Use asc CLI. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
export function fib(n: i32): i32 {
  return n < 2 ? n : fib(n - 1) + fib(n - 2);
}
```
### 4. Interop with JS

Target: Interop with JS. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
import { add } from "./build/index.js";
```

## Practice Questions

1. What is the key idea behind "WAT and AssemblyScript"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain WAT and AssemblyScript with analogies and real-world examples"
1. "Show me common mistakes beginners make with WAT and AssemblyScript"
1. "Provide advanced patterns and performance considerations for WAT and AssemblyScript"

## Key Takeaways

- Master the core ideas of WAT and AssemblyScript through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
