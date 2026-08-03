---
{
  "title": "Modules and Libraries",
  "description": "Organize Prolog code.",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create modules",
    "Export predicates",
    "Import modules",
    "Use SWI libraries"
  ],
  "knowledge_refs": [
    "prolog/prolog-18-modules"
  ],
  "prerequisites": [
    "Prolog-17: Search Algorithms"
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

# PROLOG-18-MODULES: Modules and Libraries

## Introduction

Organize Prolog code. By the end of this lesson you will be able to: Create modules; Export predicates; Import modules; Use SWI libraries.

## Key Concepts

### 1. Create modules

Target: Create modules. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
:- module(math_utils, [square/2]).
square(X, Y) :- Y is X * X.
```
### 2. Export predicates

Target: Export predicates. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
:- use_module(math_utils).
```
### 3. Import modules

Target: Import modules. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
use_module(library(lists)).
```
### 4. Use SWI libraries

Target: Use SWI libraries. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
use_module(library(dcg/basics)).
```

## Practice Questions

1. What is the key idea behind "Modules and Libraries"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Modules and Libraries with analogies and real-world examples"
1. "Show me common mistakes beginners make with Modules and Libraries"
1. "Provide advanced patterns and performance considerations for Modules and Libraries"

## Key Takeaways

- Master the core ideas of Modules and Libraries through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
