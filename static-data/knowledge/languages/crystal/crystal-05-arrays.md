---
{
  "title": "Arrays and Tuples",
  "description": "Collections and tuple types.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create arrays",
    "Use array methods",
    "Index and slice",
    "Use tuples"
  ],
  "knowledge_refs": [
    "crystal/crystal-05-arrays"
  ],
  "prerequisites": [
    "Crystal-04: Strings and Interpolation"
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

# CRYSTAL-05-ARRAYS: Arrays and Tuples

## Introduction

Collections and tuple types. By the end of this lesson you will be able to: Create arrays; Use array methods; Index and slice; Use tuples.

## Key Concepts

### 1. Create arrays

Target: Create arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
nums = [1, 2, 3]
nums << 4
puts nums.sum
```
### 2. Use array methods

Target: Use array methods. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
arr = [1, 2, 3, 4]
puts arr.select { |n| n.even? }
```
### 3. Index and slice

Target: Index and slice. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
puts arr[0]
puts arr[1..2]
```
### 4. Use tuples

Target: Use tuples. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
t = {1, "two", 3.0}
puts t[1]
```

## Practice Questions

1. What is the key idea behind "Arrays and Tuples"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays and Tuples with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays and Tuples"
1. "Provide advanced patterns and performance considerations for Arrays and Tuples"

## Key Takeaways

- Master the core ideas of Arrays and Tuples through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
