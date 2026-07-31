---
{
  "title": "Hashes and Symbols",
  "description": "Hash construction, symbol keys, iteration, and transformation.",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Build and index hashes",
    "Use symbol keys with modern syntax",
    "Iterate and transform hashes",
    "Merge and fetch with defaults"
  ],
  "knowledge_refs": [
    "ruby/ruby-07-hashes"
  ],
  "prerequisites": [
    "RUBY-06"
  ],
  "references": [
    {
      "title": "Ruby — Hash",
      "url": "https://docs.ruby-lang.org/en/master/Hash.html"
    },
    {
      "title": "Ruby — Hash Literals",
      "url": "https://docs.ruby-lang.org/en/master/syntax/literals_rdoc.html"
    },
    {
      "title": "Ruby — Symbol",
      "url": "https://docs.ruby-lang.org/en/master/Symbol.html"
    }
  ]
}
---

# RUBY-07-HASHES: Hashes and Symbols

## Introduction

Hash construction, symbol keys, iteration, and transformation. By the end of this lesson you will be able to: Build and index hashes; Use symbol keys with modern syntax; Iterate and transform hashes; Merge and fetch with defaults.

## Key Concepts

### 1. Build and index hashes

Target: Build and index hashes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
h = { "name" => "Alice", "age" => 30 }
p h["name"]       # "Alice"
h["city"] = "NYC"
p h               # 3 keys
```
### 2. Use symbol keys with modern syntax

Target: Use symbol keys with modern syntax. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
# symbol keys + modern syntax
h = { name: "Alice", age: 30 }
p h[:name]
p h.key?(:age)    # true
p h.keys, h.values
h.each { |k, v| puts "#{k}=#{v}" }
```
### 3. Iterate and transform hashes

Target: Iterate and transform hashes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
h = { a: 1, b: 2, c: 3 }
p h.select { |_, v| v > 1 }    # {b: 2, c: 3}
p h.map { |k, v| "#{k}#{v}" }
p h.transform_values { |v| v * 10 }
```
### 4. Merge and fetch with defaults

Target: Merge and fetch with defaults. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
p ({a: 1}.merge(b: 2))    # {a: 1, b: 2}
p ({a: 1}.key?(:x))       # false
p ({a: 1}.fetch(:x, 0))   # 0 (default)
```

## Practice Questions

1. What is the key idea behind "Hashes and Symbols"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Hashes and Symbols with analogies and real-world examples"
1. "Show me common mistakes beginners make with Hashes and Symbols"
1. "Provide advanced patterns and performance considerations for Hashes and Symbols"

## Key Takeaways

- Master the core ideas of Hashes and Symbols through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
