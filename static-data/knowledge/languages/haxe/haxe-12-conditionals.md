---
{
  "title": "Compile-Time Conditionals",
  "description": "Platform and build flags.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use #if/#elseif/#end",
    "Check targets",
    "Define build flags",
    "Write platform code"
  ],
  "knowledge_refs": [
    "haxe/haxe-12-conditionals"
  ],
  "prerequisites": [
    "Haxe-11: Typedefs"
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

# HAXE-12-CONDITIONALS: Compile-Time Conditionals

## Introduction

Platform and build flags. By the end of this lesson you will be able to: Use #if/#elseif/#end; Check targets; Define build flags; Write platform code.

## Key Concepts

### 1. Use #if/#elseif/#end

Target: Use #if/#elseif/#end. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
#if js
trace("running in JS");
#end
```
### 2. Check targets

Target: Check targets. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
#if (cpp || neko)
trace("native target");
#end
```
### 3. Define build flags

Target: Define build flags. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
haxe -main Main -js app.js -D debug
```
### 4. Write platform code

Target: Write platform code. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
#if debug
trace("debug build");
#end
```

## Practice Questions

1. What is the key idea behind "Compile-Time Conditionals"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Compile-Time Conditionals with analogies and real-world examples"
1. "Show me common mistakes beginners make with Compile-Time Conditionals"
1. "Provide advanced patterns and performance considerations for Compile-Time Conditionals"

## Key Takeaways

- Master the core ideas of Compile-Time Conditionals through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
