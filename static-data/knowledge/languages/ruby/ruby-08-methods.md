---
{
  "title": "Methods and Arguments",
  "description": "Method definitions, implicit returns, splat, keyword args, blocks.",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define methods with implicit returns",
    "Use splat (*) for variable arguments",
    "Use keyword and default arguments",
    "Accept blocks with &block"
  ],
  "knowledge_refs": [
    "ruby/ruby-08-methods"
  ],
  "prerequisites": [
    "RUBY-07"
  ],
  "references": [
    {
      "title": "Ruby — Methods",
      "url": "https://docs.ruby-lang.org/en/master/syntax/methods_rdoc.html"
    },
    {
      "title": "Ruby — Method Arguments",
      "url": "https://docs.ruby-lang.org/en/master/syntax/methods_rdoc.html"
    },
    {
      "title": "Ruby — Method Calling",
      "url": "https://docs.ruby-lang.org/en/master/syntax/calling_methods_rdoc.html"
    }
  ]
}
---

# RUBY-08-METHODS: Methods and Arguments

## Introduction

Method definitions, implicit returns, splat, keyword args, blocks. By the end of this lesson you will be able to: Define methods with implicit returns; Use splat (*) for variable arguments; Use keyword and default arguments; Accept blocks with &block.

## Key Concepts

### 1. Define methods with implicit returns

Target: Define methods with implicit returns. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
def greet(name)
  "Hello, #{name}!"
end
p greet("Alice")
```
### 2. Use splat (*) for variable arguments

Target: Use splat (*) for variable arguments. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
def sum(a, b)
  a + b
end
# implicit return: last expression
p sum(2, 3)   # 5
p (sum 2, 3)  # 5 (parens optional)
```
### 3. Use keyword and default arguments

Target: Use keyword and default arguments. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
# splat and keyword args
def log(*messages)
  messages
end
def config(name:, port: 80)
  [name, port]
end
p log(1, 2, 3)
p config(name: "web")
p config(name: "api", port: 3000)
```
### 4. Accept blocks with &block

Target: Accept blocks with &block. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
# default args + block param
def repeat(msg, times = 2)
  times.times { print msg }
end
def with_block(&blk)
  blk.call("inside")
end
repeat("hi ", 3)
puts
with_block { |s| puts s }
```

## Practice Questions

1. What is the key idea behind "Methods and Arguments"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Methods and Arguments with analogies and real-world examples"
1. "Show me common mistakes beginners make with Methods and Arguments"
1. "Provide advanced patterns and performance considerations for Methods and Arguments"

## Key Takeaways

- Master the core ideas of Methods and Arguments through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
