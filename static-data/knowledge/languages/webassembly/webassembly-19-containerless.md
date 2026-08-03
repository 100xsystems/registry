---
{
  "title": "Edge Computing and Serverless",
  "description": "WASM at the edge.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand edge WASM",
    "Use Fastly Compute",
    "Use Cloudflare Workers",
    "Deploy functions"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-19-containerless"
  ],
  "prerequisites": [
    "WebAssembly-18: WASI: Server-Side WASM"
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

# WEBASSEMBLY-19-CONTAINERLESS: Edge Computing and Serverless

## Introduction

WASM at the edge. By the end of this lesson you will be able to: Understand edge WASM; Use Fastly Compute; Use Cloudflare Workers; Deploy functions.

## Key Concepts

### 1. Understand edge WASM

Target: Understand edge WASM. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
// Cloudflare Workers: compile Rust to WASM
```
### 2. Use Fastly Compute

Target: Use Fastly Compute. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
wrangler publish
```
### 3. Use Cloudflare Workers

Target: Use Cloudflare Workers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
// Fastly: fastly compute serve
```
### 4. Deploy functions

Target: Deploy functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
module.exports = { fetch(req) { return new Response("hi"); } };
```

## Practice Questions

1. What is the key idea behind "Edge Computing and Serverless"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Edge Computing and Serverless with analogies and real-world examples"
1. "Show me common mistakes beginners make with Edge Computing and Serverless"
1. "Provide advanced patterns and performance considerations for Edge Computing and Serverless"

## Key Takeaways

- Master the core ideas of Edge Computing and Serverless through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
