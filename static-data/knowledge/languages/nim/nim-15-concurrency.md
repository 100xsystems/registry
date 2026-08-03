---
{
  "title": "Concurrency with Threads",
  "description": "Threads, channels, and locks.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Spawn threads",
    "Communicate with channels",
    "Protect shared state",
    "Join threads"
  ],
  "knowledge_refs": [
    "nim/nim-15-concurrency"
  ],
  "prerequisites": [
    "Nim-14: Iterators"
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

# NIM-15-CONCURRENCY: Concurrency with Threads

## Introduction

Threads, channels, and locks. By the end of this lesson you will be able to: Spawn threads; Communicate with channels; Protect shared state; Join threads.

## Key Concepts

### 1. Spawn threads

Target: Spawn threads. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
import std/threadpool

proc work(i: int) =
  echo "task ", i

parallel:
  for i in 1..4:
    spawn work(i)
```
### 2. Communicate with channels

Target: Communicate with channels. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
import std/os

try:
  doWork()
except:
  echo getCurrentExceptionMsg()
```
### 3. Protect shared state

Target: Protect shared state. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
var ch = newChannel[int](4)
ch.send(42)
echo ch.recv()
```
### 4. Join threads

Target: Join threads. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
import std/locks
var L: Lock
initLock(L)
withLock L:
  counter += 1
```

## Practice Questions

1. What is the key idea behind "Concurrency with Threads"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Concurrency with Threads with analogies and real-world examples"
1. "Show me common mistakes beginners make with Concurrency with Threads"
1. "Provide advanced patterns and performance considerations for Concurrency with Threads"

## Key Takeaways

- Master the core ideas of Concurrency with Threads through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
