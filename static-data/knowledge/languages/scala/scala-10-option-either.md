---
{
  "title": "Option and Either for Safe Handling",
  "description": "Replace null and exceptions with Option and Either for total functions.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use Option to model values that may be absent",
    "Chain optional computations with map, flatMap and getOrElse",
    "Use Either for computations that can fail with a reason",
    "Combine Either values with for comprehensions"
  ],
  "knowledge_refs": [
    "scala/scala-10-option-either"
  ],
  "prerequisites": [
    "SCALA-09"
  ],
  "references": [
    "https://docs.scala-lang.org/scala3/book/types-union.html",
    "https://www.scala-lang.org/api/current/scala/Option.html",
    "https://www.scala-lang.org/api/current/scala/util/Either.html"
  ]
}
---

# SCALA-10-OPTION-EITHER: Option and Either for Safe Handling

## Introduction

Replace null and exceptions with Option and Either for total functions. By the end of this lesson you will be able to: Use Option to model values that may be absent; Chain optional computations with map, flatMap and getOrElse; Use Either for computations that can fail with a reason; Combine Either values with for comprehensions.

## Key Concepts

### 1. Use Option to model values that may be absent

Target: Use Option to model values that may be absent. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// Option for possibly-absent values
@main def find(): Unit =
  val names = Map("ada" -> 36, "alan" -> 41)
  println(names.get("ada"))    // Some(36)
  println(names.get("grace"))  // None
```
### 2. Chain optional computations with map, flatMap and getOrElse

Target: Chain optional computations with map, flatMap and getOrElse. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// chain optional computations
@main def chain(): Unit =
  def half(n: Int): Option[Int] = if n % 2 == 0 then Some(n / 2) else None
  val result = Some(16).flatMap(half).flatMap(half)
  println(result)   // Some(4)
  println(result.getOrElse(-1))
```
### 3. Use Either for computations that can fail with a reason

Target: Use Either for computations that can fail with a reason. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// Either with a failure reason
@main def divide(a: Int, b: Int): Unit =
  val res: Either[String, Int] =
    if b == 0 then Left("division by zero") else Right(a / b)
  println(res.fold(err => s"ERROR: $err", v => s"OK: $v"))
```
### 4. Combine Either values with for comprehensions

Target: Combine Either values with for comprehensions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// combine Options with for comprehension
@main def combine(): Unit =
  def parse(s: String): Option[Int] = s.toIntOption
  val result: Option[Int] = for
    a <- parse("10")
    b <- parse("5")
    if b != 0
  yield a / b
  println(result)  // Some(2)
```

## Practice Questions

1. What is the key idea behind "Option and Either for Safe Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Option and Either for Safe Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Option and Either for Safe Handling"
1. "Provide advanced patterns and performance considerations for Option and Either for Safe Handling"

## Key Takeaways

- Master the core ideas of Option and Either for Safe Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
