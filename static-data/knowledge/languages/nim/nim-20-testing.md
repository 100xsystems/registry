---
{
  "title": "Testing with unittest",
  "description": "Write and run unit tests.",
  "type": "lesson",
  "order": 20,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write test suites",
    "Use check statements",
    "Group tests",
    "Run tests with nimble"
  ],
  "knowledge_refs": [
    "nim/nim-20-testing"
  ],
  "prerequisites": [
    "Nim-19: NimScript and Build Tooling"
  ],
  "references": [
    {
      "title": "Nim Manual",
      "url": "https://nim-lang.org/docs/manual.html",
      "description": "Official language manual"
    },
    {
      "title": "Nim by Example",
      "url": "https://nim-by-example.github.io/",
      "description": "Practical Nim examples"
    },
    {
      "title": "Nim Tutorial",
      "url": "https://nim-lang.org/docs/tut1.html",
      "description": "Official tutorial"
    },
    {
      "title": "Nim Forum",
      "url": "https://forum.nim-lang.org/",
      "description": "Community discussions"
    }
  ]
}
---

# NIM-20-TESTING: Testing with unittest

## Introduction

Write and run unit tests. By the end of this lesson you will be able to: Write test suites; Use check statements; Group tests; Run tests with nimble.

## Key Concepts

### 1. Write test suites

Target: Write test suites. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
import std/unittest

suite "math":
  test "addition":
    check(2 + 2 == 4)
```
### 2. Use check statements

Target: Use check statements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
test "string ops":
  check("abc".len == 3)
  check("a" & "b" == "ab")
```
### 3. Group tests

Target: Group tests. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
test "tables":
  var t = initTable[string, int]()
  t["k"] = 1
  check(t["k"] == 1)
```
### 4. Run tests with nimble

Target: Run tests with nimble. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
require(1 > 0)   # abort on failure
```

## Practice Questions

1. What is the key idea behind "Testing with unittest"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with unittest with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing with unittest"
1. "Provide advanced patterns and performance considerations for Testing with unittest"

## Key Takeaways

- Master the core ideas of Testing with unittest through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
