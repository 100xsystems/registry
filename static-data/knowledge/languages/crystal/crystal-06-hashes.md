---
{
  "title": "Hashes and Sets",
  "description": "Key-value storage.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create hashes",
    "Insert and fetch",
    "Iterate entries",
    "Use default values"
  ],
  "knowledge_refs": [
    "crystal/crystal-06-hashes"
  ],
  "prerequisites": [
    "Crystal-05: Arrays and Tuples"
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

# CRYSTAL-06-HASHES: Hashes and Sets

## Introduction

Key-value storage. By the end of this lesson you will be able to: Create hashes; Insert and fetch; Iterate entries; Use default values.

## Key Concepts

### 1. Create hashes

Target: Create hashes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
ages = {"ada" => 36, "grace" => 85}
puts ages["ada"]
```
### 2. Insert and fetch

Target: Insert and fetch. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
ages["alan"] = 41
puts ages
```
### 3. Iterate entries

Target: Iterate entries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
ages.each { |k, v| puts "#{k}: #{v}" }
```
### 4. Use default values

Target: Use default values. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
counts = Hash(String, Int32).new(0)
counts["x"] += 1
```

## Practice Questions

1. What is the key idea behind "Hashes and Sets"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Hashes and Sets with analogies and real-world examples"
1. "Show me common mistakes beginners make with Hashes and Sets"
1. "Provide advanced patterns and performance considerations for Hashes and Sets"

## Key Takeaways

- Master the core ideas of Hashes and Sets through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
