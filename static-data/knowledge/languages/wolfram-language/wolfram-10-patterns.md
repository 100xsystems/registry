---
{
  "title": "Pattern Matching",
  "description": "The heart of the language.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use blank patterns",
    "Use pattern rules",
    "Define replacements",
    "Use ReplaceAll"
  ],
  "knowledge_refs": [
    "wolfram-language/wolfram-10-patterns"
  ],
  "prerequisites": [
    "Wolfram-09: Iteration"
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

# WOLFRAM-10-PATTERNS: Pattern Matching

## Introduction

The heart of the language. By the end of this lesson you will be able to: Use blank patterns; Use pattern rules; Define replacements; Use ReplaceAll.

## Key Concepts

### 1. Use blank patterns

Target: Use blank patterns. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wolfram
f[x_] := x^2
```
### 2. Use pattern rules

Target: Use pattern rules. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wolfram
expr = x^2 + 2 x + 1
expr /. x -> 3
```
### 3. Define replacements

Target: Define replacements. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wolfram
{1, 2, 3} /. x_Integer -> x^2
```
### 4. Use ReplaceAll

Target: Use ReplaceAll. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wolfram
MatchQ[5, _Integer]
```

## Practice Questions

1. What is the key idea behind "Pattern Matching"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Pattern Matching with analogies and real-world examples"
1. "Show me common mistakes beginners make with Pattern Matching"
1. "Provide advanced patterns and performance considerations for Pattern Matching"

## Key Takeaways

- Master the core ideas of Pattern Matching through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
