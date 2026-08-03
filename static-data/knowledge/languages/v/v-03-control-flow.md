---
{
  "title": "Control Flow",
  "description": "if, match, and loops.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write if/else",
    "Use match",
    "Use for loops",
    "Use loops over ranges"
  ],
  "knowledge_refs": [
    "v/v-03-control-flow"
  ],
  "prerequisites": [
    "V-02: Variables and Types"
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

# V-03-CONTROL-FLOW: Control Flow

## Introduction

if, match, and loops. By the end of this lesson you will be able to: Write if/else; Use match; Use for loops; Use loops over ranges.

## Key Concepts

### 1. Write if/else

Target: Write if/else. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
score := 85
if score >= 90 {
	println("A")
} else if score >= 80 {
	println("B")
} else {
	println("C")
}
```
### 2. Use match

Target: Use match. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
n := 2
match n {
	1 { println("one") }
	2 { println("two") }
	else { println("other") }
}
```
### 3. Use for loops

Target: Use for loops. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
for i in 0..5 {
	println(i)
}
```
### 4. Use loops over ranges

Target: Use loops over ranges. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
for i := 0; i < 5; i++ {
	println(i)
}
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
