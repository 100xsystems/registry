---
{
  "title": "Type Classes and Givens",
  "description": "Implement ad-hoc polymorphism with type classes and given instances.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define a type class trait with abstract operations",
    "Provide given instances for your own and library types",
    "Use given and using to wire dependencies implicitly",
    "Write extension methods that work with type class instances"
  ],
  "knowledge_refs": [
    "scala/scala-13-type-classes-implicits"
  ],
  "prerequisites": [
    "SCALA-12"
  ],
  "references": [
    "https://docs.scala-lang.org/scala3/book/types-type-classes.html",
    "https://docs.scala-lang.org/scala3/reference/contextual/givens.html",
    "https://docs.scala-lang.org/scala3/reference/contextual/using-clauses.html"
  ]
}
---

# SCALA-13-TYPE-CLASSES-IMPLICITS: Type Classes and Givens

## Introduction

Implement ad-hoc polymorphism with type classes and given instances. By the end of this lesson you will be able to: Define a type class trait with abstract operations; Provide given instances for your own and library types; Use given and using to wire dependencies implicitly; Write extension methods that work with type class instances.

## Key Concepts

### 1. Define a type class trait with abstract operations

Target: Define a type class trait with abstract operations. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// define a type class
trait Show[A]:
  def show(a: A): String
@main def tc(): Unit =
  given Show[Int] with
    def show(a: Int): String = s"int:$a"
  def printIt[A](a: A)(using s: Show[A]): Unit = println(s.show(a))
  printIt(42)
```
### 2. Provide given instances for your own and library types

Target: Provide given instances for your own and library types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// given instances for your own types
case class Money(amount: Double, currency: String)
given Show[Money] with
  def show(m: Money): String = f"${m.amount}%.2f ${m.currency}"
@main def money(): Unit =
  def fmt[A](a: A)(using s: Show[A]): String = s.show(a)
  println(fmt(Money(19.99, "USD")))
```
### 3. Use given and using to wire dependencies implicitly

Target: Use given and using to wire dependencies implicitly. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// using clauses wire dependencies
@main def config(): Unit =
  case class Config(retries: Int)
  given Config = Config(3)
  def fetch(url: String)(using cfg: Config): String =
    s"fetch $url with ${cfg.retries} retries"
  println(fetch("https://api.example.com"))
```
### 4. Write extension methods that work with type class instances

Target: Write extension methods that work with type class instances. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// extension methods with type classes
trait Stringify[A]:
  def render(a: A): String
extension [A](a: A)(using s: Stringify[A])
  def pretty: String = s.render(a)
@main def extTc(): Unit =
  given Stringify[Int] with
    def render(i: Int): String = s"<int>$i</int>"
  println(5.pretty)
```

## Practice Questions

1. What is the key idea behind "Type Classes and Givens"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Type Classes and Givens with analogies and real-world examples"
1. "Show me common mistakes beginners make with Type Classes and Givens"
1. "Provide advanced patterns and performance considerations for Type Classes and Givens"

## Key Takeaways

- Master the core ideas of Type Classes and Givens through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
