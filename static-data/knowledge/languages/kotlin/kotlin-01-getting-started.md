---
{
  "title": "Getting Started with Kotlin",
  "description": "Install the compiler, run scripts, and meet the Kotlin playground.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install Kotlin and run your first program",
    "Use println and string templates",
    "Compile with kotlinc or run with kotlin",
    "Understand the JVM/JS/Native targets"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Kotlin — Getting Started",
      "url": "https://kotlinlang.org/docs/getting-started.html"
    },
    {
      "title": "Kotlin — Basic Syntax",
      "url": "https://kotlinlang.org/docs/basic-syntax.html"
    },
    {
      "title": "Kotlin Playground",
      "url": "https://play.kotlinlang.org/"
    }
  ]
}
---

# KOTLIN-01-GETTING-STARTED: Getting Started with Kotlin

## Introduction

Install the compiler, run scripts, and meet the Kotlin playground. By the end of this lesson you will be able to: Install Kotlin and run your first program; Use println and string templates; Compile with kotlinc or run with kotlin; Understand the JVM/JS/Native targets.

## Key Concepts

### 1. Install Kotlin and run your first program

Target: Install Kotlin and run your first program. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// hello.kt — compile: kotlinc hello.kt -include-runtime -d hello.jar
// run: java -jar hello.jar
fun main() {
    println("Hello, 100x Systems!")
    val name = "Kotlin"
    println("Welcome to $name!")
}
```
### 2. Use println and string templates

Target: Use println and string templates. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// script mode: kotlinc -script hello.kts
fun main(args: Array<String>) {
    println("args = ${args.joinToString()}")
    val who = args.firstOrNull() ?: "world"
    println("Hello, $who")
}
main()
```
### 3. Compile with kotlinc or run with kotlin

Target: Compile with kotlinc or run with kotlin. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// multiple targets
println("JVM: ${System.getProperty("java.version")}")
// Native -> standalone binary
// JS     -> browser/server code
// Wasm   -> WebAssembly
println("targets: JVM, Native, JS, Wasm")
```
### 4. Understand the JVM/JS/Native targets

Target: Understand the JVM/JS/Native targets. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// command-line tools
// kotlinc file.kt            -> compile to .class
// kotlinc -script x.kts      -> run as script
// kotlin file.kt             -> run directly
// kotlinc-jvm                -> JVM compiler
println("toolchain ready")
```

## Practice Questions

1. What is the key idea behind "Getting Started with Kotlin"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Kotlin with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Kotlin"
1. "Provide advanced patterns and performance considerations for Getting Started with Kotlin"

## Key Takeaways

- Master the core ideas of Getting Started with Kotlin through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
