---
{
  "title": "Concurrency with Futures and Promises",
  "description": "Run work on thread pools and combine asynchronous results with Futures.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create Futures with global or custom ExecutionContexts",
    "Compose async pipelines with map, flatMap and for comprehensions",
    "Recover from failures and fall back to alternatives",
    "Await results and handle timeouts deliberately"
  ],
  "knowledge_refs": [
    "scala/scala-14-concurrency-futures"
  ],
  "prerequisites": [
    "SCALA-13"
  ],
  "references": [
    "https://docs.scala-lang.org/overviews/core/futures.html",
    "https://www.scala-lang.org/api/current/scala/concurrent/Future.html",
    "https://www.scala-lang.org/api/current/scala/concurrent/ExecutionContext.html"
  ]
}
---

# SCALA-14-CONCURRENCY-FUTURES: Concurrency with Futures and Promises

## Introduction

Run work on thread pools and combine asynchronous results with Futures. By the end of this lesson you will be able to: Create Futures with global or custom ExecutionContexts; Compose async pipelines with map, flatMap and for comprehensions; Recover from failures and fall back to alternatives; Await results and handle timeouts deliberately.

## Key Concepts

### 1. Create Futures with global or custom ExecutionContexts

Target: Create Futures with global or custom ExecutionContexts. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// basic Future on the global context
import scala.concurrent.*
import scala.concurrent.ExecutionContext.Implicits.global
@main def future(): Unit =
  val f = Future { Thread.sleep(100); 21 * 2 }
  f.foreach(println)  // 42
```
### 2. Compose async pipelines with map, flatMap and for comprehensions

Target: Compose async pipelines with map, flatMap and for comprehensions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// compose async pipelines
import scala.concurrent.*
import scala.concurrent.ExecutionContext.Implicits.global
@main def pipeline(): Unit =
  def fetchUser(id: Int): Future[String] = Future { s"user-$id" }
  def fetchOrders(user: String): Future[Int] = Future { user.length * 3 }
  val total: Future[Int] = for
    user <- fetchUser(7)
    orders <- fetchOrders(user)
  yield orders
  total.foreach(n => println(s"orders: $n"))
```
### 3. Recover from failures and fall back to alternatives

Target: Recover from failures and fall back to alternatives. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// recover from failures
import scala.concurrent.*
import scala.concurrent.ExecutionContext.Implicits.global
@main def recover(): Unit =
  val risky = Future { throw new RuntimeException("boom") }
  val safe = risky.recover { case e: RuntimeException => s"caught: ${e.getMessage}" }
  safe.foreach(println)
```
### 4. Await results and handle timeouts deliberately

Target: Await results and handle timeouts deliberately. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// await with timeout
import scala.concurrent.*
import scala.concurrent.duration.*
import scala.concurrent.ExecutionContext.Implicits.global
@main def await(): Unit =
  val f = Future { Thread.sleep(50); "done" }
  val result = Await.result(f, 2.seconds)
  println(result)
```

## Practice Questions

1. What is the key idea behind "Concurrency with Futures and Promises"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Concurrency with Futures and Promises with analogies and real-world examples"
1. "Show me common mistakes beginners make with Concurrency with Futures and Promises"
1. "Provide advanced patterns and performance considerations for Concurrency with Futures and Promises"

## Key Takeaways

- Master the core ideas of Concurrency with Futures and Promises through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
