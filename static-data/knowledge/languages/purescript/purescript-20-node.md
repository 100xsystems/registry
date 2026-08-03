---
{
  "title": "Node.js Integration",
  "description": "Build Node apps.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use node libraries",
    "Read files",
    "Write HTTP servers",
    "Handle process args"
  ],
  "knowledge_refs": [
    "purescript/purescript-20-node"
  ],
  "prerequisites": [
    "PureScript-19: UI with Halogen"
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

# PURESCRIPT-20-NODE: Node.js Integration

## Introduction

Build Node apps. By the end of this lesson you will be able to: Use node libraries; Read files; Write HTTP servers; Handle process args.

## Key Concepts

### 1. Use node libraries

Target: Use node libraries. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
import Node.FS.Async (readTextFile, writeTextFile)
```
### 2. Read files

Target: Read files. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
import Node.Encoding (Encoding(UTF8))
```
### 3. Write HTTP servers

Target: Write HTTP servers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
main = launchAff_ do
  text <- readTextFile UTF8 "data.txt"
  log text
```
### 4. Handle process args

Target: Handle process args. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
import Node.HTTP as HTTP
main = HTTP.createServer handler >>= listen 8080
```

## Practice Questions

1. What is the key idea behind "Node.js Integration"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Node.js Integration with analogies and real-world examples"
1. "Show me common mistakes beginners make with Node.js Integration"
1. "Provide advanced patterns and performance considerations for Node.js Integration"

## Key Takeaways

- Master the core ideas of Node.js Integration through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
