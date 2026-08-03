---
{
  "title": "Records and Variants",
  "description": "Record types, discriminants, and variant records.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define record types",
    "Access record components",
    "Use discriminants",
    "Model with variant records"
  ],
  "knowledge_refs": [
    "ada/ada-08-records"
  ],
  "prerequisites": [
    "Ada-07: Arrays"
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

# ADA-08-RECORDS: Records and Variants

## Introduction

Record types, discriminants, and variant records. By the end of this lesson you will be able to: Define record types; Access record components; Use discriminants; Model with variant records.

## Key Concepts

### 1. Define record types

Target: Define record types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
type Point is record
   X, Y : Integer;
end record;
p : Point := (X => 1, Y => 2);
```
### 2. Access record components

Target: Access record components. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
p.X := 10;  -- mutate component
```
### 3. Use discriminants

Target: Use discriminants. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
type Square (Side : Positive) is record
   Area : Integer;
end record;
```
### 4. Model with variant records

Target: Model with variant records. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
type Shape (Kind : Shape_Kind) is record
   case Kind is
      when Circle => Radius : Float;
      when Square => Side   : Float;
   end case;
end record;
```

## Practice Questions

1. What is the key idea behind "Records and Variants"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Records and Variants with analogies and real-world examples"
1. "Show me common mistakes beginners make with Records and Variants"
1. "Provide advanced patterns and performance considerations for Records and Variants"

## Key Takeaways

- Master the core ideas of Records and Variants through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
