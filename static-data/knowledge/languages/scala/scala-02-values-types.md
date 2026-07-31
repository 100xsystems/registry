---
{
  "title": "Values, Variables and the Type System",
  "description": "Understand vals, vars, primitive types, and how Scala infers and converts types.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Distinguish immutable val from mutable var and prefer immutability",
    "Use the core numeric, boolean and string types with their operations",
    "Read and write explicit type annotations and rely on inference",
    "Handle numeric conversions and type widening safely"
  ],
  "knowledge_refs": [
    "scala/scala-02-values-types"
  ],
  "prerequisites": [
    "SCALA-01"
  ],
  "references": [
    "https://docs.scala-lang.org/scala3/book/vars-vals-defs.html",
    "https://docs.scala-lang.org/scala3/book/taste-tools.html",
    "https://docs.scala-lang.org/scala3/book/types-introduction.html"
  ]
}
---

# SCALA-02-VALUES-TYPES: Values, Variables and the Type System

## Introduction

Understand vals, vars, primitive types, and how Scala infers and converts types. By the end of this lesson you will be able to: Distinguish immutable val from mutable var and prefer immutability; Use the core numeric, boolean and string types with their operations; Read and write explicit type annotations and rely on inference; Handle numeric conversions and type widening safely.

## Key Concepts

### 1. Distinguish immutable val from mutable var and prefer immutability

Target: Distinguish immutable val from mutable var and prefer immutability. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// val is immutable; var is mutable (avoid)
@main def values(): Unit =
  val fixed = 10
  var counter = 0
  counter += 1
  println(s"fixed=$fixed counter=$counter")
```
### 2. Use the core numeric, boolean and string types with their operations

Target: Use the core numeric, boolean and string types with their operations. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// numeric types and literals
val i: Int = 42
val l: Long = 42L
val f: Float = 3.14f
val d: Double = 3.14
val c: Char = 'A'
val b: Boolean = true
```
### 3. Read and write explicit type annotations and rely on inference

Target: Read and write explicit type annotations and rely on inference. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// type inference and widening
@main def widen(): Unit =
  val small: Int = 5
  val wide: Long = small      // Int widens to Long
  val d: Double = wide
  println(d)
```
### 4. Handle numeric conversions and type widening safely

Target: Handle numeric conversions and type widening safely. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// string interpolation and formatting
@main def strings(): Unit =
  val name = "Ada"
  val age = 36
  println(s"$name is $age years old")
  println(f"$name is $age%04d years old")
```

## Practice Questions

1. What is the key idea behind "Values, Variables and the Type System"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Values, Variables and the Type System with analogies and real-world examples"
1. "Show me common mistakes beginners make with Values, Variables and the Type System"
1. "Provide advanced patterns and performance considerations for Values, Variables and the Type System"

## Key Takeaways

- Master the core ideas of Values, Variables and the Type System through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
