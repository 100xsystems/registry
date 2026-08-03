---
{
  "title": "Testing",
  "description": "Unit tests with purescript-spec.",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Set up purescript-spec",
    "Write specs",
    "Run tests",
    "Test pure functions"
  ],
  "knowledge_refs": [
    "purescript/purescript-18-testing"
  ],
  "prerequisites": [
    "PureScript-17: Asynchronous with Aff"
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

# PURESCRIPT-18-TESTING: Testing

## Introduction

Unit tests with purescript-spec. By the end of this lesson you will be able to: Set up purescript-spec; Write specs; Run tests; Test pure functions.

## Key Concepts

### 1. Set up purescript-spec

Target: Set up purescript-spec. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
import Test.Spec (describe, it, Spec)
import Test.Spec.Assertions (shouldEqual)
```
### 2. Write specs

Target: Write specs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
spec :: Spec Unit
spec = describe "math" do
  it "adds" do
    (2 + 2) `shouldEqual` 4
```
### 3. Run tests

Target: Run tests. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
spago test
```
### 4. Test pure functions

Target: Test pure functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
it "works with strings" do
  ("ab" <> "cd") `shouldEqual` "abcd"
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
