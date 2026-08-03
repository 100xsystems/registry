---
{
  "title": "Calculus",
  "description": "Differentiation and integration.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Differentiate",
    "Integrate",
    "Compute limits",
    "Find extrema"
  ],
  "knowledge_refs": [
    "wolfram-language/wolfram-16-calculus"
  ],
  "prerequisites": [
    "Wolfram-15: Symbolic Solving"
  ],
  "references": [
    {
      "title": "Wolfram Language Documentation",
      "url": "https://reference.wolfram.com/language/",
      "description": "Official reference"
    },
    {
      "title": "Wolfram Language Fast Introduction",
      "url": "https://www.wolfram.com/language/fast-introduction-for-programmers/en/",
      "description": "Fast intro"
    },
    {
      "title": "Wolfram Language Guide",
      "url": "https://reference.wolfram.com/language/guide/LanguageOverview.html",
      "description": "Language guide"
    }
  ]
}
---

# WOLFRAM-16-CALCULUS: Calculus

## Introduction

Differentiation and integration. By the end of this lesson you will be able to: Differentiate; Integrate; Compute limits; Find extrema.

## Key Concepts

### 1. Differentiate

Target: Differentiate. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wolfram
D[x^3, x]
```
### 2. Integrate

Target: Integrate. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wolfram
Integrate[x^2, x]
```
### 3. Compute limits

Target: Compute limits. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wolfram
Limit[Sin[x]/x, x -> 0]
```
### 4. Find extrema

Target: Find extrema. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wolfram
Maximize[-x^2 + 4 x, x]
```

## Practice Questions

1. What is the key idea behind "Calculus"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Calculus with analogies and real-world examples"
1. "Show me common mistakes beginners make with Calculus"
1. "Provide advanced patterns and performance considerations for Calculus"

## Key Takeaways

- Master the core ideas of Calculus through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
