---
{
  "title": "Exceptions and Error Handling",
  "description": "begin/rescue/ensure, custom exceptions, raise.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write begin/rescue/ensure blocks",
    "Rescue specific exception classes",
    "Define custom exception classes",
    "Use rescue clauses in methods"
  ],
  "knowledge_refs": [
    "ruby/ruby-14-exceptions"
  ],
  "prerequisites": [
    "RUBY-13"
  ],
  "references": [
    {
      "title": "Ruby — Exceptions",
      "url": "https://docs.ruby-lang.org/en/master/syntax/exceptions_rdoc.html"
    },
    {
      "title": "Ruby — Exception Class",
      "url": "https://docs.ruby-lang.org/en/master/Exception.html"
    },
    {
      "title": "Ruby — raise",
      "url": "https://docs.ruby-lang.org/en/master/Kernel.html#method-i-raise"
    }
  ]
}
---

# RUBY-14-EXCEPTIONS: Exceptions and Error Handling

## Introduction

begin/rescue/ensure, custom exceptions, raise. By the end of this lesson you will be able to: Write begin/rescue/ensure blocks; Rescue specific exception classes; Define custom exception classes; Use rescue clauses in methods.

## Key Concepts

### 1. Write begin/rescue/ensure blocks

Target: Write begin/rescue/ensure blocks. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
begin
  raise "custom failure"
rescue => e
  puts "caught: #{e.message}"
ensure
  puts "always runs"
end
```
### 2. Rescue specific exception classes

Target: Rescue specific exception classes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
begin
  1 / 0
rescue ZeroDivisionError => e
  puts "#{e.class}: #{e.message}"
end
```
### 3. Define custom exception classes

Target: Define custom exception classes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
class ValidationError < StandardError; end
def validate!(v)
  raise ValidationError, "bad value" if v.nil?
end
begin
  validate!(nil)
rescue ValidationError => e
  puts e.message
end
```
### 4. Use rescue clauses in methods

Target: Use rescue clauses in methods. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
def risky
  yield
rescue ArgumentError
  :argument
rescue StandardError
  :standard
end
p risky { raise ArgumentError }
p risky { raise "generic" }
```

## Practice Questions

1. What is the key idea behind "Exceptions and Error Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Exceptions and Error Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Exceptions and Error Handling"
1. "Provide advanced patterns and performance considerations for Exceptions and Error Handling"

## Key Takeaways

- Master the core ideas of Exceptions and Error Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
