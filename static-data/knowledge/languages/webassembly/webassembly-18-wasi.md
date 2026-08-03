---
{
  "title": "WASI: Server-Side WASM",
  "description": "Run WASM outside the browser.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand WASI",
    "Use wasmtime",
    "Access files",
    "Run CLI tools"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-18-wasi"
  ],
  "prerequisites": [
    "WebAssembly-17: SIMD"
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

# WEBASSEMBLY-18-WASI: WASI: Server-Side WASM

## Introduction

Run WASM outside the browser. By the end of this lesson you will be able to: Understand WASI; Use wasmtime; Access files; Run CLI tools.

## Key Concepts

### 1. Understand WASI

Target: Understand WASI. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
wasmtime run hello.wasm
```
### 2. Use wasmtime

Target: Use wasmtime. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
rustup target add wasm32-wasip1
```
### 3. Access files

Target: Access files. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
wasmtime --dir=. app.wasm
```
### 4. Run CLI tools

Target: Run CLI tools. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
cargo build --target wasm32-wasip1
```

## Practice Questions

1. What is the key idea behind "WASI: Server-Side WASM"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain WASI: Server-Side WASM with analogies and real-world examples"
1. "Show me common mistakes beginners make with WASI: Server-Side WASM"
1. "Provide advanced patterns and performance considerations for WASI: Server-Side WASM"

## Key Takeaways

- Master the core ideas of WASI: Server-Side WASM through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
