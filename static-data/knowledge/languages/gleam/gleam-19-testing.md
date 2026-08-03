---
{
  "title": "Testing",
  "description": "Write unit tests with gleeunit.",
  "type": "lesson",
  "order": 19,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Set up gleeunit",
    "Write test functions",
    "Run gleam test",
    "Test pure functions"
  ],
  "knowledge_refs": [
    "gleam/gleam-19-testing"
  ],
  "prerequisites": [
    "Gleam-18: JSON"
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

# GLEAM-19-TESTING: Testing

## Introduction

Write unit tests with gleeunit. By the end of this lesson you will be able to: Set up gleeunit; Write test functions; Run gleam test; Test pure functions.

## Key Concepts

### 1. Set up gleeunit

Target: Set up gleeunit. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
import gleeunit
import gleeunit/should

pub fn main() {
  gleeunit.main()
}

pub fn add(a: Int, b: Int) -> Int {
  a + b
}

pub fn add_test() {
  should.equal(add(2, 3), 5)
}
```
### 2. Write test functions

Target: Write test functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
gleam test
```
### 3. Run gleam test

Target: Run gleam test. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
pub fn square_test() {
  should.equal(square(4), 16)
}
```
### 4. Test pure functions

Target: Test pure functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
should.equal(string.uppercase("hi"), "HI")
```

## Practice Questions

1. What is the key idea behind "Testing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing"
1. "Provide advanced patterns and performance considerations for Testing"

## Key Takeaways

- Master the core ideas of Testing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
