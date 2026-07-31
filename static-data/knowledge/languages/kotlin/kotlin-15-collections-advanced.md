---
{
  "title": "Advanced Collections",
  "description": "Sequences, grouping, and lazy evaluation.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use sequences for lazy pipelines",
    "Group and associate elements",
    "Zip and pair collections",
    "Use windows and chunked operations"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-15-collections-advanced"
  ],
  "prerequisites": [
    "KOTLIN-06"
  ],
  "references": [
    {
      "title": "Kotlin — Sequences",
      "url": "https://kotlinlang.org/docs/sequences.html"
    },
    {
      "title": "Kotlin — Grouping",
      "url": "https://kotlinlang.org/docs/collection-grouping.html"
    },
    {
      "title": "Kotlin — Collection Operations",
      "url": "https://kotlinlang.org/docs/collection-operations.html"
    }
  ]
}
---

# KOTLIN-15-COLLECTIONS-ADVANCED: Advanced Collections

## Introduction

Sequences, grouping, and lazy evaluation. By the end of this lesson you will be able to: Use sequences for lazy pipelines; Group and associate elements; Zip and pair collections; Use windows and chunked operations.

## Key Concepts

### 1. Use sequences for lazy pipelines

Target: Use sequences for lazy pipelines. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// sequences — lazy
fun main() {
    val result = (1..1_000_000).asSequence()
        .filter { it % 2 == 0 }
        .map { it * it }
        .take(3)
        .toList()
    println(result)  // [4, 16, 36] — lazy evaluation
}
```
### 2. Group and associate elements

Target: Group and associate elements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// grouping and associating
fun main() {
    val words = listOf("apple", "apricot", "banana", "berry")
    val byFirst = words.groupBy { it.first() }
    println(byFirst.keys)  // [a, b]
    val lenMap = words.associateWith { it.length }
    println(lenMap)
}
```
### 3. Zip and pair collections

Target: Zip and pair collections. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// zip and pairs
fun main() {
    val names = listOf("Alice", "Bob")
    val ages = listOf(30, 25)
    val paired = names.zip(ages)
    println(paired)                      // [(Alice, 30), (Bob, 25)]
    val map = names.zip(ages).toMap()
    println(map)
}
```
### 4. Use windows and chunked operations

Target: Use windows and chunked operations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// windows and chunked
fun main() {
    val nums = (1..7).toList()
    println(nums.chunked(3))   // [[1, 2, 3], [4, 5, 6], [7]]
    println(nums.windowed(3, step = 2))  // [[1,2,3],[3,4,5],[5,6,7]]
    println(nums.windowed(2))  // adjacent pairs
}
```

## Practice Questions

1. What is the key idea behind "Advanced Collections"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced Collections with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced Collections"
1. "Provide advanced patterns and performance considerations for Advanced Collections"

## Key Takeaways

- Master the core ideas of Advanced Collections through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
