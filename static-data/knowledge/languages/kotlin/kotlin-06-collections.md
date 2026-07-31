---
{
  "title": "Collections",
  "description": "Lists, sets, maps, and collection operators.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Build lists, sets, and maps",
    "Distinguish mutable and read-only views",
    "Transform with map, filter, and reduce",
    "Use sorting and searching helpers"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-06-collections"
  ],
  "prerequisites": [
    "KOTLIN-05"
  ],
  "references": [
    {
      "title": "Kotlin — Collections Overview",
      "url": "https://kotlinlang.org/docs/collections-overview.html"
    },
    {
      "title": "Kotlin — List",
      "url": "https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/list/"
    },
    {
      "title": "Kotlin — Collection Operations",
      "url": "https://kotlinlang.org/docs/collection-operations.html"
    }
  ]
}
---

# KOTLIN-06-COLLECTIONS: Collections

## Introduction

Lists, sets, maps, and collection operators. By the end of this lesson you will be able to: Build lists, sets, and maps; Distinguish mutable and read-only views; Transform with map, filter, and reduce; Use sorting and searching helpers.

## Key Concepts

### 1. Build lists, sets, and maps

Target: Build lists, sets, and maps. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// lists
fun main() {
    val fruits = mutableListOf("apple", "banana")
    fruits.add("cherry")
    fruits.removeAt(0)
    println(fruits)          // [banana, cherry]
    val readOnly: List<String> = fruits  // view
    println(readOnly[0])
}
```
### 2. Distinguish mutable and read-only views

Target: Distinguish mutable and read-only views. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// sets and maps
fun main() {
    val tags = mutableSetOf("kotlin", "jvm")
    tags.add("android")
    println("kotlin" in tags)      // true
    val user = mutableMapOf("name" to "Alice", "age" to 30)
    user["admin"] = true
    user.remove("age")
    println(user)
}
```
### 3. Transform with map, filter, and reduce

Target: Transform with map, filter, and reduce. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// transform
fun main() {
    val nums = listOf(1, 2, 3, 4, 5)
    val doubled = nums.map { it * 2 }
    val evens = nums.filter { it % 2 == 0 }
    val sum = nums.sum()
    val product = nums.reduce { acc, n -> acc * n }
    println("$doubled $evens $sum $product")
}
```
### 4. Use sorting and searching helpers

Target: Use sorting and searching helpers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// sort and search
fun main() {
    val people = listOf("Zoe" to 30, "Amy" to 25, "Bo" to 40)
    val sorted = people.sortedBy { it.second }
    println(sorted.map { it.first })  // [Amy, Zoe, Bo]
    println(people.maxByOrNull { it.second })  // (Bo, 40)
    println(listOf(1, 2, 3).contains(2))      // true
}
```

## Practice Questions

1. What is the key idea behind "Collections"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Collections with analogies and real-world examples"
1. "Show me common mistakes beginners make with Collections"
1. "Provide advanced patterns and performance considerations for Collections"

## Key Takeaways

- Master the core ideas of Collections through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
