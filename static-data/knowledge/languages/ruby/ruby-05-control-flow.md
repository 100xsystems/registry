---
{
  "title": "Control Flow",
  "description": "if/elsif/else, case/when, unless, and loops.",
  "type": "lesson",
  "order": 5,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write if/elsif/else branches",
    "Use case/when expressions",
    "Use unless and inline conditionals",
    "Iterate with times, upto, and while"
  ],
  "knowledge_refs": [
    "ruby/ruby-05-control-flow"
  ],
  "prerequisites": [
    "RUBY-04"
  ],
  "references": [
    {
      "title": "Ruby — Control Expressions",
      "url": "https://docs.ruby-lang.org/en/master/syntax/control_expressions_rdoc.html"
    },
    {
      "title": "Ruby — Case Expression",
      "url": "https://docs.ruby-lang.org/en/master/syntax/control_expressions_rdoc.html#label-case+Expression"
    },
    {
      "title": "Ruby — Loops",
      "url": "https://docs.ruby-lang.org/en/master/syntax/control_expressions_rdoc.html#label-Loop+Control"
    }
  ]
}
---

# RUBY-05-CONTROL-FLOW: Control Flow

## Introduction

if/elsif/else, case/when, unless, and loops. By the end of this lesson you will be able to: Write if/elsif/else branches; Use case/when expressions; Use unless and inline conditionals; Iterate with times, upto, and while.

## Key Concepts

### 1. Write if/elsif/else branches

Target: Write if/elsif/else branches. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
score = 85
if score >= 90
  puts "A"
elsif score >= 80
  puts "B"
else
  puts "C"
end
```
### 2. Use case/when expressions

Target: Use case/when expressions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
day = 3
case day
when 1 then puts "Monday"
when 2, 3 then puts "Weekday"
else puts "Other"
end
```
### 3. Use unless and inline conditionals

Target: Use unless and inline conditionals. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
# unless: the inverse of if
logged_in = false
puts "please log in" unless logged_in
puts "welcome" if logged_in
puts "error" unless 2 > 1
```
### 4. Iterate with times, upto, and while

Target: Iterate with times, upto, and while. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
3.times { |i| print i }       # 012
puts
1.upto(3) { |i| print i }     # 123
puts
(1..3).each { |i| print i }   # 123
puts
i = 0
while i < 2
  print i
  i += 1
end                          # 01
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
