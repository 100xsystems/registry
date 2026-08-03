---
{
  "title": "Heaps Game Engine",
  "description": "High-performance 2D/3D.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create a Heaps scene",
    "Load sprites",
    "Handle the game loop",
    "Build for targets"
  ],
  "knowledge_refs": [
    "haxe/haxe-17-heaps"
  ],
  "prerequisites": [
    "Haxe-16: Games with OpenFL"
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

# HAXE-17-HEAPS: Heaps Game Engine

## Introduction

High-performance 2D/3D. By the end of this lesson you will be able to: Create a Heaps scene; Load sprites; Handle the game loop; Build for targets.

## Key Concepts

### 1. Create a Heaps scene

Target: Create a Heaps scene. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
import hxd.App;

class Main extends hxd.App {
  override function init() {
    trace("Heaps!");
  }
}
```
### 2. Load sprites

Target: Load sprites. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
var tile = hxd.Res.mySprite.toTile();
var bmp = new h2d.Bitmap(tile, s2d);
```
### 3. Handle the game loop

Target: Handle the game loop. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
override function update(dt:Float) {
  // game loop
}
```
### 4. Build for targets

Target: Build for targets. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
// build with: heaps.io toolchain
```

## Practice Questions

1. What is the key idea behind "Heaps Game Engine"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Heaps Game Engine with analogies and real-world examples"
1. "Show me common mistakes beginners make with Heaps Game Engine"
1. "Provide advanced patterns and performance considerations for Heaps Game Engine"

## Key Takeaways

- Master the core ideas of Heaps Game Engine through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
