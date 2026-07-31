---
{
  "title": "Testing with munit and ScalaTest",
  "description": "Write unit tests, property tests and test suites for Scala code.",
  "type": "lesson",
  "order": 16,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Set up munit tests in an sbt project",
    "Write assertions and expected-failure tests",
    "Organize suites with nested describes and fixtures",
    "Use property-based checks for edge-case coverage"
  ],
  "knowledge_refs": [
    "scala/scala-16-testing"
  ],
  "prerequisites": [
    "SCALA-15"
  ],
  "references": [
    "https://scalameta.org/munit/",
    "https://www.scalatest.org/user_guide",
    "https://docs.scala-lang.org/scala3/book/ca-given-imports.html"
  ]
}
---

# SCALA-16-TESTING: Testing with munit and ScalaTest

## Introduction

Write unit tests, property tests and test suites for Scala code. By the end of this lesson you will be able to: Set up munit tests in an sbt project; Write assertions and expected-failure tests; Organize suites with nested describes and fixtures; Use property-based checks for edge-case coverage.

## Key Concepts

### 1. Set up munit tests in an sbt project

Target: Set up munit tests in an sbt project. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// basic munit test
// in src/test/scala/CalcSuite.scala
import munit.FunSuite
class CalcSuite extends FunSuite:
  test("addition works") {
    assertEquals(2 + 2, 4)
  }
```
### 2. Write assertions and expected-failure tests

Target: Write assertions and expected-failure tests. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// assertions and failure expectations
import munit.FunSuite
class ErrSuite extends FunSuite:
  test("divide throws on zero") {
    intercept[ArithmeticException] {
      val _ = 1 / 0
    }
  }
```
### 3. Organize suites with nested describes and fixtures

Target: Organize suites with nested describes and fixtures. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// nested describes with fixtures
import munit.FunSuite
class DataSuite extends FunSuite:
  val nums = List(1, 2, 3)
  test("sum") { assertEquals(nums.sum, 6) }
  test("size") { assertEquals(nums.size, 3) }
```
### 4. Use property-based checks for edge-case coverage

Target: Use property-based checks for edge-case coverage. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// property-style checks with custom generators
import munit.FunSuite
class PropSuite extends FunSuite:
  test("identity function") {
    for i <- List(0, 1, 42, -7) do
      assertEquals(identity(i), i)
  }
```

## Practice Questions

1. What is the key idea behind "Testing with munit and ScalaTest"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with munit and ScalaTest with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing with munit and ScalaTest"
1. "Provide advanced patterns and performance considerations for Testing with munit and ScalaTest"

## Key Takeaways

- Master the core ideas of Testing with munit and ScalaTest through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
