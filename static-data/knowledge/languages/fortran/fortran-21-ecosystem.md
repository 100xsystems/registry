---
{
  "title": "Ecosystem and Next Steps",
  "description": "Modern tooling and the Fortran community.",
  "type": "lesson",
  "order": 21,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use fpm package manager",
    "Discover modern libraries",
    "Use Fortran stdlib",
    "Contribute to the community"
  ],
  "knowledge_refs": [
    "fortran/fortran-21-ecosystem"
  ],
  "prerequisites": [
    "Fortran-20: Scientific Computing Patterns"
  ],
  "references": [
    {
      "title": "Fortran 90/95 Standard",
      "url": "https://wg5-fortran.org/",
      "description": "The official standards committee"
    },
    {
      "title": "Fortran Best Practices",
      "url": "https://fortran-lang.org/en/learn/",
      "description": "fortran-lang.org learning resources"
    },
    {
      "title": "Modern Fortran Explained",
      "url": "https://www.oxford.universitypressscholarship.com/",
      "description": "Metcalf, Reid & Cohen textbook"
    }
  ]
}
---

# FORTRAN-21-ECOSYSTEM: Ecosystem and Next Steps

## Introduction

Modern tooling and the Fortran community. By the end of this lesson you will be able to: Use fpm package manager; Discover modern libraries; Use Fortran stdlib; Contribute to the community.

## Key Concepts

### 1. Use fpm package manager

Target: Use fpm package manager. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
fpm new my_project
cd my_project && fpm run
```
### 2. Discover modern libraries

Target: Discover modern libraries. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
fpm add stdlib
```
### 3. Use Fortran stdlib

Target: Use Fortran stdlib. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
use stdlib_strings, only: to_string
print *, "n=" // to_string(42)
```
### 4. Contribute to the community

Target: Contribute to the community. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
fpm test   # run the test suite
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
