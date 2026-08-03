---
{
  "title": "Control Flow",
  "description": "if, switch, and loops.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write if/else",
    "Use switch with type patterns",
    "Use for loops",
    "Use while loops"
  ],
  "knowledge_refs": [
    "haxe/haxe-03-control-flow"
  ],
  "prerequisites": [
    "Haxe-02: Types and Variables"
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

# HAXE-03-CONTROL-FLOW: Control Flow

## Introduction

if, switch, and loops. By the end of this lesson you will be able to: Write if/else; Use switch with type patterns; Use for loops; Use while loops.

## Key Concepts

### 1. Write if/else

Target: Write if/else. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
var grade = 85;
if (grade >= 90) trace("A");
else if (grade >= 80) trace("B");
else trace("C");
```
### 2. Use switch with type patterns

Target: Use switch with type patterns. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
switch (n) {
  case 1: trace("one");
  case 2: trace("two");
  default: trace("other");
}
```
### 3. Use for loops

Target: Use for loops. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
for (i in 0...5) trace(i);
```
### 4. Use while loops

Target: Use while loops. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
var i = 0;
while (i < 3) { trace(i); i++; }
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
