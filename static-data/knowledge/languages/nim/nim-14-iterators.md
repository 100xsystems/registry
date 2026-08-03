---
{
  "title": "Iterators",
  "description": "Custom iteration logic.",
  "type": "lesson",
  "order": 14,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write iterator procs",
    "Use yield",
    "Chain iterators",
    "Build lazy sequences"
  ],
  "knowledge_refs": [
    "nim/nim-14-iterators"
  ],
  "prerequisites": [
    "Nim-13: Streams and stdin/stdout"
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

# NIM-14-ITERATORS: Iterators

## Introduction

Custom iteration logic. By the end of this lesson you will be able to: Write iterator procs; Use yield; Chain iterators; Build lazy sequences.

## Key Concepts

### 1. Write iterator procs

Target: Write iterator procs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
iterator countdownFrom(n: int): int =
  var i = n
  while i >= 0:
    yield i
    dec i

for x in countdownFrom(3):
  echo x
```
### 2. Use yield

Target: Use yield. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
iterator doubles(s: seq[int]): int =
  for x in s:
    yield x * 2
```
### 3. Chain iterators

Target: Chain iterators. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
iterator fib(n: int): int =
  var a, b = 1
  for _ in 1..n:
    yield a
    (a, b) = (b, a + b)
```
### 4. Build lazy sequences

Target: Build lazy sequences. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
for even in filterIt(toSeq(1..10), it mod 2 == 0):
  echo even
```

## Practice Questions

1. What is the key idea behind "Iterators"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Iterators with analogies and real-world examples"
1. "Show me common mistakes beginners make with Iterators"
1. "Provide advanced patterns and performance considerations for Iterators"

## Key Takeaways

- Master the core ideas of Iterators through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
