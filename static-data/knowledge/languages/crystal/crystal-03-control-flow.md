---
{
  "title": "Control Flow",
  "description": "if, unless, case, and loops.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write if/elsif/else",
    "Use unless",
    "Use case/when",
    "Iterate with loops"
  ],
  "knowledge_refs": [
    "crystal/crystal-03-control-flow"
  ],
  "prerequisites": [
    "Crystal-02: Variables and Types"
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

# CRYSTAL-03-CONTROL-FLOW: Control Flow

## Introduction

if, unless, case, and loops. By the end of this lesson you will be able to: Write if/elsif/else; Use unless; Use case/when; Iterate with loops.

## Key Concepts

### 1. Write if/elsif/else

Target: Write if/elsif/else. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
score = 85
if score >= 90
  puts "A"
elsif score >= 80
  puts "B"
else
  puts "C"
end
```
### 2. Use unless

Target: Use unless. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
unless score < 60
  puts "passed"
end
```
### 3. Use case/when

Target: Use case/when. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
case score
when 90..100 then puts "A"
when 80...90 then puts "B"
else puts "C"
end
```
### 4. Iterate with loops

Target: Iterate with loops. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
3.times { puts "hi" }
(1..3).each { |i| puts i }
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
