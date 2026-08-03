---
{
  "title": "Strings in WASM",
  "description": "Pass strings across the boundary.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Encode strings",
    "Pass from JS to WASM",
    "Read strings in JS",
    "Use TextEncoder"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-12-strings"
  ],
  "prerequisites": [
    "WebAssembly-11: The JavaScript API"
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

# WEBASSEMBLY-12-STRINGS: Strings in WASM

## Introduction

Pass strings across the boundary. By the end of this lesson you will be able to: Encode strings; Pass from JS to WASM; Read strings in JS; Use TextEncoder.

## Key Concepts

### 1. Encode strings

Target: Encode strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
const encoder = new TextEncoder();
const bytes = encoder.encode("Hello");
new Uint8Array(memory.buffer, offset, bytes.length).set(bytes);
```
### 2. Pass from JS to WASM

Target: Pass from JS to WASM. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
(func (export "len") (param i32) (result i32)
  local.get 0
  i32.load8_u)
```
### 3. Read strings in JS

Target: Read strings in JS. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
const decoder = new TextDecoder();
const str = decoder.decode(new Uint8Array(memory.buffer, offset, len));
```
### 4. Use TextEncoder

Target: Use TextEncoder. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
instance.exports.write(offset, len);
```

## Practice Questions

1. What is the key idea behind "Strings in WASM"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings in WASM with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings in WASM"
1. "Provide advanced patterns and performance considerations for Strings in WASM"

## Key Takeaways

- Master the core ideas of Strings in WASM through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
