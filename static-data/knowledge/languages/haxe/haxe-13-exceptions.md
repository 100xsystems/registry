---
{
  "title": "Exceptions",
  "description": "Throw and catch.",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Throw exceptions",
    "Catch exceptions",
    "Use try/catch",
    "Create custom errors"
  ],
  "knowledge_refs": [
    "haxe/haxe-13-exceptions"
  ],
  "prerequisites": [
    "Haxe-12: Compile-Time Conditionals"
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

# HAXE-13-EXCEPTIONS: Exceptions

## Introduction

Throw and catch. By the end of this lesson you will be able to: Throw exceptions; Catch exceptions; Use try/catch; Create custom errors.

## Key Concepts

### 1. Throw exceptions

Target: Throw exceptions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
try {
  throw "boom";
} catch (e:String) {
  trace(e);
}
```
### 2. Catch exceptions

Target: Catch exceptions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
try {
  risky();
} catch (e:Dynamic) {
  trace("error: " + e);
}
```
### 3. Use try/catch

Target: Use try/catch. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
class MyError extends haxe.Exception {
  public function new(msg:String) super(msg);
}
```
### 4. Create custom errors

Target: Create custom errors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
if (b == 0) throw "division by zero";
```

## Practice Questions

1. What is the key idea behind "Exceptions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Exceptions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Exceptions"
1. "Provide advanced patterns and performance considerations for Exceptions"

## Key Takeaways

- Master the core ideas of Exceptions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
