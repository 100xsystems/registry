---
{
  "title": "Enumerable Module",
  "description": "map, select, reduce, group_by, tally, and lazy chains.",
  "type": "lesson",
  "order": 13,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Transform with map and select",
    "Aggregate with reduce",
    "Group and tally data",
    "Build lazy enumerator chains"
  ],
  "knowledge_refs": [
    "ruby/ruby-13-enumerable"
  ],
  "prerequisites": [
    "RUBY-12"
  ],
  "references": [
    {
      "title": "Ruby — Enumerable",
      "url": "https://docs.ruby-lang.org/en/master/Enumerable.html"
    },
    {
      "title": "Ruby — Enumerator::Lazy",
      "url": "https://docs.ruby-lang.org/en/master/Enumerator/Lazy.html"
    },
    {
      "title": "Ruby — each_with_object",
      "url": "https://docs.ruby-lang.org/en/master/Enumerable.html#method-i-each_with_object"
    }
  ]
}
---

# RUBY-13-ENUMERABLE: Enumerable Module

## Introduction

map, select, reduce, group_by, tally, and lazy chains. By the end of this lesson you will be able to: Transform with map and select; Aggregate with reduce; Group and tally data; Build lazy enumerator chains.

## Key Concepts

### 1. Transform with map and select

Target: Transform with map and select. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
# Enumerable: the heart of Ruby collections
p (1..5).map { |x| x * x }       # [1, 4, 9, 16, 25]
p (1..10).select(&:even?)        # [2, 4, 6, 8, 10]
p (1..5).reduce(:+)               # 15
```
### 2. Aggregate with reduce

Target: Aggregate with reduce. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
words = %w[cat dog elephant]
p words.max_by(&:length)          # elephant
p words.sort_by(&:length)         # [cat, dog, elephant]
p words.group_by(&:length)        # {3=>[cat, dog], 8=>[elephant]}
```
### 3. Group and tally data

Target: Group and tally data. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
p [1, 2, 3, 2].tally               # {1=>1, 2=>2, 3=>1}
p (1..5).each_with_object([]) { |x, acc| acc << x * 2 }
p [1, 2, 3].partition(&:odd?)      # [[1, 3], [2]]
```
### 4. Build lazy enumerator chains

Target: Build lazy enumerator chains. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
# enumerators are lazy chains
e = (1..Float::INFINITY).lazy.select(&:even?).first(5)
p e   # [2, 4, 6, 8, 10]
p (1..5).to_enum(:each).next
```

## Practice Questions

1. What is the key idea behind "Enumerable Module"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Enumerable Module with analogies and real-world examples"
1. "Show me common mistakes beginners make with Enumerable Module"
1. "Provide advanced patterns and performance considerations for Enumerable Module"

## Key Takeaways

- Master the core ideas of Enumerable Module through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
