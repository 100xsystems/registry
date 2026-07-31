---
{
  "title": "Inheritance and Interfaces",
  "description": "open classes, abstract classes, and interfaces.",
  "type": "lesson",
  "order": 9,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Extend open classes and override members",
    "Design with abstract classes",
    "Implement interfaces and delegation",
    "Use sealed classes for hierarchies"
  ],
  "knowledge_refs": [
    "kotlin/kotlin-09-inheritance-interfaces"
  ],
  "prerequisites": [
    "KOTLIN-08"
  ],
  "references": [
    {
      "title": "Kotlin — Inheritance",
      "url": "https://kotlinlang.org/docs/inheritance.html"
    },
    {
      "title": "Kotlin — Interfaces",
      "url": "https://kotlinlang.org/docs/interfaces.html"
    },
    {
      "title": "Kotlin — Sealed Classes",
      "url": "https://kotlinlang.org/docs/sealed-classes.html"
    }
  ]
}
---

# KOTLIN-09-INHERITANCE-INTERFACES: Inheritance and Interfaces

## Introduction

open classes, abstract classes, and interfaces. By the end of this lesson you will be able to: Extend open classes and override members; Design with abstract classes; Implement interfaces and delegation; Use sealed classes for hierarchies.

## Key Concepts

### 1. Extend open classes and override members

Target: Extend open classes and override members. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```kotlin
// open + override
open class Animal(val name: String) {
    open fun speak(): String = "..."
}
class Dog(name: String) : Animal(name) {
    override fun speak(): String = "Woof!"
}
fun main() {
    println(Dog("Rex").speak())  // Woof!
}
```
### 2. Design with abstract classes

Target: Design with abstract classes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```kotlin
// abstract classes
abstract class Shape {
    abstract fun area(): Double
    fun describe(): String = "area = ${area()}"
}
class Circle(val r: Double) : Shape() {
    override fun area(): Double = Math.PI * r * r
}
fun main() {
    println(Circle(2.0).describe())
}
```
### 3. Implement interfaces and delegation

Target: Implement interfaces and delegation. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```kotlin
// interfaces + delegation
interface Logger {
    fun log(msg: String)
}
class ConsoleLogger : Logger {
    override fun log(msg: String) = println("[log] $msg")
}
class App : Logger by ConsoleLogger()
fun main() {
    App().log("booted")  // delegated
}
```
### 4. Use sealed classes for hierarchies

Target: Use sealed classes for hierarchies. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```kotlin
// sealed hierarchies
sealed class HttpResult {
    data class Ok(val body: String) : HttpResult()
    data class Err(val code: Int) : HttpResult()
}
fun describe(r: HttpResult): String = when (r) {
    is HttpResult.Ok -> "ok: ${r.body}"
    is HttpResult.Err -> "err: ${r.code}"
}
fun main() {
    println(describe(HttpResult.Ok("data")))
}
```

## Practice Questions

1. What is the key idea behind "Inheritance and Interfaces"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Inheritance and Interfaces with analogies and real-world examples"
1. "Show me common mistakes beginners make with Inheritance and Interfaces"
1. "Provide advanced patterns and performance considerations for Inheritance and Interfaces"

## Key Takeaways

- Master the core ideas of Inheritance and Interfaces through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
