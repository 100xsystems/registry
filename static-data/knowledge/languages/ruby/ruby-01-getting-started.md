---
{
  "title": "Getting Started with Ruby",
  "description": "Install Ruby, run scripts, I/O basics, and understand the interpreter.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install Ruby and run your first script",
    "Use puts, print, p, and pp for output",
    "Read input with gets and handle ARGV",
    "Understand Ruby version and runtime"
  ],
  "knowledge_refs": [
    "ruby/ruby-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Ruby Documentation Home",
      "url": "https://www.ruby-lang.org/en/documentation/"
    },
    {
      "title": "Ruby in Twenty Minutes",
      "url": "https://www.ruby-lang.org/en/documentation/quickstart/"
    },
    {
      "title": "ruby-doc.org",
      "url": "https://ruby-doc.org/core-3.2.0/"
    }
  ]
}
---

# RUBY-01-GETTING-STARTED: Getting Started with Ruby

## Introduction

Install Ruby, run scripts, I/O basics, and understand the interpreter. By the end of this lesson you will be able to: Install Ruby and run your first script; Use puts, print, p, and pp for output; Read input with gets and handle ARGV; Understand Ruby version and runtime.

## Key Concepts

### 1. Install Ruby and run your first script

Target: Install Ruby and run your first script. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
puts "Hello, 100X Systems!"
# run: ruby hello.rb
```
### 2. Use puts, print, p, and pp for output

Target: Use puts, print, p, and pp for output. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
print "no newline "
p [1, 2, 3]      # inspect form
pp({a: 1})       # pretty print
```
### 3. Read input with gets and handle ARGV

Target: Read input with gets and handle ARGV. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
puts "What is your name?"
name = gets.chomp
puts "Hello, #{name}!"
ARGV.each { |a| puts "arg: #{a}" }
```
### 4. Understand Ruby version and runtime

Target: Understand Ruby version and runtime. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
p RUBY_VERSION
p RUBY_ENGINE
p $0            # script name
p __FILE__
p __LINE__
```

## Practice Questions

1. What is the key idea behind "Getting Started with Ruby"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Ruby with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Ruby"
1. "Provide advanced patterns and performance considerations for Getting Started with Ruby"

## Key Takeaways

- Master the core ideas of Getting Started with Ruby through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
