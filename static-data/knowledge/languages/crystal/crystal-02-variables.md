---
{
  "title": "Variables and Types",
  "description": "Type inference, unions, and constants.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use type inference",
    "Declare explicit types",
    "Use unions",
    "Define constants"
  ],
  "knowledge_refs": [
    "crystal/crystal-02-variables"
  ],
  "prerequisites": [
    "Crystal-01: Getting Started with Crystal"
  ],
  "references": [
    {
      "title": "Crystal Language Reference",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official docs"
    },
    {
      "title": "Crystal for Rubyists",
      "url": "https://crystal-lang.org/reference/guides/faq.html",
      "description": "Migration guide"
    },
    {
      "title": "Crystal Book",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official reference book"
    },
    {
      "title": "Crystal Forum",
      "url": "https://forum.crystal-lang.org/",
      "description": "Community"
    }
  ]
}
---

# CRYSTAL-02-VARIABLES: Variables and Types

## Introduction

Type inference, unions, and constants. By the end of this lesson you will be able to: Use type inference; Declare explicit types; Use unions; Define constants.

## Key Concepts

### 1. Use type inference

Target: Use type inference. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
x = 42
puts x.class
```
### 2. Declare explicit types

Target: Declare explicit types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
y : Int32 = 10
puts y
```
### 3. Use unions

Target: Use unions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
value = "hello"
value = 42   # union of String | Int32
puts value
```
### 4. Define constants

Target: Define constants. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
MAX = 100
puts MAX
```

## Practice Questions

1. What is the key idea behind "Variables and Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Types"
1. "Provide advanced patterns and performance considerations for Variables and Types"

## Key Takeaways

- Master the core ideas of Variables and Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
