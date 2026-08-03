---
{
  "title": "Lists",
  "description": "The core data structure.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create lists",
    "Access elements",
    "Map functions",
    "Use list functions"
  ],
  "knowledge_refs": [
    "wolfram-language/wolfram-04-lists"
  ],
  "prerequisites": [
    "Wolfram-03: Assignments"
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

# WOLFRAM-04-LISTS: Lists

## Introduction

The core data structure. By the end of this lesson you will be able to: Create lists; Access elements; Map functions; Use list functions.

## Key Concepts

### 1. Create lists

Target: Create lists. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wolfram
list = {1, 2, 3, 4, 5}
```
### 2. Access elements

Target: Access elements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wolfram
list[[2]]
First[list]
Last[list]
```
### 3. Map functions

Target: Map functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wolfram
Map[#^2 &, list]
list^2
```
### 4. Use list functions

Target: Use list functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wolfram
Total[list]
Length[list]
Sort[list]
```

## Practice Questions

1. What is the key idea behind "Lists"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lists with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lists"
1. "Provide advanced patterns and performance considerations for Lists"

## Key Takeaways

- Master the core ideas of Lists through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
