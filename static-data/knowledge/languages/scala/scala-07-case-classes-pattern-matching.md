---
{
  "title": "Case Classes and Pattern Matching",
  "description": "Model data with case classes and destructure it with pattern matching.",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define case classes and use their auto-generated equality and copy",
    "Destructure tuples, options and case classes in patterns",
    "Guard patterns with conditions and bind variables",
    "Model algebraic data types with sealed traits and case objects"
  ],
  "knowledge_refs": [
    "scala/scala-07-case-classes-pattern-matching"
  ],
  "prerequisites": [
    "SCALA-06"
  ],
  "references": [
    "https://docs.scala-lang.org/scala3/book/domain-modeling-tools.html",
    "https://docs.scala-lang.org/tour/case-classes.html",
    "https://docs.scala-lang.org/scala3/book/pattern-matching.html"
  ]
}
---

# SCALA-07-CASE-CLASSES-PATTERN-MATCHING: Case Classes and Pattern Matching

## Introduction

Model data with case classes and destructure it with pattern matching. By the end of this lesson you will be able to: Define case classes and use their auto-generated equality and copy; Destructure tuples, options and case classes in patterns; Guard patterns with conditions and bind variables; Model algebraic data types with sealed traits and case objects.

## Key Concepts

### 1. Define case classes and use their auto-generated equality and copy

Target: Define case classes and use their auto-generated equality and copy. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// case class with auto-generated equals/hashCode/copy
case class Point(x: Int, y: Int)
@main def points(): Unit =
  val p1 = Point(1, 2)
  val p2 = Point(1, 2)
  println(p1 == p2)          // true
  println(p1.copy(y = 99))   // Point(1, 99)
```
### 2. Destructure tuples, options and case classes in patterns

Target: Destructure tuples, options and case classes in patterns. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// destructure in patterns
@main def destructure(): Unit =
  val (a, b) = (1, 2)
  val Point(x, _) = Point(10, 20)
  println(s"a=$a b=$b x=$x")
```
### 3. Guard patterns with conditions and bind variables

Target: Guard patterns with conditions and bind variables. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// sealed trait ADT
sealed trait Shape
case class Circle(radius: Double) extends Shape
case class Rect(w: Double, h: Double) extends Shape
@main def area(s: Shape): Unit =
  val result = s match
    case Circle(r) => math.Pi * r * r
    case Rect(w, h) => w * h
  println(result)
```
### 4. Model algebraic data types with sealed traits and case objects

Target: Model algebraic data types with sealed traits and case objects. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// guards and variable binding
@main def classify(n: Int): Unit =
  val kind = n match
    case 0 => "zero"
    case x if x < 0 => "negative"
    case _ => "positive"
  println(kind)
```

## Practice Questions

1. What is the key idea behind "Case Classes and Pattern Matching"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Case Classes and Pattern Matching with analogies and real-world examples"
1. "Show me common mistakes beginners make with Case Classes and Pattern Matching"
1. "Provide advanced patterns and performance considerations for Case Classes and Pattern Matching"

## Key Takeaways

- Master the core ideas of Case Classes and Pattern Matching through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
