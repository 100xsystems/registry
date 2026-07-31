---
{
  "title": "Contextual Abstractions in Depth",
  "description": "Master using clauses, given instances and contextual lookup for flexible APIs.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write methods that require contextual parameters with using",
    "Define given instances and control implicit resolution scope",
    "Use contextual abstractions to build configurable systems",
    "Implement type classes with automatic derivation where possible"
  ],
  "knowledge_refs": [
    "scala/scala-20-contextual-abstractions"
  ],
  "prerequisites": [
    "SCALA-19"
  ],
  "references": [
    "https://docs.scala-lang.org/scala3/book/types-givens.html",
    "https://docs.scala-lang.org/scala3/reference/contextual/index.html",
    "https://docs.scala-lang.org/scala3/reference/contextual/derivation.html"
  ]
}
---

# SCALA-20-CONTEXTUAL-ABSTRACTIONS: Contextual Abstractions in Depth

## Introduction

Master using clauses, given instances and contextual lookup for flexible APIs. By the end of this lesson you will be able to: Write methods that require contextual parameters with using; Define given instances and control implicit resolution scope; Use contextual abstractions to build configurable systems; Implement type classes with automatic derivation where possible.

## Key Concepts

### 1. Write methods that require contextual parameters with using

Target: Write methods that require contextual parameters with using. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// using clauses in method signatures
@main def sort(): Unit =
  given Ordering[Int] = Ordering.Int.reverse
  def top3[A](xs: List[A])(using ord: Ordering[A]): List[A] =
    xs.sorted(ord).take(3)
  println(top3(List(5, 1, 9, 3, 7)))  // 9, 7, 5
```
### 2. Define given instances and control implicit resolution scope

Target: Define given instances and control implicit resolution scope. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// scoping given instances
@main def scope(): Unit =
  case class Point(x: Int, y: Int)
  given Ordering[Point] = Ordering.by(p => (p.y, p.x))
  val pts = List(Point(1, 5), Point(2, 3), Point(4, 3))
  println(pts.sorted)
```
### 3. Use contextual abstractions to build configurable systems

Target: Use contextual abstractions to build configurable systems. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// type classes with derivation
import scala.deriving.*
import scala.compiletime.*
trait ToJson[A]:
  def json(a: A): String
case class User(name: String, age: Int)
@main def derive(): Unit =
  given ToJson[User] with
    def json(u: User): String = s"{\"name\":\"${u.name}\",\"age\":${u.age}}"
  def emit[A](a: A)(using t: ToJson[A]): String = t.json(a)
  println(emit(User("Ada", 36)))
```
### 4. Implement type classes with automatic derivation where possible

Target: Implement type classes with automatic derivation where possible. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// contextual function types (Scala 3)
@main def ctx(): Unit =
  case class Env(debug: Boolean)
  type Effect[A] = Env ?=> A
  def log(msg: String): Effect[Unit] =
    if summon[Env].debug then println(msg)
  given Env = Env(debug = true)
  log("debugging enabled")
```

## Practice Questions

1. What is the key idea behind "Contextual Abstractions in Depth"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Contextual Abstractions in Depth with analogies and real-world examples"
1. "Show me common mistakes beginners make with Contextual Abstractions in Depth"
1. "Provide advanced patterns and performance considerations for Contextual Abstractions in Depth"

## Key Takeaways

- Master the core ideas of Contextual Abstractions in Depth through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
