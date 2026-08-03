---
{
  "title": "The JavaScript API",
  "description": "Interact with WASM from JS.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use WebAssembly.instantiate",
    "Pass parameters",
    "Share memory",
    "Handle exceptions"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-11-js-api"
  ],
  "prerequisites": [
    "WebAssembly-10: Text Format Deep Dive"
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

# WEBASSEMBLY-11-JS-API: The JavaScript API

## Introduction

Interact with WASM from JS. By the end of this lesson you will be able to: Use WebAssembly.instantiate; Pass parameters; Share memory; Handle exceptions.

## Key Concepts

### 1. Use WebAssembly.instantiate

Target: Use WebAssembly.instantiate. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
const { instance } = await WebAssembly.instantiateStreaming(
  fetch("math.wasm")
);
console.log(instance.exports.add(2, 3));
```
### 2. Pass parameters

Target: Pass parameters. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
const { module, instance } = await WebAssembly.instantiate(bytes, imports);
```
### 3. Share memory

Target: Share memory. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
WebAssembly.validate(bytes);
```
### 4. Handle exceptions

Target: Handle exceptions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
new WebAssembly.Instance(module, { env: { log } });
```

## Practice Questions

1. What is the key idea behind "The JavaScript API"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain The JavaScript API with analogies and real-world examples"
1. "Show me common mistakes beginners make with The JavaScript API"
1. "Provide advanced patterns and performance considerations for The JavaScript API"

## Key Takeaways

- Master the core ideas of The JavaScript API through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
