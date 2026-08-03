---
{
  "title": "Findall and Setof",
  "description": "Collect solutions.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use findall",
    "Use bagof",
    "Use setof",
    "Aggregate results"
  ],
  "knowledge_refs": [
    "prolog/prolog-10-findall"
  ],
  "prerequisites": [
    "Prolog-09: Assert and Retract"
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

# PROLOG-10-FINDALL: Findall and Setof

## Introduction

Collect solutions. By the end of this lesson you will be able to: Use findall; Use bagof; Use setof; Aggregate results.

## Key Concepts

### 1. Use findall

Target: Use findall. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
findall(X, likes(mary, X), L).
```
### 2. Use bagof

Target: Use bagof. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
findall(X, parent(tom, X), Children).
```
### 3. Use setof

Target: Use setof. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
setof(X, likes(_, X), Unique).
```
### 4. Aggregate results

Target: Aggregate results. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
aggregate_all(count, parent(_, _), Count).
```

## Practice Questions

1. What is the key idea behind "Findall and Setof"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Findall and Setof with analogies and real-world examples"
1. "Show me common mistakes beginners make with Findall and Setof"
1. "Provide advanced patterns and performance considerations for Findall and Setof"

## Key Takeaways

- Master the core ideas of Findall and Setof through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
