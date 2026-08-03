---
{
  "title": "Locals and Globals",
  "description": "Function locals and module globals.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare locals",
    "Use get_local and set_local",
    "Declare globals",
    "Export globals"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-03-variables"
  ],
  "prerequisites": [
    "WebAssembly-02: Value Types"
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

# WEBASSEMBLY-03-VARIABLES: Locals and Globals

## Introduction

Function locals and module globals. By the end of this lesson you will be able to: Declare locals; Use get_local and set_local; Declare globals; Export globals.

## Key Concepts

### 1. Declare locals

Target: Declare locals. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
(func (export "use_local") (param i32) (result i32)
  (local i32)
  local.get 0
  local.set 1
  local.get 1)
```
### 2. Use get_local and set_local

Target: Use get_local and set_local. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
(module
  (global $counter (mut i32) (i32.const 0))
  (func (export "inc")
    global.get $counter
    i32.const 1
    i32.add
    global.set $counter))
```
### 3. Declare globals

Target: Declare globals. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
(global $exported (export "version") i32 (i32.const 1))
```
### 4. Export globals

Target: Export globals. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
(func (param $x i32) (param $y i32) (result i32)
  local.get $x
  local.get $y
  i32.add)
```

## Practice Questions

1. What is the key idea behind "Locals and Globals"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Locals and Globals with analogies and real-world examples"
1. "Show me common mistakes beginners make with Locals and Globals"
1. "Provide advanced patterns and performance considerations for Locals and Globals"

## Key Takeaways

- Master the core ideas of Locals and Globals through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
