---
{
  "title": "Generics",
  "description": "Type-parameterized code.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write generic classes",
    "Constrain type params",
    "Use type parameters in functions",
    "Build containers"
  ],
  "knowledge_refs": [
    "haxe/haxe-10-generics"
  ],
  "prerequisites": [
    "Haxe-09: Abstract Types"
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

# HAXE-10-GENERICS: Generics

## Introduction

Type-parameterized code. By the end of this lesson you will be able to: Write generic classes; Constrain type params; Use type parameters in functions; Build containers.

## Key Concepts

### 1. Write generic classes

Target: Write generic classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
class Box<T> {
  public var value:T;
  public function new(v:T) value = v;
}
```
### 2. Constrain type params

Target: Constrain type params. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
function identity<T>(x:T):T return x;
```
### 3. Use type parameters in functions

Target: Use type parameters in functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
class Stack<T> {
  var items:Array<T> = [];
  public function push(item:T) items.push(item);
}
```
### 4. Build containers

Target: Build containers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
function max<T:(Int, Float)>(a:T, b:T):T return a > b ? a : b;
```

## Practice Questions

1. What is the key idea behind "Generics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Generics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Generics"
1. "Provide advanced patterns and performance considerations for Generics"

## Key Takeaways

- Master the core ideas of Generics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
