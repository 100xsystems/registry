---
{
  "title": "Generics",
  "description": "Type-parameterized code.",
  "type": "lesson",
  "order": 14,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write generic classes",
    "Constrain type params",
    "Use generic methods",
    "Build containers"
  ],
  "knowledge_refs": [
    "crystal/crystal-14-generics"
  ],
  "prerequisites": [
    "Crystal-13: File and Standard IO"
  ],
  "references": [
    {
      "title": "Crystal Language Reference",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official docs"
    },
    {
      "title": "Crystal for Rubyists",
      "url": "https://crystal-lang.org/reference/guides/faq.html",
      "description": "Migration guide"
    },
    {
      "title": "Crystal Book",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official reference book"
    },
    {
      "title": "Crystal Forum",
      "url": "https://forum.crystal-lang.org/",
      "description": "Community"
    }
  ]
}
---

# CRYSTAL-14-GENERICS: Generics

## Introduction

Type-parameterized code. By the end of this lesson you will be able to: Write generic classes; Constrain type params; Use generic methods; Build containers.

## Key Concepts

### 1. Write generic classes

Target: Write generic classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
class Box(T)
  getter value : T

  def initialize(@value)
  end
end

b = Box(Int32).new(42)
puts b.value
```
### 2. Constrain type params

Target: Constrain type params. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
def first(t : Array(T)) forall T
  t.first
end
```
### 3. Use generic methods

Target: Use generic methods. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
class Pair(A, B)
  getter a : A
  getter b : B

  def initialize(@a, @b)
  end
end
```
### 4. Build containers

Target: Build containers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
class Stack(T)
  @items = [] of T

  def push(item : T)
    @items << item
  end
end
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
