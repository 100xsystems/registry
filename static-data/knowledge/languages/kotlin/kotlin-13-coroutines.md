---
{
  "title": "Coroutines and Flow",
  "description": "suspend functions, coroutine scopes, and cold flows.",
  "type": "lesson",
  "order": 13,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Launch coroutines with launch and async",
    "Write suspend functions",
    "Manage concurrency with coroutine scopes",
    "Consume and build Flows"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-13-coroutines"
  ],
  "prerequisites": [
    "KOTLIN-12"
  ],
  "references": [
    {
      "title": "Kotlin — Coroutines Guide",
      "url": "https://kotlinlang.org/docs/coroutines-guide.html"
    },
    {
      "title": "Kotlin — coroutineScope",
      "url": "https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/coroutine-scope.html"
    },
    {
      "title": "Kotlin — Flow Guide",
      "url": "https://kotlinlang.org/docs/flow.html"
    }
  ]
}
---

# KOTLIN-13-COROUTINES: Coroutines and Flow

## Introduction

suspend functions, coroutine scopes, and cold flows. By the end of this lesson you will be able to: Launch coroutines with launch and async; Write suspend functions; Manage concurrency with coroutine scopes; Consume and build Flows.

## Key Concepts

### 1. Launch coroutines with launch and async

Target: Launch coroutines with launch and async. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// coroutine basics
import kotlinx.coroutines.*
fun main() = runBlocking {
    val job = launch {
        delay(100)
        println("world")
    }
    println("hello")
    job.join()
}
// hello then world
```
### 2. Write suspend functions

Target: Write suspend functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// async + await
import kotlinx.coroutines.*
fun main() = runBlocking {
    val a = async { fetch(3) }
    val b = async { fetch(4) }
    println("sum = ${a.await() + b.await()}")  // 25
}
suspend fun fetch(n: Int): Int {
    delay(10)
    return n * n
}
```
### 3. Manage concurrency with coroutine scopes

Target: Manage concurrency with coroutine scopes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// scopes and cancellation
import kotlinx.coroutines.*
fun main() = runBlocking {
    val scope = CoroutineScope(Dispatchers.Default)
    val job = scope.launch {
        repeat(100) {
            delay(50)
            println(it)
        }
    }
    delay(120)
    job.cancel()          // stops the coroutine
    println("cancelled")
}
```
### 4. Consume and build Flows

Target: Consume and build Flows. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// flow
import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*
fun main() = runBlocking {
    val squares = (1..5).asFlow()
        .map { it * it }
        .filter { it % 2 == 0 }
    squares.collect { println(it) }  // 4 16
}
```

## Practice Questions

1. What is the key idea behind "Coroutines and Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Coroutines and Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Coroutines and Flow"
1. "Provide advanced patterns and performance considerations for Coroutines and Flow"

## Key Takeaways

- Master the core ideas of Coroutines and Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
