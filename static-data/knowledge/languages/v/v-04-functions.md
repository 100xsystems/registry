---
{
  "title": "Functions",
  "description": "Typed functions and multiple returns.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write functions",
    "Use return types",
    "Return multiple values",
    "Use default params"
  ],
  "knowledge_refs": [
    "v/v-04-functions"
  ],
  "prerequisites": [
    "V-03: Control Flow"
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

# V-04-FUNCTIONS: Functions

## Introduction

Typed functions and multiple returns. By the end of this lesson you will be able to: Write functions; Use return types; Return multiple values; Use default params.

## Key Concepts

### 1. Write functions

Target: Write functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
fn add(a int, b int) int {
	return a + b
}

fn main() {
	println(add(2, 3))
}
```
### 2. Use return types

Target: Use return types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
fn divmod(a int, b int) (int, int) {
	return a / b, a % b
}

q, r := divmod(7, 2)
```
### 3. Return multiple values

Target: Return multiple values. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
fn greet(name string) string {
	return "Hello, " + name
}
```
### 4. Use default params

Target: Use default params. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
fn apply(f fn (int) int, x int) int {
	return f(x)
}
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
