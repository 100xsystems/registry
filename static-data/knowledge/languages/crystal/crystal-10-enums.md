---
{
  "title": "Enums",
  "description": "Typed enumerations.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define enums",
    "Use enum values",
    "Iterate enums",
    "Convert to strings"
  ],
  "knowledge_refs": [
    "crystal/crystal-10-enums"
  ],
  "prerequisites": [
    "Crystal-09: Modules and Mixins"
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

# CRYSTAL-10-ENUMS: Enums

## Introduction

Typed enumerations. By the end of this lesson you will be able to: Define enums; Use enum values; Iterate enums; Convert to strings.

## Key Concepts

### 1. Define enums

Target: Define enums. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
enum Color
  Red
  Green
  Blue
end

c = Color::Green
puts c
```
### 2. Use enum values

Target: Use enum values. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
enum Direction
  North
  East
  South
  West
end

Direction.each { |d| puts d }
```
### 3. Iterate enums

Target: Iterate enums. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
case Color::Red
when Color::Red   then puts "red"
when Color::Green then puts "green"
end
```
### 4. Convert to strings

Target: Convert to strings. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
puts Color::Blue.to_s
puts Color.parse("Red")
```

## Practice Questions

1. What is the key idea behind "Enums"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Enums with analogies and real-world examples"
1. "Show me common mistakes beginners make with Enums"
1. "Provide advanced patterns and performance considerations for Enums"

## Key Takeaways

- Master the core ideas of Enums through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
