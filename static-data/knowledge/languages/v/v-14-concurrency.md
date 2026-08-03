---
{
  "title": "Concurrency",
  "description": "Threads and channels.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Spawn threads",
    "Use channels",
    "Share data safely",
    "Sync threads"
  ],
  "knowledge_refs": [
    "v/v-14-concurrency"
  ],
  "prerequisites": [
    "V-13: File I/O"
  ],
  "references": [
    {
      "title": "V Documentation",
      "url": "https://docs.vlang.io/",
      "description": "Official docs"
    },
    {
      "title": "V Manual",
      "url": "https://docs.vlang.io/introduction.html",
      "description": "Language manual"
    },
    {
      "title": "V Language GitHub",
      "url": "https://github.com/vlang/v",
      "description": "Source code"
    }
  ]
}
---

# V-14-CONCURRENCY: Concurrency

## Introduction

Threads and channels. By the end of this lesson you will be able to: Spawn threads; Use channels; Share data safely; Sync threads.

## Key Concepts

### 1. Spawn threads

Target: Spawn threads. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
import sync

fn worker(id int) {
	println("worker $id")
}

mut wg := sync.new_waitgroup()
for i in 0..4 {
	wg.add(1)
	go worker(i)
}
wg.wait()
```
### 2. Use channels

Target: Use channels. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
import sync

mut ch := sync.new_channel[int](1)
ch.push(42)
println(ch.pop() or { 0 })
```
### 3. Share data safely

Target: Share data safely. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
spawn fn() {
	println("in goroutine")
}()
```
### 4. Sync threads

Target: Sync threads. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
mut shared := 0
lock {
	shared++
}
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
