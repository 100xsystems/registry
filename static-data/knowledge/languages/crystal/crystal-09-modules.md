---
{
  "title": "Modules and Mixins",
  "description": "Code reuse with modules.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define modules",
    "Include modules",
    "Extend modules",
    "Use namespaces"
  ],
  "knowledge_refs": [
    "crystal/crystal-09-modules"
  ],
  "prerequisites": [
    "Crystal-08: Classes"
  ],
  "references": [
    {
      "title": "Crystal Language Reference",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official docs"
    },
    {
      "title": "Crystal for Rubyists",
      "url": "https://crystal-lang.org/reference/guides/faq.html",
      "description": "Migration guide"
    },
    {
      "title": "Crystal Book",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official reference book"
    },
    {
      "title": "Crystal Forum",
      "url": "https://forum.crystal-lang.org/",
      "description": "Community"
    }
  ]
}
---

# CRYSTAL-09-MODULES: Modules and Mixins

## Introduction

Code reuse with modules. By the end of this lesson you will be able to: Define modules; Include modules; Extend modules; Use namespaces.

## Key Concepts

### 1. Define modules

Target: Define modules. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
module Greetings
  def hello
    "hello"
  end
end

class Person
  include Greetings
end

puts Person.new.hello
```
### 2. Include modules

Target: Include modules. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
module MathUtils
  def self.square(x)
    x * x
  end
end

puts MathUtils.square(4)
```
### 3. Extend modules

Target: Extend modules. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
module A
  def f
    "A"
  end
end

module B
  def f
    "B"
  end
end

class C
  include A
  include B
end
```
### 4. Use namespaces

Target: Use namespaces. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
module Geometry
  VERSION = "1.0"
end
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
