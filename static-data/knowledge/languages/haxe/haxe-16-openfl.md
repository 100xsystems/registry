---
{
  "title": "Games with OpenFL",
  "description": "Cross-platform game framework.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Set up OpenFL",
    "Create a game project",
    "Draw sprites",
    "Handle input"
  ],
  "knowledge_refs": [
    "haxe/haxe-16-openfl"
  ],
  "prerequisites": [
    "Haxe-15: Macros"
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

# HAXE-16-OPENFL: Games with OpenFL

## Introduction

Cross-platform game framework. By the end of this lesson you will be able to: Set up OpenFL; Create a game project; Draw sprites; Handle input.

## Key Concepts

### 1. Set up OpenFL

Target: Set up OpenFL. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
lime create project MyGame
cd MyGame
```
### 2. Create a game project

Target: Create a game project. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
import openfl.display.Sprite;

class Main extends Sprite {
  public function new() {
    super();
    trace("OpenFL!");
  }
}
```
### 3. Draw sprites

Target: Draw sprites. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
lime test neko
```
### 4. Handle input

Target: Handle input. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
lime build html5
lime build mac
```

## Practice Questions

1. What is the key idea behind "Games with OpenFL"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Games with OpenFL with analogies and real-world examples"
1. "Show me common mistakes beginners make with Games with OpenFL"
1. "Provide advanced patterns and performance considerations for Games with OpenFL"

## Key Takeaways

- Master the core ideas of Games with OpenFL through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
