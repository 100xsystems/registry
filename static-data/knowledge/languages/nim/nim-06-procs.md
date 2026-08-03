---
{
  "title": "Procedures",
  "description": "Write typed procedures with defaults.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write procedures",
    "Use return types",
    "Provide default args",
    "Use named arguments"
  ],
  "knowledge_refs": [
    "nim/nim-06-procs"
  ],
  "prerequisites": [
    "Nim-05: Strings"
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

# NIM-06-PROCS: Procedures

## Introduction

Write typed procedures with defaults. By the end of this lesson you will be able to: Write procedures; Use return types; Provide default args; Use named arguments.

## Key Concepts

### 1. Write procedures

Target: Write procedures. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
proc add(a, b: int): int =
  result = a + b

echo add(2, 3)
```
### 2. Use return types

Target: Use return types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
proc greet(name: string, excited = false) =
  if excited:
    echo name, "!!"
  else:
    echo name

greet("Ada", excited = true)
```
### 3. Provide default args

Target: Provide default args. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
proc double(x: int): int = x * 2
```
### 4. Use named arguments

Target: Use named arguments. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
proc swapInts(a, b: var int) =
  let tmp = a
  a = b
  b = tmp
```

## Practice Questions

1. What is the key idea behind "Procedures"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Procedures with analogies and real-world examples"
1. "Show me common mistakes beginners make with Procedures"
1. "Provide advanced patterns and performance considerations for Procedures"

## Key Takeaways

- Master the core ideas of Procedures through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
