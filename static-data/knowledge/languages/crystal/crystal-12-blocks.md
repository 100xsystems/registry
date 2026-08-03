---
{
  "title": "Blocks and Procs",
  "description": "Higher-order functions.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Pass blocks to methods",
    "Use yield",
    "Capture blocks as procs",
    "Build with blocks"
  ],
  "knowledge_refs": [
    "crystal/crystal-12-blocks"
  ],
  "prerequisites": [
    "Crystal-11: Exceptions"
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

# CRYSTAL-12-BLOCKS: Blocks and Procs

## Introduction

Higher-order functions. By the end of this lesson you will be able to: Pass blocks to methods; Use yield; Capture blocks as procs; Build with blocks.

## Key Concepts

### 1. Pass blocks to methods

Target: Pass blocks to methods. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
def repeat(n)
  n.times { yield }
end

repeat(3) { puts "hi" }
```
### 2. Use yield

Target: Use yield. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
def each_with_log(items)
  items.each do |item|
    puts "processing #{item}"
    yield item
  end
end
```
### 3. Capture blocks as procs

Target: Capture blocks as procs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
square = ->(x : Int32) { x * x }
puts square.call(5)
```
### 4. Build with blocks

Target: Build with blocks. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
def apply(items, &block : Int32 -> Int32)
  items.map { |i| block.call(i) }
end

puts apply([1, 2, 3]) { |i| i + 1 }
```

## Practice Questions

1. What is the key idea behind "Blocks and Procs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Blocks and Procs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Blocks and Procs"
1. "Provide advanced patterns and performance considerations for Blocks and Procs"

## Key Takeaways

- Master the core ideas of Blocks and Procs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
