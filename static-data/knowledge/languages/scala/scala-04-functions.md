---
{
  "title": "Defining Functions",
  "description": "Write functions with parameters, default values and named arguments.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define methods with explicit return types and parameter lists",
    "Use default parameter values and named arguments",
    "Write single-expression functions with the = syntax",
    "Pass functions as arguments using underscore and lambda syntax"
  ],
  "knowledge_refs": [
    "scala/scala-04-functions"
  ],
  "prerequisites": [
    "SCALA-03"
  ],
  "references": [
    "https://docs.scala-lang.org/scala3/book/methods.html",
    "https://docs.scala-lang.org/tour/default-parameter-values.html",
    "https://docs.scala-lang.org/tour/named-arguments.html"
  ]
}
---

# SCALA-04-FUNCTIONS: Defining Functions

## Introduction

Write functions with parameters, default values and named arguments. By the end of this lesson you will be able to: Define methods with explicit return types and parameter lists; Use default parameter values and named arguments; Write single-expression functions with the = syntax; Pass functions as arguments using underscore and lambda syntax.

## Key Concepts

### 1. Define methods with explicit return types and parameter lists

Target: Define methods with explicit return types and parameter lists. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// method with explicit return type
@main def funcs(): Unit =
  def square(x: Int): Int = x * x
  println(square(9))
```
### 2. Use default parameter values and named arguments

Target: Use default parameter values and named arguments. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// default parameters and named arguments
@main def greet(): Unit =
  def hello(name: String, punctuation: String = "!"): String =
    s"Hello, $name$punctuation"
  println(hello("Scala"))
  println(hello(punctuation = "?", name = "World"))
```
### 3. Write single-expression functions with the = syntax

Target: Write single-expression functions with the = syntax. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// single-expression method with = syntax
@main def combine(): Unit =
  def add(a: Int, b: Int) = a + b
  def sum(nums: Int*) = nums.sum   // varargs
  println(add(2, 3))
  println(sum(1, 2, 3, 4))
```
### 4. Pass functions as arguments using underscore and lambda syntax

Target: Pass functions as arguments using underscore and lambda syntax. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// pass functions as arguments
@main def applyTwice(): Unit =
  def twice(f: Int => Int, x: Int): Int = f(f(x))
  val inc: Int => Int = _ + 1
  println(twice(inc, 10))  // 12
```

## Practice Questions

1. What is the key idea behind "Defining Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Defining Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Defining Functions"
1. "Provide advanced patterns and performance considerations for Defining Functions"

## Key Takeaways

- Master the core ideas of Defining Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
