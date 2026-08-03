---
{
  "title": "Assignments",
  "description": "Set and SetDelayed.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Assign values with =",
    "Use := delayed assignment",
    "Clear variables",
    "Use symbols"
  ],
  "knowledge_refs": [
    "wolfram-language/wolfram-03-variables"
  ],
  "prerequisites": [
    "Wolfram-02: Numbers and Arithmetic"
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

# WOLFRAM-03-VARIABLES: Assignments

## Introduction

Set and SetDelayed. By the end of this lesson you will be able to: Assign values with =; Use := delayed assignment; Clear variables; Use symbols.

## Key Concepts

### 1. Assign values with =

Target: Assign values with =. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wolfram
x = 10
x + 5
```
### 2. Use := delayed assignment

Target: Use := delayed assignment. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wolfram
y = RandomInteger[{1, 10}]
y
```
### 3. Clear variables

Target: Clear variables. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wolfram
y := RandomInteger[{1, 10}]
y
y
```
### 4. Use symbols

Target: Use symbols. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wolfram
Clear[x]
```

## Practice Questions

1. What is the key idea behind "Assignments"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Assignments with analogies and real-world examples"
1. "Show me common mistakes beginners make with Assignments"
1. "Provide advanced patterns and performance considerations for Assignments"

## Key Takeaways

- Master the core ideas of Assignments through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
