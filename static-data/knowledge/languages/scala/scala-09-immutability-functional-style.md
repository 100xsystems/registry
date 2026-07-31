---
{
  "title": "Immutability and Functional Style",
  "description": "Write pure, referentially transparent code that avoids shared mutable state.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Keep data immutable and update structures via copy methods",
    "Recognize and isolate side effects in program boundaries",
    "Write pure functions that are easy to test and reason about",
    "Refactor a mutable imperative routine into a functional pipeline"
  ],
  "knowledge_refs": [
    "scala/scala-09-immutability-functional-style"
  ],
  "prerequisites": [
    "SCALA-08"
  ],
  "references": [
    "https://docs.scala-lang.org/scala3/book/functional-programming.html",
    "https://docs.scala-lang.org/scala3/book/fp-immutability.html",
    "https://docs.scala-lang.org/scala3/book/fp-pure-functions.html"
  ]
}
---

# SCALA-09-IMMUTABILITY-FUNCTIONAL-STYLE: Immutability and Functional Style

## Introduction

Write pure, referentially transparent code that avoids shared mutable state. By the end of this lesson you will be able to: Keep data immutable and update structures via copy methods; Recognize and isolate side effects in program boundaries; Write pure functions that are easy to test and reason about; Refactor a mutable imperative routine into a functional pipeline.

## Key Concepts

### 1. Keep data immutable and update structures via copy methods

Target: Keep data immutable and update structures via copy methods. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// update data with copy instead of mutation
case class User(name: String, age: Int, active: Boolean)
@main def copyDemo(): Unit =
  val u = User("Ada", 36, active = true)
  val older = u.copy(age = u.age + 1)
  println(older)
```
### 2. Recognize and isolate side effects in program boundaries

Target: Recognize and isolate side effects in program boundaries. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// pure function: same input, same output, no side effects
@main def pure(): Unit =
  def addTax(price: Double, rate: Double): Double = price * (1 + rate)
  println(addTax(100, 0.1))
  println(addTax(100, 0.1))  // same result every time
```
### 3. Write pure functions that are easy to test and reason about

Target: Write pure functions that are easy to test and reason about. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// refactor: imperative to functional pipeline
@main def pipeline(): Unit =
  val orders = List(15.0, 22.5, 8.0, 100.0)
  val total = orders
    .filter(_ > 10)
    .map(_ * 1.2)
    .sum
  println(total)
```
### 4. Refactor a mutable imperative routine into a functional pipeline

Target: Refactor a mutable imperative routine into a functional pipeline. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// isolate side effects at the boundary
@main def boundary(): Unit =
  def parse(s: String): Either[String, Int] =
    s.toIntOption.toRight(s"not a number: $s")
  def report(e: Either[String, Int]): String = e.fold(_.toUpperCase, _.toString)
  println(report(parse("42")))
  println(report(parse("abc")))
```

## Practice Questions

1. What is the key idea behind "Immutability and Functional Style"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Immutability and Functional Style with analogies and real-world examples"
1. "Show me common mistakes beginners make with Immutability and Functional Style"
1. "Provide advanced patterns and performance considerations for Immutability and Functional Style"

## Key Takeaways

- Master the core ideas of Immutability and Functional Style through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
