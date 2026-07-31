---
{
  "title": "For Comprehensions and Monadic Composition",
  "description": "Sequence and transform monadic values with for comprehensions.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Understand that for comprehensions desugar to map, flatMap and withFilter",
    "Compose Options and Eithers with for comprehensions",
    "Nest generators and add value guards",
    "Use for loops for side-effecting iteration when appropriate"
  ],
  "knowledge_refs": [
    "scala/scala-11-for-comprehensions"
  ],
  "prerequisites": [
    "SCALA-10"
  ],
  "references": [
    "https://docs.scala-lang.org/tour/for-comprehensions.html",
    "https://docs.scala-lang.org/scala3/book/collections-immutable.html"
  ]
}
---

# SCALA-11-FOR-COMPREHENSIONS: For Comprehensions and Monadic Composition

## Introduction

Sequence and transform monadic values with for comprehensions. By the end of this lesson you will be able to: Understand that for comprehensions desugar to map, flatMap and withFilter; Compose Options and Eithers with for comprehensions; Nest generators and add value guards; Use for loops for side-effecting iteration when appropriate.

## Key Concepts

### 1. Understand that for comprehensions desugar to map, flatMap and withFilter

Target: Understand that for comprehensions desugar to map, flatMap and withFilter. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// for comprehension desugars to flatMap/map
@main def comp(): Unit =
  val nums = List(1, 2, 3)
  val letters = List("a", "b")
  val pairs = for n <- nums; l <- letters yield s"$n$l"
  println(pairs)
  val same = nums.flatMap(n => letters.map(l => s"$n$l"))
  println(same == pairs)  // true
```
### 2. Compose Options and Eithers with for comprehensions

Target: Compose Options and Eithers with for comprehensions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// guards filter values
@main def guards(): Unit =
  val nums = 1 to 10
  val result = for
    n <- nums
    if n % 3 == 0
  yield n * n
  println(result)  // Vector(9, 36, 81)
```
### 3. Nest generators and add value guards

Target: Nest generators and add value guards. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// compose Options
@main def options(): Unit =
  def parse(s: String): Option[Int] = s.toIntOption
  val combined: Option[Int] = for
    a <- parse("12")
    b <- parse("4")
    if b != 0
  yield a / b
  println(combined)  // Some(3)
```
### 4. Use for loops for side-effecting iteration when appropriate

Target: Use for loops for side-effecting iteration when appropriate. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// for loop for side effects
@main def printGrid(): Unit =
  for
    x <- 1 to 3
    y <- 1 to 2
  do println(s"($x,$y)")
```

## Practice Questions

1. What is the key idea behind "For Comprehensions and Monadic Composition"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain For Comprehensions and Monadic Composition with analogies and real-world examples"
1. "Show me common mistakes beginners make with For Comprehensions and Monadic Composition"
1. "Provide advanced patterns and performance considerations for For Comprehensions and Monadic Composition"

## Key Takeaways

- Master the core ideas of For Comprehensions and Monadic Composition through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
