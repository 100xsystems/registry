---
{
  "title": "Advanced: Pattern Matching and Refinements",
  "description": "Case/in patterns, guards, and refinements.",
  "type": "lesson",
  "order": 21,
  "duration": "75 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Use hash and array patterns",
    "Destructure with in",
    "Guard patterns with if conditions",
    "Scope changes with refinements"
  ],
  "knowledge_refs": [
    "ruby/ruby-21-advanced"
  ],
  "prerequisites": [
    "RUBY-20"
  ],
  "references": [
    {
      "title": "Ruby — Pattern Matching",
      "url": "https://docs.ruby-lang.org/en/master/syntax/pattern_matching_rdoc.html"
    },
    {
      "title": "Ruby — Refinements",
      "url": "https://docs.ruby-lang.org/en/master/syntax/refinements_rdoc.html"
    },
    {
      "title": "Ruby — Case/In",
      "url": "https://docs.ruby-lang.org/en/master/syntax/control_expressions_rdoc.html"
    }
  ]
}
---

# RUBY-21-ADVANCED: Advanced: Pattern Matching and Refinements

## Introduction

Case/in patterns, guards, and refinements. By the end of this lesson you will be able to: Use hash and array patterns; Destructure with in; Guard patterns with if conditions; Scope changes with refinements.

## Key Concepts

### 1. Use hash and array patterns

Target: Use hash and array patterns. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
# pattern matching (Ruby 2.7+/3.x)
case { name: "Alice", age: 30 }
in { name:, age: }
  puts "name=#{name} age=#{age}"
else
  puts "no match"
end
```
### 2. Destructure with in

Target: Destructure with in. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
case [1, 2, 3]
in [first, *rest]
  p [first, rest]   # [1, [2, 3]]
end
```
### 3. Guard patterns with if conditions

Target: Guard patterns with if conditions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
value = 42
case value
in Integer => n if n > 40
  puts "big int #{n}"
in String
  puts "string"
end
```
### 4. Scope changes with refinements

Target: Scope changes with refinements. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
# refinements: scoped monkey-patching
module UppercaseRefinement
  refine String do
    def shout; upcase + "!"; end
  end
end
using UppercaseRefinement
p "hello".shout   # HELLO!
```

## Practice Questions

1. What is the key idea behind "Advanced: Pattern Matching and Refinements"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced: Pattern Matching and Refinements with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced: Pattern Matching and Refinements"
1. "Provide advanced patterns and performance considerations for Advanced: Pattern Matching and Refinements"

## Key Takeaways

- Master the core ideas of Advanced: Pattern Matching and Refinements through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
