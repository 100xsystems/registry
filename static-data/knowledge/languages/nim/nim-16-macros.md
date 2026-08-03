---
{
  "title": "Macros and Metaprogramming",
  "description": "Compile-time code generation.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand AST concepts",
    "Write simple macros",
    "Use quote and parseExpr",
    "Generate code at compile time"
  ],
  "knowledge_refs": [
    "nim/nim-16-macros"
  ],
  "prerequisites": [
    "Nim-15: Concurrency with Threads"
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

# NIM-16-MACROS: Macros and Metaprogramming

## Introduction

Compile-time code generation. By the end of this lesson you will be able to: Understand AST concepts; Write simple macros; Use quote and parseExpr; Generate code at compile time.

## Key Concepts

### 1. Understand AST concepts

Target: Understand AST concepts. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
import std/macros

macro hello(): untyped =
  result = newLit("hello from macro")

echo hello()
```
### 2. Write simple macros

Target: Write simple macros. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
macro twice(x: untyped): untyped =
  result = quote do:
    `x`
    `x`
```
### 3. Use quote and parseExpr

Target: Use quote and parseExpr. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
import std/macros
echo treeRepr(parseExpr("1 + 2 * 3"))
```
### 4. Generate code at compile time

Target: Generate code at compile time. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
const val = block:
  var s = 0
  for i in 1..10: s += i
  s
echo val
```

## Practice Questions

1. What is the key idea behind "Macros and Metaprogramming"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Macros and Metaprogramming with analogies and real-world examples"
1. "Show me common mistakes beginners make with Macros and Metaprogramming"
1. "Provide advanced patterns and performance considerations for Macros and Metaprogramming"

## Key Takeaways

- Master the core ideas of Macros and Metaprogramming through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
