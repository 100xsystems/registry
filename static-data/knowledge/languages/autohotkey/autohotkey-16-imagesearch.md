---
{
  "title": "Image and Pixel Search",
  "description": "Find on-screen images and colors.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use ImageSearch",
    "Use PixelSearch",
    "Click found locations",
    "Build automation loops"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-16-imagesearch"
  ],
  "prerequisites": [
    "AutoHotkey-15: Advanced Hotkeys"
  ],
  "references": [
    {
      "title": "AutoHotkey Documentation",
      "url": "https://www.autohotkey.com/docs/",
      "description": "Official docs"
    },
    {
      "title": "AutoHotkey v2 Changes",
      "url": "https://www.autohotkey.com/docs/v2/",
      "description": "Version 2 documentation"
    },
    {
      "title": "AutoHotkey Forum",
      "url": "https://www.autohotkey.com/boards/",
      "description": "Community forum"
    }
  ]
}
---

# AUTOHOTKEY-16-IMAGESEARCH: Image and Pixel Search

## Introduction

Find on-screen images and colors. By the end of this lesson you will be able to: Use ImageSearch; Use PixelSearch; Click found locations; Build automation loops.

## Key Concepts

### 1. Use ImageSearch

Target: Use ImageSearch. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
ImageSearch &x, &y, 0, 0, A_ScreenWidth, A_ScreenHeight, "button.png"
if (ErrorLevel = 0)
    Click x, y
```
### 2. Use PixelSearch

Target: Use PixelSearch. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
PixelSearch &px, &py, 0, 0, 100, 100, 0xFF0000
if (ErrorLevel = 0)
    MsgBox "found red at " px "," py
```
### 3. Click found locations

Target: Click found locations. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
loop
{
    ImageSearch &x, &y, 0, 0, 1000, 800, "target.png"
    if (ErrorLevel = 0)
        break
    Sleep 200
}
```
### 4. Build automation loops

Target: Build automation loops. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
CoordMode "Mouse", "Screen"
```

## Practice Questions

1. What is the key idea behind "Image and Pixel Search"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Image and Pixel Search with analogies and real-world examples"
1. "Show me common mistakes beginners make with Image and Pixel Search"
1. "Provide advanced patterns and performance considerations for Image and Pixel Search"

## Key Takeaways

- Master the core ideas of Image and Pixel Search through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
