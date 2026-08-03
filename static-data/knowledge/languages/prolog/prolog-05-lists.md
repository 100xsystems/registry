---
{
  "title": "Lists",
  "description": "Build and process lists.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use list syntax",
    "Pattern match head/tail",
    "Write list predicates",
    "Use append"
  ],
  "knowledge_refs": [
    "prolog/prolog-05-lists"
  ],
  "prerequisites": [
    "Prolog-04: Recursion"
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

# PROLOG-05-LISTS: Lists

## Introduction

Build and process lists. By the end of this lesson you will be able to: Use list syntax; Pattern match head/tail; Write list predicates; Use append.

## Key Concepts

### 1. Use list syntax

Target: Use list syntax. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
?- [a, b, c] = [H | T].
H = a, T = [b, c].
```
### 2. Pattern match head/tail

Target: Pattern match head/tail. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
member(X, [X | _]).
member(X, [_ | T]) :- member(X, T).
```
### 3. Write list predicates

Target: Write list predicates. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
len([], 0).
len([_ | T], N) :- len(T, N1), N is N1 + 1.
```
### 4. Use append

Target: Use append. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
append([], L, L).
append([H | T], L, [H | R]) :- append(T, L, R).
```

## Practice Questions

1. What is the key idea behind "Lists"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lists with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lists"
1. "Provide advanced patterns and performance considerations for Lists"

## Key Takeaways

- Master the core ideas of Lists through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
