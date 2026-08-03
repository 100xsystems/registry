---
{
  "title": "Assert and Retract",
  "description": "Dynamic knowledge bases.",
  "type": "lesson",
  "order": 9,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Assert facts dynamically",
    "Retract facts",
    "Use dynamic declarations",
    "Build expert systems"
  ],
  "knowledge_refs": [
    "prolog/prolog-09-assert-retract"
  ],
  "prerequisites": [
    "Prolog-08: Atoms, Strings, and Text"
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

# PROLOG-09-ASSERT-RETRACT: Assert and Retract

## Introduction

Dynamic knowledge bases. By the end of this lesson you will be able to: Assert facts dynamically; Retract facts; Use dynamic declarations; Build expert systems.

## Key Concepts

### 1. Assert facts dynamically

Target: Assert facts dynamically. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
:- dynamic visited/1.
assert(visited(mars)).
```
### 2. Retract facts

Target: Retract facts. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
visited(X).
```
### 3. Use dynamic declarations

Target: Use dynamic declarations. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
retract(visited(mars)).
```
### 4. Build expert systems

Target: Build expert systems. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
add_fact(P, C) :-
    assertz(parent(P, C)).
```

## Practice Questions

1. What is the key idea behind "Assert and Retract"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Assert and Retract with analogies and real-world examples"
1. "Show me common mistakes beginners make with Assert and Retract"
1. "Provide advanced patterns and performance considerations for Assert and Retract"

## Key Takeaways

- Master the core ideas of Assert and Retract through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
