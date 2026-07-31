---
{
  "title": "Numbers and Arithmetic",
  "description": "Integer/Float semantics, operators, precision, and big numbers.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Perform arithmetic with integers and floats",
    "Understand division semantics",
    "Use numeric literals and rounding",
    "Work with arbitrary-precision numbers"
  ],
  "knowledge_refs": [
    "ruby/ruby-03-numbers"
  ],
  "prerequisites": [
    "RUBY-02"
  ],
  "references": [
    {
      "title": "Ruby — Integer",
      "url": "https://docs.ruby-lang.org/en/master/Integer.html"
    },
    {
      "title": "Ruby — Float",
      "url": "https://docs.ruby-lang.org/en/master/Float.html"
    },
    {
      "title": "Ruby — BigDecimal",
      "url": "https://docs.ruby-lang.org/en/master/BigDecimal.html"
    }
  ]
}
---

# RUBY-03-NUMBERS: Numbers and Arithmetic

## Introduction

Integer/Float semantics, operators, precision, and big numbers. By the end of this lesson you will be able to: Perform arithmetic with integers and floats; Understand division semantics; Use numeric literals and rounding; Work with arbitrary-precision numbers.

## Key Concepts

### 1. Perform arithmetic with integers and floats

Target: Perform arithmetic with integers and floats. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
a = 17
b = 5
p a + b, a - b, a * b, a / b, a % b   # 22 12 85 3 2
p 17.0 / 5.0                          # 3.4 (float division)
```
### 2. Understand division semantics

Target: Understand division semantics. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
p 2 ** 10        # 1024 (power)
p 7 / 2          # 3 (integer division)
p 7.0 / 2        # 3.5
p -7 / 2         # -4 (Ruby floors)
```
### 3. Use numeric literals and rounding

Target: Use numeric literals and rounding. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
p 1_000_000      # readability underscores
p 0xFF           # 255 hex
p 0b1010         # 10 binary
p 3.14.round(1)  # 3.1
p 3.7.floor, 3.2.ceil, -3.14.abs
```
### 4. Work with arbitrary-precision numbers

Target: Work with arbitrary-precision numbers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
# arbitrary-precision integers
p 2 ** 100
p 10.class.ancestors.first(3)
require "bigdecimal"
p BigDecimal("0.1") + BigDecimal("0.2")
```

## Practice Questions

1. What is the key idea behind "Numbers and Arithmetic"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Numbers and Arithmetic with analogies and real-world examples"
1. "Show me common mistakes beginners make with Numbers and Arithmetic"
1. "Provide advanced patterns and performance considerations for Numbers and Arithmetic"

## Key Takeaways

- Master the core ideas of Numbers and Arithmetic through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
