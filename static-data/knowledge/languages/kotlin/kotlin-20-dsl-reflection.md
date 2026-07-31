---
{
  "title": "DSLs, Reflection, and Metaprogramming",
  "description": "Type-safe builders, reflection, and annotation processing.",
  "type": "lesson",
  "order": 20,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Build type-safe DSLs",
    "Inspect types with reflection",
    "Use annotation processing",
    "Write compiler plugins conceptually"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-20-dsl-reflection"
  ],
  "prerequisites": [
    "KOTLIN-19"
  ],
  "references": [
    {
      "title": "Kotlin — Type-Safe Builders",
      "url": "https://kotlinlang.org/docs/type-safe-builders.html"
    },
    {
      "title": "Kotlin — Reflection",
      "url": "https://kotlinlang.org/docs/reflection.html"
    },
    {
      "title": "Kotlin — Annotations",
      "url": "https://kotlinlang.org/docs/annotations.html"
    }
  ]
}
---

# KOTLIN-20-DSL-REFLECTION: DSLs, Reflection, and Metaprogramming

## Introduction

Type-safe builders, reflection, and annotation processing. By the end of this lesson you will be able to: Build type-safe DSLs; Inspect types with reflection; Use annotation processing; Write compiler plugins conceptually.

## Key Concepts

### 1. Build type-safe DSLs

Target: Build type-safe DSLs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// type-safe builder DSL
class HtmlBuilder {
    private val parts = mutableListOf<String>()
    fun p(text: String) { parts.add("<p>$text</p>") }
    fun h1(text: String) { parts.add("<h1>$text</h1>") }
    override fun toString(): String = parts.joinToString("\n")
}
fun html(builder: HtmlBuilder.() -> Unit): String {
    val b = HtmlBuilder()
    b.builder()
    return b.toString()
}
fun main() {
    val page = html {
        h1("Title")
        p("Body text")
    }
    println(page)
}
```
### 2. Inspect types with reflection

Target: Inspect types with reflection. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// reflection
fun main() {
    data class User(val name: String)
    val props = User::class.members.map { it.name }
    println(props.contains("name"))
    val klass = "hello".let { it.javaClass }
    println(klass.simpleName)
}
```
### 3. Use annotation processing

Target: Use annotation processing. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// annotations
@Target(AnnotationTarget.FUNCTION)
@Retention(AnnotationRetention.RUNTIME)
annotation class RateLimit(val limit: Int)
@RateLimit(100)
fun apiCall() = println("calling api")
fun main() {
    val ann = ::apiCall.annotations.firstOrNull()
    println(ann)
}
```
### 4. Write compiler plugins conceptually

Target: Write compiler plugins conceptually. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// kotlin.test assertions
import kotlin.test.*
fun main() {
    assertEquals(4, 2 + 2)
    assertContains(listOf(1, 2), 2)
    assertTrue("abc".length == 3)
    println("kotlin.test works")
}
```

## Practice Questions

1. What is the key idea behind "DSLs, Reflection, and Metaprogramming"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain DSLs, Reflection, and Metaprogramming with analogies and real-world examples"
1. "Show me common mistakes beginners make with DSLs, Reflection, and Metaprogramming"
1. "Provide advanced patterns and performance considerations for DSLs, Reflection, and Metaprogramming"

## Key Takeaways

- Master the core ideas of DSLs, Reflection, and Metaprogramming through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
