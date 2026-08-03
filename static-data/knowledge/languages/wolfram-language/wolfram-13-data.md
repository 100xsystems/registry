---
{
  "title": "Data Frames and Datasets",
  "description": "Work with tabular data.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create datasets",
    "Query datasets",
    "Filter rows",
    "Aggregate data"
  ],
  "knowledge_refs": [
    "wolfram-language/wolfram-13-data"
  ],
  "prerequisites": [
    "Wolfram-12: Graphics"
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

# WOLFRAM-13-DATA: Data Frames and Datasets

## Introduction

Work with tabular data. By the end of this lesson you will be able to: Create datasets; Query datasets; Filter rows; Aggregate data.

## Key Concepts

### 1. Create datasets

Target: Create datasets. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wolfram
data = Dataset[{<|"a" -> 1, "b" -> 2|>, <|"a" -> 3, "b" -> 4|>}]
```
### 2. Query datasets

Target: Query datasets. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wolfram
data[All, "a"]
```
### 3. Filter rows

Target: Filter rows. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wolfram
data[Select[#a > 1 &]]
```
### 4. Aggregate data

Target: Aggregate data. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wolfram
data[Total, "b"]
```

## Practice Questions

1. What is the key idea behind "Data Frames and Datasets"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Data Frames and Datasets with analogies and real-world examples"
1. "Show me common mistakes beginners make with Data Frames and Datasets"
1. "Provide advanced patterns and performance considerations for Data Frames and Datasets"

## Key Takeaways

- Master the core ideas of Data Frames and Datasets through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
