---
{
  "title": "Classes and Objects",
  "description": "Classes, constructors, properties, and data classes.",
  "type": "lesson",
  "order": 8,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define classes with primary and secondary constructors",
    "Use properties and backing fields",
    "Write data classes for value holders",
    "Use object declarations and companion objects"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-08-classes"
  ],
  "prerequisites": [
    "KOTLIN-07"
  ],
  "references": [
    {
      "title": "Kotlin — Classes",
      "url": "https://kotlinlang.org/docs/classes.html"
    },
    {
      "title": "Kotlin — Properties",
      "url": "https://kotlinlang.org/docs/properties.html"
    },
    {
      "title": "Kotlin — Data Classes",
      "url": "https://kotlinlang.org/docs/data-classes.html"
    }
  ]
}
---

# KOTLIN-08-CLASSES: Classes and Objects

## Introduction

Classes, constructors, properties, and data classes. By the end of this lesson you will be able to: Define classes with primary and secondary constructors; Use properties and backing fields; Write data classes for value holders; Use object declarations and companion objects.

## Key Concepts

### 1. Define classes with primary and secondary constructors

Target: Define classes with primary and secondary constructors. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// class with constructor + properties
class Product(
    val name: String,
    val price: Double,
    var stock: Int = 0,
) {
    fun summary(): String = "$name — $$price (stock: $stock)"
}
fun main() {
    val p = Product("Keyboard", 49.99, 12)
    println(p.summary())
}
```
### 2. Use properties and backing fields

Target: Use properties and backing fields. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// init blocks and secondary constructors
class Counter {
    var count: Int
    init { count = 0 }          // runs on construction
    constructor(start: Int) { count = start }
    fun increment() { count++ }
}
fun main() {
    val c = Counter(10)
    c.increment()
    println(c.count)  // 11
}
```
### 3. Write data classes for value holders

Target: Write data classes for value holders. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// data classes
data class User(val name: String, val age: Int)
fun main() {
    val a = User("Alice", 30)
    val b = a.copy(age = 31)     // immutable copy
    println(a)                   // User(name=Alice, age=30)
    println(a == User("Alice", 30))  // true — structural
    println(b)
}
```
### 4. Use object declarations and companion objects

Target: Use object declarations and companion objects. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// object + companion
object Config {
    val version = "1.0"
}
class Service {
    companion object {
        const val NAME = "svc"
    }
}
fun main() {
    println(Config.version)
    println(Service.NAME)
}
```

## Practice Questions

1. What is the key idea behind "Classes and Objects"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Classes and Objects with analogies and real-world examples"
1. "Show me common mistakes beginners make with Classes and Objects"
1. "Provide advanced patterns and performance considerations for Classes and Objects"

## Key Takeaways

- Master the core ideas of Classes and Objects through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
