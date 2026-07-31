---
{
  "title": "Functional Kotlin",
  "description": "Higher-order functions, immutability, and DSLs.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Compose functions and use let/run/with/apply",
    "Build small DSLs with lambdas with receivers",
    "Prefer immutability with val and copy",
    "Use standard functional helpers"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-16-functional"
  ],
  "prerequisites": [
    "KOTLIN-07"
  ],
  "references": [
    {
      "title": "Kotlin — Scope Functions",
      "url": "https://kotlinlang.org/docs/scope-functions.html"
    },
    {
      "title": "Kotlin — Lambdas with Receivers",
      "url": "https://kotlinlang.org/docs/lambdas.html#function-literals-with-receiver"
    },
    {
      "title": "Kotlin — Idioms",
      "url": "https://kotlinlang.org/docs/idioms.html"
    }
  ]
}
---

# KOTLIN-16-FUNCTIONAL: Functional Kotlin

## Introduction

Higher-order functions, immutability, and DSLs. By the end of this lesson you will be able to: Compose functions and use let/run/with/apply; Build small DSLs with lambdas with receivers; Prefer immutability with val and copy; Use standard functional helpers.

## Key Concepts

### 1. Compose functions and use let/run/with/apply

Target: Compose functions and use let/run/with/apply. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// let, run, with, apply, also
fun main() {
    val name = "Alice"
    name?.let { println("let: $it") }
    val len = run { name.length }
    val text = with(name) { "with: $this" }
    val applied = StringBuilder().apply {
        append("a"); append("b")
    }.toString()
    val also = mutableListOf(1).also { it.add(2) }
    println("$len $text $applied $also")
}
```
### 2. Build small DSLs with lambdas with receivers

Target: Build small DSLs with lambdas with receivers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// immutability
fun main() {
    data class Point(val x: Int, val y: Int)
    val p = Point(1, 2)
    val q = p.copy(y = 5)   // never mutate, always copy
    println(q)
    val arr = listOf(1, 2, 3)  // read-only view
    println(arr)
}
```
### 3. Prefer immutability with val and copy

Target: Prefer immutability with val and copy. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// function composition
fun main() {
    fun String.prep(): String = trim().lowercase()
    fun List<String>.unique(): List<String> = distinct().sorted()
    val cleaned = listOf("  B ", "a", "A ")
        .map { it.prep() }
        .unique()
    println(cleaned)  // [a, b]
}
```
### 4. Use standard functional helpers

Target: Use standard functional helpers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// lambdas with receivers (mini-DSL)
fun buildString(builder: StringBuilder.() -> Unit): String {
    val sb = StringBuilder()
    sb.builder()
    return sb.toString()
}
fun main() {
    val s = buildString {
        append("Hello ")
        append("DSL!")
    }
    println(s)
}
```

## Practice Questions

1. What is the key idea behind "Functional Kotlin"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functional Kotlin with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functional Kotlin"
1. "Provide advanced patterns and performance considerations for Functional Kotlin"

## Key Takeaways

- Master the core ideas of Functional Kotlin through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
