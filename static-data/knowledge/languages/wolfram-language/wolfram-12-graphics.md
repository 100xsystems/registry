---
{
  "title": "Graphics",
  "description": "Draw primitives.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use graphics primitives",
    "Style shapes",
    "Compose scenes",
    "Export images"
  ],
  "knowledge_refs": [
    "wolfram-language/wolfram-12-graphics"
  ],
  "prerequisites": [
    "Wolfram-11: Associations"
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

# WOLFRAM-12-GRAPHICS: Graphics

## Introduction

Draw primitives. By the end of this lesson you will be able to: Use graphics primitives; Style shapes; Compose scenes; Export images.

## Key Concepts

### 1. Use graphics primitives

Target: Use graphics primitives. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wolfram
Graphics[{Circle[], Rectangle[]}]
```
### 2. Style shapes

Target: Style shapes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wolfram
Graphics[{Red, Disk[{0, 0}, 1]}]
```
### 3. Compose scenes

Target: Compose scenes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wolfram
Graphics[{Line[{{0, 0}, {1, 1}}]}]
```
### 4. Export images

Target: Export images. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wolfram
Export["circle.png", Graphics[Circle[]]]
```

## Practice Questions

1. What is the key idea behind "Graphics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Graphics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Graphics"
1. "Provide advanced patterns and performance considerations for Graphics"

## Key Takeaways

- Master the core ideas of Graphics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
