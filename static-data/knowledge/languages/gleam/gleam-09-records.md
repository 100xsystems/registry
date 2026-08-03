---
{
  "title": "Records",
  "description": "Named fields and updates.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define record types",
    "Create records",
    "Access fields",
    "Update records"
  ],
  "knowledge_refs": [
    "gleam/gleam-09-records"
  ],
  "prerequisites": [
    "Gleam-08: Custom Types"
  ],
  "references": [
    {
      "title": "Gleam Documentation",
      "url": "https://gleam.run/documentation/",
      "description": "Official docs"
    },
    {
      "title": "Gleam Language Tour",
      "url": "https://tour.gleam.run/",
      "description": "Interactive tour"
    },
    {
      "title": "Gleam Book",
      "url": "https://gleam.run/book/",
      "description": "The official book"
    }
  ]
}
---

# GLEAM-09-RECORDS: Records

## Introduction

Named fields and updates. By the end of this lesson you will be able to: Define record types; Create records; Access fields; Update records.

## Key Concepts

### 1. Define record types

Target: Define record types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
pub type Person {
  Person(name: String, age: Int)
}

let ada = Person("Ada", 36)
```
### 2. Create records

Target: Create records. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
io.debug(ada.name)
```
### 3. Access fields

Target: Access fields. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
let older = Person(..ada, age: 37)
```
### 4. Update records

Target: Update records. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
pub fn describe(p: Person) -> String {
  p.name <> " is " <> int.to_string(p.age)
}
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
