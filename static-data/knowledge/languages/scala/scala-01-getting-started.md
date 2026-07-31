---
{
  "title": "Getting Started with Scala 3",
  "description": "Set up the Scala toolchain and write your first programs in the REPL and with sbt.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install and run the Scala 3 toolchain (scala-cli, sbt)",
    "Explore expressions interactively in the Scala REPL",
    "Write and compile a standalone program with a main method",
    "Structure a minimal sbt project with source files and dependencies"
  ],
  "knowledge_refs": [
    "scala/scala-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    "https://docs.scala-lang.org/getting-started/index.html",
    "https://docs.scala-lang.org/scala3/book/taste-intro.html",
    "https://www.scala-lang.org/download/",
    "https://www.scala-sbt.org/1.x/docs/index.html"
  ]
}
---

# SCALA-01-GETTING-STARTED: Getting Started with Scala 3

## Introduction

Set up the Scala toolchain and write your first programs in the REPL and with sbt. By the end of this lesson you will be able to: Install and run the Scala 3 toolchain (scala-cli, sbt); Explore expressions interactively in the Scala REPL; Write and compile a standalone program with a main method; Structure a minimal sbt project with source files and dependencies.

## Key Concepts

### 1. Install and run the Scala 3 toolchain (scala-cli, sbt)

Target: Install and run the Scala 3 toolchain (scala-cli, sbt). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// Scala 3 REPL: run with scala-cli repl or sbt console
scala> val greeting = "Hello, Scala!"
scala> println(greeting.toUpperCase)
```
### 2. Explore expressions interactively in the Scala REPL

Target: Explore expressions interactively in the Scala REPL. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// @main is the Scala 3 entry point
// save as Hello.scala, run with: scala-cli run Hello.scala
@main def hello(): Unit =
  println("Hello, Scala!")
```
### 3. Write and compile a standalone program with a main method

Target: Write and compile a standalone program with a main method. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// sbt project layout:
//   build.sbt            -> project config
//   src/main/scala/      -> source files
//   src/test/scala/      -> test files
// build.sbt
ThisBuild / scalaVersion := "3.3.4"
lazy val root = project.in(file("."))
```
### 4. Structure a minimal sbt project with source files and dependencies

Target: Structure a minimal sbt project with source files and dependencies. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// types are inferred but can be annotated
@main def intro(): Unit =
  val n: Int = 42
  val s: String = "one hundred"
  val d: Double = 3.14
  println(s"The answer is $n, pi is $d, name is $s")
```

## Practice Questions

1. What is the key idea behind "Getting Started with Scala 3"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Scala 3 with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Scala 3"
1. "Provide advanced patterns and performance considerations for Getting Started with Scala 3"

## Key Takeaways

- Master the core ideas of Getting Started with Scala 3 through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
