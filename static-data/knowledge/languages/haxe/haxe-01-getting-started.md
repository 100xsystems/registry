---
{
  "title": "Getting Started with Haxe",
  "description": "Install, compile targets, hello world.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install Haxe",
    "Write hello world",
    "Compile to multiple targets",
    "Use the build tool"
  ],
  "knowledge_refs": [
    "haxe/haxe-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
  ],
  "references": [
    {
      "title": "Haxe Documentation",
      "url": "https://haxe.org/documentation/",
      "description": "Official docs"
    },
    {
      "title": "Haxe Manual",
      "url": "https://haxe.org/manual/introduction.html",
      "description": "The language manual"
    },
    {
      "title": "Haxe Cookbook",
      "url": "https://code.haxe.org/",
      "description": "Community recipes"
    }
  ]
}
---

# HAXE-01-GETTING-STARTED: Getting Started with Haxe

## Introduction

Install, compile targets, hello world. By the end of this lesson you will be able to: Install Haxe; Write hello world; Compile to multiple targets; Use the build tool.

## Key Concepts

### 1. Install Haxe

Target: Install Haxe. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
class Main {
  static function main() {
    trace("Hello, World!");
  }
}
```
### 2. Write hello world

Target: Write hello world. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
haxe -main Main -neko hello.n
neko hello.n
```
### 3. Compile to multiple targets

Target: Compile to multiple targets. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
haxe -main Main -js hello.js
node hello.js
```
### 4. Use the build tool

Target: Use the build tool. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
haxe -main Main -cpp bin
```

## Practice Questions

1. What is the key idea behind "Getting Started with Haxe"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Haxe with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Haxe"
1. "Provide advanced patterns and performance considerations for Getting Started with Haxe"

## Key Takeaways

- Master the core ideas of Getting Started with Haxe through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
