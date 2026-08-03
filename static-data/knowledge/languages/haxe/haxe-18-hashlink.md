---
{
  "title": "HashLink VM",
  "description": "Native VM for Haxe.",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand HashLink",
    "Compile to HL",
    "Use hxd for graphics",
    "Run native code"
  ],
  "knowledge_refs": [
    "haxe/haxe-18-hashlink"
  ],
  "prerequisites": [
    "Haxe-17: Heaps Game Engine"
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

# HAXE-18-HASHLINK: HashLink VM

## Introduction

Native VM for Haxe. By the end of this lesson you will be able to: Understand HashLink; Compile to HL; Use hxd for graphics; Run native code.

## Key Concepts

### 1. Understand HashLink

Target: Understand HashLink. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
haxe -main Main -hl out.hl
hl out.hl
```
### 2. Compile to HL

Target: Compile to HL. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
haxe -main Main -hl out.c
# then compile C to a native binary
```
### 3. Use hxd for graphics

Target: Use hxd for graphics. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
// HL has JIT and AOT modes
```
### 4. Run native code

Target: Run native code. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
hl --run out.hl
```

## Practice Questions

1. What is the key idea behind "HashLink VM"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain HashLink VM with analogies and real-world examples"
1. "Show me common mistakes beginners make with HashLink VM"
1. "Provide advanced patterns and performance considerations for HashLink VM"

## Key Takeaways

- Master the core ideas of HashLink VM through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
