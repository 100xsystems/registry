---
{
  "title": "Functions",
  "description": "Typed functions and lambdas.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write typed functions",
    "Use default arguments",
    "Use lambdas",
    "Use optional args"
  ],
  "knowledge_refs": [
    "haxe/haxe-04-functions"
  ],
  "prerequisites": [
    "Haxe-03: Control Flow"
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

# HAXE-04-FUNCTIONS: Functions

## Introduction

Typed functions and lambdas. By the end of this lesson you will be able to: Write typed functions; Use default arguments; Use lambdas; Use optional args.

## Key Concepts

### 1. Write typed functions

Target: Write typed functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
function add(a:Int, b:Int):Int {
  return a + b;
}
```
### 2. Use default arguments

Target: Use default arguments. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
function greet(name:String, excited:Bool = false):String {
  return excited ? "HI " + name : "hi " + name;
}
```
### 3. Use lambdas

Target: Use lambdas. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
var square = function(x:Int) return x * x;
trace(square(5));
```
### 4. Use optional args

Target: Use optional args. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
function greet(?name:String) {
  trace(name == null ? "no name" : name);
}
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
