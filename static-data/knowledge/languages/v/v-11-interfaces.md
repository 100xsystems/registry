---
{
  "title": "Interfaces and Sum Types",
  "description": "Polymorphism.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define interfaces",
    "Implement interfaces",
    "Use sum types",
    "Use type switches"
  ],
  "knowledge_refs": [
    "v/v-11-interfaces"
  ],
  "prerequisites": [
    "V-10: Optionals and Results"
  ],
  "references": [
    {
      "title": "V Documentation",
      "url": "https://docs.vlang.io/",
      "description": "Official docs"
    },
    {
      "title": "V Manual",
      "url": "https://docs.vlang.io/introduction.html",
      "description": "Language manual"
    },
    {
      "title": "V Language GitHub",
      "url": "https://github.com/vlang/v",
      "description": "Source code"
    }
  ]
}
---

# V-11-INTERFACES: Interfaces and Sum Types

## Introduction

Polymorphism. By the end of this lesson you will be able to: Define interfaces; Implement interfaces; Use sum types; Use type switches.

## Key Concepts

### 1. Define interfaces

Target: Define interfaces. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
interface Shape {
	area() f64
}

struct Circle {
	radius f64
}

fn (c Circle) area() f64 {
	return 3.14159 * c.radius * c.radius
}
```
### 2. Implement interfaces

Target: Implement interfaces. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
fn print_area(s Shape) {
	println(s.area())
}
```
### 3. Use sum types

Target: Use sum types. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
type Expr = Num | Add | Mul
struct Num {
	value int
}
struct Add {
	a Expr
	b Expr
}
```
### 4. Use type switches

Target: Use type switches. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
match e {
	Num { println("num: ${e.value}") }
	Add { println("add") }
}
```

## Practice Questions

1. What is the key idea behind "Interfaces and Sum Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Interfaces and Sum Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Interfaces and Sum Types"
1. "Provide advanced patterns and performance considerations for Interfaces and Sum Types"

## Key Takeaways

- Master the core ideas of Interfaces and Sum Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
