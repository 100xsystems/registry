---
{
  "title": "Exceptions and Error Handling",
  "description": "Throwables, try-catch, and custom exceptions.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Throw and catch exceptions",
    "Use try as an expression",
    "Define custom exception types",
    "Run cleanup with finally"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-11-exceptions"
  ],
  "prerequisites": [
    "KOTLIN-10"
  ],
  "references": [
    {
      "title": "Kotlin — Exceptions",
      "url": "https://kotlinlang.org/docs/exceptions.html"
    },
    {
      "title": "Kotlin — try/catch",
      "url": "https://kotlinlang.org/docs/exceptions.html#try-catch-expressions"
    },
    {
      "title": "Kotlin — runCatching",
      "url": "https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/run-catching.html"
    }
  ]
}
---

# KOTLIN-11-EXCEPTIONS: Exceptions and Error Handling

## Introduction

Throwables, try-catch, and custom exceptions. By the end of this lesson you will be able to: Throw and catch exceptions; Use try as an expression; Define custom exception types; Run cleanup with finally.

## Key Concepts

### 1. Throw and catch exceptions

Target: Throw and catch exceptions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// try-catch
fun main() {
    try {
        val n = "abc".toInt()
        println(n)
    } catch (e: NumberFormatException) {
        println("bad number: ${e.message}")
    }
}
```
### 2. Use try as an expression

Target: Use try as an expression. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// try as expression
fun parse(raw: String): Int = try {
    raw.toInt()
} catch (e: NumberFormatException) {
    0
}
fun main() {
    println(parse("42"))  // 42
    println(parse("x"))   // 0
}
```
### 3. Define custom exception types

Target: Define custom exception types. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// custom exceptions + finally
class PaymentFailed(message: String) : Exception(message)
fun charge(amount: Double) {
    if (amount > 100.0) throw PaymentFailed("limit exceeded")
}
fun main() {
    try {
        charge(500.0)
    } catch (e: PaymentFailed) {
        println("payment: ${e.message}")
    } finally {
        println("cleanup done")
    }
}
```
### 4. Run cleanup with finally

Target: Run cleanup with finally. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// runCatching
fun main() {
    val result = runCatching { "7x".toInt() }
    result.onSuccess { println("parsed $it") }
    result.onFailure { println("failed: ${it.message}") }
    val n = result.getOrDefault(0)
    println(n)
}
```

## Practice Questions

1. What is the key idea behind "Exceptions and Error Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Exceptions and Error Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Exceptions and Error Handling"
1. "Provide advanced patterns and performance considerations for Exceptions and Error Handling"

## Key Takeaways

- Master the core ideas of Exceptions and Error Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
