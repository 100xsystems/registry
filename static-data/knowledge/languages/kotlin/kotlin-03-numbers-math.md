---
{
  "title": "Numbers and Math",
  "description": "Integer types, floating point, overflow, and math APIs.",
  "type": "lesson",
  "order": 3,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use Int, Long, Float, and Double",
    "Understand overflow and ranges",
    "Use the kotlin.math API",
    "Format numbers for output"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-03-numbers-math"
  ],
  "prerequisites": [
    "KOTLIN-02"
  ],
  "references": [
    {
      "title": "Kotlin — Numbers",
      "url": "https://kotlinlang.org/docs/numbers.html"
    },
    {
      "title": "Kotlin — Math Functions",
      "url": "https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.math/"
    },
    {
      "title": "Kotlin — Ranges and Progressions",
      "url": "https://kotlinlang.org/docs/ranges.html"
    }
  ]
}
---

# KOTLIN-03-NUMBERS-MATH: Numbers and Math

## Introduction

Integer types, floating point, overflow, and math APIs. By the end of this lesson you will be able to: Use Int, Long, Float, and Double; Understand overflow and ranges; Use the kotlin.math API; Format numbers for output.

## Key Concepts

### 1. Use Int, Long, Float, and Double

Target: Use Int, Long, Float, and Double. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// integer types
fun main() {
    val byte: Byte = 127
    val short: Short = 32767
    val int = 2_147_483_647
    val long = 9_223_372_036_854_775_807L
    println("$byte $short $int $long")
}
```
### 2. Understand overflow and ranges

Target: Understand overflow and ranges. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// floating point + overflow
fun main() {
    val d = 0.1 + 0.2            // Double
    println(d)                   // 0.30000000000000004
    val f = 0.1f + 0.2f          // Float
    println(f)
    val max = Int.MAX_VALUE
    // val boom = max + 1        // overflow wraps silently in Kotlin!
    println("$max overflow wraps to ${max + 1}")
}
```
### 3. Use the kotlin.math API

Target: Use the kotlin.math API. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// kotlin.math
import kotlin.math.*
fun main() {
    println(sqrt(16.0))         // 4.0
    println(pow(2.0, 10.0))     // 1024.0
    println(round(3.5))         // 4.0
    println(abs(-7))            // 7
}
```
### 4. Format numbers for output

Target: Format numbers for output. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// ranges
fun main() {
    val dice = (1..6).random()
    println("d6 = $dice")
    for (i in 1..5) print(i)   // 12345
    println()
    for (i in 10 downTo 1 step 3) print("$i ") // 10 7 4 1
    println()
    println(3 in 1..5)         // true
}
```

## Practice Questions

1. What is the key idea behind "Numbers and Math"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Numbers and Math with analogies and real-world examples"
1. "Show me common mistakes beginners make with Numbers and Math"
1. "Provide advanced patterns and performance considerations for Numbers and Math"

## Key Takeaways

- Master the core ideas of Numbers and Math through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
