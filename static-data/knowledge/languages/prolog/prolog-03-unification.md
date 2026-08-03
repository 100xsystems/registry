---
{
  "title": "Unification",
  "description": "The core of Prolog.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Understand unification",
    "Match terms",
    "Use variables",
    "Distinguish = and is"
  ],
  "knowledge_refs": [
    "prolog/prolog-03-unification"
  ],
  "prerequisites": [
    "Prolog-02: Facts and Rules"
  ],
  "references": [
    {
      "title": "SWI-Prolog Documentation",
      "url": "https://www.swi-prolog.org/pldoc/",
      "description": "Official SWI-Prolog docs"
    },
    {
      "title": "Learn Prolog Now!",
      "url": "https://www.learnprolognow.org/",
      "description": "The classic free textbook"
    },
    {
      "title": "Prolog Wiki",
      "url": "https://en.wikipedia.org/wiki/Prolog",
      "description": "Overview article"
    }
  ]
}
---

# PROLOG-03-UNIFICATION: Unification

## Introduction

The core of Prolog. By the end of this lesson you will be able to: Understand unification; Match terms; Use variables; Distinguish = and is.

## Key Concepts

### 1. Understand unification

Target: Understand unification. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
?- X = 5.
X = 5.
```
### 2. Match terms

Target: Match terms. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
?- f(X, a) = f(b, Y).
X = b, Y = a.
```
### 3. Use variables

Target: Use variables. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
?- X = Y, Y = 42.
X = Y, Y = 42.
```
### 4. Distinguish = and is

Target: Distinguish = and is. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
?- X is 3 + 4.
X = 7.
```

## Practice Questions

1. What is the key idea behind "Unification"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Unification with analogies and real-world examples"
1. "Show me common mistakes beginners make with Unification"
1. "Provide advanced patterns and performance considerations for Unification"

## Key Takeaways

- Master the core ideas of Unification through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
