---
{
  "title": "Getting Started with PureScript",
  "description": "Install, spago, hello world.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install PureScript and spago",
    "Create a project",
    "Write hello world",
    "Run with node"
  ],
  "knowledge_refs": [
    "purescript/purescript-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
  ],
  "references": [
    {
      "title": "PureScript Documentation",
      "url": "https://pursuit.purescript.org/",
      "description": "Official package search"
    },
    {
      "title": "PureScript by Example",
      "url": "https://book.purescript.org/",
      "description": "The official book"
    },
    {
      "title": "PureScript Guide",
      "url": "https://github.com/JordanMartinez/purescript-jordans-reference",
      "description": "Community reference"
    }
  ]
}
---

# PURESCRIPT-01-GETTING-STARTED: Getting Started with PureScript

## Introduction

Install, spago, hello world. By the end of this lesson you will be able to: Install PureScript and spago; Create a project; Write hello world; Run with node.

## Key Concepts

### 1. Install PureScript and spago

Target: Install PureScript and spago. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
module Main where

import Prelude
import Effect (Effect)
import Effect.Console (log)

main :: Effect Unit
main = log "Hello, World!"
```
### 2. Create a project

Target: Create a project. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
spago init
spago run
```
### 3. Write hello world

Target: Write hello world. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
module Main where

import Prelude
import Effect.Console (log)

main = log "Hello, PureScript!"
```
### 4. Run with node

Target: Run with node. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
spago build
node .spago/output/Main/index.js
```

## Practice Questions

1. What is the key idea behind "Getting Started with PureScript"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with PureScript with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with PureScript"
1. "Provide advanced patterns and performance considerations for Getting Started with PureScript"

## Key Takeaways

- Master the core ideas of Getting Started with PureScript through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
