---
{
  "title": "Strings and String Templates",
  "description": "String literals, templates, and the string API.",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write strings and raw triple-quoted strings",
    "Interpolate with templates",
    "Manipulate strings with the standard library",
    "Work with multi-line and formatted output"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-04-strings"
  ],
  "prerequisites": [
    "KOTLIN-02"
  ],
  "references": [
    {
      "title": "Kotlin — Strings",
      "url": "https://kotlinlang.org/docs/strings.html"
    },
    {
      "title": "Kotlin — String Templates",
      "url": "https://kotlinlang.org/docs/basic-syntax.html#string-templates"
    },
    {
      "title": "Kotlin — Regex",
      "url": "https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/-regex/"
    }
  ]
}
---

# KOTLIN-04-STRINGS: Strings and String Templates

## Introduction

String literals, templates, and the string API. By the end of this lesson you will be able to: Write strings and raw triple-quoted strings; Interpolate with templates; Manipulate strings with the standard library; Work with multi-line and formatted output.

## Key Concepts

### 1. Write strings and raw triple-quoted strings

Target: Write strings and raw triple-quoted strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// literals and templates
fun main() {
    val name = "Alice"
    val age = 30
    val msg = "$name is $age years old"
    val expr = "double: ${age * 2}"
    val dollar = "cost: \$5"     // escaped dollar
    println(msg)
    println(expr)
    println(dollar)
}
```
### 2. Interpolate with templates

Target: Interpolate with templates. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// raw triple-quoted strings
fun main() {
    val raw = """
        Line one
        Line two
        """.trimIndent()
    println(raw)
    val withVars = """
        name: Alice
        age: 30
    """.trimIndent()
    println(withVars)
}
```
### 3. Manipulate strings with the standard library

Target: Manipulate strings with the standard library. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// string operations
fun main() {
    val s = "Hello, World"
    println(s.uppercase())         // HELLO, WORLD
    println(s.lowercase())
    println(s.startsWith("Hello")) // true
    println(s.split(","))          // [Hello,  World]
    println(s.replace("World", "Kotlin"))
    println(s.substring(0, 5))     // Hello
}
```
### 4. Work with multi-line and formatted output

Target: Work with multi-line and formatted output. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// builders and formats
fun main() {
    val sb = StringBuilder()
    repeat(3) { i -> sb.append("line$i; ") }
    println(sb)
    println("pi = %.2f".format(3.14159))  // pi = 3.14
    val csv = listOf("a", "b", "c").joinToString(" | ")
    println(csv)
}
```

## Practice Questions

1. What is the key idea behind "Strings and String Templates"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings and String Templates with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings and String Templates"
1. "Provide advanced patterns and performance considerations for Strings and String Templates"

## Key Takeaways

- Master the core ideas of Strings and String Templates through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
