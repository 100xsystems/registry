---
{
  "title": "Strings and String Methods",
  "description": "String manipulation, interpolation, formatting, and mutation.",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use common string methods",
    "Interpolate and format strings",
    "Split, join, and replace text",
    "Understand mutability and freeze"
  ],
  "knowledge_refs": [
    "ruby/ruby-04-strings"
  ],
  "prerequisites": [
    "RUBY-03"
  ],
  "references": [
    {
      "title": "Ruby — String",
      "url": "https://docs.ruby-lang.org/en/master/String.html"
    },
    {
      "title": "Ruby — String Literals",
      "url": "https://docs.ruby-lang.org/en/master/syntax/literals_rdoc.html"
    },
    {
      "title": "Ruby — format/sprintf",
      "url": "https://docs.ruby-lang.org/en/master/Kernel.html#method-i-sprintf"
    }
  ]
}
---

# RUBY-04-STRINGS: Strings and String Methods

## Introduction

String manipulation, interpolation, formatting, and mutation. By the end of this lesson you will be able to: Use common string methods; Interpolate and format strings; Split, join, and replace text; Understand mutability and freeze.

## Key Concepts

### 1. Use common string methods

Target: Use common string methods. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
greeting = "hello"
p greeting.upcase       # HELLO
p greeting.capitalize   # Hello
p greeting.reverse      # olleh
p greeting.length       # 5
p greeting.include?("ell")  # true
```
### 2. Interpolate and format strings

Target: Interpolate and format strings. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
name = "World"
p "Hello, #{name}!"      # interpolation
p '#{name} not interpolated'
p format("%.2f", 3.14159)
```
### 3. Split, join, and replace text

Target: Split, join, and replace text. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
s = "a,b,c"
p s.split(",")          # ["a", "b", "c"]
p ["x", "y"].join("-")  # "x-y"
p "hello world".gsub("l", "L")  # heLLo worLd
```
### 4. Understand mutability and freeze

Target: Understand mutability and freeze. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
# mutable strings; freeze to protect
s = "abc"
s << "d"       # mutates
p s            # abcd
frozen = "abc".freeze
p frozen.frozen?  # true
```

## Practice Questions

1. What is the key idea behind "Strings and String Methods"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings and String Methods with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings and String Methods"
1. "Provide advanced patterns and performance considerations for Strings and String Methods"

## Key Takeaways

- Master the core ideas of Strings and String Methods through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
