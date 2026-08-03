---
{
  "title": "Ecosystem and Next Steps",
  "description": "Alire, libraries, and production Ada.",
  "type": "lesson",
  "order": 21,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use Alire package manager",
    "Discover key libraries",
    "Understand certification contexts",
    "Find community resources"
  ],
  "knowledge_refs": [
    "ada/ada-21-ecosystem"
  ],
  "prerequisites": [
    "Ada-20: Embedded and Real-Time Ada"
  ],
  "references": [
    {
      "title": "Ada Reference Manual",
      "url": "https://www.adaic.org/resources/add_content/standards/",
      "description": "The official language standard"
    },
    {
      "title": "Learn Ada",
      "url": "https://learn.adacore.com/",
      "description": "AdaCore official interactive course"
    },
    {
      "title": "Ada Programming (Wikibooks)",
      "url": "https://en.wikibooks.org/wiki/Ada_Programming",
      "description": "Community textbook"
    }
  ]
}
---

# ADA-21-ECOSYSTEM: Ecosystem and Next Steps

## Introduction

Alire, libraries, and production Ada. By the end of this lesson you will be able to: Use Alire package manager; Discover key libraries; Understand certification contexts; Find community resources.

## Key Concepts

### 1. Use Alire package manager

Target: Use Alire package manager. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
alr init --bin my_project
cd my_project && alr build
```
### 2. Discover key libraries

Target: Discover key libraries. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
alr search json   # find JSON libraries
```
### 3. Understand certification contexts

Target: Understand certification contexts. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
alr with libadalang --only
```
### 4. Find community resources

Target: Find community resources. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
gnatmake -gnatwa main.adb   # all warnings on
```

## Practice Questions

1. What is the key idea behind "Ecosystem and Next Steps"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Ecosystem and Next Steps with analogies and real-world examples"
1. "Show me common mistakes beginners make with Ecosystem and Next Steps"
1. "Provide advanced patterns and performance considerations for Ecosystem and Next Steps"

## Key Takeaways

- Master the core ideas of Ecosystem and Next Steps through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
