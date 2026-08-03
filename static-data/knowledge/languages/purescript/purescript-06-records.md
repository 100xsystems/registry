---
{
  "title": "Records",
  "description": "Named fields.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create records",
    "Access fields",
    "Update records",
    "Use record puns"
  ],
  "knowledge_refs": [
    "purescript/purescript-06-records"
  ],
  "prerequisites": [
    "PureScript-05: Arrays"
  ],
  "references": [
    {
      "title": "PureScript Documentation",
      "url": "https://pursuit.purescript.org/",
      "description": "Official package search"
    },
    {
      "title": "PureScript by Example",
      "url": "https://book.purescript.org/",
      "description": "The official book"
    },
    {
      "title": "PureScript Guide",
      "url": "https://github.com/JordanMartinez/purescript-jordans-reference",
      "description": "Community reference"
    }
  ]
}
---

# PURESCRIPT-06-RECORDS: Records

## Introduction

Named fields. By the end of this lesson you will be able to: Create records; Access fields; Update records; Use record puns.

## Key Concepts

### 1. Create records

Target: Create records. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
type Person = { name :: String, age :: Int }

ada :: Person
ada = { name: "Ada", age: 36 }
```
### 2. Access fields

Target: Access fields. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
ada.name
```
### 3. Update records

Target: Update records. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
older = ada { age = 37 }
```
### 4. Use record puns

Target: Use record puns. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
describe :: Person -> String
describe { name, age } = name <> " is " <> show age
```

## Practice Questions

1. What is the key idea behind "Records"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Records with analogies and real-world examples"
1. "Show me common mistakes beginners make with Records"
1. "Provide advanced patterns and performance considerations for Records"

## Key Takeaways

- Master the core ideas of Records through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
