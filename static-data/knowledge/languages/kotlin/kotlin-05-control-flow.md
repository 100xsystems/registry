---
{
  "title": "Control Flow",
  "description": "if expressions, when, and loops.",
  "type": "lesson",
  "order": 5,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use if as an expression",
    "Match with when (Kotlin's switch)",
    "Iterate with for and while",
    "Use break, continue, and labels"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-05-control-flow"
  ],
  "prerequisites": [
    "KOTLIN-02"
  ],
  "references": [
    {
      "title": "Kotlin — Control Flow",
      "url": "https://kotlinlang.org/docs/control-flow.html"
    },
    {
      "title": "Kotlin — When Expression",
      "url": "https://kotlinlang.org/docs/control-flow.html#when-expression"
    },
    {
      "title": "Kotlin — For Loops",
      "url": "https://kotlinlang.org/docs/control-flow.html#for-loops"
    }
  ]
}
---

# KOTLIN-05-CONTROL-FLOW: Control Flow

## Introduction

if expressions, when, and loops. By the end of this lesson you will be able to: Use if as an expression; Match with when (Kotlin's switch); Iterate with for and while; Use break, continue, and labels.

## Key Concepts

### 1. Use if as an expression

Target: Use if as an expression. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// if as expression
fun main() {
    val score = 85
    val grade = if (score >= 90) "A" else if (score >= 80) "B" else "C"
    println(grade)
    val pass = if (score >= 50) "pass" else "fail"
    println(pass)
}
```
### 2. Match with when (Kotlin's switch)

Target: Match with when (Kotlin's switch). Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// when expression
fun main() {
    val status = 404
    val message = when (status) {
        200, 204 -> "ok"
        404 -> "not found"
        500 -> "server error"
        in 400..499 -> "client error"
        else -> "unknown"
    }
    println(message)  // not found
}
```
### 3. Iterate with for and while

Target: Iterate with for and while. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// loops
fun main() {
    for (i in 0 until 5) print(i)   // 01234
    println()
    val items = listOf("a", "b", "c")
    for ((idx, v) in items.withIndex()) print("$idx:$v ")
    println()
    var n = 0
    while (n < 3) { n++ }
    println(n)
}
```
### 4. Use break, continue, and labels

Target: Use break, continue, and labels. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// break, continue, labels
fun main() {
    outer@ for (i in 1..5) {
        for (j in 1..5) {
            if (j == 2) continue
            if (i == 3) break@outer
            print("($i,$j) ")
        }
    }
    println()
}
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
