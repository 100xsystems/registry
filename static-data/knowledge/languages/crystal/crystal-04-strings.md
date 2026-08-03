---
{
  "title": "Strings and Interpolation",
  "description": "String ops, interpolation, and heredocs.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Interpolate strings",
    "Concatenate and transform",
    "Use string methods",
    "Work with heredocs"
  ],
  "knowledge_refs": [
    "crystal/crystal-04-strings"
  ],
  "prerequisites": [
    "Crystal-03: Control Flow"
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

# CRYSTAL-04-STRINGS: Strings and Interpolation

## Introduction

String ops, interpolation, and heredocs. By the end of this lesson you will be able to: Interpolate strings; Concatenate and transform; Use string methods; Work with heredocs.

## Key Concepts

### 1. Interpolate strings

Target: Interpolate strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
name = "Ada"
puts "Hello, #{name}!"
```
### 2. Concatenate and transform

Target: Concatenate and transform. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
puts "hello".upcase
puts "  hi  ".strip
```
### 3. Use string methods

Target: Use string methods. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
puts "a,b,c".split(",").join(" | ")
```
### 4. Work with heredocs

Target: Work with heredocs. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
text = <<-EOF
  multi-line
  heredoc
EOF
puts text
```

## Practice Questions

1. What is the key idea behind "Strings and Interpolation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings and Interpolation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings and Interpolation"
1. "Provide advanced patterns and performance considerations for Strings and Interpolation"

## Key Takeaways

- Master the core ideas of Strings and Interpolation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
