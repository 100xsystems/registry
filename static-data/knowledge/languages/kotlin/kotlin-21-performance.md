---
{
  "title": "Performance and Best Practices",
  "description": "Inline functions, allocations, and idiomatic performance.",
  "type": "lesson",
  "order": 21,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use inline functions to avoid overhead",
    "Minimize allocations in hot paths",
    "Apply idiomatic best practices",
    "Profile and benchmark Kotlin code"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-21-performance"
  ],
  "prerequisites": [
    "KOTLIN-20"
  ],
  "references": [
    {
      "title": "Kotlin — Inline Functions",
      "url": "https://kotlinlang.org/docs/inline-functions.html"
    },
    {
      "title": "Kotlin — Performance Best Practices",
      "url": "https://kotlinlang.org/docs/best-practices.html"
    },
    {
      "title": "Kotlin — JavaScript/Wasip Performance",
      "url": "https://kotlinlang.org/docs/js-performance.html"
    }
  ]
}
---

# KOTLIN-21-PERFORMANCE: Performance and Best Practices

## Introduction

Inline functions, allocations, and idiomatic performance. By the end of this lesson you will be able to: Use inline functions to avoid overhead; Minimize allocations in hot paths; Apply idiomatic best practices; Profile and benchmark Kotlin code.

## Key Concepts

### 1. Use inline functions to avoid overhead

Target: Use inline functions to avoid overhead. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// inline functions avoid lambda allocation
inline fun measure(block: () -> Unit) {
    val start = System.nanoTime()
    block()
    println("took ${(System.nanoTime() - start) / 1e6} ms")
}
fun main() {
    measure { println("work") }
}
```
### 2. Minimize allocations in hot paths

Target: Minimize allocations in hot paths. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// avoid allocations in hot paths
fun main() {
    // prefer primitive loops over heavy mapping in tight loops
    var sum = 0L
    for (i in 1..1_000_000) sum += i
    println(sum)
    // useIntArray etc. to avoid boxing
    val arr = IntArray(100) { it }
    println(arr.sum())
}
```
### 3. Apply idiomatic best practices

Target: Apply idiomatic best practices. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// idiomatic best practices
fun main() {
    // prefer val over var
    val config = mapOf("debug" to false)
    // prefer data classes for DTOs
    data class Config(val debug: Boolean)
    // use scope functions sparingly
    val msg = config["debug"]?.let { "debug on" } ?: "debug off"
    println(msg)
}
```
### 4. Profile and benchmark Kotlin code

Target: Profile and benchmark Kotlin code. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// benchmarking
fun main() {
    val n = 1_000_000
    val start = System.nanoTime()
    val sum = (1..n).sumOf { it.toLong() }
    val elapsedMs = (System.nanoTime() - start) / 1e6
    println("sum=$sum in ${elapsedMs} ms")
}
```

## Practice Questions

1. What is the key idea behind "Performance and Best Practices"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance and Best Practices with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance and Best Practices"
1. "Provide advanced patterns and performance considerations for Performance and Best Practices"

## Key Takeaways

- Master the core ideas of Performance and Best Practices through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
