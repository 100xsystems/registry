---
{
  "title": "Putting It All Together",
  "description": "Build a complete idiomatic Scala program combining FP, OOP and safe IO.",
  "type": "lesson",
  "order": 21,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Design a small domain with case classes and sealed traits",
    "Compose parsing, validation and reporting into a pipeline",
    "Structure the program with a clear entry point and error handling",
    "Write tests that lock in the behavior of the full program"
  ],
  "knowledge_refs": [
    "scala/scala-21-idiomatic-scala"
  ],
  "prerequisites": [
    "SCALA-20"
  ],
  "references": [
    "https://docs.scala-lang.org/scala3/book/introduction.html",
    "https://docs.scala-lang.org/scala3/book/domain-modeling-intro.html"
  ]
}
---

# SCALA-21-IDIOMATIC-SCALA: Putting It All Together

## Introduction

Build a complete idiomatic Scala program combining FP, OOP and safe IO. By the end of this lesson you will be able to: Design a small domain with case classes and sealed traits; Compose parsing, validation and reporting into a pipeline; Structure the program with a clear entry point and error handling; Write tests that lock in the behavior of the full program.

## Key Concepts

### 1. Design a small domain with case classes and sealed traits

Target: Design a small domain with case classes and sealed traits. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// a complete domain model with ADTs
sealed trait OrderStatus
case object Pending extends OrderStatus
case class Shipped(tracking: String) extends OrderStatus
case class Delivered(ts: Long) extends OrderStatus
case class Order(id: String, amount: Double, status: OrderStatus)
```
### 2. Compose parsing, validation and reporting into a pipeline

Target: Compose parsing, validation and reporting into a pipeline. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// parsing + validation pipeline
@main def pipeline(): Unit =
  def parseAmount(raw: String): Either[String, Double] =
    raw.toDoubleOption.filter(_ > 0).toRight(s"invalid amount: $raw")
  def parseId(raw: String): Either[String, String] =
    Option.when(raw.nonEmpty)(raw).toRight("empty id")
  val order = for
    id <- parseId("A-1")
    amt <- parseAmount("99.50")
  yield Order(id, amt, Pending)
  println(order)
```
### 3. Structure the program with a clear entry point and error handling

Target: Structure the program with a clear entry point and error handling. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// reporting with safe error handling
@main def report(): Unit =
  val status = Order("A-1", 99.50, Shipped("TRK123"))
  val message = status.status match
    case Pending => "your order is pending"
    case Shipped(t) => s"shipped, tracking $t"
    case Delivered(_) => "delivered"
  println(message)
```
### 4. Write tests that lock in the behavior of the full program

Target: Write tests that lock in the behavior of the full program. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// lock behavior in with tests
import munit.FunSuite
class OrderSuite extends FunSuite:
  test("parse valid order") {
    val result = parseId("A-1").flatMap(id => parseAmount("10").map(Order(id, _, Pending)))
    assert(result.isRight)
  }
  def parseId(raw: String): Either[String, String] = Right(raw)
  def parseAmount(raw: String): Either[String, Double] = Right(raw.toDouble)
```

## Practice Questions

1. What is the key idea behind "Putting It All Together"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Putting It All Together with analogies and real-world examples"
1. "Show me common mistakes beginners make with Putting It All Together"
1. "Provide advanced patterns and performance considerations for Putting It All Together"

## Key Takeaways

- Master the core ideas of Putting It All Together through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
