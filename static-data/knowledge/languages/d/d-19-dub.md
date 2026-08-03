---
{
  "title": "DUB and Packaging",
  "description": "Package management and builds.",
  "type": "lesson",
  "order": 19,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create a DUB project",
    "Add dependencies",
    "Build and run",
    "Publish packages"
  ],
  "knowledge_refs": [
    "d/d-19-dub"
  ],
  "prerequisites": [
    "D-18: Unit Testing with unittest"
  ],
  "references": [
    {
      "title": "D Language Reference",
      "url": "https://dlang.org/spec/spec.html",
      "description": "Official language spec"
    },
    {
      "title": "D Programming Tour",
      "url": "https://tour.dlang.org/",
      "description": "Interactive language tour"
    },
    {
      "title": "D Wiki",
      "url": "https://wiki.dlang.org/",
      "description": "Community wiki"
    },
    {
      "title": "DUB Package Manager",
      "url": "https://code.dlang.org/",
      "description": "Package registry"
    }
  ]
}
---

# D-19-DUB: DUB and Packaging

## Introduction

Package management and builds. By the end of this lesson you will be able to: Create a DUB project; Add dependencies; Build and run; Publish packages.

## Key Concepts

### 1. Create a DUB project

Target: Create a DUB project. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
dub init myapp
cd myapp && dub run
```
### 2. Add dependencies

Target: Add dependencies. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
{
  "name": "myapp",
  "dependencies": {
    "vibe-d": "~>0.9"
  }
}
```
### 3. Build and run

Target: Build and run. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
dub add deimos-openssl
// or edit dub.json
```
### 4. Publish packages

Target: Publish packages. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
dub build -b release
```

## Practice Questions

1. What is the key idea behind "DUB and Packaging"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain DUB and Packaging with analogies and real-world examples"
1. "Show me common mistakes beginners make with DUB and Packaging"
1. "Provide advanced patterns and performance considerations for DUB and Packaging"

## Key Takeaways

- Master the core ideas of DUB and Packaging through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
