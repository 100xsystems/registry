---
{
  "title": "Functions",
  "description": "Function declarations, default args, and lambdas.",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare functions with named and default arguments",
    "Use single-expression functions",
    "Write lambdas and higher-order functions",
    "Use extension functions"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-07-functions"
  ],
  "prerequisites": [
    "KOTLIN-05"
  ],
  "references": [
    {
      "title": "Kotlin — Functions",
      "url": "https://kotlinlang.org/docs/functions.html"
    },
    {
      "title": "Kotlin — Lambdas",
      "url": "https://kotlinlang.org/docs/lambdas.html"
    },
    {
      "title": "Kotlin — Extension Functions",
      "url": "https://kotlinlang.org/docs/extensions.html"
    }
  ]
}
---

# KOTLIN-07-FUNCTIONS: Functions

## Introduction

Function declarations, default args, and lambdas. By the end of this lesson you will be able to: Declare functions with named and default arguments; Use single-expression functions; Write lambdas and higher-order functions; Use extension functions.

## Key Concepts

### 1. Declare functions with named and default arguments

Target: Declare functions with named and default arguments. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// default + named arguments
fun greet(name: String, times: Int = 1): String =
    "Hi $name! ".repeat(times)
fun main() {
    println(greet("Alice"))
    println(greet("Bob", times = 2))
}
```
### 2. Use single-expression functions

Target: Use single-expression functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// single-expression + local functions
fun square(n: Int) = n * n
fun main() {
    fun local(x: Int) = x + 1
    println(square(9))     // 81
    println(local(41))     // 42
}
```
### 3. Write lambdas and higher-order functions

Target: Write lambdas and higher-order functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// lambdas and higher-order
fun main() {
    val add: (Int, Int) -> Int = { a, b -> a + b }
    val triple: (Int) -> Int = { it * 3 }
    println(add(2, 3))        // 5
    println(triple(14))       // 42
    val names = listOf("Zoe", "Amy")
    println(names.map { it.uppercase() })
}
```
### 4. Use extension functions

Target: Use extension functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// extension functions
fun String.shout(): String = "$this!!".uppercase()
fun main() {
    println("hello".shout())       // HELLO!!
    println(listOf(1, 2, 3).sum()) // 6
    fun Int.isEven() = this % 2 == 0
    println(4.isEven())            // true
}
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
