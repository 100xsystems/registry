---
{
  "title": "Generics",
  "description": "Generic types, variance, and reified types.",
  "type": "lesson",
  "order": 12,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write generic functions and classes",
    "Use type parameters with bounds",
    "Understand in and out variance",
    "Use reified type parameters"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-12-generics"
  ],
  "prerequisites": [
    "KOTLIN-09"
  ],
  "references": [
    {
      "title": "Kotlin — Generics",
      "url": "https://kotlinlang.org/docs/generics.html"
    },
    {
      "title": "Kotlin — Variance",
      "url": "https://kotlinlang.org/docs/generics.html#variance"
    },
    {
      "title": "Kotlin — Reified Types",
      "url": "https://kotlinlang.org/docs/inline-functions.html#reified-type-parameters"
    }
  ]
}
---

# KOTLIN-12-GENERICS: Generics

## Introduction

Generic types, variance, and reified types. By the end of this lesson you will be able to: Write generic functions and classes; Use type parameters with bounds; Understand in and out variance; Use reified type parameters.

## Key Concepts

### 1. Write generic functions and classes

Target: Write generic functions and classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// generic functions
fun <T> identity(value: T): T = value
fun main() {
    println(identity(42))
    println(identity("text"))
}
```
### 2. Use type parameters with bounds

Target: Use type parameters with bounds. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// generic classes
class Stack<T> {
    private val items = mutableListOf<T>()
    fun push(item: T) { items.add(item) }
    fun pop(): T? = items.removeLastOrNull()
    val size get() = items.size
}
fun main() {
    val s = Stack<Int>()
    s.push(1); s.push(2)
    println(s.pop())  // 2
}
```
### 3. Understand in and out variance

Target: Understand in and out variance. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// bounds
fun <T : Comparable<T>> maxOf2(a: T, b: T): T = if (a > b) a else b
fun main() {
    println(maxOf2(3, 7))
    println(maxOf2("cat", "dog"))
}
```
### 4. Use reified type parameters

Target: Use reified type parameters. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// reified + inline
inline fun <reified T> typeName(): String = T::class.simpleName ?: "?"
fun main() {
    println(typeName<String>())  // String
    println(typeName<Int>())      // Int
}
```

## Practice Questions

1. What is the key idea behind "Generics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Generics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Generics"
1. "Provide advanced patterns and performance considerations for Generics"

## Key Takeaways

- Master the core ideas of Generics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
