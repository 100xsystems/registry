---
{
  "title": "Files and I/O",
  "description": "Read and write files, parse lines, and stream large inputs lazily.",
  "type": "lesson",
  "order": 15,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read text files line by line with scala.io.Source",
    "Write files with java.nio.file APIs",
    "Parse structured data such as CSV and JSON",
    "Manage resources safely with automatic resource handling"
  ],
  "knowledge_refs": [
    "scala/scala-15-files-io"
  ],
  "prerequisites": [
    "SCALA-14"
  ],
  "references": [
    "https://docs.scala-lang.org/overviews/scala-book/file-io.html",
    "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/file/Files.html",
    "https://www.scala-lang.org/api/current/scala/io/Source.html"
  ]
}
---

# SCALA-15-FILES-IO: Files and I/O

## Introduction

Read and write files, parse lines, and stream large inputs lazily. By the end of this lesson you will be able to: Read text files line by line with scala.io.Source; Write files with java.nio.file APIs; Parse structured data such as CSV and JSON; Manage resources safely with automatic resource handling.

## Key Concepts

### 1. Read text files line by line with scala.io.Source

Target: Read text files line by line with scala.io.Source. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// read a file line by line
import scala.io.Source
@main def readFile(path: String): Unit =
  val lines = Source.fromFile(path).getLines().toList
  lines.take(3).foreach(println)
  println(s"total lines: ${lines.size}")
```
### 2. Write files with java.nio.file APIs

Target: Write files with java.nio.file APIs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// write with java.nio
import java.nio.file.{Files, Paths}
@main def writeFile(): Unit =
  val content = List("one", "two", "three").mkString("\n")
  Files.writeString(Paths.get("out.txt"), content)
  println("written")
```
### 3. Parse structured data such as CSV and JSON

Target: Parse structured data such as CSV and JSON. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// parse CSV
@main def csv(): Unit =
  val raw = "name,age\nAda,36\nAlan,41"
  val rows = raw.linesIterator.map(_.split(",")).toList
  rows.drop(1).foreach { cols => println(s"${cols(0)} is ${cols(1)}") }
```
### 4. Manage resources safely with automatic resource handling

Target: Manage resources safely with automatic resource handling. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// using for automatic resource management
import scala.io.Source
@main def managed(): Unit =
  using Source.fromFile("data.txt") { source =>
    source.getLines().foreach(println)
  }
```

## Practice Questions

1. What is the key idea behind "Files and I/O"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Files and I/O with analogies and real-world examples"
1. "Show me common mistakes beginners make with Files and I/O"
1. "Provide advanced patterns and performance considerations for Files and I/O"

## Key Takeaways

- Master the core ideas of Files and I/O through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
