---
{
  "title": "Control Flow",
  "description": "branch and block structures.",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use block and end",
    "Use if/else",
    "Use br and br_if",
    "Use loop"
  ],
  "knowledge_refs": [
    "webassembly/webassembly-07-control-flow"
  ],
  "prerequisites": [
    "WebAssembly-06: Memory Operations"
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

# WEBASSEMBLY-07-CONTROL-FLOW: Control Flow

## Introduction

branch and block structures. By the end of this lesson you will be able to: Use block and end; Use if/else; Use br and br_if; Use loop.

## Key Concepts

### 1. Use block and end

Target: Use block and end. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wast
(func (export "max") (param i32 i32) (result i32)
  local.get 0
  local.get 1
  i32.gt_s
  if (result i32)
    local.get 0
  else
    local.get 1
  end)
```
### 2. Use if/else

Target: Use if/else. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wast
(func (export "sum") (param i32) (result i32)
  (local i32)
  block
    loop
      local.get 0
      i32.eqz
      br_if 1
      local.get 1
      local.get 0
      i32.add
      local.set 1
      local.get 0
      i32.const 1
      i32.sub
      local.set 0
      br 0
    end
  end
  local.get 1)
```
### 3. Use br and br_if

Target: Use br and br_if. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wast
(func (export "abs") (param i32) (result i32)
  local.get 0
  i32.const 0
  i32.lt_s
  if (result i32)
    local.get 0
    i32.const -1
    i32.mul
  else
    local.get 0
  end)
```
### 4. Use loop

Target: Use loop. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wast
(func (export "fib") (param i32) (result i32)
  ...)
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
