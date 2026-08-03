---
{
  "title": "Debugging Prolog",
  "description": "Trace and inspect.",
  "type": "lesson",
  "order": 19,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use trace",
    "Set spy points",
    "Use debug predicates",
    "Profile queries"
  ],
  "knowledge_refs": [
    "prolog/prolog-19-debugging"
  ],
  "prerequisites": [
    "Prolog-18: Modules and Libraries"
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

# PROLOG-19-DEBUGGING: Debugging Prolog

## Introduction

Trace and inspect. By the end of this lesson you will be able to: Use trace; Set spy points; Use debug predicates; Profile queries.

## Key Concepts

### 1. Use trace

Target: Use trace. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
trace.
factorial(5, F).
```
### 2. Set spy points

Target: Set spy points. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
spy(factorial/2).
```
### 3. Use debug predicates

Target: Use debug predicates. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
debug.
```
### 4. Profile queries

Target: Profile queries. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
statistics(runtime, [T, _]).
```

## Practice Questions

1. What is the key idea behind "Debugging Prolog"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Debugging Prolog with analogies and real-world examples"
1. "Show me common mistakes beginners make with Debugging Prolog"
1. "Provide advanced patterns and performance considerations for Debugging Prolog"

## Key Takeaways

- Master the core ideas of Debugging Prolog through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
