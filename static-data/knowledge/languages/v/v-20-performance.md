---
{
  "title": "Performance",
  "description": "V compiles to fast native code.",
  "type": "lesson",
  "order": 20,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use -prod builds",
    "Avoid allocations",
    "Use fixed arrays",
    "Profile code"
  ],
  "knowledge_refs": [
    "v/v-20-performance"
  ],
  "prerequisites": [
    "V-19: Database Access"
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

# V-20-PERFORMANCE: Performance

## Introduction

V compiles to fast native code. By the end of this lesson you will be able to: Use -prod builds; Avoid allocations; Use fixed arrays; Profile code.

## Key Concepts

### 1. Use -prod builds

Target: Use -prod builds. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
v -prod -o app app.v
```
### 2. Avoid allocations

Target: Avoid allocations. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
import time

start := time.now()
// work
println(time.now() - start)
```
### 3. Use fixed arrays

Target: Use fixed arrays. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
mut arr := [0]!1000   // fixed array
```
### 4. Profile code

Target: Profile code. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
for i in 0..1000000 { _ = i }
```

## Practice Questions

1. What is the key idea behind "Performance"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance"
1. "Provide advanced patterns and performance considerations for Performance"

## Key Takeaways

- Master the core ideas of Performance through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
