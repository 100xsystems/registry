---
{
  "title": "Getting Started with V",
  "description": "Install, compile, and hello world.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install V",
    "Compile with v run",
    "Write hello world",
    "Build executables"
  ],
  "knowledge_refs": [
    "v/v-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
  ],
  "references": [
    {
      "title": "V Documentation",
      "url": "https://docs.vlang.io/",
      "description": "Official docs"
    },
    {
      "title": "V Manual",
      "url": "https://docs.vlang.io/introduction.html",
      "description": "Language manual"
    },
    {
      "title": "V Language GitHub",
      "url": "https://github.com/vlang/v",
      "description": "Source code"
    }
  ]
}
---

# V-01-GETTING-STARTED: Getting Started with V

## Introduction

Install, compile, and hello world. By the end of this lesson you will be able to: Install V; Compile with v run; Write hello world; Build executables.

## Key Concepts

### 1. Install V

Target: Install V. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
fn main() {
	println("Hello, World!")
}
```
### 2. Compile with v run

Target: Compile with v run. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
v run hello.v
```
### 3. Write hello world

Target: Write hello world. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
v hello.v -o hello
./hello
```
### 4. Build executables

Target: Build executables. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
fn main() {
	println("Hello, " + "V!")
}
```

## Practice Questions

1. What is the key idea behind "Getting Started with V"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with V with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with V"
1. "Provide advanced patterns and performance considerations for Getting Started with V"

## Key Takeaways

- Master the core ideas of Getting Started with V through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
