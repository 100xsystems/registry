---
{
  "title": "Exceptions and Error Handling",
  "description": "try/except and raise.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Raise exceptions",
    "Catch with try/except",
    "Use finally",
    "Define custom exceptions"
  ],
  "knowledge_refs": [
    "nim/nim-10-exceptions"
  ],
  "prerequisites": [
    "Nim-09: Generics"
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

# NIM-10-EXCEPTIONS: Exceptions and Error Handling

## Introduction

try/except and raise. By the end of this lesson you will be able to: Raise exceptions; Catch with try/except; Use finally; Define custom exceptions.

## Key Concepts

### 1. Raise exceptions

Target: Raise exceptions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
try:
  let x = parseInt("abc")
except ValueError:
  echo "bad number"
```
### 2. Catch with try/except

Target: Catch with try/except. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
proc check(n: int) =
  if n < 0:
    raise newException(ValueError, "negative")

try:
  check(-1)
except ValueError as e:
  echo e.msg
```
### 3. Use finally

Target: Use finally. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
try:
  risky()
finally:
  echo "always runs"
```
### 4. Define custom exceptions

Target: Define custom exceptions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
type
  MyError = object of CatchableError

raise newException(MyError, "custom failure")
```

## Practice Questions

1. What is the key idea behind "Exceptions and Error Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Exceptions and Error Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Exceptions and Error Handling"
1. "Provide advanced patterns and performance considerations for Exceptions and Error Handling"

## Key Takeaways

- Master the core ideas of Exceptions and Error Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
