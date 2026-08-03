---
{
  "title": "Ecosystem and Next Steps",
  "description": "Shards, community, and production use.",
  "type": "lesson",
  "order": 21,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use shards package manager",
    "Discover popular shards",
    "Build production services",
    "Join the community"
  ],
  "knowledge_refs": [
    "crystal/crystal-21-ecosystem"
  ],
  "prerequisites": [
    "Crystal-20: Testing with Spec"
  ],
  "references": [
    {
      "title": "Crystal Language Reference",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official docs"
    },
    {
      "title": "Crystal for Rubyists",
      "url": "https://crystal-lang.org/reference/guides/faq.html",
      "description": "Migration guide"
    },
    {
      "title": "Crystal Book",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official reference book"
    },
    {
      "title": "Crystal Forum",
      "url": "https://forum.crystal-lang.org/",
      "description": "Community"
    }
  ]
}
---

# CRYSTAL-21-ECOSYSTEM: Ecosystem and Next Steps

## Introduction

Shards, community, and production use. By the end of this lesson you will be able to: Use shards package manager; Discover popular shards; Build production services; Join the community.

## Key Concepts

### 1. Use shards package manager

Target: Use shards package manager. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
shards init my_app
shards install
```
### 2. Discover popular shards

Target: Discover popular shards. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
dependencies:
  kemal:
    github: kemalcr/kemal
```
### 3. Build production services

Target: Build production services. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
shards search http
```
### 4. Join the community

Target: Join the community. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
puts "Crystal compiles to native binaries — great for CLIs"
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
