---
{
  "title": "Inheritance",
  "description": "Subclassing, super, override, and ancestry.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Subclass and override methods",
    "Call parent code with super",
    "Extend parent behavior",
    "Inspect ancestry with ancestors"
  ],
  "knowledge_refs": [
    "ruby/ruby-11-inheritance"
  ],
  "prerequisites": [
    "RUBY-10"
  ],
  "references": [
    {
      "title": "Ruby — Inheritance",
      "url": "https://docs.ruby-lang.org/en/master/syntax/classes_and_modules_rdoc.html"
    },
    {
      "title": "Ruby — super",
      "url": "https://docs.ruby-lang.org/en/master/syntax/methods_rdoc.html"
    },
    {
      "title": "Ruby — Module#ancestors",
      "url": "https://docs.ruby-lang.org/en/master/Module.html#method-i-ancestors"
    }
  ]
}
---

# RUBY-11-INHERITANCE: Inheritance

## Introduction

Subclassing, super, override, and ancestry. By the end of this lesson you will be able to: Subclass and override methods; Call parent code with super; Extend parent behavior; Inspect ancestry with ancestors.

## Key Concepts

### 1. Subclass and override methods

Target: Subclass and override methods. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
class Animal
  def speak
    "..."
  end
end
class Dog < Animal
  def speak
    "Woof"
  end
end
p Dog.new.speak
```
### 2. Call parent code with super

Target: Call parent code with super. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
class Base
  def initialize(x)
    @x = x
  end
end
class Derived < Base
  def initialize(x, y)
    super(x)     # call parent
    @y = y
  end
  attr_reader :x, :y
end
d = Derived.new(1, 2)
p [d.x, d.y]
```
### 3. Extend parent behavior

Target: Extend parent behavior. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
class Animal
  def speak; "animal"; end
end
class Dog < Animal
  def speak
    super + " (dog)"
  end
end
p Dog.new.speak   # animal (dog)
```
### 4. Inspect ancestry with ancestors

Target: Inspect ancestry with ancestors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
# is_a? and ancestry
class Cat < Animal; end
c = Cat.new
p c.is_a?(Cat)
p c.is_a?(Animal)
p Cat.ancestors.first(4)
```

## Practice Questions

1. What is the key idea behind "Inheritance"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Inheritance with analogies and real-world examples"
1. "Show me common mistakes beginners make with Inheritance"
1. "Provide advanced patterns and performance considerations for Inheritance"

## Key Takeaways

- Master the core ideas of Inheritance through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
