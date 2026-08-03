---
{
  "title": "Concurrency",
  "description": "Threads, messages, and shared data.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Spawn threads",
    "Use synchronized",
    "Pass messages",
    "Use shared memory"
  ],
  "knowledge_refs": [
    "d/d-14-concurrency"
  ],
  "prerequisites": [
    "D-13: Templates and Generics"
  ],
  "references": [
    {
      "title": "D Language Reference",
      "url": "https://dlang.org/spec/spec.html",
      "description": "Official language spec"
    },
    {
      "title": "D Programming Tour",
      "url": "https://tour.dlang.org/",
      "description": "Interactive language tour"
    },
    {
      "title": "D Wiki",
      "url": "https://wiki.dlang.org/",
      "description": "Community wiki"
    },
    {
      "title": "DUB Package Manager",
      "url": "https://code.dlang.org/",
      "description": "Package registry"
    }
  ]
}
---

# D-14-CONCURRENCY: Concurrency

## Introduction

Threads, messages, and shared data. By the end of this lesson you will be able to: Spawn threads; Use synchronized; Pass messages; Use shared memory.

## Key Concepts

### 1. Spawn threads

Target: Spawn threads. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
import std.stdio;
import core.thread;

void work() {
    writeln("in thread");
}

void main() {
    auto t = new Thread(&work);
    t.start();
    t.join();
}
```
### 2. Use synchronized

Target: Use synchronized. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
import std.concurrency;

auto tid = spawn(() => 42);
writeln(receiveOnly!int);
```
### 3. Pass messages

Target: Pass messages. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
int counter;
synchronized void inc() {
    counter++;
}
```
### 4. Use shared memory

Target: Use shared memory. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
shared int x;
// use with care — D keeps shared memory explicit
```

## Practice Questions

1. What is the key idea behind "Concurrency"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Concurrency with analogies and real-world examples"
1. "Show me common mistakes beginners make with Concurrency"
1. "Provide advanced patterns and performance considerations for Concurrency"

## Key Takeaways

- Master the core ideas of Concurrency through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
