---
{
  "title": "Classes, Traits and Inheritance",
  "description": "Build object-oriented abstractions with classes, traits and extension.",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Declare classes with constructor parameters and access modifiers",
    "Define traits and mix them into classes for shared behavior",
    "Override methods and use abstract members",
    "Use extension methods to add behavior to existing types"
  ],
  "knowledge_refs": [
    "scala/scala-08-classes-traits"
  ],
  "prerequisites": [
    "SCALA-07"
  ],
  "references": [
    "https://docs.scala-lang.org/scala3/book/domain-modeling-oop.html",
    "https://docs.scala-lang.org/tour/traits.html",
    "https://docs.scala-lang.org/scala3/book/ca-extension-methods.html"
  ]
}
---

# SCALA-08-CLASSES-TRAITS: Classes, Traits and Inheritance

## Introduction

Build object-oriented abstractions with classes, traits and extension. By the end of this lesson you will be able to: Declare classes with constructor parameters and access modifiers; Define traits and mix them into classes for shared behavior; Override methods and use abstract members; Use extension methods to add behavior to existing types.

## Key Concepts

### 1. Declare classes with constructor parameters and access modifiers

Target: Declare classes with constructor parameters and access modifiers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// class with constructor params and access control
class Account(private var balance: Double):
  def deposit(amount: Double): Unit = balance += amount
  def current: Double = balance
@main def bank(): Unit =
  val acc = Account(100.0)
  acc.deposit(50)
  println(acc.current)  // 150.0
```
### 2. Define traits and mix them into classes for shared behavior

Target: Define traits and mix them into classes for shared behavior. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// trait as shared behavior
trait Greeter:
  def name: String
  def greet: String = s"Hello from $name"
class Robot(val name: String) extends Greeter
@main def greet(): Unit =
  println(Robot("R2D2").greet)
```
### 3. Override methods and use abstract members

Target: Override methods and use abstract members. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// abstract members and override
abstract class Animal:
  def sound: String
  def speak: String = s"$sound $sound"
class Dog extends Animal:
  override val sound = "woof"
@main def zoo(): Unit = println(Dog().speak)
```
### 4. Use extension methods to add behavior to existing types

Target: Use extension methods to add behavior to existing types. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// extension methods (Scala 3)
extension (n: Int)
  def isEven: Boolean = n % 2 == 0
  def cubed: Int = n * n * n
@main def ext(): Unit =
  println(4.isEven)
  println(3.cubed)
```

## Practice Questions

1. What is the key idea behind "Classes, Traits and Inheritance"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Classes, Traits and Inheritance with analogies and real-world examples"
1. "Show me common mistakes beginners make with Classes, Traits and Inheritance"
1. "Provide advanced patterns and performance considerations for Classes, Traits and Inheritance"

## Key Takeaways

- Master the core ideas of Classes, Traits and Inheritance through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
