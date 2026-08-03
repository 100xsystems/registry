---
{
  "title": "Rust and wasm-bindgen",
  "description": "Compile Rust to WASM.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Set up wasm-pack",
    "Write Rust functions",
    "Use wasm-bindgen",
    "Publish to npm"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-13-rust-wasm"
  ],
  "prerequisites": [
    "WebAssembly-12: Strings in WASM"
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

# WEBASSEMBLY-13-RUST-WASM: Rust and wasm-bindgen

## Introduction

Compile Rust to WASM. By the end of this lesson you will be able to: Set up wasm-pack; Write Rust functions; Use wasm-bindgen; Publish to npm.

## Key Concepts

### 1. Set up wasm-pack

Target: Set up wasm-pack. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
wasm-pack new myapp
cd myapp
```
### 2. Write Rust functions

Target: Write Rust functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn add(a: u32, b: u32) -> u32 {
    a + b
}
```
### 3. Use wasm-bindgen

Target: Use wasm-bindgen. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
wasm-pack build --target web
```
### 4. Publish to npm

Target: Publish to npm. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
import { add } from "./pkg/myapp.js";
console.log(add(2, 3));
```

## Practice Questions

1. What is the key idea behind "Rust and wasm-bindgen"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Rust and wasm-bindgen with analogies and real-world examples"
1. "Show me common mistakes beginners make with Rust and wasm-bindgen"
1. "Provide advanced patterns and performance considerations for Rust and wasm-bindgen"

## Key Takeaways

- Master the core ideas of Rust and wasm-bindgen through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
