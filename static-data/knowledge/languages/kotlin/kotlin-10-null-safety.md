---
{
  "title": "Null Safety",
  "description": "Nullable types, safe calls, and the Elvis operator.",
  "type": "lesson",
  "order": 10,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare nullable types with ?",
    "Use safe calls and the Elvis operator",
    "Force-unwrap deliberately",
    "Use let, also, and other scope functions"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-10-null-safety"
  ],
  "prerequisites": [
    "KOTLIN-02"
  ],
  "references": [
    {
      "title": "Kotlin — Null Safety",
      "url": "https://kotlinlang.org/docs/null-safety.html"
    },
    {
      "title": "Kotlin — Scope Functions",
      "url": "https://kotlinlang.org/docs/scope-functions.html"
    },
    {
      "title": "Kotlin — Idioms (Elvis)",
      "url": "https://kotlinlang.org/docs/idioms.html#elvis-operator"
    }
  ]
}
---

# KOTLIN-10-NULL-SAFETY: Null Safety

## Introduction

Nullable types, safe calls, and the Elvis operator. By the end of this lesson you will be able to: Declare nullable types with ?; Use safe calls and the Elvis operator; Force-unwrap deliberately; Use let, also, and other scope functions.

## Key Concepts

### 1. Declare nullable types with ?

Target: Declare nullable types with ?. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// nullable basics
fun main() {
    var maybe: String? = "hello"
    println(maybe)            // hello
    maybe = null
    println(maybe?.length)    // null
    println(maybe ?: 0)       // 0
}
```
### 2. Use safe calls and the Elvis operator

Target: Use safe calls and the Elvis operator. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// safe call chains
class Address(val city: String)
class Person(val address: Address?)
fun main() {
    val p = Person(Address("Paris"))
    println(p.address?.city)       // Paris
    val none = Person(null)
    println(none.address?.city ?: "unknown")  // unknown
}
```
### 3. Force-unwrap deliberately

Target: Force-unwrap deliberately. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// let + safe call
fun main() {
    val name: String? = "Alice"
    name?.let {
        println("hello $it")     // runs only if non-null
    }
    val result = name?.uppercase() ?: "N/A"
    println(result)
}
```
### 4. Use let, also, and other scope functions

Target: Use let, also, and other scope functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// !! and smart casts
fun main() {
    var raw: String? = "42"
    val n = raw!!.toInt()       // deliberate unwrap
    println(n)
    raw = null
    if (raw != null) {
        // smart cast: raw is String here
        println(raw.length)
    } else {
        println("null")
    }
}
```

## Practice Questions

1. What is the key idea behind "Null Safety"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Null Safety with analogies and real-world examples"
1. "Show me common mistakes beginners make with Null Safety"
1. "Provide advanced patterns and performance considerations for Null Safety"

## Key Takeaways

- Master the core ideas of Null Safety through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
