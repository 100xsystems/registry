---
{
  "title": "Classes and Objects",
  "description": "Class definitions, initialize, attr_*, self, to_s.",
  "type": "lesson",
  "order": 9,
  "duration": "75 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define classes with initialize",
    "Use attr_reader/writer/accessor",
    "Use class variables and methods",
    "Override to_s and inspect"
  ],
  "knowledge_refs": [
    "ruby/ruby-09-classes"
  ],
  "prerequisites": [
    "RUBY-08"
  ],
  "references": [
    {
      "title": "Ruby — Classes",
      "url": "https://docs.ruby-lang.org/en/master/syntax/classes_and_modules_rdoc.html"
    },
    {
      "title": "Ruby — attr_accessor",
      "url": "https://docs.ruby-lang.org/en/master/Module.html#method-i-attr_accessor"
    },
    {
      "title": "Ruby — Object Basics",
      "url": "https://docs.ruby-lang.org/en/master/Object.html"
    }
  ]
}
---

# RUBY-09-CLASSES: Classes and Objects

## Introduction

Class definitions, initialize, attr_*, self, to_s. By the end of this lesson you will be able to: Define classes with initialize; Use attr_reader/writer/accessor; Use class variables and methods; Override to_s and inspect.

## Key Concepts

### 1. Define classes with initialize

Target: Define classes with initialize. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
class Dog
  def speak
    "Woof"
  end
end
p Dog.new.speak
```
### 2. Use attr_reader/writer/accessor

Target: Use attr_reader/writer/accessor. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
class Person
  def initialize(name)
    @name = name
  end
  attr_reader :name
  attr_writer :name
  attr_accessor :age
end
p = Person.new("Alice")
p p.name
p.name = "Bob"
p p.name
```
### 3. Use class variables and methods

Target: Use class variables and methods. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
class Counter
  @@count = 0
  def initialize
    @@count += 1
  end
  def self.count
    @@count
  end
end
Counter.new; Counter.new
p Counter.count   # 2
```
### 4. Override to_s and inspect

Target: Override to_s and inspect. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
# to_s and inspect
class Point
  def initialize(x, y)
    @x, @y = x, y
  end
  def to_s
    "(#{@x}, #{@y})"
  end
end
puts Point.new(3, 4)   # (3, 4)
```

## Practice Questions

1. What is the key idea behind "Classes and Objects"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Classes and Objects with analogies and real-world examples"
1. "Show me common mistakes beginners make with Classes and Objects"
1. "Provide advanced patterns and performance considerations for Classes and Objects"

## Key Takeaways

- Master the core ideas of Classes and Objects through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
