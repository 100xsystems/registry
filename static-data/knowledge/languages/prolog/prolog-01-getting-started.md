---
{
  "title": "Getting Started with Prolog",
  "description": "SWI-Prolog, facts, and queries.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install SWI-Prolog",
    "Write facts",
    "Ask queries",
    "Run a .pl file"
  ],
  "knowledge_refs": [
    "prolog/prolog-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# PROLOG-01-GETTING-STARTED: Getting Started with Prolog

## Introduction

SWI-Prolog, facts, and queries. By the end of this lesson you will be able to: Install SWI-Prolog; Write facts; Ask queries; Run a .pl file.

## Key Concepts

### 1. Install SWI-Prolog

Target: Install SWI-Prolog. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
% facts.pl
likes(mary, pizza).
likes(john, sushi).
```
### 2. Write facts

Target: Write facts. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
swipl facts.pl
?- likes(mary, pizza).
true.
```
### 3. Ask queries

Target: Ask queries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
?- likes(X, pizza).
X = mary.
```
### 4. Run a .pl file

Target: Run a .pl file. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
writeln("Hello, World!").
```

## Practice Questions

1. What is the key idea behind "Getting Started with Prolog"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Prolog with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Prolog"
1. "Provide advanced patterns and performance considerations for Getting Started with Prolog"

## Key Takeaways

- Master the core ideas of Getting Started with Prolog through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
