---
{
  "title": "Generics and the Type System",
  "description": "Write reusable code with type parameters, bounds and variance.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define generic classes and methods with type parameters",
    "Constrain types with upper and lower bounds",
    "Understand covariance and contravariance for collections",
    "Use given instances for type-based dispatch"
  ],
  "knowledge_refs": [
    "scala/scala-12-generics-type-system"
  ],
  "prerequisites": [
    "SCALA-11"
  ],
  "references": [
    "https://docs.scala-lang.org/tour/generic-classes.html",
    "https://docs.scala-lang.org/tour/variances.html",
    "https://docs.scala-lang.org/tour/upper-type-bounds.html"
  ]
}
---

# SCALA-12-GENERICS-TYPE-SYSTEM: Generics and the Type System

## Introduction

Write reusable code with type parameters, bounds and variance. By the end of this lesson you will be able to: Define generic classes and methods with type parameters; Constrain types with upper and lower bounds; Understand covariance and contravariance for collections; Use given instances for type-based dispatch.

## Key Concepts

### 1. Define generic classes and methods with type parameters

Target: Define generic classes and methods with type parameters. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// generic class
class Box[A](val value: A)
@main def generic(): Unit =
  val intBox = Box(42)
  val strBox = Box("scala")
  println(intBox.value + 1)
  println(strBox.value.toUpperCase)
```
### 2. Constrain types with upper and lower bounds

Target: Constrain types with upper and lower bounds. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// generic method with upper bound
@main def max(): Unit =
  def maximum[A <: Comparable[A]](a: A, b: A): A =
    if a.compareTo(b) >= 0 then a else b
  println(maximum(3, 7))
  println(maximum("apple", "zebra"))
```
### 3. Understand covariance and contravariance for collections

Target: Understand covariance and contravariance for collections. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// variance: List is covariant
class Pet
class Dog extends Pet
@main def variance(): Unit =
  val dogs: List[Dog] = List(Dog())
  val pets: List[Pet] = dogs   // covariance works
  println(pets.size)
```
### 4. Use given instances for type-based dispatch

Target: Use given instances for type-based dispatch. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// union types for flexibility
@main def union(): Unit =
  def describe(x: Int | String): String = x match
    case i: Int => s"integer $i"
    case s: String => s"string $s"
  println(describe(42))
  println(describe("hi"))
```

## Practice Questions

1. What is the key idea behind "Generics and the Type System"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Generics and the Type System with analogies and real-world examples"
1. "Show me common mistakes beginners make with Generics and the Type System"
1. "Provide advanced patterns and performance considerations for Generics and the Type System"

## Key Takeaways

- Master the core ideas of Generics and the Type System through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
