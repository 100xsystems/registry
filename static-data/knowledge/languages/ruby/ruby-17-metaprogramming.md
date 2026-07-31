---
{
  "title": "Metaprogramming",
  "description": "define_method, method_missing, send, instance_eval.",
  "type": "lesson",
  "order": 17,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define methods dynamically",
    "Handle missing methods",
    "Dispatch dynamically with send",
    "Evaluate code in object context"
  ],
  "knowledge_refs": [
    "ruby/ruby-17-metaprogramming"
  ],
  "prerequisites": [
    "RUBY-16"
  ],
  "references": [
    {
      "title": "Ruby — define_method",
      "url": "https://docs.ruby-lang.org/en/master/Module.html#method-i-define_method"
    },
    {
      "title": "Ruby — method_missing",
      "url": "https://docs.ruby-lang.org/en/master/BasicObject.html#method-i-method_missing"
    },
    {
      "title": "Ruby — send",
      "url": "https://docs.ruby-lang.org/en/master/Object.html#method-i-send"
    }
  ]
}
---

# RUBY-17-METAPROGRAMMING: Metaprogramming

## Introduction

define_method, method_missing, send, instance_eval. By the end of this lesson you will be able to: Define methods dynamically; Handle missing methods; Dispatch dynamically with send; Evaluate code in object context.

## Key Concepts

### 1. Define methods dynamically

Target: Define methods dynamically. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
# metaprogramming: define methods dynamically
class Calculator
  %i[add sub mul].each do |op|
    define_method(op) do |a, b|
      a.public_send(op == :mul ? :* : (op == :add ? :+ : :-), b)
    end
  end
end
c = Calculator.new
p c.add(2, 3)   # 5
```
### 2. Handle missing methods

Target: Handle missing methods. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
class Ghost
  def method_missing(name, *args)
    "#{name} called with #{args.inspect}"
  end
  def respond_to_missing?(name, include_private = false)
    true
  end
end
p Ghost.new.any_method(1, 2)
```
### 3. Dispatch dynamically with send

Target: Dispatch dynamically with send. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
# send: dynamic dispatch
class Greeter
  def hello; "hi"; end
  def goodbye; "bye"; end
end
g = Greeter.new
p g.send(:hello)
p g.public_send(:goodbye)
```
### 4. Evaluate code in object context

Target: Evaluate code in object context. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
# instance_eval: execute in object context
class Config
  def initialize; @values = {}; end
end
c = Config.new
c.instance_eval { @values[:timeout] = 30 }
p c.instance_variable_get(:@values)
```

## Practice Questions

1. What is the key idea behind "Metaprogramming"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Metaprogramming with analogies and real-world examples"
1. "Show me common mistakes beginners make with Metaprogramming"
1. "Provide advanced patterns and performance considerations for Metaprogramming"

## Key Takeaways

- Master the core ideas of Metaprogramming through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
