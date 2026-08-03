---
{
  "title": "Import and Export",
  "description": "Read and write data.",
  "type": "lesson",
  "order": 14,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Import files",
    "Export data",
    "Handle CSV",
    "Import images"
  ],
  "knowledge_refs": [
    "wolfram-language/wolfram-14-import-export"
  ],
  "prerequisites": [
    "Wolfram-13: Data Frames and Datasets"
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

# WOLFRAM-14-IMPORT-EXPORT: Import and Export

## Introduction

Read and write data. By the end of this lesson you will be able to: Import files; Export data; Handle CSV; Import images.

## Key Concepts

### 1. Import files

Target: Import files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wolfram
Import["data.csv"]
```
### 2. Export data

Target: Export data. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wolfram
Export["out.csv", {{1, 2}, {3, 4}}]
```
### 3. Handle CSV

Target: Handle CSV. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wolfram
Import["image.png"]
```
### 4. Import images

Target: Import images. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wolfram
ImportString["1,2,3", "CSV"]
```

## Practice Questions

1. What is the key idea behind "Import and Export"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Import and Export with analogies and real-world examples"
1. "Show me common mistakes beginners make with Import and Export"
1. "Provide advanced patterns and performance considerations for Import and Export"

## Key Takeaways

- Master the core ideas of Import and Export through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
