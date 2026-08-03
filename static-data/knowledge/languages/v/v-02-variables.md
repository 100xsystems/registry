---
{
  "title": "Variables and Types",
  "description": "immutable, mut, and built-in types.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare immutable vars",
    "Use mut variables",
    "Use built-in types",
    "Use string interpolation"
  ],
  "knowledge_refs": [
    "v/v-02-variables"
  ],
  "prerequisites": [
    "V-01: Getting Started with V"
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

# V-02-VARIABLES: Variables and Types

## Introduction

immutable, mut, and built-in types. By the end of this lesson you will be able to: Declare immutable vars; Use mut variables; Use built-in types; Use string interpolation.

## Key Concepts

### 1. Declare immutable vars

Target: Declare immutable vars. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
fn main() {
	name := "Ada"
	age := 36
	println(name)
}
```
### 2. Use mut variables

Target: Use mut variables. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
mut count := 0
count++
println(count)
```
### 3. Use built-in types

Target: Use built-in types. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
x := 42
y := 3.14
b := true
```
### 4. Use string interpolation

Target: Use string interpolation. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
println("Hello, ${name}!")
```

## Practice Questions

1. What is the key idea behind "Variables and Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Types"
1. "Provide advanced patterns and performance considerations for Variables and Types"

## Key Takeaways

- Master the core ideas of Variables and Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
