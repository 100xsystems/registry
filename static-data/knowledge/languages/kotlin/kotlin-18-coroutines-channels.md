---
{
  "title": "Channels and Structured Concurrency",
  "description": "Channels, select, and structured concurrency patterns.",
  "type": "lesson",
  "order": 18,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Build pipelines with Channels",
    "Select across multiple suspending sources",
    "Cancel and handle timeouts",
    "Understand structured concurrency rules"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-18-coroutines-channels"
  ],
  "prerequisites": [
    "KOTLIN-13"
  ],
  "references": [
    {
      "title": "Kotlin — Channels Guide",
      "url": "https://kotlinlang.org/docs/channels.html"
    },
    {
      "title": "Kotlin — select Expression",
      "url": "https://kotlinlang.org/docs/select-expression.html"
    },
    {
      "title": "Kotlin — Composing Suspending Functions",
      "url": "https://kotlinlang.org/docs/composing-suspending-functions.html"
    }
  ]
}
---

# KOTLIN-18-COROUTINES-CHANNELS: Channels and Structured Concurrency

## Introduction

Channels, select, and structured concurrency patterns. By the end of this lesson you will be able to: Build pipelines with Channels; Select across multiple suspending sources; Cancel and handle timeouts; Understand structured concurrency rules.

## Key Concepts

### 1. Build pipelines with Channels

Target: Build pipelines with Channels. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// channels
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*
fun main() = runBlocking {
    val ch = Channel<Int>(capacity = 3)
    launch { for (x in 1..5) ch.send(x) }
    repeat(5) { println(ch.receive()) }  // 1..5
}
```
### 2. Select across multiple suspending sources

Target: Select across multiple suspending sources. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// producer-consumer pipeline
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*
fun main() = runBlocking {
    val ch = Channel<String>()
    launch { ch.send("job-1"); ch.send("job-2"); ch.close() }
    for (job in ch) {
        println("processing $job")
    }
}
```
### 3. Cancel and handle timeouts

Target: Cancel and handle timeouts. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// select
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*
import kotlinx.coroutines.selects.*
fun main() = runBlocking {
    val a = Channel<Int>(1)
    val b = Channel<Int>(1)
    launch { delay(50); a.send(1) }
    launch { delay(10); b.send(2) }
    val winner = select<Int> {
        a.onReceive { it }
        b.onReceive { it }
    }
    println("first: $winner")  // 2 (b is faster)
}
```
### 4. Understand structured concurrency rules

Target: Understand structured concurrency rules. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// timeout and structured concurrency
import kotlinx.coroutines.*
fun main() = runBlocking {
    val result = withTimeoutOrNull(100) {
        delay(50)
        "done in time"
    }
    println(result)  // done in time
    // coroutineScope waits for children before returning
    coroutineScope {
        launch { delay(10); println("child done") }
    }
}
```

## Practice Questions

1. What is the key idea behind "Channels and Structured Concurrency"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Channels and Structured Concurrency with analogies and real-world examples"
1. "Show me common mistakes beginners make with Channels and Structured Concurrency"
1. "Provide advanced patterns and performance considerations for Channels and Structured Concurrency"

## Key Takeaways

- Master the core ideas of Channels and Structured Concurrency through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
