---
{
  "title": "Facts and Rules",
  "description": "Build a knowledge base.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write multi-argument facts",
    "Write rules",
    "Use variables in rules",
    "Query with variables"
  ],
  "knowledge_refs": [
    "prolog/prolog-02-facts-rules"
  ],
  "prerequisites": [
    "Prolog-01: Getting Started with Prolog"
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

# PROLOG-02-FACTS-RULES: Facts and Rules

## Introduction

Build a knowledge base. By the end of this lesson you will be able to: Write multi-argument facts; Write rules; Use variables in rules; Query with variables.

## Key Concepts

### 1. Write multi-argument facts

Target: Write multi-argument facts. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
parent(tom, bob).
parent(bob, ann).
```
### 2. Write rules

Target: Write rules. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
```
### 3. Use variables in rules

Target: Use variables in rules. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
?- grandparent(tom, ann).
true.
```
### 4. Query with variables

Target: Query with variables. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
```

## Practice Questions

1. What is the key idea behind "Facts and Rules"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Facts and Rules with analogies and real-world examples"
1. "Show me common mistakes beginners make with Facts and Rules"
1. "Provide advanced patterns and performance considerations for Facts and Rules"

## Key Takeaways

- Master the core ideas of Facts and Rules through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
