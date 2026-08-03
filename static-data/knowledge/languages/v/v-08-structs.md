---
{
  "title": "Structs",
  "description": "User-defined types.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define structs",
    "Create instances",
    "Access fields",
    "Use struct methods"
  ],
  "knowledge_refs": [
    "v/v-08-structs"
  ],
  "prerequisites": [
    "V-07: Strings"
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

# V-08-STRUCTS: Structs

## Introduction

User-defined types. By the end of this lesson you will be able to: Define structs; Create instances; Access fields; Use struct methods.

## Key Concepts

### 1. Define structs

Target: Define structs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
struct Person {
	name string
	age int
}

ada := Person{
	name: "Ada"
	age: 36
}
println(ada.name)
```
### 2. Create instances

Target: Create instances. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
mut p := Person{}
p.name = "Grace"
p.age = 85
```
### 3. Access fields

Target: Access fields. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
struct Point {
	x int
	y int
}

p := Point{1, 2}
```
### 4. Use struct methods

Target: Use struct methods. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
fn (p Person) greet() string {
	return "Hi, I am ${p.name}"
}

println(ada.greet())
```

## Practice Questions

1. What is the key idea behind "Structs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Structs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Structs"
1. "Provide advanced patterns and performance considerations for Structs"

## Key Takeaways

- Master the core ideas of Structs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
