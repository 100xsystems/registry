---
{
  "title": "Arrays",
  "description": "Indexed and multi-dimensional arrays with bounds.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Declare array types",
    "Use array slices",
    "Iterate with attributes",
    "Build multi-dimensional arrays"
  ],
  "knowledge_refs": [
    "ada/ada-07-arrays"
  ],
  "prerequisites": [
    "Ada-06: Strings"
  ],
  "references": [
    {
      "title": "Ada Reference Manual",
      "url": "https://www.adaic.org/resources/add_content/standards/",
      "description": "The official language standard"
    },
    {
      "title": "Learn Ada",
      "url": "https://learn.adacore.com/",
      "description": "AdaCore official interactive course"
    },
    {
      "title": "Ada Programming (Wikibooks)",
      "url": "https://en.wikibooks.org/wiki/Ada_Programming",
      "description": "Community textbook"
    }
  ]
}
---

# ADA-07-ARRAYS: Arrays

## Introduction

Indexed and multi-dimensional arrays with bounds. By the end of this lesson you will be able to: Declare array types; Use array slices; Iterate with attributes; Build multi-dimensional arrays.

## Key Concepts

### 1. Declare array types

Target: Declare array types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
type Vector is array (1 .. 10) of Integer;
v : Vector := (others => 0);
```
### 2. Use array slices

Target: Use array slices. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
Matrix : array (1 .. 3, 1 .. 3) of Integer := (others => (others => 0));
```
### 3. Iterate with attributes

Target: Iterate with attributes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
scores : array (1 .. 5) of Integer := (10, 20, 30, 40, 50);
slice : array (1 .. 2) of Integer := scores (2 .. 3);
```
### 4. Build multi-dimensional arrays

Target: Build multi-dimensional arrays. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
for i in v'Range loop
   Put (Integer'Image (v (i)));
end loop;
```

## Practice Questions

1. What is the key idea behind "Arrays"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays"
1. "Provide advanced patterns and performance considerations for Arrays"

## Key Takeaways

- Master the core ideas of Arrays through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
