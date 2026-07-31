---
{
  "title": "Error Handling with Try and Either",
  "description": "Model failures explicitly and recover with Try, Either and validated data.",
  "type": "lesson",
  "order": 17,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Wrap risky operations in Try and inspect success or failure",
    "Convert exceptions into typed Either results",
    "Recover from errors with recover and recoverWith",
    "Combine fallible operations into readable pipelines"
  ],
  "knowledge_refs": [
    "scala/scala-17-error-handling-try"
  ],
  "prerequisites": [
    "SCALA-16"
  ],
  "references": [
    "https://www.scala-lang.org/api/current/scala/util/Try.html",
    "https://www.scala-lang.org/api/current/scala/util/Success.html",
    "https://www.scala-lang.org/api/current/scala/util/Failure.html"
  ]
}
---

# SCALA-17-ERROR-HANDLING-TRY: Error Handling with Try and Either

## Introduction

Model failures explicitly and recover with Try, Either and validated data. By the end of this lesson you will be able to: Wrap risky operations in Try and inspect success or failure; Convert exceptions into typed Either results; Recover from errors with recover and recoverWith; Combine fallible operations into readable pipelines.

## Key Concepts

### 1. Wrap risky operations in Try and inspect success or failure

Target: Wrap risky operations in Try and inspect success or failure. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// Try wraps risky operations
import scala.util.{Try, Success, Failure}
@main def risky(): Unit =
  val result = Try { "42".toInt }
  result match
    case Success(n) => println(s"parsed $n")
    case Failure(e) => println(s"failed: ${e.getMessage}")
```
### 2. Convert exceptions into typed Either results

Target: Convert exceptions into typed Either results. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// convert exceptions into Either
@main def toEither(): Unit =
  def parseInt(s: String): Either[String, Int] =
    Try(s.toInt).toEither.left.map(_.getMessage)
  println(parseInt("7"))
  println(parseInt("x"))
```
### 3. Recover from errors with recover and recoverWith

Target: Recover from errors with recover and recoverWith. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// recover from failures
import scala.util.{Try, Success, Failure}
@main def fallback(): Unit =
  val config = Try { sys.env("MISSING_KEY") }
    .recover { case _ => "default-value" }
  println(config.get)
```
### 4. Combine fallible operations into readable pipelines

Target: Combine fallible operations into readable pipelines. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// combine fallible operations
import scala.util.Try
@main def combined(): Unit =
  def parse(s: String): Try[Int] = Try(s.toInt)
  def divide(a: Int, b: Int): Try[Int] = Try(a / b)
  val result = for
    a <- parse("10")
    b <- parse("2")
    r <- divide(a, b)
  yield r
  println(result)  // Success(5)
```

## Practice Questions

1. What is the key idea behind "Error Handling with Try and Either"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Error Handling with Try and Either with analogies and real-world examples"
1. "Show me common mistakes beginners make with Error Handling with Try and Either"
1. "Provide advanced patterns and performance considerations for Error Handling with Try and Either"

## Key Takeaways

- Master the core ideas of Error Handling with Try and Either through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
