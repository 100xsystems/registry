---
{
  "title": "Strings",
  "description": "String operations and interpolation.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Concatenate strings",
    "Use string interpolation",
    "Split and join",
    "Use string methods"
  ],
  "knowledge_refs": [
    "haxe/haxe-06-strings"
  ],
  "prerequisites": [
    "Haxe-05: Arrays and Maps"
  ],
  "references": [
    {
      "title": "Haxe Documentation",
      "url": "https://haxe.org/documentation/",
      "description": "Official docs"
    },
    {
      "title": "Haxe Manual",
      "url": "https://haxe.org/manual/introduction.html",
      "description": "The language manual"
    },
    {
      "title": "Haxe Cookbook",
      "url": "https://code.haxe.org/",
      "description": "Community recipes"
    }
  ]
}
---

# HAXE-06-STRINGS: Strings

## Introduction

String operations and interpolation. By the end of this lesson you will be able to: Concatenate strings; Use string interpolation; Split and join; Use string methods.

## Key Concepts

### 1. Concatenate strings

Target: Concatenate strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
var s = "Hello" + " " + "World";
```
### 2. Use string interpolation

Target: Use string interpolation. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
var name = "Ada";
var msg = "Hello, $name";   // interpolation
```
### 3. Split and join

Target: Split and join. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
var parts = "a,b,c".split(",");
```
### 4. Use string methods

Target: Use string methods. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
trace("hello".toUpperCase());
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
