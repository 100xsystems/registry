---
{
  "title": "Variables and Data Types",
  "description": "Local/instance/class/global variables, dynamic typing, symbols.",
  "type": "lesson",
  "order": 2,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use the main object types and their classes",
    "Understand variable scope types",
    "Leverage dynamic typing",
    "Use symbols as lightweight identifiers"
  ],
  "knowledge_refs": [
    "ruby/ruby-02-variables-types"
  ],
  "prerequisites": [
    "RUBY-01"
  ],
  "references": [
    {
      "title": "Ruby — Variables",
      "url": "https://docs.ruby-lang.org/en/master/syntax/assignment_rdoc.html"
    },
    {
      "title": "Ruby — Symbols",
      "url": "https://docs.ruby-lang.org/en/master/Symbol.html"
    },
    {
      "title": "Ruby — Literals",
      "url": "https://docs.ruby-lang.org/en/master/syntax/literals_rdoc.html"
    }
  ]
}
---

# RUBY-02-VARIABLES-TYPES: Variables and Data Types

## Introduction

Local/instance/class/global variables, dynamic typing, symbols. By the end of this lesson you will be able to: Use the main object types and their classes; Understand variable scope types; Leverage dynamic typing; Use symbols as lightweight identifiers.

## Key Concepts

### 1. Use the main object types and their classes

Target: Use the main object types and their classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
x = 42
y = 3.14
name = "Alice"
flag = true
nothing = nil
p x.class, y.class, name.class, flag.class, nothing.class
```
### 2. Understand variable scope types

Target: Understand variable scope types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
# scope types: local, instance, class, global
class Demo
  @iv = 1          # instance variable
  @@cv = 2         # class variable
  $gv = 3          # global variable
  def show
    lv = 4         # local variable
    [@iv, @@cv, $gv, lv]
  end
end
p Demo.new.show
```
### 3. Leverage dynamic typing

Target: Leverage dynamic typing. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
# dynamic typing: same variable, different types
v = 42
v = "hello"
v = [1, 2, 3]
p v
```
### 4. Use symbols as lightweight identifiers

Target: Use symbols as lightweight identifiers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
# symbols are immutable, interned identifiers
:name.object_id == :name.object_id   # => true
p :name.class
p "name".to_sym
```

## Practice Questions

1. What is the key idea behind "Variables and Data Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Data Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Data Types"
1. "Provide advanced patterns and performance considerations for Variables and Data Types"

## Key Takeaways

- Master the core ideas of Variables and Data Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
