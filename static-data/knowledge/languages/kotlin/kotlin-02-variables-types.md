---
{
  "title": "Variables and Data Types",
  "description": "val, var, type inference, and the core types.",
  "type": "lesson",
  "order": 2,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare values with val and var",
    "Let the compiler infer types",
    "Work with Int, Long, Double, String, Boolean",
    "Use nullable types with ?"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-02-variables-types"
  ],
  "prerequisites": [
    "KOTLIN-01"
  ],
  "references": [
    {
      "title": "Kotlin — Basic Types",
      "url": "https://kotlinlang.org/docs/basic-types.html"
    },
    {
      "title": "Kotlin — Null Safety",
      "url": "https://kotlinlang.org/docs/null-safety.html"
    },
    {
      "title": "Kotlin — Type Checks and Casts",
      "url": "https://kotlinlang.org/docs/typecasts.html"
    }
  ]
}
---

# KOTLIN-02-VARIABLES-TYPES: Variables and Data Types

## Introduction

val, var, type inference, and the core types. By the end of this lesson you will be able to: Declare values with val and var; Let the compiler infer types; Work with Int, Long, Double, String, Boolean; Use nullable types with ?.

## Key Concepts

### 1. Declare values with val and var

Target: Declare values with val and var. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// val vs var
fun main() {
    val name = "Kotlin"   // immutable
    var score = 42        // mutable
    score += 1
    // name = "Java"      // error: val cannot be reassigned
    println("$name: $score")
}
```
### 2. Let the compiler infer types

Target: Let the compiler infer types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// type inference
fun main() {
    val count = 10            // Int
    val pi = 3.14             // Double
    val greeting = "hi"       // String
    val ok = true             // Boolean
    val big = 9_000_000_000L  // Long (L suffix)
    println("$count $pi $greeting $ok $big")
}
```
### 3. Work with Int, Long, Double, String, Boolean

Target: Work with Int, Long, Double, String, Boolean. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// explicit types and conversion
fun main() {
    val a: Int = 5
    val b: Double = 2.5
    val sum = a + b.toInt()   // 7
    val text = sum.toString() // "7"
    val asLong = a.toLong()
    println("$sum $text $asLong")
}
```
### 4. Use nullable types with ?

Target: Use nullable types with ?. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// nullable types
fun main() {
    var maybe: String? = "hello"
    maybe = null             // allowed on nullable
    val len = maybe?.length  // safe call -> null
    println(len ?: 0)        // 0 via Elvis
}
```

## Practice Questions

1. What is the key idea behind "Variables and Data Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Data Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Data Types"
1. "Provide advanced patterns and performance considerations for Variables and Data Types"

## Key Takeaways

- Master the core ideas of Variables and Data Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
