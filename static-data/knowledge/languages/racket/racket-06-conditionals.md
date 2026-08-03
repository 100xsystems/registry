---
{
  "title": "Conditionals",
  "description": "if, cond, and cases.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use if",
    "Use cond",
    "Use case",
    "Use boolean logic"
  ],
  "knowledge_refs": [
    "racket/racket-06-conditionals"
  ],
  "prerequisites": [
    "Racket-05: Lists"
  ],
  "references": [
    {
      "title": "Racket Documentation",
      "url": "https://docs.racket-lang.org/",
      "description": "Official docs"
    },
    {
      "title": "How to Design Programs",
      "url": "https://htdp.org/",
      "description": "The classic textbook"
    },
    {
      "title": "Racket Guide",
      "url": "https://docs.racket-lang.org/guide/",
      "description": "Official language guide"
    }
  ]
}
---

# RACKET-06-CONDITIONALS: Conditionals

## Introduction

if, cond, and cases. By the end of this lesson you will be able to: Use if; Use cond; Use case; Use boolean logic.

## Key Concepts

### 1. Use if

Target: Use if. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(if (> 3 2) "yes" "no")
```
### 2. Use cond

Target: Use cond. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(cond [(> x 0) "positive"]
      [(< x 0) "negative"]
      [else "zero"])
```
### 3. Use case

Target: Use case. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
(case 2
  [(1) "one"]
  [(2) "two"]
  [else "other"])
```
### 4. Use boolean logic

Target: Use boolean logic. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
(and #t #f)
(or #f #t)
(not #t)
```

## Practice Questions

1. What is the key idea behind "Conditionals"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Conditionals with analogies and real-world examples"
1. "Show me common mistakes beginners make with Conditionals"
1. "Provide advanced patterns and performance considerations for Conditionals"

## Key Takeaways

- Master the core ideas of Conditionals through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
