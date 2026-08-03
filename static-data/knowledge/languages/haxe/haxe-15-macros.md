---
{
  "title": "Macros",
  "description": "Compile-time metaprogramming.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write macro functions",
    "Inspect AST",
    "Generate code",
    "Use build macros"
  ],
  "knowledge_refs": [
    "haxe/haxe-15-macros"
  ],
  "prerequisites": [
    "Haxe-14: Iterators"
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

# HAXE-15-MACROS: Macros

## Introduction

Compile-time metaprogramming. By the end of this lesson you will be able to: Write macro functions; Inspect AST; Generate code; Use build macros.

## Key Concepts

### 1. Write macro functions

Target: Write macro functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
import haxe.macro.Context;

macro function hello() {
  return macro trace("from macro");
}
```
### 2. Inspect AST

Target: Inspect AST. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
macro function logMe(e:Expr) {
  trace(e);
  return e;
}
```
### 3. Generate code

Target: Generate code. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
@:build(macro function build() { ... })
class Generated { }
```
### 4. Use build macros

Target: Use build macros. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
macro function twice(e:Expr) {
  return macro { $e; $e; };
}
```

## Practice Questions

1. What is the key idea behind "Macros"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Macros with analogies and real-world examples"
1. "Show me common mistakes beginners make with Macros"
1. "Provide advanced patterns and performance considerations for Macros"

## Key Takeaways

- Master the core ideas of Macros through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
