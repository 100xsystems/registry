---
{
  "title": "Functions",
  "description": "Define and use functions.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define pure functions",
    "Use # and &",
    "Define named functions",
    "Use function options"
  ],
  "knowledge_refs": [
    "wolfram-language/wolfram-05-functions"
  ],
  "prerequisites": [
    "Wolfram-04: Lists"
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

# WOLFRAM-05-FUNCTIONS: Functions

## Introduction

Define and use functions. By the end of this lesson you will be able to: Define pure functions; Use # and &; Define named functions; Use function options.

## Key Concepts

### 1. Define pure functions

Target: Define pure functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wolfram
square[x_] := x^2
square[5]
```
### 2. Use # and &

Target: Use # and &. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wolfram
#^2 &[5]
```
### 3. Define named functions

Target: Define named functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wolfram
Map[# * 2 &, {1, 2, 3}]
```
### 4. Use function options

Target: Use function options. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wolfram
f[x_, y_] := x^2 + y^2
f[3, 4]
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
