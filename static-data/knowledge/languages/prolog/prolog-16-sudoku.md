---
{
  "title": "Sudoku Solver",
  "description": "A classic CLP(FD) program.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Model a grid",
    "Set up constraints",
    "Run label search",
    "Verify solutions"
  ],
  "knowledge_refs": [
    "prolog/prolog-16-sudoku"
  ],
  "prerequisites": [
    "Prolog-15: Constraint Handling"
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

# PROLOG-16-SUDOKU: Sudoku Solver

## Introduction

A classic CLP(FD) program. By the end of this lesson you will be able to: Model a grid; Set up constraints; Run label search; Verify solutions.

## Key Concepts

### 1. Model a grid

Target: Model a grid. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
sudoku(Rows) :-
    length(Rows, 9),
    maplist(same_length(Rows), Rows),
    append(Rows, Vs), Vs ins 1..9,
    maplist(all_distinct, Rows),
    transpose(Rows, Cols),
    maplist(all_distinct, Cols),
    Rows = [A, B, C, D, E, F, G, H, I],
    blocks(A, B, C), blocks(D, E, F), blocks(G, H, I),
    label(Vs).
```
### 2. Set up constraints

Target: Set up constraints. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
all_distinct([1, 2, 3]).
```
### 3. Run label search

Target: Run label search. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
X in 1..9, X #\= 2.
```
### 4. Verify solutions

Target: Verify solutions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
labeling([], Vs).
```

## Practice Questions

1. What is the key idea behind "Sudoku Solver"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Sudoku Solver with analogies and real-world examples"
1. "Show me common mistakes beginners make with Sudoku Solver"
1. "Provide advanced patterns and performance considerations for Sudoku Solver"

## Key Takeaways

- Master the core ideas of Sudoku Solver through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
