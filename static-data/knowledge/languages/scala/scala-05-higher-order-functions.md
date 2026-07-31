---
{
  "title": "Higher-Order Functions and Lambdas",
  "description": "Transform collections with map, filter, fold and other higher-order functions.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write anonymous functions (lambdas) with the => syntax",
    "Apply map and filter to transform and select elements",
    "Fold collections with foldLeft and reduce to combine values",
    "Compose functions with andThen and compose"
  ],
  "knowledge_refs": [
    "scala/scala-05-higher-order-functions"
  ],
  "prerequisites": [
    "SCALA-04"
  ],
  "references": [
    "https://docs.scala-lang.org/scala3/book/fun.html",
    "https://docs.scala-lang.org/tour/higher-order-functions.html",
    "https://docs.scala-lang.org/overviews/collections-2.13/seq.html"
  ]
}
---

# SCALA-05-HIGHER-ORDER-FUNCTIONS: Higher-Order Functions and Lambdas

## Introduction

Transform collections with map, filter, fold and other higher-order functions. By the end of this lesson you will be able to: Write anonymous functions (lambdas) with the => syntax; Apply map and filter to transform and select elements; Fold collections with foldLeft and reduce to combine values; Compose functions with andThen and compose.

## Key Concepts

### 1. Write anonymous functions (lambdas) with the => syntax

Target: Write anonymous functions (lambdas) with the => syntax. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// lambda syntax
@main def lambdas(): Unit =
  val square = (x: Int) => x * x
  val numbers = List(1, 2, 3, 4)
  println(numbers.map(square))
```
### 2. Apply map and filter to transform and select elements

Target: Apply map and filter to transform and select elements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// map and filter
@main def transform(): Unit =
  val nums = List(1, 2, 3, 4, 5, 6)
  val evens = nums.filter(_ % 2 == 0)
  val doubled = evens.map(_ * 2)
  println(doubled)  // List(4, 8, 12)
```
### 3. Fold collections with foldLeft and reduce to combine values

Target: Fold collections with foldLeft and reduce to combine values. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// foldLeft to accumulate
@main def fold(): Unit =
  val nums = List(1, 2, 3, 4)
  val sum = nums.foldLeft(0)((acc, n) => acc + n)
  val product = nums.reduce(_ * _)
  println(s"sum=$sum product=$product")
```
### 4. Compose functions with andThen and compose

Target: Compose functions with andThen and compose. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// compose functions
@main def compose(): Unit =
  val double = (x: Int) => x * 2
  val inc = (x: Int) => x + 1
  val dThenI = double.andThen(inc)
  val iThenD = double.compose(inc)
  println(dThenI(3))  // 7
  println(iThenD(3))  // 8
```

## Practice Questions

1. What is the key idea behind "Higher-Order Functions and Lambdas"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Higher-Order Functions and Lambdas with analogies and real-world examples"
1. "Show me common mistakes beginners make with Higher-Order Functions and Lambdas"
1. "Provide advanced patterns and performance considerations for Higher-Order Functions and Lambdas"

## Key Takeaways

- Master the core ideas of Higher-Order Functions and Lambdas through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
