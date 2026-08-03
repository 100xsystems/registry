---
{
  "title": "Control Flow",
  "description": "if, case, and loops.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write if/elif/else",
    "Use case statements",
    "Write for and while loops",
    "Use break and continue"
  ],
  "knowledge_refs": [
    "nim/nim-03-control-flow"
  ],
  "prerequisites": [
    "Nim-02: Variables and Types"
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

# NIM-03-CONTROL-FLOW: Control Flow

## Introduction

if, case, and loops. By the end of this lesson you will be able to: Write if/elif/else; Use case statements; Write for and while loops; Use break and continue.

## Key Concepts

### 1. Write if/elif/else

Target: Write if/elif/else. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
let score = 85
if score >= 90:
  echo "A"
elif score >= 80:
  echo "B"
else:
  echo "C"
```
### 2. Use case statements

Target: Use case statements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
let n = 2
case n
of 1: echo "one"
of 2: echo "two"
else: echo "other"
```
### 3. Write for and while loops

Target: Write for and while loops. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
for i in 1..5:
  echo i
```
### 4. Use break and continue

Target: Use break and continue. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
var i = 0
while i < 3:
  inc i
echo i
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
