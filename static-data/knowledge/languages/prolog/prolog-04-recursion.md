---
{
  "title": "Recursion",
  "description": "Recursive rules for lists and trees.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write recursive rules",
    "Use base cases",
    "Use recursive cases",
    "Trace recursion"
  ],
  "knowledge_refs": [
    "prolog/prolog-04-recursion"
  ],
  "prerequisites": [
    "Prolog-03: Unification"
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

# PROLOG-04-RECURSION: Recursion

## Introduction

Recursive rules for lists and trees. By the end of this lesson you will be able to: Write recursive rules; Use base cases; Use recursive cases; Trace recursion.

## Key Concepts

### 1. Write recursive rules

Target: Write recursive rules. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
descendant(X, Y) :- child(X, Y).
descendant(X, Y) :- child(X, Z), descendant(Z, Y).
```
### 2. Use base cases

Target: Use base cases. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
factorial(0, 1).
factorial(N, F) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, F1),
    F is N * F1.
```
### 3. Use recursive cases

Target: Use recursive cases. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
?- factorial(5, F).
F = 120.
```
### 4. Trace recursion

Target: Trace recursion. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
trace.
factorial(3, F).
```

## Practice Questions

1. What is the key idea behind "Recursion"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Recursion with analogies and real-world examples"
1. "Show me common mistakes beginners make with Recursion"
1. "Provide advanced patterns and performance considerations for Recursion"

## Key Takeaways

- Master the core ideas of Recursion through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
