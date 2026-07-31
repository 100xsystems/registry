---
{
  "title": "Modules and Mixins",
  "description": "include, extend, prepend, and namespace modules.",
  "type": "lesson",
  "order": 10,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define and include modules",
    "Use extend for class methods",
    "Understand include vs prepend ordering",
    "Compose behavior with mixins"
  ],
  "knowledge_refs": [
    "ruby/ruby-10-modules"
  ],
  "prerequisites": [
    "RUBY-09"
  ],
  "references": [
    {
      "title": "Ruby — Modules",
      "url": "https://docs.ruby-lang.org/en/master/syntax/classes_and_modules_rdoc.html"
    },
    {
      "title": "Ruby — Module#include",
      "url": "https://docs.ruby-lang.org/en/master/Module.html#method-i-include"
    },
    {
      "title": "Ruby — Module#prepend",
      "url": "https://docs.ruby-lang.org/en/master/Module.html#method-i-prepend"
    }
  ]
}
---

# RUBY-10-MODULES: Modules and Mixins

## Introduction

include, extend, prepend, and namespace modules. By the end of this lesson you will be able to: Define and include modules; Use extend for class methods; Understand include vs prepend ordering; Compose behavior with mixins.

## Key Concepts

### 1. Define and include modules

Target: Define and include modules. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
module Greetable
  def greet
    "Hello from #{self.class}"
  end
end
class Person
  include Greetable
end
p Person.new.greet
```
### 2. Use extend for class methods

Target: Use extend for class methods. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
module Logger
  def log(msg)
    puts "[LOG] #{msg}"
  end
end
class Service
  extend Logger   # class-level methods
end
Service.log("started")
```
### 3. Understand include vs prepend ordering

Target: Understand include vs prepend ordering. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
module M1
  def who; "M1"; end
end
module M2
  def who; "M2"; end
end
class Both
  include M1
  include M2   # later include wins
end
p Both.new.who
```
### 4. Compose behavior with mixins

Target: Compose behavior with mixins. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
# prepend vs include (prepend is consulted first)
module Wrap
  def greet
    "wrapped: " + super
  end
end
class Greeter
  prepend Wrap
  def greet; "hi"; end
end
p Greeter.new.greet   # wrapped: hi
```

## Practice Questions

1. What is the key idea behind "Modules and Mixins"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Modules and Mixins with analogies and real-world examples"
1. "Show me common mistakes beginners make with Modules and Mixins"
1. "Provide advanced patterns and performance considerations for Modules and Mixins"

## Key Takeaways

- Master the core ideas of Modules and Mixins through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
