---
{
  "title": "File I/O and Serialization",
  "description": "Reading and writing files, and kotlinx.serialization.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read and write text files",
    "Work with the java.io and java.nio APIs",
    "Serialize with kotlinx.serialization",
    "Handle binary data"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-14-file-io"
  ],
  "prerequisites": [
    "KOTLIN-11"
  ],
  "references": [
    {
      "title": "Kotlin — Serialization",
      "url": "https://kotlinlang.org/docs/serialization.html"
    },
    {
      "title": "Kotlinx Serialization — GitHub",
      "url": "https://github.com/Kotlin/kotlinx.serialization"
    },
    {
      "title": "Java — File I/O Guide",
      "url": "https://docs.oracle.com/javase/tutorial/essential/io/"
    }
  ]
}
---

# KOTLIN-14-FILE-IO: File I/O and Serialization

## Introduction

Reading and writing files, and kotlinx.serialization. By the end of this lesson you will be able to: Read and write text files; Work with the java.io and java.nio APIs; Serialize with kotlinx.serialization; Handle binary data.

## Key Concepts

### 1. Read and write text files

Target: Read and write text files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// reading and writing files
import java.io.File
fun main() {
    File("data.txt").writeText("line one\nline two\n")
    val text = File("data.txt").readText()
    val lines = File("data.txt").readLines()
    println(text)
    println(lines)
}
```
### 2. Work with the java.io and java.nio APIs

Target: Work with the java.io and java.nio APIs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// paths with java.nio
import java.nio.file.Files
import java.nio.file.Path
fun main() {
    val p = Path.of("data.txt")
    Files.writeString(p, "hello nio")
    println(Files.readString(p))
    Files.deleteIfExists(p)
}
```
### 3. Serialize with kotlinx.serialization

Target: Serialize with kotlinx.serialization. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// serialization setup
// build.gradle.kts:
//   plugins { kotlin("plugin.serialization") version "2.0.0" }
//   dependencies { implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.0") }
import kotlinx.serialization.Serializable
@Serializable
data class User(val name: String, val age: Int)
```
### 4. Handle binary data

Target: Handle binary data. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// JSON round-trip
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json
@Serializable
data class Item(val id: Int, val title: String)
fun main() {
    val json = Json.encodeToString(Item(1, "keyboard"))
    println(json)                     // {"id":1,"title":"keyboard"}
    val back = Json.decodeFromString<Item>(json)
    println(back.title)
}
```

## Practice Questions

1. What is the key idea behind "File I/O and Serialization"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File I/O and Serialization with analogies and real-world examples"
1. "Show me common mistakes beginners make with File I/O and Serialization"
1. "Provide advanced patterns and performance considerations for File I/O and Serialization"

## Key Takeaways

- Master the core ideas of File I/O and Serialization through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
