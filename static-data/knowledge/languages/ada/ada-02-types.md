---
{
  "title": "Types and Subtypes",
  "description": "Ada's strong typing, ranges, and derived types.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare scalar types with ranges",
    "Create subtypes and derived types",
    "Use type qualification",
    "Understand strong typing benefits"
  ],
  "knowledge_refs": [
    "ada/ada-02-types"
  ],
  "prerequisites": [
    "Ada-01: Getting Started with Ada"
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

# ADA-02-TYPES: Types and Subtypes

## Introduction

Ada's strong typing, ranges, and derived types. By the end of this lesson you will be able to: Declare scalar types with ranges; Create subtypes and derived types; Use type qualification; Understand strong typing benefits.

## Key Concepts

### 1. Declare scalar types with ranges

Target: Declare scalar types with ranges. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
type Day is range 1 .. 31;
today : Day := 15;
```
### 2. Create subtypes and derived types

Target: Create subtypes and derived types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
type Percent is range 0 .. 100;
subtype Grade is Percent range 0 .. 100;
```
### 3. Use type qualification

Target: Use type qualification. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
type Celsius is digits 7 range -273.15 .. 1.0e10;
temp : Celsius := 21.5;
```
### 4. Understand strong typing benefits

Target: Understand strong typing benefits. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
type Colors is (Red, Green, Blue);
c : Colors := Green;
```

## Practice Questions

1. What is the key idea behind "Types and Subtypes"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Types and Subtypes with analogies and real-world examples"
1. "Show me common mistakes beginners make with Types and Subtypes"
1. "Provide advanced patterns and performance considerations for Types and Subtypes"

## Key Takeaways

- Master the core ideas of Types and Subtypes through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
