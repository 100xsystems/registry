---
{
  "title": "Arithmetic",
  "description": "Numbers and arithmetic expressions.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use is for evaluation",
    "Compare numbers",
    "Use arithmetic functions",
    "Build calculators"
  ],
  "knowledge_refs": [
    "prolog/prolog-07-arithmetic"
  ],
  "prerequisites": [
    "Prolog-06: The Cut (!)"
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

# PROLOG-07-ARITHMETIC: Arithmetic

## Introduction

Numbers and arithmetic expressions. By the end of this lesson you will be able to: Use is for evaluation; Compare numbers; Use arithmetic functions; Build calculators.

## Key Concepts

### 1. Use is for evaluation

Target: Use is for evaluation. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
?- X is 2 + 3 * 4.
X = 14.
```
### 2. Compare numbers

Target: Compare numbers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
?- 5 > 3.
true.
```
### 3. Use arithmetic functions

Target: Use arithmetic functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
sum(List, Total) :-
    sum_aux(List, 0, Total).
sum_aux([], Acc, Acc).
sum_aux([H | T], Acc, Total) :-
    Acc1 is Acc + H,
    sum_aux(T, Acc1, Total).
```
### 4. Build calculators

Target: Build calculators. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
X is mod(7, 3).
```

## Practice Questions

1. What is the key idea behind "Arithmetic"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arithmetic with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arithmetic"
1. "Provide advanced patterns and performance considerations for Arithmetic"

## Key Takeaways

- Master the core ideas of Arithmetic through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
