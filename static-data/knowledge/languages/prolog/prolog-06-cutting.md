---
{
  "title": "The Cut (!)",
  "description": "Control backtracking.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Understand backtracking",
    "Use cut to stop search",
    "Use cut-fail",
    "Use negation as failure"
  ],
  "knowledge_refs": [
    "prolog/prolog-06-cutting"
  ],
  "prerequisites": [
    "Prolog-05: Lists"
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

# PROLOG-06-CUTTING: The Cut (!)

## Introduction

Control backtracking. By the end of this lesson you will be able to: Understand backtracking; Use cut to stop search; Use cut-fail; Use negation as failure.

## Key Concepts

### 1. Understand backtracking

Target: Understand backtracking. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
```
### 2. Use cut to stop search

Target: Use cut to stop search. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
not(X) :- X, !, fail.
not(_).
```
### 3. Use cut-fail

Target: Use cut-fail. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
member_opt(X, [X | _]) :- !.
member_opt(X, [_ | T]) :- member_opt(X, T).
```
### 4. Use negation as failure

Target: Use negation as failure. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
positive(X) :- X > 0, !.
positive(_) :- fail.
```

## Practice Questions

1. What is the key idea behind "The Cut (!)"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain The Cut (!) with analogies and real-world examples"
1. "Show me common mistakes beginners make with The Cut (!)"
1. "Provide advanced patterns and performance considerations for The Cut (!)"

## Key Takeaways

- Master the core ideas of The Cut (!) through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
