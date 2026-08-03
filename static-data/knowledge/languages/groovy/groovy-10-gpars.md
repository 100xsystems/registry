---
{
  "title": "Concurrency with GPars",
  "description": "Parallel and async programming.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use parallel collections",
    "Create async tasks",
    "Use dataflow",
    "Coordinate actors"
  ],
  "knowledge_refs": [
    "groovy/groovy-10-gpars"
  ],
  "prerequisites": [
    "Groovy-09: Metaprogramming"
  ],
  "references": [
    {
      "title": "Groovy Documentation",
      "url": "https://groovy-lang.org/documentation.html",
      "description": "Official docs"
    },
    {
      "title": "Groovy Tutorial (Groovy-lang)",
      "url": "https://groovy-lang.org/single-page-documentation.html",
      "description": "Official reference"
    },
    {
      "title": "Groovy in Action",
      "url": "https://www.manning.com/books/groovy-in-action-second-edition",
      "description": "Book"
    }
  ]
}
---

# GROOVY-10-GPARS: Concurrency with GPars

## Introduction

Parallel and async programming. By the end of this lesson you will be able to: Use parallel collections; Create async tasks; Use dataflow; Coordinate actors.

## Key Concepts

### 1. Use parallel collections

Target: Use parallel collections. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
@Grab(group="org.codehaus.gpars", module="gpars", version="1.2.1")
import groovyx.gpars.GParsPool

def result = GParsPool.withPool {
  (1..100).collectParallel { it * 2 }
}
```
### 2. Create async tasks

Target: Create async tasks. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
def future = GParsPool.withPool { async { 42 } }
println future.get()
```
### 3. Use dataflow

Target: Use dataflow. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
def ch = new groovyx.gpars.dataflow.DataflowQueue()
ch << 42
println ch.val
```
### 4. Coordinate actors

Target: Coordinate actors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
GParsPool.withPool(4) { (1..10).eachParallel { println it } }
```

## Practice Questions

1. What is the key idea behind "Concurrency with GPars"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Concurrency with GPars with analogies and real-world examples"
1. "Show me common mistakes beginners make with Concurrency with GPars"
1. "Provide advanced patterns and performance considerations for Concurrency with GPars"

## Key Takeaways

- Master the core ideas of Concurrency with GPars through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
