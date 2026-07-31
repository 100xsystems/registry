---
{
  "title": "Control Flow: if, match and Loops",
  "description": "Write expressive branching with if-expressions and pattern-matching match expressions.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use if/else as an expression that returns a value",
    "Match on values, guards and types with the match expression",
    "Iterate with while loops and for loops",
    "Compose conditions with Boolean operators and short-circuiting"
  ],
  "knowledge_refs": [
    "scala/scala-03-control-flow"
  ],
  "prerequisites": [
    "SCALA-02"
  ],
  "references": [
    "https://docs.scala-lang.org/scala3/book/control-structures.html",
    "https://docs.scala-lang.org/scala3/book/pattern-matching.html",
    "https://docs.scala-lang.org/tour/pattern-matching.html"
  ]
}
---

# SCALA-03-CONTROL-FLOW: Control Flow: if, match and Loops

## Introduction

Write expressive branching with if-expressions and pattern-matching match expressions. By the end of this lesson you will be able to: Use if/else as an expression that returns a value; Match on values, guards and types with the match expression; Iterate with while loops and for loops; Compose conditions with Boolean operators and short-circuiting.

## Key Concepts

### 1. Use if/else as an expression that returns a value

Target: Use if/else as an expression that returns a value. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// if/else is an expression with a value
@main def grade(score: Int): Unit =
  val result = if score >= 90 then "A" else if score >= 50 then "B" else "F"
  println(result)
```
### 2. Match on values, guards and types with the match expression

Target: Match on values, guards and types with the match expression. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// match expression with guards
@main def status(code: Int): Unit =
  val label = code match
    case 200 => "OK"
    case 404 => "Not Found"
    case n if n >= 500 => "Server Error"
    case _ => "Other"
  println(label)
```
### 3. Iterate with while loops and for loops

Target: Iterate with while loops and for loops. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// while loop for side effects
@main def loop(): Unit =
  var n = 5
  while n > 0 do
    println(n)
    n -= 1
```
### 4. Compose conditions with Boolean operators and short-circuiting

Target: Compose conditions with Boolean operators and short-circuiting. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// for loop over a range
@main def forloop(): Unit =
  for i <- 1 to 5 do
    println(s"i = $i")
  for c <- "ab" do println(c)
```

## Practice Questions

1. What is the key idea behind "Control Flow: if, match and Loops"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow: if, match and Loops with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow: if, match and Loops"
1. "Provide advanced patterns and performance considerations for Control Flow: if, match and Loops"

## Key Takeaways

- Master the core ideas of Control Flow: if, match and Loops through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
