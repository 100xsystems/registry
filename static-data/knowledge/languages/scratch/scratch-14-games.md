---
{
  "title": "Build a Game: Catcher",
  "description": "A complete catch game.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Design a game loop",
    "Control a paddle",
    "Spawn falling items",
    "Track score"
  ],
  "knowledge_refs": [
    "scratch/scratch-14-games"
  ],
  "prerequisites": [
    "Scratch-13: Clones"
  ],
  "references": [
    {
      "title": "Scratch Wiki",
      "url": "https://en.scratch-wiki.info/",
      "description": "The official wiki"
    },
    {
      "title": "Scratch Documentation",
      "url": "https://scratch.mit.edu/",
      "description": "Official site"
    },
    {
      "title": "Scratch Forums",
      "url": "https://scratch.mit.edu/discuss/",
      "description": "Community forum"
    }
  ]
}
---

# SCRATCH-14-GAMES: Build a Game: Catcher

## Introduction

A complete catch game. By the end of this lesson you will be able to: Design a game loop; Control a paddle; Spawn falling items; Track score.

## Key Concepts

### 1. Design a game loop

Target: Design a game loop. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```text
# Player: follow mouse-pointer with paddle sprite
```
### 2. Control a paddle

Target: Control a paddle. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```text
# Items: repeat forever, create clone, move down
```
### 3. Spawn falling items

Target: Spawn falling items. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```text
# Clones: if touching player, add 1 to score, delete clone
```
### 4. Track score

Target: Track score. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```text
# Game over: if lives = 0, stop all
```

## Practice Questions

1. What is the key idea behind "Build a Game: Catcher"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Build a Game: Catcher with analogies and real-world examples"
1. "Show me common mistakes beginners make with Build a Game: Catcher"
1. "Provide advanced patterns and performance considerations for Build a Game: Catcher"

## Key Takeaways

- Master the core ideas of Build a Game: Catcher through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
