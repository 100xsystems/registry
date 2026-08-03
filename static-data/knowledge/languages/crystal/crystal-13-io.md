---
{
  "title": "File and Standard IO",
  "description": "Read and write files.",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read files",
    "Write files",
    "Read stdin",
    "Handle paths"
  ],
  "knowledge_refs": [
    "crystal/crystal-13-io"
  ],
  "prerequisites": [
    "Crystal-12: Blocks and Procs"
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

# CRYSTAL-13-IO: File and Standard IO

## Introduction

Read and write files. By the end of this lesson you will be able to: Read files; Write files; Read stdin; Handle paths.

## Key Concepts

### 1. Read files

Target: Read files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
puts File.read("data.txt")
```
### 2. Write files

Target: Write files. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
File.write("out.txt", "hello")
```
### 3. Read stdin

Target: Read stdin. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
input = gets
puts "You said: #{input}"
```
### 4. Handle paths

Target: Handle paths. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
File.open("log.txt", "a") do |f|
  f.puts "new line"
end
```

## Practice Questions

1. What is the key idea behind "File and Standard IO"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File and Standard IO with analogies and real-world examples"
1. "Show me common mistakes beginners make with File and Standard IO"
1. "Provide advanced patterns and performance considerations for File and Standard IO"

## Key Takeaways

- Master the core ideas of File and Standard IO through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
