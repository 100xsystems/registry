---
{
  "title": "Collections: List, Vector, Map and Set",
  "description": "Choose the right immutable collection and use its API effectively.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Build and inspect Lists, Vectors and their performance profiles",
    "Work with immutable Maps and Sets for lookup and membership",
    "Slice, group and sort collections with the standard API",
    "Convert between collection types and aggregate with groupingBy"
  ],
  "knowledge_refs": [
    "scala/scala-06-collections"
  ],
  "prerequisites": [
    "SCALA-05"
  ],
  "references": [
    "https://docs.scala-lang.org/overviews/collections-2.13/introduction.html",
    "https://docs.scala-lang.org/overviews/collections-2.13/performance-characteristics.html",
    "https://docs.scala-lang.org/scala3/book/collections-classes.html"
  ]
}
---

# SCALA-06-COLLECTIONS: Collections: List, Vector, Map and Set

## Introduction

Choose the right immutable collection and use its API effectively. By the end of this lesson you will be able to: Build and inspect Lists, Vectors and their performance profiles; Work with immutable Maps and Sets for lookup and membership; Slice, group and sort collections with the standard API; Convert between collection types and aggregate with groupingBy.

## Key Concepts

### 1. Build and inspect Lists, Vectors and their performance profiles

Target: Build and inspect Lists, Vectors and their performance profiles. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// List vs Vector performance
@main def collections(): Unit =
  val list = List(1, 2, 3)          // fast prepend
  val vector = Vector(1, 2, 3)      // fast append + index
  println(list.head + 1)            // 2
  println(vector(2))                // 3
```
### 2. Work with immutable Maps and Sets for lookup and membership

Target: Work with immutable Maps and Sets for lookup and membership. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// immutable Map and Set
@main def maps(): Unit =
  val ages = Map("Ada" -> 36, "Alan" -> 41)
  val updated = ages.updated("Grace", 45)
  val tags = Set("scala", "fp", "types")
  println(updated.get("Grace"))
  println(tags.contains("fp"))
```
### 3. Slice, group and sort collections with the standard API

Target: Slice, group and sort collections with the standard API. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// slice, group and sort
@main def organize(): Unit =
  val nums = List(3, 1, 4, 1, 5, 9, 2, 6)
  println(nums.take(3))
  println(nums.sorted.take(4))
  println(nums.grouped(2).toList)
```
### 4. Convert between collection types and aggregate with groupingBy

Target: Convert between collection types and aggregate with groupingBy. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// groupBy for aggregation
@main def group(): Unit =
  val words = List("scala", "is", "a", "great", "language")
  val byLength = words.groupBy(_.length)
  println(byLength)
  println(byLength(4))  // List("great")
```

## Practice Questions

1. What is the key idea behind "Collections: List, Vector, Map and Set"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Collections: List, Vector, Map and Set with analogies and real-world examples"
1. "Show me common mistakes beginners make with Collections: List, Vector, Map and Set"
1. "Provide advanced patterns and performance considerations for Collections: List, Vector, Map and Set"

## Key Takeaways

- Master the core ideas of Collections: List, Vector, Map and Set through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
