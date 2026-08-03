---
{
  "title": "Sequences and Arrays",
  "description": "Dynamic sequences and fixed arrays.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create sequences",
    "Index and iterate",
    "Use array literals",
    "Slice collections"
  ],
  "knowledge_refs": [
    "nim/nim-04-collections"
  ],
  "prerequisites": [
    "Nim-03: Control Flow"
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

# NIM-04-COLLECTIONS: Sequences and Arrays

## Introduction

Dynamic sequences and fixed arrays. By the end of this lesson you will be able to: Create sequences; Index and iterate; Use array literals; Slice collections.

## Key Concepts

### 1. Create sequences

Target: Create sequences. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
var nums = @[1, 2, 3]
nums.add(4)
echo nums
```
### 2. Index and iterate

Target: Index and iterate. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
let fixed = [10, 20, 30]
echo fixed[1]
```
### 3. Use array literals

Target: Use array literals. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
for n in nums:
  echo n
```
### 4. Slice collections

Target: Slice collections. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
let a = @[1, 2, 3, 4, 5]
echo a[1..3]   # @[2, 3, 4]
```

## Practice Questions

1. What is the key idea behind "Sequences and Arrays"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Sequences and Arrays with analogies and real-world examples"
1. "Show me common mistakes beginners make with Sequences and Arrays"
1. "Provide advanced patterns and performance considerations for Sequences and Arrays"

## Key Takeaways

- Master the core ideas of Sequences and Arrays through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
