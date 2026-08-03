---
{
  "title": "SPARK and Formal Methods",
  "description": "High-integrity subset with proof tools.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand SPARK subset rules",
    "Annotate with contracts",
    "Run proof tools",
    "Write provable code"
  ],
  "knowledge_refs": [
    "ada/ada-19-spark"
  ],
  "prerequisites": [
    "Ada-18: Pragmas and Preconditions"
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

# ADA-19-SPARK: SPARK and Formal Methods

## Introduction

High-integrity subset with proof tools. By the end of this lesson you will be able to: Understand SPARK subset rules; Annotate with contracts; Run proof tools; Write provable code.

## Key Concepts

### 1. Understand SPARK subset rules

Target: Understand SPARK subset rules. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
pragma SPARK_Mode (On);
```
### 2. Annotate with contracts

Target: Annotate with contracts. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
procedure Increment (X : in out Integer)
   with Pre  => X < Integer'Last,
        Post => X = X'Old + 1;
```
### 3. Run proof tools

Target: Run proof tools. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
pragma Assert (X >= 0);
```
### 4. Write provable code

Target: Write provable code. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
function Max (A, B : Integer) return Integer
   with Post => Max'Result >= A and Max'Result >= B;
```

## Practice Questions

1. What is the key idea behind "SPARK and Formal Methods"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain SPARK and Formal Methods with analogies and real-world examples"
1. "Show me common mistakes beginners make with SPARK and Formal Methods"
1. "Provide advanced patterns and performance considerations for SPARK and Formal Methods"

## Key Takeaways

- Master the core ideas of SPARK and Formal Methods through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
