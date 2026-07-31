---
{
  "title": "Arrays",
  "description": "Indexing, slicing, sorting, and Enumerable-powered transformation.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Index and slice arrays",
    "Sort and search arrays",
    "Transform with map, select, reject",
    "Use nested and unique arrays"
  ],
  "knowledge_refs": [
    "ruby/ruby-06-arrays"
  ],
  "prerequisites": [
    "RUBY-05"
  ],
  "references": [
    {
      "title": "Ruby — Array",
      "url": "https://docs.ruby-lang.org/en/master/Array.html"
    },
    {
      "title": "Ruby — Enumerable",
      "url": "https://docs.ruby-lang.org/en/master/Enumerable.html"
    },
    {
      "title": "Ruby — Array Literals",
      "url": "https://docs.ruby-lang.org/en/master/syntax/literals_rdoc.html"
    }
  ]
}
---

# RUBY-06-ARRAYS: Arrays

## Introduction

Indexing, slicing, sorting, and Enumerable-powered transformation. By the end of this lesson you will be able to: Index and slice arrays; Sort and search arrays; Transform with map, select, reject; Use nested and unique arrays.

## Key Concepts

### 1. Index and slice arrays

Target: Index and slice arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
arr = [1, 2, 3]
p arr[0]          # 1
p arr[-1]         # 3 (from end)
p arr[0, 2]       # [1, 2] (slice)
p arr[1..2]       # [2, 3]
arr << 4          # append
p arr             # [1, 2, 3, 4]
```
### 2. Sort and search arrays

Target: Sort and search arrays. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
arr = [5, 2, 8, 1]
p arr.sort        # [1, 2, 5, 8]
p arr.sort.reverse
p arr.max, arr.min, arr.sum
p arr.first(2), arr.last(2)
```
### 3. Transform with map, select, reject

Target: Transform with map, select, reject. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
arr = [1, 2, 3, 4]
p arr.select { |x| x.even? }   # [2, 4]
p arr.reject { |x| x.even? }   # [1, 3]
p arr.map { |x| x * 2 }        # [2, 4, 6, 8]
p arr.any?(&:even?)            # true
```
### 4. Use nested and unique arrays

Target: Use nested and unique arrays. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
# multidimensional and uniq
grid = [[1, 2], [3, 4]]
p grid[1][0]      # 3
p [1, 1, 2].uniq  # [1, 2]
p [1, 2, 3].include?(2)  # true
```

## Practice Questions

1. What is the key idea behind "Arrays"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays"
1. "Provide advanced patterns and performance considerations for Arrays"

## Key Takeaways

- Master the core ideas of Arrays through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
