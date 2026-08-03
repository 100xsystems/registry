---
{
  "title": "Fibers and Channels",
  "description": "Green threads and CSP.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Spawn fibers",
    "Use channels",
    "Coordinate with select",
    "Understand Crystal scheduling"
  ],
  "knowledge_refs": [
    "crystal/crystal-15-concurrency"
  ],
  "prerequisites": [
    "Crystal-14: Generics"
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

# CRYSTAL-15-CONCURRENCY: Fibers and Channels

## Introduction

Green threads and CSP. By the end of this lesson you will be able to: Spawn fibers; Use channels; Coordinate with select; Understand Crystal scheduling.

## Key Concepts

### 1. Spawn fibers

Target: Spawn fibers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
spawn do
  puts "in fiber"
end

Fiber.yield
puts "main"
```
### 2. Use channels

Target: Use channels. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
ch = Channel(Int32).new
spawn do
  ch.send(42)
end

puts ch.receive
```
### 3. Coordinate with select

Target: Coordinate with select. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
ch = Channel(Int32).new
10.times do |i|
  spawn { ch.send(i) }
end

10.times { puts ch.receive }
```
### 4. Understand Crystal scheduling

Target: Understand Crystal scheduling. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
select
when msg = ch1.receive
  puts "from ch1: #{msg}"
when msg = ch2.receive
  puts "from ch2: #{msg}"
end
```

## Practice Questions

1. What is the key idea behind "Fibers and Channels"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Fibers and Channels with analogies and real-world examples"
1. "Show me common mistakes beginners make with Fibers and Channels"
1. "Provide advanced patterns and performance considerations for Fibers and Channels"

## Key Takeaways

- Master the core ideas of Fibers and Channels through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
