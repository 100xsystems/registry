---
{
  "title": "Exceptions",
  "description": "Raise and rescue errors.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Raise exceptions",
    "Rescue errors",
    "Use ensure",
    "Create custom exceptions"
  ],
  "knowledge_refs": [
    "crystal/crystal-11-exceptions"
  ],
  "prerequisites": [
    "Crystal-10: Enums"
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

# CRYSTAL-11-EXCEPTIONS: Exceptions

## Introduction

Raise and rescue errors. By the end of this lesson you will be able to: Raise exceptions; Rescue errors; Use ensure; Create custom exceptions.

## Key Concepts

### 1. Raise exceptions

Target: Raise exceptions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
def check(n)
  raise "negative" if n < 0
end

begin
  check(-1)
rescue e
  puts e.message
end
```
### 2. Rescue errors

Target: Rescue errors. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
begin
  risky
rescue ArgumentError
  puts "bad arg"
rescue
  puts "other"
end
```
### 3. Use ensure

Target: Use ensure. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
begin
  work
ensure
  cleanup
end
```
### 4. Create custom exceptions

Target: Create custom exceptions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
class MyError < Exception
end

raise MyError.new("custom")
```

## Practice Questions

1. What is the key idea behind "Exceptions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Exceptions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Exceptions"
1. "Provide advanced patterns and performance considerations for Exceptions"

## Key Takeaways

- Master the core ideas of Exceptions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
