---
{
  "title": "Tail Recursion and Performance",
  "description": "Write stack-safe recursion and reason about allocation and performance.",
  "type": "lesson",
  "order": 19,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Identify tail-recursive calls and annotate with @tailrec",
    "Convert naive recursion into accumulator-based tail recursion",
    "Use lazy val for memoized, on-demand initialization",
    "Avoid common performance pitfalls with collections and boxing"
  ],
  "knowledge_refs": [
    "scala/scala-19-tail-recursion"
  ],
  "prerequisites": [
    "SCALA-18"
  ],
  "references": [
    "https://docs.scala-lang.org/scala3/book/taste-functions.html",
    "https://www.scala-lang.org/api/current/scala/annotation/tailrec.html"
  ]
}
---

# SCALA-19-TAIL-RECURSION: Tail Recursion and Performance

## Introduction

Write stack-safe recursion and reason about allocation and performance. By the end of this lesson you will be able to: Identify tail-recursive calls and annotate with @tailrec; Convert naive recursion into accumulator-based tail recursion; Use lazy val for memoized, on-demand initialization; Avoid common performance pitfalls with collections and boxing.

## Key Concepts

### 1. Identify tail-recursive calls and annotate with @tailrec

Target: Identify tail-recursive calls and annotate with @tailrec. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// @tailrec guarantees stack safety
import scala.annotation.tailrec
@main def fact(): Unit =
  @tailrec
  def factorial(n: Int, acc: Int): Int =
    if n <= 1 then acc else factorial(n - 1, acc * n)
  println(factorial(10, 1))
```
### 2. Convert naive recursion into accumulator-based tail recursion

Target: Convert naive recursion into accumulator-based tail recursion. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// naive recursion overflows the stack
@main def naive(): Unit =
  def sum(n: Int): Int =
    if n == 0 then 0 else n + sum(n - 1)   // not tail-recursive
  println(sum(10))
```
### 3. Use lazy val for memoized, on-demand initialization

Target: Use lazy val for memoized, on-demand initialization. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// lazy val memoizes on demand
@main def lazyVal(): Unit =
  lazy val heavy = {
    println("computing...")
    40 + 2
  }
  println("before")
  println(heavy)  // computing happens here
  println(heavy)  // cached
```
### 4. Avoid common performance pitfalls with collections and boxing

Target: Avoid common performance pitfalls with collections and boxing. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// avoid boxing in hot loops
@main def boxing(): Unit =
  def sumEven(n: Int): Long =
    var total = 0L
    var i = 0
    while i < n do
      if i % 2 == 0 then total += i
      i += 1
    total
  println(sumEven(100))
```

## Practice Questions

1. What is the key idea behind "Tail Recursion and Performance"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Tail Recursion and Performance with analogies and real-world examples"
1. "Show me common mistakes beginners make with Tail Recursion and Performance"
1. "Provide advanced patterns and performance considerations for Tail Recursion and Performance"

## Key Takeaways

- Master the core ideas of Tail Recursion and Performance through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
