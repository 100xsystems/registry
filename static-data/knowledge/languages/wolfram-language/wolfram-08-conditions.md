---
{
  "title": "Conditionals",
  "description": "If, Which, and patterns.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use If",
    "Use Which",
    "Use Switch",
    "Use patterns in conditions"
  ],
  "knowledge_refs": [
    "wolfram-language/wolfram-08-conditions"
  ],
  "prerequisites": [
    "Wolfram-07: Strings"
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

# WOLFRAM-08-CONDITIONS: Conditionals

## Introduction

If, Which, and patterns. By the end of this lesson you will be able to: Use If; Use Which; Use Switch; Use patterns in conditions.

## Key Concepts

### 1. Use If

Target: Use If. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wolfram
If[x > 0, "positive", "non-positive"]
```
### 2. Use Which

Target: Use Which. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wolfram
Which[x > 0, "pos", x == 0, "zero", True, "neg"]
```
### 3. Use Switch

Target: Use Switch. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wolfram
Switch[x, 1, "one", 2, "two", _, "other"]
```
### 4. Use patterns in conditions

Target: Use patterns in conditions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wolfram
x_ /; x > 0
```

## Practice Questions

1. What is the key idea behind "Conditionals"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Conditionals with analogies and real-world examples"
1. "Show me common mistakes beginners make with Conditionals"
1. "Provide advanced patterns and performance considerations for Conditionals"

## Key Takeaways

- Master the core ideas of Conditionals through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
