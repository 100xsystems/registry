---
{
  "title": "Exporting Games",
  "description": "Build for platforms.",
  "type": "lesson",
  "order": 19,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Configure export presets",
    "Export for desktop",
    "Export for web",
    "Optimize builds"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-19-export-game"
  ],
  "prerequisites": [
    "GDScript-18: Autoload Singletons"
  ],
  "references": [
    {
      "title": "Godot Docs: GDScript",
      "url": "https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/index.html",
      "description": "Official documentation"
    },
    {
      "title": "GDScript Reference",
      "url": "https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html",
      "description": "Language reference"
    },
    {
      "title": "Godot Community",
      "url": "https://godotengine.org/community/",
      "description": "Community links"
    }
  ]
}
---

# GDSCRIPT-19-EXPORT-GAME: Exporting Games

## Introduction

Build for platforms. By the end of this lesson you will be able to: Configure export presets; Export for desktop; Export for web; Optimize builds.

## Key Concepts

### 1. Configure export presets

Target: Configure export presets. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
project.godot
[application]
config/name="My Game"
```
### 2. Export for desktop

Target: Export for desktop. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
godot --headless --export-release "Windows Desktop" build/game.exe
```
### 3. Export for web

Target: Export for web. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
godot --headless --export-release "Web" build/index.html
```
### 4. Optimize builds

Target: Optimize builds. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
--optimize: enable texture compression in export settings
```

## Practice Questions

1. What is the key idea behind "Exporting Games"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Exporting Games with analogies and real-world examples"
1. "Show me common mistakes beginners make with Exporting Games"
1. "Provide advanced patterns and performance considerations for Exporting Games"

## Key Takeaways

- Master the core ideas of Exporting Games through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
