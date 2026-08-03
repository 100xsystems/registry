---
{
  "title": "Tables and Sets",
  "description": "Hash tables and sets from stdlib.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create tables",
    "Insert and lookup",
    "Iterate key-value pairs",
    "Use sets"
  ],
  "knowledge_refs": [
    "nim/nim-11-tables"
  ],
  "prerequisites": [
    "Nim-10: Exceptions and Error Handling"
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

# NIM-11-TABLES: Tables and Sets

## Introduction

Hash tables and sets from stdlib. By the end of this lesson you will be able to: Create tables; Insert and lookup; Iterate key-value pairs; Use sets.

## Key Concepts

### 1. Create tables

Target: Create tables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
import std/tables

var ages = initTable[string, int]()
ages["ada"] = 36
echo ages["ada"]
```
### 2. Insert and lookup

Target: Insert and lookup. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
let caps = {"us": "DC", "uk": "London"}.toTable
echo caps["us"]
```
### 3. Iterate key-value pairs

Target: Iterate key-value pairs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
for k, v in ages:
  echo k, ": ", v
```
### 4. Use sets

Target: Use sets. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
import std/sets
var s = toHashSet([1, 2, 3])
if 2 in s: echo "yes"
```

## Practice Questions

1. What is the key idea behind "Tables and Sets"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Tables and Sets with analogies and real-world examples"
1. "Show me common mistakes beginners make with Tables and Sets"
1. "Provide advanced patterns and performance considerations for Tables and Sets"

## Key Takeaways

- Master the core ideas of Tables and Sets through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
