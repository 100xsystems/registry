---
{
  "title": "Plotting",
  "description": "Visualize functions.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Plot functions",
    "Use Plot options",
    "Plot lists",
    "Make 3D plots"
  ],
  "knowledge_refs": [
    "wolfram-language/wolfram-06-plotting"
  ],
  "prerequisites": [
    "Wolfram-05: Functions"
  ],
  "references": [
    {
      "title": "Wolfram Language Documentation",
      "url": "https://reference.wolfram.com/language/",
      "description": "Official reference"
    },
    {
      "title": "Wolfram Language Fast Introduction",
      "url": "https://www.wolfram.com/language/fast-introduction-for-programmers/en/",
      "description": "Fast intro"
    },
    {
      "title": "Wolfram Language Guide",
      "url": "https://reference.wolfram.com/language/guide/LanguageOverview.html",
      "description": "Language guide"
    }
  ]
}
---

# WOLFRAM-06-PLOTTING: Plotting

## Introduction

Visualize functions. By the end of this lesson you will be able to: Plot functions; Use Plot options; Plot lists; Make 3D plots.

## Key Concepts

### 1. Plot functions

Target: Plot functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```wolfram
Plot[Sin[x], {x, 0, 2 Pi}]
```
### 2. Use Plot options

Target: Use Plot options. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```wolfram
Plot[x^2, {x, -3, 3}, PlotStyle -> Red]
```
### 3. Plot lists

Target: Plot lists. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```wolfram
ListPlot[{1, 4, 9, 16}]
```
### 4. Make 3D plots

Target: Make 3D plots. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```wolfram
Plot3D[Sin[x] Cos[y], {x, -3, 3}, {y, -3, 3}]
```

## Practice Questions

1. What is the key idea behind "Plotting"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Plotting with analogies and real-world examples"
1. "Show me common mistakes beginners make with Plotting"
1. "Provide advanced patterns and performance considerations for Plotting"

## Key Takeaways

- Master the core ideas of Plotting through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
