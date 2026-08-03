---
{
  "title": "Search Algorithms",
  "description": "Implement DFS and BFS.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Model graphs",
    "Implement DFS",
    "Implement BFS",
    "Find paths"
  ],
  "knowledge_refs": [
    "prolog/prolog-17-search"
  ],
  "prerequisites": [
    "Prolog-16: Sudoku Solver"
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

# PROLOG-17-SEARCH: Search Algorithms

## Introduction

Implement DFS and BFS. By the end of this lesson you will be able to: Model graphs; Implement DFS; Implement BFS; Find paths.

## Key Concepts

### 1. Model graphs

Target: Model graphs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
edge(a, b).
edge(b, c).
edge(a, c).
```
### 2. Implement DFS

Target: Implement DFS. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
path(X, X, [X]).
path(X, Y, [X | P]) :-
    edge(X, Z),
    path(Z, Y, P).
```
### 3. Implement BFS

Target: Implement BFS. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
bfs(Start, Goal) :-
    bfs([[Start]], Goal, Path).
```
### 4. Find paths

Target: Find paths. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
?- path(a, c, P).
```

## Practice Questions

1. What is the key idea behind "Search Algorithms"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Search Algorithms with analogies and real-world examples"
1. "Show me common mistakes beginners make with Search Algorithms"
1. "Provide advanced patterns and performance considerations for Search Algorithms"

## Key Takeaways

- Master the core ideas of Search Algorithms through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
