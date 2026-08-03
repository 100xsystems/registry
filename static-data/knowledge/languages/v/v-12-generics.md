---
{
  "title": "Generics",
  "description": "Type-parameterized code.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write generic functions",
    "Use generic structs",
    "Constrain types",
    "Build containers"
  ],
  "knowledge_refs": [
    "v/v-12-generics"
  ],
  "prerequisites": [
    "V-11: Interfaces and Sum Types"
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

# V-12-GENERICS: Generics

## Introduction

Type-parameterized code. By the end of this lesson you will be able to: Write generic functions; Use generic structs; Constrain types; Build containers.

## Key Concepts

### 1. Write generic functions

Target: Write generic functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
fn identity[T](x T) T {
	return x
}

println(identity(42))
println(identity("hi"))
```
### 2. Use generic structs

Target: Use generic structs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
struct Box[T] {
	value T
}

b := Box[int]{value: 42}
```
### 3. Constrain types

Target: Constrain types. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
fn max[T](a T, b T) T {
	return if a > b { a } else { b }
}
```
### 4. Build containers

Target: Build containers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
fn first[T](arr []T) T {
	return arr[0]
}
```

## Practice Questions

1. What is the key idea behind "Generics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Generics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Generics"
1. "Provide advanced patterns and performance considerations for Generics"

## Key Takeaways

- Master the core ideas of Generics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
