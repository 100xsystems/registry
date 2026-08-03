---
{
  "title": "Enums",
  "description": "Typed enumerations.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define enums",
    "Use enum values",
    "Match enums",
    "Convert to strings"
  ],
  "knowledge_refs": [
    "v/v-09-enums"
  ],
  "prerequisites": [
    "V-08: Structs"
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

# V-09-ENUMS: Enums

## Introduction

Typed enumerations. By the end of this lesson you will be able to: Define enums; Use enum values; Match enums; Convert to strings.

## Key Concepts

### 1. Define enums

Target: Define enums. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
enum Color {
	red
	green
	blue
}

c := Color.green
println(c)
```
### 2. Use enum values

Target: Use enum values. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
match c {
	.red { println("red") }
	.green { println("green") }
	.blue { println("blue") }
}
```
### 3. Match enums

Target: Match enums. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
println(Color.values())
```
### 4. Convert to strings

Target: Convert to strings. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
c := Color.from_string("blue") or { Color.red }
```

## Practice Questions

1. What is the key idea behind "Enums"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Enums with analogies and real-world examples"
1. "Show me common mistakes beginners make with Enums"
1. "Provide advanced patterns and performance considerations for Enums"

## Key Takeaways

- Master the core ideas of Enums through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
