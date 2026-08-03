---
{
  "title": "Strings",
  "description": "String operations.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Concatenate strings",
    "Interpolate values",
    "Split and join",
    "Use string methods"
  ],
  "knowledge_refs": [
    "v/v-07-strings"
  ],
  "prerequisites": [
    "V-06: Maps"
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

# V-07-STRINGS: Strings

## Introduction

String operations. By the end of this lesson you will be able to: Concatenate strings; Interpolate values; Split and join; Use string methods.

## Key Concepts

### 1. Concatenate strings

Target: Concatenate strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
s := "Hello" + " " + "World"
println(s)
```
### 2. Interpolate values

Target: Interpolate values. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
name := "Ada"
println("Hello, $name!")
```
### 3. Split and join

Target: Split and join. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
println("a,b,c".split(",").join(" | "))
```
### 4. Use string methods

Target: Use string methods. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
println("hello".to_upper())
```

## Practice Questions

1. What is the key idea behind "Strings"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings"
1. "Provide advanced patterns and performance considerations for Strings"

## Key Takeaways

- Master the core ideas of Strings through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
